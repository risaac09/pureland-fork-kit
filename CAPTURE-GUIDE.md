# Capture guide: raw material behind a record

Use this guide to decide what to record while you run [the method](METHOD.md), what each kind of raw material can stand behind, and what stays private. It sits beside the [self-guided packet](templates/run-it-yourself.md) and the [field-test template](templates/field-test.md). It is not a step of the method.

## The rule this guide follows

The record is text. An evidence item in the [structured record](data/field-test.schema.json) carries an ID, a description, a source reference, whether it existed before analysis, and a public flag. The [report](templates/field-test.md) adds the artifact-version review status. Neither holds a file. A screen recording, a voice note, a transcript, or footage is raw material. It sits behind the record, in private custody, and the record cites it by the ID you assign. [data/README.md](data/README.md) keeps recordings and transcripts out of the repository, so raw material never enters it in any profile below. Your own recording, if you publish it, lives elsewhere and the record links it.

Capturing more does not raise the ceiling in [CURRENT-EVIDENCE.md](CURRENT-EVIDENCE.md). A recording nothing in the record cites is storage. A recording the record cites lets a second reader check a reading. Footage and screen recordings cannot supply the Attend entry, produce the affected person's challenge, or replace the follow-up that only elapsed time produces.

## Attend stays in your own words

The [packet](templates/run-it-yourself.md#attend) asks you to leave the worksheet, use the [practice frame](PRACTICE-FRAME.md) during the practice, and return to write what you noticed. Speaking works as well as writing, under two conditions.

Record the note after the practice, not during it. Narrating while you practice turns the practice into a performance for the recorder, which is the risk the [self-filming form](FILMING-FORMS.md#self-filming) names. A screen recording, if you make one, runs during the practice and witnesses what the tool did. The voice note comes afterward and carries what you noticed. Keep them as two files.

Transcribe the note word for word, yourself or with a transcription tool you name in the record, and check the text against the audio before it stands in for the audio. The Attend entry is that text, marked as yours. A model in the [run-with-a-model packet](templates/run-with-a-model.md) may quote it. The [agent lane](llms.txt) forbids a model to produce the Attend entry, and a summarized or tidied version of your note is one.

## Three capture profiles

Each profile names a kind of practice, what to capture, whose permission it needs, and the smallest version that still produces a record. The table after the profiles says which step each kind of material can stand behind. All three profiles end in the same [worksheet](templates/run-it-yourself.md). Only a run that seeks a public return goes on to the [field-test report](templates/field-test.md), the structured record, the rights review, and the artifact-version decision.

### One person, one tool

- **Practice.** Your own use of an app, a feed, a model, or an inbox.
- **Capture.** A screen recording with the microphone off during the practice. A voice note or written note afterward for Attend. The tool's own exports, settings pages, and history as evidence that existed before analysis; they define the document-access set and its denominator.
- **Permission.** Your own, until another person appears in the material: a chat, a shared document, a name in the inbox. Their words are participant material, and for that material the run moves to the second or third profile.
- **Smallest version.** No recording. A written note for Attend and a dated list of what you looked at.

### A live facilitation practice

- **Practice.** A session you facilitate or take part in, with other people present.
- **Capture.** Name the [filming form](FILMING-FORMS.md) in use at each moment and who holds the camera. Hold the [protocol's pre-conversation](PROTOCOL.md#hold-a-pre-conversation) first. Audio alone is a smaller ask than video and is often enough. Your Attend note comes after the session, off camera, in your words. The participants' response to the footage is the affected-party challenge the record needs; it enters the record only with their permission, in their words or in wording they approved.
- **Permission.** One [consent register](templates/consent-register.md) per rights holder before the recorder starts, with audio, video, retention, transcript, each reviewer, and each artifact decided separately. The [editing interval](PROTOCOL.md#wait-before-editing) and the return default in the filming forms apply. Where the practice is held in common, the protocol's community-authority rule applies at full strength. Nothing from the session enters the repository; the public record describes the practice in general terms and cites the private artifacts by ID with their review status.
- **Smallest version.** No recorder. Your own note afterward, and one participant's challenge, collected in a form they chose and logged in the register.

### An organization's practice

- **Practice.** A team's, a business's, or an institution's handling of information: a reporting cycle, a customer data flow, a meeting rhythm.
- **Capture.** The material already exists: spreadsheets, decks, policies, tickets, chat exports, meeting recordings. List it as evidence that existed before analysis, with a denominator, exclusions, and a time window. Make no new recording before the register exists. Existing meeting recordings are participant material and follow the second profile. The Attend entry is still one named person's notice of their own attention inside the practice, written after being inside it, not after reading the files.
- **Permission.** Client and confidential records are protected material. If the run seeks a public return, they enter only through Stage 2, which [RIGHTS-AND-CONSENT.md](RIGHTS-AND-CONSENT.md#two-stage-intake) says begins only after the maintainer establishes a private channel, and the repository designates none by default. A transcription service or a model you run over the material is an AI-processing decision in the register and is disclosed in the report's AI-assistance section. The [AI system annex](AI-SYSTEM-ANNEX.md) applies when the organization's own practice includes a model, not to your tooling. The public record names the artifact set by count and kind, never by content. Anonymization does not settle re-identification or publication authority.
- **Smallest version.** One named person, one bounded flow, one document set counted rather than copied, and that person's own Attend note.

## What each kind of raw material can stand behind

| Raw material | Can stand behind | Cannot stand behind | Where it lives |
|---|---|---|---|
| Screen recording of your own use | Read and Trace readings cited by timestamp; the before and after of a reversible change at Adapt | The Attend entry; any causal claim | Your files, named in the record by ID |
| Voice note after the practice | The Attend entry, as its word-for-word text marked as yours | A reading, a score, or a finding | Your files |
| Session footage or audio | Read and Trace for the encounter; the participants' challenge in their words | Your Attend entry; consent to an edit, which is its own decision | Private custody, named in the register |
| Session transcript | The same, in searchable form | Anything the audio does not | Private custody; each transcript is a register decision |
| Documents, exports, spreadsheets, decks | The document-access set, its denominator, and the four access readings | A person-level outcome | Private custody; counted, not copied, in the public record |
| Model output over any of the above | A structural check, or a proposal marked as a proposal | Attend, a reading, a challenge, an outcome | The record's AI-assistance disclosure; the register holds the processing decision |

Before the recorder starts, assign the ID the record will cite, and complete the protocol's [custody and limits](PROTOCOL.md#record-custody-and-limits) items and, for anyone else's material, the register.

## What this does not do

This guide names material. It grants no permission and cannot produce a second reader, an affected person's challenge, or elapsed time. The [rights and consent guide](RIGHTS-AND-CONSENT.md), the [facilitation protocol](PROTOCOL.md), and the [filming forms](FILMING-FORMS.md) govern what may be recorded and kept.

**What would count against this.** If runs that keep recordings produce no more inspectable readings, word-for-word Attend entries, or affected-party challenges than runs kept in notes, the guide adds custody burden and buys nothing. If people who voice-note their Attend can hear themselves performing on playback, the after-not-during rule is not enough and the note should be written instead. Nobody has tested either; see [RESEARCH-STATUS.md](RESEARCH-STATUS.md) for both.
