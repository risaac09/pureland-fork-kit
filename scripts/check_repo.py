#!/usr/bin/env python3
"""Run small, dependency-free integrity checks for the PureLand repository."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git"}
SELF = Path(__file__).resolve()

LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
ATTR_LINK = re.compile(r"\b(src|href|srcset)=(['\"])(.*?)\2")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
PLACEHOLDER = re.compile(r"\b(TODO|TBD|INSERT[_ -]?HERE)\b", re.IGNORECASE)

FIELD_TEST_SCHEMA = ROOT / "data" / "field-test.schema.json"
REQUIRED_ARCHITECTURE = (
    "LICENSE",
    "LICENSE.md",
    "README.md",
    "BRIEF.md",
    "JOURNEY.md",
    "METHOD.md",
    "HYPOTHESIS.md",
    "TESTING.md",
    "CURRENT-EVIDENCE.md",
    "RESEARCH-STATUS.md",
    "FIELD-TESTING.md",
    "FIELD-TRIALS.md",
    "OFFERING.md",
    "data/README.md",
    "data/field-test.schema.json",
    "templates/field-test.md",
)

JOURNEY_STATIONS = {"ground", "observe", "map", "trace", "adapt", "return"}
ACCESS_DIMENSIONS = {"understandable", "reachable", "adaptable", "traceable"}
RECIPROCITY_DIMENSIONS = {"consent", "attribution", "value_return"}
INCOMPLETE_COMPLETION_WORDING = re.compile(r"\bmethod\s+completion\b", re.IGNORECASE)

SUPPORTED_SCHEMA_KEYS = {
    "$schema",
    "$id",
    "title",
    "description",
    "type",
    "additionalProperties",
    "required",
    "properties",
    "enum",
    "const",
    "minLength",
    "minItems",
    "items",
    "minimum",
    "pattern",
    "uniqueItems",
}

# Entry points a reader (or a fork) actually lands on. Orphan detection asks
# whether every other content file is reachable from here by some chain of
# links, not just whether something happens to point at it.
LINK_ROOTS = {ROOT / "README.md", ROOT / "JOURNEY.md", ROOT / "BRIEF.md"}

# Files that are legitimately not woven into prose: citation metadata and a
# changelog are conventionally browsed directly, not linked from the text.
ORPHAN_ALLOWLIST = {ROOT / "CITATION.cff", ROOT / "CHANGELOG.md"}

# File types that carry repo content, subject to orphan detection. .github/
# is excluded below: GitHub discovers issue templates, PR templates, and
# workflows on its own, not through prose links, so it is not part of the
# "reachable from README" contract.
CONTENT_SUFFIXES = {".md", ".html", ".css", ".json", ".cff", ".svg"}

# File types scanned for TODO/TBD/INSERT_HERE placeholder tokens.
PLACEHOLDER_SUFFIXES = {".md", ".html", ".json", ".yml", ".yaml", ".py"}

JSON_TYPES = {
    "object": dict,
    "array": list,
    "string": str,
    "number": (int, float),
    "integer": int,
    "boolean": bool,
    "null": type(None),
}


def type_matches(value: object, expected: object) -> bool:
    names = expected if isinstance(expected, list) else [expected]
    for name in names:
        py = JSON_TYPES.get(name)
        if py is None:
            continue
        # bool is a subclass of int in Python; JSON does not agree.
        if name in ("number", "integer") and isinstance(value, bool):
            continue
        if isinstance(value, py):
            return True
    return False


def validate_against_schema(value: object, schema: dict, where: str) -> list[str]:
    """Validate one record against the subset of JSON Schema this repo uses.

    Deliberately hand-rolled: check_repo.py is dependency-free by design and CI
    installs nothing, so pulling in jsonschema would trade the property that
    makes this runnable anywhere for keywords the schema does not use. The
    schema-definition check below rejects unsupported keywords instead of
    silently skipping them.
    """
    errors: list[str] = []

    if "const" in schema and value != schema["const"]:
        errors.append(f"{where}: must be {json.dumps(schema['const'])}, got {json.dumps(value)}")
        return errors

    if "type" in schema and not type_matches(value, schema["type"]):
        errors.append(f"{where}: expected {schema['type']}, got {json.dumps(value)}")
        return errors

    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{where}: must be one of {schema['enum']}, got {json.dumps(value)}")
    if "minLength" in schema and isinstance(value, str) and len(value) < schema["minLength"]:
        errors.append(f"{where}: must be at least {schema['minLength']} character(s)")
    if "minItems" in schema and isinstance(value, list) and len(value) < schema["minItems"]:
        errors.append(f"{where}: must have at least {schema['minItems']} item(s)")
    if "minimum" in schema and isinstance(value, (int, float)) and not isinstance(value, bool):
        if value < schema["minimum"]:
            errors.append(f"{where}: must be at least {schema['minimum']}, got {value}")
    if "pattern" in schema and isinstance(value, str):
        if re.search(schema["pattern"], value) is None:
            errors.append(f"{where}: must match /{schema['pattern']}/, got {json.dumps(value)}")
    if schema.get("uniqueItems") is True and isinstance(value, list):
        serialized = [json.dumps(item, sort_keys=True) for item in value]
        if len(serialized) != len(set(serialized)):
            errors.append(f"{where}: items must be unique")

    if isinstance(value, list) and "items" in schema:
        for index, item in enumerate(value):
            errors.extend(validate_against_schema(item, schema["items"], f"{where}[{index}]"))

    if isinstance(value, dict):
        properties = schema.get("properties", {})
        for name in schema.get("required", []):
            if name not in value:
                errors.append(f"{where}: missing required field '{name}'")
        if schema.get("additionalProperties") is False:
            for name in value:
                if name not in properties:
                    errors.append(f"{where}: unexpected field '{name}'")
        for name, subschema in properties.items():
            if name in value:
                errors.extend(validate_against_schema(value[name], subschema, f"{where}.{name}"))

    return errors


def validate_schema_definition(schema: object, where: str = "$") -> list[str]:
    """Check that the published schema is well-formed for the enforced subset.

    This is not a replacement for the JSON Schema metaschema. It makes the
    dependency-free contract explicit: every keyword in the repository schema
    must be understood and deterministically enforced by this script.
    """
    if not isinstance(schema, dict):
        return [f"schema {where}: expected an object"]

    errors: list[str] = []
    for key in schema:
        if key not in SUPPORTED_SCHEMA_KEYS:
            errors.append(f"schema {where}: unsupported keyword '{key}'")

    declared_type = schema.get("type")
    if declared_type is not None:
        type_names = declared_type if isinstance(declared_type, list) else [declared_type]
        if not type_names or any(name not in JSON_TYPES for name in type_names):
            errors.append(f"schema {where}.type: unknown or empty type declaration")
        if len(type_names) != len(set(type_names)):
            errors.append(f"schema {where}.type: duplicate type declaration")

    properties = schema.get("properties")
    if properties is not None and not isinstance(properties, dict):
        errors.append(f"schema {where}.properties: expected an object")
        properties = {}

    required = schema.get("required")
    if required is not None:
        if not isinstance(required, list) or not all(isinstance(name, str) for name in required):
            errors.append(f"schema {where}.required: expected an array of strings")
        else:
            if len(required) != len(set(required)):
                errors.append(f"schema {where}.required: duplicate field name")
            known = set(properties or {})
            for name in required:
                if name not in known:
                    errors.append(f"schema {where}.required: '{name}' has no property schema")

    if "additionalProperties" in schema and not isinstance(schema["additionalProperties"], bool):
        errors.append(f"schema {where}.additionalProperties: expected a boolean")
    if "enum" in schema and (not isinstance(schema["enum"], list) or not schema["enum"]):
        errors.append(f"schema {where}.enum: expected a non-empty array")
    elif "enum" in schema:
        serialized_enum = [json.dumps(item, sort_keys=True) for item in schema["enum"]]
        if len(serialized_enum) != len(set(serialized_enum)):
            errors.append(f"schema {where}.enum: duplicate value")
    for keyword in ("minLength", "minItems"):
        if keyword in schema:
            value = schema[keyword]
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                errors.append(f"schema {where}.{keyword}: expected a non-negative integer")
    if "minimum" in schema:
        value = schema["minimum"]
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            errors.append(f"schema {where}.minimum: expected a number")
    if "uniqueItems" in schema and not isinstance(schema["uniqueItems"], bool):
        errors.append(f"schema {where}.uniqueItems: expected a boolean")
    if "pattern" in schema:
        if not isinstance(schema["pattern"], str):
            errors.append(f"schema {where}.pattern: expected a string")
        else:
            try:
                re.compile(schema["pattern"])
            except re.error as exc:
                errors.append(f"schema {where}.pattern: invalid regular expression: {exc}")

    if isinstance(properties, dict):
        for name, subschema in properties.items():
            errors.extend(validate_schema_definition(subschema, f"{where}.properties.{name}"))

    if "items" in schema:
        errors.extend(validate_schema_definition(schema["items"], f"{where}.items"))

    return errors


def files(suffix: str) -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob(f"*{suffix}")
        if not any(part in IGNORED for part in path.parts)
    )


def content_files() -> list[Path]:
    """Every file subject to orphan detection: repo content, not tooling."""
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.suffix in CONTENT_SUFFIXES
        and not any(part in IGNORED for part in path.parts)
        and ".github" not in path.parts
    )


def slugify(heading: str) -> str:
    """Approximate GitHub's heading-to-anchor slug rule."""
    text = re.sub(r"[^\w\s-]", "", heading.strip().lower())
    return re.sub(r"\s+", "-", text)


