# Field-test report

Complete this report and a JSON record that conforms to [`data/field-test.schema.json`](../data/field-test.schema.json). Use the same IDs and facts in both files. Do not hide required facts in one context paragraph.

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

| Evidence ID | Description | Source or public link | Public-safe |
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
- Participant-material status:
- Public-return permission:
- Research-use permission:
- AI-use permission:
- Restrictions:
- Rights evidence:
- Contestability route status:
- Correction route:
- Refusal route:
- Review authority:
- Tested by an affected party: yes or no
- Contestability evidence:

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

## Public privacy review

- [ ] Review status is complete.
- [ ] No participant data or identifying material is included.
- [ ] Every linked artifact is safe and permitted for public release.
- [ ] The JSON record sets `safe_for_public_release` to `true` only after review.
- Reviewer and notes:
