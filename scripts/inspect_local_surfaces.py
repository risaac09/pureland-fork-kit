#!/usr/bin/env python3
"""Count direct folder entries behind a macOS sandbox. Fail closed elsewhere.

The worker exposes no command execution or content analysis interface.
Run --help for the permission file shape and limits.
"""

import argparse
import collections
import datetime as dt
import errno
import json
import os
from pathlib import Path
import re
import shlex
import stat
import subprocess
import sys


CHOICES = {"yes", "no", "not yet"}
BOUNDARY = "Other archives: physical, spiritual, relational, and remembered material require human description or demonstration."


def load_permissions(path):
    data = json.loads(path.read_text())
    if set(data) != {"window", "surfaces"} or not isinstance(data["surfaces"], list):
        raise ValueError("Expected window and surfaces.")
    if not isinstance(data["window"], str) or not data["window"].strip():
        raise ValueError("State the snapshot window.")
    ids = set()
    for row in data["surfaces"]:
        if set(row) != {"id", "path", "metadata", "content"}:
            raise ValueError("Each surface needs id, path, metadata, and content.")
        if not isinstance(row["id"], str) or not re.fullmatch(r"[a-z0-9-]{1,40}", row["id"]):
            raise ValueError("Use an opaque lowercase surface id.")
        if row["id"] in ids:
            raise ValueError("Duplicate surface id.")
        ids.add(row["id"])
        if row["metadata"] not in CHOICES or row["content"] not in CHOICES:
            raise ValueError("Choices are yes, no, or not yet.")
        if not isinstance(row["path"], str):
            raise ValueError("Path must be text.")
        if row["metadata"] == "yes" and not Path(row["path"]).is_absolute():
            raise ValueError("An approved metadata surface needs an absolute path.")
    return data


def scan_folder(path):
    """Inspect direct entries through a held directory descriptor; open no file content."""
    fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        root_stat = os.fstat(fd)
        counts = collections.Counter()
        excluded = collections.Counter()
        entries = sorted(os.listdir(fd))
        for name in entries:
            try:
                meta = os.stat(name, dir_fd=fd, follow_symlinks=False)
                if stat.S_ISLNK(meta.st_mode):
                    excluded["symlink"] += 1
                elif stat.S_ISDIR(meta.st_mode):
                    excluded["subdirectory"] += 1
                elif not stat.S_ISREG(meta.st_mode) or meta.st_dev != root_stat.st_dev:
                    excluded["special-or-other-device"] += 1
                else:
                    # Fixed bins avoid printing a sensitive extension as prose.
                    ext = Path(name).suffix.lower()
                    kind = {".md": "markdown", ".txt": "text", ".pdf": "pdf",
                            ".jpg": "image", ".jpeg": "image", ".png": "image"}.get(ext, "other")
                    counts[kind] += 1
            except OSError:
                excluded["unreadable-or-changed"] += 1
        return dict(sorted(counts.items())), dict(sorted(excluded.items())), len(entries)
    finally:
        os.close(fd)


def profile(surfaces, permission_record=None):
    # Read access covers executable support files plus the selected folders.
    # No process in this profile can write a source or establish a socket.
    q = lambda value: json.dumps(str(value))
    support = ["/System", "/usr/lib", sys.base_prefix, str(Path(sys.executable).resolve().parent)]
    rules = ["(version 1)", "(allow default)", "(deny network*)", "(deny file-write*)",
             "(deny file-read*)", "(allow file-read* " + " ".join("(subpath " + q(p) + ")" for p in support)
             + " (literal " + q(Path(__file__).resolve()) + ") (literal \"/dev/null\"))"]
    if permission_record:
        rules.append("(allow file-read* (literal " + q(permission_record) + "))")
    for row in surfaces:
        if row["metadata"] == "yes":
            rules.append("(allow file-read-metadata (subpath " + q(row["path"]) + "))")
            rules.append("(allow file-read-data (literal " + q(row["path"]) + "))")
    return "".join(rules)


def sandbox_command(policy, mode, payload):
    return ["/usr/bin/sandbox-exec", "-p", policy, sys.executable, "-I", "-B",
            str(Path(__file__).resolve()), mode, json.dumps(payload)]


def probe(payload):
    """Use synthetic targets before archive access. A denial must come from the OS."""
    import socket
    denied = 0
    for family, address in ((socket.AF_INET, ("127.0.0.1", 9)),
                            (socket.AF_INET6, ("::1", 9))):
        connection = None
        try:
            connection = socket.socket(family, socket.SOCK_STREAM)
            connection.connect(address)
        except OSError as exc:
            if exc.errno in (errno.EPERM, errno.EACCES):
                denied += 1
        finally:
            if connection:
                connection.close()
    try:
        fd = os.open(payload["canary"], os.O_WRONLY)
    except OSError as exc:
        if exc.errno in (errno.EPERM, errno.EACCES):
            denied += 1
    else:
        os.close(fd)
    return 0 if denied == 3 else 1


def worker(surfaces):
    results = []
    for row in surfaces:
        if row["metadata"] != "yes":
            results.append({"id": row["id"], "status": "unmeasurable", "reason": row["metadata"]})
            continue
        try:
            if os.path.realpath(row["path"]) != row["path"]:
                raise OSError("Refuse a source alias.")
            counts, excluded, candidates = scan_folder(row["path"])
            results.append({"id": row["id"], "status": "partly demonstrated" if excluded else "demonstrated",
                            "counts": counts, "excluded": excluded, "candidates": candidates,
                            "denominator": sum(counts.values())})
        except OSError:
            results.append({"id": row["id"], "status": "unmeasurable", "reason": "OS denied or source changed"})
    print(json.dumps(results, sort_keys=True))


