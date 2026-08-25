# AI assistance record

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
