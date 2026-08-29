# AI system annex

This is a branch of [the journey](JOURNEY.md), carried into the map station. Use this annex when the practice you are assessing includes a model, an automated decision, a generative interface, a recommender, a transcription service, or an agent.

## Define the audited unit

Name the complete system boundary:

| Component | Version or location | Public access | Rights or restriction | Evidence gap |
|---|---|---|---|---|
| Data and data documentation | | | | |
| Source code | | | | |
| Model architecture | | | | |
| Parameters or weights | | | | |
| Prompts and system instructions | | | | |
| Evaluation sets and results | | | | |
| Deployment configuration | | | | |
| Logs and feedback | | | | |
| Human review and appeal | | | | |

Do not call a whole AI system open because one repository is visible. The [Open Source AI Definition](PROVENANCE.md#open-and-ai-system-references) asks whether people can use, study, modify, and share a system, with access to the preferred form for making changes.

Running the assessed model on hardware you own is one way to close the deployment-configuration and logs rows of this table with first-hand evidence; the [open-model lane](OPEN-MODEL-LANE.md) describes that practice and its limits.

## Lifecycle record

For design, data collection, training, evaluation, deployment, monitoring, and retirement, record:

- the purpose and the affected people;
- who owns the decision;
- the consent or other authority behind it;
- the known limitations and the misuse you can reasonably foresee;
- the evaluation evidence, and the populations missing from it;
- the routes for incidents, corrections, appeals, and takedowns;
- the retention and retirement conditions.

Use the NIST AI Risk Management Framework as a risk-management reference, not a certification.

## Attention sovereignty test

- What behavior is being optimized, and what stand-in measure represents it?
- Does the interface invite a deliberate choice or exploit an impulse?
- Can a person see why the system acted, and change or refuse the action?
- Does personalization narrow what a person sees without showing them the narrowing?
- Does the system reward continued contact when stopping would serve the person better?
- What evidence could show that the system gathers attention rather than fragments it?

## Consent for data and models

Permission to participate, publish, transcribe, train, evaluate, and retain must each be separate. Name the specific provider and model whenever third-party AI processing happens. State whether inputs are kept, reviewed by humans, or used to improve a service.

If someone withdraws training consent after the model weights already exist, do not promise full erasure unless the process can prove it. Record which of these applies: data deletion, retraining, unlearning, output filtering, or an honest inability to fix it.

## Documentation bundle

Publish, where rights and safety allow:

- a datasheet for each dataset that matters;
- a model card for each model version;
- the evaluation protocols and the results, broken out by group;
- change, incident, and known-limitations logs;
- the license and access status of every component;
- a public route for correction and appeal.

Anything withheld for privacy or safety should carry a stated reason and a review date.
