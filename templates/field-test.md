# Field-test report

Complete this report and a JSON record that conforms to [`data/field-test.schema.json`](../data/field-test.schema.json) only after Stage 1 scoping and any required private rights review. Use the same IDs and facts in both files. Do not hide required facts in one context paragraph. Do not paste this completed report into the public Stage 1 issue.

## Record identity and tested hypothesis

- Record ID (`record_id`):
- Kit version or commit (`kit_version`):
- Test status (`test_status`):
- Hypothesis ID and version:
- Hypothesis kind: primary, secondary, or design
- Tested statement:
- Predeclared before analysis: yes or no
- Scope: whole journey, one instrument, or custom
- Instrument:
- Scope rationale:

## Measurement units and people

### Walking person

- ID or public-safe role:
- Present or absent:
- Role:
- Description:

### Affected people

Add one row for each affected person or group. Use each `affected_party_id` again in agency and impact records.

| Affected-party ID | Public-safe description | Role | Relationship to the practice |
|---|---|---|---|
| | | | |

### Assessor and second reader

- Assessor ID or public-safe role:
- Assessor relationship to the practice:
- Assessor independence:
- Second-reader status: none, planned, or completed
- Second-reader ID or public-safe role:
- Independent: yes, no, or not established
- Second-reader relationship and evidence:

## Practice, boundary, and document-access set

- Practice name:
- Bounded practice unit:
- Boundary:
- Boundary rationale:
- Plausible alternative boundary:
- How the alternative could change the reading:
- Document-access set name:
- Artifact or surface unit:
- Set items:
- Denominator:
- Exclusions:
- Access-reading time-window start and end:
- Time-window basis:

The document denominator supports artifact-level readings only. It is not a person-level outcome denominator.

## Evidence available before analysis

Every JSON evidence item must set `available_before_analysis` to `true`.

| Evidence ID | Description | Public-safe source reference | Artifact-version review status |
|---|---|---|---|
| | | | |

## Disconfirming condition

- Condition:
- Predeclared before analysis: yes or no
- Assessment: not-assessed, met, partially-met, not-met, mixed, or unmeasurable
- Interpretation:

## Station completion and human Observe

| Station | Required | Status: not-started, incomplete, complete, or not-applicable | Evidence |
|---|---|---|---|
| Ground | | | |
| Observe | | | |
| Map | | | |
| Trace | | | |
| Adapt | | | |
| Return | | | |

- Human Observe status: performed, not-performed, or not-required
- Human performer:
- Human Observe evidence:
- AI or design analysis substituted: yes or no

AI or design analysis does not satisfy a required human Observe station.

## Access readings

Keep all four readings separate. Record count categories and denominators where counts apply.

| Reading | Status | Finding | Denominator reference | Counts | Evidence IDs |
|---|---|---|---|---|---|
| Understandable | | | | | |
| Reachable | | | | | |
| Adaptable | | | | | |
| Traceable | | | | | |

## Reciprocity readings

| Reading | Status | Finding | Affected-party IDs | Evidence IDs |
|---|---|---|---|---|
| Consent | | | | |
| Attribution | | | | |
| Meaningful return | | | | |

## Agency actions

Predefine at least one concrete action. Add one block for each action.

### Action ID

- Actor ID:
- Action: stop, continue, question, correct, adapt, or refuse
- Operational definition:
- Predefined before analysis: yes or no
- Baseline status, description, and date:
- Follow-up status, description, and date:
- Result: improved, weakened, no-change, mixed, unmeasurable, or pending
- Evidence:

## Burden, exposure, and extractability by affected party

Add one block for each affected-party ID. Record baseline and follow-up separately. For each reading, give status, description, evidence, and `material_increase` as yes, no, or not established.

### Affected-party ID

| Period | Dimension | Status | Description | Material increase | Evidence |
|---|---|---|---|---|---|
| Baseline | Exposure | | | | |
| Baseline | Extractability | | | | |
| Baseline | Shifted burden | | | | |
| Follow-up | Exposure | | | | |
| Follow-up | Extractability | | | | |
| Follow-up | Shifted burden | | | | |

