# Field test FT-001: the journey walked on Alchemy

The first recorded walk of [the journey](../../JOURNEY.md), run on the [Alchemy app](https://github.com/risaac09/alchemy) as the assessed practice. This is a worked example, not an independent trial: the assessor is an AI agent working for the kit's maintainer, on the maintainer's own app. It does not count toward the version 0.2 gate, which requires independent applications. Structured record: [data/field-tests/ft-001-alchemy.json](../../data/field-tests/ft-001-alchemy.json).

## Context

| Field | Entry |
|---|---|
| Kit version or commit | 62259ec, 2026-08-24 |
| Practice and system boundary | The Alchemy repository at commit b7ae829: seven public surfaces (PWA, embed funnel, Obsidian plugin, Chrome extension, iOS wrapper, bookmarklet, embodied service), read as one published information-metabolism practice |
| Assessor's relationship to the practice | An AI agent (Claude Code) directed by the practice's owner and maintainer; not independent |
| Scope | The whole journey |
| Why this scope | The journey shipped the same day; its first test should be the full sequence, and the kit names Alchemy its companion app, so the companion is the natural first subject |
| Second reader | None available; recorded as a failure below |
| Known exclusions | The live deployed site and app stores were not exercised; all evidence is the repository at the named commit plus its own documents |
| Time window | Snapshot at 2026-08-24; no longitudinal observation |

## Disconfirming condition

Written before scoring: if the walk surfaces nothing beyond what Alchemy's own README, CLAUDE.md, docs/PRODUCT.md, and HONEST-ACCOUNT.md already state, then the journey adds no analytic value over reading a well-documented repo, and the sequencing hypothesis in [RESEARCH-STATUS.md](../../RESEARCH-STATUS.md) loses its first support.

Verdict, written after: partially defeated. Four readings below do not appear in those documents (the provenance-versus-finitude category strain, decay as a designed cost of absence, the diagnostic composite tuning the app's constants as a behavior-shaping loop, and the second-reader parallel between the embodied service and this kit). Two headline findings were already documented by the practice itself (the Chrome extension documentation gap, the pull-request posture). The journey found less that was new than the walk's length suggests, and what it found came mostly from the extraction check's framing, not the counting.

## Station 1: Ground

Practice named above. Purpose, in the practice's own words: a tool built around human finitude instead of infinite engagement. Affected people: users of the free PWA and plugin, past buyers of The Metabolizer ($29), visitors who meet the embedded diagnostic on the marketing site, users of the embodied reflection service, and the owner. Evidence available before scoring: the repository's own documents (README, CLAUDE.md, docs/PRODUCT.md, HONEST-ACCOUNT.md, embodied-service/README.md), the source files, and stack-data's repo registry. No participant material exists or was used; the protocol branch was not taken. The AI branch was taken for one component, the embodied service.

## Station 2: Observe

**Method failure, recorded first:** the practice frame assumes a human assessor. An AI agent has no somatic register, so the self-observation this station requires could not be performed. The station ran as design analysis instead, reading the practice against the condition table. A human walker must redo this station for it to count.

Read as design analysis: the practice designs against greed (the 7-item cap, 72-hour decay, 90-day compost), against sensual desire (no infinite continuation, no streaks or badges), and against dullness (forced 30-second settle, a one-word body check before reflection). The condition most present in the design is restlessness: a resurfacing loop returns one archived item every 3 days, and opt-in decay notifications nudge before dissolution. Both are bounded and disclosed, and the diagnostic tuning stretches the resurfacing window for users whose return flow reads weak, which moves in the calming direction.

## Station 3: Map (four accesses)

Unit: a public surface of the repository. Set: the six surfaces named in docs/PRODUCT.md plus the embodied service. Denominator: 7. Window: the named commit. No composite.

**AI system annex, carried into this station per branch question 2.** The audited unit for the AI component was defined before any counting. The embodied service is a Cloudflare Worker with a version-pinned model call and a verbatim version-pinned prompt, a deterministic crisis pre-screen that answers without calling the model, input validation with an allowlist, durable rate limits and a daily spend cap, no content logging, and a static UI. Status: SEL-1, experimental, gate not cleared, and the service says so at /api/status. The system is not an open AI system in the OSAID sense: the weights are a third party's. The open obligation the annex surfaces: the live verifications and the independent re-grade are still owed, and the grader must be someone who did not write the prompt.

**Legibility: 6/7.** Six surfaces have a reachable plain-language description (README, ios/README.md, embodied-service/README.md, docs/PRODUCT.md). The Chrome extension has no documentation beyond its manifest; the practice's own PRODUCT.md names this gap. Extraction question: mapping this system easier benefits forkers, not an extractor, since there is nothing behind it to reach.

**Permeability.** Publicly reachable: 7/7. Documented inbound routes: forking is explicitly invited; issues are in active use by the practice's own review ritual; pull requests are explicitly deprioritized ("generally not reviewed: this is a personal tool with deliberate constraints"). Median response time: `unmeasurable`, no record. One traced path with its permission boundary: the embed funnel's email travels by postMessage to the host page, which owns capture; the app never stores or sends it, and the field is optional with a visible skip (verified in embed-funnel.js). Extraction question: opening the boundary exposed nothing carrying different consent, because the practice holds no participant material.

**Forkability.** Explicit reuse permission: 7/7 (MIT, whole repository). Enough instructions to adapt: 6/7 (the Chrome extension again; the embed contract is documented inside embed-funnel.js). The README actively transfers the practice: "fork it and make it yours."

**Provenance**, over a sampled claim set of 7, not exhaustive. Verified 4: the Metabolizer lineage (README plus INTEGRATION-PLAN.md); the no-external-calls claim (a search of app.js finds no fetch, XHR, beacon, or analytics call); the surface separation (index.html loads app.js only; the funnel code states and keeps the boundary); the diagnostic-reactive tuning (app.js lines 66-71). Partly verified 2: the plugin and iOS version claims (files and manifests exist; store and community submission states are unverified, which PRODUCT.md itself flags). Unverified 1: the README claim that the plugin is findable under Obsidian Community Plugins. Intentionally anonymous: 0. Extraction question: traceability here creates no re-identification risk; there is no person in the record.

**Category disagreement, preserved:** the scorecard's provenance access assumes that keeping records of origin and transformation is a virtue. Alchemy's decay deletes unattended and composted material unrecoverably, on purpose; the practice's own account calls the loss real and sometimes wrong, and still the feature. The instrument and the practice disagree about whether designed ephemerality is a provenance failure. Not resolved here.

## Station 4: Trace (extraction check)

Value trace. PWA and plugin users: attention and captured content leave the person into their own browser or vault; nothing accumulates with the owner; what returns is the practice itself and the retained gold. Funnel visitors: an optional email leaves to the host page and accumulates with the owner; what returns is the diagnostic report and a follow-up offer, with a working skip. Metabolizer buyers: $29 left them historically; the concept returned to everyone free, and the README addresses those buyers directly. Embodied-service users: a reflection leaves to a third-party model provider under that provider's terms, is not stored or logged by the worker, and a governed reflection returns.

Bands, separate, with no averaging:

- **Consent: Usable.** The PWA collects nothing, so there is nothing to consent to; export and deletion are user-held. The funnel email is optional, skippable, and never stored by the app. The embodied service names third-party processing and does not store content. Burden: low. Disagreement: none found.
- **Attribution: Usable.** Lineage is public (Metabolizer, the absorbed diagnostic repo), MIT keeps origin visible through reuse, and no identification of users is possible because no user record exists.
- **Value return: Usable, not Shared.** The free tool returns a paid product's concept to everyone, and the honest account returns the failures too. Users do not help govern the terms, and no mechanism exists for them to; that is what keeps this band below Shared.

Attention sovereignty. Contact is user-initiated; the only outbound cue is an opt-in decay notification. Stopping carries no manufactured loss, no streaks, no penalty mechanics; but stopping does carry a designed real loss: unattended items dissolve at 72 hours, so absence costs captured material. The practice's account owns this ("some of what decays mattered... the loss is not recoverable"). Recorded as the sharpest sovereignty tension in the design: decay is both the anti-hoarding mechanism and a cost imposed on the person who walks away.

Sovereignty paradox: the protective friction (settle, body check) costs adoption, which the account admits. The user pays time; the owner pays reach. The safeguards increase the participant's agency rather than reducing the owner's liability.

Collective lens: largely not applicable to a single-user local tool. The borrowed register ("information metabolism," the liver, the alchemical frame) is disclosed as metaphor by the practice itself.

The embodied service's consent posture, traced here rather than in the annex: reflections go to the named third-party provider under its terms, unstored and unlogged by the worker, and the annex's open obligation (the independent re-grade) is recorded at station 3.

## Station 5: Adapt

One bounded adaptation, chosen from the trace: the practice invites forks out but documents no return path in. Pull requests are deprioritized by design; nothing tells a user or forker where a correction, a failure report, or a field test of Alchemy should land. The kit's thesis is that a fork is judged by both directions of travel.

- Baseline: zero inbound field reports; PRs deprioritized; issues used only by the owner's own ritual.
- Change to test: one README paragraph in the Alchemy repo naming the inbound route: field reports and corrections as issues, linked to this kit's journey and field-test form.
- Consent needed: the owner's. The live PWA is public-facing and gated; this walk does not touch it. **Status: proposed, not executed.**
- Intended benefit: a return path, closing the loop the practice's own fork-table draws.
- Plausible new harm: triage burden on a personal tool, and an implied promise of support that the honest account explicitly declines.
- Observation window: 90 days, one compost cycle. Review date: 2026-11-22. Follow-up evidence: count of inbound reports and what they cost.

No causal claim is made or available.

## Station 6: Return

This report and its JSON record are the return, submitted by pull request per FIELD-TESTING.md and linked from the [field-trial ledger](../../FIELD-TRIALS.md).

## Failure and burden

- The observe station cannot be executed as designed by an AI assessor; it ran as design analysis and needs a human redo.
- No second reader existed; every count above is single-assessor and no disagreement could be preserved except the assessor's own, which is structurally weaker.
- Legibility was judged from inside the practice's orbit; "a person outside the core" was simulated, not real, and the scores may be generous.
- The journey gave no guidance on bounding a multi-surface repository; the seven-surface set was the assessor's choice, and a different bounding would change every denominator.
- The provenance access and the practice's designed ephemerality conflict; the instrument has no category for virtuous deletion.
- Burden: roughly two hours of agent time plus the owner's review; a careful human walk would take substantially longer. Who did the work: the maintainer's side, entirely.

## Adaptation summary

See station 5: proposed README inbound-route paragraph in the Alchemy repo, pending owner consent, 90-day window. Not executed in this walk.

## Privacy check

- [x] No participant material or identifying data is included.
- [x] The assessor has authority to link every artifact cited; all are public repository files.
- [x] AI assistance and verification are disclosed: an AI agent (Claude Code) performed the repository analysis, counting, and drafting on 2026-08-24; the human verification is the owner's review of the pull request that lands this report.
