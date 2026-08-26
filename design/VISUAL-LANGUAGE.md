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

## Motifs

- **Roman numerals I through VI** appear in two explicitly labeled sequences: the six public research functions and the method's six journey stations. Never let one sequence stand in for the other.
- **Hairline rules.** 1px, Graphite, reduced opacity. They divide without shouting.
- **Small arrow annotations.** `→` followed by a monospace caption, used the way a specimen label points to a detail.
- **Strikethrough in Oxblood** for visible revision. A crossed-out line stays legible; it is a record of what changed, not a deletion.
- **Engraved or etched line illustration.** Thin strokes, no fills, specimen-plate feel, for any future illustration work.
- **The fork mark.** See below.

## The mark: the fork

The mark diagrams the causal chain in [PRACTICE-FRAME.md](../PRACTICE-FRAME.md#the-proliferation-chain): one stem rises, then splits into two branches at its midpoint. A single line becomes two, the point [PROVENANCE.md](../PROVENANCE.md) names as papañca, proliferation past thinking.

The retired mark adapted an ensō, a form associated with Zen Buddhist practice; see PROVENANCE.md for that history and why it changed. This mark borrows no form from any tradition's own mark-making. It draws the chain PureLand already cites, nothing else.

The fork carries no further interpretation beyond the split itself. It does not authenticate the method or certify a result.

The mark is line-work only: no fills, a roughly uniform stroke with slightly tapered ends where the medium allows. It should read clearly at 32px.

## Usage

- **README banner.** A quiet header above the title: the mark at left, the project name in letterspaced serif caps, a short monospace caption beneath a Brass hairline rule. See `design/assets/banner-light.svg` and `design/assets/banner-dark.svg`.
- **Docs.** Hairline rules divide sections. Monospace labels mark fields and data. Roman numerals identify either the six public functions or the six journey stations only when the sequence is named.
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
