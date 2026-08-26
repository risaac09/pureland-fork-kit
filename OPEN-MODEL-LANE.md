# The open-model lane

Use this document when your information practice includes AI models and you want two things at once: fewer places your words travel to, and evidence for your own quality claims. It describes how to run open-weight models on hardware you own, how to reach hosted open models without scattering credentials, and how to test model quality yourself instead of repeating a vendor's claim.

This is infrastructure guidance, not a certification. Running a model locally reduces one class of exposure: the prompt and the output stay on machines you control. It does not make your practice open, safe, or extraction-free by itself. The [AI system annex](AI-SYSTEM-ANNEX.md) still applies, and its rule still holds: do not call a whole system open because one part of it is visible.

## Why this is in the kit

Most AI use sends attention outward. Every prompt is a record of what you were thinking about, held by someone else, under terms you did not write. The [extraction check](EXTRACTION-CHECK.md) asks where value and records travel. For hosted AI, the honest answer is usually: out, continuously, in detail.

An open-weight model on your own hardware changes that one answer. The record stays home. That is the whole claim. Quality, bias, consent around training data, and the labor that produced the model are separate questions this lane does not settle.

## The three tiers

The lane assumes ordinary equipment: one main computer, maybe a spare machine, and a modest budget. Hostnames, ports, and model names below are examples to replace with your own.

### Tier 1: an always-on small model on a spare machine

A small open-weight model (a few billion parameters) can run continuously on a spare computer without disturbing anything else. Serve it with an OpenAI-compatible server such as `llama-server` from llama.cpp, supervised by the operating system's service manager (launchd on macOS, systemd on Linux) so it restarts on failure and survives reboots.

Point tools at it with one environment variable, for example `LLM_BASE_URL=http://workshop.local:8080`. Anything that speaks the OpenAI chat-completions protocol can use it.

Unlike the on-demand tier below, this server listens on your local network so other machines can reach it, and it has no authentication of its own. That is a deliberate trade: make it only on a network you trust, such as a home LAN or a private mesh network, and never expose the port to the internet. If only one machine will use it, bind it to localhost there instead.

Give it low-impact work only: format conversion, summarization of material you will re-read, bulk classification, first drafts you will rewrite. Two disciplines keep a small model useful:

- **Single-shot microprompts.** Send one system message and one user message, read one completion, end the session. A small model's quality drops fast as conversation history accumulates, well before a frontier model would notice. A task with several steps becomes several short calls, not one long chat.
- **A quality floor.** Work that audits, sweeps a corpus, or ships in your own voice does not go to the small model. If the output would need a careful human read anyway, the small model has not saved you anything.

### Tier 2: an on-demand large model on your main computer

A larger open-weight model (tens of billions of parameters, quantized) can run on a well-equipped personal computer, but only on demand. Start it when you need it, stop it when you are done. Four constraints matter, and each one comes from a real failure mode:

- **Never make it a persistent service.** On machines with unified memory, a large resident model starves every other memory-hungry application, including the creative tools the machine exists for. Start and stop by hand.
- **Cap the context size explicitly.** Servers default to the model's full trained context length. The memory for that context, on top of the model weights, can exceed physical RAM the moment a real prompt arrives, crashing mid-generation rather than at startup. Set a context size that fits your machine and your actual use.
- **Bind to localhost.** An on-demand personal model has no reason to listen on the network. Bind `127.0.0.1`, not `0.0.0.0`.
- **Keep the process record in a private directory.** A PID file with a fixed name in a shared temporary directory can go stale, and a recycled process ID means your stop command signals an unrelated process. Use a directory only this tool writes to.

The companion script [scripts/llm-lane.sh](scripts/llm-lane.sh) implements this tier and tier 1's client side as shell functions you can adapt.

### Tier 3: hosted open models through a gateway

Some open-weight models are too large for personal hardware. A gateway service that fronts many providers through one OpenAI-compatible endpoint lets you reach them with one account and one spending cap. This tier trades the locality claim away: the prompt leaves your machine again. Use it knowingly, for the work the local tiers cannot do, and keep the credential discipline below.

Configure providers by reference, not by value:

```yaml
providers:
  gateway:
    api: openai-completions
    baseURL: https://gateway.example.com/api/v1
    apiKeyEnv: GATEWAY_API_KEY   # the name of a variable, never the key itself
    models:
      - id: example/open-model-large
```

The configuration file names an environment variable. The key itself lives in a separate credentials file outside every repository, readable only by you. Set a hard spending cap at the provider before the first call.

