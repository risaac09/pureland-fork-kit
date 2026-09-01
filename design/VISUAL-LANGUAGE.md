# Visual language: Ink & Bone

PureLand asks whether information practices can increase practical agency without increasing exposure or extraction. Its own visuals belong inside that question. Ink & Bone makes stopping and leaving visible through restraint, hairline rules, and visible revision. The design states an intention. It does not prove an attention-sovereignty outcome.

## Principles

1. **Quiet over grabby.** PureLand studies attention extraction, so its visuals must not practice it. Generous whitespace, calm contrast, no saturated attention-bait. Nothing blinks or shouts.
2. **Archival honesty.** The look of a field ledger and a specimen record: monospace labels, hairline rules, roman numerals, engraved-illustration heritage. Records look inspectable, not designed to persuade.
3. **Revision stays visible.** Strikethrough is a first-class mark. Corrections remain in the record rather than disappearing. Disagreement is shown, not smoothed over.
4. **Nothing certifies.** No badges, seals, trophies, or score-like emblems. Marks describe; they never award. The fork mark carries the same refusal as a scorecard without a single number: a stem and two branches, not a seal or a checkmark.

## Palette

| Name | Hex | Role |
|---|---|---|
| Ink | `#1C1815` | Warm near-black. Primary ground in dark contexts, primary text on Bone. |
| Bone | `#F3EDE0` | Warm parchment cream. Primary ground in light contexts, primary text on Ink. |
| Brass | `#B4945F` | Contemplative accent. Display headings, key rules. |
| Oxblood | `#7B2D26` | The extraction register. Warnings, costs, the three poisons, strikethrough color. |
| Celadon | `#8FAE9B` | The return register. Growth, reciprocity, learning that travels back. |
| Graphite | `#6B6257` | Secondary text, captions, hairline rules. |

Contrast notes:

- Ink on Bone and Bone on Ink are the high-contrast pairs. Use them for body text.
- Brass and Celadon are accent-only on either ground. Do not set long body text in them.
- Oxblood passes contrast on Bone, but reserve it for short emphasis: a strikethrough, a warning word, a poison named in a table cell.

## Typography

- **Display.** A high-contrast serif in letterspaced capitals, for the engraved or Didone feeling of an old specimen plate. Stack: `"Cormorant Garamond", "EB Garamond", Georgia, serif`. Set short titles uppercase with `letter-spacing: 0.08em`. A sentence-length line stays in sentence case; at that length letterspaced capitals shout, which principle 1 rules out.
- **Body.** A readable old-style serif. Stack: `"EB Garamond", Georgia, "Times New Roman", serif`.
- **Ledger labels, data, tokens.** Monospace, uppercase, wide tracking, for anything that reads as a field entry rather than prose. Stack: `"IBM Plex Mono", "Courier Prime", "Courier New", monospace` with `letter-spacing: 0.12em`.

The first face of each stack is self-hosted as a latin woff2 subset in `design/fonts/` under the OFL, and the fallback renders any glyph outside that subset.

## Motifs

- **Roman numerals** appear in two explicitly labeled sequences: the public research functions and the method's six journey stations. Never let one sequence stand in for the other, and read the count from the sequence itself rather than fixing it here, where it would drift.
- **Hairline rules.** 1px, Graphite, reduced opacity. They divide without shouting.
- **Small arrow annotations.** `→` followed by a monospace caption, used the way a specimen label points to a detail.
- **Strikethrough in Oxblood** for visible revision. A crossed-out line stays legible; it is a record of what changed, not a deletion.
- **Engraved or etched line illustration.** Thin strokes, no fills, specimen-plate feel, for any future illustration work.
- **Drawn line-work.** See below.
- **The fork mark.** See below.

## Drawn line-work

An engraved plate can draw itself once, the way a hand lays down a line. On a screen surface, a diagram may animate its own strokes as they arrive.

Two rules bound the event class, and both come from principle 1. The dial, defined under Motion below, is the one drawing outside them and carries its own rule.

