"""Synthetic rule probes. No fixture represents a person's execution."""

import copy
import datetime as dt
import json
import unittest

from jsonschema import Draft202012Validator, FormatChecker

import check_repo as check


def fixture():
    record = json.loads(check.FT001.read_text())
    record["record_id"] = "FT-999"
    record["tested_hypothesis"]["kind"] = "primary"
    record["materiality_rule"]["predeclared_before_analysis"] = True
    record["contestability"]["route_status"] = "usable"
    record["contestability"]["affected_party_tested"] = True
    action = record["agency_actions"][0]
    action["predefined_before_analysis"] = True
    for period in ("baseline", "follow_up"):
        action[period]["status"] = "observed"
        action[period]["observed_at"] = "2026-08-24"
    action["result"] = "no-change"
    record["outcome"]["classification"] = "supports-tested-context"
    return record


class RecordRules(unittest.TestCase):
    def gaps(self, record):
        return check.primary_support_gaps(record, dt.date(2026, 11, 23))

    def errors(self, record):
        errors = []
        check.check_record_rules(check.FT001, record, errors)
        return errors

    def test_reported_gap_is_schema_conformant_but_rejected(self):
        record = fixture()
        schema = json.loads(check.FIELD_TEST_SCHEMA.read_text())
        Draft202012Validator(schema, format_checker=FormatChecker()).validate(record)
        self.assertTrue(self.errors(record), "R6 accepted unsupported primary support")

    def test_existing_record_survives(self):
        record = json.loads(check.FT001.read_text())
        self.assertEqual(self.errors(record), [])

    def test_rule_checks_leave_record_unchanged(self):
        record = fixture()
        before = copy.deepcopy(record)
        self.errors(record)
        self.assertEqual(record, before)

    def test_no_change_cannot_support_primary(self):
        self.assertIn("improved predeclared person-level action", self.gaps(fixture()))

    def test_attend_cannot_be_waived_for_primary(self):
        record = fixture()
        record["station_completion"]["observe"]["required"] = False
        self.assertIn("human Attend evidence", self.gaps(record))
        self.assertIn("complete six-step execution", self.gaps(record))

    def test_every_party_and_dimension_needs_observed_follow_up(self):
        for party in range(len(fixture()["party_impacts"])):
            for dimension in ("exposure", "extractability", "shifted_burden"):
                for status in ("pending", "estimated", "not-observed", "unmeasurable"):
                    with self.subTest(party=party, dimension=dimension, status=status):
                        record = fixture()
                        for impact in record["party_impacts"]:
                            for period in ("baseline", "follow_up"):
                                for reading in impact[period].values():
                                    reading.update(status="observed", evidence=["synthetic probe"], material_increase=False)
                        record["party_impacts"][party]["follow_up"][dimension]["status"] = status
                        self.assertIn("observed impacts for every party under the materiality rule", self.gaps(record))

    def test_observed_impact_requires_explicit_negative_and_evidence(self):
        record = fixture()
        for impact in record["party_impacts"]:
            for period in ("baseline", "follow_up"):
                for reading in impact[period].values():
                    reading.update(status="observed", evidence=["synthetic probe"], material_increase=False)
        key = "observed impacts for every party under the materiality rule"
        self.assertNotIn(key, self.gaps(record))
        reading = record["party_impacts"][0]["follow_up"]["exposure"]
        reading["material_increase"] = None
        self.assertIn(key, self.gaps(record))
        reading["material_increase"] = False
        reading["evidence"] = []
        self.assertIn(key, self.gaps(record))

    def test_closed_status_alone_cannot_close_future_window(self):
        record = fixture()
        record["follow_up"]["status"] = "complete"
        gaps = check.primary_support_gaps(record, dt.date(2026, 9, 5))
        self.assertIn("closed observed follow-up window", gaps)

    def test_unknown_reversed_and_missing_windows(self):
        for start, end in ((None, None), ("bad", "2026-11-22"), ("2026-11-23", "2026-11-22")):
            with self.subTest(start=start, end=end):
                record = fixture()
                record["follow_up"]["status"] = "complete"
                record["follow_up"]["observation_window"].update(start=start, end=end)
                self.assertIn("closed observed follow-up window", self.gaps(record))

    def test_improved_action_needs_person_and_dates(self):
        record = fixture()
        record["walking_person"]["id"] = record["agency_actions"][0]["actor_id"]
        record["follow_up"]["status"] = "complete"
        record["agency_actions"][0]["result"] = "improved"
        record["agency_actions"][0]["evidence"] = ["synthetic probe"]
        key = "improved predeclared person-level action"
        self.assertNotIn(key, self.gaps(record))
        record["agency_actions"][0]["follow_up"]["observed_at"] = "2026-12-01"
        self.assertIn(key, self.gaps(record))

    def test_partial_design_claim_retains_narrow_rules(self):
        record = fixture()
        record["tested_hypothesis"]["kind"] = "design"
        self.assertEqual(self.errors(record), [])

    def test_material_harm_blocks_all_support(self):
        record = fixture()
        record["tested_hypothesis"]["kind"] = "design"
        record["party_impacts"][0]["follow_up"]["exposure"]["material_increase"] = True
        self.assertTrue(any("recorded material increase" in e for e in self.errors(record)))

    def test_unmeasurable_keeps_adverse_signal(self):
        record = fixture()
        record["outcome"]["classification"] = "unmeasurable"
        record["party_impacts"][0]["follow_up"]["exposure"]["material_increase"] = True
        before = copy.deepcopy(record)
        self.assertEqual(self.errors(record), [])
        self.assertEqual(record, before)

    def test_conflicting_action_blocks_support(self):
        record = fixture()
        record["agency_actions"][0]["result"] = "weakened"
        self.assertIn("classification preserving conflicting action results", self.gaps(record))

    def test_unexecuted_adaptation_blocks_support(self):
        record = fixture()
        record["adaptation"]["status"] = "proposed"
        self.assertIn("executed adaptation", self.gaps(record))

    def test_coverage_mismatch_still_fails(self):
        record = fixture()
        record["party_impacts"].pop()
        self.assertTrue(any("coverage mismatch" in e for e in self.errors(record)))


if __name__ == "__main__":
    unittest.main()
