# Agent reading

This is the agent lane. It is addressed to a model, agent, or automated reader
working with this repository. The human lane is [the journey](JOURNEY.md), which
is walked. This lane is addressed. The two are set against each other element by
element in the [crosswalk](CROSSWALK.md), and held together in
[READERSHIP.md](READERSHIP.md).

This document is not the [AI system annex](AI-SYSTEM-ANNEX.md). The annex is an
instrument a person uses at the map station when the practice under inquiry
contains a model. It is about AI as a subject. This document is about AI as a
reader. The names sit close together and the crosswalk says so out loud.

## Entry point

[llms.txt](llms.txt) is the entry point and stays the entry point. It is a
published convention, so a fetcher that knows the convention looks for that path
and finds only this file there. It is the index: what each file is. This document is the path: what to read, in
what order, and where to stop.

## The order to read in

[README.md](README.md) publishes a different order. That is deliberate, not
drift. The README order runs from argument to evidence, which is how a person
decides whether to trust the work. This order runs from ceiling to boundary to
record, which is how a reader avoids saying something false before it has read
enough to know.

1. **The ceiling.** [CURRENT-EVIDENCE.md](CURRENT-EVIDENCE.md). Read it before
   anything else. It caps every statement you can make about what PureLand has
   shown. Nothing later in this repository raises that cap.
2. **The boundary.** [RIGHTS-AND-CONSENT.md](RIGHTS-AND-CONSENT.md),
   [SECURITY.md](SECURITY.md), and [data/README.md](data/README.md). These say
   what may never enter the repository and what a license does not grant.
3. **The spine.** [THESIS.md](THESIS.md), [METHOD.md](METHOD.md),
   [HYPOTHESIS.md](HYPOTHESIS.md), [TESTING.md](TESTING.md), and
   [RESEARCH-STATUS.md](RESEARCH-STATUS.md). The argument, the procedure, the
   testable claim, the testing program, and the limits ledger. The spine belongs
   to neither lane and this lane does not restate it.
4. **The instruments.** [TOOLBOX.md](TOOLBOX.md) indexes them. Read an
   instrument to learn what it asks of a walker, not to fill it in.
5. **The records.** [FIELD-TRIALS.md](FIELD-TRIALS.md), then
   [research/field-tests/ft-001-alchemy.md](research/field-tests/ft-001-alchemy.md)
   and its structured twin
   [data/field-tests/ft-001-alchemy.json](data/field-tests/ft-001-alchemy.json).

## The architecture contract

`REQUIRED_ARCHITECTURE` in [scripts/check_repo.py](scripts/check_repo.py) lists
the files this repository must contain. It is the only statement of that
contract. No prose file restates the list, because a second copy would drift from
the first. Read it from the script, or have the script print it:

```sh
python3 scripts/check_repo.py --list-architecture
```

The same script enforces the rest of the structure: every content file reachable
from `README.md`, `JOURNEY.md`, or `BRIEF.md` by a chain of links; no leftover
placeholder token, against a short list the script spells out and this file
cannot quote, with the structured records under `data/field-tests/` exempt and
Markdown reports not exempt; local and Pages links that resolve; heading anchors that exist; and agreement
between the release version the entry points announce and `CITATION.cff`.

## The schema

[data/field-test.schema.json](data/field-test.schema.json) is JSON Schema, Draft
2020-12. It is the structural gate on public field-test records.

Schema conformance means the record carries the required fields and satisfies
structural rules. It does not mean the method was completed, the evidence
supports the hypothesis, or any construct has been validated. `check_repo.py`
applies semantic rules on top of conformance: a record that requires the Observe
station cannot claim completion without human Observe evidence, no record can
claim support with a recorded material increase, and any record must classify its
outcome `unmeasurable` when the required rights or action-outcome evidence is
missing.

## What you may generate

- A summary that carries the ceiling with it.
- A structural check, a link check, or a report of what a record is missing.
- Record scaffolding with the required fields named and left empty for a person.
- A correction to a broken link, a stale cross-reference, or a false
  self-description.
- A statement of what is absent. Naming a gap is the useful output here.

## What you may never generate

- An Observe-station entry. Nothing a model produces is self-observation.
- `human_observe.status` set to `performed`, or any text that implies a person
  observed when none did.
- An access reading, a reciprocity band, or an outcome classification presented
  as observed rather than proposed.
- A second reader's disagreement. A generated dissent is not an independent
  reading and would corrupt the one control the instruments have.
- A completed consent register, a participant name, a transcript, or any
  material [SECURITY.md](SECURITY.md) keeps out of the repository.
- A claim about what PureLand has shown that goes past
  [CURRENT-EVIDENCE.md](CURRENT-EVIDENCE.md).
- The [ORIGIN.md](ORIGIN.md) account. It is the maintainer's personal history and
  the file says no other contributor should draft it for him.
- A combined, composite, or average score. The instruments refuse one.
  `check_repo.py` catches three literal field names and no more, so the refusal
  is yours to keep, not the checker's to enforce.

## What you must hand back

Hand these to a person, unstarted or clearly marked as a proposal:

- The Observe station. It has no agent form.
- The practice boundary. You may propose one and name a plausible alternative.
  A person chooses it and records the rationale.
- The affected-party challenge. A walk cannot be called complete without it and
  you cannot supply it.
- The filming form, when a camera is present. You may propose which of the four
  forms in [FILMING-FORMS.md](FILMING-FORMS.md) is in use at a given moment,
  which is the unit that file asks for: a project can move through more than one
  form, and each one in use carries its own value trace. The question each form
  asks before rolling belongs to whoever is in the room.
- Refusal, and the record of a walk that stopped.
- The public-safe decision on an artifact version.
- The follow-up outcome after an observation window closes.

## What you cannot do, stated plainly

You have no body, so the practice frame's noticing has no input from you. You are
not an affected party, so you cannot register the harm the extraction check looks
for. You can decline to produce output, which is not the refusal the journey
means: a person who leaves takes their own record and their own reasons with
them.

These are not defects to work around. They are the shape of the lane.

## When you cannot proceed

Write `unmeasurable` and say what is missing.
[HYPOTHESIS.md](HYPOTHESIS.md) states the rule this follows: a refusal, a private
result, or an `unmeasurable` result is valid evidence about the method, and
absence never defaults to favorable. A gap you name is worth more here than a
field you fill.
