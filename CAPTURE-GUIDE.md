# Capture guide: raw material behind a record

Use this guide to decide what to record while you run [the method](METHOD.md), what each kind of raw material can stand behind, and what stays private. It sits beside the [self-guided packet](templates/run-it-yourself.md) and the [field-test template](templates/field-test.md). It is not a step of the method, and it adds no instrument.

## The rule this guide follows

The record is text. Every evidence field in the [field-test schema](data/field-test.schema.json) holds a reference and a review status, not a file. A screen recording, a voice note, a transcript, or footage is raw material. It sits behind the record, in private custody, and the record cites it by an ID you assign. The repository holds methods, templates, and public-safe records, so raw material never enters it, in any profile below, whoever it belongs to. See [SECURITY.md](SECURITY.md) and [data/README.md](data/README.md).

Capturing more does not raise the ceiling in [CURRENT-EVIDENCE.md](CURRENT-EVIDENCE.md). A recording that nothing in the record cites is storage, not evidence. A recording the record cites lets a second reader check a reading. It cannot supply the Attend entry, the affected person's challenge, or the follow-up that only elapsed time produces.

## Attend stays in your own words

The [practice frame](PRACTICE-FRAME.md) asks you to leave the worksheet, run the practice, and return to write what you noticed. Speaking works as well as writing, under two conditions.

