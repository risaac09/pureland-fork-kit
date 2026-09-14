# Field & Form: PureLand visual system 02

Status: local design draft, 2026-09-14. [Homepage preview](index.html) · [Visual specification](system.html) · [README candidate](README-preview.md) · [Review](REVIEW.md).

## Design decision

Keep the research character of Ink & Bone. Give first-time visitors a readable introduction, a visible action, and a short path to the evidence. Use wabi-sabi restraint through material color, an asymmetric page composition, and the existing fork line. Keep alignment, controls, and reading order precise.

The requested order-of-magnitude improvement is a design ambition. No usability study establishes a tenfold gain. Judge this draft on concrete changes and then test comprehension with people who have not read the repository.

## Page structure

1. Header: PureLand, Method, Evidence, Research, explicit GitHub exit, optional theme control.
2. Hero: a short invitation to examine an information practice, a plain-language description, and one dominant method action. Evidence is the secondary action. The fork illustration supports the copy at desktop widths; the phone layout omits it.
3. Status line: release and validation state, with an evidence link. The status is readable text, not a certification badge.
4. Method: six always-visible step names, brief hints, native disclosures for details. Scope begins expanded. All six can remain open together for comparison.
5. Evidence: the canonical ceiling in full, beside the accepted partial record and the missing human and independent work. No motion in this section.
6. Use: self-guided and model-use packets. Field Pilot routes to the offering terms before the public issue form.
7. Research: the same five canonical document functions and order as the README.
8. Rights and footer: readable boundary, direct source links, AI-reader entry, correction path, and changelog.

The page is a front door. Readers follow source links for full instrument instructions. A short overview cannot support a claim that the reader ran the method.

## Color roles

| Token | Value | Use |
|---|---|---|
| Paper | `#F4F1E9` | Main light ground |
| Mineral | `#283F38` | Display text, primary action, evidence ground |
| Ink | `#252B27` | Body text |
| Stone | `#596259` | Secondary copy and labels |
| Lichen | `#DDE3D8` | Light linework on Mineral; dark-theme primary action |
| Clay | `#865944` | Short annotations and focus on Paper |
| Brass | `#BCA77E` | Decorative marks on Mineral |
| Ink ground | `#1E2924` | Dark theme reading ground |

