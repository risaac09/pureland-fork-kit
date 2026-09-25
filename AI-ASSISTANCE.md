# AI assistance record

## The disclosure rule

When AI assists with source discovery, synthesis, coding, or drafting, disclose:

- the tool and model, if known;
- the date and task;
- the material provided to the system;
- how a human verified the output;
- the corrections made after verification;
- the material withheld for consent or privacy;
- the resources the assistance consumed, such as agents, tokens, or minutes, where the tool reports them, or `not recorded`.

An absent resources line reads as not recorded, never as none.

AI output is not a source. Cite the document that supports the claim. Every entry below is written against this rule, and [RESEARCH-STATUS.md](RESEARCH-STATUS.md) points here rather than restating it.

## 2026-09-25 energy and water row, and a resources line in this rule

| Field | Record |
|---|---|
| Tool | Claude Code. The model attribution is carried by the commit trailer |
| Task | 2026-09-25. On the maintainer's request to ground his internal system's self-improvement in the kit's relation to the earth and the environment, find what the kit says about the physical cost of the AI systems it audits and about the cost of AI assistance to the kit itself, and propose the smallest change. Landed as an energy and water row in `AI-SYSTEM-ANNEX.md`, a resources line in this rule with an optional `ai_assistance.resources` field in `data/field-test.schema.json`, a sentence in `templates/field-test.md`, two tests in `scripts/test_check_repo.py`, and this record |
| Material provided | The repository at `d741a7a`. The maintainer's request and his choice of scope among three offered options. No participant material entered the session or the repository |
| Source verification | A search of every Markdown file in the kit for energy, electricity, water, carbon, and ecology returned nothing. That is the finding, and it is recorded in the pull request apart from the change. No external figure was used, and the row forbids borrowing one. `scripts/check_repo.py`, its 32 prior unit tests, and both gap probes pass. The new fixture fails against the pre-change schema with "Additional properties are not allowed ('resources' was unexpected)" and passes after |
| Corrections after verification | The row was drafted as "Energy, water, and hardware". It carries the maintainer's own words, "energy and water", and hardware stays out until someone asks for it |
| Resources | Part of a larger internal pass in the maintainer's private operations repository: 8 subagents, about 1.67M subagent tokens, 54 minutes before any change was written. The kit changes were made in the main session, whose share for this pull request was not recorded separately |
| Human review | Pending. The maintainer decides whether the row and the rule change belong in the kit, and merges or not |
| Sensitive material | None. Nothing from the private repository beyond the resource figures above entered this record |

## 2026-09-23 two tracks of knowing and the Ackoff citation

