# Field testing

This is the submission discipline for [the method](METHOD.md) and [testing protocol](TESTING.md). Field tests should try to break the primary hypothesis. Confirmation alone is weak evidence.

## Prepare one record

1. Assign a record ID, kit version, and test status.
2. Name the tested hypothesis, scope, instrument, walking person or role, assessor relationship, and second-reader status.
3. Name every affected person or group.
4. Define the practice, unit, boundary, boundary rationale, alternative boundary, artifact or surface set, denominator, exclusions, and document-access time window. An artifact denominator is not a person-level outcome.
5. List the evidence available before analysis and write one disconfirming condition.
6. Record permission and rights-review status before using participant material or executing a change.
7. Predefine at least one action: `stop`, `continue`, `question`, `correct`, `adapt`, or `refuse`. Record a baseline and planned follow-up for every action.

## Keep the required evidence separate

- Record each station's completion status. For the whole journey, record human Observe separately. An AI design analysis cannot complete it.
- Keep understandable, reachable, adaptable, and traceable access readings separate.
- Keep consent, attribution, and value-return reciprocity readings separate.
- For every affected party, record exposure, extractability, and shifted burden at baseline and follow-up.
- Keep disagreements and participant objections. `Not collected` is not agreement.
- Record the adaptation status, intended benefit, possible new harm, observation window, review date, and follow-up.
- Record whether the return is public, private, refused, or unmeasurable.
- Disclose AI assistance and complete a public privacy review.

Missing evidence stays `unmeasurable`. Do not calculate an average or composite score. Do not make a causal claim from a before-and-after impression.

## Submit matching Markdown and JSON

Complete the [Markdown field-test template](templates/field-test.md) and a JSON record that conforms to [data/field-test.schema.json](data/field-test.schema.json). Follow the repository's [public data boundary](data/README.md). The same facts should appear under the same labels. Do not hide required fields in one context paragraph.

Run:

```sh
python3 scripts/check_repo.py
```

The check enforces structure, not construct validity. A passing record can still be methodologically weak, mixed, defeated, or unmeasurable.

Submit the report and record as an issue or pull request. The maintainer adds accepted reports to [FIELD-TRIALS.md](FIELD-TRIALS.md) as evidence links, not endorsements. Current interpretation and open evidence stay in [CURRENT-EVIDENCE.md](CURRENT-EVIDENCE.md).

No participant recordings, transcripts, names, contact details, or protected community knowledge belong in a public report. Use a private result when the evidence cannot be made public safely.
