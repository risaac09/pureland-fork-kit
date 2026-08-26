# Data maturity audit

Point-in-time audit of the kit's data layer at commit `a2044a9`, 2026-08-25. It reads the infrastructure that carries evidence: the boundary, the schema, the checker, the records, and the documents that must stay consistent with them. It does not read the evidence itself. [CURRENT-EVIDENCE.md](CURRENT-EVIDENCE.md) controls what the evidence permits, and nothing here upgrades it.

This audit is maintainer-side and AI-assisted. No second reader has checked it. By the kit's own standard, that limits what it can claim.

## Method

Each dimension gets one level on this ladder:

| Level | Name | Meaning |
|---|---|---|
| 0 | Absent | Nothing names the concern |
| 1 | Declared | A document states the rule |
| 2 | Structured | The schema or a template carries fields for it |
| 3 | Enforced | `scripts/check_repo.py` fails CI when a record violates it |
| 4 | Exercised | At least one real record has passed through the gate |
| 5 | Independently exercised | A contributor outside the maintainer's orbit has passed through it |

Levels stay separate. No overall grade is calculated, for the same reason the scorecard calculates no composite: a single number would hide exactly the differences that matter. A high level means the gate works, not that the construct behind it is validated.

No dimension is at level 5. The kit has no independent contribution, and says so.

## Readings

