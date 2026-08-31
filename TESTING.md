# Testing

PureLand tests the method by trying to break it. A confirming story is not enough. Every test begins with a result that would count against the tested hypothesis.

This document holds the claim and the work of testing it: the primary hypothesis, the constructs a test must look for, the rule for classifying a result, the testing program that says what stage the evidence is at, and the discipline a single test follows before, during, and after use. The journey walks alongside it. [Ground](JOURNEY.md#1-ground) uses the before-use section, and [Return](JOURNEY.md#6-return) uses the after-use section.

## Primary hypothesis

[THESIS.md](THESIS.md) describes the shape of the work. The hypothesis makes a claim that field evidence can weaken or defeat.

> When a person walks the PureLand method on one bounded information practice and tests one contestable adaptation, their practical agency can improve without a material increase in exposure, extractability, or shifted burden.

This is a working hypothesis, not a demonstrated effect. It is untested as an outcome claim. [FT-001](research/field-tests/ft-001-alchemy.md) is a maintainer-side partial dry run. It produced an assessor interpretation about analytic value. It did not test a person-level agency or attention-sovereignty outcome. See [CURRENT-EVIDENCE.md](CURRENT-EVIDENCE.md).

## Secondary claims

The [research-status ledger](RESEARCH-STATUS.md) carries every other claim the kit makes, each with its status and the evidence it still needs, so a revision moves a claim once. One secondary claim is tested here and recorded nowhere else: one bounded adaptation can increase a person's control over their attention. Each claim can fail on its own, and evidence for one does not validate the others.

## Provisional constructs, version 0.1

These are construct definitions. They specify what a test must look for. They are not validated measures, scales, thresholds, or evidence that the constructs move together.

| Construct | Provisional definition | Required observation |
|---|---|---|
| Practical agency | A named person's ability to carry out a concrete action concerning the bounded practice | Predefine one or more actions from `stop`, `continue`, `question`, `correct`, `adapt`, or `refuse`; record a baseline and follow-up for each action |
| Attention sovereignty | A person's practical ability to direct, withhold, resume, and end attention under terms they can understand and contest | Record action-level evidence, attention conditions, manufactured or real costs of stopping, and the person's own challenge; do not infer it from document access |
| Exposure | The people or systems newly able to see, receive, link, retain, or act on a person's information, behavior, or participation | Record scope, duration, permission, reversibility, and affected party before and after the adaptation |
| Extractability | The ease with which material or behavior can be copied, aggregated, inferred from, transferred, monetized, or reused beyond the immediate practice | Record the extraction path, recipient, permitted purpose, possible reuse, and affected party before and after the adaptation |
| Shifted burden | Time, money, attention, work, risk, or relational cost moved from one party to another | Record each burden by affected party, including who gains authority and who must do more work |
| Material increase | A context-specific increase large enough to change safety, rights, cost, access, or the practical ability to act | Predefine the qualitative or quantitative materiality rule before analysis; do not import one universal threshold |
| Contestability | Affected people can understand the reading, object or correct it, refuse participation or return, reach a review authority, and receive a usable response | Record the correction route, refusal route, review authority, timeliness, accessibility, and whether an affected person used or challenged the route |
| Meaningful return | Benefit, knowledge, control, credit, or resources reach the people whose participation or material generated value, in a permitted form they can recognize and use | Record what returned, to whom, under whose permission, and whether the receiving party regarded it as useful; publication alone is not return |

Each instrument reading remains separate. A construct definition does not become a validated measure because it appears in the schema. The result is a profile, not one score. The per-stage sections below say what a test records against each construct.

## Classification rule

Classify the tested context only after recording the complete profile:

1. Evidence may support the hypothesis only for the bounded practice, walking person, affected parties, actions, and observation window tested.
2. Missing required action-outcome evidence or rights evidence makes the hypothesis result `unmeasurable`.
3. A material increase in exposure, extractability, or shifted burden weakens or defeats the hypothesis for that context, even when an access reading improves.
4. An unusable correction or refusal route weakens the hypothesis. An absent route cannot support it.
5. Conflicting dimensions remain `mixed`. Do not average them into a favorable result.
6. A before-and-after impression is not a causal claim. Record the adaptation, timing, evidence, and competing explanations.
7. A refusal, private result, or `unmeasurable` result is valid evidence about the method. Absence never defaults to favorable.

Allowed classifications are `supports-tested-context`, `weakens-tested-context`, `defeats-tested-context`, `mixed`, and `unmeasurable`. Return disposition is recorded separately as `public-return`, `private-result`, `refusal`, `unmeasurable`, or `pending-follow-up`.

## Disconfirming results

Any of these results should weaken or defeat the primary hypothesis for the tested context:

- the method produces no useful reading beyond an ordinary review of the same evidence;
- the adaptation increases legibility for the assessor while increasing exposure for an affected person;
- safeguards mainly reduce institutional liability while shifting material burden to participants;
- the person cannot stop, refuse, correct, or challenge the reading in practice;
- missing evidence is converted into a favorable result;
- the return is meaningful to the maintainer but not to the people who generated the value;
- independent readers cannot use the constructs consistently enough to support the stated interpretation;
- the burden of the full journey is not justified by what it adds over a smaller instrument.

## Testing program

| Stage | Purpose | Evidence status |
|---|---|---|
| Partial dry run | Check which required stations and record fields can be executed; surface design failures | One maintainer-side partial execution, FT-001 |
| Independent application | Test use outside the maintainer's own practice and orbit | None accepted |
| Second-reader comparison | Expose construct ambiguity and classification disagreement | None completed |
| Bounded adaptation follow-up | Observe benefit, burden, exposure, possible new harm, and durability after a change | One follow-up window open, no outcome yet |
| Cross-context comparison | Test whether findings survive different practices and settings | None completed |

This table cuts the record by stage. The [ledger](CURRENT-EVIDENCE.md#the-ledger) cuts it by trial and is the source, so an accepted trial changes the ledger row first and this column second.

## Before a test

Complete the matching sections in the [Markdown template](templates/field-test.md) and [JSON record](data/field-test.schema.json):

1. Record the record ID, kit version, test status, tested hypothesis, scope, instrument, and disconfirming condition.
2. Name the walking person, or record that no human walker is present.
3. Name each affected person or group separately.
4. Record the assessor's relationship to the practice, and the second reader's status and independence.
5. Define the practice, unit, boundary, boundary rationale, plausible alternative boundary, and how that alternative could change the reading.
6. Define the artifact or surface set used for document-access counts. List its items, denominator, exclusions, and time window.
7. List the evidence available before analysis.
8. Mark which stations the scope requires.
9. Predefine one or more concrete actions from `stop`, `continue`, `question`, `correct`, `adapt`, or `refuse`. Record the action baseline and expected follow-up.
10. Predefine the context-specific rule for a material increase in exposure, extractability, or shifted burden.
11. Record separate decisions for recording, retention, named-reviewer access, publication, the exact artifact version, research use, AI processing, and model training. Record community authority where it applies.

Do not submit private participant material. If a test includes participant material, the [facilitation protocol](PROTOCOL.md) and [rights and consent guide](RIGHTS-AND-CONSENT.md) control. Public testing does not override consent.

## During a test

- Record each station as `not-started`, `incomplete`, `complete`, or `not-applicable`. Use `not-applicable` only when the recorded scope makes the station unnecessary.
- Record required human Observe work as `performed` or `not-performed`. AI design analysis does not count as human Observe.
- Keep understandable, reachable, adaptable, and traceable readings separate. An artifact denominator is not a person count.
- Keep consent, attribution, and meaningful-return readings separate. A public artifact is not meaningful return.
- Record exposure, extractability, and burden for each affected party at baseline and follow-up.
- Preserve assessor disagreements, second-reader disagreements, and participant objections. Use explicit statuses when none were sought or none were recorded. Do not smooth conflict into agreement.
- Record correction, takedown, and refusal routes; review authority; withdrawal actions; and whether an affected person could use the routes.
- Use a second independent reader where practical.
- Keep missing evidence `unmeasurable`.
- Do not treat contemplative categories as labels for participants.
- Do not calculate an average or composite score.

## After a test

Record:

- adaptation status, consent, execution evidence, intended benefit, and possible new harm;
- observation-window dates, review date, follow-up status, and follow-up evidence;
- each action's follow-up against its baseline;
- the classification and return disposition defined by the [classification rule](#classification-rule);
- causal-claim status and competing explanations;
- the contestability result and the rights result;
- AI assistance and the artifact-version public-safe review.

A record with missing required stations may conform to the schema only as a partial execution. It cannot claim completion when a required station is incomplete or a required human Observe was not performed. Missing action-outcome or rights evidence makes the hypothesis result `unmeasurable`.

The review date is watched. A record left `open` or `not-started` past its own `review_date` raises a warning in `scripts/check_repo.py`, and a weekly scheduled run opens an issue against the repository. Close the window with an outcome, or record it as `closed-unmeasurable`. An expired window carried as open is missing evidence, and missing evidence never counts as favorable.

The public issue form is Stage 1 scoping only. Do not paste a completed report, structured record, evidence link, or protected detail into that issue. After any required private rights review, a report and JSON record may enter through a pull request only when the exact artifact versions have a `clear` public-safe decision. A private result, refusal, or `unmeasurable` outcome does not require a public report. The maintainer may add a cleared report to the [ledger in CURRENT-EVIDENCE.md](CURRENT-EVIDENCE.md#the-ledger) with links. An entry is an inspectable record, not an endorsement.

No participant recordings, transcripts, names, contact details, consent records, confidential records, client records, or protected community knowledge belong in a public report.

## Minimum comparison for a tested change

Record an action baseline, the change, the intended benefit, a plausible new harm, the observation window, the action follow-up, and burden and exposure by affected party. A before-and-after impression does not establish that the change caused the result.

## Provisional version 0.2 planning target

The current planning target is five to ten independent applications across at least three contexts, with two readers where practical. Those numbers are maintainer-chosen and have no derived empirical basis. Revise them when feasibility or design evidence warrants it. Preserve disagreements, objections, failed adaptations, missing evidence, and instrument changes. Do not tune only toward agreement. Meeting this target would not validate the method by itself.

This is the kit's single statement of the gate. [RESEARCH-STATUS.md](RESEARCH-STATUS.md) and [CURRENT-EVIDENCE.md](CURRENT-EVIDENCE.md) point here rather than restating the numbers, so a revision moves them once.

## Current open tests

- Can a human complete the Observe station in a way that another person can inspect without turning first-person experience into an objective score?
- Does the full journey add enough value over the extraction check alone to justify its burden?
- Can the traceable construct distinguish missing provenance from intentional, accountable deletion?
- Can two readers bound the same practice and produce comparable denominators?
- Does the full journey improve completion and report quality over a single-instrument entry?
