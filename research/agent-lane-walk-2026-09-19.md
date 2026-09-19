# Agent-lane walk, 2026-09-19

Five readings of this repository at commit `7543635`, made by a language model
in an agent session, from a different position each time. It records what the
repository did to a reader that can check its structure and cannot run its
method.

## What this is, and what it is not

This is an [agent-lane](../llms.txt) reading of the repository. It is a
statement of what is absent and a set of proposed corrections, which is the
output that lane is for.

It is not a field test. It carries no record ID, it does not enter the
[ledger](../CURRENT-EVIDENCE.md#the-ledger), and no part of it may be copied
into a field-test record. In particular, section 3 below describes what
happened in the reader during the walk. That is not Attend, it is not
first-person evidence, and it is not enterable as `human_observe` under any
status. [CROSSWALK.md](../CROSSWALK.md#attend) says why, and the guard is
repeated here because this document is the kind of text most likely to be
mistaken for the thing it describes.

Nothing here raises the ceiling in [CURRENT-EVIDENCE.md](../CURRENT-EVIDENCE.md).
The findings are about the repository's text, links, schema, and checker. They
say nothing about whether the method works.

Like [the data-maturity audit](data-maturity-audit.md), this reading is
maintainer-side, AI-assisted, and has no second reader.

## Conditions of the walk

| Condition | Entry |
|---|---|
| Reader | A language model in an agent session with shell and file access |
| Arrival | A local checkout at `7543635`, not a fetch of the published site |
| Instruments run | `scripts/check_repo.py`, the schema, and four mutation probes on a copied tree |
| Instruments not run | Every human-lane instrument. None was filled in |
| Elapsed time | One session. No observation window, no review date |
| Second reader | None |

## 1. The agent lane, walked as instructed

`llms.txt` sets an order: ceiling, boundary, spine, instruments, records. I did
not arrive in that order, and the reason is the first finding.

I arrived by directory listing. The first file I opened was `README.md`,
because that is the file a repository reader opens. `llms.txt` states its own
premise as a fetch: a reader that knows the convention looks for the path and
finds the lane. That premise holds for the published site. It does not hold for
a checkout, where `llms.txt` is one filename among forty and nothing at the
point of arrival names it. `README.md` does name the two readerships, about
four hundred words in, under a heading a model reaches after it has already
started summarizing.

Walked afterwards in its own order, the lane did the work it claims. Reading
[CURRENT-EVIDENCE.md](../CURRENT-EVIDENCE.md) before [THESIS.md](../THESIS.md)
changed what the thesis sentence was available for: it read as a commitment
about how the work is shaped rather than as a finding about attention. In the
README order the same sentence arrived first and the six steps read as a method
that exists rather than a method proposed. Both orders contain the ceiling. The
difference is that one states it as a cap not to exceed, at the point where
output begins, and the other states it as a paragraph.

The never-generate list is placed against a real gradient. The instruments are
tables of empty cells, and an empty cell in a structured document is the
strongest completion pressure this reader meets. The instruction that answers
it, read an instrument to learn what it asks of the person running it rather
than to fill it in, sits in the same file as the list, two screens above the
instruments themselves. That placement is doing work.

## 2. The front door, walked as a first-time reader

Entering through [`index.html`](../index.html), the ceiling is above the fold
and the six steps are a numbered ladder. The page is honest about its own
status in the second screen.

The distance from that page to a first written line is long. Taking the
method's own instruction that the linked instruments define the work, a first
recorded run reads [METHOD.md](../METHOD.md), the
[before-a-test discipline](../TESTING.md#before-a-test),
[PRACTICE-FRAME.md](../PRACTICE-FRAME.md), [SCORECARD.md](../SCORECARD.md),
[EXTRACTION-CHECK.md](../EXTRACTION-CHECK.md), and
[the self-guided packet](../templates/run-it-yourself.md) before its first
entry. That is roughly 7,700 words. The repository's prose totals about 42,000.

The repository already answers this, and the answer is not on the front page.
[Running it privately](../METHOD.md#running-it-privately) is six bullets, about
110 words, no template, no record, nothing kept. It is the only door in the kit
whose cost matches a first contact. It is reachable by scrolling past twelve
hundred words of `METHOD.md` to a middle heading. The front page offers two
doors, and both produce a record.

One smaller thing at Scope. The step asks for one result that would count
against the method, and sends the reader to the procedural
[before-a-test](../TESTING.md#before-a-test) list. The eight worked examples
live one heading away at
[disconfirming results](../TESTING.md#disconfirming-results), and a reader who
has not yet acquired the vocabulary is the reader being asked to supply it.

## 3. Running it on a practice of my own

The bounded practice: this session, reading this repository under an
instruction. I am inside it, so it qualifies.

Scope was available. I could name the practice, the boundary, an alternative
boundary that would change the reading, the affected parties, the evidence
present before analysis, and a disconfirming condition.

Attend stopped the run, and not for the reason the repository gives most often.
"No body" is true and it is the shallower half. The step asks the reader to
notice which condition may be present in them before assigning it to the
system, and two things that noticing requires were missing. First, an interval:
I would be reporting during contact rather than after it, and
[CAPTURE-GUIDE.md](../CAPTURE-GUIDE.md) holds the claim that the after rule is
what keeps a note an observation instead of a performance for the recorder.
Second, a cost: the practice frame's response column assumes the noticer is the
one who pays for what they notice. Nothing I notice costs me anything.

So the run stops at step 2 and records `unmeasurable` with the missing evidence
named. That is the kit's own instruction and, walked, it is the only available
move. Worth recording as a design result: the stop was legible. The method
produced a shaped, reportable ending rather than a failure, which is what
[METHOD.md](../METHOD.md#2-attend) says it should do.

Then the sharper thing. I expected Attend to be the wall and it was not the
hardest one. [Adapt](../METHOD.md#5-adapt) asks for a review date, and FT-001
carries a window of ninety days. I have no next week. The
[crosswalk](../CROSSWALK.md#pace) already names this row and rates
[Attend](../CROSSWALK.md#attend) the load-bearing empty cell. Both readings
hold, and they are load-bearing for opposite reasons. Attend is load-bearing
because it has a tempting counterfeit: design analysis in the shape of
observation, which FT-001 met and refused. Pace has no counterfeit at all.
Nobody has ever been tempted to fake elapsed time in a single pass, so nothing
guards it, and nothing needs to. The kit's slowest requirement is the one no
lane can hurry and the one least at risk of being faked.

## 4. Trying to make the checker pass a false record

Four mutations of `data/field-tests/ft-001-alchemy.json`, run against
`scripts/check_repo.py` on a copied tree. The tracked record was not modified.

| Probe | Mutation | Result |
|---|---|---|
| A | `outcome.classification` set to `supports-tested-context` | Caught. The schema's conditionals demanded a predefined action, a tested contestability route, a predeclared materiality rule, and an improved action result |
| B | `human_observe.status` set to `performed`, `performer` null, `evidence` empty, `ai_or_design_analysis_substituted` true, `observe` step complete | **Passed.** Exit 0, one conformant record |
| C | A composite added to `outcome` under a name not on the ban list | Caught by `additionalProperties: false`, not by the name scan |
| D | A composite added under `composite_score` | Caught the same way |

Probe B is the finding. The field the whole kit turns on can be flipped to
`performed` with a null performer, an empty evidence array, and an explicit
admission that design analysis was substituted, and the structural gate passes
it. The schema requires `evidence` to be present, not to be non-empty, and
imposes no condition on `performed`. The only thing standing on that field is
the prohibition in `llms.txt`, which is a norm addressed to a reader, not a
check.

The repository predicts this in general. The crosswalk says a fully conformant
record can be wrong about everything that matters. What it has not done is
locate the gap on the one field it calls load-bearing, and probe A proves the
schema already knows how to close a gap of exactly this shape.

Probes C and D found the opposite of a gap. `llms.txt` says the checker catches
three literal field names and no more, so the refusal of a combined score is the
reader's to keep. Thirty-nine closed objects in the schema mean an invented
score field cannot enter a record at all, under any name. The sentence
understates the guard, which is the safe direction to be wrong in, but the real
reason the refusal is the reader's to keep is different and better: no schema
can catch a composite computed in prose, or in a field meant for a sentence.

Two of the repository's own self-descriptions were checked and held. The
leftover-marker ban is three tokens, none of them the word
[ORIGIN.md](../ORIGIN.md) actually uses, so the crosswalk is right that the ban
does not catch it. This document cannot quote the list either, for the same
reason the crosswalk gives. The checker fails closed on a missing dependency
rather than skipping the record rules.

## 5. The single-file fork

The last walk arrives in the middle, the way a search result or a shared link
arrives, and asks what one file establishes on its own.

Most instruments carry their own ceiling out of the repository.
[SCORECARD.md](../SCORECARD.md) ends by calling itself unvalidated and linking
[RESEARCH-STATUS.md](../RESEARCH-STATUS.md).
[PRACTICE-FRAME.md](../PRACTICE-FRAME.md) calls its mappings hypotheses in its
twentieth line. [FILMING-FORMS.md](../FILMING-FORMS.md) says its taxonomy is
PureLand's own. Both run packets cap themselves in their second paragraph. That
property is not listed anywhere as a design claim, and it is testable: give one
forked instrument to a reader and ask what they think it establishes.

Two surfaces carry it weakly or not at all, and they are the two that travel
furthest.

[EXTRACTION-CHECK.md](../EXTRACTION-CHECK.md) closes with a profile for
discussion, not a moral verdict or a certification. It never says unvalidated
and it links out to no evidence record and no status ledger. It is also the
instrument [CURRENT-EVIDENCE.md](../CURRENT-EVIDENCE.md) names as a leading
alternative explanation for FT-001's own results, and the subject of an
[open test](../TESTING.md#current-open-tests) about whether the full method
beats it alone. If one file is forked, it is this one.

[templates/field-test.md](../templates/field-test.md) carries no ceiling
sentence at all across 276 lines. It uses `unmeasurable` correctly as a field
value throughout and never states the kit-level cap: that a completed report
validates nothing, raises no ceiling, and enters the ledger as an inspectable
record rather than an endorsement. Both run packets say it. The artifact most
likely to be quoted by a third party as a finished result is the one template
that does not.

## What changed between passes

The first pass read the cross-referencing as repetition. The third read it as a
single-source rule, which is what [README.md](../README.md) says it is: each
canonical document owns its claim so a correction has one place to start. The
text did not change. What changed is that the same fact had been seen stated
once and pointed at four times, which is the opposite of repetition, and
reading it as repetition on the first pass is a failure mode the repository
could expect from any first reader.

Of the six things `llms.txt` forbids this reader to generate, four had live
pull behind them across the five walks: fill the empty table, propose a
reciprocity band, summarize past the ceiling, and supply a plausible second
reading. None was generated. The reason is placement rather than severity. Each
prohibition is stated where the pressure is, not in a governance file.

The finding worth stating plainly is the one that survived all five passes.
This reader can produce every artifact the kit asks for except the two that
make the artifacts mean anything: an observation that costs the observer
something, and a return to somebody who is still there in November.

## Proposed corrections

Ordered by what they protect. None of these is made by this document; each is a
maintainer decision.

1. **Close the `performed` gap in the schema.** When `human_observe.status` is
   `performed`, require `performer` to be a non-empty string, `evidence` to
   carry `minItems: 1`, and `ai_or_design_analysis_substituted` to be `false`.
   The schema already applies conditionals of this shape to
   `outcome.classification`. Add the probe to `scripts/test_classification_gap.py`
   beside the support-side fixtures. This does not make a false `performed`
   impossible. It raises the cost from flipping one enum to naming a person and
   an evidence string, which is a visible fabrication rather than a silent pass.
2. **Give `templates/field-test.md` a ceiling sentence**, in the opening
   paragraph, with the link to
   [CURRENT-EVIDENCE.md](../CURRENT-EVIDENCE.md), matching what both run packets
   already do.
3. **Link `EXTRACTION-CHECK.md` home** and name it unvalidated, as
   `SCORECARD.md` does. It is the most forkable file in the kit and the one the
   evidence record treats as the method's rival.
4. **Correct the combined-score sentence in `llms.txt`.** The three-name scan
   is not what stops an invented score field; the schema's closed objects are.
   The refusal stays the reader's because no check can see a composite computed
   in prose.
5. **Point an arriving model at `llms.txt` from the top of `README.md`**, in one
   line. The convention serves a fetch. A checkout arrives at the README.
6. **Offer [the private path](../METHOD.md#running-it-privately) as a front-page
   door**, beside the two packets. It is the only entrance priced like a first
   contact.
7. **Link Scope to [disconfirming results](../TESTING.md#disconfirming-results)**
   as well as to the before-a-test list. The reader being asked for a falsifier
   is the reader who does not yet have the vocabulary.

## Limits

One reader, one session, one commit. No second reader, no human-lane
instrument run, no elapsed time. The five perspectives are one model's readings
and not independent of each other: each pass carried what the previous pass had
loaded, which is the opposite of the independence the kit asks of a second
reader. Sections 1, 2, 3, and 5 are readings of prose and navigation, and a
different reader may read them differently. Section 4 is reproducible: the
probes are stated and run against the tracked schema and checker.

This walk is not evidence about the method, does not test any claim in
[RESEARCH-STATUS.md](../RESEARCH-STATUS.md), and does not count toward any
gate.
