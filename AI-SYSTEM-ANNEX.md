# AI system annex

Use this annex when the assessed practice includes a model, automated decision, generative interface, recommender, transcription service, or agent.

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

Do not call a whole AI system open because one repository is visible. The Open Source AI Definition asks whether people can use, study, modify, and share a system, with access to the preferred form for making modifications.

## Lifecycle record

For design, data collection, training, evaluation, deployment, monitoring, and retirement, record:

- purpose and affected people;
- decision owner;
- consent or other authority;
- known limitations and reasonably foreseeable misuse;
- evaluation evidence and missing populations;
- incident, correction, appeal, and takedown routes;
- retention and retirement conditions.

Use the NIST AI Risk Management Framework as a risk-management reference, not a certification.

## Attention sovereignty test

- What behavior is optimized and what proxy represents it?
- Does the interface invite a deliberate choice or exploit an impulse?
- Can a person see why the system acted and change or refuse the action?
- Does personalization narrow the field without making that narrowing visible?
- Does the system reward continued contact when stopping would better serve the person?
- Which evidence could show that the system gathers rather than fragments attention?

## Consent for data and models

Permission to participate, publish, transcribe, train, evaluate, and retain must be separate. Name the specific provider and model when third-party AI processing occurs. State whether inputs are retained, reviewed by humans, or used to improve a service.

If training consent is withdrawn after weights exist, do not promise full erasure unless the process can prove it. Record whether data deletion, retraining, unlearning, output filtering, or an inability to remediate applies.

## Documentation bundle

Publish, where rights and safety allow:

- a datasheet for each consequential dataset;
- a model card for each model version;
- evaluation protocols and disaggregated results;
- change, incident, and known-limitations logs;
- the license and access status of every component;
- a public route for correction and appeal.

Material withheld for privacy or safety should carry a closure rationale and review date.
