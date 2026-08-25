#!/usr/bin/env python3
"""Run deterministic structural checks for the PureLand repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git"}
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
PLACEHOLDER = re.compile(r"\b(TODO|TBD|INSERT[_ -]?HERE)\b", re.IGNORECASE)
METHOD_COMPLETION = re.compile(r"\bmethod completion\b", re.IGNORECASE)
FIELD_TEST_SCHEMA = ROOT / "data" / "field-test.schema.json"
FIELD_TEST_DIR = ROOT / "data" / "field-tests"
FT001 = FIELD_TEST_DIR / "ft-001-alchemy.json"

REQUIRED_ARCHITECTURE = [
    "LICENSE",
    "README.md",
    "THESIS.md",
    "METHOD.md",
    "TOOLBOX.md",
    "HYPOTHESIS.md",
    "TESTING.md",
    "CURRENT-EVIDENCE.md",
    "RESEARCH-STATUS.md",
    "FIELD-TESTING.md",
    "FIELD-TRIALS.md",
    "data/README.md",
    "data/field-test.schema.json",
    "templates/field-test.md",
    "research/field-tests/ft-001-alchemy.md",
]

REQUIRED_FT001_PATHS = [
    ("record_id",),
    ("kit_version",),
    ("test_status",),
    ("tested_hypothesis", "statement"),
    ("scope", "instrument"),
    ("walking_person", "status"),
    ("affected_people",),
    ("assessor", "relationship_to_practice"),
    ("second_reader", "status"),
    ("second_reader", "independent"),
    ("practice", "unit"),
    ("practice", "boundary"),
    ("practice", "boundary_rationale"),
    ("practice", "alternative_boundary"),
    ("document_access_set", "items"),
    ("document_access_set", "denominator"),
    ("document_access_set", "exclusions"),
    ("document_access_set", "time_window"),
    ("evidence_available_before_analysis",),
    ("disconfirming_condition", "statement"),
    ("station_completion", "observe", "status"),
    ("human_observe", "status"),
    ("access_readings", "understandable"),
    ("access_readings", "reachable"),
    ("access_readings", "adaptable"),
    ("access_readings", "traceable"),
    ("reciprocity_readings", "consent"),
    ("reciprocity_readings", "attribution"),
    ("reciprocity_readings", "meaningful_return"),
    ("agency_actions",),
    ("agency_actions", 0, "baseline"),
    ("agency_actions", 0, "follow_up"),
    ("party_impacts",),
    ("materiality_rule", "predeclared_before_analysis"),
    ("disagreements", "status"),
    ("participant_objections", "status"),
    ("rights_review", "status"),
    ("contestability", "route_status"),
    ("contestability", "takedown_route"),
    ("withdrawal", "status"),
    ("adaptation", "status"),
    ("adaptation", "intended_benefit"),
    ("adaptation", "possible_new_harm"),
    ("follow_up", "observation_window"),
    ("follow_up", "review_date"),
    ("follow_up", "status"),
    ("outcome", "classification"),
    ("outcome", "return_disposition"),
    ("outcome", "causal_claim"),
    ("ai_assistance", "used"),
    ("public_safe_review", "artifact_version"),
    ("public_safe_review", "decision"),
    ("public_safe_review", "categories", "artifact_specific_permission", "status"),
]


def files(suffix: str) -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob(f"*{suffix}")
        if not any(part in IGNORED for part in path.parts)
    )


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def load_json(path: Path, errors: list[str]) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid JSON: {relative(path)}: {exc}")
        return None


def has_path(value: Any, path: tuple[str | int, ...]) -> bool:
    current = value
    for part in path:
        if isinstance(part, int):
            if not isinstance(current, list) or part >= len(current):
                return False
            current = current[part]
        else:
            if not isinstance(current, dict) or part not in current:
                return False
            current = current[part]
    return True


def find_prohibited_score_keys(value: Any, prefix: str = "") -> list[str]:
    prohibited = {"average_score", "composite_score", "overall_score"}
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            location = f"{prefix}.{key}" if prefix else key
            if key.lower() in prohibited:
                found.append(location)
            found.extend(find_prohibited_score_keys(child, location))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(find_prohibited_score_keys(child, f"{prefix}[{index}]"))
    return found


def incomplete_required_stations(record: dict[str, Any]) -> list[str]:
    incomplete: list[str] = []
    for station, entry in record.get("station_completion", {}).items():
        if entry.get("required") is True and entry.get("status") != "complete":
            incomplete.append(station)
    return incomplete


def has_observed_action_outcome(record: dict[str, Any]) -> bool:
    for action in record.get("agency_actions", []):
        if (
            action.get("predefined_before_analysis") is True
            and action.get("baseline", {}).get("status") == "observed"
            and action.get("follow_up", {}).get("status") == "observed"
        ):
            return True
    return False


def has_material_increase(record: dict[str, Any]) -> bool:
    for impact in record.get("party_impacts", []):
        for period in ("baseline", "follow_up"):
            for dimension in ("exposure", "extractability", "shifted_burden"):
                if impact.get(period, {}).get(dimension, {}).get("material_increase") is True:
                    return True
    return False


def check_markdown(errors: list[str]) -> None:
    for path in files(".md"):
        text = path.read_text(encoding="utf-8")
        for target in LINK.findall(text):
            clean = target.split("#", 1)[0]
            if not clean or clean.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / clean).resolve()
            if ROOT not in resolved.parents and resolved != ROOT:
                errors.append(f"link escapes repository: {relative(path)} -> {target}")
            elif not resolved.exists():
                errors.append(f"broken local link: {relative(path)} -> {target}")
        if PLACEHOLDER.search(text):
            errors.append(f"placeholder token: {relative(path)}")


def check_record_rules(path: Path, record: dict[str, Any], errors: list[str]) -> None:
    record_label = record.get("record_id", relative(path))
    incomplete = incomplete_required_stations(record)

    if record.get("test_status") == "complete" and incomplete:
        errors.append(
            f"{record_label} claims completion with incomplete required stations: {', '.join(incomplete)}"
        )
    if (
        record.get("test_status") == "complete"
        and record.get("station_completion", {}).get("observe", {}).get("required") is True
        and record.get("human_observe", {}).get("status") != "performed"
    ):
        errors.append(f"{record_label} claims completion without required human Observe evidence")
    if record.get("test_status") == "complete":
        if not any(
            action.get("predefined_before_analysis") is True
            for action in record.get("agency_actions", [])
        ):
            errors.append(f"{record_label} claims completion without a predefined agency action")
        if record.get("materiality_rule", {}).get("predeclared_before_analysis") is not True:
            errors.append(f"{record_label} claims completion without a predeclared materiality rule")
        if record.get("rights_review", {}).get("status") != "complete":
            errors.append(f"{record_label} claims completion without a completed rights review")
        if (
            record.get("contestability", {}).get("route_status") != "usable"
            or record.get("contestability", {}).get("affected_party_tested") is not True
        ):
            errors.append(
                f"{record_label} claims completion without tested, usable contestability"
            )

    if incomplete:
        record_id = str(record.get("record_id", "")).lower()
        for markdown in files(".md"):
            text = markdown.read_text(encoding="utf-8")
            if record_id and record_id in text.lower() and METHOD_COMPLETION.search(text):
                errors.append(
                    f"prohibited completion wording for incomplete {record_label}: {relative(markdown)}"
                )

    outcome = record.get("outcome", {}).get("classification")
    rights_status = record.get("rights_review", {}).get("status")
    if (rights_status != "complete" or not has_observed_action_outcome(record)) and outcome != "unmeasurable":
        errors.append(
            f"{record_label} must be unmeasurable when required rights or action-outcome evidence is missing"
        )
    if (
        record.get("materiality_rule", {}).get("predeclared_before_analysis") is not True
        and outcome != "unmeasurable"
    ):
        errors.append(f"{record_label} must be unmeasurable without a predeclared materiality rule")
    if has_material_increase(record) and outcome == "supports-tested-context":
        errors.append(f"{record_label} cannot support the hypothesis with a recorded material increase")
    if outcome == "supports-tested-context" and (
        record.get("contestability", {}).get("route_status") != "usable"
        or record.get("contestability", {}).get("affected_party_tested") is not True
    ):
        errors.append(f"{record_label} cannot support the hypothesis without tested, usable contestability")

    rights_review = record.get("rights_review", {})
    allowed_public_permissions = {"granted", "not-required"}
    public_safe_review = record.get("public_safe_review", {})
    public_safe_categories = public_safe_review.get("categories", {})
    if public_safe_review.get("decision") != "clear":
        errors.append(f"{record_label} public record lacks a clear artifact-version public-safe decision")
    unclear_categories = sorted(
        name
        for name, category in public_safe_categories.items()
        if category.get("status") in {"blocked", "not-yet-clear"}
    )
    if unclear_categories:
        errors.append(
            f"{record_label} public-safe decision conflicts with uncleared categories: "
            f"{', '.join(unclear_categories)}"
        )
    for permission in ("publication_permission", "artifact_approval"):
        if rights_review.get(permission) not in allowed_public_permissions:
            errors.append(f"{record_label} public record lacks {permission.replace('_', ' ')}")
    if (
        record.get("ai_assistance", {}).get("used") is True
        and rights_review.get("ai_processing_permission") not in allowed_public_permissions
    ):
        errors.append(f"{record_label} records AI use without AI-processing permission")
    if (
        rights_review.get("model_training_permission") in {"unknown", "not-sought"}
        and public_safe_categories.get("model_training", {}).get("status") == "clear"
    ):
        errors.append(f"{record_label} clears model training without a recorded decision")

    withdrawal = record.get("withdrawal", {})
    if withdrawal.get("status") in {"acted", "partially-acted"} and not withdrawal.get("actions"):
        errors.append(f"{record_label} records withdrawal action without an action history")

    access_set = record.get("document_access_set", {})
    if access_set.get("denominator") != len(access_set.get("items", [])):
        errors.append(f"{record_label} document-access denominator does not match the named set")
    expected_denominator = access_set.get("denominator")
    for name, reading in record.get("access_readings", {}).items():
        if reading.get("denominator_ref") == "document_access_set":
            for count in reading.get("counts", []):
                if count.get("denominator") != expected_denominator:
                    errors.append(
                        f"{record_label} {name} count denominator does not match document_access_set"
                    )

    affected_ids = {party.get("id") for party in record.get("affected_people", [])}
    impact_ids = {impact.get("affected_party_id") for impact in record.get("party_impacts", [])}
    if affected_ids != impact_ids:
        missing = sorted(str(item) for item in affected_ids - impact_ids)
        extra = sorted(str(item) for item in impact_ids - affected_ids)
        errors.append(
            f"{record_label} party-impact coverage mismatch; missing={missing}, extra={extra}"
        )
    allowed_actor_ids = set(affected_ids)
    walking_id = record.get("walking_person", {}).get("id")
    if walking_id:
        allowed_actor_ids.add(walking_id)
    for action in record.get("agency_actions", []):
        if action.get("actor_id") not in allowed_actor_ids:
            errors.append(
                f"{record_label} agency action {action.get('id')} names an unknown actor_id"
            )

    for key_path in find_prohibited_score_keys(record):
        errors.append(f"prohibited combined-score field in {record_label}: {key_path}")


def check_schema_and_records(json_data: dict[Path, Any], errors: list[str]) -> None:
    try:
        from jsonschema import Draft202012Validator, FormatChecker
        from jsonschema.exceptions import SchemaError
    except ImportError:
        errors.append(
            'missing required dependency: install "jsonschema>=4.18" before running scripts/check_repo.py'
        )
        return

    schema = json_data.get(FIELD_TEST_SCHEMA)
    if not isinstance(schema, dict):
        return
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        errors.append(f"invalid field-test schema: {exc.message}")
        return

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for path in sorted(FIELD_TEST_DIR.glob("*.json")):
        record = json_data.get(path)
        if not isinstance(record, dict):
            continue
        for validation_error in sorted(validator.iter_errors(record), key=lambda error: list(error.path)):
            location = "/".join(str(part) for part in validation_error.path) or "<root>"
            errors.append(
                f"field-test schema violation: {relative(path)}:{location}: {validation_error.message}"
            )
        check_record_rules(path, record, errors)


def main() -> int:
    errors: list[str] = []

    for name in REQUIRED_ARCHITECTURE:
        if not (ROOT / name).is_file():
            errors.append(f"missing required file: {name}")

    json_data: dict[Path, Any] = {}
    for path in files(".json"):
        json_data[path] = load_json(path, errors)

    check_markdown(errors)
    check_schema_and_records(json_data, errors)

    ft001 = json_data.get(FT001)
    if isinstance(ft001, dict):
        for path in REQUIRED_FT001_PATHS:
            if not has_path(ft001, path):
                rendered = ".".join(str(part) for part in path)
                errors.append(f"FT-001 missing required structured field: {rendered}")

    if errors:
        print("Repository checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    record_count = len(list(FIELD_TEST_DIR.glob("*.json")))
    print(
        "Repository checks passed: "
        f"{len(files('.md'))} Markdown files, {len(files('.json'))} JSON files, "
        f"{record_count} schema-conformant field-test record(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
