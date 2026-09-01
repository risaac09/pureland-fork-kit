# AI assistance record

## The disclosure rule

When AI assists with source discovery, synthesis, coding, or drafting, disclose:

- the tool and model, if known;
- the date and task;
- the material provided to the system;
- how a human verified the output;
- the corrections made after verification;
- the material withheld for consent or privacy.

AI output is not a source. Cite the document that supports the claim. Every entry below is written against this rule, and [RESEARCH-STATUS.md](RESEARCH-STATUS.md) points here rather than restating it.

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
