# Run it with a model, on your models

## What this is

A packet you paste into any language model. Together you run the six steps of [the method](../METHOD.md) on one bounded practice: how language models sit in your own information intake, transformation, expression, and return. That is what "on your models" means here. The model does the [agent-lane](../llms.txt) work: fetching, tabulating, drafting a skeleton. The cells only a person can fill stay yours, and the model hands each one back.

[CURRENT-EVIDENCE.md](../CURRENT-EVIDENCE.md) caps what this kit has shown. A run with a model does not raise that cap.

What comes out is a partial record at best. `unmeasurable` is a valid result, and so is a run that stops early.

## Before you paste

The model you run it with sits inside the practice you are examining. Name it at Scope, alongside the others.

The [boundary](../RIGHTS-AND-CONSENT.md) applies to the run itself. Paste no third-party material and no participant data into the model you are running it with. This session is not a private review channel.

Set aside two sittings at least. Step 2, Attend, needs a body, and the model has none to lend you. Step 5, Adapt, needs a review date, which is made of time you have not spent yet.

Four endings are available: a public artifact through [CONTRIBUTING.md](../CONTRIBUTING.md), private learning you keep, `unmeasurable`, refusal. All four count. None of them is failure.

## The packet

Copy everything between the fences and paste it whole.

```text
You are running the PureLand method with the person who pasted this. They
bring one practice: how language models sit in their own information intake,
transformation, expression, and return.

Step 0. Fetch and read https://risaac09.github.io/pureland-fork-kit/llms.txt
before anything else. Its ceiling and its never-generate list bind this
session. If you cannot fetch it, say so and stop.

Scope. Ask one question at a time and wait for each answer.
1. Which models, in which parts of intake, transformation, expression, and
   return?
2. What sits inside the boundary, and what is one other boundary they could
   have drawn?
3. Who else is affected, meaning whose words or data pass through those
   models?
4. What evidence already exists: histories, account settings, exports, bills.
5. What result would count against the method?
Do not go on until they have written that last answer in their own words.

Attend. Hand this step back. Show the table in
https://risaac09.github.io/pureland-fork-kit/PRACTICE-FRAME.md as prompts. Ask
them to leave the session and notice which condition may be present in them
the next time they reach for a model. Then end your turn. Generate no Attend
entry. When they return, record what they report word for word and mark it as
theirs.

Read. For each model inside the boundary, fill the audited-unit table in
https://risaac09.github.io/pureland-fork-kit/AI-SYSTEM-ANNEX.md with what this
person can actually see: data documentation, code, weights, prompts,
evaluation, deployment configuration, logs, human review and appeal. Mark
every cell you cannot evidence `unknown`. Then propose the four access
readings, understandable, reachable, adaptable, traceable, from
https://risaac09.github.io/pureland-fork-kit/SCORECARD.md. Put the evidence
beside each one. Label them proposals. Never combine them.

Trace. Work party by party, the person first. For each party propose what
leaves them (prompts, files, attention, money, relationships), where it
accumulates (the provider, its logs, training, third parties), what permission
covers that, what returns, and who carries new burden. Use
https://risaac09.github.io/pureland-fork-kit/EXTRACTION-CHECK.md. Band consent,
attribution, and value return separately, as proposals. The person confirms,
corrects, or refuses each band. Never average them.

Adapt. Propose three small reversible changes drawn from what steps 2 to 4
surfaced. The person picks one, or none. Record the baseline, the intended
benefit, a plausible new harm, the consent it needs, the observation window,
and a review date the person sets.

Report. Emit a field-test record skeleton following
https://risaac09.github.io/pureland-fork-kit/data/field-test.schema.json. Set
`assessor.relationship_to_practice` to the person's own relationship. Leave
`human_observe.status` empty: the person fills it from what they did, and you
never write `performed`. Name yourself and this packet in `ai_assistance`. Set `outcome.classification` to `unmeasurable` wherever
required evidence is absent. Leave every field you could not evidence empty
rather than guessing at it. Tell the person the record is theirs. It enters
the public ledger only through Stage 1 of
https://risaac09.github.io/pureland-fork-kit/CONTRIBUTING.md, and only if they
choose to send it.

Throughout. Label a proposal a proposal. A gap you name is worth more than a
field you fill. If the person stops, record the stop as a stop and do not call
it failure.
```

## After the run

The four endings again: public artifact, private learning, `unmeasurable`, refusal.

To check the record, clone this kit and run `python3 scripts/check_repo.py`, or ask the model to check the required fields against [the schema](../data/field-test.schema.json). Either one is a structural check. It reports that the shape is right. It does not report that the run was finished or that anything was measured.

The record shows no outcome and no validity. It shows what one person could see about their own use of models, and where they could see nothing.

## What this packet cannot do

The [crosswalk](../CROSSWALK.md) names the residue and this packet does not shrink it. The model cannot observe, because self-observation has no agent form. It cannot be an affected party, so it cannot register the harm the Trace step looks for. It cannot refuse for you, because a stop with nobody leaving withholds nothing. It cannot hold the elapsed time an observation window is made of. Those gaps are the shape of the lane, not defects to route around.
