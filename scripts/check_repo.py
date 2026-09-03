#!/usr/bin/env python3
"""Run deterministic structural checks for the PureLand repository."""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git"}
SELF = Path(__file__).resolve()

LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
ATTR_LINK = re.compile(r"\b(src|href|srcset)=(['\"])(.*?)\2")
CSS_URL = re.compile(r"url\(\s*['\"]?([^'\")]+)['\"]?\s*\)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
PLACEHOLDER = re.compile(r"\b(TODO|TBD|INSERT[_ -]?HERE)\b", re.IGNORECASE)
METHOD_COMPLETION = re.compile(r"\bmethod completion\b", re.IGNORECASE)
PAGES_BASE = "https://risaac09.github.io/pureland-fork-kit/"
BLOB_BASE = "https://github.com/risaac09/pureland-fork-kit/blob/main/"
RELEASE_CLAIM = re.compile(r"\bThis is version (\d+)\.(\d+)\.")
# A sentence ends at a period followed by space and a capital. An
# abbreviation before a lowercase word or a digit does not end one.
SENTENCE_END = re.compile(r"\.(?=\s+[A-Z])")
CFF_VERSION = re.compile(r"^version:\s*[\"']?(\d+)\.(\d+)", re.MULTILINE)

# A follow-up in one of these states is still owed an outcome. The other
# statuses in the schema enum (complete, closed-unmeasurable, refused) are
# closed results, and a closed result cannot go stale.
OPEN_FOLLOW_UP_STATUSES = {"not-started", "open"}
TODAY_OVERRIDE = "PURELAND_TODAY"

FIELD_TEST_SCHEMA = ROOT / "data" / "field-test.schema.json"
FIELD_TEST_DIR = ROOT / "data" / "field-tests"
FT001 = FIELD_TEST_DIR / "ft-001-alchemy.json"
LLMS_TXT = ROOT / "llms.txt"
INDEX_HTML = ROOT / "index.html"
CITATION = ROOT / "CITATION.cff"

REQUIRED_ARCHITECTURE = [
    "LICENSE",
    "LICENSE.md",
    "README.md",
    "llms.txt",
    "index.html",
    "JOURNEY.md",
    "CROSSWALK.md",
    "OFFERING.md",
    "THESIS.md",
    "METHOD.md",
    "TOOLBOX.md",
    "TESTING.md",
    "CURRENT-EVIDENCE.md",
    "RESEARCH-STATUS.md",
    "data/README.md",
    "data/field-test.schema.json",
    "templates/field-test.md",
    "templates/walk-it-yourself.md",
    "templates/walk-with-a-model.md",
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

# Field-test records are free-text, first-person accounts of what a
# contributor found, including what is still open. data/README.md and
# CONTRIBUTING.md ask for exactly that ("PureLand needs documented
# disagreement more than applause"), so an honest "second reader: TBD" in a
# submitted record is content, not a placeholder left behind by mistake.
FIELD_TEST_RECORDS = ROOT / "data" / "field-tests"

# Entry points a reader (or a fork) actually lands on. Orphan detection asks
# whether every other content file is reachable from here by some chain of
# links, not just whether something happens to point at it.
LINK_ROOTS = {ROOT / "README.md", ROOT / "JOURNEY.md"}

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

def files(suffix: str) -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob(f"*{suffix}")
        if not any(part in IGNORED for part in path.parts)
    )


def prose_files() -> list[Path]:
    """Markdown documents plus the model-facing llms.txt index."""
    return files(".md") + ([LLMS_TXT] if LLMS_TXT.is_file() else [])


def record_files() -> list[Path]:
    """Every JSON under data/ that is a field-test record, not the schema.

    rglob, not glob: records live in data/field-tests/, one level below data/,
    and a record dropped anywhere else under data/ still has to clear the same
    privacy boundary. Assumption: every JSON under data/ other than the schema
    is a field-test record. That holds today. A data file of some other shape
    would fail against this schema, so add a path filter here before adding one.
    """
    return sorted(
        path for path in (ROOT / "data").rglob("*.json") if path != FIELD_TEST_SCHEMA
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


def content_files() -> list[Path]:
    """Every file subject to orphan detection: repo content, not tooling."""
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and (path.suffix in CONTENT_SUFFIXES or path == LLMS_TXT)
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


def check_targets(
    path: Path,
    raw_targets: list[str],
    text_by_path: dict[Path, str],
    errors: list[str],
    graph: dict[Path, set[Path]],
) -> None:
    for target in raw_targets:
        clean, _, fragment = target.partition("#")
        # Links to this repository's own Pages site are checked as local
        # files; llms.txt uses the absolute form so its links work for a
        # model reading the raw file, and rot there must still fail here.
        if clean.startswith(PAGES_BASE):
            clean = "/" + clean[len(PAGES_BASE):]
            if clean == "/":
                clean = "/index.html"
        # index.html points at kit documents by their rendered GitHub URL, so
        # they read as pages rather than as raw Markdown a browser downloads.
        # Those links were skipped as external and could rot silently while a
        # relative link to the same file failed loudly. Rewriting them to local
        # paths puts both forms under the same check. Only blob/main is
        # rewritten: a link pinned to another ref or a commit names a state
        # this working tree cannot speak for.
        # A bare blob/main/ link is GitHub's file listing for the repository
        # root, not a file in it, so it stays external and is skipped rather
        # than rewritten to "/" and passed as an existing path.
        elif clean.startswith(BLOB_BASE) and len(clean) > len(BLOB_BASE):
            clean = "/" + clean[len(BLOB_BASE):]
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
        for prose in prose_files():
            text = prose.read_text(encoding="utf-8")
            if record_id and record_id in text.lower() and METHOD_COMPLETION.search(text):
                errors.append(
                    f"prohibited completion wording for incomplete {record_label}: {relative(prose)}"
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


def reference_date(errors: list[str]) -> dt.date:
    """Today, in UTC, unless PURELAND_TODAY names another date.

    The override exists so the overdue check can be fired on demand. A
    date-dependent check nobody can test is the same silent absence it was
    built to catch: without it, the first real run happens on the day it
    matters, with no evidence it works.

    Set it locally, never in a workflow. Under --fail-on-overdue-follow-up
    the notices are errors, so a frozen past date in the scheduled watch's
    environment would hide a real overdue follow-up behind a green run.
    """
    override = os.environ.get(TODAY_OVERRIDE)
    if not override:
        return dt.datetime.now(dt.timezone.utc).date()
    try:
        return dt.date.fromisoformat(override)
    except ValueError:
        errors.append(f"invalid {TODAY_OVERRIDE} value: {override!r}; expected YYYY-MM-DD")
        return dt.datetime.now(dt.timezone.utc).date()


def overdue_follow_ups(
    path: Path, record: dict[str, Any], today: dt.date, notices: list[str]
) -> None:
    """Notice a follow-up left open past its own review date.

    TESTING.md requires an observation window, a review date, and a
    follow-up status, and nothing compared that date to the calendar. An
    expired window that nobody closes becomes missing evidence carried as an
    open status, and TESTING.md is explicit that absence never defaults to
    favorable. This is the calendar half of that rule.
    """
    label = record.get("record_id", relative(path))
    follow_up = record.get("follow_up", {})
    status = follow_up.get("status")
    if status not in OPEN_FOLLOW_UP_STATUSES:
        return

    raw = follow_up.get("review_date")
    try:
        review_date = dt.date.fromisoformat(raw)
    except (TypeError, ValueError):
        # Only schema-conformant records reach here, so the date parsed once
        # already. Reaching this branch means the schema stopped enforcing
        # the format, which is worth saying out loud rather than skipping.
        notices.append(f"{label} follow-up review_date is not a readable date: {raw!r}")
        return

    if review_date < today:
        days = (today - review_date).days
        notices.append(
            f"{label} follow-up is still {status} {days} day(s) past its review date "
            f"{review_date.isoformat()}: close it with an outcome, or record it as "
            f"closed-unmeasurable"
        )


THROUGH_DATE = re.compile(r"\bthrough (\d{4}-\d{2}-\d{2})")
FOLLOW_UP_LINE = re.compile(r"follow-?up", re.IGNORECASE)
CURRENT_EVIDENCE = ROOT / "CURRENT-EVIDENCE.md"
UNRELEASED_DRIFT_WARNING = (
    "the live site deploys main and carries unreleased changes; "
    "cut a patch release or accept the drift."
)


def git_commit_status(commit: str) -> tuple[bool | None, str | None]:
    """Return whether a commit resolves, plus a reason when it cannot be checked."""
    try:
        shallow = subprocess.run(
            ["git", "rev-parse", "--is-shallow-repository"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return None, "git is unavailable"

    if shallow.returncode != 0:
        return None, "Git metadata is unavailable"

    try:
        resolved = subprocess.run(
            ["git", "cat-file", "-e", f"{commit}^{{commit}}"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return None, "git is unavailable"
    if resolved.returncode == 0:
        return True, None
    if shallow.stdout.strip() == "true":
        return None, "the checkout is shallow"
    return False, None


def public_safe_report_section(text: str) -> str:
    """Return the report text from its artifact-version public-safe marker onward."""
    lines = text.splitlines()
    marker = next(
        (
            index
            for index, line in enumerate(lines)
            if "artifact-version public-safe" in line.lower()
        ),
        None,
    )
    if marker is None:
        return ""
    end = next(
        (
            index
            for index in range(marker + 1, len(lines))
            if lines[index].startswith("## ")
        ),
        len(lines),
    )
    return "\n".join(lines[marker:end])


def markdown_h2_section(text: str, heading: str) -> str:
    """Return one level-two Markdown section without later peer sections."""
    lines = text.splitlines()
    start = next(
        (
            index + 1
            for index, line in enumerate(lines)
            if line.strip().lower() == f"## {heading.lower()}"
        ),
        None,
    )
    if start is None:
        return ""
    end = next(
        (index for index in range(start, len(lines)) if lines[index].startswith("## ")),
        len(lines),
    )
    return "\n".join(lines[start:end])


def changelog_has_unreleased_entries() -> bool:
    """Read the release record rather than maintaining a second status copy."""
    changelog = ROOT / "CHANGELOG.md"
    if not changelog.is_file():
        return False
    section = markdown_h2_section(
        changelog.read_text(encoding="utf-8"), "Unreleased"
    )
    section = re.sub(r"<!--.*?-->", "", section, flags=re.DOTALL)
    return bool(section.strip())


def check_record_consistency(
    conformant: set[Path],
    json_data: dict[Path, Any],
    errors: list[str],
    warnings: list[str],
) -> tuple[int, int]:
    """Tie each conformant record to its report, ledger row, and kit commit."""
    records = [
        (path, json_data[path])
        for path in sorted(conformant)
        if isinstance(json_data.get(path), dict)
    ]
    ids: defaultdict[str, list[Path]] = defaultdict(list)
    for path, record in records:
        ids[str(record.get("record_id", ""))].append(path)
    for record_id, paths in sorted(ids.items()):
        if record_id and len(paths) > 1:
            errors.append(
                f"duplicate record_id {record_id}: "
                + ", ".join(relative(path) for path in paths)
            )

    ledger_lines = (
        markdown_h2_section(
            CURRENT_EVIDENCE.read_text(encoding="utf-8"), "The ledger"
        ).splitlines()
        if CURRENT_EVIDENCE.is_file()
        else []
    )

    for path, record in records:
        record_id = str(record.get("record_id", ""))
        label = record_id or relative(path)
        expected_prefix = record_id.lower() + "-"
        if record_id and not path.stem.startswith(expected_prefix):
            errors.append(
                f"{label} record filename must begin {expected_prefix!r}: {relative(path)}"
            )

        report = ROOT / "research" / "field-tests" / f"{path.stem}.md"
        report_text = report.read_text(encoding="utf-8") if report.is_file() else ""
        if not report.is_file():
            errors.append(f"{label} missing paired report: {relative(report)}")

        matching_rows = [line for line in ledger_lines if path.name in line]
        if len(matching_rows) != 1:
            errors.append(
                f"{label} must have exactly one CURRENT-EVIDENCE.md ledger row naming "
                f"{path.name}; found {len(matching_rows)}"
            )

        kit_version = str(record.get("kit_version", ""))
        match = re.match(r"\s*([0-9a-fA-F]{7,40})\b", kit_version)
        if match is None:
            errors.append(f"{label} kit_version has no leading hexadecimal commit: {kit_version!r}")
            continue
        commit = match.group(1)
        if report.is_file() and commit not in report_text:
            errors.append(f"{label} kit_version {commit} is missing from {relative(report)}")
        if len(matching_rows) == 1 and commit not in matching_rows[0]:
            errors.append(
                f"{label} kit_version {commit} is missing from its CURRENT-EVIDENCE.md ledger row"
            )

        artifact_version = str(
            record.get("public_safe_review", {}).get("artifact_version", "")
        )
        if report.is_file() and artifact_version not in public_safe_report_section(report_text):
            errors.append(
                f"{label} public-safe artifact_version {artifact_version!r} is missing from "
                f"{relative(report)}'s public-safe section"
            )

        reachable, reason = git_commit_status(commit)
        if reachable is False:
            errors.append(f"{label} kit_version commit is unreachable in the full clone: {commit}")
        elif reachable is None:
            warnings.append(
                f"{label} kit_version commit {commit} was not verified because {reason}"
            )

    independent = sum(
        record.get("assessor", {}).get("independence") == "independent"
        for _, record in records
    )
    practices = {
        name
        for _, record in records
        if isinstance((name := record.get("practice", {}).get("name")), str) and name
    }
    return independent, len(practices)


def check_follow_up_date_copies(path: Path, record: dict[str, Any], errors: list[str]) -> None:
    """Tie the prose copies of a follow-up review date to the record.

    overdue_follow_ups() compares follow_up.review_date to the calendar, and
    two prose surfaces advertise the same date: the ledger row in
    CURRENT-EVIDENCE.md and the record's report. Nothing compared those
    copies to the record, so a window closed or extended in the JSON would
    leave a stale date advertised on a green run.

    The scope follows check_version_claims(): only lines that mention the
    follow-up are read, and only the date after the word "through" on such a
    line is compared, because dated history (CHANGELOG.md, research
    snapshots) legitimately keeps old dates and comparing every date would
    fail a true statement. While the follow-up is open, the ledger row has to
    carry the date: the row is the one live advertisement of the window, and
    deleting the date would otherwise disarm this tie silently.
    """
    label = record.get("record_id", relative(path))
    follow_up = record.get("follow_up", {})
    raw = follow_up.get("review_date")
    if not isinstance(raw, str):
        # overdue_follow_ups() reports an unreadable date; nothing to tie.
        return

    # The report belongs to this record, so every follow-up line in it is
    # read. CURRENT-EVIDENCE.md is shared between records, so only the lines
    # that name this record's file are read: without that filter, one
    # record's check would attribute another record's ledger row to it the
    # moment a second record lands.
    report = ROOT / "research" / "field-tests" / (path.stem + ".md")
    for surface in (CURRENT_EVIDENCE, report):
        if not surface.is_file():
            continue
        for number, line in enumerate(
            surface.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if surface == CURRENT_EVIDENCE and path.name not in line:
                continue
            if not FOLLOW_UP_LINE.search(line):
                continue
            for found in THROUGH_DATE.findall(line):
                if found != raw:
                    errors.append(
                        f"{relative(surface)}:{number} says the {label} follow-up runs "
                        f"through {found}, but the record's review_date is {raw}"
                    )

    if follow_up.get("status") not in OPEN_FOLLOW_UP_STATUSES:
        return
    if CURRENT_EVIDENCE.is_file():
        ledger_rows = [
            line
            for line in CURRENT_EVIDENCE.read_text(encoding="utf-8").splitlines()
            if path.name in line
        ]
        if ledger_rows and not any(raw in line for line in ledger_rows):
            errors.append(
                f"the CURRENT-EVIDENCE.md ledger row for {label} does not carry its "
                f"open follow-up review date {raw}; the row is the one live copy"
            )


def check_version_claims(errors: list[str]) -> None:
    """Tie the release version the entry points announce to CITATION.cff.

    index.html, README.md, and llms.txt each open by naming the release, and
    llms.txt's summary is the fragment a context-limited consumer keeps. Those
    numerals were copies nothing compared, so a release that bumped
    CITATION.cff alone would leave any of the three entry points announcing
    the old version.

    Only the "This is version N.M." sentence is read, and every occurrence is
    compared rather than the first. The remaining numeral in llms.txt names the
    method contract, which does not move with a release, so comparing every
    numeral would fail a true sentence. llms.txt and index.html have to carry
    the claim, because the check is the tie and rephrasing the numeral away
    would otherwise disarm it silently; README.md is compared when it carries
    one. A missing file is REQUIRED_ARCHITECTURE's error, not this one. The
    patch level stays CITATION.cff's alone; the prose names major and minor.
    """
    if not LLMS_TXT.is_file():
        return
    claims: list[tuple[Path, tuple[int, int]]] = []
    for path in (LLMS_TXT, ROOT / "README.md", INDEX_HTML):
        if not path.is_file():
            continue
        for claim in RELEASE_CLAIM.finditer(path.read_text(encoding="utf-8")):
            claims.append((path, (int(claim.group(1)), int(claim.group(2)))))
    missing = [
        required
        for required in (LLMS_TXT, INDEX_HTML)
        if required.is_file() and not any(path == required for path, _ in claims)
    ]
    for required in missing:
        errors.append(
            f'{relative(required)} announces no release version: it needs a '
            '"This is version N.M." sentence'
        )
    if missing:
        return
    if not CITATION.is_file():
        errors.append("CITATION.cff missing: the release claims cannot be checked")
        return
    released = CFF_VERSION.search(CITATION.read_text(encoding="utf-8"))
    if released is None:
        errors.append("CITATION.cff has no parsable version field")
        return
    current = (int(released.group(1)), int(released.group(2)))
    for path, announced in claims:
        if announced != current:
            errors.append(
                f"{relative(path)} announces version {announced[0]}.{announced[1]}, "
                f"but CITATION.cff released {current[0]}.{current[1]}"
            )


def check_ceiling_copy(errors: list[str]) -> None:
    """Tie the page's evidence ceiling to CURRENT-EVIDENCE.md's first sentence.

    The page carried four paraphrases of the ceiling that nothing compared;
    now one copy stands, in the evidence band, and it is checked against the
    record rather than restated from memory. The tied text is the first
    non-empty line in CURRENT-EVIDENCE.md after the H1, cut at its first
    sentence end, a period followed by space and a capital letter, so an
    abbreviation before a lowercase word does not shorten it. Zero
    occurrences in index.html means the page has lost the ceiling; more than
    one means it carries the ceiling twice, which is the same drift the four
    paraphrases caused. The match runs over the page's source, so the copy
    has to sit in one text node with no tag or entity inside the sentence.
    """
    # Both files are in REQUIRED_ARCHITECTURE, which already reports either
    # one missing; a second error here would name one cause twice.
    if not CURRENT_EVIDENCE.is_file() or not INDEX_HTML.is_file():
        return

    text = CURRENT_EVIDENCE.read_text(encoding="utf-8")
    h1 = next((m for m in HEADING.finditer(text) if m.group(1) == "#"), None)
    body = text[h1.end():] if h1 else text
    first_line = next((line.strip() for line in body.splitlines() if line.strip()), None)
    if first_line is None:
        errors.append(
            "CURRENT-EVIDENCE.md has no non-empty line after its H1: the "
            "ceiling copy cannot be checked"
        )
        return

    end = SENTENCE_END.search(first_line)
    sentence = first_line[: end.end()] if end else first_line
    count = INDEX_HTML.read_text(encoding="utf-8").count(sentence)
    if count == 0:
        errors.append(
            "index.html has lost the evidence ceiling: CURRENT-EVIDENCE.md's "
            f"first sentence does not appear on the page: {sentence!r}"
        )
    elif count > 1:
        errors.append(
            f"index.html carries the evidence ceiling {count} times, not once: "
            f"{sentence!r}"
        )


def check_schema_and_records(json_data: dict[Path, Any], errors: list[str]) -> set[Path]:
    """Validate every field-test record against data/field-test.schema.json.

    Returns the records that conformed. check_record_rules() reads a record by
    the shape the schema guarantees, so a record that failed here is not handed
    to it: a contributor who writes a list where the schema says object should
    get the schema violation, not a traceback.
    """
    try:
        from jsonschema import Draft202012Validator, FormatChecker
        from jsonschema.exceptions import SchemaError
    except ImportError:
        errors.append(
            'missing required dependency: install "jsonschema>=4.18" before running scripts/check_repo.py'
        )
        return set()

    schema = json_data.get(FIELD_TEST_SCHEMA)
    if not isinstance(schema, dict):
        if FIELD_TEST_SCHEMA.exists():
            errors.append("field-test schema present but unreadable; cannot validate data/")
        return set()
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        errors.append(f"invalid field-test schema: {exc.message}")
        return set()

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    conformant: set[Path] = set()
    for path in record_files():
        record = json_data.get(path)
        if record is None:
            # Unparseable JSON already reported by load_json(); a parseable
            # non-dict record still goes through the validator so the schema's
            # top-level "type": "object" rejects it instead of a silent skip.
            continue
        violations = sorted(validator.iter_errors(record), key=lambda error: list(error.path))
        for violation in violations:
            location = "/".join(str(part) for part in violation.path) or "<root>"
            errors.append(
                f"field-test schema violation: {relative(path)}:{location}: {violation.message}"
            )
        if not violations:
            conformant.add(path)
    return conformant


STRICT_FOLLOW_UP_FLAG = "--fail-on-overdue-follow-up"
LIST_ARCHITECTURE_FLAG = "--list-architecture"


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    # The scheduled follow-up watch passes this flag so an overdue review
    # turns the run red and reaches a person. An ordinary push or pull
    # request never sets it: a contributor's PR should not fail over a
    # maintainer's calendar, the same reason orphan detection only warns.
    strict_follow_ups = STRICT_FOLLOW_UP_FLAG in args
    known = {STRICT_FOLLOW_UP_FLAG, LIST_ARCHITECTURE_FLAG}
    unknown = [arg for arg in args if arg not in known]
    if unknown:
        print(f"unknown argument(s): {' '.join(unknown)}", file=sys.stderr)
        print(
            f"usage: check_repo.py [{STRICT_FOLLOW_UP_FLAG}] "
            f"[{LIST_ARCHITECTURE_FLAG}]",
            file=sys.stderr,
        )
        return 2

    # REQUIRED_ARCHITECTURE is the only statement of what this repository must
    # contain, and a person had no way to read it without opening this file.
    # This renders the one copy rather than letting a prose copy exist
    # anywhere: a second copy would drift, and the drift would stay invisible
    # until a release.
    #
    # It refuses to run beside another flag. This branch returns 0 without
    # validating anything, so a run that combined it with the strict
    # follow-up flag would report success having checked nothing, and the
    # scheduled watch reads a green run as "no follow-up is overdue".
    if LIST_ARCHITECTURE_FLAG in args:
        if len(args) > 1:
            print(
                f"{LIST_ARCHITECTURE_FLAG} prints the architecture and runs no "
                f"checks; it cannot be combined with another flag",
                file=sys.stderr,
            )
            return 2
        for name in REQUIRED_ARCHITECTURE:
            print(name)
        return 0

    errors: list[str] = []
    warnings: list[str] = []

    if changelog_has_unreleased_entries():
        warnings.append(UNRELEASED_DRIFT_WARNING)

    for name in REQUIRED_ARCHITECTURE:
        if not (ROOT / name).is_file():
            errors.append(f"missing required file: {name}")

    check_version_claims(errors)
    check_ceiling_copy(errors)

    json_data: dict[Path, Any] = {}
    for path in files(".json"):
        json_data[path] = load_json(path, errors)

    # data/README.md tells contributors to "validate it against
    # field-test.schema.json", but nothing did: this check parsed JSON and
    # stopped, so a submission with privacy_review false, or carrying extra
    # identifying fields the schema forbids, passed CI green. The schema sets
    # the repo's privacy boundary, so it has to be enforced, not just published.
    #
    # Validation goes through jsonschema rather than a hand-rolled subset. The
    # research-arc schema uses $ref, $defs, 13 allOf/if/then pairs, not, and
    # contains; those applicators are exactly where a hand-rolled validator
    # gets it quietly wrong, and this schema is the repo's privacy gate. CI
    # installs the dependency (see .github/workflows/validate.yml).
    conformant = check_schema_and_records(json_data, errors)

    today = reference_date(errors)
    follow_up_notices: list[str] = []

    # Schema conformance is structural. The research arc's rules are semantic:
    # what a record may claim given the rights, contestability, and
    # action-outcome evidence it actually carries. Both have to hold.
    for path in sorted(conformant):
        record = json_data.get(path)
        if isinstance(record, dict):
            check_record_rules(path, record, errors)
            overdue_follow_ups(path, record, today, follow_up_notices)
            check_follow_up_date_copies(path, record, errors)

    independent_count, practice_count = check_record_consistency(
        conformant, json_data, errors, warnings
    )
    print(
        "Gate accounting (counts, not scores): "
        f"independent records={independent_count}; "
        f"distinct practice.name values={practice_count}."
    )

    # Where these land depends on who is asking. The scheduled watch wants a
    # red run; everyone else wants a note that does not block their work.
    (errors if strict_follow_ups else warnings).extend(follow_up_notices)

    ft001 = json_data.get(FT001)
    if isinstance(ft001, dict):
        for required_path in REQUIRED_FT001_PATHS:
            if not has_path(ft001, required_path):
                rendered = ".".join(str(part) for part in required_path)
                errors.append(f"FT-001 missing required structured field: {rendered}")

    # Links, anchors, and the reachability graph. HTML is scanned via
    # src=/href=/srcset= attributes, both in .html files and in raw HTML
    # embedded in Markdown (the README banner uses <picture>, <source>,
    # <img>, none of which markdown-link syntax would ever see).
    text_by_path: dict[Path, str] = {}
    for path in prose_files() + files(".html") + files(".css"):
        text_by_path[path] = path.read_text(encoding="utf-8")

    graph: dict[Path, set[Path]] = defaultdict(set)

    for path in prose_files():
        text = text_by_path[path]
        check_targets(path, LINK.findall(text), text_by_path, errors, graph)
        check_targets(path, attr_targets(text), text_by_path, errors, graph)
        if PLACEHOLDER.search(text):
            errors.append(f"placeholder token: {relative(path)}")

    for path in files(".html"):
        text = text_by_path[path]
        check_targets(path, attr_targets(text), text_by_path, errors, graph)
    # A stylesheet's url() references are links too. The self-hosted font
    # files were the one class of local reference nothing resolved: a renamed
    # woff2 passed green and the visitor got the fallback face with no signal.
    for path in files(".css"):
        text = text_by_path[path]
        check_targets(path, CSS_URL.findall(text), text_by_path, errors, graph)

    # Placeholder tokens beyond Markdown. .py is included deliberately: this
    # script's own source is exempt, because the PLACEHOLDER pattern above
    # literally spells out TODO / TBD / INSERT_HERE and would otherwise flag
    # itself for doing its job, not for actually containing a placeholder.
    # data/field-tests/ records are exempt too: they are contributors' own
    # free-text accounts, and an honest "TBD" there is content, not litter.
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in PLACEHOLDER_SUFFIXES:
            continue
        if any(part in IGNORED for part in path.parts):
            continue
        if path == SELF or path.suffix == ".md" or FIELD_TEST_RECORDS in path.parents:
            continue
        text = text_by_path.get(path)
        if text is None:
            text = path.read_text(encoding="utf-8")
        if PLACEHOLDER.search(text):
            errors.append(f"placeholder token: {relative(path)}")

    # Orphan detection: every content file should be reachable from README or
    # JOURNEY by some chain of links. This is a warning, not a
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
            f"orphan: {relative(path)} is not reachable from "
            f"README.md or JOURNEY.md by any link"
        )

    if warnings:
        print("Repository check warnings (do not fail this check):")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("Repository checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    record_count = len(record_files())
    print(
        "Repository checks passed: "
        f"{len(files('.md'))} Markdown files, 1 model index, "
        f"{len(files('.json'))} JSON files, "
        f"{record_count} schema-conformant field-test record(s), "
        f"{len(warnings)} warning(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
