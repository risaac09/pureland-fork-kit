#!/usr/bin/env python3
"""Tests for the semantic record rules in check_repo.py.

Run with `python3 scripts/test_check_repo.py`.

These tests exist because of one finding. Before `support_blockers()`, a
field-test record could claim `supports-tested-context` for the primary
hypothesis while a required Attend went unperformed, its predeclared action
came back `no-change`, every follow-up impact reading sat `pending` with an
unknown material increase, and its observation window stayed open. That record
passed the schema and every semantic rule with zero errors. The completion
gates all key on `test_status: complete`, and the record never claimed
completion.

FT-001 was never exposed to it, because FT-001 classifies itself
`unmeasurable`. The gap would have bitten on the second record. The fixture
below is that second record, built in memory from FT-001 so it stays a real
record rather than a hand-written shape, and it is kept as a test so the gate
is known to have failed once.
"""

from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

import check_repo  # noqa: E402

FT001_PATH = check_repo.ROOT / "data" / "field-tests" / "ft-001-alchemy.json"
SCHEMA_PATH = check_repo.ROOT / "data" / "field-test.schema.json"
FIXTURE_PATH = check_repo.ROOT / "data" / "field-tests" / "ft-900-fixture.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def errors_for(record: dict[str, Any]) -> list[str]:
    found: list[str] = []
    check_repo.check_record_rules(FIXTURE_PATH, record, found)
    return found


def supporting_record() -> dict[str, Any]:
    """FT-001 rewritten as a record that claims support for the primary hypothesis.

    Only the fields a support claim turns on are touched. Everything the gap
    left unguarded keeps FT-001's own value: Attend not performed, the window
    open, and every follow-up impact reading pending with an unknown material
    increase.
    """
    record = copy.deepcopy(load(FT001_PATH))
    record["record_id"] = "FT-900"
    record["tested_hypothesis"]["kind"] = "primary"
    action = record["agency_actions"][0]
    action["predefined_before_analysis"] = True
    action["follow_up"]["status"] = "observed"
    action["follow_up"]["observed_at"] = "2026-09-05"
    action["result"] = "no-change"
    record["materiality_rule"]["predeclared_before_analysis"] = True
    record["contestability"]["route_status"] = "usable"
    record["contestability"]["affected_party_tested"] = True
    record["outcome"]["classification"] = "supports-tested-context"
    return record


def evidenced_record() -> dict[str, Any]:
    """The same claim with the evidence the primary hypothesis actually needs."""
    record = supporting_record()
    record["test_status"] = "complete"
    for station in record["station_completion"].values():
        station["status"] = "complete"
    record["human_observe"]["status"] = "performed"
    record["human_observe"]["performer"] = "walker"
    record["human_observe"]["ai_or_design_analysis_substituted"] = False
    record["walking_person"]["id"] = "walker"
    record["walking_person"]["status"] = "present"
    record["agency_actions"][0]["result"] = "improved"
    record["follow_up"]["status"] = "complete"
    for impact in record["party_impacts"]:
        for dimension in ("exposure", "extractability", "shifted_burden"):
            impact["baseline"][dimension]["status"] = "observed"
            reading = impact["follow_up"][dimension]
            reading["status"] = "observed"
            reading["material_increase"] = False
            reading["evidence"] = ["Observed at the close of the window."]
    return record


class SupportGate(unittest.TestCase):
    def test_the_gap_fixture_is_now_refused(self) -> None:
        found = errors_for(supporting_record())
        joined = "\n".join(found)
        self.assertTrue(found, "the synthetic support claim raised no error")
        for expected in (
            "without performed human Attend where the scope requires it",
            "test status is partial-execution",
            "improved on its baseline",
            "unresolved follow-up impact readings",
            "observation window recorded open",
        ):
            self.assertIn(expected, joined)

    def test_the_gap_fixture_still_conforms_to_the_schema(self) -> None:
        """The gate is semantic. The schema was never the thing that caught this."""
        import jsonschema

        jsonschema.validate(supporting_record(), load(SCHEMA_PATH))

    def test_an_evidenced_support_claim_passes(self) -> None:
        self.assertEqual(errors_for(evidenced_record()), [])

    def test_a_no_change_result_cannot_support(self) -> None:
        record = evidenced_record()
        record["agency_actions"][0]["result"] = "no-change"
        self.assertIn("improved on its baseline", "\n".join(errors_for(record)))

    def test_an_unknown_material_increase_cannot_support(self) -> None:
        record = evidenced_record()
        record["party_impacts"][0]["follow_up"]["exposure"]["material_increase"] = None
        self.assertIn("material increase unknown", "\n".join(errors_for(record)))

    def test_a_refused_or_unmeasurable_window_cannot_support(self) -> None:
        """A closed window is not a settled one. Neither of these produced evidence."""
        for status in ("refused", "closed-unmeasurable"):
            with self.subTest(status=status):
                record = evidenced_record()
                record["follow_up"]["status"] = status
                self.assertIn(
                    f"observation window recorded {status}", "\n".join(errors_for(record))
                )

    def test_an_unread_baseline_cannot_support(self) -> None:
        """An increase is measured against a baseline, so an unread one grounds nothing."""
        record = evidenced_record()
        record["party_impacts"][0]["baseline"]["exposure"]["status"] = "pending"
        self.assertIn("baseline.exposure (pending)", "\n".join(errors_for(record)))

    def test_a_design_hypothesis_keeps_its_narrower_claim(self) -> None:
        """A partial instrument test may still support its own design hypothesis."""
        record = supporting_record()
        record["tested_hypothesis"]["kind"] = "design"
        record["human_observe"]["status"] = "performed"
        record["station_completion"]["observe"]["status"] = "complete"
        self.assertEqual(errors_for(record), [])


class LiveRecords(unittest.TestCase):
    def test_ft001_is_unaffected(self) -> None:
        self.assertEqual(errors_for(load(FT001_PATH)), [])

    def test_the_fixture_never_entered_the_repository(self) -> None:
        """The failing record is built in memory. data/ holds public-safe records only."""
        self.assertFalse(FIXTURE_PATH.exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
