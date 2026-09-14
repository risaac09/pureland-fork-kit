# PureLand front-page review and second visual system

Reviewed 2026-09-14. [Homepage draft](index.html) · [Visual system](system.html) · [Specification and integration plan](SPECIFICATION.md) · [README candidate](README-preview.md).

## Finding

The public page and repository are technically aligned. The design makes a first-time reader work too hard to find the method and evidence. The best next step is a clearer front door, with the same research character and evidence limits.

Field & Form is a second visual-system draft. It uses warm paper, mineral green, large mixed-case display type, and a system-sans reading face. It retains the original fork mark as a supporting illustration. Native disclosures make the method inspectable without the existing long scenes.

## Live state

- Repository: [risaac09/pureland-fork-kit](https://github.com/risaac09/pureland-fork-kit), origin verified as `git@github.com:risaac09/pureland-fork-kit.git`.
- Refreshed `origin/main`: `88216c083285807a78a7ddb497a0684adb505e5d`.
- [Live page](https://risaac09.github.io/pureland-fork-kit/): GitHub Pages reports `built`, from `main`, root `/`. Latest build reports the same commit, updated 2026-09-13T01:31:31Z.
- Downloaded live HTML and local `index.html` have the same SHA-256: `5b581cb9930aec7812837e6d5ef2371fc5727cd3d20d9852e0d8ab526217b6c8`.
- [PR #48](https://github.com/risaac09/pureland-fork-kit/pull/48) changes the homepage, README, and both existing token formats. It remains open. [PR #49](https://github.com/risaac09/pureland-fork-kit/pull/49) carries separate canonical-terms work. These are not deployed merely because they exist.
- This draft uses branch `design/field-form-20260914`, based on refreshed `origin/main`, in its own worktree. Root homepage, README, and active tokens remain unchanged.

Verification used Git, GitHub's Pages API, a downloaded HTML comparison, and actual browser rendering. A memory note identified prior share-readiness work as a lead; live checks superseded its historical PR status. No project graph exists in the primary checkout, so source tracing used direct files.

## Design diagnosis

| Priority | Observed issue | Consequence | Draft response |
|---|---|---|---|
| High | At 1280 × 720 the hero question starts around y=560, after the large fork image. The first action starts around y=1142. | The initial viewport offers little explanation and no primary action. | Move a short headline and description left of a contained specimen. Put the primary action in the first viewport. |
| High | Method starts around y=3145; evidence starts around y=7613. | The important reader tasks require a long scroll past framing and scenes. | Lead with the method. Place the evidence next, with direct navigation from the header and hero. |
| High | Oxblood `#7B2D26` remains the text color of field boundaries on the dark `#1C1815` ground. | The pair is 1.89:1, below the normal-text target; some consequential limits are difficult to read. | Use separate light and dark text roles and measured contrast for secondary copy. |
| Medium | Navigation is 11.2 px, uppercase, and widely tracked; many record labels are about 10.5–12 px. | Functional information reads like marginal annotation. | Use 14 px sans navigation and 44 px interaction targets. Reserve mono for short record labels. |
| Medium | The current page mixes small serif reading text, letterspaced headings, dense mono fields, and a fixed horizon crossing sections. | The archival motif competes with reading order. | Use a large serif for hierarchy, sans for reading, and section-bound rules. |
| Medium | The README repeats a large banner/title and requires substantial conceptual orientation before its use routes. | The repository entry feels heavier than its practical next steps. | Use the shared banner, early use links, and a compact five-document map in native Markdown. |
| Medium | Similar release, evidence, and offering summaries appear on several surfaces. | Visual alignment alone will not prevent future content drift. | Name each canonical owner and reconcile summaries with PR #48 before promotion. |

Existing strengths worth retaining: self-hosted fonts, original linework with disclosed provenance, permission boundaries, visible absence, dark-mode support, and motion preferences. The second system develops those strengths.

## Measured layout comparison

Same browser, 1280 × 720. Measurements are CSS pixels with default font size, after rendering. Draft method state: Scope expanded, remaining steps collapsed.

| Measure | Live Ink & Bone | Field & Form draft |
|---|---:|---:|
| First prominent action, y | 1142 | 600 |
| Evidence section, y | 7613 | 1675 |
| Initial document height | 10108 | 4224 |
| Navigation type | 11.2 px | 14 px |

Initial height falls about 58%. Evidence appears about 78% earlier in document distance. These are layout measurements, not a measured gain in understanding, task success, or attention sovereignty. Disclosure expansion changes document height. No tenfold usability claim is supported.

## Verification

Completed:

- Rendered the homepage at 320, 390, 768, and 1280 px. No horizontal overflow at those widths. The primary action begins at y=522 at 320 px, y=512 at 390 px, y=519 at 768 px, and y=600 at 1280 px. Viewport heights were 812, 844, 1024, and 720 px respectively.
- Inspected paper and ink themes in the browser. Theme switching updates its accessible action name and persists the local preference.
- Opened and closed Attend with Enter/Space. The disclosure retained native keyboard behavior and a visible 3 px focus outline. Verified the primary method and evidence anchor links.
- Rendered a temporary copy with all script tags removed: zero scripts, one H1, one main landmark, hidden theme control, and Attend opened through its native disclosure. The temporary fixture was removed after checking.
- Reviewed the repository banner and README composition in the specimen page. That page produced no captured warning or error logs during the check. This is a rendered README concept, not a screenshot of a published README.
- Calculated the declared text contrast: Ink/Paper 12.80:1, Stone/Paper 5.61:1, Mineral/Paper 10.01:1, Clay/Paper 5.28:1, dark secondary/Ink ground 8.74:1. Decorative lines are separate from functional boundaries.
- `python3 scripts/check_repo.py`: passed, with the existing unreleased-changelog warning. The checker resolves the new Markdown, HTML, CSS, image, and font links as part of its repository walk.
- `python3 -m unittest scripts/test_check_repo.py`: all 22 existing tests passed.
- `python3 scripts/test_classification_gap.py`: all three probes passed.
- `node --check design/v2/theme.js`: passed.
- `git diff --check`: passed.

The first test attempt used a Python 3.12 installation without the required jsonschema dependency. The successful run used the existing system Python installation with jsonschema; no project dependency was changed.

Remaining validation: the reduced-motion media rules were inspected in source, not exercised with an operating-system preference change. Browser zoom at 200%, a full screen-reader audit, cross-browser testing, and first-time-reader comprehension have not run. This draft is not a WCAG conformance claim. Production acceptance remains governed by the specification.

## Scope and remaining decisions

This is a reviewable local draft, not a deployed change. No push, PR creation, merge, or publication occurred. Review the [visual system](system.html) and [README candidate](README-preview.md) together. Their common introduction, palette, fork image, research-map order, and source labels create continuity within GitHub's native UI constraints.

Before adoption: reconcile with PR #48, review the shorter front-page copy, preserve legacy fragment routes, update active token contracts together, and run first-time-reader comprehension checks. [SPECIFICATION.md](SPECIFICATION.md) gives a bounded implementation sequence and acceptance criteria.

## AI assistance

OpenAI Codex inspected the live public page and repository, drafted the HTML/CSS/JavaScript and SVG assets, and wrote this review. Project claims came from the public repository. No participant material or confidential records entered the draft. The design and shorter copy still need maintainer review before adoption. AI-produced layout measurements are browser observations; they are not research evidence that PureLand works.