## Materiality rule

- Predeclared before analysis: yes or no
- Context-specific rule:
- Dimensions covered: exposure, extractability, shifted burden

## Disagreements and participant objections

- Disagreement status: present, none-recorded, not-sought, or unmeasurable
- Each disagreement: party, issue, position, and resolution
- Participant-objection status: present, none-recorded, not-sought, or unmeasurable
- Each objection: party, issue, position, and resolution

`none-recorded`, `not-sought`, and `unmeasurable` are different results.

## Permission, rights, and contestability

- Rights-review status:
- Private rights-record status:
- Participant-material status:
- Community-authority status:
- Recording permission:
- Retention permission:
- Access by each named reviewer:
- Publication permission:
- Approval of this exact artifact and version:
- Research-use permission:
- AI-processing permission:
- Model-training or fine-tuning permission:
- Restrictions:
- Rights evidence:
- Contestability route status:
- Correction route:
- Takedown route:
- Refusal route:
- Review authority:
- Tested by an affected party: yes or no
- Contestability evidence:

Keep each permission separate. `Granted` in one row does not imply permission anywhere else.

## Withdrawal actions

- Status: not-requested, pending, acted, partially-acted, refused, or unmeasurable
- Protected route:
- Each request date, action, action date, status, and material that remains with the reason:
- Known limits on removal from archives, backups, model weights, external copies, or downstream adaptations:

## Adaptation and follow-up

- Adaptation status:
- Description:
- Consent status:
- Execution date:
- Execution evidence:
- Intended benefit:
- Possible new harm:
- Observation-window start and end:
- Observation-window basis:
- Review date:
- Follow-up status:
- Follow-up evidence:
- Follow-up finding:

## Outcome and return

- Classification: supports-tested-context, weakens-tested-context, defeats-tested-context, mixed, or unmeasurable
- Return disposition: public-return, private-result, refusal, unmeasurable, or pending-follow-up
- Rationale:
- Causal claim: yes or no
- Causal limitations:
- Competing explanations:
- Missing evidence:

Missing required action-outcome or rights evidence makes the result `unmeasurable`. A material increase in exposure, extractability, or shifted burden cannot be averaged away. Mixed profiles remain mixed.

## AI assistance

- Used: yes or no
- Systems:
- Tasks:
- Human verification:
- Corrections after verification:
- Material withheld:

## Artifact-version public-safe review

- Artifact ID:
- Exact artifact version:
- Decision: clear, blocked, or not-yet-clear
- Reviewer identity or accountable role:
- Decision date:
- Next review date:

Record one row for every category. A Boolean privacy checkbox is not a rights review.

| Category | Status: clear, blocked, not-yet-clear, or not-applicable | Public basis summary | Limits | Actions required |
|---|---|---|---|---|
| Participant material | | | | |
| Direct identifiers | | | | |
| Indirect identifiers | | | | |
| Confidential records | | | | |
| Client records | | | | |
| Protected community knowledge | | | | |
| Third-party copyright | | | | |
| Privacy interests | | | | |
| Publicity interests | | | | |
| Artifact-specific permission | | | | |
| Re-identification risk | | | | |
| Attribution risk | | | | |
| AI processing | | | | |
| Model training | | | | |
| Retention and withdrawal | | | | |

Do not publish a `blocked` or `not-yet-clear` artifact. The detailed private record must hold provider, model, purpose, inputs, access, retention, training decision, withdrawal route, and known limits. Never commit that private record under `data/`.

## Return route

This section records nothing in the JSON record. Fill it to decide where the report goes after the review above.

- Return disposition recorded above:
- Asking for a second reading: yes or no
- Route used:
- Exact artifact version cleared for that route:
- Material withheld from the route:
- Scale of the question asked: the walking person's own practice, or a practice shared with other people

A second reading is one reply from the maintainer on a report you have already cleared, described in the journey's [Return station](../JOURNEY.md#6-return). Ask for it with a public-safe note in an [issue](https://github.com/risaac09/pureland-fork-kit/issues). Do not paste this completed report there. A private result, a refusal, and an `unmeasurable` outcome are complete endings that need no route at all.
