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

FIELD_TEST_SCHEMA = ROOT / "data" / "field-test.schema.json"

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


def validate_against_schema(value: object, schema: dict, where: str) -> list[str]:
    """Validate one record against the subset of JSON Schema this repo uses.

    Deliberately hand-rolled: check_repo.py is dependency-free by design and CI
    installs nothing, so pulling in jsonschema would trade the property that
    makes this runnable anywhere for keywords the schema does not use. Covers
    exactly what data/field-test.schema.json declares: type, required,
    additionalProperties, properties, enum, const, minLength, minItems, items.
    """
    errors: list[str] = []

    if "const" in schema and value != schema["const"]:
        errors.append(f"{where}: must be {json.dumps(schema['const'])}, got {json.dumps(value)}")
        return errors

    if "type" in schema and not type_matches(value, schema["type"]):
        errors.append(f"{where}: expected {schema['type']}, got {json.dumps(value)}")
        return errors

    if "enum" in schema and value not in schema["enum"]:
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


def main() -> int:
    errors: list[str] = []

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
        for path in sorted((ROOT / "data").glob("*.json")):
            if path == FIELD_TEST_SCHEMA or path not in parsed:
                continue
            errors.extend(
                validate_against_schema(parsed[path], schema, path.relative_to(ROOT).as_posix())
            )

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

    required = ["LICENSE", "README.md", "RESEARCH-STATUS.md", "FIELD-TRIALS.md"]
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
