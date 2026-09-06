#!/usr/bin/env python3
"""Count the surfaces of one person's own information ecosystem, on their machine.

    python3 scripts/ecosystem_inventory.py --permissions PATH [--out PATH]

This is a proposal, not an instrument the kit has adopted. It exists because
the openness scorecard demands a unit, a set, a time window, and a denominator
before anything is counted, and in the self lane nobody has ever supplied them.
It supplies denominators. It settles nothing else.
https://risaac09.github.io/pureland-fork-kit/CURRENT-EVIDENCE.md caps what this
kit has shown, and a count does not raise that cap.

What it does
------------
Reads only the surfaces named `yes` in a permission record the person writes
first. Reads names, sizes, and modification times. Never opens a file. Writes
one Markdown file and changes nothing else. Makes no network call, and proves
it: an audit hook armed before it reads anything raises on every socket,
urllib, ssl, http, and ftp event, so a run that reached the network would end
in a traceback instead of a report.

What it refuses
---------------
It never acts on the person's behalf, never offers to, and never watches in the
background. One run, one report, and it exits. It produces no score, no map, no
band, no verdict, and no ranking. It reads no surface the person did not mark,
and it reads no private or undocumented data store, because a read nobody can
describe cannot be honestly named in a permission record.

Statuses
--------
A walk can report `demonstrated`, `partly demonstrated`, `unmeasurable`, and
`intentionally absent`. It never reports `reported`, because reporting is
something a person does. A figure the person wrote stays in the estimate
column, where it is visibly theirs.

The estimate column
-------------------
The permission record asks the person to write their own estimate of each count
before the run. What this instrument measures is the distance between that
estimate and the count, surface by surface. The distances are reported
separately and are never added, averaged, or turned into a figure about the
person. If the estimates match the counts, the counting added nothing that the
person could not already say, and the instrument has failed its own test.

What it cannot establish
------------------------
A count of one machine is not an ecosystem. It says nothing about whether
anybody's attention improved, nothing about the archives that are physical,
remembered, relational, or held in practice, and nothing about what any of it
means. Those enter by the person's own description. This file counts what a
directory walk can see and prints the boundary as its last row.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import stat
import sys
from pathlib import Path
from typing import Any

_NETWORK_PREFIXES = ("socket", "urllib", "ssl", "http", "ftplib", "smtplib")


def _refuse_network(event: str, args: object) -> None:
    """Raise on any audited network event.

    main() arms this before it reads anything. It is not armed at import,
    because an audit hook cannot be removed once added: arming it on import
    would take networking away from any process that merely imported this
    module, which is a side effect this script has no business causing.
    """
    if event.split(".")[0] in _NETWORK_PREFIXES:
        raise RuntimeError(
            f"ecosystem_inventory made a network call ({event}). "
            "This script is local only and the run is void."
        )


WALK_CAP = 200_000
RECENT_DAYS = 365
PERMISSIONS = ("yes", "no", "not-yet", "absent")

TEMPLATE = """# PureLand ecosystem inventory: permission record
#
# Nothing is read until this file says so. Write it yourself. It is the record
# of what you allowed, and it is written before the first read on purpose.
#
# One surface per line, five columns separated by a pipe:
#
#   surface | permission | target | estimate | note
#
# surface     A name. Handlers exist for: files, notes, models. Any other name
#             is recorded unmeasurable, because nothing here can count it.
# permission  yes, no, not-yet, or absent.
#               yes      read this target: names, sizes, modification times
#               no       do not read it. The surface is recorded unmeasurable
#               not-yet  undecided. The surface is recorded unmeasurable
#               absent   this surface is not part of your life, on purpose.
#                        Write the reason in the note column
# target      An absolute path, or - when there is nothing to read
# estimate    Your own guess at the count, written before you run this, or -
# note        Your reason. Required for absent, optional everywhere else
#
# Write the estimate first. What this run measures is the distance between your
# estimate and the count, one surface at a time. Those distances are never
# added together and never become a figure about you.
#
# A `no` is a complete answer. It yields unmeasurable and never a failure.

