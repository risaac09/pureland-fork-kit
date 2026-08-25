#!/usr/bin/env python3
"""Run small, dependency-free integrity checks for the PureLand repository."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git"}
SELF = Path(__file__).resolve()

LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
ATTR_LINK = re.compile(r"\b(src|href|srcset)=(['\"])(.*?)\2")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
PLACEHOLDER = re.compile(r"\b(TODO|TBD|INSERT[_ -]?HERE)\b", re.IGNORECASE)

FIELD_TEST_SCHEMA = ROOT / "data" / "field-test.schema.json"

# Field-test records are free-text, first-person accounts of what a
# contributor found, including what is still open. data/README.md and
# CONTRIBUTING.md ask for exactly that ("PureLand needs documented
# disagreement more than applause"), so an honest "second reader: TBD" in a
# submitted record is content, not a placeholder left behind by mistake.
FIELD_TEST_RECORDS = ROOT / "data" / "field-tests"

# Entry points a reader (or a fork) actually lands on. Orphan detection asks
# whether every other content file is reachable from here by some chain of
# links, not just whether something happens to point at it.
LINK_ROOTS = {ROOT / "README.md", ROOT / "JOURNEY.md", ROOT / "BRIEF.md"}

# Files that are legitimately not woven into prose: citation metadata and a
# changelog are conventionally browsed directly, not linked from the text.
ORPHAN_ALLOWLIST = {ROOT / "CITATION.cff", ROOT / "CHANGELOG.md"}

# File types that carry repo content, subject to orphan detection. .github/
# is excluded below: GitHub discovers issue templates, PR templates, and
# workflows on its own, not through prose links, so it is not part of the
# "reachable from README" contract.
CONTENT_SUFFIXES = {".md", ".html", ".css", ".json", ".cff", ".svg"}

# File types scanned for TODO/TBD/INSERT_HERE placeholder tokens.
PLACEHOLDER_SUFFIXES = {".md", ".html", ".json", ".yml", ".yaml", ".py"}

# Keywords validate_against_schema() actually enforces. Anything else in the
# schema is either an annotation (below) or a rule this script cannot apply,
# and an unenforced rule is worse than an absent one: it reads as covered.
SUPPORTED_KEYWORDS = {
    "type",
    "required",
    "additionalProperties",
    "properties",
    "enum",
    "const",
    "minLength",
    "minItems",
    "items",
}

# Annotations carry no constraint, so ignoring them is correct, not a gap.
ANNOTATION_KEYWORDS = {
    "$schema",
    "$id",
    "title",
    "description",
    "$comment",
    "examples",
    "default",
}

JSON_TYPES = {
    "object": dict,
    "array": list,
    "string": str,
    "number": (int, float),
    "integer": int,
    "boolean": bool,
    "null": type(None),
}


def type_matches(value: object, expected: object) -> bool:
    names = expected if isinstance(expected, list) else [expected]
    for name in names:
        py = JSON_TYPES.get(name)
        if py is None:
            continue
        # bool is a subclass of int in Python; JSON does not agree.
        if name in ("number", "integer") and isinstance(value, bool):
            continue
        if isinstance(value, py):
            return True
    return False


def json_equal(value: object, expected: object) -> bool:
    """Compare two JSON values the way JSON Schema does, not the way Python does.

    The trap: Python treats True == 1 and False == 0, so a plain == would accept
    a record carrying "privacy_review": 1 or 1.0 against {"const": true}, which
    Draft 2020-12 rejects. privacy_review is this repo's privacy gate, so the
    loose comparison would open it. type_matches() above already guards the same
    bool/int confusion for the "type" keyword; const and enum need it too.
    """
    if isinstance(value, bool) != isinstance(expected, bool):
        return False
    if isinstance(value, list) and isinstance(expected, list):
        return len(value) == len(expected) and all(
            json_equal(item, other) for item, other in zip(value, expected)
        )
    if isinstance(value, dict) and isinstance(expected, dict):
        return value.keys() == expected.keys() and all(
            json_equal(value[name], expected[name]) for name in value
        )
    return value == expected


def unsupported_keywords(schema: object, where: str) -> list[str]:
    """Name any schema keyword this validator would silently ignore.

    Without this, adding pattern, maxLength, or oneOf to field-test.schema.json
    would publish a rule that nothing enforces while CI stayed green. Failing
    loudly here forces the choice: implement the keyword, or do not declare it.
    """
    errors: list[str] = []
    if not isinstance(schema, dict):
        return errors
    for name in schema:
        if name not in SUPPORTED_KEYWORDS and name not in ANNOTATION_KEYWORDS:
            errors.append(f"{where}: schema keyword '{name}' is declared but not enforced")
    # additionalProperties is enforced only in its boolean form. Given a
    # subschema, validate_against_schema() would ignore it, so the keyword
    # being on the supported list is not enough on its own.
    if isinstance(schema.get("additionalProperties"), dict):
        errors.append(f"{where}: additionalProperties as a subschema is declared but not enforced")
    for name, subschema in schema.get("properties", {}).items():
        errors.extend(unsupported_keywords(subschema, f"{where}.{name}"))
    if "items" in schema:
        errors.extend(unsupported_keywords(schema["items"], f"{where}[]"))
    return errors


def validate_against_schema(value: object, schema: dict, where: str) -> list[str]:
    """Validate one record against the subset of JSON Schema this repo uses.

    Deliberately hand-rolled: check_repo.py is dependency-free by design and CI
    installs nothing, so pulling in jsonschema would trade the property that
    makes this runnable anywhere for keywords the schema does not use. Enforces
    the nine keywords in SUPPORTED_KEYWORDS, which is what
    data/field-test.schema.json declares today; const and enum compare by JSON
    equality through json_equal(), not by Python ==. Any other keyword added to
    the schema later is reported by unsupported_keywords() rather than ignored.
    """
    errors: list[str] = []

    if "const" in schema and not json_equal(value, schema["const"]):
        errors.append(f"{where}: must be {json.dumps(schema['const'])}, got {json.dumps(value)}")
        return errors

    if "type" in schema and not type_matches(value, schema["type"]):
        errors.append(f"{where}: expected {schema['type']}, got {json.dumps(value)}")
        return errors

    if "enum" in schema and not any(json_equal(value, option) for option in schema["enum"]):
        errors.append(f"{where}: must be one of {schema['enum']}, got {json.dumps(value)}")
    if "minLength" in schema and isinstance(value, str) and len(value) < schema["minLength"]:
        errors.append(f"{where}: must be at least {schema['minLength']} character(s)")
    if "minItems" in schema and isinstance(value, list) and len(value) < schema["minItems"]:
        errors.append(f"{where}: must have at least {schema['minItems']} item(s)")

    if isinstance(value, list) and "items" in schema:
        for index, item in enumerate(value):
            errors.extend(validate_against_schema(item, schema["items"], f"{where}[{index}]"))

    if isinstance(value, dict):
        properties = schema.get("properties", {})
        for name in schema.get("required", []):
            if name not in value:
                errors.append(f"{where}: missing required field '{name}'")
        if schema.get("additionalProperties") is False:
            for name in value:
                if name not in properties:
                    errors.append(f"{where}: unexpected field '{name}'")
        for name, subschema in properties.items():
            if name in value:
                errors.extend(validate_against_schema(value[name], subschema, f"{where}.{name}"))

    return errors


def files(suffix: str) -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob(f"*{suffix}")
        if not any(part in IGNORED for part in path.parts)
    )


def content_files() -> list[Path]:
    """Every file subject to orphan detection: repo content, not tooling."""
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.suffix in CONTENT_SUFFIXES
        and not any(part in IGNORED for part in path.parts)
        and ".github" not in path.parts
    )


def slugify(heading: str) -> str:
    """Approximate GitHub's heading-to-anchor slug rule."""
    text = re.sub(r"[^\w\s-]", "", heading.strip().lower())
    return re.sub(r"\s+", "-", text)


