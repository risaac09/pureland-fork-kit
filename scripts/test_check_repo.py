#!/usr/bin/env python3
"""Subprocess tests for PureLand's cross-artifact record gates."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SOURCE = Path(__file__).resolve().parents[1]
RECORD = Path("data/field-tests/ft-001-alchemy.json")
REPORT = Path("research/field-tests/ft-001-alchemy.md")
LEDGER = Path("CURRENT-EVIDENCE.md")
VERSION = "62259ec"
ARTIFACT_VERSION = "FT-001-integrated-v0.1-2026-08-24"


class CheckRepoConsistencyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.repo = Path(self.temporary.name) / "repo"
        shutil.copytree(
            SOURCE,
            self.repo,
            ignore=shutil.ignore_patterns(".git", "work", "__pycache__"),
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_checker(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "scripts/check_repo.py"],
            cwd=self.repo,
            capture_output=True,
            text=True,
            check=False,
        )

    def read_record(self) -> dict:
        return json.loads((self.repo / RECORD).read_text(encoding="utf-8"))

    def write_record(self, record: dict, path: Path = RECORD) -> None:
        (self.repo / path).write_text(
            json.dumps(record, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    def replace(self, path: Path, old: str, new: str) -> None:
        target = self.repo / path
        target.write_text(
            target.read_text(encoding="utf-8").replace(old, new),
            encoding="utf-8",
        )

    def init_git(self, shallow: bool = False) -> None:
        subprocess.run(["git", "init", "-q"], cwd=self.repo, check=True)
        subprocess.run(["git", "add", "."], cwd=self.repo, check=True)
        subprocess.run(
            [
                "git",
                "-c",
                "user.name=PureLand Test",
                "-c",
                "user.email=pureland-test@example.invalid",
                "commit",
                "-qm",
                "fixture",
            ],
            cwd=self.repo,
            check=True,
        )
        if shallow:
            head = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=self.repo,
                capture_output=True,
                text=True,
                check=True,
            ).stdout.strip()
            (self.repo / ".git" / "shallow").write_text(head + "\n", encoding="utf-8")

    def set_version(self, version: str) -> None:
        record = self.read_record()
        record["kit_version"] = f"{version} (2026-08-24)"
        self.write_record(record)
        self.replace(REPORT, VERSION, version)
        self.replace(LEDGER, VERSION, version)

    def assert_failed_with(self, expected: str) -> None:
        result = self.run_checker()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(expected, result.stdout)

    def test_positive(self) -> None:
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(
            "Gate accounting (counts, not scores): independent records=0; "
            "distinct practice.name values=1.",
            result.stdout,
        )

    def test_duplicate_id(self) -> None:
        duplicate = self.read_record()
        path = Path("data/field-tests/ft-001-copy.json")
        self.write_record(duplicate, path)
        ledger = self.repo / LEDGER
        matching = next(line for line in ledger.read_text().splitlines() if RECORD.name in line)
        ledger.write_text(ledger.read_text() + "\n" + matching.replace(RECORD.name, path.name) + "\n")
        shutil.copy2(self.repo / REPORT, self.repo / "research/field-tests/ft-001-copy.md")
        self.assert_failed_with("duplicate record_id FT-001")

    def test_filename_mismatch(self) -> None:
        wrong = Path("data/field-tests/wrong-name.json")
        (self.repo / RECORD).rename(self.repo / wrong)
        self.assert_failed_with("record filename must begin 'ft-001-'")

    def test_filename_prefix_must_be_lowercase(self) -> None:
        wrong = Path("data/field-tests/FT-001-alchemy.json")
        (self.repo / RECORD).rename(self.repo / wrong)
        self.assert_failed_with("record filename must begin 'ft-001-'")

    def test_missing_report(self) -> None:
        (self.repo / REPORT).unlink()
        self.assert_failed_with("FT-001 missing paired report")

    def test_missing_ledger_row(self) -> None:
        self.replace(LEDGER, RECORD.name, "missing-record.json")
        self.assert_failed_with("found 0")

    def test_two_ledger_rows(self) -> None:
        ledger = self.repo / LEDGER
        text = ledger.read_text(encoding="utf-8")
        matching = next(line for line in text.splitlines() if RECORD.name in line)
        ledger.write_text(text.replace(matching, matching + "\n" + matching, 1), encoding="utf-8")
        self.assert_failed_with("found 2")

    def test_version_mismatch_in_report(self) -> None:
        self.replace(REPORT, VERSION, "1111111")
        self.assert_failed_with(f"kit_version {VERSION} is missing from research/field-tests")

    def test_version_mismatch_in_ledger(self) -> None:
        self.replace(LEDGER, VERSION, "1111111")
        self.assert_failed_with(
            f"kit_version {VERSION} is missing from its CURRENT-EVIDENCE.md ledger row"
        )

    def test_public_safe_artifact_version_mismatch(self) -> None:
        self.replace(REPORT, ARTIFACT_VERSION, "FT-001-integrated-v0.1-wrong")
        self.assert_failed_with(
            f"public-safe artifact_version '{ARTIFACT_VERSION}' is missing"
        )

    def test_unreachable_commit_in_full_clone_is_error(self) -> None:
        self.set_version("deadbeef")
        self.init_git()
        self.assert_failed_with("kit_version commit is unreachable in the full clone: deadbeef")

    def test_unreachable_commit_in_shallow_clone_is_warning(self) -> None:
        self.set_version("deadbeef")
        self.init_git(shallow=True)
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("not verified because the checkout is shallow", result.stdout)

    def test_malformed_json(self) -> None:
        (self.repo / RECORD).write_text("{not json}\n", encoding="utf-8")
        self.assert_failed_with("invalid JSON: data/field-tests/ft-001-alchemy.json")


if __name__ == "__main__":
    unittest.main()
