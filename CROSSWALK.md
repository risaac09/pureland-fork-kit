# Crosswalk

This sets [the human lane](JOURNEY.md) against [the agent lane](AGENT-READING.md)
element by element. For each element it names what mimics it in the other lane,
the respect in which the mimicry holds, and the respect in which it fails.

An empty cell is a finding. Where one lane has no counterpart, this file says so
and stops. It does not invent one.

This is the flat view. It runs across the two lanes and stays there. The vertical
view, what PureLand is such that both lanes render it, is
[READERSHIP.md](READERSHIP.md). The two are not the same document and neither
substitutes for the other.

Nothing here changes what the kit has shown.
[CURRENT-EVIDENCE.md](CURRENT-EVIDENCE.md) holds that, and an architecture
change is not evidence.

## The register at a glance

| Element | Verdict |
|---|---|
| [Entry point](#entry-point) | Both lanes have one; they are reached differently |
| [Reading order](#reading-order) | Both lanes have one; the orders differ on purpose |
| [Orientation](#orientation) | Partial |
| [The Observe station](#the-observe-station) | No agent counterpart |
| [The boundary decision](#the-boundary-decision) | Partial |
| [Evidence ceiling](#evidence-ceiling) | Close, in two grammars |
| [Refusal](#refusal) | Weak |
| [Consent](#consent) | Weak |
| [Error correction](#error-correction) | Partial, and half of it is unpracticed |
| [Provenance](#provenance) | Partial |
| [Pace](#pace) | No mimicry |
| [The architecture contract](#the-architecture-contract) | No human counterpart |
| [Schema conformance](#schema-conformance) | No human counterpart |
| [Front page](#front-page) | Both lanes have one; one was unlisted |
| [The placeholder](#the-placeholder) | Looks like mimicry, is not |
| [The name collision](#the-name-collision) | No mimicry; a naming accident |

## Entry point

- **Human lane.** [README.md](README.md), reached by choosing to look.
- **Agent lane.** [llms.txt](llms.txt), reached by path convention.
- **Holds.** Both open with the same question and the same version 0.1 limits.
  A reader of either learns the ceiling within the first paragraph.
- **Fails.** A person arrives having decided to be there. A fetcher arrives
  having decided nothing. The README can assume curiosity. `llms.txt` cannot, so
  it has to state the prohibition before it states the invitation.

## Reading order

- **Human lane.** The six numbered documents in `README.md`, running from
  argument to evidence.
- **Agent lane.** [AGENT-READING.md](AGENT-READING.md), running from ceiling to
  boundary to record.
- **Holds.** Both are orders through the same files, and neither adds content.
- **Fails.** The orders are not the same. The human order is built for someone
  deciding whether to trust the work. The agent order is built to stop a reader
  from saying something false before it has read enough to know. The agent side
  carried an index and no order at all until the lane was written.

## Orientation

- **Human lane.** Station 1, Ground. Name the practice, the boundary, the
  purpose, and the affected people, then write one result that would count
  against the method.
- **Agent lane.** The ceiling-first summary at the top of `llms.txt`.
- **Holds.** Both put the limit ahead of the content.
- **Fails.** Ground asks the walker to commit to a disconfirming condition before
  looking at anything. Nothing asks a model to commit to anything. It can read
  the record first and choose its framing afterward, which is the order the
  station exists to prevent.

## The Observe station

- **Human lane.** [PRACTICE-FRAME.md](PRACTICE-FRAME.md) at station 2. Notice
  which condition may be present in you before assigning it to the system.
- **Agent lane.** No counterpart.
- **Holds.** Nothing.
- **Fails.** There is no mimicry to assess. This is the load-bearing empty cell
  in the register, and the record already demonstrates it:
  [FT-001](research/field-tests/ft-001-alchemy.md) was AI-assisted, Observe was
  not performed, and the structured record carries that as
  `human_observe.status: not-performed`. The agent lane now states that a model
  may not fill that field. Before the lane existed, no surface said so.

## The boundary decision

- **Human lane.** The assessor draws the practice boundary, records the
  rationale, and names a plausible alternative that could change the reading.
- **Agent lane.** The schema requires `practice.boundary`,
  `practice.boundary_rationale`, and `practice.alternative_boundary` to be
  present.
- **Holds.** Structure enforces that the decision was made and written down
  rather than left implicit.
- **Fails.** The schema checks that a boundary exists. It never checks that it
  was the right one. FT-001's boundary is seven surfaces the assessor chose, and
  a conformant record and a defensible boundary are separate things.

## Evidence ceiling

- **Human lane.** [CURRENT-EVIDENCE.md](CURRENT-EVIDENCE.md) as prose a reader
  can weigh and argue with.
- **Agent lane.** The first bullet of `llms.txt`, stated as an instruction not to
  exceed.
- **Holds.** Same cap, same file, two grammars.
- **Fails.** A person can disagree with the ceiling and say so. A model is told
  not to exceed it, which is compliance rather than agreement. Compliance breaks
  silently when the file falls out of context. A person who forgets can go back
  and read it again, and knows that they forgot.

## Refusal

- **Human lane.** You may stop or leave at any station. Record the stop, the
  refusal, or the missing permission without turning it into failure by the
  participant.
- **Agent lane.** The hand-back list in `AGENT-READING.md`. Nothing preceded it.
- **Holds.** Weakly. Both produce a stop, and both are supposed to leave a record
  behind.
- **Fails.** A person's refusal is theirs. It carries their reasons out of the
  record and those reasons stay with them. An agent's stop is an absence of
  output. Nobody leaves, so nothing is withheld.

## Consent

- **Human lane.** [PROTOCOL.md](PROTOCOL.md) and
  [RIGHTS-AND-CONSENT.md](RIGHTS-AND-CONSENT.md). Separate decisions per use,
  made with the people involved, revisable by them.
- **Agent lane.** A prohibition list. What must never enter the repository.
- **Holds.** Both keep the same material out of public view.
- **Fails.** Consent is something a person grants and can withdraw. A prohibition
  is a boundary somebody else drew. A model can obey the list perfectly and take
  part in no consent decision at all. The list protects the repository. It does
  not stand in for the decision.

## Error correction

- **Human lane.** A second reader scores the same material and the disagreement
  is kept rather than resolved away.
- **Agent lane.** [scripts/check_repo.py](scripts/check_repo.py).
- **Holds.** Both catch a class of error before publication, and both are meant
  to run before a record goes public.
- **Fails.** The checker finds structural error. It cannot find a wrong reading,
  and a fully conformant record can be wrong about everything that matters. The
  human half of this row is also a design rather than a practice: no second
  reader has completed a comparison, which [TESTING.md](TESTING.md) records as
  evidence not yet obtained.

## Provenance

- **Human lane.** [PROVENANCE.md](PROVENANCE.md) with sources and locators, plus
  [AI-ASSISTANCE.md](AI-ASSISTANCE.md) for how the text was produced.
- **Agent lane.** [CITATION.cff](CITATION.cff) and the version-claim check that
  ties the release the entry points announce to the metadata.
- **Holds.** Both make a version citable, and both fail loudly when a release
  moves and a copy does not.
- **Fails.** `PROVENANCE.md` records what shaped the thinking, including what is
  unsettled about a source. `CITATION.cff` records what to cite. A model that
  reads the metadata and stops learns the release and none of the debts.

## Pace

- **Human lane.** A body and a schedule. Stations spread over days. FT-001's
  adaptation carries a 90-day observation window running to a 2026-11-22 review.
- **Agent lane.** A context window and one pass.
- **Holds.** Nothing worth calling mimicry.
- **Fails.** Part of the method's evidence is made of elapsed time. No agent
  reading persists to a review date. The kit's slowest requirement is the one the
  agent lane cannot hold at all, and `check_repo.py` says so on the calendar's
  behalf by noticing a follow-up left open past its own review date.

## The architecture contract

- **Human lane.** No counterpart.
- **Agent lane.** `REQUIRED_ARCHITECTURE` in `scripts/check_repo.py`.
- **Holds.** Nothing.
- **Fails.** A person learns this repository's architecture by reading it and
  inferring the shape. There is no prose statement of what must be present, and
  this file does not add one. A second copy of the list would drift from the
  first, and the drift would be invisible until a release.

## Schema conformance

- **Human lane.** No counterpart.
- **Agent lane.** [data/field-test.schema.json](data/field-test.schema.json),
  Draft 2020-12.
- **Holds.** Nothing.
- **Fails.** The absence is protective. A human-legible equivalent of
  conformance would be read as completion, and [data/README.md](data/README.md)
  exists to deny exactly that reading. This empty cell should stay empty.

## Front page

- **Human lane.** [index.html](index.html), served at the Pages root.
- **Agent lane.** `llms.txt`, served from the same root.
- **Holds.** Same origin, same version claim, same six stations.
- **Fails.** `index.html` went unlisted in `llms.txt` until the lanes were named.
  Pages served both and only one was indexed for the other lane. A model reading
  the index had no way to know the human front page existed.

## The placeholder

- **Human lane.** [ORIGIN.md](ORIGIN.md) opens by saying the section is not yet
  written and that the maintainer is writing it himself.
- **Agent lane.** The placeholder ban in `check_repo.py`, which looks for a short
  list of leftover-marker tokens. This file cannot quote the list, because the
  ban would flag the quotation. Read it from the script.
- **Holds.** Not at all, despite appearing to.
- **Fails.** The ban does not catch the word `ORIGIN.md` actually uses. A person
  reads an honest empty section and knows to skip it. A parser reads a section
  with prose in it. This is the clearest case in the register of one lane's
  honesty being invisible to the other.

## The name collision

- **Human lane.** [AI-SYSTEM-ANNEX.md](AI-SYSTEM-ANNEX.md) is an instrument. A
  person carries it into the map station when the practice under inquiry contains
  a model, an automated decision, a recommender, or an agent.
- **Agent lane.** `AGENT-READING.md` is a lane. It addresses the model doing the
  reading.
- **Holds.** Nothing. The overlap is in the names.
- **Fails.** One file is about AI as a subject of assessment. The other is about
  AI as a reader. A reader who opens the annex looking for the agent lane finds a
  table for auditing somebody else's system.
  [OPEN-MODEL-LANE.md](OPEN-MODEL-LANE.md) is a third thing again: infrastructure
  guidance for a person running open-weight models, human-addressed despite the
  name. This row exists so the trip happens once.
