#!/usr/bin/env python3
"""Read-only inventory of a person's own information ecosystem.

This is the instrument half of kit 0.2: a companion to the self-assessment
that Alchemy already runs, aimed at the surfaces nobody has ever enumerated.
See kit-02-instrument-<source id>.md for the instrument's grammar, what it
buys, and what it cannot establish. This file is the instrument's script,
described there in section 4.

What it is not: a scanner of your whole machine, a background watcher, or
an agent that acts. It reads only the surfaces you mark `yes` in a
permission record you write yourself, before its first read. It never
executes anything on your behalf and never runs unattended.

Two commands:

    python3 scripts/ecosystem_inventory.py --init PERMISSION_FILE
        Writes a blank permission record template. Reads and scans nothing.

    python3 scripts/ecosystem_inventory.py --permission-file PERMISSION_FILE \\
        --out OUTPUT.md [--notes-dir PATH] [--repo PATH ...] \\
        [--author NAME_OR_EMAIL] [--bookmarks-file PATH]
        Runs the scan and writes one Markdown file.

Removal: delete the permission file and the output file. Nothing else is
written anywhere.
"""

from __future__ import annotations

import argparse
import json
import shutil
import socket
import subprocess
import sys
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

VERSION = "0.1"

# Every surface this instrument names, whether or not it has a reader below.
# A surface with no reader is still accounted for: its status is
# `unmeasurable`, with the reason on the record, never silently skipped.
SURFACES = [
    "notes",
    "commits",
    "local-models",
    "bookmarks",
    "browser-history",
    "mail",
    "notifications",
    "screen-time",
    "photos",
    "physical-archive",
    "spiritual-archive",
    "relational-archive",
    "memory",
]

# Surfaces this script can actually read. Every other surface in SURFACES is
# named on purpose and reported `unmeasurable: no reader in this version`
# rather than left off the record.
IMPLEMENTED = {"notes", "commits", "local-models", "bookmarks"}

# These four are never scanned regardless of the permission decision. They
# enter the record only through the person's own written note, per the
# instrument's boundary on physical, spiritual, relational, and remembered
# material.
DESCRIBE_ONLY = {"physical-archive", "spiritual-archive", "relational-archive", "memory"}

DECISIONS = {"yes", "no", "not yet"}


def block_network() -> None:
    """Make any attempted network connection raise instead of succeeding.

    This guard proves the claim rather than asserting it: if anything in
    this script or an imported module ever tries to open a socket, the run
    stops loudly here rather than sending something silently.
    """

    def _blocked(*_args: Any, **_kwargs: Any) -> None:
        raise RuntimeError(
            "ecosystem_inventory.py blocked a network connection attempt; "
            "this instrument makes none by design"
        )

    socket.socket.connect = _blocked  # type: ignore[assignment]
    socket.socket.connect_ex = _blocked  # type: ignore[assignment]
    socket.create_connection = _blocked  # type: ignore[assignment]


def write_permission_template(path: Path) -> None:
    template = {
        "instrument_version": VERSION,
        "written_before_first_read": True,
        "instructions": (
            "Set each surface's decision to 'yes', 'no', or 'not yet'. A "
            "surface left 'not yet' is not read. The four archive rows "
            "cannot be scanned regardless of decision: write what you want "
            "on record in 'note' instead, or leave 'no' and say nothing."
        ),
        "surfaces": {
            surface: {"decision": "not yet", "note": ""} for surface in SURFACES
        },
    }
    path.write_text(json.dumps(template, indent=2) + "\n", encoding="utf-8")


def load_permission_record(path: Path) -> dict[str, Any]:
    record = json.loads(path.read_text(encoding="utf-8"))
    surfaces = record.get("surfaces", {})
    for surface in SURFACES:
        entry = surfaces.get(surface)
        if not isinstance(entry, dict) or entry.get("decision") not in DECISIONS:
            raise ValueError(
                f"permission record is missing a valid decision for '{surface}'; "
                "run --init to regenerate the template"
            )
    return record


def age_bucket(mtime: float, now: float) -> str:
    days = (now - mtime) / 86400
    if days < 30:
        return "under 30 days"
    if days < 180:
        return "30 to 180 days"
    return "over 180 days"


def read_notes(notes_dir: Path | None, read_log: list[str]) -> dict[str, Any]:
    if notes_dir is None:
        return {"status": "unmeasurable", "reason": "no --notes-dir given"}
    if not notes_dir.is_dir():
        return {"status": "unmeasurable", "reason": f"not a directory: {notes_dir}"}
    now = datetime.now(timezone.utc).timestamp()
    by_extension: dict[str, int] = {}
    by_age: dict[str, int] = {"under 30 days": 0, "30 to 180 days": 0, "over 180 days": 0}
    total = 0
    for entry in notes_dir.rglob("*"):
        if not entry.is_file():
            continue
        total += 1
        read_log.append(str(entry))
        ext = entry.suffix.lower() or "(no extension)"
        by_extension[ext] = by_extension.get(ext, 0) + 1
        by_age[age_bucket(entry.stat().st_mtime, now)] += 1
    return {
        "status": "demonstrated" if total else "reported",
        "denominator": total,
        "by_extension": by_extension,
        "by_age": by_age,
    }


