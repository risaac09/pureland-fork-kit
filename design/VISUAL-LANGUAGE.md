# Visual language: Field & Form

PureLand asks whether an information practice can increase a person's control over their attention without increasing exposure or extraction. Its own visuals belong inside that question. Field & Form gives a first-time reader a readable introduction, one visible action, and a short path to the evidence: warm paper and mineral green, a large serif for hierarchy, the reader's own system sans for reading, and monospace only for short record labels. The design states an intention. It does not prove an attention-sovereignty outcome, and no first-time reader has yet been observed reading it.

Field & Form replaced Ink & Bone on 2026-09-14. Ink & Bone, its tokens, and its scroll-linked drawn walk live complete at commit `0e853f5`, together with the Field & Form draft, its specification, its review, and its specimen board under `design/v2/`.

## Principles

1. **Quiet over grabby.** PureLand studies attention extraction, so its visuals must not practice it. Muted color, generous space, no saturated attention-bait, no manufactured scroll distance, and no motion the reader did not ask for.
2. **The method first.** The first screen says what PureLand is and offers one action. The six steps come next, then the evidence, then the ways to use the method. Framing waits.
3. **Archival honesty.** Monospace labels for record fields, hairline rules, roman numerals on the six steps, and an annotated specimen plate for the mark. Records look inspectable, not designed to persuade.
4. **Revision stays visible.** Corrections remain in the record rather than disappearing, and absence is stated wherever nobody has observed something.
5. **Nothing certifies.** No badges, seals, trophies, or score-like emblems. Green is the project's identity color, never a mark of success or validation, and a text label carries the meaning wherever color appears.

## Palette

| Name | Hex | Role |
|---|---|---|
| Paper | `#F4F1E9` | The main reading ground. |
| Mineral | `#283F38` | Display text, the primary action, and the evidence ground. |
| Ink | `#252B27` | Body text on Paper. |
| Stone | `#596259` | Secondary copy and labels on Paper. |
| Lichen | `#DDE3D8` | Line-work on Mineral; the primary action in the ink theme. |
| Clay | `#865944` | Short annotations and the focus outline on Paper. |
| Brass | `#BCA77E` | Decorative marks on Mineral. |
| Ink ground | `#1E2924` | The reading ground of the ink theme. |

The eight pigments do not change with the theme. The roles built from them do: [design/tokens.css](tokens.css) declares each role once with `light-dark()`, paper value first, ink value second, and `color-scheme` on the root picks between them. The reader's system preference applies until they choose, and an explicit choice persists in their browser. The ink theme assigns lighter secondary and accent text instead of reusing dark pigment values.

Calculated text contrast, from the declared sRGB values:

| Text on ground | Ratio | Use |
|---|---:|---|
| Ink on Paper | 12.80:1 | Body text |
| Stone on Paper | 5.61:1 | Secondary text |
| Mineral on Paper | 10.01:1 | Headings |
| Clay on Paper | 5.28:1 | Small annotations |
| Paper on Mineral | 10.01:1 | Primary action and evidence |
| Plate caption on Mineral | 7.37:1 | Illustration labels |
| Ink-theme secondary on Ink ground | 8.74:1 | Secondary text in the ink theme |

Targets are 4.5:1 for normal text and 3:1 for functional boundaries. Decorative hairlines carry no information alone. These figures are the arithmetic behind the choices; they do not establish accessibility conformance. Clay is an annotation color and must not replace the extraction semantics of any instrument diagram without a separate semantic review.

## Typography

- **Display.** Cormorant Garamond, weight 600, mixed case, self-hosted as a latin woff2 subset in `design/fonts/`. Tight line height and modest negative tracking apply only at display sizes. The hero heading is about 83 px at 1280 px wide, about 51 px at 390 px, and 37 px at 320 px.
- **Body.** The reader's system sans, `-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`, at 16 px with a 1.65 line height; the hero lead is 18 px on desktop. Document titles and the primary action use the medium weight.
- **Labels.** IBM Plex Mono, weight 400, self-hosted, for short record labels only. Twelve pixels is the floor for a label that carries content. Never set paragraphs or primary navigation in monospace.
- **Navigation** is 14 px sans with a 44 px minimum target, and the primary action is at least 50 px high.

Both faces are subset to the latin block, and every `url()` in `design/tokens.css` is resolved by `scripts/check_repo.py`, so a renamed font file fails the run instead of falling back in silence. Their license is [LICENSES/OFL.txt](../LICENSES/OFL.txt).

## Layout

The page is one column of at most 76 rem, with gutters from 20 px on a phone to 64 px on a desktop. Main sections carry 80 px of vertical padding on desktop and 56 px on phones. Body copy runs about 45 to 60 characters where the grid permits. On a phone the hero drops the specimen plate, the six steps stack as full-width disclosures, and the two use paths fall into one column.

## Motifs

