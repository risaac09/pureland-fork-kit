#!/usr/bin/env python3
"""Run small, dependency-free integrity checks for the PureLand repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git"}
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
PLACEHOLDER = re.compile(r"\b(TODO|TBD|INSERT[_ -]?HERE)\b", re.IGNORECASE)


def files(suffix: str) -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob(f"*{suffix}")
        if not any(part in IGNORED for part in path.parts)
    )


def main() -> int:
    errors: list[str] = []

    for path in files(".json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid JSON: {path.relative_to(ROOT)}: {exc}")

    for path in files(".md"):
        text = path.read_text(encoding="utf-8")
        for target in LINK.findall(text):
            clean = target.split("#", 1)[0]
            if not clean or clean.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / clean).resolve()
            if ROOT not in resolved.parents and resolved != ROOT:
                errors.append(f"link escapes repository: {path.relative_to(ROOT)} -> {target}")
            elif not resolved.exists():
                errors.append(f"broken local link: {path.relative_to(ROOT)} -> {target}")
        if PLACEHOLDER.search(text):
            errors.append(f"placeholder token: {path.relative_to(ROOT)}")

    required = [
        "LICENSE",
        "README.md",
        "THESIS.md",
        "METHOD.md",
        "TOOLBOX.md",
        "HYPOTHESIS.md",
        "PURELAND.md",
        "TESTING.md",
        "RESULTS.md",
        "DISCUSSION.md",
        "CONCLUSION.md",
        "RESEARCH-STATUS.md",
        "FIELD-TRIALS.md",
    ]
    for name in required:
        if not (ROOT / name).is_file():
            errors.append(f"missing required file: {name}")

    if errors:
        print("Repository checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Repository checks passed: {len(files('.md'))} Markdown files, {len(files('.json'))} JSON files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