def read_commits(
    repos: list[Path], author: str | None, read_log: list[str]
) -> dict[str, Any]:
    if not repos:
        return {"status": "unmeasurable", "reason": "no --repo given"}
    if not author:
        return {"status": "unmeasurable", "reason": "no --author given"}
    per_repo: dict[str, Any] = {}
    total_commits = 0
    total_by_author = 0
    for repo in repos:
        if not (repo / ".git").exists():
            per_repo[str(repo)] = {"status": "unmeasurable", "reason": "not a git repository"}
            continue
        read_log.append(f"git log --all (read-only): {repo}")
        all_count = _git_count(repo, ["log", "--all", "--oneline"])
        author_count = _git_count(repo, ["log", "--all", f"--author={author}", "--oneline"])
        total_commits += all_count
        total_by_author += author_count
        per_repo[str(repo)] = {
            "denominator": all_count,
            "by_named_author": author_count,
        }
    return {
        "status": "demonstrated" if total_commits else "reported",
        "denominator": total_commits,
        "by_named_author": total_by_author,
        "per_repo": per_repo,
    }


def _git_count(repo: Path, args: list[str]) -> int:
    try:
        result = subprocess.run(
            ["git", "-C", str(repo), *args],
            capture_output=True,
            text=True,
            check=True,
            timeout=30,
        )
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        return 0
    lines = [line for line in result.stdout.splitlines() if line.strip()]
    return len(lines)


def read_local_models(read_log: list[str]) -> dict[str, Any]:
    home = Path.home()
    candidates = {
        "ollama directory": home / ".ollama",
        "LM Studio (macOS)": home / "Library" / "Application Support" / "LMStudio",
        "LM Studio (Linux)": home / ".cache" / "lm-studio",
        "llama.cpp models dir": home / "llama.cpp" / "models",
    }
    found: dict[str, str] = {}
    for label, path in candidates.items():
        read_log.append(f"existence check only, no content read: {path}")
        if path.exists():
            found[label] = str(path)
    for binary in ("ollama", "llama-server", "llama-cli"):
        read_log.append(f"PATH lookup only: {binary}")
        located = shutil.which(binary)
        if located:
            found[f"{binary} on PATH"] = located
    return {
        "status": "demonstrated" if found else "reported",
        "denominator": len(candidates) + 3,
        "count": len(found),
        "found": found,
    }


def read_bookmarks(bookmarks_file: Path | None, read_log: list[str]) -> dict[str, Any]:
    if bookmarks_file is None:
        return {"status": "unmeasurable", "reason": "no --bookmarks-file given"}
    if not bookmarks_file.is_file():
        return {"status": "unmeasurable", "reason": f"not a file: {bookmarks_file}"}
    read_log.append(str(bookmarks_file))
    text = bookmarks_file.read_text(encoding="utf-8", errors="replace")
    hrefs = [
        segment.split('"', 1)[0]
        for segment in text.split('HREF="')[1:]
        if segment
    ]
    domains: dict[str, int] = {}
    for href in hrefs:
        domain = urllib.parse.urlparse(href).netloc or "(no domain)"
        domains[domain] = domains.get(domain, 0) + 1
    return {
        "status": "demonstrated" if hrefs else "reported",
        "denominator": len(hrefs),
        "unique_domains": len(domains),
        "top_domains": dict(sorted(domains.items(), key=lambda item: -item[1])[:10]),
    }


