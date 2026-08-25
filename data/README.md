# Data boundary

This directory contains schemas, not participant data. Do not commit completed consent registers, recordings, transcripts, identifying information, or protected community knowledge.

Field-test JSON may be submitted only when every value is safe for public release. Use a private result when the required evidence cannot be published safely.

Each public record must match [field-test.schema.json](field-test.schema.json) and the labels in the [Markdown field-test template](../templates/field-test.md). The schema requires explicit missing, refused, private, and unmeasurable states so absence cannot become a favorable default. It carries the measurement boundary, evidence available before analysis, station status, action baselines and follow-ups, affected-party harms, rights review, disagreements, adaptation, outcome, AI assistance, and public privacy review.

Run `python3 scripts/check_repo.py`. The standard-library checker validates the schema structure, each JSON record, cross-field completion rules, and the repository links. Passing the check does not validate the constructs or the conclusion.