def recorded_worker(payload):
    """Require the already-written permission record even on the internal route."""
    text = Path(payload["permission_record"]).read_text()
    if "Permission record written before directory enumeration." not in text:
        raise ValueError("Missing written permission record.")
    encoded = text.split("```json\n", 1)[1].split("\n```", 1)[0]
    if json.loads(encoded)["surfaces"] != payload["surfaces"]:
        raise ValueError("Permission record differs from worker input.")
    worker(payload["surfaces"])


def inspect(permission, output):
    data = load_permissions(permission)
    # These are lexical checks. Record permission before any source metadata read.
    approved = [row for row in data["surfaces"] if row["metadata"] == "yes"]
    for row in approved:
        path = Path(row["path"])
        if str(path) != row["path"] or ".." in path.parts:
            raise ValueError("Use a normalized absolute source path.")
        if path == Path(path.anchor):
            raise ValueError("Select a bounded folder.")
        if output == path or path in output.parents:
            raise ValueError("Output must stay outside every selected source.")
    if output.is_symlink() or output.parent != output.parent.resolve():
        raise ValueError("Output parent must be canonical.")
    # Exclusive creation preserves an existing result. The record precedes enumeration.
    fd = os.open(output, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    with os.fdopen(fd, "w") as report:
        report.write("# Private surface snapshot\n\nStatus: partial execution.\n\n")
        report.write("Permission input and window:\n\n```json\n" + json.dumps(data, indent=2) + "\n```\n\n")
        report.write("Snapshot UTC: " + dt.datetime.now(dt.timezone.utc).isoformat() + "\n\n")
        report.write("Launch directory: " + str(Path.cwd()) + "\n\n")
        report.write("Permission record written before directory enumeration.\n\n")
        report.flush()
        os.fsync(report.fileno())
        status, reads = "REFUSED: isolation rehearsal unavailable; no source enumerated.", "permission file; runtime support files"
        rehearsal_status = "Unavailable; no successful isolation rehearsal."
        exit_code = 2
        try:
            policy = profile(data["surfaces"], output)
            rehearsal = subprocess.run(sandbox_command(policy, "--probe", {"canary": str(output)}),
                                       capture_output=True, timeout=10)
            if rehearsal.returncode == 0:
                rehearsal_status = "OS denied IPv4 and IPv6 loopback connections and a write-open of the output canary."
                payload = {"surfaces": data["surfaces"], "permission_record": str(output)}
                counted = subprocess.run(sandbox_command(policy, "--worker", payload),
                                         capture_output=True, text=True, timeout=60)
                if counted.returncode == 0:
                    results = json.loads(counted.stdout)
                    report.write("Counts:\n\n```json\n" + json.dumps(results, indent=2) + "\n```\n\n")
                    status = "Completed one snapshot under OS network and write denial."
                    reads += "; direct entry names and stat metadata for approved folders (see permission record)"
                    exit_code = 0
                else:
                    status = "REFUSED: worker failed; selected directories may have been partially enumerated."
                    reads += "; selected directories may have been partially enumerated"
        except (OSError, ValueError, subprocess.TimeoutExpired, KeyboardInterrupt):
            status = "STOPPED: no complete snapshot; selected directories may have been partially enumerated."
            reads += "; selected directories may have been partially enumerated"
        display = os.path.relpath(output)
        check = (status + "\nRead: " + reads + ".\n"
                 "Wrote: " + display + " (private Markdown, mode 0600).\n"
                 "Refused: content; unapproved surfaces; recursion; symlinks; source writes; model execution.\n"
                 "Left the machine: no source payload sent by this script.\n"
                 "Isolation rehearsal: " + rehearsal_status + "\n"
                 "Scope limit: the script cannot govern sync clients or backups outside its processes.\n"
                 "Remove from launch directory: rm -- " + shlex.quote(display) + "\n" + BOUNDARY + "\n")
        report.write("Self-check:\n\n```text\n" + check + "```\n")
        print(check, end="")
        return exit_code


def main():
    # Worker entry points are internal. The launcher always rehearses the profile.
    if len(sys.argv) == 3 and sys.argv[1] == "--probe":
        return probe(json.loads(sys.argv[2]))
    if len(sys.argv) == 3 and sys.argv[1] == "--worker":
        # Requiring OS-denied sockets also blocks a direct unsandboxed worker call.
        if probe({"canary": str(Path(__file__).resolve())}) != 0:
            return 2
        try:
            recorded_worker(json.loads(sys.argv[2]))
        except (KeyError, IndexError, OSError, TypeError, ValueError):
            return 2
        return 0
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("permission", type=Path, help='JSON: {"window":"description","surfaces":[{"id":"notes","path":"absolute path","metadata":"yes|no|not yet","content":"yes|no|not yet"}]}')
    parser.add_argument("output", type=Path, help="New Markdown file in an existing private, unsynced directory")
    args = parser.parse_args()
    try:
        return inspect(args.permission.resolve(), args.output.absolute())
    except (OSError, ValueError, TypeError) as exc:
        print("REFUSED before enumeration: " + str(exc) + "\n"
              "Read: permission file and runtime support only.\n"
              "Wrote: nothing. Refused: every source. Left the machine: no source payload.\n"
              "Remove: no artifact created.\n" + BOUNDARY, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
