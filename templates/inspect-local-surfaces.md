# Inspect selected local surfaces

This optional Scope exercise supplies evidence for [the method](../METHOD.md). Read its [private-use path](../METHOD.md#run-it-yourself) first. The [evidence ceiling](../CURRENT-EVIDENCE.md) still applies. The instrument's name remains [reserved].

## Before a read

Keep the run private on your own machine. Choose an unsynced output directory. Disconnect the machine's outbound connection and pause sync clients before using sources. If you cannot establish that boundary, use paper and manual tasks. The script cannot govern another process, a remote filesystem, or a backup service.

Write a permission file yourself. Record each surface's metadata choice and content choice separately as `yes`, `no`, or `not yet`. Choose opaque surface IDs. A rejected surface may have an empty path. This is a local access instruction; it grants no rights over another person's material. The [rights boundary](../RIGHTS-AND-CONSENT.md) applies.

```json
{"window":"person supplies the snapshot window","surfaces":[
  {"id":"selected-folder","path":"[reserved]","metadata":"not yet","content":"no"}
]}
```

The person chooses every path and permission. An operating-system file dialog or access grant permits a process to attempt access. It grants no research or publication permission. Never enable Full Disk Access for this exercise. A rejected permission yields `unmeasurable`. Record a deliberate offline boundary separately as `intentionally absent`, with reasons only if you want to give them.

## Run once

The [script](../scripts/inspect_local_surfaces.py) takes the permission file and a new output path:

```sh
python3 -B scripts/inspect_local_surfaces.py /absolute/permission.json /absolute/private/snapshot.md
```

The automated path is a gated prototype for macOS. It requires a successful OS sandbox rehearsal. The development session could test its refusal when sandbox creation was denied; it could not verify a successful isolated scan. Keep automated use gated until a second reader runs synthetic fixtures on a host that permits isolation, confirms denied egress and writes, and inspects the produced file. The [synthetic tests](../scripts/test_local_surfaces.py) do not clear that gate.

The script writes the permission record before enumeration. It opens approved folders once and inspects direct directory entries. It counts regular-file entries by fixed file-type bins. It excludes subdirectories and links. It never opens file contents. The candidate-entry count includes exclusions; the counted-file denominator excludes them. Empty sets have a zero denominator and no ratio. Hard links count as entries. They do not establish distinct works. Concurrent changes can prevent reproduction; use a stable selected folder or an existing local export.

Press Control-C to stop. A stopped report remains incomplete. The final self-check prints the reads and the single output, along with the removal command. Deleting that file cannot erase copies held by another process. The script never starts a model or watches for changes.

## Compare the evidence

Before counting, write what you expect to find and one route you believe works. Attempt a retrieval under a time limit you choose first. Record help and refusals separately from unsuccessful attempts. After counting, identify any changed expectation and the exact evidence that changed it. A count can describe a selected set while leaving the retrieval problem unexplained.

Use the [scorecard context](../SCORECARD.md#context) per surface. Complete the [value trace](../EXTRACTION-CHECK.md#1-trace-value) yourself. For a model in the practice, use the [audited-unit table](../AI-SYSTEM-ANNEX.md#define-the-audited-unit). Counts cannot establish recipients, consent, or value return. The script leaves those readings to the person.

Use the survey and manual tasks if no script or model is available. The person writes Attend. A model may propose a reading only under [llms.txt](../llms.txt); it has no command authority. Any optional model runtime requires a separate verified application boundary before receiving even the count report. No runtime integration ships here.

You own the report. Review it at the end of each sitting. At the final review, choose deletion or a private retention event. Record each party's active minutes separately from elapsed days. Sharing with the maintainer, research use, and publication each require a later decision. Keep these decisions unavailable until the [private handling gate](../OFFERING.md#present-arrangement) has been exercised.