- **Roman numerals** number the six method steps and nothing else on the page. The five research documents carry arabic numbers, so the two sequences cannot be confused.
- **Hairline rules**, one pixel in the line role, divide sections and rows without shouting.
- **Monospace labels** mark record fields: the release, the research status, a record's date and outcome.
- **The specimen plate.** The fork mark sits on a Mineral plate with Brass guide lines and monospace annotations, a study in line rather than a logo.
- **Native disclosures.** The six steps are `<details>` elements. All six can stand open at once for comparison, and a link to a step opens that step.

## Movement

Two bounded events, and nothing else moves.

- **The fork stroke.** On page load the mark draws once in 800 ms: the stem and one branch first, the second branch after it, so the split reads as a split. The line is complete without JavaScript and stays drawn.
- **A response.** Hover and disclosure feedback answers in 160 ms with the `cubic-bezier(.2,.65,.3,1)` easing.

Text never waits for animation. Under `prefers-reduced-motion: reduce` the stroke appears complete and the transitions are gone. Nothing is scroll-linked, nothing holds a scene, no section counts down or manufactures scroll distance, and anchor navigation uses the browser's own behavior. The evidence section never moves.

## The mark: the fork

The mark diagrams the causal chain in [PRACTICE-FRAME.md](../PRACTICE-FRAME.md#the-proliferation-chain): one stem rises, then splits into two branches at its midpoint. A single line becomes two, the point [PROVENANCE.md](../PROVENANCE.md) names as papañca, proliferation past thinking.

The retired mark adapted an ensō, a form associated with Zen Buddhist practice; see PROVENANCE.md for that history and why it changed. This mark borrows no form from any tradition's own mark-making. It draws the chain PureLand already cites, nothing else.

The fork carries no further interpretation beyond the split itself. It does not authenticate the method or certify a result.

The mark is line-work only: no fills, a roughly uniform stroke with slightly tapered ends where the medium allows. It should read clearly at 32px. The standalone files are [mark-light.svg](assets/mark-light.svg) and [mark-dark.svg](assets/mark-dark.svg). The masthead icon draws the same geometry at 29 by 36 px; the hero's specimen plate and the README banner draw it larger, with the same stem and branches.

## Usage

- **README banner.** A paper and ink pair in `design/assets/`, chosen by `<picture>`: the eyebrow, the project name in the display face, the same one-sentence description the page opens with, and the mark on a Mineral block. GitHub renders the rest of the README in its own type and colors.
- **Docs.** Hairline rules divide sections. Monospace labels mark fields and data. Roman numerals identify the method's six steps only when that sequence is named.
- **Field-report artifacts.** Ledger styling for anything that functions as a record: monospace headers, corrections kept visible, no color used to imply a verdict.

## What to avoid

- Badges, seals, trophies, or any score-like emblem. PureLand does not certify practices and its visuals should not imply that it does.
- Saturated, alarm-toned color used for urgency or attention-bait. Clay annotates; it is not a siren.
- Dark-pattern layouts: countdowns, forced scroll, infinite continuation, disguised close controls, anything that manufactures an impulse instead of inviting a choice.
- Buddhist iconography used as decoration or proof of authority. PRACTICE-FRAME.md does not turn Buddhist categories into labels for someone else, and the fork mark does not borrow a visual form from any tradition's own mark-making; it diagrams PureLand's own added material instead.

## Contracts

The page keeps these, and `scripts/check_repo.py` checks the ones a script can check.

- One `h1`, meaningful landmarks, native disclosures, a visible 3 px focus outline on every control, and 44 px targets on every control and standalone link. Inline links inside prose are the one exception.
- Both themes, chosen by the reader or by the system, with a saved choice applied before first paint.
- Full content and navigation without JavaScript; the theme control stays hidden when its script is unavailable. No tracker, external font request, or client framework.
- The release sentence and the evidence ceiling sentence appear on the page exactly as the checker requires, and `design/tokens.json` matches `design/tokens.css`.
- The fragments `#spine` and `#readerships` remain as anchors on the research and use sections, for links from outside the repository that predate this system.
- Not yet run: a screen-reader audit, 200 percent zoom, cross-browser rendering, and the first-time-reader test. A short checklist and a contrast calculation do not establish conformance with [WCAG 2.2](https://www.w3.org/TR/WCAG22/).

## Tokens

[design/tokens.css](tokens.css) is the source of the palette, roles, type stacks, page width, and motion values. [design/tokens.json](tokens.json) mirrors its `:root` declarations verbatim for anything that cannot read CSS, and `scripts/check_repo.py` fails when the two differ. Change this document and the token file together.

## Licensing note

Design assets in this directory are original text, diagrams, and marks made for PureLand, and are licensed the same way as the project's eligible text: [CC BY-SA 4.0](../LICENSE). See [LICENSE.md](../LICENSE.md) for the full boundary, including what stays excluded from that license.