files  | not-yet | - | - |
notes  | not-yet | - | - |
models | not-yet | - | - |
"""

HANDLERS: dict[str, dict[str, Any]] = {
    "files": {
        "suffixes": None,
        "rule": "Every regular file under {target}. Symlinks are not followed.",
    },
    "notes": {
        "suffixes": {".md", ".txt", ".org", ".markdown"},
        "rule": "Every regular file under {target} whose suffix is .md, .markdown, .txt, or .org. "
        "Symlinks are not followed.",
    },
    "models": {
        "suffixes": {".gguf", ".safetensors", ".bin"},
        "rule": "Every regular file under {target} whose suffix is .gguf, .safetensors, or .bin. "
        "Symlinks are not followed.",
    },
}


class Surface:
    def __init__(self, name: str, permission: str, target: str, estimate: str, note: str) -> None:
        self.name = name
        self.permission = permission
        self.target = target
        self.estimate = estimate
        self.note = note
        self.status = "unmeasurable"
        self.detail = ""
        self.rule = "No read was attempted."
        self.count: int | None = None
        self.recent: int | None = None
        self.unreadable = 0


def parse_permissions(path: Path) -> list[Surface]:
    surfaces: list[Surface] = []
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        # maxsplit keeps a pipe inside the note where the person put it.
        parts = [cell.strip() for cell in line.split("|", 4)]
        if len(parts) < 4:
            raise SystemExit(f"{path}:{number}: expected at least four columns, found {len(parts)}")
        parts += [""] * (5 - len(parts))
        name, permission, target, estimate, note = parts[:5]
        if permission not in PERMISSIONS:
            raise SystemExit(
                f"{path}:{number}: permission {permission!r} is not one of {', '.join(PERMISSIONS)}"
            )
        surfaces.append(Surface(name, permission, target, estimate, note))
    return surfaces


def key(path: str) -> str:
    """A comparable form of a path, case-folded because macOS filesystems are."""
    return os.path.normcase(os.path.realpath(path))


OWN_REPORT = re.compile(r"^ecosystem-inventory-\d{4}-\d{2}-\d{2}\.md$")


def walk(root: Path, suffixes: set[str] | None, excluded: set[str]) -> dict[str, int]:
    """Count matching regular files and everything the walk could not see.

    Returns the count, how many changed recently, how many files refused a
    read, how many directories refused a listing, and whether the walk was cut
    short. A directory nobody could list may hide any number of files, so it is
    counted apart from a single unreadable file and never folded into it.
    """
    cutoff = dt.datetime.now().timestamp() - RECENT_DAYS * 86400
    total = recent = unreadable = seen = 0
    unlistable = []

    def note_error(_error: OSError) -> None:
        unlistable.append(1)

    for directory, subdirectories, names in os.walk(root, followlinks=False, onerror=note_error):
        subdirectories[:] = [
            name for name in subdirectories if not os.path.islink(os.path.join(directory, name))
        ]
        for name in names:
            seen += 1
            if seen > WALK_CAP:
                return {
                    "count": total,
                    "recent": recent,
                    "unreadable": unreadable,
                    "unlistable": len(unlistable),
                    "truncated": 1,
                }
            entry = os.path.join(directory, name)
            if os.path.islink(entry):
                continue
            if key(entry) in excluded or OWN_REPORT.match(name):
                continue
            if suffixes is not None and os.path.splitext(name)[1].lower() not in suffixes:
                continue
            try:
                info = os.stat(entry)
            except OSError:
                unreadable += 1
                continue
            # A FIFO, socket, or device node is not a document. The rule printed
            # beside the count says regular files, so count regular files.
            if not stat.S_ISREG(info.st_mode):
                continue
            total += 1
            if info.st_mtime >= cutoff:
                recent += 1
    return {
        "count": total,
        "recent": recent,
        "unreadable": unreadable,
        "unlistable": len(unlistable),
        "truncated": 0,
    }


def measure(surface: Surface, excluded: set[str]) -> None:
    if surface.permission == "absent":
        if surface.note:
            surface.status = "intentionally absent"
            surface.detail = surface.note
        else:
            surface.status = "unmeasurable"
            surface.detail = "recorded absent with no reason, and an absence without its reason is not a boundary"
        return
    if surface.permission in ("no", "not-yet"):
        # A `no` yields unmeasurable and never a failure. An estimate beside it
        # stays the person's own figure and does not become a measurement.
        surface.status = "unmeasurable"
        surface.detail = "declined" if surface.permission == "no" else "undecided"
        return

    handler = HANDLERS.get(surface.name)
    if handler is None:
        surface.detail = f"no handler counts a surface named {surface.name!r}"
        return
    root = Path(os.path.expanduser(surface.target)).resolve()
    if surface.target in ("", "-") or not root.is_dir():
        surface.detail = f"target {surface.target!r} is not a readable directory"
        return

    surface.rule = str(handler["rule"]).format(target=root) + (
        " This tool's own permission record and its reports, named "
        "ecosystem-inventory-<date>.md, are excluded."
    )
    walked = walk(root, handler["suffixes"], excluded)
    surface.count, surface.recent = walked["count"], walked["recent"]
    surface.unreadable = walked["unreadable"] + walked["unlistable"]
    notes = []
    if walked["truncated"]:
        notes.append(f"stopped after {WALK_CAP} entries, so the count is a floor")
    if walked["unreadable"]:
        was = "file refused a read" if walked["unreadable"] == 1 else "files refused a read"
        notes.append(f"{walked['unreadable']} {was}")
    if walked["unlistable"]:
        was = "location refused" if walked["unlistable"] == 1 else "locations refused"
        notes.append(
            f"{walked['unlistable']} {was} to be listed, and each may hide any number of files"
        )
    if notes:
        surface.status = "partly demonstrated"
        surface.detail = "; ".join(notes)
    else:
        surface.status = "demonstrated"


def cell(value: object) -> str:
    return "" if value is None or value == "" else md(str(value))


def md(value: str) -> str:
    """Escape a pipe so one in a path or a note cannot break the table."""
    return value.replace("|", "\\|")


def given(value: str) -> str:
    """An estimate the person actually wrote. A dash means they wrote none."""
    return "" if value.strip() in ("", "-") else value.strip()


def report(surfaces: list[Surface], permissions: Path) -> str:
    stamp = dt.date.today().isoformat()
    lines = [
        "# Ecosystem inventory",
        "",
        f"Run on {stamp} against the permission record at `{permissions}`.",
        "",
        "This is a count of surfaces on one machine. It is not an ecosystem, not a score, and not a",
        "reading. It shows what a directory walk could see where this person allowed one, and it",
        "shows nothing about their attention. The counts describe this machine on this date under",
        "the enumeration rule printed beside each one, and they describe nothing else.",
        "",
        "## Surfaces",
        "",
        "| Surface | Status | Counted | Modified in the last 365 days | Estimated first | Enumeration rule |",
        "|---|---|---|---|---|---|",
    ]
    for surface in surfaces:
        lines.append(
            f"| {md(surface.name)} | {surface.status} | {cell(surface.count)} | "
            f"{cell(surface.recent)} | {cell(given(surface.estimate))} | {md(surface.rule)} |"
        )
    lines += [
        "",
        "Read each row on its own. The distance between an estimate and a count belongs to that",
        "surface. Adding or averaging those distances would make the composite every instrument in",
        "this kit refuses.",
        "",
        "## What each status means",
        "",
    ]
    for surface in surfaces:
        if surface.detail:
            lines.append(
                f"- **{md(surface.name)}**: {surface.status}. {md(surface.detail).rstrip('.')}."
            )
        else:
            lines.append(f"- **{md(surface.name)}**: {surface.status}.")

    models = [s for s in surfaces if s.name == "models" and s.count]
    lines += ["", "## The audited unit, where a model was found", ""]
    if models:
        lines += [
            "Running a model on hardware you own closes the deployment-configuration and logs rows of",
            "the AI system annex's table with first-hand evidence. It closes those two rows. This run",
            "found local weight files and can evidence their location. Every other row of that table",
            "stays `unknown` until a person fills it.",
        ]
    else:
        lines.append("No local weight files were counted. Every row of the annex table stays `unknown`.")

    lines += [
        "",
        "## What no script reached",
        "",
        "The physical archive, the spiritual archive, the relational record, and memory are not",
        "scannable and were not scanned. A shelf, a practice, an obligation, and a thing somebody",
        "remembers enter this record only by the person's own description or demonstration. Nothing",
        "here asks anyone to digitize any of them, and their absence from this table is a property of",
        "the table.",
        "",
    ]
    return "\n".join(lines) + "\n"


def self_check(surfaces: list[Surface], written: list[Path]) -> str:
    read = [s.target for s in surfaces if s.permission == "yes" and s.count is not None]
    refused = [
        f"{s.name} ({s.permission})"
        for s in surfaces
        if s.permission in ("no", "not-yet", "absent")
    ]
    # A surface the person allowed that nothing here could count is also unread.
    # Reporting only the declines would let the self-check overstate what it did.
    refused += [
        f"{s.name} (allowed, {s.detail})"
        for s in surfaces
        if s.permission == "yes" and s.count is None
    ]
    removal = " ".join(f"'{path}'" for path in written)
    return "\n".join(
        [
            "",
            "Self-check for this run",
            "-----------------------",
            "  What left this machine:  nothing. The network audit hook was armed before this run",
            "                           read anything, and it raises on every socket, urllib, ssl,",
            "                           http, and ftp event. This run finished, so none fired.",
            f"  What it read:            {', '.join(read) if read else 'nothing'}",
            "                           Names, sizes, and modification times. No file was opened.",
            f"  What it refused:         {', '.join(refused) if refused else 'nothing was declined'}",
            f"  What it wrote:           {', '.join(str(p) for p in written)}",
            "  What it changed:         nothing in any source directory.",
            f"  Remove everything it made:  rm {removal}",
            "",
        ]
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--permissions", required=True, help="path to the permission record")
    parser.add_argument("--out", default=None, help="path for the report (default: beside the record)")
    args = parser.parse_args(argv)

    sys.addaudithook(_refuse_network)

    permissions = Path(os.path.expanduser(args.permissions))
    if not permissions.exists():
        permissions.parent.mkdir(parents=True, exist_ok=True)
        permissions.write_text(TEMPLATE, encoding="utf-8")
        print("No permission record existed, so nothing was read.")
        print(f"A blank one is now at {permissions}. Fill it in and run this again.")
        print(f"Remove it with:  rm '{permissions}'")
        return 2

    surfaces = parse_permissions(permissions)
    if not surfaces:
        print(f"{permissions} names no surfaces. Nothing was read.")
        return 2

    out = Path(os.path.expanduser(args.out)) if args.out else permissions.with_name(
        f"ecosystem-inventory-{dt.date.today().isoformat()}.md"
    )
    # This script writes one file and overwrites nothing. Refusing here is what
    # makes the self-check's "changed nothing" line true rather than hopeful.
    if key(str(out)) == key(str(permissions)):
        print("The report would overwrite the permission record. Choose another --out.")
        return 2
    if out.exists():
        print(f"{out} already exists and this script overwrites nothing.")
        print(f"Remove it or pass another --out:  rm '{out}'")
        return 2
    # The report and the permission record can sit inside a counted directory,
    # which is the obvious layout for a notes surface. Counting them would let
    # this tool's own output inflate the next run's denominator.
    excluded = {key(str(permissions)), key(str(out))}
    for surface in surfaces:
        measure(surface, excluded)

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report(surfaces, permissions), encoding="utf-8")
    print(self_check(surfaces, [out]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