def heading_slugs(text: str) -> set[str]:
    """Anchor slugs a Markdown file's own headings would produce.

    Duplicate headings get GitHub's -1, -2, ... suffix so a link that only
    resolves because of that suffix is still caught as valid.
    """
    seen: dict[str, int] = {}
    slugs: set[str] = set()
    for _, title in HEADING.findall(text):
        slug = slugify(title)
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        slugs.add(slug if count == 0 else f"{slug}-{count}")
    return slugs


def targets_in_attr(attr_name: str, raw: str) -> list[str]:
    """Split one src=/href=/srcset= attribute value into link targets.

    Only srcset packs multiple "url descriptor" entries separated by commas;
    src and href carry exactly one target, which may itself legally contain a
    comma (a query string, for instance), so it must not be comma-split.
    """
    if attr_name != "srcset":
        return [raw.strip()] if raw.strip() else []
    return [entry.strip().split()[0] for entry in raw.split(",") if entry.strip()]


def attr_targets(text: str) -> list[str]:
    """All src=/href=/srcset= link targets in one file's text."""
    return [
        target
        for match in ATTR_LINK.finditer(text)
        for target in targets_in_attr(match.group(1), match.group(3))
    ]


def dimension_errors(
    value: object,
    key: str,
    expected: set[str],
    where: str,
) -> list[str]:
    """Require one structured reading for every named dimension."""
    if not isinstance(value, list) or not all(isinstance(item, dict) for item in value):
        return []  # The schema validator reports the shape error.
    names = [item.get(key) for item in value]
    errors: list[str] = []
    if len(names) != len(set(names)):
        errors.append(f"{where}: duplicate {key} values")
    found = {name for name in names if isinstance(name, str)}
    if found != expected:
        errors.append(f"{where}: expected {sorted(expected)}, got {sorted(found)}")
    return errors


