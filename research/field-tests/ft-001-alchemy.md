# Field test FT-001: partial journey dry run on Alchemy

FT-001 is a maintainer-side, AI-assisted partial dry run of [the journey](../../JOURNEY.md) on the [Alchemy app](https://github.com/risaac09/alchemy). It is not an independent trial and does not count toward the version 0.2 gate. Structured record: [data/field-tests/ft-001-alchemy.json](../../data/field-tests/ft-001-alchemy.json).

## Record identity and status

| Field | Entry |
|---|---|
| Record ID | FT-001 |
| Kit version | 62259ec, 2026-08-24 |
| Status | Partial execution; adaptation executed; follow-up open through 2026-11-22 |
| Scope | Whole journey |
| Assessor | An AI agent, Claude Code, directed by the Alchemy owner and PureLand maintainer |
| Assessor relationship | Maintainer-side; not independent |
| Second reader | None |
| Human walker | None |
| Tested design-hypothesis classification | `unmeasurable`; no comparator was run |
| Primary-hypothesis status | Not tested; outcome `unmeasurable` |

## Tested hypothesis and disconfirming condition

FT-001 tested a design hypothesis, not the primary agency hypothesis:

> The whole journey adds useful analytic value beyond an ordinary review of the same evidence and enough value to justify its additional burden.

Before analysis, the assessor recorded this disconfirming condition: if the walk surfaces nothing beyond what Alchemy's README, CLAUDE.md, docs/PRODUCT.md, and HONEST-ACCOUNT.md already state, then the journey adds no analytic value over an ordinary repository review.

Assessment: `mixed`. The assessor identified some readings that were not explicit in the named documents and repeated two known findings. No ordinary-review or single-instrument comparator was run. The record cannot establish that the journey caused the additional readings or justified its burden.

## Measurement units

| Unit | FT-001 definition |
|---|---|
| Walking person | Absent. An AI assessor performed repository analysis and could not supply human first-person evidence. |
| Bounded information practice | Alchemy repository commit `b7ae829`, read as one published information-metabolism practice |
| Affected groups | Local-tool users; funnel visitors; past Metabolizer buyers; embodied-service users; the maintainer |
| Document-access set | Seven public surfaces chosen by the assessor: PWA, embed funnel, Obsidian plugin, Chrome extension, iOS wrapper, bookmarklet, embodied service |
| Observation window | Repository snapshot on 2026-08-24; adaptation follow-up from 2026-08-24 through 2026-11-22 |

The seven-surface denominator applies only to artifact-level access readings. It is not a count of people and supports no person-level agency outcome.

### Boundary rationale and alternative

The assessor grouped the six product surfaces named in `docs/PRODUCT.md` with the embodied service because the repository presents them as one companion practice. This was the assessor's choice, not a participant-agreed boundary.

A plausible alternative would treat the repository core, each client surface, and the embodied service as separate practices, or exclude the experimental embodied service. That choice would change every artifact denominator and isolate the third-party model exposure.

Known exclusions: the live deployed site and app stores were not exercised; store and community-plugin listings were not independently verified; no participant experience or affected-user testimony entered the analysis.

## Evidence available before analysis

- [README](https://github.com/risaac09/alchemy/blob/b7ae829/README.md)
- [CLAUDE.md](https://github.com/risaac09/alchemy/blob/b7ae829/CLAUDE.md)
- [HONEST-ACCOUNT.md](https://github.com/risaac09/alchemy/blob/b7ae829/HONEST-ACCOUNT.md)
- [docs/PRODUCT.md](https://github.com/risaac09/alchemy/blob/b7ae829/docs/PRODUCT.md)
- [embodied-service/README.md](https://github.com/risaac09/alchemy/blob/b7ae829/embodied-service/README.md)
- [app.js](https://github.com/risaac09/alchemy/blob/b7ae829/app.js)
- [embed-funnel.js](https://github.com/risaac09/alchemy/blob/b7ae829/embed-funnel.js)
- [LICENSE](https://github.com/risaac09/alchemy/blob/b7ae829/LICENSE)

No participant material was available or used.

## Station completion

| Station | Required | Status | Evidence |
|---|---|---|---|
| Ground | Yes | Complete | Practice, boundary, evidence, affected groups, and disconfirming condition recorded |
| Observe | Yes | Incomplete | No human walker; AI design analysis does not satisfy first-person Observe work |
| Map | Yes | Complete | Four separate access readings recorded over the seven-surface set |
| Trace | Yes | Complete | Consent, attribution, return, exposure, extraction, and burden traced from repository evidence |
| Adapt | Yes | Complete | Inbound correction route selected and executed through Alchemy pull request 15 |
| Return | Yes | Complete | Public report and structured record returned without participant material |

Because required Observe work is incomplete, this record cannot claim a completed journey.

## Human Observe status

Status: `not-performed`. An AI agent has no somatic or first-person register. The assessor instead analyzed design conditions: the seven-item cap, 72-hour decay, 90-day compost, absence of streaks and badges, 30-second settle, body check, resurfacing loop, and opt-in decay notifications. That analysis may describe the practice. It does not replace a human account of attention or the body.

## Access readings

The record keeps the names used at the assessed kit version alongside the current plain-language names. No composite was calculated.

| Reading | Artifact result | Limits |
|---|---|---|
| Understandable, formerly legibility | 6/7 selected surfaces had a reachable plain-language description | The Chrome extension had no documentation beyond its manifest |
| Reachable, formerly permeability | 7/7 selected surfaces were publicly reachable | Inbound response time was `unmeasurable`; pull requests were deprioritized |
| Adaptable, formerly forkability | 7/7 had MIT reuse permission; 6/7 had enough instructions for the assessor to judge adaptation support | The Chrome extension remained the documentation gap |
| Traceable, formerly provenance | 4/7 sampled claims verified; 2/7 partly verified; 1/7 unverified | The instrument could not distinguish missing provenance from intentional, accountable deletion |

### AI system annex

For the embodied-service component, the assessor defined the unit as a Cloudflare Worker with a version-pinned model call and prompt, deterministic crisis pre-screen, input allowlist, durable rate limits, daily spend cap, no content logging, and static UI. The service was SEL-1, experimental, with its gate uncleared. The model weights belonged to a third party. Live verification and an independent re-grade remained open.

## Reciprocity readings

- **Consent, assessor reading: Usable.** The local tool held no owner-side participant record. The funnel email was optional and skippable. The embodied service disclosed third-party processing and no worker-side content storage. No affected user challenged this reading.
- **Attribution, assessor reading: Usable.** The repository disclosed the Metabolizer and absorbed-diagnostic lineages. No user identification was available because no user record entered the test.
- **Meaningful return, assessor reading: Usable, not Shared.** The assessor read the free practice, diagnostic report, user-held retained material, and honest account as forms of return. No affected party confirmed that the return was meaningful, and users did not share governance.

These are single-assessor readings. They do not establish meaningful return for affected people.

## Agency action and materiality

FT-001 did not predefine a person-level agency action. After analysis, the adaptation supplied a candidate action for follow-up:

| Field | Entry |
|---|---|
| Actor | Local-tool users |
| Action | Correct |
| Operational definition | Submit a correction or field report through the named GitHub issue route and receive a maintainer response without relying on a pull request |
| Predefined before analysis | No |
| Baseline | Zero inbound field reports; pull requests deprioritized; no dedicated inbound route documented |
| Follow-up | Pending through 2026-11-22 |

FT-001 also lacked a predeclared materiality rule for exposure, extractability, or shifted burden. The follow-up cannot turn those missing readings into favorable evidence.

## Burden, exposure, and extractability by affected group

| Affected group | Baseline reading | Follow-up status |
|---|---|---|
| Local-tool users | Content remained in the user's browser or vault; users paid time and possible loss created by settle, body-check, and decay rules | Public-issue exposure, reuse paths, and correction effort pending |
| Funnel visitors | Optional email could pass to the host page; the embedded app did not store it | Adaptation not tested with funnel visitors; outcome pending |
| Past buyers | No buyer record entered the test; buyers had paid $29 for the earlier product before the concept returned free | Adaptation not tested with past buyers; outcome pending |
| Embodied-service users | Reflections passed to a named model provider without worker-side storage; provider-side behavior was not inspected | Adaptation not tested with service users; outcome pending |
| Maintainer | Public repository and design account were exposed; the maintainer directed and reviewed the work | Triage burden, criticism exposure, and implied support expectations pending |

No affected-party follow-up result is available. The record therefore makes no finding about material increase.

## Disagreement, objection, and contestability

Two assessor-side disagreements remain open:

1. The traceable construct reads missing retained provenance as a gap. Alchemy treats visible, accountable ephemerality as an intentional feature. The instrument needs separate categories without treating deletion as favorable by default.
2. The assessor interpreted the journey as adding some analytic value. Familiarity, review time, or the extraction-check vocabulary alone may explain the same reading.

Participant-objection status: `not-sought`. No affected user challenged the analysis, correction route, refusal route, or intended benefit.

Contestability status: `not-tested`. [Alchemy pull request 15](https://github.com/risaac09/alchemy/pull/15) added a GitHub issue route for corrections and field reports. The maintainer remained the review authority. No affected party tested whether the route was accessible, timely, or effective, and the test did not exercise a refusal route.

## Adaptation and open follow-up

The assessor selected one README paragraph naming GitHub issues as the inbound route for corrections and field reports and linking to the PureLand journey and field-test form.

- Status: executed on owner consent, 2026-08-24.
- Evidence: [Alchemy pull request 15](https://github.com/risaac09/alchemy/pull/15), merged as `bf5e411`.
- Intended benefit: create a visible correction and return path without changing the deliberate pull-request posture.
- Possible new harm: triage burden and an implied support promise that the honest account declines.
- Observation window: 2026-08-24 through 2026-11-22.
- Follow-up evidence: inbound-report count, handling burden, affected-user challenge, and possible new harm.
- Current follow-up status: open. No follow-up finding is available.

## Rights, privacy, and public return

The test used public repository evidence and no participant material. The owner permitted the repository analysis, AI assistance, research use, and public return. This report does not permit claims about affected-user experience.

Public privacy review:

- [x] No participant recordings, transcripts, identifying data, contact details, or protected knowledge are included.
- [x] Every linked artifact is public and rights-cleared for this record.
- [x] AI assistance and human verification are disclosed.

## Outcome

Tested design-hypothesis classification: `unmeasurable`. No ordinary-review or single-instrument comparator was run.

The primary hypothesis is also `unmeasurable`. FT-001 lacks a human Observe result, a predefined person-level action, an observed action follow-up, an affected-user challenge, a predefined materiality rule, an independent reader, and a completed observation window. It supports no causal claim, primary-hypothesis claim, or attention-sovereignty result.

The report and JSON record are a `public-return` of a partial dry run. Public return does not make the return meaningful to affected people and does not turn the test into validation.

## Assessor interpretation and competing explanations

The assessor interpreted the walk as surfacing four readings not explicit in the named Alchemy documents: the provenance-versus-finitude tension, decay as a designed cost of absence, the diagnostic tuning loop, and the second-reader parallel between the embodied service and PureLand. Two headline findings were already documented by Alchemy.

This interpretation competes with the assessor's familiarity with both repositories, the time spent, the extraction-check vocabulary, the assessor-chosen boundary, maintainer-side evidence selection, and the lack of a second reader. FT-001 cannot separate these explanations.

## AI assistance

Claude Code performed repository analysis, artifact counting, and drafting on 2026-08-24 under maintainer direction. The maintainer reviewed the pull request landing the record. AI output was checked against the source files cited above. The record distinguishes the six product surfaces named in `docs/PRODUCT.md` from the seven-surface assessment boundary that adds the embodied service.