def heading_slugs(text: str) -> set[str]:
    """Anchor slugs a Markdown file's own headings would produce.

    Duplicate headings get GitHub's -1, -2, ... suffix so a link that only
    resolves because of that suffix is still caught as valid.
    """
    seen: dict[str, int] = {}
    slugs: set[str] = set()
    for _, title in HEADING.findall(text):
        slug = slugify(title)
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        slugs.add(slug if count == 0 else f"{slug}-{count}")
    return slugs


def targets_in_attr(attr_name: str, raw: str) -> list[str]:
    """Split one src=/href=/srcset= attribute value into link targets.

    Only srcset packs multiple "url descriptor" entries separated by commas;
    src and href carry exactly one target, which may itself legally contain a
    comma (a query string, for instance), so it must not be comma-split.
    """
    if attr_name != "srcset":
        return [raw.strip()] if raw.strip() else []
    return [entry.strip().split()[0] for entry in raw.split(",") if entry.strip()]


def attr_targets(text: str) -> list[str]:
    """All src=/href=/srcset= link targets in one file's text."""
    return [
        target
        for match in ATTR_LINK.finditer(text)
        for target in targets_in_attr(match.group(1), match.group(3))
    ]


def check_targets(
    path: Path,
    raw_targets: list[str],
    text_by_path: dict[Path, str],
    errors: list[str],
    graph: dict[Path, set[Path]],
) -> None:
    for target in raw_targets:
        clean, _, fragment = target.partition("#")
        if not clean or clean.startswith(("http://", "https://", "mailto:", "data:", "//")):
            continue
        # A leading "/" is repo-root-relative (as GitHub treats it), not a
        # filesystem-root path. Path's "/" operator would otherwise discard
        # path.parent entirely and resolve against the real filesystem root.
        if clean.startswith("/"):
            resolved = (ROOT / clean.lstrip("/")).resolve()
        else:
            resolved = (path.parent / clean).resolve()
        if not resolved.is_relative_to(ROOT):
            errors.append(f"link escapes repository: {path.relative_to(ROOT)} -> {target}")
            continue
        if not resolved.exists():
            errors.append(f"broken local link: {path.relative_to(ROOT)} -> {target}")
            continue
        graph[path].add(resolved)
        if fragment and resolved.suffix == ".md":
            target_text = text_by_path.get(resolved)
            if target_text is None:
                target_text = resolved.read_text(encoding="utf-8")
                text_by_path[resolved] = target_text
            if fragment not in heading_slugs(target_text):
                errors.append(
                    f"broken anchor: {path.relative_to(ROOT)} -> {target} "
                    f"(no heading in {resolved.relative_to(ROOT)} produces #{fragment})"
                )


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    parsed: dict[Path, object] = {}
    for path in files(".json"):
        try:
            parsed[path] = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid JSON: {path.relative_to(ROOT)}: {exc}")

    # data/README.md tells contributors to "validate it against
    # field-test.schema.json", but nothing did: this check parsed JSON and
    # stopped, so a submission with privacy_review false, or carrying extra
    # identifying fields the schema forbids, passed CI green. The schema sets
    # the repo's privacy boundary, so it has to be enforced, not just published.
    schema = parsed.get(FIELD_TEST_SCHEMA)
    if schema is None:
        if FIELD_TEST_SCHEMA.exists():
            errors.append("field-test schema present but unreadable; cannot validate data/")
    else:
        errors.extend(
            unsupported_keywords(schema, FIELD_TEST_SCHEMA.relative_to(ROOT).as_posix())
        )
        # rglob, not glob: submitted records live in data/field-tests/, one
        # level below data/ itself. A non-recursive glob here would only ever
        # see the schema file and validate nothing.
        #
        # Assumption: every JSON file under data/ other than the schema is a
        # field-test record. That holds today. A data file of some other shape
        # would fail against this schema, so add a path filter here before
        # adding one.
        for path in sorted((ROOT / "data").rglob("*.json")):
            if path == FIELD_TEST_SCHEMA or path not in parsed:
                continue
            errors.extend(
                validate_against_schema(parsed[path], schema, path.relative_to(ROOT).as_posix())
            )

    # Links, anchors, and the reachability graph. HTML is scanned via
    # src=/href=/srcset= attributes, both in .html files and in raw HTML
    # embedded in Markdown (the README banner uses <picture>, <source>,
    # <img>, none of which markdown-link syntax would ever see).
    text_by_path: dict[Path, str] = {}
    for path in files(".md") + files(".html"):
        text_by_path[path] = path.read_text(encoding="utf-8")

    graph: dict[Path, set[Path]] = defaultdict(set)

    for path in files(".md"):
        text = text_by_path[path]
        check_targets(path, LINK.findall(text), text_by_path, errors, graph)
        check_targets(path, attr_targets(text), text_by_path, errors, graph)
        if PLACEHOLDER.search(text):
            errors.append(f"placeholder token: {path.relative_to(ROOT)}")

    for path in files(".html"):
        text = text_by_path[path]
        check_targets(path, attr_targets(text), text_by_path, errors, graph)

    # Placeholder tokens beyond Markdown. .py is included deliberately: this
    # script's own source is exempt, because the PLACEHOLDER pattern above
    # literally spells out TODO / TBD / INSERT_HERE and would otherwise flag
    # itself for doing its job, not for actually containing a placeholder.
    # data/field-tests/ records are exempt too: they are contributors' own
    # free-text accounts, and an honest "TBD" there is content, not litter.
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in PLACEHOLDER_SUFFIXES:
            continue
        if any(part in IGNORED for part in path.parts):
            continue
        if path == SELF or path.suffix == ".md" or FIELD_TEST_RECORDS in path.parents:
            continue
        text = text_by_path.get(path)
        if text is None:
            text = path.read_text(encoding="utf-8")
        if PLACEHOLDER.search(text):
            errors.append(f"placeholder token: {path.relative_to(ROOT)}")

    # Orphan detection: every content file should be reachable from README,
    # JOURNEY, or BRIEF by some chain of links. This is a warning, not a
    # failure. A few files are legitimately unlinked (see ORPHAN_ALLOWLIST),
    # and a good-faith field-test PR should never fail CI over an unrelated
    # file it cannot fix.
    reachable: set[Path] = set(LINK_ROOTS)
    queue = list(LINK_ROOTS)
    while queue:
        current = queue.pop()
        for target in graph.get(current, ()):
            if target not in reachable:
                reachable.add(target)
                queue.append(target)

    for path in content_files():
        if path in reachable or path in ORPHAN_ALLOWLIST:
            continue
        warnings.append(
            f"orphan: {path.relative_to(ROOT)} is not reachable from "
            f"README.md, JOURNEY.md, or BRIEF.md by any link"
        )

    required = [
        "LICENSE",
        "LICENSE.md",
        "README.md",
        "RESEARCH-STATUS.md",
        "FIELD-TRIALS.md",
        "JOURNEY.md",
        "BRIEF.md",
        "OFFERING.md",
    ]
    for name in required:
        if not (ROOT / name).is_file():
            errors.append(f"missing required file: {name}")

    if warnings:
        print("Repository check warnings (do not fail this check):")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("Repository checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Repository checks passed: {len(files('.md'))} Markdown files, "
        f"{len(files('.json'))} JSON files, {len(warnings)} warning(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
