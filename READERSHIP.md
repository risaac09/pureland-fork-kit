# Readership

This repository has two readerships. A person walks it as
[the journey](JOURNEY.md). A model reads it as
[the agent lane](AGENT-READING.md). The [crosswalk](CROSSWALK.md) sets the two
against each other element by element and stays flat.

This file is the other view. It asks what PureLand is such that both lanes are
renderings of it, what survives the change of reader, and which differences have
to stay unreconciled. It is one tier above the lanes, not a point between them.
If it ever reads as an average of the two, it is wrong and should be rewritten.

## The statement both lanes render

PureLand is a set of instruments whose validity depends on who used them.

The repository can be read, indexed, validated, forked, and checked by anything.
It can only be walked by someone the answer can reach. Every instrument in
[the toolbox](TOOLBOX.md) asks its user for something no record can supply on the
user's behalf: attention paid before a category is assigned, a boundary somebody
is accountable for, a change that costs the person who makes it, and a challenge
from someone the change lands on.

The two lanes are two renderings of that one condition. The human lane renders it
as a path with stations, because a person can be asked to walk. The agent lane
renders it as a list of things that must be handed back, because a model can be
told where it stops. Neither rendering is a shortened version of the other, and
neither lane is half of PureLand.

## What survives the change of reader

Four things read the same to anybody and anything.

**The ceiling.** [CURRENT-EVIDENCE.md](CURRENT-EVIDENCE.md) caps every claim
about what PureLand has shown. Version 0.1, instruments unvalidated, one
maintainer-side AI-assisted partial dry run, no independent field trial. The cap
does not move because the reader changed.

**The boundary.** [RIGHTS-AND-CONSENT.md](RIGHTS-AND-CONSENT.md) and
[SECURITY.md](SECURITY.md) keep the same material out of the repository whoever
is holding it. A license does not create permission for participant or
third-party material, and it does not create one for a model either.

**The record.** [FIELD-TRIALS.md](FIELD-TRIALS.md) and the FT-001 pair say the
same thing to both lanes, including what was not observed. The absences are part
of the record, not a gap in the writing.

**The architecture.** What files must exist, what must link to what, and which
version this is. `scripts/check_repo.py` and [CITATION.cff](CITATION.cff) hold
it, and it is the same architecture from either side.

## What does not survive

The walking does not survive. Neither does the observing, the being affected, the
refusing, or the waiting.

That is the whole asymmetry, and it is not a defect in the agent lane. It is what
the thesis claims. [THESIS.md](THESIS.md) holds that attention sovereignty cannot
be separated from how information is collected, interpreted, changed, returned,
and governed. A reader that cannot be changed by the material cannot test that
claim. It can carry the claim accurately, check whether the record is honest
about its own limits, and say what is missing. Those are real jobs. They are not
the same job.

## The named residue

### Human, with no agent form

- **Self-observation at station 2.** Nothing a model produces is noticing.
- **Being an affected party.** The extraction check looks for what leaves a
  person and where it accumulates. A model is not on either side of that ledger.
- **Refusal that takes its reasons with it.** A person who stops leaves holding
  something. A model that stops produces nothing, which is not the same event.
- **Elapsed time as evidence.** An observation window is made of days. A pass
  through a context window is not.
- **A disagreement that belongs to someone.** A generated dissent is not an
  independent reading, and treating it as one would remove the only control the
  instruments currently have.

### Agent, with no human form

- **Schema conformance.** A structural verdict on a record, with no human
  equivalent, and the absence is protective. Conformance is not completion, and
  a human-legible version of it would be read as completion.
- **The reachability graph.** Every content file reachable from an entry point by
  a chain of links. A person notices a broken link. Nobody reads for orphans.
- **`REQUIRED_ARCHITECTURE`.** The only machine-readable statement of what this
  repository must contain, and deliberately not restated in prose.
- **Deterministic re-checking.** `scripts/check_repo.py` reads every file on
  every run and reaches the same verdict each time. A maintainer cannot, and
  neither can a model, which is why the checks are a script.

## Why the residue stays unreconciled

Give the human-only residue an agent form and the kit starts producing records
that look complete and are not. That failure is already on the record: FT-001 ran
AI-assisted, Observe was not performed, and the record says so only because a
person wrote it down. Automating the station would have removed the evidence of
its own absence.

Give the agent-only residue a human form and the structural checks become prose,
prose drifts from the code it describes, and the drift stays invisible until a
release. Worse, a human-readable conformance report would start being cited as
though it were a result.

Holding the two apart is the design. The crosswalk's empty cells are the working
part of this repository's architecture, not a backlog.

## What this document may claim

Only what PureLand is and how it is read. Nothing here states or implies anything
about what PureLand has shown. Naming a readership is a change in the shape of
the kit, not evidence that the kit works.
[CURRENT-EVIDENCE.md](CURRENT-EVIDENCE.md) is unchanged by it, and
[RESEARCH-STATUS.md](RESEARCH-STATUS.md) gains no row, because a readership is
not a claim about the world that field evidence could weaken.
