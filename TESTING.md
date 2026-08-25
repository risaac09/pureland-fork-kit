# Testing

Use this protocol to test [H-PRIMARY-0.1](HYPOTHESIS.md#primary-hypothesis-h-primary-01). The field-test record is an evidence record, not a score sheet.

## Before analysis

Record:

- record ID, kit version, test status, and tested hypothesis;
- the scope, instrument, walking person or role, assessor relationship, and second-reader status;
- every affected person or group;
- the practice, unit, boundary, boundary rationale, and one alternative boundary;
- the artifact or surface set, denominator, exclusions, and document-access time window;
- the evidence available before analysis;
- one disconfirming condition;
- the permission and rights-review status; and
- at least one concrete action from `stop`, `continue`, `question`, `correct`, `adapt`, or `refuse`.

For each action, state the baseline, the observation method, the planned follow-up, and a materiality threshold before collecting follow-up evidence. A threshold may be qualitative when it names the decision or right that would change. Do not choose it after seeing the result.

## During analysis

Record each station as `not_started`, `not_performed`, `partial`, `completed`, or `not_applicable`. A whole-journey record cannot be `completed` unless every required station is `completed`. Human Observe must record a human observation. System-design analysis is not a substitute.

Keep these profiles separate:

- understandable, reachable, adaptable, and traceable access readings;
- consent, attribution, and value-return reciprocity readings;
- baseline and follow-up for each agency action; and
- exposure, extractability, and shifted burden for each affected party.

Record disagreements and participant objections as evidence. `No objection collected` is different from `no objection`.

## After an adaptation

Record whether the adaptation was proposed, authorized, executed, declined, or withdrawn. State the intended benefit and possible new harm. Keep the observation window, review date, follow-up evidence, and outcome status explicit.

Apply the classification rule in [HYPOTHESIS.md](HYPOTHESIS.md#classification-rule). The allowed outcomes are support for the tested context, weakened, defeated for the tested context, mixed, unmeasurable, private result, or refused. A public record may report any of them.

Do not:

- average or combine the readings;
- treat missing evidence as favorable;
- use an artifact denominator as a person-level outcome;
- treat an unusable correction route as contestability;
- infer an affected person's view from the assessor's view; or
- make a causal claim from one before-and-after comparison.

The Markdown [field-test template](templates/field-test.md) and JSON [field-test schema](data/field-test.schema.json) carry the same required facts. [FIELD-TESTING.md](FIELD-TESTING.md) explains submission and public privacy review.