def validate_record_structure(record: object, path: Path) -> list[str]:
    """Check cross-field evidence-record rules without judging the concepts."""
    if not isinstance(record, dict):
        return []  # The schema validator reports the top-level type error.

    where = path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else str(path)
    errors: list[str] = []

    measurement = record.get("measurement_unit")
    if isinstance(measurement, dict):
        artifact_set = measurement.get("artifact_set")
        denominator = measurement.get("denominator")
        if isinstance(artifact_set, list) and isinstance(denominator, int):
            if len(artifact_set) != denominator:
                errors.append(
                    f"{where}.measurement_unit: denominator {denominator} "
                    f"does not match artifact_set length {len(artifact_set)}"
                )

    affected = record.get("affected_people")
    impacts = record.get("impacts_by_affected_party")
    if isinstance(affected, list) and all(isinstance(item, dict) for item in affected):
        affected_ids = [item.get("party_id") for item in affected]
        if len(affected_ids) != len(set(affected_ids)):
            errors.append(f"{where}.affected_people: duplicate party_id values")
        if isinstance(impacts, list) and all(isinstance(item, dict) for item in impacts):
            impact_ids = [item.get("party_id") for item in impacts]
            if len(impact_ids) != len(set(impact_ids)):
                errors.append(f"{where}.impacts_by_affected_party: duplicate party_id values")
            if set(impact_ids) != set(affected_ids):
                errors.append(
                    f"{where}.impacts_by_affected_party: party IDs must exactly match affected_people"
                )

    errors.extend(
        dimension_errors(record.get("access_readings"), "access", ACCESS_DIMENSIONS, f"{where}.access_readings")
    )
    errors.extend(
        dimension_errors(
            record.get("reciprocity_readings"),
            "dimension",
            RECIPROCITY_DIMENSIONS,
            f"{where}.reciprocity_readings",
        )
    )

    actions = record.get("agency_actions")
    if isinstance(actions, list) and all(isinstance(item, dict) for item in actions):
        action_ids = [item.get("action_id") for item in actions]
        if len(action_ids) != len(set(action_ids)):
            errors.append(f"{where}.agency_actions: duplicate action_id values")

    scope = record.get("scope_and_instrument")
    whole_journey = isinstance(scope, dict) and scope.get("whole_journey") is True
    stations = record.get("station_completion")
    station_map: dict[object, object] = {}
    if isinstance(stations, list) and all(isinstance(item, dict) for item in stations):
        station_names = [item.get("station") for item in stations]
        if len(station_names) != len(set(station_names)):
            errors.append(f"{where}.station_completion: duplicate station values")
        station_map = {item.get("station"): item.get("status") for item in stations}
        if whole_journey and set(station_names) != JOURNEY_STATIONS:
            errors.append(
                f"{where}.station_completion: a whole journey requires exactly {sorted(JOURNEY_STATIONS)}"
            )

    human_observe = record.get("human_observe")
    observe_status = human_observe.get("status") if isinstance(human_observe, dict) else None
    if whole_journey and station_map.get("observe") != observe_status:
        errors.append(
            f"{where}: Observe station status and human_observe status must match"
        )

    if whole_journey and record.get("test_status") == "completed":
        incomplete = sorted(
            station for station in JOURNEY_STATIONS if station_map.get(station) != "completed"
        )
        if incomplete:
            errors.append(
                f"{where}: test_status completed with incomplete required stations: {incomplete}"
            )
        if observe_status != "completed":
            errors.append(
                f"{where}: test_status completed requires completed human Observe"
            )

    has_incomplete_station = whole_journey and any(
        station_map.get(station) != "completed" for station in JOURNEY_STATIONS
    )
    if has_incomplete_station:
        completion_sources = [(where, json.dumps(record, ensure_ascii=False))]
        completion_sources.extend(
            (candidate.relative_to(ROOT).as_posix(), candidate.read_text(encoding="utf-8"))
            for candidate in files(".md")
        )
        for source_name, text_to_check in completion_sources:
            if INCOMPLETE_COMPLETION_WORDING.search(text_to_check):
                errors.append(
                    f"{where}: incomplete required stations cannot be described with "
                    f"completion wording in {source_name}"
                )

    second_reader = record.get("second_reader")
    if isinstance(second_reader, dict):
        if second_reader.get("status") == "absent" and second_reader.get("independent") is not False:
            errors.append(f"{where}.second_reader: an absent reader cannot be independent")

    objections = record.get("participant_objections")
    if isinstance(objections, dict):
        items = objections.get("items")
        status = objections.get("status")
        if status in {"not_collected", "not_applicable", "refused", "collected_none"} and items:
            errors.append(f"{where}.participant_objections: status {status} requires an empty items list")
        if status == "collected_with_objections" and isinstance(items, list) and not items:
            errors.append(f"{where}.participant_objections: collected_with_objections requires an item")

    outcome = record.get("outcome")
    rights = record.get("permission_and_rights")
    classification = outcome.get("classification") if isinstance(outcome, dict) else None
    if isinstance(rights, dict) and rights.get("rights_review") == "incomplete":
        if classification != "unmeasurable":
            errors.append(f"{where}: incomplete rights review requires an unmeasurable outcome")

    if classification == "support_tested_context" and isinstance(outcome, dict):
        required_outcomes = (
            outcome.get("practical_agency"),
            outcome.get("attention_sovereignty"),
            outcome.get("contestability"),
            outcome.get("meaningful_return"),
        )
        if any(value != "supported" for value in required_outcomes):
            errors.append(f"{where}: support requires supported person, contestability, and return outcomes")
        if not isinstance(actions, list) or not any(
            isinstance(action, dict) and action.get("follow_up_status") == "measured"
            for action in actions
        ):
            errors.append(f"{where}: support requires at least one measured predefined action")
        if not isinstance(rights, dict) or rights.get("rights_review") not in {"completed", "private"}:
            errors.append(f"{where}: support requires completed or private rights evidence")
        if isinstance(rights, dict) and (
            rights.get("assessment_permission") not in {"obtained", "not_required"}
            or rights.get("adaptation_permission") not in {"obtained", "not_required"}
        ):
            errors.append(f"{where}: support requires applicable assessment and adaptation permission")
        if isinstance(impacts, list):
            harm_statuses = [
                item.get(dimension, {}).get("status")
                for item in impacts
                if isinstance(item, dict)
                for dimension in ("exposure", "extractability", "shifted_burden")
                if isinstance(item.get(dimension), dict)
            ]
            if any(status in {"material_increase", "unmeasurable"} for status in harm_statuses):
                errors.append(
                    f"{where}: support cannot contain a material or unmeasurable affected-party harm"
                )

    if isinstance(outcome, dict):
        construct_results = {
            outcome.get("practical_agency"),
            outcome.get("attention_sovereignty"),
            outcome.get("contestability"),
            outcome.get("meaningful_return"),
        }
        if "mixed" in construct_results and classification != "mixed":
            errors.append(f"{where}: a mixed construct profile must remain mixed")

    privacy = record.get("public_privacy_review")
    if isinstance(privacy, dict):
        if privacy.get("status") == "passed" and privacy.get("safe_for_public_release") is not True:
            errors.append(f"{where}.public_privacy_review: passed requires safe_for_public_release true")

    if path.name == "ft-001-alchemy.json":
        expected = {
            "record_id": record.get("record_id") == "FT-001",
            "partial dry-run status": record.get("test_status") == "partial_dry_run",
            "maintainer-side assessor": isinstance(record.get("assessor_relationship"), dict)
            and record["assessor_relationship"].get("category") == "maintainer_side",
            "non-human walking role": isinstance(record.get("walking_person"), dict)
            and record["walking_person"].get("is_human") is False,
            "no second reader": isinstance(second_reader, dict)
            and second_reader.get("status") == "absent"
            and second_reader.get("independent") is False,
            "seven-surface denominator": isinstance(measurement, dict)
            and measurement.get("denominator") == 7,
            "human Observe not performed": observe_status == "not_performed",
            "no affected-user challenge": isinstance(objections, dict)
            and objections.get("status") == "not_collected",
            "executed adaptation": isinstance(record.get("adaptation"), dict)
            and record["adaptation"].get("status") == "executed"
            and any("/pull/15" in item for item in record["adaptation"].get("evidence", [])),
            "open follow-up through 2026-11-22": isinstance(record.get("follow_up"), dict)
            and record["follow_up"].get("status") == "open"
            and record["follow_up"].get("review_date") == "2026-11-22",
            "unmeasurable non-causal outcome": isinstance(outcome, dict)
            and outcome.get("classification") == "unmeasurable"
            and outcome.get("practical_agency") == "unmeasurable"
            and outcome.get("attention_sovereignty") == "unmeasurable"
            and outcome.get("causal_claim") is False,
        }
        for fact, present in expected.items():
            if not present:
                errors.append(f"{where}: FT-001 must preserve {fact}")

    return errors