- **Once only.** An event diagram draws when it first reaches the reader and then stays drawn. Nothing loops, redraws on a second pass, or moves again once it has landed. A mark that keeps moving is asking for attention rather than carrying a reading.
- **`prefers-reduced-motion: reduce` disables the drawing.** Under that setting every diagram is present and complete from the first frame. The reading never depends on having watched the stroke arrive, so a reader who turns motion off loses nothing but the motion.

### Motion

Line-work moves in exactly two ways, and each way has a rule.

- **The event.** A diagram draws once when it first reaches the reader and then stays drawn. The two rules above govern it. Station plates, the fork mark, and every fade are events.
- **The dial.** The journey thread is scroll-linked: its drawn length is the reader's position on the walk, and its tip rides the fixed horizon. A dial moves only while the hand moves. Scroll back and the line retreats, because the line is a reading of where you are, not a reward for having been there. It never advances on its own, and its timing function is linear, since any easing on a position reading would misreport the hand.

Scroll-linked, never scroll-jacked. The page never takes the scroll away from the hand, and it plays no motion the hand did not make. A held scene comes from `position: sticky` and releases the moment the reader keeps walking. Under `prefers-reduced-motion: reduce` both classes arrive fully drawn and nothing moves. The evidence section refuses motion entirely, in every mode: absence does not perform.

The motion grammar is published as named tokens in [design/tokens.css](tokens.css), beside the palette and type it moves.

The same restraint governs what the drawing may do. It reveals a line that was going to be there anyway. It does not stagger content into view, gate a section behind a scroll, or make the reader wait for a claim.

## The mark: the fork

The mark diagrams the causal chain in [PRACTICE-FRAME.md](../PRACTICE-FRAME.md#the-proliferation-chain): one stem rises, then splits into two branches at its midpoint. A single line becomes two, the point [PROVENANCE.md](../PROVENANCE.md) names as papañca, proliferation past thinking.

The retired mark adapted an ensō, a form associated with Zen Buddhist practice; see PROVENANCE.md for that history and why it changed. This mark borrows no form from any tradition's own mark-making. It draws the chain PureLand already cites, nothing else.

The fork carries no further interpretation beyond the split itself. It does not authenticate the method or certify a result.

The mark is line-work only: no fills, a roughly uniform stroke with slightly tapered ends where the medium allows. It should read clearly at 32px.

## Usage

- **README banner.** A quiet header above the title: the mark at left, the project name in letterspaced serif caps, a short monospace caption beneath a Brass hairline rule. See `design/assets/banner-light.svg` and `design/assets/banner-dark.svg`.
- **Docs.** Hairline rules divide sections. Monospace labels mark fields and data. Roman numerals identify either the public research functions or the six journey stations only when the sequence is named.
- **Field-report artifacts.** Ledger styling for anything that functions as a record: monospace headers, Oxblood strikethrough for corrections, no color used to imply a verdict.

## What to avoid

- Badges, seals, trophies, or any score-like emblem. PureLand does not certify practices and its visuals should not imply that it does.
- Saturated, alarm-toned color used for urgency or attention-bait. Oxblood is a register, not a siren; keep it to short, deliberate emphasis.
- Dark-pattern layouts: countdowns, forced scroll, infinite continuation, disguised close controls, anything that manufactures an impulse instead of inviting a choice.
- Buddhist iconography used as decoration or proof of authority. PRACTICE-FRAME.md does not turn Buddhist categories into labels for someone else, and the fork mark does not borrow a visual form from any tradition's own mark-making; it diagrams PureLand's own added material instead.

## Tokens

The palette, type stacks, spacing, and rules above are published as [design/tokens.css](tokens.css) for stylesheets and [design/tokens.json](tokens.json) for anything else that needs them. Change this document and the token files together.

## Licensing note

Design assets in this directory are original text, diagrams, and marks made for PureLand, and are licensed the same way as the project's eligible text: [CC BY-SA 4.0](../LICENSE). See [LICENSE.md](../LICENSE.md) for the full boundary, including what stays excluded from that license.
