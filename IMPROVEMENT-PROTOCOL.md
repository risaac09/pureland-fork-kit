# Improvement protocol

How a finding about this kit becomes a change to it.

[METHOD.md](METHOD.md#when-a-run-ends) ends a run with one instruction: keep
the disagreement, revise the method. This is the procedure behind that
sentence. [CONTRIBUTING.md](CONTRIBUTING.md#process) states how a change is
submitted and [GOVERNANCE.md](GOVERNANCE.md#merge-criteria) states who decides
and on what criteria. Neither says what a finding licenses, what a change to an
instrument owes the records already scored with it, or what a revision may
never do. This file owns those three things and restates nothing else.

A protocol for improving the kit is itself a claim about the kit, so it carries
the same status as any other: untested. Its row is in
[RESEARCH-STATUS.md](RESEARCH-STATUS.md).

## Intake

A finding is any observation that some part of this kit is wrong, unclear,
unenforced, or unsupported. Findings arrive from a field test, a second reader,
a reply at Report, an agent-lane reading, the checker, a review bot, or the
maintainer's own re-reading.

Write the finding down before writing the fix, and write it separately. A
finding recorded only as the change that answered it cannot be contested by
somebody who disagrees with the fix but accepts the problem.

Record with each finding:

- what was observed, and where;
- how it was checked, closely enough for a second reader to repeat it;
- what would have shown it was not a problem;
- which part of the kit it lands on, from the table below.

An unfixed finding is not a failure of the protocol. A finding whose fix is
declined stays on the register in [Declined](#declined).

## Triage by claim kind

What a finding lands on decides what a change may do and what the change owes.

| Finding lands on | What a change may do | What the change also owes |
|---|---|---|
| Prose, a link, an anchor, navigation, or a false self-description | Land directly | The checker and a changelog line. Nothing more |
| An instrument's wording, in the toolbox | Change the instrument | Name every record scored under the old wording; re-read each one, or state why it was left unread. Record the revision as untested |
| A construct definition in [TESTING.md](TESTING.md#classification-rule) | Change the definition | Everything an instrument change owes, plus the reading the old definition would have produced, kept beside the new one |
| The schema or the checker | Tighten a rule, or loosen one that was wrong | A fixture that fails before the change and passes after, in `scripts/test_classification_gap.py` or `scripts/test_check_repo.py`. A statement of what a previously conformant record now asserts |
| A falsifier, in `RESEARCH-STATUS.md` or an instrument | Replace it with a sharper one | The reason, and the old falsifier kept in the record. See the second rule below |
| A new instrument, arriving as code or as a document | Land it | A row in [RESEARCH-STATUS.md](RESEARCH-STATUS.md) carrying its claim and its falsifier, an entry in [TOOLBOX.md](TOOLBOX.md), and a statement of what a first use would have to show for the instrument to have failed its own test. An instrument nobody can find and no ledger tracks is not in the kit, whatever the repository contains |
| The [ledger](CURRENT-EVIDENCE.md#the-ledger) or the evidence ceiling | Nothing but an accepted trial moves these | The trial's own record, through [CONTRIBUTING.md](CONTRIBUTING.md#process) |
| The thesis, or the [primary hypothesis](TESTING.md#primary-hypothesis) | Nothing but field evidence | The evidence, and what it does not establish |

The rows are ordered by what a change costs. A finding that looks like the
first row and turns out to belong to a later one is common, and the later row
governs. When two rows could apply, take the lower.

Name the claim kind in the vocabulary
[RESEARCH-STATUS.md](RESEARCH-STATUS.md) already defines. A change that moves a
claim between kinds, from practice-derived to source-backed, or from a
provisional instrument hypothesis to a tested one, is a change to the ledger
row and not only to the prose.

## Before a change lands

In addition to what [CONTRIBUTING.md](CONTRIBUTING.md#process) and
[GOVERNANCE.md](GOVERNANCE.md#merge-criteria) require:

1. The finding is written down, separately, with its falsifier.
2. The change is the smallest one that answers the finding. A second
   improvement noticed along the way is a second finding.
3. Everything the triage row owes is in the same change, not promised for
   later.
4. What the change does **not** establish is written in the same commit
   message. A tightened check does not make a record true. A clearer sentence
   does not make an instrument valid.
5. Any AI assistance is disclosed under
   [the disclosure rule](AI-ASSISTANCE.md#the-disclosure-rule).
6. `python3 scripts/check_repo.py` and the unit tests pass, with the
   dependency in `requirements.txt` installed.

## What a change may never do

These are the revision-level counterparts of the rules the method already
applies to a run. A run may not average its bands or let absence default to
favorable. A revision may not do the equivalent to the kit.

- **Never weaken a falsifier because it is close to failing.** A falsifier may
  be replaced only by a sharper one, with the reason recorded and the old one
  kept. A falsifier removed while the evidence that would defeat it is being
  collected is a result, not a revision.
- **Never change a construct after seeing a result the old construct would
  have read less favorably**, without recording both readings. This has already
  happened once here. The traceable construct was revised after
  [FT-001](research/field-tests/ft-001-alchemy.md) read intentional deletion as
  a provenance gap. The revision is disclosed and marked untested, and no
  re-read of FT-001 under the new wording exists. That is the shape this rule
  exists to make visible rather than to forbid.
- **Never raise the evidence ceiling by any route but an accepted trial.**
  Architecture, tooling, design, and documentation do not raise it, and
  [CROSSWALK.md](CROSSWALK.md) says so for its own case.
- **Never loosen a check to turn a failure into a pass.** A rule may be
  loosened when the rule was wrong. It may not be loosened because the
  repository is inconvenient. The distinction is whether the loosened rule
  would still have caught the case it was written for.
- **Never edit a record to make it conform.** When a record fails a new rule,
  the failure is the finding. The record is corrected only if the record was
  wrong.
- **Never delete a recorded disagreement, objection, refusal, or absence.** A
  superseded reading is marked superseded and kept.
- **Never soften a stated limit without evidence that the limit moved.**
  Rewording a limit is a change to a claim.

Where these rules and a repository convention disagree, these rules hold. Where
these rules and an affected person's rights under
[GOVERNANCE.md](GOVERNANCE.md#rights-that-do-not-depend-on-merge-authority)
disagree, the rights hold.

## Declined

A proposal that is declined leaves a record. The kit says absence stays in the
record, and until this section existed the only decisions it kept were the ones
it accepted.

Each entry names the date, the proposal, the reason class from
[GOVERNANCE.md](GOVERNANCE.md#release-authority), which separates source
evidence, project synthesis, rights limits, and maintainer judgment, and a link
to where it was proposed.

| Date | Proposal | Reason class | Reason | Proposed in |
|---|---|---|---|---|

The table is empty because no proposal has been declined on the record. An
empty table is the current state, not a claim that nothing has ever been
turned down.

## Worked batch: the 2026-09-19 walk

The [agent-lane walk](research/agent-lane-walk-2026-09-19.md) produced seven
proposals. Triaged, they are four different kinds of change, and the kinds
decide the order and the grouping.

| Proposal | Lands on | Owes | Group |
|---|---|---|---|
| Close the `performed` gap in the schema | Schema and checker | A fixture that fails before and passes after; a statement that records conformant under the old rule asserted less than they appeared to | Alone |
| Give `templates/field-test.md` a ceiling sentence | Prose | Checker and changelog | With the next two |
| Link `EXTRACTION-CHECK.md` home and name it unvalidated | Prose | Checker and changelog | With the above |
| Correct the combined-score sentence in `llms.txt` | Prose, a false self-description | Checker and changelog | With the above |
| Point an arriving model at `llms.txt` from `README.md` | Navigation | Checker and changelog | With the last two |
| Offer the private path as a front-page door | Navigation | Checker and changelog | With the above |
| Link Scope to the disconfirming-results list | Navigation | Checker and changelog | With the above |

The first proposal is alone because it is the only one that changes what a
conformant record asserts. The remaining six are prose and navigation, and none
of them changes an instrument, a construct, a falsifier, or the ceiling.

Neither the walk nor this file makes any of the seven.

### How the batch actually landed

All seven were made in pull request #55, by a different session, before this
file reached `main`. That makes the batch the first test of the triage above
against an outcome it did not produce, and the triage was wrong in two places.
Both are recorded here rather than corrected away, because a procedure that
only ever reports its own success is the thing the [never](#what-a-change-may-never-do)
section exists to prevent.

- **The grouping prediction failed.** The table proposed one change alone and
  two groups of three. The work landed as one pull request carrying all three
  bundles. The grouping column read a change's cost as a claim about how it
  should be shipped, and those are different questions. Cost decides what a
  change owes; it does not decide how many pull requests it takes.
- **The `owes` column was incomplete on the row that mattered most.** It asked
  the schema change for a fixture that fails before and passes after, and for a
  statement about what previously conformant records asserted. #55 delivered
  both and something the column did not name: it wrote the new binding into
  `templates/field-test.md` and `TESTING.md`, so a person who writes `performed`
  learns what it commits instead of meeting a conformance error naming JSON
  paths. A rule that changes what a person must supply owes that person a
  sentence in the place they are working, and the table did not say so.

One thing the triage got right: the schema row was the only one that changes
what a conformant record asserts, and it is the one that needed a test that can
fail. #55's `scripts/test_performed_gap.py` exits 1 against the pre-repair
schema.

A decline still belongs in [Declined](#declined) above. This batch produced
none.

### A second batch, and a row that was missing

Pull request #44 landed `scripts/ecosystem_inventory.py` on 2026-09-19, after
this file reached `main`. It is the second batch triaged here and the first
finding that fit no row at all.

The table's rows all described changing something that already existed: an
instrument's wording, a construct's definition, a rule, a falsifier. #44 added
an instrument. Nothing said what a new one owes, so it landed carrying its own
falsifiable claim with no row in `RESEARCH-STATUS.md`, no entry in
`TOOLBOX.md`, and one mention in `CHANGELOG.md`. A reader of the toolbox cannot
find it and the claim ledger does not know it exists.

The row above is written from that case. #44 predates it, so this is a gap the
protocol now catches rather than a rule anybody broke, and the same change that
adds the row pays what the row asks for.

Two batches, two findings against the triage. The grouping column answered a
question cost does not settle; the `owes` column was silent on a rule change's
debt to the person who must satisfy it; and the table had no row for the thing
arriving rather than changing. A table revised three times by its first two
real uses is a table that was written from one case.

## What this protocol does not do

It does not decide anything. [GOVERNANCE.md](GOVERNANCE.md) holds merge and
release authority, and that concentration is the project risk that file names.
A procedure written by the person who holds the authority does not constrain
that person; it only makes a departure from it visible to somebody reading the
record afterward.

It has not been used on a batch that was not its own worked example, and it may
turn out that findings do not sort into the rows above. Its falsifiers are in
[RESEARCH-STATUS.md](RESEARCH-STATUS.md).