def check_targets(
    path: Path,
    raw_targets: list[str],
    text_by_path: dict[Path, str],
    errors: list[str],
    graph: dict[Path, set[Path]],
) -> None:
    for target in raw_targets:
        clean, _, fragment = target.partition("#")
        if not clean or clean.startswith(("http://", "https://", "mailto:", "data:", "//")):
            continue
        # A leading "/" is repo-root-relative (as GitHub treats it), not a
        # filesystem-root path. Path's "/" operator would otherwise discard
        # path.parent entirely and resolve against the real filesystem root.
        if clean.startswith("/"):
            resolved = (ROOT / clean.lstrip("/")).resolve()
        else:
            resolved = (path.parent / clean).resolve()
        if not resolved.is_relative_to(ROOT):
            errors.append(f"link escapes repository: {path.relative_to(ROOT)} -> {target}")
            continue
        if not resolved.exists():
            errors.append(f"broken local link: {path.relative_to(ROOT)} -> {target}")
            continue
        graph[path].add(resolved)
        if fragment and resolved.suffix == ".md":
            target_text = text_by_path.get(resolved)
            if target_text is None:
                target_text = resolved.read_text(encoding="utf-8")
                text_by_path[resolved] = target_text
            if fragment not in heading_slugs(target_text):
                errors.append(
                    f"broken anchor: {path.relative_to(ROOT)} -> {target} "
                    f"(no heading in {resolved.relative_to(ROOT)} produces #{fragment})"
                )


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    parsed: dict[Path, object] = {}
    for path in files(".json"):
        try:
            parsed[path] = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid JSON: {path.relative_to(ROOT)}: {exc}")

    # data/README.md tells contributors to "validate it against
    # field-test.schema.json", but nothing did: this check parsed JSON and
    # stopped, so a submission with an unsafe public privacy review, or with
    # extra identifying fields the schema forbids, passed CI green. The schema
    # sets the repo's privacy boundary, so it has to be enforced, not just published.
    schema = parsed.get(FIELD_TEST_SCHEMA)
    if schema is None:
        if FIELD_TEST_SCHEMA.exists():
            errors.append("field-test schema present but unreadable; cannot validate data/")
    elif not isinstance(schema, dict):
        errors.append("field-test schema must be a JSON object")
    else:
        errors.extend(validate_schema_definition(schema))
        # rglob, not glob: submitted records live in data/field-tests/, one
        # level below data/ itself. A non-recursive glob here would only ever
        # see the schema file and validate nothing.
        for path in sorted((ROOT / "data").rglob("*.json")):
            if path == FIELD_TEST_SCHEMA or path not in parsed:
                continue
            errors.extend(
                validate_against_schema(parsed[path], schema, path.relative_to(ROOT).as_posix())
            )
            errors.extend(validate_record_structure(parsed[path], path))

    # Links, anchors, and the reachability graph. HTML is scanned via
    # src=/href=/srcset= attributes, both in .html files and in raw HTML
    # embedded in Markdown (the README banner uses <picture>, <source>,
    # <img>, none of which markdown-link syntax would ever see).
    text_by_path: dict[Path, str] = {}
    for path in files(".md") + files(".html"):
        text_by_path[path] = path.read_text(encoding="utf-8")

    graph: dict[Path, set[Path]] = defaultdict(set)

    for path in files(".md"):
        text = text_by_path[path]
        check_targets(path, LINK.findall(text), text_by_path, errors, graph)
        check_targets(path, attr_targets(text), text_by_path, errors, graph)
        if PLACEHOLDER.search(text):
            errors.append(f"placeholder token: {path.relative_to(ROOT)}")

    for path in files(".html"):
        text = text_by_path[path]
        check_targets(path, attr_targets(text), text_by_path, errors, graph)

    # Placeholder tokens beyond Markdown. .py is included deliberately: this
    # script's own source is exempt, because the PLACEHOLDER pattern above
    # literally spells out TODO / TBD / INSERT_HERE and would otherwise flag
    # itself for doing its job, not for actually containing a placeholder.
    # Structured field-test records use explicit unmeasurable, refused, and
    # private states, so placeholder tokens in JSON are errors rather than an
    # acceptable way to carry missing evidence.
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in PLACEHOLDER_SUFFIXES:
            continue
        if any(part in IGNORED for part in path.parts):
            continue
        if path == SELF or path.suffix == ".md":
            continue
        text = text_by_path.get(path)
        if text is None:
            text = path.read_text(encoding="utf-8")
        if PLACEHOLDER.search(text):
            errors.append(f"placeholder token: {path.relative_to(ROOT)}")

    # Orphan detection: every content file should be reachable from README,
    # JOURNEY, or BRIEF by some chain of links. This is a warning, not a
    # failure. A few files are legitimately unlinked (see ORPHAN_ALLOWLIST),
    # and a good-faith field-test PR should never fail CI over an unrelated
    # file it cannot fix.
    reachable: set[Path] = set(LINK_ROOTS)
    queue = list(LINK_ROOTS)
    while queue:
        current = queue.pop()
        for target in graph.get(current, ()):
            if target not in reachable:
                reachable.add(target)
                queue.append(target)

    for path in content_files():
        if path in reachable or path in ORPHAN_ALLOWLIST:
            continue
        warnings.append(
            f"orphan: {path.relative_to(ROOT)} is not reachable from "
            f"README.md, JOURNEY.md, or BRIEF.md by any link"
        )

    for name in REQUIRED_ARCHITECTURE:
        if not (ROOT / name).is_file():
            errors.append(f"missing required file: {name}")

    if warnings:
        print("Repository check warnings (do not fail this check):")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("Repository checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Repository checks passed: {len(files('.md'))} Markdown files, "
        f"{len(files('.json'))} JSON files, {len(warnings)} warning(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
