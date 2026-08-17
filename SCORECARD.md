# The Openness Scorecard (blank)

*(Pure)Land fork kit, component 2 of 5. Score a practice, an archive, an organization, or an estate. Pair every reading with the [extraction check](EXTRACTION-CHECK.md); an openness score without one is exposure accounting.*

## How to use this

Openness here is not one number. It decomposes into four accesses, each with its own question, its own way of counting, and its own failure mode. You will produce four separate readings.

Three rules before you start:

1. **Name your denominator before you count.** Decide what the whole set is (every repository, every published artifact, every method document) and write it down first. A score with a chosen-after denominator is a story, not a measurement.
2. **Never average the four accesses.** The denominators differ. A composite openness index launders four different questions into one false one. Report four numbers or none.
3. **Unmeasurable is a finding, not a zero.** If a question cannot be answered from the record, write "unmeasurable" and say what record would be needed. A gap is a gap, not a pass.

## The four accesses

### 1. Legibility

*Can someone outside the core parse what is here?*

Count: artifacts that are public AND carry a plain-language description of what they are, over all artifacts in the named set. Plain language means a stranger can tell what the thing is and whether it concerns them without insider vocabulary.

| | |
|---|---|
| Set (denominator) | |
| Legible artifacts (numerator) | |
| Score | / |
| What blocked the rest | |

Extraction pairing: raising legibility lowers search and targeting cost for everyone, including crawlers and model-training collectors. Before raising it, ask who gains the map.

### 2. Permeability

*Can information actually move in and out, in both directions?*

Count two things separately: the fraction of the set publicly reachable at all, and the depth of the permission gradient (how many tiers, how many permission boundaries, between the public surface and the working core; count both endpoints as tiers, count each permission change as a boundary).

| | |
|---|---|
| Set (denominator) | |
| Publicly reachable (numerator) | |
| Score | / |
| Deepest traced path (tiers / boundaries) | |
| Inbound: how does a request from outside reach the core, and how fast is it answered? | |

Extraction pairing: publishing past a privacy boundary can collapse the distinction between a finished artifact, a participant's words, and raw working material. They carried different consent. Check that the boundary you are opening was not holding someone else's.

### 3. Forkability

*Can others take the material and build on it without permission or an existing relationship?*

Count: artifacts that are public AND carry an explicit license permitting reuse without asking, over the named set. An artifact that is public but unlicensed is readable, not forkable.

| | |
|---|---|
| Set (denominator) | |
| Explicitly licensed for permissionless reuse (numerator) | |
| Score | / |
| Licenses in use | |

Extraction pairing: a permissionless license authorizes reuse outside the relationship that produced the material. Reciprocity does not automatically travel with an open license; if it matters here, it must be written in (see [LICENSE.md](LICENSE.md) for how this kit does it).

### 4. Provenance

*Can a claim or artifact be traced to where it came from?*

Count: records whose source is verified against the origin (not merely cited, verified), over all records in the named set. Report the verified, partially verified, and unverified counts separately; a schema field that exists is not a verification that happened.

| | |
|---|---|
| Set (denominator) | |
| Verified (numerator) | |
| Partially verified | |
| Unverified | |
| Score | / |

Extraction pairing: stronger identity-to-claim joins improve accountability and also improve re-identification and surveillance. Where provenance touches people, use public-safe identifiers and keep a revocation path; a provenance trail that makes deletion impossible has traded one harm for another.

## Closure rationale

For anything you measured as closed, record why, in your own words, before anyone asks. Closure is a decision somebody made; the scorecard's job is to make the decision visible, not to shame it. A closed artifact with a stated reason is in better condition than an open one nobody decided about.

| Closed artifact or set | Stated reason for closure |
|---|---|
| | |

## Reading the result

Four numbers, a depth trace, and a closure table. No composite. The instrument behind this scorecard is specified and has been run once by its authors; it is not validated. If your reading surprises you, the reading might be wrong, the instrument might be wrong, or the surprise might be real. Send what you find (see [README.md](README.md)); disagreement with this scorecard is one of the things it exists to collect.
