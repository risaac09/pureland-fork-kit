# Crosswalk

This sets [the human lane](JOURNEY.md) against the agent lane, which is
[llms.txt](llms.txt), element by element. For each element it names what mimics
it in the other lane, the respect in which the mimicry holds, and the respect in
which it fails.

An empty cell is a finding. Where one lane has no counterpart, this file says so
and stops. It does not invent one.

The empty cells stay empty on purpose. Give the human-only residue an agent form
and the kit starts producing records that look complete and are not. That failure
is already on the record: [FT-001](research/field-tests/ft-001-alchemy.md) ran
AI-assisted, Observe was not performed, and the record says so only because a
person wrote it down. Give the agent-only residue a human form and the structural
checks become prose, prose drifts from the code it describes, and a
human-readable conformance report starts being cited as a result.

Nothing here changes what the kit has shown.
[CURRENT-EVIDENCE.md](CURRENT-EVIDENCE.md) holds that, and an architecture
change is not evidence.

## The register at a glance

| Element | Verdict |
|---|---|
| [Entry point](#entry-point) | Both lanes have one; they are reached differently |
| [Orientation](#orientation) | Partial |
| [The Observe station](#the-observe-station) | No agent counterpart |
| [The boundary decision](#the-boundary-decision) | Partial |
| [Evidence ceiling](#evidence-ceiling) | Close, in two grammars |
| [Refusal](#refusal) | Weak |
| [Consent](#consent) | Weak |
| [The camera](#the-camera) | No agent counterpart |
| [Error correction](#error-correction) | Partial, and half of it is unpracticed |
| [Provenance](#provenance) | Partial |
| [Pace](#pace) | No mimicry |
| [The architecture contract](#the-architecture-contract) | Derived, not parallel |
| [Schema conformance](#schema-conformance) | No human counterpart |
| [The placeholder](#the-placeholder) | Looks like mimicry, is not |

## Entry point

- **Human lane.** [README.md](README.md), reached by choosing to look.
- **Agent lane.** `llms.txt`, reached by path convention.
- **Holds.** Both open with the same question and the same version 0.1 limits.
- **Fails.** A person arrives having decided to be there. A fetcher arrives
  having decided nothing. The README can assume curiosity. `llms.txt` cannot, so
  it states the prohibitions before it states the invitation.

## Orientation

- **Human lane.** Station 1, Ground. Name the practice, the boundary, the
  purpose, and the affected people, then write one result that would count
  against the method.
- **Agent lane.** The ceiling-first opening of `llms.txt`.
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
  in the register, and the record already demonstrates it: FT-001 was
  AI-assisted, Observe was not performed, and the structured record carries that
  as `human_observe.status: not-performed`. Automating the station would have
  removed the evidence of its own absence.

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
- **Agent lane.** The first line of `llms.txt`, stated as an instruction not to
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
- **Agent lane.** The hand-back list in `llms.txt`.
- **Holds.** Weakly. Both produce a stop, and both leave a record behind.
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

## The camera

- **Human lane.** [PROTOCOL.md](PROTOCOL.md) for any recorded encounter, and
  [FILMING-FORMS.md](FILMING-FORMS.md) for the four forms a camera-based one can
  take. Each form ends in a question asked before rolling.
- **Agent lane.** No counterpart.
- **Holds.** Nothing.
- **Fails.** The four forms are relational positions and a model occupies none of
  them. It cannot hold the third position a triadic encounter needs somebody to
  actually stand in, and in environmental filming it is not among the people
  connected to the place who were never asked. "Is this footage of an encounter
  with myself, or is it already footage of an audience I'm imagining?" cannot be
  answered by a reader who was not in the room. A model can propose which form is
  in use at a given moment, which is what the instrument asks to be named. It
  cannot be in any of them.

## Error correction

- **Human lane.** A second reader scores the same material and the disagreement
  is kept rather than resolved away.
- **Agent lane.** [scripts/check_repo.py](scripts/check_repo.py).
- **Holds.** Both catch a class of error a single author working alone will
  miss.
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
- **Holds.** Both make a version traceable to a point in the work's history.
- **Fails.** `PROVENANCE.md` records what shaped the thinking, including what is
  unsettled about a source. `CITATION.cff` records what to cite. A model that
  reads the metadata and stops learns the release and none of the debts. Only the
  agent side is guarded: nothing at all catches a `PROVENANCE.md` that has gone
  stale.

## Pace

- **Human lane.** A body and a schedule. Stations spread over days. FT-001's
  adaptation carries a 90-day observation window.
- **Agent lane.** A context window and one pass.
- **Holds.** Nothing worth calling mimicry.
- **Fails.** Part of the method's evidence is made of elapsed time. No agent
  reading persists to a review date. The kit's slowest requirement is the one the
  agent lane cannot hold at all, and `check_repo.py` says so on the calendar's
  behalf by noticing a follow-up left open past its own review date.

## The architecture contract

- **Human lane.** `python3 scripts/check_repo.py --list-architecture`, which
  prints the required files.
- **Agent lane.** `REQUIRED_ARCHITECTURE` in `scripts/check_repo.py`.
- **Holds.** Both read the same list, because there is only one list. The human
  side is a rendering of the agent side rather than a parallel artifact, so it
  cannot drift from it.
- **Fails.** A rendering only reaches someone who knows to ask for it, and a
  printed list says which files must exist without saying why any of them is
  required. No prose statement of the contract exists and this file does not add
  one.

## Schema conformance

- **Human lane.** No counterpart.
- **Agent lane.** [data/field-test.schema.json](data/field-test.schema.json),
  Draft 2020-12.
- **Holds.** Nothing.
- **Fails.** The absence is protective. A human-legible equivalent of
  conformance would be read as completion, and [data/README.md](data/README.md)
  exists to deny exactly that reading. This empty cell should stay empty.

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
