#!/usr/bin/env python3
"""Regression test for the kit 0.2 disposition register's item R6.

Two independent reads of the kit at commit 38ce830 found the same gap with
an in-memory fixture, the kit itself untouched: a record could claim
`supports-tested-context` while human Attend was not performed, the
predefined action's own observed result never improved, a party's follow-up
impact stayed pending, and the follow-up window stayed open. The record was
schema-conformant and check_record_rules() in scripts/check_repo.py raised
zero errors against it.

This script builds that fixture from FT-001's own public record with the
minimal field changes needed to reach the gap, confirms the fixture is still
schema-conformant (otherwise it would prove nothing about the semantic
rules), then calls check_record_rules() and asserts that the four guards
added alongside this test each fire. It writes nothing to data/: the fixture
lives only in memory, so it never becomes a record scripts/check_repo.py
would validate on an ordinary run.

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


def build_gap_fixture() -> dict[str, Any]:
    """FT-001's own record, changed just enough to expose the gap.

    Every other field, including human_observe.status ("not-performed") and
    every party_impacts follow-up ("pending", material_increase null), is
    left exactly as the public FT-001 record carries it today.
    """
    record: dict[str, Any] = json.loads(FT001_PATH.read_text(encoding="utf-8"))
    record["record_id"] = "FT-999"
    record["materiality_rule"]["predeclared_before_analysis"] = True
    record["contestability"]["route_status"] = "usable"
    record["contestability"]["affected_party_tested"] = True
    record["agency_actions"][0]["predefined_before_analysis"] = True
    record["agency_actions"][0]["follow_up"]["status"] = "observed"
    record["agency_actions"][0]["result"] = "no-change"
    record["outcome"]["classification"] = "supports-tested-context"
    return record


def main() -> int:
    from jsonschema import Draft202012Validator, FormatChecker

    schema = json.loads(check_repo.FIELD_TEST_SCHEMA.read_text(encoding="utf-8"))
    fixture = build_gap_fixture()

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    schema_errors = sorted(validator.iter_errors(fixture), key=lambda e: list(e.path))
    if schema_errors:
        print("FAIL: the fixture is not schema-conformant, so it cannot exercise the gap:")
        for error in schema_errors:
            print(f"- {'/'.join(str(part) for part in error.path) or '<root>'}: {error.message}")
        return 1

    errors: list[str] = []
    check_repo.check_record_rules(FT001_PATH, fixture, errors)

    expected_substrings = [
        "without a predefined action whose own observed result improved",
        "while a party's follow-up impact is still pending",
        "with an unclosed follow-up window",
        "without performed human Attend",
    ]
    missing = [
        substring
        for substring in expected_substrings
        if not any(substring in error for error in errors)
    ]
    if missing:
        print("FAIL: the classification gap was not fully caught. Missing guard(s):")
        for substring in missing:
            print(f"- ...{substring}")
        print("Errors actually raised:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "PASS: the schema-conformant support-classification gap fixture is "
        f"caught by {len(errors)} check_record_rules() error(s):"
    )
    for error in errors:
        print(f"- {error}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
