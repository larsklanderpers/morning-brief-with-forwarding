# Research Note — Taking back control of your inference: the on-ramp ladder
For: Sat Aug 8 diversion ("Own the kitchen / build your own rung") · Depth: deep · Date: 2026-07-29

## Bottom line (read this first)
Lars's thesis holds and the evidence sharpens it. "Full frontier on a laptop" is genuinely
oversold — but a *useful small* model on a Mac you already own is real, cheap, and private,
and the honest story is the **graduated ladder**, not the hardware. The cost curve
substantiates the line exactly: the first rungs cost pennies or are already paid for (cost of
curiosity → 0); real local/on-prem control costs your time and then real hardware (cost of
tooling ≠ 0). **One major finding to flag before drafting:** the "Hermes" Lars wants to
recommend as an on-ramp is the *same* open-source Nous Research agent that ran YOLO-mode
post-exploitation against Thailand's Finance Ministry in this week's cyber brief — same tool,
confirmed. That's not a landmine; handled deliberately it's the sharpest possible illustration
of the whole week's guardrails-as-freedom thesis. But it means Hermes is an advanced rung with
a caution built in, not a beginner's first step.

## What's solid

- **What actually runs on an Apple Silicon Mac, by memory tier** (unified memory = the model's
  "VRAM"). Solid, multi-tier, with a named benchmark (Simon Willison):
  - 8GB: Gemma 4 E2B (~1.5GB), Qwen 3.5 4B, Llama 3.2 3B — 25–45 tok/s. Tight; macOS eats 2–3GB.
  - **16GB (the realistic everyday MacBook): Qwen 3.5 9B Q4 (~6.6GB) — 20–40 tok/s, "strong
    all-rounder."** This is where most readers actually are.
  - 24GB: Qwen 3.6-27B Q4 (~16.8GB) — 18–28 tok/s (Willison clocked 25.57), "flagship-class
    coding output on a single Mac."
  - 32–48GB: Qwen 3.6-35B-A3B MoE (~20GB) — 35–55 tok/s (MoE activates only 3B/token).
  - 64GB+: Llama 3.1 70B Q6 (~55GB) — 8–15 tok/s (slower than reading speed).
  - Source: [InsiderLLM, Best Local LLMs for Mac 2026](https://insiderllm.com/guides/best-local-llms-mac-2026/).
- **The unified-memory advantage is the "leverage what's already there" fact:** a 32B model
  runs on a Mac that would need a $1,000+ discrete GPU on a PC. The MacBook someone already owns
  is a surprisingly capable rung — for free.
- **The "Rex runs it on his MacBook for his golf trainer" anecdote is fully plausible.** A
  bounded, personal-context assistant (coaching notes, drills, Q&A) on a 16GB+ Mac running
  Qwen 9B or Gemma via Ollama/LM Studio is precisely local's sweet spot: private, always-on, no
  per-token cost. Safe to use as the concrete opener.
- **Hermes = the attack tool, confirmed as the same thing.** The Thai Finance Ministry agent is
  "Hermes, an open-source assistant from Nous Research that people install to manage their mail,
  run chores, and take instructions over Telegram or Slack… It is not a hacking tool." The
  operator enabled **YOLO mode** — "a documented feature with its own command-line flag"
  (`--yolo`) that disables the approval prompts. It "runs locally on the operator's machine," so
  no vendor could monitor or ban it. Sources:
  [The Hacker News](https://thehackernews.com/2026/07/hacker-runs-hermes-ai-agent-unattended.html),
  [BleepingComputer](https://www.bleepingcomputer.com/news/security/hermes-ai-agent-used-to-automate-attack-on-thai-finance-ministry/).
- **Two distinct Nous "Hermes" things** — don't conflate: **Hermes (LLM family)**, fine-tuned
  open-weight *models*; and **Hermes Agent**, an MIT-licensed autonomous *framework* (plans,
  calls tools, executes code in sandboxes, self-improves, model-agnostic — points at OpenAI,
  Anthropic, OpenRouter, or 300+ models). The attack and the YOLO flag are the **Agent**.
  Source: [AI Engineer Insights](https://aiengineerinsights.com/blog/hermes-agent-nous-research-guide/).
- **OpenRouter genuinely fixes the "you didn't get the model you paid for" problem — by making
  routing explicit.** You can pin a specific provider/model, and enforce Zero Data Retention
  globally, per-model-group, or per-request (`zdr` parameter). Source (primary):
  [OpenRouter ZDR docs](https://openrouter.ai/docs/guides/features/zdr).

## What's contested / watch out

- **"Control" via an aggregator is real but partial — say so.** ZDR means a provider won't
  *retain* your data, not that it never *sees* it: "Providers… receive your data to process
  requests," some "retain data without training on it to scan for abuse or for legal reasons,"
  and "a provider's general policy may differ from the specific policy for a given endpoint"
  ([OpenRouter](https://openrouter.ai/docs/guides/features/zdr)). So the aggregator rung buys
  *visibility and configurability* over model identity + retention — it moves the trust boundary
  and lets you set it; it does not eliminate it. **Real inference containment (data never leaves)
  begins at the local rung.** This is the honest spine of Q4.
- **Frontier-class open weights ≠ laptop.** Kimi K3 (2.8T sparse MoE, reportedly matches Opus
  4.8) is the "own the kitchen" event — but that's the *serving* tier (datacenter-scale, the
  1.4TB reality), not a Mac. The laptop tier is 9B–35B small models. Keep the two rungs visibly
  separate. (Also: the Opus-parity claim is single-source benchmark reporting — don't assert it
  as settled; and Chinese-origin weights carry a provenance flag.) Source: vault
  `Kimi K3 open weights`.

## Couldn't verify / scoped out

- **The `The open-weight ceiling is physical` [VERIFY] resolves by scope, not by number.** Its
  HBM/energy/datacenter bottleneck claim is about who can *serve a frontier model in-house* — it
  is irrelevant at the laptop tier, where small models run fine on hardware you own. So Saturday
  does **not** need those unverified figures at all; the Mac benchmarks above are the anchor.
  The ceiling note stays out of this piece. ([VERIFY] therefore never has to ship here.)
- **Exact OpenRouter fee mechanics** (credit-purchase fee %, any minimums) — not pinned to a
  primary pricing page in this pass. Frame usage as "pay-per-token credits, no subscription;
  light personal use runs to cents-to-a-few-dollars a month" and don't quote a specific fee.

## The economics — the cost curve that proves the thesis

| Rung | What it is | Dollar cost | Tooling / time cost | Control you actually get |
|---|---|---|---|---|
| 0 | The AI you already pay for (ChatGPT Plus / Claude Pro) | ~$20/mo, already sunk | ~0 | Least — vendor routes & retains per their terms |
| 1 | Aggregator (OpenRouter) | Pay-per-token; cents–few $/mo light use | ~1 hr to wire up | Pin the model; configure ZDR. Visibility + config, not containment |
| 2 | Hosted open-weight (Nous Portal / Together / Fireworks; Hermes *models*) | Sub or per-token | Low | Choose open model; still hosted |
| 3 | Local on a Mac you own (Ollama / LM Studio) | $0 marginal | ~1 hr setup; small models only | Real containment — data never leaves |
| 4 | 24GB workstation / dedicated box (MarkTechPost tier) | $1–2k+ hardware | Real setup + upkeep | Serious on-prem agentic |

**The line, substantiated:** cost of *curiosity* → 0 (rungs 0–1 are pennies or already paid; the
Mac you own is a free rung 3 for small models). Cost of *tooling* ≠ 0 (rungs 3–4 cost your time,
then real capital). "Be prudent, leverage what's already there" = start at rung 0/1, and note the
laptop you already own is a more capable rung 3 than people assume.

## Drop-in facts (citable, ready for the draft)

- "Qwen 3.5 9B on a 16GB Mac: ~20–40 tok/s, a strong all-rounder" — [InsiderLLM](https://insiderllm.com/guides/best-local-llms-mac-2026/).
- "Simon Willison clocked Qwen 3.6-27B at 25.57 tok/s on a 24GB Mac — flagship-class coding on a single machine" — [InsiderLLM](https://insiderllm.com/guides/best-local-llms-mac-2026/).
- "Hermes is an open-source assistant from Nous Research that people install to manage their mail, run chores… It is not a hacking tool" — [The Hacker News](https://thehackernews.com/2026/07/hacker-runs-hermes-ai-agent-unattended.html).
- "YOLO… a documented feature with its own command-line flag" that disables approval prompts — [The Hacker News](https://thehackernews.com/2026/07/hacker-runs-hermes-ai-agent-unattended.html).
- OpenRouter ZDR is enforceable "globally, per model group… or per individual request" but providers still receive the data to process it — [OpenRouter](https://openrouter.ai/docs/guides/features/zdr).
- 24GB-GPU tier verdicts (workstation, not laptop): Qwen3.6-27B general default; Gemma 4 26B vision/140+ languages; Mistral Small 3.2 24B lightest; runtimes Ollama / llama.cpp / vLLM — [MarkTechPost, 19 Jul](https://www.marktechpost.com/2026/07/19/best-local-llms-you-can-run-on-a-single-24gb-gpu-in-2026-qwen-gemma-mistral-deepseek-compared/).

## Angles this opens

- **The Hermes dual-use bridge (Saturday ↔ Monday ↔ capstone).** The exact tool you'd recommend
  for sovereign, local, no-vendor-oversight inference is the one an attacker ran unattended —
  *because* it's local with no vendor oversight. The `--yolo` flag literally is the guardrail:
  human-in-the-loop approval ships ON; YOLO turns it off. That is the capstone's
  "guardrails are how you give it away" rendered in one command-line flag. Recommend the ladder,
  and use Hermes as the cautionary top rung, not the first step.
- **Explicit routing as the fix for hidden routing.** OpenRouter answers Monday's "you didn't get
  the model you paid for": the cure for opaque vendor routing is a layer where *you* pin the model.
