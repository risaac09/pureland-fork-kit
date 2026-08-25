# AI assistance record

## 2026-08-24 research-spine restructuring

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Task | Restructuring PureLand from a fork-kit-first repository into an ordered thesis, method, toolbox, hypothesis, applied PureLand, testing, results, discussion, and conclusion |
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
| Corrections after verification | Two review passes corrected a set-definition miscount (six surfaces, not seven), a mislabeled disagreement class, the annex station ordering, and stale evidence lines on four surfaces |
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