def render_report(
    permission_path: Path,
    permission_record: dict[str, Any],
    results: dict[str, dict[str, Any]],
    read_log: list[str],
    args: argparse.Namespace,
    started_at: datetime,
    finished_at: datetime,
) -> str:
    lines: list[str] = []
    lines.append("# Ecosystem inventory")
    lines.append("")
    lines.append(
        "This is a read-only, local count. It is not a score, a map, or a "
        "verdict. Every status below is `demonstrated`, `partly "
        "demonstrated`, `reported`, `unmeasurable`, or `intentionally "
        "absent`, per the instrument's own rule against combining them."
    )
    lines.append("")
    lines.append(f"- Instrument version: {VERSION}")
    lines.append(f"- Permission record: {permission_path}")
    lines.append(
        f"- Active time: {(finished_at - started_at).total_seconds():.1f} seconds "
        "(effort, recorded separately from elapsed calendar days)"
    )
    lines.append(f"- Run started: {started_at.isoformat()}")
    lines.append(f"- Run finished: {finished_at.isoformat()}")
    lines.append("")
    lines.append("## Permission record, as written before this run's first read")
    lines.append("")
    lines.append("| Surface | Decision | Note |")
    lines.append("|---|---|---|")
    for surface in SURFACES:
        entry = permission_record["surfaces"][surface]
        note = entry.get("note", "").replace("|", "/") or "(none)"
        lines.append(f"| {surface} | {entry['decision']} | {note} |")
    lines.append("")
    lines.append("## Per-surface result")
    lines.append("")
    for surface in SURFACES:
        entry = permission_record["surfaces"][surface]
        lines.append(f"### {surface}")
        lines.append("")
        if surface in DESCRIBE_ONLY:
            note = entry.get("note", "").strip()
            if entry["decision"] == "yes" and note:
                lines.append("- Status: reported (the person's own words; nothing here was measured)")
                lines.append(f"- Record: {note}")
            elif entry["decision"] == "no":
                lines.append("- Status: intentionally absent")
                lines.append(f"- Reason: {note or '(no reason given)'}")
            else:
                lines.append("- Status: unmeasurable")
                lines.append("- Reason: no decision or no note recorded")
            lines.append(
                "- This surface is never scanned. It enters only by the "
                "person's description or demonstration."
            )
            lines.append("")
            continue
        if entry["decision"] == "no":
            lines.append("- Status: intentionally absent")
            lines.append(f"- Reason: {entry.get('note') or 'declined by permission record'}")
            lines.append("")
            continue
        if entry["decision"] == "not yet":
            lines.append("- Status: unmeasurable")
            lines.append("- Reason: no decision recorded")
            lines.append("")
            continue
        # decision is "yes" past this point.
        if surface not in IMPLEMENTED:
            lines.append("- Status: unmeasurable")
            lines.append("- Reason: no reader implemented in this version of the instrument")
            lines.append("")
            continue
        result = results.get(surface, {"status": "unmeasurable", "reason": "not run"})
        for key, value in result.items():
            lines.append(f"- {key}: {value}")
        lines.append("")
    lines.append("## What this run cannot establish")
    lines.append("")
    lines.append(
        "- Whether any count above changed anything about the person's "
        "practical agency. Adapt and Report answer that question; this "
        "instrument only counts."
    )
    lines.append(
        "- Anything about a surface marked `no` or `not yet`. Absence here "
        "is a recorded boundary. It carries no favorable reading."
    )
    lines.append(
        "- Anything about the physical, spiritual, relational, or "
        "remembered material named above. Those enter only by the "
        "person's own account."
    )
    lines.append("")
    lines.append("## Self-check, printed on every run")
    lines.append("")
    lines.append(f"- What left this machine: nothing. Network connections were blocked for this run.")
    lines.append(f"- What it wrote: {args.out}")
    lines.append(f"- What it read ({len(read_log)} item(s)):")
    for item in read_log:
        lines.append(f"  - {item}")
    if not read_log:
        lines.append("  - (nothing; every surface was `no`, `not yet`, or unimplemented)")
    refused = [
        surface
        for surface in SURFACES
        if permission_record["surfaces"][surface]["decision"] != "yes"
        or (surface not in IMPLEMENTED and surface not in DESCRIBE_ONLY)
    ]
    lines.append(f"- What it refused to read ({len(refused)} surface(s)):")
    for surface in refused:
        lines.append(f"  - {surface}")
    lines.append(
        f"- Remove everything this run made: rm {args.permission_file} {args.out}"
    )
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    block_network()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--init", metavar="PERMISSION_FILE", help="write a blank permission template and exit")
    parser.add_argument("--permission-file", metavar="PATH")
    parser.add_argument("--out", metavar="PATH")
    parser.add_argument("--notes-dir", metavar="PATH")
    parser.add_argument("--repo", action="append", default=[], metavar="PATH")
    parser.add_argument("--author", metavar="NAME_OR_EMAIL")
    parser.add_argument("--bookmarks-file", metavar="PATH")
    args = parser.parse_args(argv)

    if args.init:
        init_path = Path(args.init)
        write_permission_template(init_path)
        print(f"Wrote a blank permission template to {init_path}.")
        print("Nothing was read. Edit it, then run with --permission-file.")
        return 0

    if not args.permission_file or not args.out:
        parser.error("--permission-file and --out are required unless --init is given")

    permission_path = Path(args.permission_file)
    permission_record = load_permission_record(permission_path)

    started_at = datetime.now(timezone.utc)
    read_log: list[str] = []
    results: dict[str, dict[str, Any]] = {}

    def decided_yes(surface: str) -> bool:
        return permission_record["surfaces"][surface]["decision"] == "yes"

    if decided_yes("notes"):
        results["notes"] = read_notes(
            Path(args.notes_dir) if args.notes_dir else None, read_log
        )
    if decided_yes("commits"):
        results["commits"] = read_commits(
            [Path(repo) for repo in args.repo], args.author, read_log
        )
    if decided_yes("local-models"):
        results["local-models"] = read_local_models(read_log)
    if decided_yes("bookmarks"):
        results["bookmarks"] = read_bookmarks(
            Path(args.bookmarks_file) if args.bookmarks_file else None, read_log
        )

    finished_at = datetime.now(timezone.utc)
    report = render_report(
        permission_path, permission_record, results, read_log, args, started_at, finished_at
    )
    out_path = Path(args.out)
    out_path.write_text(report, encoding="utf-8")
    print(f"Wrote {out_path}.")
    print(f"What left this machine: nothing. Remove everything with: rm {permission_path} {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
