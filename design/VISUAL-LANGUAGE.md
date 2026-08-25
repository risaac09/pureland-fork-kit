# Visual language: Ink & Bone

PureLand studies how information practices extract attention. Its own visuals are one of those practices, so they carry the same working hypothesis: a look can make people easier to hold or easier to leave. Ink & Bone is built to be easy to leave. It uses restraint, hairline rules, and visible revision instead of color pressure, motion, or badges, so the kit's appearance argues for the same sovereignty its instruments measure.

## Principles

1. **Quiet over grabby.** The kit studies attention extraction, so its visuals must not practice it. Generous whitespace, calm contrast, no saturated attention-bait. Nothing blinks or shouts.
2. **Archival honesty.** The look of a field ledger and a specimen record: monospace labels, hairline rules, roman numerals, engraved-illustration heritage. Records look inspectable, not designed to persuade.
3. **Revision stays visible.** Strikethrough is a first-class mark. Corrections remain in the record rather than disappearing. Disagreement is shown, not smoothed over.
4. **Nothing certifies.** No badges, seals, trophies, or score-like emblems. Marks describe; they never award. The ensō in the mark is deliberately left open, for the same reason the scorecard refuses a single number.

## Palette

| Name | Hex | Role |
|---|---|---|
| Ink | `#1C1815` | Warm near-black. Primary ground in dark contexts, primary text on Bone. |
| Bone | `#F3EDE0` | Warm parchment cream. Primary ground in light contexts, primary text on Ink. |
| Brass | `#B4945F` | Contemplative accent. Display headings, the mark, key rules. |
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

- **Roman numerals I through VI** for the method's six stations: ground, observe, map, trace, adapt, return. JOURNEY.md holds the canonical list.
- **Hairline rules.** 1px, Graphite, reduced opacity. They divide without shouting.
- **Small arrow annotations.** `→` followed by a monospace caption, used the way a specimen label points to a detail.
- **Strikethrough in Oxblood** for visible revision. A crossed-out line stays legible; it is a record of what changed, not a deletion.
- **Engraved or etched line illustration.** Thin strokes, no fills, specimen-plate feel, for any future illustration work.
- **The ensō-fork mark.** See below.

## The mark: ensō-fork

The mark is a single-stroke open circle, an ensō, drawn with a hand-drawn feel: the stroke visibly does not close, leaving a gap at roughly one to two o'clock. A stem rises from the bottom of the circle and forks into two branches inside the circle. One branch curves outward and passes through the circle's edge: the fork that travels out. One branch curves back inward toward the center: the learning that returns.

The open circle means nothing certifies. It is not a seal, a checkmark, or a badge. It marks a practice that stays open to correction, the same way the scorecard refuses a single composite score and the extraction check refuses a moral verdict.

The two branches mean a fork is judged by both directions of travel. Code and method can leave the origin. Something, learning, credit, correction, a returned report, has to travel back for the fork to be more than extraction with a license file attached.

The mark is line-work only: no fills, a roughly uniform stroke with slightly tapered ends where the medium allows. It should read clearly at 32px.

## Usage

- **README banner.** A quiet header above the title: the mark at left, the kit name in letterspaced serif caps, a short monospace caption beneath a Brass hairline rule. See `design/assets/banner-light.svg` and `design/assets/banner-dark.svg`.
- **Docs.** Hairline rules to divide sections, monospace labels for field names and data, roman numerals where the six stations are named directly.
- **Field-report artifacts.** Ledger styling for anything that functions as a record: monospace headers, Oxblood strikethrough for corrections, no color used to imply a verdict.

## What to avoid

- Badges, seals, trophies, or any score-like emblem. The kit does not certify practices and its visuals should not imply that it does.
- Saturated, alarm-toned color used for urgency or attention-bait. Oxblood is a register, not a siren; keep it to short, deliberate emphasis.
- Dark-pattern layouts: countdowns, forced scroll, infinite continuation, disguised close controls, anything that manufactures an impulse instead of inviting a choice.
- Buddhist iconography used as decoration. PRACTICE-FRAME.md is careful not to turn Buddhist categories into labels for someone else; the visual language holds the same care and does not use lotus, wheel, or other devotional imagery as ornament. The ensō is used here for its plain meaning, an open, unfinished circle, not as a religious symbol standing in for the kit's authority.

## Tokens

The palette, type stacks, spacing, and rules above are published as [design/tokens.css](tokens.css) for stylesheets and [design/tokens.json](tokens.json) for anything else that needs them. Change this document and the token files together.

## Licensing note

Design assets in this directory are original text, diagrams, and marks made for this kit, and are licensed the same way as the kit's text: [CC BY-SA 4.0](../LICENSE). See [LICENSE.md](../LICENSE.md) for the full boundary, including what stays excluded from that license.