| Dimension | Level | Evidence |
|---|---|---|
| Data boundary | 4 | [data/README.md](data/README.md); schema `additionalProperties: false`; public-safe gating in the checker |
| Record structure | 4 | [field-test.schema.json](data/field-test.schema.json), Draft 2020-12, 31 required fields, validated in CI |
| Claim integrity | 4 | `check_record_rules` in [check_repo.py](scripts/check_repo.py) |
| Provenance binding | 2 | `kit_version`, `artifact_version`, version-scoped public-safe decisions |
| Record base | 4 | [FT-001](data/field-tests/ft-001-alchemy.json), one partial maintainer-side execution |
| Instrument coverage | 2 | `scope.instrument` enum; [issue 12](https://github.com/risaac09/pureland-fork-kit/issues/12) |
| Follow-up lifecycle | 2 | `follow_up` fields required; no overdue check |
| Cross-artifact consistency | 1 | [FIELD-TRIALS.md](FIELD-TRIALS.md), `research/`, `data/` hand-synchronized |
| Private-half custody | 2 | [RIGHTS-AND-CONSENT.md](RIGHTS-AND-CONSENT.md); [consent-register template](templates/consent-register.md) |
| Gate accounting | 1 | Version 0.2 target counted by hand |

### Data boundary, level 4

[data/README.md](data/README.md) declares what may enter `data/`. Every record object validates against a definition that rejects unknown fields, so a record cannot smuggle an extra identifying field past review. The checker refuses a record without a `clear` public-safe decision; the docs scope that decision to the exact artifact version, and the provenance reading below covers what the checker cannot verify about the scoping. FT-001 passed through all of it. The boundary against free prose in `research/` reports rests on review rather than tooling, and has to: no script can read consent.

### Record structure, level 4

The schema requires 31 top-level fields and validates in CI through `jsonschema` Draft 2020-12, with the real applicators the schema uses. One gap: nothing checks that `record_id` values are unique across records or that a record's filename agrees with its id. At one record this cannot bite. The FT-NNN pattern implies a register that no code maintains.

### Claim integrity, level 4

The strongest dimension. The semantic pass refuses a record that claims completion with incomplete stations, without human Observe evidence, without a predefined agency action, a predeclared materiality rule, a completed rights review, or tested contestability. It forces `unmeasurable` when rights or action-outcome evidence is missing. It refuses a favorable result over a recorded material increase. It checks denominators against the named set, party-impact coverage against the named parties, action actors against known people, and it scans prose for completion wording about incomplete records. It rejects combined-score fields by key. The record cannot say what the evidence does not carry.

### Provenance binding, level 2

The fields exist and are required: `kit_version`, `artifact_version`, and a public-safe decision scoped to the exact version. But the binding between a version string and actual content is declared, not verified. Nothing confirms that `62259ec (2026-08-24)` names a reachable commit, or that the artifact version a reviewer cleared matches the text now committed. The strings are honest today because one person wrote them. That is custody by memory, not by structure.

### Record base, level 4

One record has exercised the full pipeline: schema, semantic rules, public-safe gate, ledger row, paired report. It is maintainer-side, AI-assisted, and partial, and every document that mentions it says so. Level 5 for this dimension is the version 0.2 gate itself: five to ten independent applications across at least three contexts. That ceiling is by design, and this audit does not treat it as a defect.

### Instrument coverage, level 2

`scope.instrument` cannot name a station-level entry for Ground, Adapt, or Return ([issue 12](https://github.com/risaac09/pureland-fork-kit/issues/12)). A contributor who walks one of those stations alone cannot record the scope truthfully without `custom`. The enum shapes what the record base can contain, so the hole propagates forward into every future record until it closes.

### Follow-up lifecycle, level 2

The schema requires an observation window, a review date, and a follow-up status. Nothing compares the review date to the calendar. CI runs on push and pull request only, so a repository nobody touches checks nothing. FT-001's window closes on 2026-11-22, and the repository holds no mechanism that will notice. The kit's core rule is that absence never defaults to favorable; an expired window that nobody closes is exactly such an absence, converted silently into an open status.

### Cross-artifact consistency, level 1

Each accepted record lives three times: the JSON in `data/field-tests/`, the report in `research/field-tests/`, and the row in [FIELD-TRIALS.md](FIELD-TRIALS.md). Nothing checks that the three agree on existence, version, or status. One person can hold three copies of one record in their head. Nobody holds three copies of ten, and ten is the stated target.

### Private-half custody, level 2

[RIGHTS-AND-CONSENT.md](RIGHTS-AND-CONSENT.md) declares what the private review record must contain, and the [consent-register template](templates/consent-register.md) gives it a shape. Whether the maintainer-side private record for FT-001 exists where the declaration says is not verifiable from this repository, and must not become verifiable here: publishing the custody trail would publish what it protects. The move this dimension allows is maintainer-side only, a private note naming where the private halves live, their retention terms, and their review dates.

### Gate accounting, level 1

The version 0.2 gate is counted by hand. The records carry most of what a count needs: `assessor.independence` and `second_reader` status are named fields, while distinct contexts would have to be derived from the `practice` fields, since no context field exists. A checker summary that counts independent applications would keep the gate honest as records accumulate. A count of trials is not a composite score of a practice; the no-composite rule governs readings, not the ledger.

## Next moves, ranked

1. **Overdue-follow-up warning.** Teach the checker to warn when `follow_up.status` is open past `review_date`, and add a scheduled CI run so the warning fires without a push. Smallest change, and it closes a live hole before 2026-11-22.
2. **Close issue 12.** Extend `scope.instrument` to the six stations. Every record written before the fix narrows what the record base can say.
3. **Cross-artifact check.** One checker pass: every record has a ledger row and a paired report, ids are unique, filenames agree, versions match. Cheap at one record, load-bearing at ten.
4. **Gate accounting line.** The checker prints the independent-application and distinct-context counts on every run. A count, not a score.
5. **Provenance binding.** Verify in CI that a record's `kit_version` prefix names a reachable commit. The artifact-version half stays human: a reviewer's clearance cannot be recomputed by a script.

## What this audit cannot see

It cannot see whether the constructs survive a second reader, whether the private custody declared actually happens, or whether any gate holds against a contributor who is not also its author. Those are the version 0.2 questions, and infrastructure levels do not answer them.

## AI assistance

Drafted by Claude (Fable 5) on 2026-08-25 from the public repository at `a2044a9`. No material beyond the repository was provided. Human verification: pending maintainer review; corrections made after that review belong in this section.