Record the note after the practice, not during it. Narrating while you practise turns the practice into a performance for the recorder, which is the risk the [self-filming form](FILMING-FORMS.md#self-filming) names. A screen recording, if you make one, runs during the practice and witnesses what the tool did. The voice note comes afterward and carries what you noticed. Keep them as two files.

A transcript of your note is a copy, not a rewrite. Transcribe it word for word, mark it as yours, and check it against the audio before it stands in for the audio. A model may transcribe verbatim. It may not summarize, tidy, or infer what you meant. The [agent lane](llms.txt) forbids a model to produce an Attend entry, and a cleaned-up transcript is one. The packet's rule holds in either medium: a model may hold your place or quote you.

## Three capture profiles

Each profile names a kind of practice, what to capture, which step each piece feeds, whose permission it needs, and the smallest version that still produces a record. All three end in the same [worksheet](templates/run-it-yourself.md). Only a run that seeks a public return goes on to the [field-test report](templates/field-test.md), the structured record, the rights review, and the artifact-version decision.

### One person, one tool

- **Practice.** Your own use of an app, a feed, a model, or an inbox.
- **Capture.** A screen recording with the microphone off during the practice. A voice note or written note afterward for Attend. The tool's own exports, settings pages, and history as evidence that existed before analysis.
- **What each piece feeds.** The recording feeds Read and Trace, cited by timestamp: what you could see, reach, adapt, and trace, and what left and where it went. The note feeds Attend. The exports define the document-access set and its denominator.
- **Permission.** Your own, until another person appears in the material: a chat, a shared document, a name in the inbox. Their words are participant material, and for that material the run moves to the second or third profile.
- **Public.** You may publish your own recording elsewhere. That is still a separate artifact-version decision, and the record links it rather than holding it.
- **Smallest version.** No recording. A written note for Attend and a dated list of what you looked at.

### A live facilitation practice

- **Practice.** A session you facilitate or take part in, with other people present.
- **Capture.** Name the [filming form](FILMING-FORMS.md) in use at each moment and who holds the camera. Hold the [protocol's pre-conversation](PROTOCOL.md#hold-a-pre-conversation) first. Audio alone is a smaller ask than video and is often enough. Your Attend note comes after the session, off camera, in your words.
- **What each piece feeds.** Footage or audio feeds Read and Trace for the session and gives the participants something concrete to challenge. Their challenge is the affected-party challenge the record needs. It enters the record only with their permission and in their words or in wording they approved. Your note feeds Attend.
- **Permission.** One [consent register](templates/consent-register.md) per rights holder before the recorder starts: audio, video, retention, transcript, each reviewer, each artifact, each a separate decision. The [editing interval](PROTOCOL.md#wait-before-editing) and the return default in the filming forms apply. Where the practice is held in common, the protocol's community-authority rule applies at full strength.
- **Public.** Nothing from the session enters the repository. The public record describes the practice in general terms and cites the private artifacts by ID with their review status.
- **Smallest version.** No recorder. Your own note afterward, and one participant's challenge, collected in a form they chose and logged in the register.

### An organization's practice

- **Practice.** A team's, a business's, or an institution's handling of information: a reporting cycle, a customer data flow, a meeting rhythm.
- **Capture.** The material already exists: spreadsheets, decks, policies, tickets, chat exports, meeting recordings. List it as evidence that existed before analysis, with a denominator, exclusions, and a time window. Make no new recording before the register exists. The Attend entry is still one named person's notice of their own attention inside the practice, written after being inside it, not after reading the files.
- **What each piece feeds.** Documents feed Read. Flows, contracts, and vendor terms feed Trace. Existing meeting recordings are participant material and follow the second profile's permission rules.
- **Permission.** Client and confidential records make this Stage 2 by definition. [RIGHTS-AND-CONSENT.md](RIGHTS-AND-CONSENT.md#two-stage-intake) requires a private channel before any of it is received, and the repository designates none by default. A transcription service or a model run over the material is an AI-processing decision in the register and brings the [AI system annex](AI-SYSTEM-ANNEX.md) into Read.
- **Public.** The record names the artifact set by count and kind, never by content. Anonymization does not settle re-identification or publication authority.
- **Smallest version.** One named person, one bounded flow, one document set counted rather than copied, and that person's own Attend note.

## What each kind of raw material can stand behind

| Raw material | Can stand behind | Cannot stand behind | Where it lives |
|---|---|---|---|
| Screen recording of your own use | Read and Trace readings cited by timestamp; the before and after of a reversible change | The Attend entry; any causal claim | Your files, named in the record by ID |
| Voice note after the practice | The Attend entry, transcribed word for word | A reading, a score, or a finding | Your files; the transcript in the record if you choose |
| Session footage or audio | Read and Trace for the encounter; the participants' challenge in their words | Your Attend entry; consent to an edit, which is its own decision | Private custody, named in the register |
| Session transcript | The same, in searchable form | Anything the audio does not | Private custody; each transcript is a register decision |
| Documents, exports, spreadsheets, decks | The document-access set, its denominator, and the four access readings | A person-level outcome | Private custody; counted, not copied, in the public record |
| Model output over any of the above | A structural check, or a proposal marked as a proposal | Attend, a reading, a challenge, an outcome | The record's AI-assistance disclosure; the register holds the processing decision |

## Before you press record

- Name the file and the date. Decide the ID the record will cite.
- Name the custodian, the storage location, the backups, and every third party that will hold a copy. The register has a row for each.
- Set the deletion or review date before collecting, not after.
- Choose the ending you want from the packet: private result, refusal, `unmeasurable`, or a public-safe return after review.
- For anyone else's material, complete the register before the recorder starts. Silence is not consent.

## What this does not do

This guide names material. It grants no permission, certifies nothing, and cannot produce a second reader, an affected person's challenge, or elapsed time. The [rights and consent guide](RIGHTS-AND-CONSENT.md), the [facilitation protocol](PROTOCOL.md), and the [filming forms](FILMING-FORMS.md) govern what may be recorded and kept. This guide only says what a recording can and cannot stand behind once it exists.

None of it has been tested. **What would count against it.** If runs that keep recordings produce no more inspectable readings, verbatim Attend entries, or affected-party challenges than runs kept in notes, the guide adds custody burden and buys nothing. If people who voice-note their Attend can hear themselves performing on playback, the after-not-during rule is not enough and the note should be written instead. Nobody has tested either.
