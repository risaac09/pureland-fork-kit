# Field testing

This is the operational discipline inside the [testing program](TESTING.md). It runs alongside [the journey](JOURNEY.md). Field tests try to break the method. Confirmation alone is weak evidence.

## Before use

Complete the matching sections in the [Markdown template](templates/field-test.md) and [JSON record](data/field-test.schema.json):

1. Record the record ID, kit version, test status, tested hypothesis, scope, instrument, and disconfirming condition.
2. Name the walking person or record that no human walker is present.
3. Name each affected person or group separately.
4. Record the assessor's relationship to the practice and the second reader's status and independence.
5. Define the practice, unit, boundary, boundary rationale, plausible alternative boundary, and how that alternative could change the reading.
6. Define the artifact or surface set used for document-access counts. List its items, denominator, exclusions, and time window.
7. List the evidence available before analysis.
8. Mark which stations the scope requires.
9. Predefine one or more concrete actions from `stop`, `continue`, `question`, `correct`, `adapt`, or `refuse`. Record the action baseline and expected follow-up.
10. Predefine the context-specific rule for a material increase in exposure, extractability, or shifted burden.
11. Record separate decisions for recording, retention, named-reviewer access, publication, the exact artifact version, research use, AI processing, and model training. Record community authority where it applies.

Do not submit private participant material. If the test includes participant material, the [facilitation protocol](PROTOCOL.md) and [rights and consent guide](RIGHTS-AND-CONSENT.md) control.

## During use

- Record each station as `not-started`, `incomplete`, `complete`, or `not-applicable`.
- Record required human Observe work as `performed` or `not-performed`. AI design analysis does not count as human Observe.
- Keep understandable, reachable, adaptable, and traceable readings separate.
- Keep consent, attribution, and meaningful-return readings separate.
- Record exposure, extractability, and burden for each affected party at baseline and follow-up.
- Preserve assessor disagreements, second-reader disagreements, and participant objections. Use explicit statuses when none were sought or none were recorded.
- Record correction, takedown, and refusal routes; review authority; withdrawal actions; and whether an affected person could use the routes.
- Keep missing evidence `unmeasurable`.
- Do not calculate an average or composite score.

## After use

Record:

- adaptation status, consent, execution evidence, intended benefit, and possible new harm;
- observation-window dates, review date, follow-up status, and follow-up evidence;
- each action's follow-up against its baseline;
- the classification and return disposition defined in [HYPOTHESIS.md](HYPOTHESIS.md);
- causal-claim status and competing explanations;
- AI assistance and the artifact-version public-safe review.

A structurally conforming record can document a partial execution. It cannot claim completion when a required station is incomplete or a required human Observe was not performed. Missing action-outcome or rights evidence makes the hypothesis result `unmeasurable`.

The public issue form is Stage 1 scoping only. Do not paste a completed report, structured record, evidence link, or protected detail into that issue. After any required private rights review, a report and JSON record may enter through a pull request only when the exact artifact versions have a `clear` public-safe decision. A private result, refusal, or `unmeasurable` outcome does not require a public report. The maintainer may add a cleared report to [FIELD-TRIALS.md](FIELD-TRIALS.md) with links. An entry is an inspectable record, not an endorsement.

## Minimum comparison for a tested change

Record an action baseline, the change, the intended benefit, a plausible new harm, the observation window, the action follow-up, and burden and exposure by affected party. A before-and-after impression does not establish that the change caused the result.

No participant recordings, transcripts, names, contact details, consent records, confidential records, client records, or protected community knowledge belong in a public report.