## Credential discipline

These rules are cheap to follow and expensive to violate:

- Keys live in files outside every repository, in your home directory, excluded from backups that leave your control.
- Configuration and code reference keys by environment-variable name. No key appears in a file you might ever publish.
- A tool that needs a key reads it fresh at call time and does not export it into the environment of child processes, write it to logs, or echo it in errors.
- Anything published from a machine that holds keys gets a sweep first: search the change for key-shaped strings, provider names, and internal hostnames before it leaves.
- Test harnesses strip credential variables from the environment themselves rather than trusting a shell alias to have done it. An alias protects interactive shells only.

## Routing: match the model to the work

The lane only helps if work goes to the right tier on purpose. A simple routing habit:

| Work | Route |
|---|---|
| Deterministic transformation with no judgment | A script, not a model |
| Conversion, summarization, bulk classification, rough drafts | Tier 1 small model, single-shot |
| Heavy local reasoning, long documents, private material | Tier 2 large model, on demand |
| Work beyond local capacity, after weighing the exposure | Tier 3 gateway, capped |
| Audits, corpus sweeps, anything shipping in your own voice | Above the lane's floor: your strongest available model, and your own read |

The first row matters most. A model call that a twenty-line script could replace costs money or watts, adds nondeterminism, and teaches you nothing.

## Test it yourself: the paired bench

Model quality claims deserve the same discipline the kit asks of every other claim: an inspectable record, not a vibe. The paired bench is a method for answering one question: **do two models produce equivalent quality on the work classes I actually route between them?** It is not a leaderboard and it does not crown a winner. Its output is a routing decision per category of work.

The method, in the order a run executes:

1. **One task set, one harness.** Both models get the same tasks through the same harness, with the same prompts and the same tool access. If one side runs with tools and the other without, or one side's credentials leak extra context, the comparison measures the harness, not the models. This is the parity rule, and it is the first thing to check when a result surprises you.
2. **Deterministic graders first.** Each output is scored by scripts with a fixed contract: candidate text in, one line of verdict JSON out (`pass`, or `skipped` with a reason). A grader that crashes must report `skipped`, never `pass`. Silence read as success inverts the whole method.
3. **Planted-bad probes.** The task set includes at least one known-bad fixture the graders must fail. If a probe passes, the graders are not discriminating anything and the run is invalid. This catches the quiet failure where every check returns green because every check is broken.
4. **Coverage before verdict.** A run where any generation, grader, or judge failed to return is incomplete, and incomplete is never a pass. Count what actually ran before reading what it said.
5. **Blind paired judging, both orders.** For the qualities scripts cannot score, model judges compare the two outputs without knowing which model produced which. Each judge sees the pair twice with the order swapped. A judge that picks a different winner when the order flips has told you it is judging position, not quality: score that comparison a tie. Judge identity stays independent of the contestants; a judge never inherits a contestant's configuration, and using judges from both model families keeps the judge-favors-its-own-family bias symmetrical instead of hidden.
6. **Judge the judges.** Judges are models too, and an untested judge is a leak in the method. Track agreement between judges across runs, re-judge stored outputs to measure whether a judge agrees with itself, and check whether a judge systematically favors outputs from its own family. Report judge health next to the results it produced.
7. **Count the cost.** Record tokens, duration, and money (or watts) per generation, and carry a cost column in every report. A quality difference only becomes a routing decision when you can see what the difference costs.
8. **Decide per category, on repetition.** One run is an anecdote. A routing change waits for the same divergence to appear across independent runs, and it applies to the category of work where it appeared, not to everything.

A reference implementation of this method runs in the maintainer's private stack; the harness itself is not part of this kit. What the kit offers is the method and the card format, so you can build a harness of any size, from a shell script to a real pipeline, and know which properties it must not lose. [templates/bench-card.yaml](templates/bench-card.yaml) is the card: one file that declares the contestants, the task set, the judges, and the pass threshold for one bench, so a run is reproducible and a reader can see what was compared.

## What this document does not claim

- It does not claim local models match hosted frontier models in quality. Often they do not. The bench exists so you know where, for your work, the difference is real.
- It does not claim locality equals privacy in general. Your operating system, your network, and your backups have their own exposure paths.
- It does not audit the provenance of open-weight models themselves: training data consent, labor, and energy remain open questions the [extraction check](EXTRACTION-CHECK.md) can be pointed at.
- No field test of this lane exists in the [trial ledger](FIELD-TRIALS.md). The lane is offered as documented practice from one stack, not as validated method.
