#!/usr/bin/env python3
"""Regression test for the kit 0.2 disposition register's item R6.

Two independent reads of the kit at commit 38ce830 found the same gap with
an in-memory fixture, the kit itself untouched: a record could claim
`supports-tested-context` while human Attend was not performed, the
predefined action's own observed result never improved, a party's follow-up
impact stayed pending, and the follow-up window stayed open. The record was
schema-conformant and check_record_rules() in scripts/check_repo.py raised
zero errors against it.

A code-review pass on the first fix found the same gap survives by another
name: the follow-up-impact guard checked only for a `pending` status, and a
`material_increase: null` reading left `unmeasurable` slips past it exactly
as `pending` did. The second case below is that finding, turned into a test.

Both cases build their fixture from FT-001's own public record with the
minimal field changes needed to reach the gap, confirm the fixture is still
schema-conformant (otherwise it would prove nothing about the semantic
rules), then call check_record_rules() and assert that the expected guards
fire. Nothing is written to data/: each fixture lives only in memory, so
neither becomes a record scripts/check_repo.py would validate on an
ordinary run.

Run directly: python3 scripts/test_classification_gap.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_repo  # noqa: E402

FT001_PATH = check_repo.FT001


def load_ft001() -> dict[str, Any]:
    return json.loads(FT001_PATH.read_text(encoding="utf-8"))


def base_gap_fixture() -> dict[str, Any]:
    """FT-001's own record, changed just enough to reach a schema-conformant
    `supports-tested-context` claim.

    Every other field, including human_observe.status ("not-performed"), is
    left exactly as the public FT-001 record carries it today.
    """
    record = load_ft001()
    record["record_id"] = "FT-999"
    record["materiality_rule"]["predeclared_before_analysis"] = True
    record["contestability"]["route_status"] = "usable"
    record["contestability"]["affected_party_tested"] = True
    record["agency_actions"][0]["predefined_before_analysis"] = True
    record["agency_actions"][0]["follow_up"]["status"] = "observed"
    record["agency_actions"][0]["result"] = "no-change"
    record["outcome"]["classification"] = "supports-tested-context"
    return record


def pending_impact_fixture() -> dict[str, Any]:
    """The original gap: every party_impacts follow-up left `pending`.

    FT-001 carries this shape today; the statuses are set here anyway so the
    case keeps testing `pending` if the public record ever moves on.
    """
    record = base_gap_fixture()
    for impact in record["party_impacts"]:
        for dimension in impact["follow_up"].values():
            if isinstance(dimension, dict) and "status" in dimension:
                dimension["status"] = "pending"
    return record


def incomplete_step_fixture() -> dict[str, Any]:
    """A required step other than Attend left incomplete on a support claim.

    The other guards look at the action, the impacts, the window, and Attend.
    A record with `map` required and unfinished, on a partial execution, has
    to be refused too, or the completion rule and the support rule disagree.
    """
    record = base_gap_fixture()
    record["station_completion"]["map"]["required"] = True
    record["station_completion"]["map"]["status"] = "incomplete"
    return record


def unmeasurable_impact_fixture() -> dict[str, Any]:
    """The code-review finding: `pending` swapped for `unmeasurable`.

    material_increase stays null either way; only the status label changes.
    A guard that checks for `pending` alone must not miss this one.
    """
    record = base_gap_fixture()
    for impact in record["party_impacts"]:
        for dimension in ("exposure", "extractability", "shifted_burden"):
            impact["follow_up"][dimension]["status"] = "unmeasurable"
    return record


def check_fixture(
    label: str, fixture: dict[str, Any], expected_substrings: list[str], schema: dict[str, Any]
) -> list[str]:
    """Return a list of failure lines; an empty list means the case passed."""
    from jsonschema import Draft202012Validator, FormatChecker

    failures: list[str] = []
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    schema_errors = sorted(validator.iter_errors(fixture), key=lambda e: list(e.path))
    if schema_errors:
        failures.append(f"{label}: fixture is not schema-conformant, so it proves nothing:")
        for error in schema_errors:
            where = "/".join(str(part) for part in error.path) or "<root>"
            failures.append(f"  - {where}: {error.message}")
        return failures

    errors: list[str] = []
    check_repo.check_record_rules(FT001_PATH, fixture, errors)
    missing = [
        substring
        for substring in expected_substrings
        if not any(substring in error for error in errors)
    ]
    if missing:
        failures.append(f"{label}: the gap was not fully caught. Missing guard(s):")
        for substring in missing:
            failures.append(f"  - ...{substring}")
        failures.append(f"{label}: errors actually raised:")
        for error in errors:
            failures.append(f"  - {error}")
        return failures

    print(f"PASS ({label}): caught by {len(errors)} check_record_rules() error(s):")
    for error in errors:
        print(f"  - {error}")
    return failures


def main() -> int:
    schema = json.loads(check_repo.FIELD_TEST_SCHEMA.read_text(encoding="utf-8"))

    common = [
        "without a predefined action whose own observed result improved",
        "with an unclosed follow-up window",
        "without performed human Attend",
    ]
    cases = [
        (
            "pending follow-up impact",
            pending_impact_fixture(),
            [*common, "while a party's follow-up impact is not resolved to observed or estimated"],
        ),
        (
            "unmeasurable follow-up impact",
            unmeasurable_impact_fixture(),
            [*common, "while a party's follow-up impact is not resolved to observed or estimated"],
        ),
        (
            "incomplete required step other than Attend",
            incomplete_step_fixture(),
            [*common, "with incomplete required steps: observe, map"],
        ),
    ]

    all_failures: list[str] = []
    for label, fixture, expected in cases:
        all_failures.extend(check_fixture(label, fixture, expected, schema))

    if all_failures:
        print("FAIL:")
        for line in all_failures:
            print(line)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
