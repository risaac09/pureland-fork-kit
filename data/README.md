# Data boundary

This directory contains public-safe schemas and structured field-test records, not participant data. Do not commit completed consent registers, recordings, transcripts, identifying information, contact details, confidential records, or protected community knowledge.

The [field-test schema](field-test.schema.json) implements the required record for method version 0.1. Schema conformance means the record carries the required fields and satisfies structural rules. It does not mean the method was completed, the evidence supports the hypothesis, or any construct has been validated.

## Validation dependency

Repository validation requires Python package `jsonschema` version 4.18 or newer for Draft 2020-12 schema and format checking:

```sh
python3 -m pip install "jsonschema>=4.18"
python3 scripts/check_repo.py
```

CI must install that dependency before running `scripts/check_repo.py`. The checker fails with an explicit message when the package is absent. It never skips schema validation.

Field-test JSON may be submitted only when every value is safe for public release. A partial execution may conform when it records incomplete work and an allowed non-completion status. It may not claim completion or turn absent outcome or rights evidence into favorable support.
