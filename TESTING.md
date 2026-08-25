# Testing

PureLand tests the method by trying to break it. A confirming story is not enough. Every test begins with a result that would count against the tested hypothesis.

## Testing program

| Stage | Purpose | Evidence status |
|---|---|---|
| Partial dry run | Check which required stations and record fields can be executed; surface design failures | One maintainer-side partial execution, FT-001 |
| Independent application | Test use outside the maintainer's own practice and orbit | None accepted |
| Second-reader comparison | Expose construct ambiguity and classification disagreement | None completed |
| Bounded adaptation follow-up | Observe benefit, burden, exposure, possible new harm, and durability after a change | One follow-up window open, no outcome yet |
| Cross-context comparison | Test whether findings survive different practices and settings | None completed |

## Before a test

Follow [FIELD-TESTING.md](FIELD-TESTING.md). Record:

1. the tested hypothesis, practice, measurement unit, boundary, boundary rationale, and plausible alternative boundary;
2. the walking person and each affected person or group;
3. the document-access set, denominator, exclusions, and time window;
4. the assessor relationship, second-reader plan, evidence available before analysis, and disconfirming condition;
5. one or more concrete actions from `stop`, `continue`, `question`, `correct`, `adapt`, or `refuse`;
6. the baseline, expected follow-up, and materiality rule for each action and affected party;
7. permission, rights-review, public-return, research-use, and AI-use status.

If a test includes participant material, the [facilitation protocol](PROTOCOL.md) and [rights and consent guide](RIGHTS-AND-CONSENT.md) control. Public testing does not override consent.

## During a test

- Keep missing evidence `unmeasurable`.
- Keep the four access readings separate.
- Keep consent, attribution, and meaningful return separate.
- Record burden, exposure, extractability, disagreement, participant objection, and bounding decisions by affected party.
- Mark every required station `complete`, `incomplete`, or `not-started`. Use `not-applicable` only when the recorded scope makes the station unnecessary.
- Mark Observe incomplete when a required human first-person observation did not occur.
- Use a second independent reader where practical.
- Do not treat contemplative categories as labels for participants.
- Do not calculate an average or composite score.

## After a test

Record each action's follow-up, the adaptation, intended benefit, possible new harm, observation window, review date, follow-up evidence, contestability result, rights result, and limits on causal interpretation. Apply the classification rule in [HYPOTHESIS.md](HYPOTHESIS.md).

A record with missing required stations may conform to the schema only as a partial execution. It cannot claim completion. A record with missing outcome or rights evidence must classify the hypothesis result as `unmeasurable`.

Use the [field-test template](templates/field-test.md) and structured [schema](data/field-test.schema.json). Accepted public-safe reports enter the [field-trial ledger](FIELD-TRIALS.md) as inspectable records, not endorsements.

## Version 0.2 evidence gate

Seek five to ten independent applications across at least three contexts. Use two readers where practical. Preserve disagreements, objections, failed adaptations, missing evidence, and instrument changes. Passing this research gate does not validate the method by itself.

## Current open tests

- Can a human complete the Observe station in a way that another person can inspect without turning first-person experience into an objective score?
- Does the full journey add enough value over the extraction check alone to justify its burden?
- Can the traceable construct distinguish missing provenance from intentional, accountable deletion?
- Can two readers bound the same practice and produce comparable denominators?
- Does the applied [PureLand](PURELAND.md) experience improve completion and report quality over the toolbox alone?