| Field | Record |
|---|---|
| Tool | Claude Fable 5.1 in Claude Code. The model attribution is also carried by the commit trailer |
| Task | 2026-09-23. On request, write into the kit a distinction the maintainer dictated in conversation: embodied awareness developing into insight through mindfulness on one side, Ackoff's data-to-wisdom ladder for information systems and digital life on the other, and the kit's purpose of supporting awareness of how digital and embodied life integrate. Cite Ackoff. Landed as a section in `THESIS.md`, a source entry in `PROVENANCE.md`, a fields-and-limits row, two rows in `RESEARCH-STATUS.md`, and this record (#60) |
| Material provided | The repository at `c8966fd`; the maintainer's dictation; a transcript of the maintainer's 2026-09-22 call with a collaborator, used only to confirm how he describes the kit's motivation in his own words. No participant material entered the repository |
| Source verification | Ackoff's bibliographic details (journal, volume, year, pages) were checked against two independent reference records by web search; no open-access copy of the paper was located and the provenance entry says so. Eliot's chorus and the 1934 first performance were checked against the play's public record. The kit was searched for any existing use of the ladder before writing; none exists, and the maintainer's own 2025 essay in his private corpus is the only prior citation of Ackoff in his work. `scripts/check_repo.py` and the unit tests pass |
| Corrections after verification | A first draft of the thesis section described the motivating claim as "unstated until now"; that characterized the maintainer's history rather than his words, and was cut. The section says the claim is his and marks it as an untested hypothesis. The improvement protocol reserves changes to the thesis for field evidence; the session read that as a bar on the organizing argument in the blockquote, which is unchanged, and not on framing prose beside it, and says so in the pull request so the maintainer can overrule the reading. A review pass on the branch found three more: the claim that everything a person can know arrives at a sense door rested on the Sabba Sutta, which the provenance record did not carry, so SN 35.23 was added and linked; the Ackoff paragraph read as a paraphrase of a paper no copy of was read, so the thesis and the provenance entry now say the description follows the standard summary; and "usually names four" overstated how often the kit names the ladder at all |
| Human review | Pending. The maintainer reviews the section against what he meant, decides whether the two-track cut is the right one, and merges or not |
| Sensitive material | The call transcript stayed in the session's scratch directory and in the maintainer's own files; nothing from it beyond the maintainer's own description of the kit was used, and no other party's words were quoted |

## 2026-09-21 human-review rows filled for four merged pull requests

| Field | Record |
|---|---|
| Tool | Claude Fable 5.1 in Claude Code. The model attribution is also carried by the commit trailer |
| Task | 2026-09-21. Replace the four `Human review: Pending` rows for #54 (two entries), #57, and #58 with what the maintainer stated in conversation: he read all four diffs and merged each on green CI. No other row changed |
| Material provided | The repository at `ef3fb75`, the maintainer's one-sentence dictation, `git tag`, and `gh release list`. No participant material |
| Source verification | Each PR's merge date and merger were read from `gh pr view`; the tag and release dates from `git tag` and `gh release list`. The dictation is the maintainer's own statement about his own act and is recorded as such, not verified by any other means |
| Corrections after verification | None |
| Human review | The maintainer supplied the sentence being recorded, reviews the wording, and merges the pull request |
| Sensitive material | None involved |

## 2026-09-21 improvement-protocol row for a new instrument

| Field | Record |
|---|---|
| Tool | Claude Code, remote session. The model attribution is carried by the commit trailer rather than restated here |
| Task | 2026-09-21. Log the session's learnings on request. The one not already recorded was a gap in the triage table in `IMPROVEMENT-PROTOCOL.md`, found by #44; this adds the missing row, records the second batch against the table, and pays what the new row asks for on `scripts/ecosystem_inventory.py` |
| Material provided | The repository at `aec2134`, and this session's own record of the two batches triaged against the protocol. No participant material |
| Source verification | The gap was checked rather than assumed. All seven existing rows were read and each describes changing something that already exists: an instrument's wording, a construct's definition, a rule in the schema or checker, a falsifier, the ledger, the thesis. #44 added an instrument and matched none. The consequence was measured directly: `grep -i` over `RESEARCH-STATUS.md` and `TOOLBOX.md` returns nothing for the script, and `grep -rln` over every Markdown file finds it named only in `CHANGELOG.md`. The falsifier written into the new ledger row is the script's own, quoted from its module docstring, not one composed for it. `scripts/check_repo.py` passes with the standing changelog warning, and the 32 unit tests, `test_classification_gap.py` and `test_performed_gap.py` pass |
| Corrections after verification | A first version of the ledger row waited for the first run before recording the claim, on the reasoning that a row needs evidence. That was backwards: `RESEARCH-STATUS.md` holds claims with the evidence they still need, and predeclaring is the discipline the kit asks for everywhere else. The row is written now, before any run, and says no run exists |
| Human review | 2026-09-21: the maintainer read the full diff of #58 and merged it on green CI. The row stays and the instrument's claim stands as written. Neither the protocol nor its triage table has yet been used by anyone other than the session that wrote them |
| Sensitive material | None involved |

## 2026-09-19 release 0.1.1

| Field | Record |
|---|---|
| Tool | Claude Code, remote session. The model attribution is carried by the commit trailer rather than restated here |
| Task | 2026-09-19. Cut release 0.1.1 on request: move the `## Unreleased` entries under a dated heading, draft the release framing, bump `CITATION.cff`, and add the missing changelog line for #56 |
| Material provided | The repository at `c7b2061`. `GOVERNANCE.md` for what a release decision requires, `TESTING.md` for the version 0.2 gate, `scripts/check_repo.py` for `check_version_claims` and the drift warning, and the GitHub release and tag list. No participant material |
| Source verification | The version number was decided from the code and the gate rather than from convention. `check_version_claims` states that the patch level stays `CITATION.cff`'s alone while the prose names major and minor, so `0.1.1` leaves the three entry-point sentences correct and unedited; the checker confirms it. `0.2` was refused because `TESTING.md` makes it a research gate of five to ten independent applications across at least three contexts and `CURRENT-EVIDENCE.md` records none. The twenty pull request numbers in the new section were counted from the section itself, not from memory. The previous release was read from the GitHub release list: `v0.1.0`, tag at `53ebf43`, published 2026-09-02. `scripts/check_repo.py` now reports 0 warnings, the drift warning having cleared, and the 32 unit tests, `test_classification_gap.py`, and `test_performed_gap.py` pass |
| Corrections after verification | A first framing said "Nineteen pull requests since 0.1.0". Two faults: #56 had merged that day with no changelog line at all, and "since 0.1.0" would have had to account for #45, closed unmerged, and #53, which corrected #37's bullet in place rather than adding one. The missing #56 entry was written and the sentence became "Twenty pull requests are named below", which is checkable against the section. #53 still has no line of its own, which is the existing convention for a correction to an entry rather than a change to the kit. Cutting the release then broke a test: `test_unreleased_entries_warn_from_changelog` asserted the drift warning while reading the repository's own `## Unreleased` section, so emptying that section failed it. The rule was left alone and the test was given its own seeded entry, matching the sibling that already built the empty case, then checked against a deliberately disabled drift rule to confirm it still fails when the rule is wrong |
| Human review | 2026-09-19: the maintainer read the full diff of #57, merged it on green CI, and cut the release himself: tag `v0.1.1` and the GitHub release PureLand 0.1.1 exist, created 2026-09-19. Pages and release state were his verification, as `GOVERNANCE.md` reserves; no check performs it |
| Sensitive material | None involved |

## 2026-09-19 improvement protocol

| Field | Record |
|---|---|
| Tool | Claude Code, remote session. The model attribution is carried by the commit trailer rather than restated here |
| Task | 2026-09-19. Draft `IMPROVEMENT-PROTOCOL.md` on request, after the agent-lane walk produced seven proposals and the kit had no stated procedure for what happens to a finding. Linked it from `METHOD.md`, `TOOLBOX.md`, `CONTRIBUTING.md`, and `llms.txt`, and added its two falsifiers to `RESEARCH-STATUS.md` |
| Material provided | The repository at `b0d0fbc`, read for what `CONTRIBUTING.md`, `GOVERNANCE.md`, `TESTING.md`, `RESEARCH-STATUS.md`, `CURRENT-EVIDENCE.md`, and `AI-ASSISTANCE.md` each already own, so the new file would restate none of them. The maintainer's choice between three readings of the request, made in conversation. No participant material |
| Source verification | Every ownership boundary the file claims was read from the file that holds it rather than assumed. The one worked case in the never-weaken section, the traceable construct revised after FT-001 read intentional deletion as a provenance gap, was taken from `research/field-tests/ft-001-alchemy.md` and `CURRENT-EVIDENCE.md`, both of which record the revision as untested and neither of which records a re-read. The seven triaged proposals are the walk's own, unchanged. `scripts/check_repo.py` passes at 38 Markdown files with the standing changelog warning, and the 32 unit tests pass |
| Corrections after verification | A first outline gave the file an intake form and a merge checklist, which `CONTRIBUTING.md` and `GOVERNANCE.md` already own; both were cut and replaced with pointers, because a second copy drifts from the first. A first draft asserted the declined-proposal table was empty because nothing had been declined; the table now says an empty table is the current state and not a claim that nothing has ever been turned down |
| Human review | 2026-09-19: the maintainer read the full diff of #54 and merged it on green CI, adopting the procedure. The limit stands: a procedure written by the person holding merge authority does not constrain that person, and the file still says so in its closing section |
| Sensitive material | None involved |

## 2026-09-19 agent-lane walk

| Field | Record |
|---|---|
| Tool | Claude Code, remote session. The model attribution is carried by the commit trailer rather than restated here |
| Task | 2026-09-19. Read the repository five times from a different position each time and record what held and what gave way, on request. Wrote `research/agent-lane-walk-2026-09-19.md`, listed it in the research lane index, and made this disclosure |
| Material provided | The repository at `7543635`, read in full apart from the license texts, the fonts, and the binary design assets. No material from outside the repository. No participant material |
| Source verification | Every claim in the walk was run before it was written. `scripts/check_repo.py` passes at `7543635` with one changelog warning, after `pip install -r requirements.txt`; it exits 1 on a missing dependency rather than skipping the record rules. The four mutation probes ran against a copy of the tree under a scratch directory, and the tracked record was restored and re-checked. The leftover-marker regex and the three prohibited score names were read from the script; the 39 closed objects and the `human_observe` requirements were counted from the schema. Word counts were measured with `wc`. The absent ceiling sentence in `templates/field-test.md` and the absent links out of `EXTRACTION-CHECK.md` were checked by grep over the whole file, not by reading the opening |
| Corrections after verification | A first reading recorded the checker as exiting 0 on a missing dependency. That was wrong: the 0 came from a pipe, and a direct run exits 1. The claim was dropped rather than published. A first draft of the walk quoted the three leftover-marker tokens, which `scripts/check_repo.py` would have flagged in the quoting file; `CROSSWALK.md` already states why that quotation cannot be made, and the sentence was rewritten to point at the script. A first draft read `EXTRACTION-CHECK.md` as carrying no ceiling at all; it carries a weak one in its closing line, and the finding was narrowed to the missing link home and the missing word unvalidated |
| Human review | 2026-09-19: the maintainer read the full diff of #54 and merged it on green CI, so the reading sits in the research lane. None of the seven proposed corrections was made by that merge; #58 later added one triage row that #44 had exposed. The walk remains one model's reading with no second reader, and its four probes are the only reproducible part |
| Sensitive material | None involved. No participant, client, identifying, confidential, consent, or protected community material entered the walk. The scratch copy used for the probes stays outside the repository |

## 2026-09-18 changelog correction for #37

| Field | Record |
|---|---|
| Tool | Claude Opus 5 in Claude Code |
| Task | 2026-09-18. Correct the `CHANGELOG.md` bullet for #37, which understated the rule that pull request shipped |
| Material provided | The repository at `66ea814`. The discrepancy surfaced while merging `main` into `v02/r1-merged-08` for #44, whose held branch carries a fuller wording of the same bullet. No participant material |
| Source verification | `git log -S` traced all three understated facts to one commit, `f875275`, which is #37's own: the support-side incomplete-step rule in `scripts/check_repo.py`, the `incomplete_step_fixture` third variant in `scripts/test_classification_gap.py`, and the line adding that probe to `.github/workflows/validate.yml`. The commit's diff was read directly to confirm it added five support conditions where the bullet named four, and three probe fixtures where the bullet named two. `.github/workflows/validate.yml` was read for the trigger wording. The bullet sits under Unreleased, so no released record is rewritten. `scripts/check_repo.py`, the 32 unit tests, and the classification probes pass |
| Corrections after verification | The first reading of this discrepancy assumed the fuller wording on #44's branch was the correct one and could simply be carried over. It was not carried over. The history check came first, because the alternative explanation, that a later pull request added the rule and the #37 bullet was accurate for #37, would have made the change wrong. The wording here is written from `f875275`'s diff rather than copied from the held branch, and the CI clause names the actual triggers |
| Human review | The maintainer reviews and merges the pull request. This is a correction to the record of a change, not a change to the method or the instruments |
| Sensitive material | None involved |

## 2026-09-17 collaborator provenance entry

| Field | Record |
|---|---|
| Tool | Claude Fable 5.1 in Claude Code |
| Task | 2026-09-17. Add a `PROVENANCE.md` entry for Samara's Sanctuary Studios' theory of change, after the maintainer attributed the four-term outcome framing he is drafting toward to that source and asked for the entry |
| Material provided | The repository at `bbddae0`; the maintainer's statement and attribution in conversation; a private transcript of Justin Taylor's S³ prototype presentation; the public Open Collective, Substack, and Say Why pages the entry links. No participant material |
| Source verification | The quoted sentence was fetched from the Open Collective page on 2026-09-17 and matches verbatim. The Substack post was fetched the same day; it carries the developmental-infrastructure framing and not the sentence, so the entry cites it for the account of the studio only. The Say Why page was fetched and names Justin Taylor and the studio, spelled there as Samara Sanctuary Studios. The spoken variant in the private transcript, "generates harmonic organizations for prosperous work," is not quoted in the kit. `scripts/check_repo.py` and the unit tests pass |
| Corrections after verification | The first draft of the maintainer's private note on this source treated it as unfetchable and gated naming Justin Taylor on a consent decision. Both were wrong: the sentence is published under S³'s name, and the Say Why episode naming him has been public since 2026-06-30. The maintainer's instruction, name the source and quote it with a link, set the entry's form. Program outcome figures spoken in the private transcript were left out because they are not on the linked pages |
| Human review | The maintainer asked for the entry and reviews and merges the pull request. The maintainer vouches for the attribution on the basis of the working relationship; corrections from S³ enter through `CONTRIBUTING.md` |
| Sensitive material | The private presentation transcript and the maintainer's private notes stay outside the repository |

## 2026-09-14 front-page promotion

| Field | Record |
|---|---|
| Tool | Claude Fable 5.1 in Claude Code |
| Task | 2026-09-14. Promote the Field & Form draft merged in #50 into the root page, the README, and the active design assets, following the integration sequence in the draft's specification, after the maintainer viewed the desktop and phone layouts and asked for the promotion |
| Material provided | The repository at `0e853f5`, the draft's specification and review, and the maintainer's instruction in conversation. No participant material |
| Source verification | The root page is the reconciled draft with its asset paths resolved, the draft strip removed, and anchors for the two retired fragments; its body copy was not changed, and the title, description, and footer line are the promotion's. `design/tokens.json` was written from `design/tokens.css` and a new checker rule fails when they differ, with seven regression tests. `scripts/check_repo.py`, the regression tests, and the classification probes passed. The page rendered at 1280 and 390 px from the branch without horizontal overflow, with both themes, the fragment routes, the legacy anchors, and the script-free structure checked. A review pass of three finders read the page and assets against the merged draft, the records and the visual-language document against the code, and the checker rule against constructed fixtures; a second pass ran before push |
| Corrections after verification | The mark asset files lost their only link when the old banner went, so the visual-language document now links them, and they still carried the retired palette's hex values, so they now take Mineral on paper and Lichen on the ink ground. The first anchor for a retired fragment sat inside a grid section and became a grid item; both anchors are zero-height blocks before their sections. The checker rule read its block before stripping comments, stopped at a semicolon inside quotes, ignored a second `:root` block, and stayed silent when one file was missing; it now strips comments first, brace-matches every block, tolerates quoted semicolons, reports a declaration it cannot read, and errors on a conflicting duplicate or a missing counterpart, with four tests covering those cases. The model index said the rule fails only on a differing value; it now says differing or missing. The visual-language document claimed a medium-weight primary action, Brass guide lines on the plate, and the documented easing on hover; both sentences now match the code and the hover transition now uses the easing |
| Human review | The maintainer accepted the design on the draft's rendering and asked for the promotion. No first-time reader has read the page; the specification's reader test remains owed before any claim that the page is easier to understand |
| Sensitive material | None involved |

## 2026-09-14 second visual-system draft

| Field | Record |
|---|---|
| Tool | OpenAI Codex for the draft; model variant and effort are not recorded in the draft's own record. Claude Fable 5.1 in Claude Code for the reconciliation, the review passes, and pull request #50 |
| Task | 2026-09-14. Review the live front page and repository against a first-time reader's needs, draft a second visual system under `design/v2/` (homepage, specimen board, README candidate, specification, review), then reconcile the draft's copy with PR #48 and the checker's contracts and prepare it for maintainer review |
| Material provided | The public repository at `88216c0`, the live page, PR #48's diff, and the maintainer's instructions outside the kit. No participant material |
| Source verification | Claims on the draft pages were taken from the canonical files named in `design/v2/SPECIFICATION.md` and read back against them after the reconciliation. `scripts/check_repo.py`, the 22 regression tests, and the three classification probes passed before and after the reconciliation. The draft rendered at 320, 390, 768, and 1280 px without horizontal overflow, in both themes, with keyboard disclosure and script-free fallback checked; the reconciled page was measured again at 320, 390, 768, and 1280 px. One adversarial review pass, five finders and a sweep with each finding verified against the files, ran on the branch after the reconciliation; its corrections are listed below. A second pass over the fix commit before push found no code regression and two prose corrections, applied |
| Corrections after verification | The draft restated the Field Pilot's terms on three surfaces, omitted the reply at Report, and announced the release as "Version 0.1", which `check_version_claims` would reject on promotion; all three were reconciled to PR #48's wording. A link inside step copy inherited the 44 px block-link rule, and the status row lost its alignment wherever a sentence wrapped; both stylesheet rules were narrowed. The README candidate had dropped the sentence that names the repository as the record behind the front page; restored. The review pass found and the branch fixes: a saved theme flashed the wrong palette before the deferred script ran (an inline script now applies it before first paint); the print stylesheet kept ink-theme colors and dropped the specimen's ground (print now forces the paper scheme and keeps the ground); a link to a step landed on a closed disclosure (the script opens the step named in the fragment); the phone status link had a 32 px target, the figcaption link none, and twelve arrow glyphs were read aloud (all corrected); the heading sizes inverted between the tablet and phone queries (the phone cap now matches); the two fork paths drew at once (the second branch now waits for the stem); the dark tokens were declared twice and eleven tokens were unused (one declaration per role with light-dark(); the spacing scale and measure removed, brass now referenced by the specimen board); the specimen board hardcoded its swatches and the research table was worded three ways (one wording now); a render-blocking import, an unused rule, and an imperceptible grain layer were removed; the README mockup linked the draft where it named the live page and shortened the evidence sentence (both now match the candidate); the Adapt step omitted two of the method's seven record fields (restored from METHOD.md); the research list's visible numbers doubled the list's own numbering for screen readers (hidden from assistive technology); the system board lacked a description and font hints (added); the specification named a model in its continuation advice (now tool-agnostic); and the review had stated a pull request in the past tense before one existed (reworded) |
| Human review | Pending. The maintainer decides whether the direction is adopted, and no first-time reader has read either page. Layout measurements are browser observations, not evidence that the method or the page works |
| Sensitive material | None involved. No participant, client, identifying, confidential, consent, or protected community material entered the draft; local paths, the originating brief, and the session record stay outside the repository |

## 2026-09-13 capture guide

| Field | Record |
|---|---|
| Tool | Claude Fable 5.1 in Claude Code, desktop app; the effort setting is not exposed in the task context |
| Task | 2026-09-13. Draft `CAPTURE-GUIDE.md` on `docs/capture-guide-2026-09-13` from `88216c0`; link it from `TOOLBOX.md` and `llms.txt`; add its two falsifiers to `RESEARCH-STATUS.md` |
| Material provided | The maintainer's brief, given in conversation: which raw material a run produces for a person on a tool, a live facilitation practice, and an organization, and that screen recording with audio or a voice note is the easiest capture for a person on a tool. The repository at `88216c0`, read for the packet, the filming forms, the protocol, the rights guide, the consent register, the schema, the agent lane, and the research-status ledger |
| Source verification | The checker and both test scripts passed on the branch at each commit, with the expected unreleased-changelog warning; every link and anchor in the new file resolves under the checker, and the file is reachable from `README.md` through `TOOLBOX.md`. Four read-only review agents read the draft against the linked files and returned 24 findings, each quoting the source it relied on; the maintainer's assistant re-checked the quoted lines before acting. This is software review, not human reader evidence |
| Corrections after verification | The draft said every evidence field holds a review status; the schema's evidence item carries an ID, description, source, and a before-analysis flag, and the review status lives in the report template. The draft attributed the leave-the-worksheet instruction to the practice frame; it is the packet's. The draft let a model transcribe a voice note, which the agent lane's never-generate list reads as a transcript; the person or a named tool now transcribes and the model may only quote. The draft sent an assessor's own transcription tool into the AI system annex, which is scoped to the assessed practice. The draft widened the repository boundary past its sources and restated the protocol's custody list; both now cite the source. The material-to-step mapping appeared twice and had already diverged; it is carried once. The two falsifiers had no ledger rows; they have them now. A pre-push pass moved the changelog line to the top of Unreleased, where the newest change sits, narrowed the Stage 2 sentence to runs that seek a public return, named the schema's public flag, and separated what footage cannot supply from what it cannot produce |
| Human review | Pending. The maintainer has not read the draft |
| Sensitive material | None. No participant, client, or identifying material was provided or produced. The brief named no person |

## 2026-09-13 reader entry and model discovery

| Field | Record |
|---|---|
| Tool | OpenAI Codex, GPT-6; exact model variant and effort unavailable in the task context |
| Task | 2026-09-13. Read the kit at `88216c0`, report, and prepare changes on `share/readiness-2026-09-13` and `share/watch-carrier-2026-09-13` |
| Material provided | The maintainer's execution prompt, outside the kit, and the repository at `88216c0` |
| Source verification | Read the source files and PR metadata at the pinned base. The working branch passed the checker, 25 regression tests, and three classification probes; the held branch passed its 22-test suite. The combined tree passed all checks and YAML parsing. The overdue simulation failed on FT-001 as expected. A Codex source audit and draft diff review completed. Frozen files, model prohibitions, license text, desktop and phone layout, and required-file discovery passed direct checks. Publication checks and final heads appear in the pull requests |
| Corrections after verification | Anchored the imported PR #45 verification to its historical branch. Marked unknown PR #46 provenance owed. Preserved schema keys while repairing live step names; added raw-link regression tests |
| Human review | Pending. Model review and automated checks supply no independent field evidence or maintainer approval |
| Sensitive material | No participant material was used. The execution prompt and private report remain outside the repository |

## 2026-09-12 reconciliation review

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Task | Review the local reconciliation candidate against current main and the held pull requests, repair reproduced inconsistencies, and prepare it for maintainer review |
| Material provided | Public repository at `655ea84`, local candidate `f3b4d60`, pull requests 44 and 45, and the maintainer's handoff and resource decisions |
| Source verification | Read the changed files against the rights guide, method, testing discipline, FT-001 report and record, ledger, workflows, and GitHub state. The original checker accepted a wrong report ID, a wrong kit version accompanied by a stray correct mention, and an artifact version with an extra suffix |
| Corrections after verification | Bound checks to identity fields and exact artifact versions; required Git reachability; added regression cases; aligned intake with the charter; added action and materiality prompts; made the release warning state only what the local check observes; linked the public routes to rendered repository packets |
| Human review | Pending. Automated tests and this model review do not count as maintainer approval or independent field evidence |
| Sensitive material | No participant material was used. Local paths and working history remain outside the repository |

## 2026-09-11 roadmap gate reconciliation

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Task | Reconciling the unmerged Gate 1 and Gate 2 work with the current method, public offer, rights architecture, field-test records, release state, and repository checks |
| Material provided | The current public repository at `655ea84`; preserved Gate 1 commit `b256f85`; preserved Gate 2 commit `d8b3610`; the maintainer's decision that the Field Pilot should be public, may use commissioned, funded, or limited voluntary terms, and should publish no price |
| Source verification | The change was checked against `METHOD.md`, `OFFERING.md`, `RIGHTS-AND-CONSENT.md`, `GOVERNANCE.md`, `CURRENT-EVIDENCE.md`, the issue form, the FT-001 report and record, both workflows, and `scripts/check_repo.py` |
| Corrections after verification | Replaced the retired journey vocabulary with Scope, Attend, Read, Trace, Adapt, Report; kept the private no-record path; separated co-research from the public Field Pilot; required a completed charter before Stage 2; kept fees and funding separate from research, publication, and material-use permission |
| Human review | The maintainer chose the public resource model and the no-public-price rule. Review of the integrated branch remains required before push, pull request, merge, release, or publication |
| Sensitive material | None involved; no participant, client, identifying, confidential, consent, or protected community material entered the repository |

## 2026-09-09 arrival mark accent

| Field | Record |
|---|---|
| Tool | Claude Fable 5.1, from PR #46's commit co-author trailer; execution surface owed |
| Task | Change one stylesheet line in index.html in PR #46; no visible words changed |
| Material provided | Owed |
| Source verification | Owed |
| Corrections after verification | Owed |
| Human review | Owed |
| Sensitive material | Owed; the commit alone does not establish what material the model received |

## 2026-09-06 maintainer-side revision round

The rows below preserve [PR #45](https://github.com/risaac09/pureland-fork-kit/pull/45)'s historical account against `38ce830`. In these rows, "this branch" means that revision branch and the verification describes that round.

| Field | Record |
|---|---|
| Tool | Five models, one task. Candidates: Claude Opus 5 and Claude Sonnet 5 as Claude Code agent contexts with the effort setting unpinned; gpt-6-astra through the Codex CLI at reasoning xhigh, with network blocked inside its sandbox; Qwen3.6-35B-A3B at Q4 on a local llama-server as a control. Cross-readers: the same Opus 5, Sonnet 5, and gpt-6-astra, each excluded from its own candidate. Synthesis, gate, blind set, planted probe, and this branch: Claude Fable 5.1 in Claude Code, which produced no candidate |
| Task | PRs #37, #38, #39, #40, #41, #42, and #43. 2026-09-05 to 2026-09-06. Each candidate model received the same packet against `38ce830` and returned a repair proposal, an instrument design, and a self-report, plus a local branch where it had repository access. A deterministic gate ran the checker and the overdue watch on every branch, a voice linter, a privacy scan, word caps, and a network-denied sandbox run of every shipped script. The candidates were relabelled by letter beside a planted probe and read blind by the other models. The synthesizer merged what converged into this branch, one commit per change, re-implemented from the base where branches conflicted, and held every contested item open for the maintainer |
| Material provided | The packet: a public-safe task statement, the kit's facts of record at `38ce830`, a 23-row critique register compiled from two earlier model reads, the output contract, the invariants, and the reserved list, version r2. The repository at `38ce830`. The 22 published documents, fetched live by the two Claude candidates and byte-matched to the base; the Codex candidate worked from the local files. No participant material, no name, no price, no channel, and no message to anyone entered the packet or any output |
| Source verification | Every register row was checked against the live files by each candidate before it was dispositioned. The classification gap was reproduced independently three times with in-memory fixtures; the fixture on this branch was seen passing the base checker with zero errors before the fix. `python3 scripts/check_repo.py` exits 0 at every commit on this branch, `PURELAND_TODAY=2026-11-23 python3 scripts/check_repo.py --fail-on-overdue-follow-up` still fails on FT-001 exactly as at the base, and `python3 scripts/test_classification_gap.py` passes and now runs in CI. Two adversarial review passes ran on this branch before push: the first found ten defects and the second two, all fixed in their own commits; one rule question was held for the maintainer instead of changed. The rights files, the consent register, the evidence record, TESTING.md, and the page are byte-identical to the base |
| Corrections after verification | Owed at the round. No human had read the branch, and the maintainer's own gate outside this repository had not been met. The sequence recorded then was the disagreement ledger first, then the candidate, then the pull requests, each merged, revised, or held |
| Human review | Owed at the round. The blind cross-read is a second reading by other models, and a model reading another model counts as no human review |
| Sensitive material | None involved. The round's working files live outside this repository; the planted probe and the letter map are among them and are not part of the kit |

## 2026-09-04 method vocabulary

| Field | Record |
|---|---|
| Tool | Claude Code |
| Task | Renaming the method's vocabulary across the live documents: the six steps to Scope, Attend, Read, Trace, Adapt, Report; a person runs the method rather than walking a journey through stations; `JOURNEY.md` folded into `METHOD.md`; `templates/walk-with-a-model.md` renamed to `templates/run-with-a-model.md`; the free reading at Report rewritten as a reply to the maintainer's address; `index.html`, `llms.txt`, `CROSSWALK.md`, `README.md`, `TESTING.md`, `TOOLBOX.md`, `OFFERING.md`, `RESEARCH-STATUS.md`, `CURRENT-EVIDENCE.md`, `THESIS.md`, the six instrument and branch documents, `design/VISUAL-LANGUAGE.md`, `templates/field-test.md`, the issue form, and `scripts/check_repo.py` updated to match |
| Material provided | The maintainer's decisions in conversation: that the pilgrimage register (journey, walk, station) was inaccurate for a research-program prototype, the six step names proposed and accepted, the choice to fold the journey into the method, and the shape of the reply at Report (give the address, no privacy questionnaire, consent asked on the actual artifact when a use exists). Every live file named above was read in full or at every matching line before it was edited |
| Source verification | Every replacement was an exact-match substitution asserted to occur once, so no wording changed that the assistant had not read. `scripts/check_repo.py` was run after the edits and resolved every link and heading anchor, including the new `METHOD.md` anchors. A final search for the old vocabulary across live files found only schema keys, the recorded `journey` instrument value, and the word crosswalk |
| Corrections after verification | The FT-001 report's link to `JOURNEY.md` broke when the file folded; its target was pointed at `METHOD.md` and the report's prose left as written, since a record keeps the vocabulary of its version. Naming step 1 Scope collided with the template's `Scope:` coverage field and the issue form's Scope dropdown; both labels became Coverage, with the schema's `scope` object unchanged |
| Human review | The maintainer chose the vocabulary in writing before the edit and merges the pull request |
| Sensitive material | None involved. The maintainer's public address, already published in the Alchemy embed funnel, now also appears at the Report step |

## 2026-09-01 walk-with-a-model packet

| Field | Record |
|---|---|
| Tool | Claude Code |
| Task | Writing `templates/walk-with-a-model.md`, the packet a person pastes into a language model to walk the six stations on their own use of language models, and wiring it into `llms.txt`, `TOOLBOX.md`, `JOURNEY.md`, `README.md`, `CROSSWALK.md`, `RESEARCH-STATUS.md`, `index.html`, `CHANGELOG.md`, and `REQUIRED_ARCHITECTURE` |
| Material provided | The orchestrating assistant's written brief for the packet, drafted from the clean read the maintainer approved that day and fixing the packet's sections, budgets, and wiring, plus the twelve repository files it named for reading: `llms.txt`, `CROSSWALK.md`, `JOURNEY.md`, `PRACTICE-FRAME.md`, `AI-SYSTEM-ANNEX.md`, `EXTRACTION-CHECK.md`, `SCORECARD.md`, `TESTING.md`, `templates/field-test.md`, `data/field-test.schema.json`, `RIGHTS-AND-CONSENT.md`, and `CONTRIBUTING.md` |
| Source verification | Every station instruction was checked against the instrument it names, and every schema field named inside the packet (`assessor.relationship_to_practice`, `human_observe.status`, `ai_assistance`, `outcome.classification`) was confirmed present in `data/field-test.schema.json` before it was written. Nothing the packet asks a model to do sits outside the may-generate list in `llms.txt`, and nothing it hands back sits outside the hand-back list |
| Corrections after verification | The may-generate list ended its fifth item with a period as the closing item, so that item took a semicolon when the new one moved to the end. The packet was then read twice, once as the model it addresses and once as a reader who has never seen the repository, and the sentences that tripped either reader were rewritten |
| Human review | The orchestrating assistant reviewed the diff at the gate and corrected the Return step so the model leaves `human_observe.status` empty rather than writing `performed` on a confirmation; the maintainer merges |
| Sensitive material | None involved |

## 2026-08-31 hindrance renderings

| Field | Record |
|---|---|
| Tool | Claude Code |
| Task | Renaming the five hindrances in `PRACTICE-FRAME.md` to the maintainer's directed wording, craving, aversion, sloth and torpor, restlessness and worry, and doubt, adding the Pali term beside every poison and hindrance, and stating the rendering choice in the frame |
| Material provided | The maintainer's written direction naming the five exact words and asking whether their order is canonical |
| Source verification | The order was checked against the canonical sequence (kāmacchanda, byāpāda, thīna-middha, uddhacca-kukkucca, vicikicchā; Saṁyutta Nikāya 45.177 as already cited in `PROVENANCE.md`) and confirmed correct. The prior wording was the cited Sujato translation's; `PROVENANCE.md` keeps that wording so the source register stays intact |
| Corrections after verification | The renaming put aversion in both lists, where the poison is dosa and the hindrance is byāpāda. The Pali terms were added to every row so the two stay distinct, and the frame now says the doubling is deliberate rather than leaving a reader to wonder |
| Human review | The maintainer directed the wording in advance, in writing. The assistant executed and merged |
| Sensitive material | None involved |

## 2026-08-31 follow-up date guard

| Field | Record |
|---|---|
| Tool | Claude Code |
| Task | Adding `check_follow_up_date_copies()` to `scripts/check_repo.py`: for every conformant field-test record, the follow-up dates advertised on follow-up lines of `CURRENT-EVIDENCE.md` and the record's report must equal the record's `follow_up.review_date`, and the ledger row must carry the date while the follow-up is open. Wired into the per-record loop as errors, with the new failure class added to `llms.txt`'s account of what fails a run |
| Material provided | The repository at the merge of its two documentation cuts; the deferred finding from the first cut's review, which named the untied prose copies; and the maintainer's written direction to build the guard |
| Source verification | The live date copies were enumerated by grep before scoping: the ledger row and four report lines carry the date on follow-up lines, and `CHANGELOG.md` and the research snapshots carry it as dated history, which the follow-up-line scope exempts by construction |
| Corrections after verification | The guard was fired in all four failure directions before shipping: a moved record date, a moved ledger date, a deleted ledger date, and truth restored, with the strict overdue flag confirmed to exit nonzero on a simulated past date. An adversarial review pass then found a real bug the single-record repository masked: the first draft read every follow-up line of the shared ledger for every record, so a second record's row would have been attributed to the first the moment one landed. The scan is now filtered to the lines naming the record's own file, and a synthetic two-record scenario confirmed no cross-attribution and a correctly attributed mismatch. A registered guard that has never failed is indistinguishable from a broken one |
| Human review | The maintainer directed the guard and its landing in advance, in writing. The assistant executed both |
| Sensitive material | None involved |

## 2026-08-30 technology theory row

| Field | Record |
|---|---|
| Tool | Claude Code |
| Task | Adding a technology theory row to the fields-and-limits table in `THESIS.md`, with the matching clause in the each-field-fails paragraph, mirrored in `index.html`, which also moves from somatic practice to body-based practice so the two surfaces carry one wording |
| Material provided | The maintainer's written direction to add the row, and the second cut's pull-request note that named technology theory as a lens the kit uses without naming it |
| Source verification | The claim that the kit already uses the lens was checked against the tree before the changelog stated it: the Open Source AI Definition, the NIST AI Risk Management Framework, and the datasheets and model-cards papers are cited in `PROVENANCE.md` and applied in `AI-SYSTEM-ANNEX.md` |
| Corrections after verification | The draft considered naming information theory as a field in the same pass and did not, because the kit removed an unsupported information-theory contribution on 2026-08-24 and its cited sources are the political economy of information rather than information theory; adding the field would restate the removed claim |
| Human review | The maintainer directed the addition and its merge in advance, in writing. The assistant executed both |
| Sensitive material | None involved |

## 2026-08-30 second documentation cut

| Field | Record |
|---|---|
| Tool | Claude Code |
| Task | A second pass over the same repository, testing four named clusters against one sorting principle from the maintainer: this kit is Rubinstein Productions sharing its tools, read through Buddhism, information theory, and technology theory, so a document earns its place by helping someone take the tools. Folding `AGENT-READING.md` into `llms.txt`, removing `READERSHIP.md` from the kit, cutting `CROSSWALK.md` from seventeen elements to twelve, merging `HYPOTHESIS.md` into `TESTING.md`, thinning `OFFERING.md`, and moving `REQUIRED_ARCHITECTURE`, `llms.txt`, `README.md`, `THESIS.md`, `METHOD.md`, `TOOLBOX.md`, `JOURNEY.md`, `RESEARCH-STATUS.md`, `index.html`, and `design/VISUAL-LANGUAGE.md` with them |
| Material provided | The public repository at commit `bc20be3`, read in full; the open pull request this branch stacks on, including its disposition table and review record; and the maintainer's written instruction set for the second cut, which named the four clusters and required a verdict on each |
| Source verification | No new sources cited. Every duplication claimed here was read one side at a time: `HYPOTHESIS.md`'s required-observations table against its own constructs column and against the during-a-test list in `TESTING.md`, the five secondary hypotheses against the fourteen rows of the `RESEARCH-STATUS.md` ledger, the residue lists in `READERSHIP.md` against the crosswalk rows they restate, and the checker's sweep of `llms.txt` read from `scripts/check_repo.py` to confirm the folded rules keep the checks they had |
| Corrections after verification | The first plan removed the secondary-hypothesis section outright. Four of its five claims are ledger rows, but the fifth, that one bounded adaptation can increase a person's control over attention, appears in no ledger row, so the section survives as a pointer that states the fifth claim rather than a deletion that would have lost it. The first plan also left `TESTING.md` without a ceiling of its own after the merge, since the ceiling paragraph sat in `HYPOTHESIS.md`'s current-status section; it now opens the merged document. The first crosswalk pass cut three rows and left the file at 210 lines, still the longest document in the kit; two more rows went, both of them findings `llms.txt` now states itself. The record cluster was tested for a merge and kept at three documents. Two adversarial review passes over the draft, one hunting for content that now survives nowhere and one for statements the cut had made false, found five further defects, all fixed: `llms.txt` said the checker enforces reachability, which only warns, so it now separates what fails a run from what does not; `README.md` still announced six distinct jobs after the functions became five, and still promised that the reason for the two reading orders sat in a section that no longer held it; the changelog entry below miscounted the offering's possible outputs as eleven where the list had nine; and `llms.txt` claimed to say what each file is while indexing neither template, so it now names both and claims less. The lost-content pass found no rule, claim, falsifier, or evidence ceiling that survives nowhere |
| Human review | The maintainer reviews and merges the pull request. This stacks on an open pull request and changes a public repository's architecture, so it opens ready rather than draft and waits for him. No file was merged or pushed by the assistant |
| Sensitive material | None involved. No participant material, names, or consent records entered the repository, and `RIGHTS-AND-CONSENT.md`, `SECURITY.md`, `LICENSE.md`, `GOVERNANCE.md`, `CONTRIBUTING.md`, `templates/consent-register.md`, `data/README.md`, and the field-test schema have a zero diff |

## 2026-08-30 documentation cut

| Field | Record |
|---|---|
| Tool | Claude Code |
| Task | Producing a disposition for every root-level document, then executing it: merging `FIELD-TESTING.md` into `TESTING.md` and `FIELD-TRIALS.md` into `CURRENT-EVIDENCE.md`, deleting `BRIEF.md` after placing its surviving content, spinning `OPEN-MODEL-LANE.md` and its two companion files out of the repository, moving the data-maturity audit into the research lane, and updating `REQUIRED_ARCHITECTURE`, `LINK_ROOTS`, `llms.txt`, `TOOLBOX.md`, `CROSSWALK.md`, `AGENT-READING.md`, `READERSHIP.md`, `index.html`, and the follow-up watch to match |
| Material provided | The public repository at commit `0e55746`, read in full, and the maintainer's written instruction set for the cut, which set the constraint that the delete and spin-out lists be non-empty or the sprawl be defended document by document |
| Source verification | No new sources cited. Every claim in the changelog entry was checked against the files: the four surfaces carrying the same evidence sentence were read one by one, `BRIEF.md`'s line count was compared with `README.md`'s, each of its sections was traced to the document that already held the same material, and `llms.txt` was checked for the open-model lane, which it had never listed |
| Corrections after verification | The mediated-attention grouping the instruction set offered as a hypothesis was tested and rejected rather than adopted; the reasoning is in the pull request, and the four documents stayed where they were. The first pass would have left `RESEARCH-STATUS.md` without an evidence ceiling of its own after removing its current-evidence bullets, which would have thinned claim custody on a surface readers land on directly, so the ceiling stayed and only the drift-prone detail moved. The first pass also missed that `TOOLBOX.md` had never indexed `CURRENT-EVIDENCE.md`, and that `index.html`'s method ledger printed Trace, Adapt, and Return twice |
| Human review | The maintainer reviews and merges the pull request. This is a structural change to a public repository, so it opens ready rather than draft and waits for him. No file was merged or pushed by the assistant |
| Sensitive material | None involved. No participant material, names, or consent records entered the repository, and nothing in `RIGHTS-AND-CONSENT.md`, `SECURITY.md`, the consent-register template, or the public-safe gate in the checker was touched |

## 2026-08-28 two readerships, crosswalk, and synthesis

| Field | Record |
|---|---|
| Tool | Claude Code |
| Task | Naming the repository's two readerships and writing the four artifacts the maintainer specified: the agent lane (`AGENT-READING.md`), the crosswalk between the lanes (`CROSSWALK.md`), the synthesis above them (`READERSHIP.md`), and a short re-addressing of `JOURNEY.md` as the human lane. Re-addressing pass across `README.md`, `llms.txt`, `TOOLBOX.md`, `BRIEF.md`, and `index.html`, plus three additions to `REQUIRED_ARCHITECTURE` in `scripts/check_repo.py` |
| Material provided | The public repository at commit `42341bf`, and the maintainer's written brief specifying the four artifacts, the constraint that the crosswalk stay flat and the synthesis stay vertical, and the evidence ceiling |
| Source verification | No new sources cited. Every claim about the repository's current state was read from the files rather than recalled: the `human_observe.status` value from `data/field-tests/ft-001-alchemy.json`, the checker's behavior from `scripts/check_repo.py`, the second-reader status from `TESTING.md`, and the absence-never-defaults rule from `HYPOTHESIS.md` |
| Corrections after verification | The first draft of `AGENT-READING.md` and `CROSSWALK.md` quoted the checker's placeholder tokens verbatim and the placeholder ban failed both files; both now point at the script instead of reprinting the list. Two review passes over the draft caught five further overstatements about the repository's own guards, each corrected against the code: the placeholder exemption covers the JSON records under `data/field-tests/` and not Markdown reports; the combined-score check matches three literal field names rather than any combined score; the completion rule for human Observe applies only when the station is marked required; nothing guards `PROVENANCE.md` against a release bump, so the crosswalk's provenance row no longer implies it does; and exhaustive re-checking belongs to `scripts/check_repo.py` rather than to a model's diligence. Four `index.html` links were absolute GitHub URLs the link checker skips and are now relative |
| Human review | The maintainer approved the plan, the two file names, and the decision to leave `llms.txt` as the agent entry point, before any file changed. Review of the shipped text remains required before merge |
| Sensitive material | None involved. No participant material, names, or consent records entered the repository |
| Follow-on in the same pass | At the maintainer's direction, two mechanisms the review had surfaced as open questions: `check_targets` now rewrites this repository's own `blob/main` URLs to local paths, and `check_repo.py` takes `--list-architecture`. Both were tested against the working tree before being described in prose, including a deliberate broken-link run to confirm the new rewrite fails rather than passing quietly. After `FILMING-FORMS.md` merged from PR #20, it was placed in the human lane as a seventeenth crosswalk row. The first draft of that row said a model may name which form "a project is in", which contradicts the instrument's own rule that the form is named per moment of use because a project can move through more than one; it also summarized the forms as three camera positions and dropped environmental filming, where the affected people are absent from the frame by definition. Both corrected against the file |

## 2026-08-26 ensō-fork mark retirement

| Field | Record |
|---|---|
| Tool | Claude Code |
| Task | Replacing the adapted ensō-fork mark with a fork diagram built from the papañca causal sequence, per the maintainer's chosen direction and selection among four proposed options |
| Material provided | The public repository; four line-work mark concepts drawn this session and shown to the maintainer for reaction, none adopted without his selection; the maintainer's direct choice of direction (replace, not retire or reinterpret) and of the specific option (a plain two-branch fork, no return stroke, no two-tone system) |
| Source verification | Not applicable; this is original diagram work, not a claim requiring a citation. Checked only that no Zen-specific or ensō-derived language survived in `design/VISUAL-LANGUAGE.md`, `PROVENANCE.md`, or `index.html` after the change |
| Corrections after verification | None found needing correction |
| Human review | Maintainer chose the direction and the specific mark before any file was changed; review of the shipped SVGs and prose remains required before merge |
| Sensitive material | None involved |

## 2026-08-26 RAIN addition

| Field | Record |
|---|---|
| Tool | Claude Code |
| Task | Adding RAIN (Recognize, Allow, Investigate, Non-Identification) to `PRACTICE-FRAME.md` as the response method feeding the practice loop; citing it in `PROVENANCE.md` under a new "Modern practice tools" section |
| Material provided | The public repository; the maintainer's own direct instruction, naming RAIN and its four steps by name and stating he wanted the Non-Identification (not the later "Nurture") version |
| Source verification | A dedicated research pass checked the exact wording against Tara Brach's published 2013 chapter, and the originator attribution against Michele McDonald's own retreat center, secondary coverage, and McDonald's full Dharma Seed talk archive (396 talks, 1984-2020) for a datable primary coining statement |
| Corrections after verification | Declined to state a coining year for McDonald as settled fact; secondary sources range from the 1980s to around 2001, McDonald's own dated talk archive shows no talk titled "RAIN" before 2015, and no primary text fixing an earlier date was found. Declined to present McDonald's own recorded wording ("Recognition, Acceptance, Investigation, Non-Identification") as identical to the "Recognize, Allow, Investigate, Non-Identification" phrasing in circulation; PROVENANCE.md now names both and flags the difference. Labeled RAIN a modern teaching device, not a canonical text, in a section kept separate from the sutta and Abhidhamma citations above it |
| Human review | Maintainer review remains required before merge. The earlier "rain metaphor" question in the pull request is now answered: it names this framework, not an unresolved metaphor. The ensō-mark decision remains open separately |
| Sensitive material | None involved |

## 2026-08-26 papañca register correction

| Field | Record |
|---|---|
| Tool | Claude Code |
| Task | Shifting Zen-specific symbolism toward baseline early-Buddhist, papañca-centered framing; folding the Madhupiṇḍika Sutta's causal chain and the Abhidhamma's javāna account into `PRACTICE-FRAME.md`; citing both in `PROVENANCE.md`; adding `ORIGIN.md` as a placeholder for the maintainer's own account |
| Material provided | The public repository; a private synthesis note from the maintainer's own research vault (treated as a lead, not a source, since its own citation list does not resolve); a private register-discipline standard (`buddhist-flattening-critique.md`) the maintainer already holds elsewhere in his stack; the maintainer's own direct instruction naming the two biographical facts that appear as examples in `ORIGIN.md`'s placeholder text (an undergraduate advisor, and reading *Zen Mind, Beginner's Mind*) |
| Source verification | A dedicated research pass checked the Madhupiṇḍika Sutta chain and its "shift in agency" reading against Bhikkhu Sujato's suttacentral.net translation and translator notes directly; checked the Abhidhamma javāna-and-bhavaṅga model against Bhikkhu Bodhi's *A Comprehensive Manual of Abhidhamma* and a parallel classical exposition; found no source support for reading javāna "looping" as a distinct mechanism, and labeled that reading as PureLand's own extension |
| Corrections after verification | Declined to attribute the grammatical "shift in agency" reading to Bhikkhu Bodhi, since that attribution in the private note could not be verified this session; cited Sujato's own translator note instead. Declined to carry forward the private note's framing of papañca as "a bug to be patched" and something technology has "learned to externalize and weaponize," since neither phrase is supported by the Abhidhamma source. Left the adapted ensō mark, its visual form, and its existing disclaimers unchanged; the mark is a maintainer decision, presented as options in the pull request rather than implemented |
| Human review | Maintainer review remains required before merge. The mark options are left open, alongside two unresolved questions raised in the pull request rather than answered here: a practice-frame reorganization question, and a referenced "rain metaphor" |
| Sensitive material | None involved; the private research note consulted is the maintainer's own non-participant research writing, used only to identify which primary sources to verify |

## 2026-08-24 concurrent-lane integration

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Task | Verifying and integrating the architecture, measurement, and rights writer commits; reconciling the public architecture, field-test schema, FT-001 record, intake path, and public-safe review contract; running structural and adversarial acceptance checks |
| Material provided | Local baseline `252ea70`; writer commits `bb98f2b`, `e228830`, and `81bf2c8`; writer reports and prompts; the public repository only |
| Source verification | Git established writer ancestry, exclusive file ownership, clean worktrees, and local-only state; repository records and enforcing files were read after integration; no private vault or research workspace was accessed |
| Corrections after verification | Replaced the Boolean privacy review with an artifact-version public-safe review, separated rights decisions, added withdrawal actions and takedown routing, made public issues Stage 1 scoping only, removed four unpublished compatibility layers, and kept the version 0.2 sample target explicitly provisional |
| Human review | The integrated branch is local. Maintainer approval remains required before push, pull request, merge, or publication. |
| Sensitive material | None involved; no participant, client, confidential, consent, or protected community record was accessed |

## 2026-08-24 research-architecture correction

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Task | Reducing the public research architecture to six functions; narrowing FT-001 and Alchemy claims; correcting lineage, symbolism, visual-language, and metadata drift |
| Material provided | The local pre-concurrency research-arc baseline at commit `252ea70`; the public Alchemy repository at its current `bf5e411` and FT-001's pinned `b7ae829`; no private research files |
| Source verification | Public architecture links were checked in the repository; the seven-surface FT-001 boundary was checked against its report and JSON record; Alchemy's pinned `docs/PRODUCT.md` names six product surfaces and FT-001 adds the embodied service as the seventh assessed surface |
| Corrections after verification | Removed the separate applied-PureLand layer, unsupported information-theory contribution, three-layer visual motif, non-extractive outcome wording, unsupported precedent superlative, and derived-evidence framing for provisional sample targets |
| Human review | Maintainer review remains required before integration, push, or publication. These edits narrow public claims; they do not add evidence. |
| Sensitive material | None involved; all inspected project and Alchemy records are public |

## 2026-08-24 research-spine restructuring

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Task | Restructuring PureLand from a fork-kit-first repository into a draft thesis, method, toolbox, hypothesis, applied layer, testing, results, discussion, and conclusion |
| Material provided | A clean clone of the public `pureland-fork-kit` repository at commit `f57f42f`; an existing read-only PureLand graph used to map prior relationships |
| Source verification | Every current-result statement was checked against FT-001, its structured record, the field-trial ledger, and the research-status ledger; local links and JSON by `scripts/check_repo.py`; FT-001 against `data/field-test.schema.json`; the site through Python's HTML parser; `CITATION.cff` through Ruby YAML parsing; whitespace by `git diff --check` |
| Corrections after verification | The working draft initially used the wrong name for the applied layer. The maintainer corrected it to PureLand; the file, links, descriptions, and validation check were changed before handoff. |
| Human review | Maintainer review remains required before commit, push, or publication. The new primary hypothesis and applied-layer definition are drafts, not evidence. |
| Sensitive material | None involved; no participant material, consent record, or private research file entered the clean clone |

## 2026-08-24 journey consolidation and field test FT-001

| Field | Record |
|---|---|
| Tool | Claude Code |
| Task | Consolidating the entry path into `JOURNEY.md`; wiring in the Alchemy companion; walking the journey on Alchemy and drafting FT-001 (repository analysis, counting, report and record drafting) |
| Material provided | The public `pureland-fork-kit` and `alchemy` repositories at named commits; stack-data's repository registry |
| Source verification | Every FT-001 claim was checked against the Alchemy source files pinned at commit b7ae829; local links and JSON by `scripts/check_repo.py`; the record against `data/field-test.schema.json` |
| Corrections after verification | Two review passes corrected the product inventory to six surfaces named in `docs/PRODUCT.md`, plus the embodied service, for seven surfaces in the assessed FT-001 set. They also corrected a mislabeled disagreement class, the annex station ordering, and stale evidence lines on four surfaces. |
| Human review | The maintainer reviews and merges the pull requests that land this work; FT-001's observe station additionally needs a human redo, recorded in the report |
| Sensitive material | None involved; both repositories are public and hold no participant material |

## 2026-08-21 repository restructuring

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Task | Adversarial repository review, source discovery, drafting, link and structure checks |
| Material provided | The local PureLand working folder and the private `risaac09/pureland-fork-kit` repository |
| Source verification | Primary-source links were checked during research; local links and JSON were checked by `scripts/check_repo.py` |
| Corrections after verification | Not recorded. This is the oldest entry and the corrections row was added to the format later. Reconstructing the corrections now would be invention rather than disclosure, so the gap is named instead of filled |
| Human review | Maintainer review remains required before treating the prose or source interpretations as final |
| Sensitive material | No participant recordings or consent records were added to the repository |

AI output is not cited as evidence. [PROVENANCE.md](PROVENANCE.md) names the sources used to support substantive claims.
