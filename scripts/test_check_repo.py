#!/usr/bin/env python3
"""Subprocess tests for PureLand's cross-artifact record gates."""

from __future__ import annotations

import json
import re
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
UNRELEASED_DRIFT_WARNING = (
    "CHANGELOG.md contains unreleased changes; before publication, "
    "verify Pages and release state, then cut a release or accept the drift."
)


class CheckRepoConsistencyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.repo = Path(self.temporary.name) / "repo"
        shutil.copytree(
            SOURCE,
            self.repo,
            ignore=shutil.ignore_patterns(
                ".git", "graphify-out", "work", "__pycache__"
            ),
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
            (self.repo / ".git" / "shallow").write_text(
                head + "\n", encoding="utf-8"
            )

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

    def test_unreleased_entries_warn_from_changelog(self) -> None:
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(UNRELEASED_DRIFT_WARNING, result.stdout)

    def test_empty_unreleased_section_does_not_warn(self) -> None:
        changelog = self.repo / "CHANGELOG.md"
        text = changelog.read_text(encoding="utf-8")
        cleared = re.sub(
            r"(?ms)(^## Unreleased\s*\n).*?(?=^## )",
            r"\1\n",
            text,
            count=1,
        )
        changelog.write_text(cleared, encoding="utf-8")
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn(UNRELEASED_DRIFT_WARNING, result.stdout)

    def test_duplicate_id(self) -> None:
        duplicate = self.read_record()
        path = Path("data/field-tests/ft-001-copy.json")
        self.write_record(duplicate, path)
        ledger = self.repo / LEDGER
        text = ledger.read_text(encoding="utf-8")
        matching = next(line for line in text.splitlines() if RECORD.name in line)
        ledger.write_text(
            text + "\n" + matching.replace(RECORD.name, path.name) + "\n",
            encoding="utf-8",
        )
        shutil.copy2(
            self.repo / REPORT,
            self.repo / "research/field-tests/ft-001-copy.md",
        )
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
        ledger.write_text(
            text.replace(matching, matching + "\n" + matching, 1),
            encoding="utf-8",
        )
        self.assert_failed_with("found 2")

    def test_version_mismatch_in_report(self) -> None:
        self.replace(REPORT, VERSION, "1111111")
        self.assert_failed_with(
            f"kit_version {VERSION} is missing from research/field-tests"
        )

    def test_version_mismatch_in_ledger(self) -> None:
        self.replace(LEDGER, VERSION, "1111111")
        self.assert_failed_with(
            f"kit_version {VERSION} is missing from its CURRENT-EVIDENCE.md ledger row"
        )

    def test_public_safe_artifact_version_mismatch(self) -> None:
        self.replace(
            REPORT,
            ARTIFACT_VERSION,
            "FT-001-integrated-v0.1-wrong",
        )
        self.assert_failed_with(
            f"public-safe artifact_version '{ARTIFACT_VERSION}' is missing"
        )

    def test_unreachable_commit_in_full_clone_is_error(self) -> None:
        self.set_version("deadbeef")
        self.init_git()
        self.assert_failed_with(
            "kit_version commit is unreachable in the full clone: deadbeef"
        )

    def test_unreachable_commit_in_shallow_clone_is_warning(self) -> None:
        self.set_version("deadbeef")
        self.init_git(shallow=True)
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("not verified because the checkout is shallow", result.stdout)

    def test_malformed_json(self) -> None:
        (self.repo / RECORD).write_text("{not json}\n", encoding="utf-8")
        self.assert_failed_with("invalid JSON: data/field-tests/ft-001-alchemy.json")

    def test_wrong_report_id(self) -> None:
        self.replace(REPORT, "| Record ID | FT-001 |", "| Record ID | FT-999 |")
        self.assert_failed_with("paired report Record ID does not match")

    def test_stray_version_does_not_clear_wrong_identity(self) -> None:
        self.replace(REPORT, VERSION, "1111111")
        report = self.repo / REPORT
        report.write_text(report.read_text() + f"\nEarlier unrelated commit: {VERSION}\n")
        self.assert_failed_with(f"kit_version {VERSION} is missing from research/field-tests")

    def test_artifact_version_suffix_is_mismatch(self) -> None:
        self.replace(REPORT, ARTIFACT_VERSION, ARTIFACT_VERSION + "-wrong")
        self.assert_failed_with(f"public-safe artifact_version '{ARTIFACT_VERSION}' is missing")

    def test_ledger_version_must_be_in_version_column(self) -> None:
        self.replace(LEDGER, f"| {VERSION} |", f"| 1111111 |")
        self.replace(LEDGER, "Maintainer's side,", f"Earlier commit {VERSION}; Maintainer's side,")
        self.assert_failed_with(f"kit_version {VERSION} is missing from its CURRENT-EVIDENCE.md ledger row")

    def test_commit_object_without_retained_ref_is_unreachable(self) -> None:
        self.init_git()
        tree = subprocess.check_output(["git", "rev-parse", "HEAD^{tree}"], cwd=self.repo, text=True).strip()
        commit = subprocess.check_output(
            ["git", "-c", "user.name=PureLand Test", "-c",
             "user.email=pureland-test@example.invalid", "commit-tree", tree,
             "-m", "unreferenced fixture"], cwd=self.repo, text=True,
        ).strip()
        self.set_version(commit)
        self.assert_failed_with(f"kit_version commit is unreachable in the full clone: {commit}")

    def test_commit_reachable_from_head_passes(self) -> None:
        self.init_git()
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=self.repo, text=True).strip()
        self.set_version(commit)
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("kit_version commit", result.stdout)

    def test_raw_repository_links_resolve_existing_files_and_anchors(self) -> None:
        index = self.repo / "llms.txt"
        with index.open("a") as stream:
            stream.write("\n[raw method](https://raw.githubusercontent.com/risaac09/pureland-fork-kit/main/METHOD.md#1-scope)\n")
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_raw_repository_links_reject_missing_files_fragments_and_escapes(self) -> None:
        index = self.repo / "llms.txt"
        original = index.read_text()
        for target, diagnostic in [
            ("missing-file.md", "broken local link"),
            ("METHOD.md#missing-section", "broken anchor"),
            ("../outside.md", "link escapes repository"),
        ]:
            with self.subTest(target=target):
                index.write_text(original + "\n[raw target](https://raw.githubusercontent.com/risaac09/pureland-fork-kit/main/" + target + ")\n")
                self.assert_failed_with(diagnostic)

    def test_other_raw_repositories_and_refs_remain_external(self) -> None:
        index = self.repo / "llms.txt"
        with index.open("a") as stream:
            for target in [
                "https://raw.githubusercontent.com/example/other/main/missing.md",
                "https://raw.githubusercontent.com/risaac09/pureland-fork-kit/88216c0/missing.md",
                "https://raw.githubusercontent.com/risaac09/pureland-fork-kit/main/",
            ]:
                stream.write("\n[external target](" + target + ")\n")
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_current_report_template_identity_and_version_pass(self) -> None:
        template = (SOURCE / "templates/field-test.md").read_text()
        identity = template.split("## Record identity and tested hypothesis\n", 1)[1].split("\n## ", 1)[0]
        identity = identity.replace("- Record ID (`record_id`):", "- Record ID (`record_id`): FT-001")
        identity = identity.replace("- Kit version or commit (`kit_version`):", f"- Kit version or commit (`kit_version`): {VERSION}")
        report = self.repo / REPORT
        text = re.sub(
            r"(?ms)^## Record identity and status\n.*?(?=^## )",
            "## Record identity and tested hypothesis\n" + identity + "\n",
            report.read_text(), count=1,
        )
        text = re.sub(
            r"(?m)^- Artifact:.*$",
            f"- Artifact ID: FT-001-public-report-and-record\n- Exact artifact version: {ARTIFACT_VERSION}",
            text, count=1,
        )
        report.write_text(text)
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
