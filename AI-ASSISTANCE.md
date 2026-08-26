# AI assistance record

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
| Human review | Maintainer review remains required before treating the prose or source interpretations as final |
| Sensitive material | No participant recordings or consent records were added to the repository |

AI output is not cited as evidence. [PROVENANCE.md](PROVENANCE.md) names the sources used to support substantive claims.