[tokens.css](tokens.css) owns the complete theme roles. [system.html](system.html#contrast) records calculated text contrast. Dark mode assigns lighter secondary and accent text instead of reusing dark pigment values. A user's explicit theme choice persists locally; otherwise the operating-system preference applies.

Green communicates identity, not success. Diagram text labels carry meaning independently of color. Clay should not replace the existing extraction semantics in instrument diagrams without a separate semantic review. This prototype introduces no new extraction/return diagram and leaves the existing mark's meaning intact.

## Type and spacing

- Cormorant Garamond, weight 600: mixed-case display. Use the repository's existing WOFF2. Desktop hero about 83 px at 1280 px; mobile about 51 px at 390 px, reducing to 37 px at 320 px. Tight line height and modest negative tracking apply only to large display.
- System sans: 16 px default body at 1.65 line height; hero lead 18 px on desktop. Use system medium for document titles and primary action labels. Individual supporting passages use 14–15 px; keep long prose in the default body size.
- IBM Plex Mono, weight 400: short labels, minimum 12 px for normal content labels. Decorative SVG annotations and the draft-only utility strip may be smaller. Avoid paragraphs or primary navigation in monospace.
- Navigation: 14 px with a 44 px minimum target height. Primary action: at least 50 px high.
- Layout: maximum outer width 76 rem, with 20 px minimum mobile gutters and up to 64 px desktop gutters. Spacing steps are multiples of 4 px. Main sections have 80 px vertical padding on desktop and 56 px on phones.
- Body measure: about 45–60 characters where the grid permits. Large hero copy can use editorial line breaks; reassess those breaks at every breakpoint.

No additional font download is needed. Reusing an existing family preserves continuity and its recorded license. The system-sans body improves the functional contrast between instructions and display type.

## Movement

Use two bounded events: an 800 ms fork stroke on page load, and 160 ms response for hover/disclosure feedback. Easing is `cubic-bezier(.2,.65,.3,1)`.

Text never waits for animation. The fork is complete without JavaScript. Reduced-motion preference eliminates its animation and UI transitions. Do not animate evidence, use parallax, add sticky reading scenes, count down, or manufacture scroll distance. Anchor navigation uses the browser's immediate native behavior.

## Repository alignment and source ownership

| Public-page element | Canonical owner |
|---|---|
| Research question and conceptual scope | [THESIS.md](../../THESIS.md) |
| Six steps and human Attend boundary | [METHOD.md](../../METHOD.md), [PRACTICE-FRAME.md](../../PRACTICE-FRAME.md) |
| Claim, test conditions, disconfirmation | [TESTING.md](../../TESTING.md) |
| Present evidence and open follow-up | [CURRENT-EVIDENCE.md](../../CURRENT-EVIDENCE.md), [FT-001](../../research/field-tests/ft-001-alchemy.md) |
| Offering terms and intake stages | [OFFERING.md](../../OFFERING.md) |
| Permissions, confidentiality, withdrawal | [RIGHTS-AND-CONSENT.md](../../RIGHTS-AND-CONSENT.md) |
| Mark and traditions | [PROVENANCE.md](../../PROVENANCE.md), [VISUAL-LANGUAGE.md](../VISUAL-LANGUAGE.md) |
| Agent reading order and prohibitions | [llms.txt](../../llms.txt) |
| Visual roles | [tokens.css](tokens.css) |
| Presentation and interaction | [index.html](index.html), [styles.css](styles.css), [theme.js](theme.js) |

GitHub owns the surrounding navigation, fonts, and color scheme. Improve the README with the shared [banner](banner.svg), the same one-sentence description, early use routes, and a compact five-row research table. Keep its body native Markdown. Avoid custom HTML layouts that depend on unsupported CSS, or a raster image that replaces essential links and text. The banner is supplemental and has descriptive alternative text.

## Integration sequence for AI-assisted development

Recommended continuation: one writer in an isolated worktree at high reasoning effort; no delegation required.

1. Fetch and read the final `main` and PR #48 content. Both #48 and this direction touch homepage presentation. Retain the final approved wording, link coverage, and test contracts from that work before applying the new layout. Do not merge a stale whole-page replacement over it.
2. Review this local draft as a visual direction. Recheck wording against the canonical owner table. Retain the clear separation between the five document functions and six method steps.
3. Promote the agreed layout into root `index.html`, resolve asset paths, and preserve existing fragment routes, including `#spine`, `#readerships`, `#what-it-studies`, and all six step IDs. The prototype currently uses `#research` and `#start`; legacy aliases remain a promotion requirement. A step-fragment arrival should expose the linked step.
4. Reconcile the active visual-language document, CSS, and JSON token contracts together. Prefer deriving JSON from one token source; if the existing manual pairing remains, add a parity check. Do not keep two independently maintained active palettes. The v2 prototype intentionally has one CSS token source.
5. Apply the README candidate and banner through a focused diff. Convert candidate source links back to relative repository paths and keep the public-page link. Keep claims in their canonical files and summaries short.
6. Extend the existing repository checker to cover the chosen active assets and contracts. Verify local links, all fragment destinations, correct evidence ceiling, release state, and no third-party runtime requests. Run the repository's required checks once after integration.
7. Inspect actual rendering at phone, tablet, and desktop widths. Verify paper and ink, keyboard, reduced motion, and no-script behavior. Use at least one first-time reader for comprehension. Ask them to explain what PureLand is, whether it is validated, and which path they would take. Record errors; do not equate page length with usability.
8. Record AI assistance and the changelog, perform a focused review, and prepare the PR. Push, merge, deployment, release, and user testing are separate states; this draft reaches none of those states by being viewed.

## Acceptance criteria

- At 390 × 844 and 1280 × 720, the primary method action appears in the first viewport with the headline and description.
- No horizontal overflow at 320, 390, 768, or 1280 px. Content remains usable when enlarged; measure 200% zoom separately before production acceptance.
- One H1, meaningful landmarks, native disclosures, visible keyboard focus, and sufficiently sized primary controls.
- Normal text pairs meet 4.5:1. Functional outlines meet 3:1. Color is not the only indication of state.
- Full content and navigation work without JavaScript. The optional theme control remains hidden if its script is unavailable. No tracker, external font request, or client framework.
- Evidence and permission limits remain visible. No new validation, lineage, causal, safety, commercial, or attention-outcome claims.

Reference: [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/). A short checklist and contrast calculation do not establish conformance.
