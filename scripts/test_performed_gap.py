#!/usr/bin/env python3
"""Regression test for the `performed` gap in human_observe.

A five-pass agent-lane reading of the kit at commit 7543635 found that
`human_observe.status` could read `performed` while `performer` was null,
`evidence` was empty, and `ai_or_design_analysis_substituted` was true. The
record stayed schema-conformant, and check_record_rules() in
scripts/check_repo.py raised zero errors against it. Both layers were run
against the unrepaired schema before the fix and both returned nothing, so
the gap is a measured result rather than a reading of the source.

The label is load-bearing, which is what makes the gap worth closing. Two
guards in check_repo.py read `human_observe.status != "performed"` to refuse
a claim: one refuses a completion claim, the other refuses a support claim.
A forged `performed` does not sit inert in the record. It switches both
guards off.

The repair is a schema conditional rather than a new semantic rule. Whenever
the status reads `performed`, the schema now requires a non-empty performer,
at least one evidence item, and `ai_or_design_analysis_substituted` false.
The conditional sits next to the rule that mandates the `performed` label on
a complete record with Observe required, because that rule creates the
obligation this one makes truthful.

A code-review pass on the first repair found the gap surviving by another
name, exactly as the follow-up impact gap did at #37. `minLength` counts
characters and `minItems` counts items, so a performer of "   " and an
evidence item of "   " satisfied both and the forged record was accepted
again. The conditional now also requires a `\\S` match on the performer and
on every evidence item, which counts content rather than length. The two
whitespace cases below are that finding, turned into tests.

The cases below cover the full forgery and each single-field forgery on its
own, so that dropping any one leg of the conditional fails this test instead
of surviving by another name. Each refusal also asserts that no other
human_observe field was refused, so a conditional that later over-reaches
into the `not-performed` branch fails here rather than passing. The final
case validates FT-001's own published record unchanged: the rule constrains the `performed` branch only, and a
`not-performed` record must stay free to carry evidence explaining why Attend
did not happen, which is what FT-001 carries today.

Nothing is written to data/: every fixture lives only in memory, so none
becomes a record scripts/check_repo.py would validate on an ordinary run.

Run directly: python3 scripts/test_performed_gap.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_repo  # noqa: E402

FT001_PATH = check_repo.FT001

LEGITIMATE_OBSERVE: dict[str, Any] = {
    "status": "performed",
    "performer": "Named walker; second reader countersigned the notes.",
    "evidence": ["First-person Observe notes taken during the sitting."],
    "ai_or_design_analysis_substituted": False,
}


def load_ft001() -> dict[str, Any]:
    return json.loads(FT001_PATH.read_text(encoding="utf-8"))


def performed_fixture(**overrides: Any) -> dict[str, Any]:
    """FT-001's record with human_observe replaced by a `performed` claim.

    FT-001 is a partial execution, so none of the completion conditionals
    fire on it. That isolates the new rule as the only thing that can refuse
    these fixtures, which is what makes each refusal below mean something.
    """
    record = load_ft001()
    record["record_id"] = "FT-998"
    record["human_observe"] = {**LEGITIMATE_OBSERVE, **overrides}
    return record


def schema_errors(fixture: dict[str, Any], schema: dict[str, Any]) -> list[Any]:
    from jsonschema import Draft202012Validator, FormatChecker

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return sorted(validator.iter_errors(fixture), key=lambda e: list(e.path))


def describe(error: Any) -> str:
    where = "/".join(str(part) for part in error.path) or "<root>"
    return f"{where}: {error.message}"


def expect_refused(
    label: str, fixture: dict[str, Any], expected_paths: list[str], schema: dict[str, Any]
) -> list[str]:
    """Return failure lines; an empty list means the forgery was refused."""
    failures: list[str] = []
    errors = schema_errors(fixture, schema)
    if not errors:
        failures.append(f"{label}: the schema accepted the forged record. The gap is open.")
        return failures

    seen = {"/".join(str(part) for part in error.path) for error in errors}
    missing = [path for path in expected_paths if path not in seen]
    if missing:
        failures.append(f"{label}: refused, but not on the field(s) under test:")
        for path in missing:
            failures.append(f"  - nothing raised against {path}")
        failures.append(f"{label}: errors actually raised:")
        for error in errors:
            failures.append(f"  - {describe(error)}")
        return failures

    unexpected = sorted(
        path
        for path in seen
        if path.startswith("human_observe") and path not in expected_paths
    )
    if unexpected:
        failures.append(f"{label}: the rule refused field(s) the fixture did not forge:")
        for path in unexpected:
            failures.append(f"  - {path}")
        failures.append(f"{label}: errors actually raised:")
        for error in errors:
            failures.append(f"  - {describe(error)}")
        return failures

    print(f"PASS ({label}): refused by {len(errors)} schema error(s):")
    for error in errors:
        print(f"  - {describe(error)}")
    return failures


def expect_accepted(label: str, fixture: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    """Return failure lines; an empty list means the honest record passed."""
    failures: list[str] = []
    errors = schema_errors(fixture, schema)
    if errors:
        failures.append(f"{label}: the schema refused a record it should accept:")
        for error in errors:
            failures.append(f"  - {describe(error)}")
        return failures

    print(f"PASS ({label}): accepted, as an honest record must be.")
    return failures


def main() -> int:
    schema = json.loads(check_repo.FIELD_TEST_SCHEMA.read_text(encoding="utf-8"))

    refusals = [
        (
            "probe B: performed with no performer, no evidence, AI substituted",
            performed_fixture(
                performer=None, evidence=[], ai_or_design_analysis_substituted=True
            ),
            [
                "human_observe/performer",
                "human_observe/evidence",
                "human_observe/ai_or_design_analysis_substituted",
            ],
        ),
        (
            "performed with a null performer only",
            performed_fixture(performer=None),
            ["human_observe/performer"],
        ),
        (
            "performed with an empty performer string",
            performed_fixture(performer=""),
            ["human_observe/performer"],
        ),
        (
            "performed with a whitespace-only performer",
            performed_fixture(performer="   "),
            ["human_observe/performer"],
        ),
        (
            "performed with no evidence only",
            performed_fixture(evidence=[]),
            ["human_observe/evidence"],
        ),
        (
            "performed with a whitespace-only evidence item",
            performed_fixture(evidence=["   "]),
            ["human_observe/evidence/0"],
        ),
        (
            "performed with AI analysis substituted only",
            performed_fixture(ai_or_design_analysis_substituted=True),
            ["human_observe/ai_or_design_analysis_substituted"],
        ),
    ]

    all_failures: list[str] = []
    for label, fixture, expected in refusals:
        all_failures.extend(expect_refused(label, fixture, expected, schema))

    all_failures.extend(
        expect_accepted("a legitimate performed record", performed_fixture(), schema)
    )
    all_failures.extend(
        expect_accepted(
            "FT-001's published record, not-performed and unchanged", load_ft001(), schema
        )
    )

    if all_failures:
        print("FAIL:")
        for line in all_failures:
            print(line)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
