"""Synthetic filesystem tests; successful OS isolation remains a separate gate."""

import contextlib
import io
import json
import os
from pathlib import Path
import stat
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import inspect_local_surfaces as scan


class LocalSurfaces(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1] / "work")
        self.root = Path(self.temp.name).resolve()
        self.source = self.root / "source"
        self.source.mkdir()
        self.permission = self.root / "permission.txt"
        self.output = self.root / "snapshot.txt"
        self.data = {"window": "Synthetic snapshot", "surfaces": [
            {"id": "selected", "path": str(self.source), "metadata": "yes", "content": "no"},
            {"id": "declined", "path": "/never-inspect-this", "metadata": "no", "content": "no"}]}
        self.save()

    def tearDown(self):
        self.temp.cleanup()

    def save(self):
        self.permission.write_text(json.dumps(self.data))

    def test_direct_counts_exclude_symlinks_directories_and_special_files(self):
        (self.source / "a.md").write_text("synthetic content")
        (self.source / "b.txt").write_text("synthetic content")
        (self.source / "nested").mkdir()
        (self.source / "alias").symlink_to(self.source / "a.md")
        os.mkfifo(self.source / "pipe")
        self.assertEqual(scan.scan_folder(self.source),
                         ({"markdown": 1, "text": 1}, {"special-or-other-device": 1, "subdirectory": 1, "symlink": 1}, 5))

    def test_counting_is_repeatable_and_preserves_source_bytes(self):
        file = self.source / "a.md"
        file.write_bytes(b"synthetic sentinel")
        before = file.stat()
        first = scan.scan_folder(self.source)
        self.assertEqual(first, scan.scan_folder(self.source))
        self.assertEqual(file.read_bytes(), b"synthetic sentinel")
        self.assertEqual(before.st_mtime_ns, file.stat().st_mtime_ns)

    def test_directory_descriptor_does_not_open_file_content(self):
        original = os.open
        calls = []
        def tracked(path, flags, *args, **kwargs):
            calls.append((path, flags))
            return original(path, flags, *args, **kwargs)
        (self.source / "private.md").write_text("synthetic only")
        with patch.object(scan.os, "open", tracked):
            scan.scan_folder(self.source)
        self.assertEqual(len(calls), 1)
        self.assertTrue(calls[0][1] & os.O_DIRECTORY)
        self.assertFalse(calls[0][1] & os.O_WRONLY)

    def test_no_and_not_yet_never_resolve_or_scan_paths(self):
        for choice in ("no", "not yet"):
            rows = [{"id": "declined", "path": "/never-inspect-this", "metadata": choice, "content": "no"}]
            with patch.object(scan.os.path, "realpath", side_effect=AssertionError), patch.object(scan, "scan_folder", side_effect=AssertionError):
                with contextlib.redirect_stdout(io.StringIO()) as output:
                    scan.worker(rows)
            self.assertEqual(json.loads(output.getvalue())[0]["status"], "unmeasurable")

    def test_bad_permission_rejected(self):
        for bad in ("YES", "true", True, None):
            self.data["surfaces"][0]["metadata"] = bad
            self.save()
            with self.assertRaises((ValueError, TypeError)):
                scan.load_permissions(self.permission)

    def test_duplicate_id_rejected(self):
        self.data["surfaces"][1]["id"] = "selected"
        self.save()
        with self.assertRaises(ValueError):
            scan.load_permissions(self.permission)

    def test_output_inside_source_rejected(self):
        with self.assertRaises(ValueError):
            scan.inspect(self.permission, self.source / "output.txt")
        self.assertEqual(list(self.source.iterdir()), [])

    def test_existing_output_preserved(self):
        self.output.write_text("keep")
        with self.assertRaises(FileExistsError):
            scan.inspect(self.permission, self.output)
        self.assertEqual(self.output.read_text(), "keep")

    def test_permission_is_written_before_isolation_or_source_read(self):
        def denied(*args, **kwargs):
            self.assertIn('"metadata": "yes"', self.output.read_text())
            return subprocess.CompletedProcess(args, 71, b"", b"denied")
        with patch.object(scan.subprocess, "run", denied), patch.object(scan, "scan_folder", side_effect=AssertionError):
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(scan.inspect(self.permission, self.output), 2)
        self.assertEqual(stat.S_IMODE(self.output.stat().st_mode), 0o600)
        self.assertIn("no source enumerated", self.output.read_text())

    def test_stop_prints_incomplete_result(self):
        with patch.object(scan.subprocess, "run", side_effect=KeyboardInterrupt):
            with contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(scan.inspect(self.permission, self.output), 2)
        self.assertIn("STOPPED", output.getvalue())
        self.assertIn("Remove from launch directory", output.getvalue())

    def test_profile_denies_network_and_writes_and_excludes_rejected_path(self):
        policy = scan.profile(self.data["surfaces"])
        self.assertIn("(deny network*)", policy)
        self.assertIn("(deny file-write*)", policy)
        self.assertNotIn("/never-inspect-this", policy)

    def test_internal_worker_refuses_missing_permission_record(self):
        with patch.object(scan, "worker", side_effect=AssertionError):
            with self.assertRaises(FileNotFoundError):
                scan.recorded_worker({"surfaces": self.data["surfaces"], "permission_record": str(self.output)})

    def test_internal_worker_refuses_changed_permission(self):
        self.output.write_text('```json\n{"surfaces":[]}\n```\nPermission record written before directory enumeration.')
        with patch.object(scan, "worker", side_effect=AssertionError):
            with self.assertRaises(ValueError):
                scan.recorded_worker({"surfaces": self.data["surfaces"], "permission_record": str(self.output)})


if __name__ == "__main__":
    (Path(__file__).resolve().parents[1] / "work").mkdir(exist_ok=True)
    unittest.main()
