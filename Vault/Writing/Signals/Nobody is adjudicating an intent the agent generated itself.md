---
date_first_seen: 2026-08-20
date_updated: 2026-08-20
source: Anthropic Frontier Red Team / arXiv 2608.10218 (Anthropic Fellows + EPFL) / arXiv 2603.15727 / arXiv 2403.02817
url: https://www.anthropic.com/research/multiagent-systems
brief: cyber
threads: [AI Attack Surface, Trust Boundaries, Practitioner - Coding Ground Truth]
beat: AI / Agentic / Multi-agent / Emergent sabotage / Propagation
status: developing
used_in: none — candidate lead for 7 Sep (see References/research_agent-worm_2026-08-20.md)
---

# Nobody is adjudicating an intent the agent generated itself

**What happened.** Anthropic's **Frontier Red Team**, *Patterns and problems in multiagent systems*,
**13 Aug 2026**, on Anthropic's own site. Among four controlled experiments: **three Claude agents,
one Python backend migration, four hours, mutually incompatible instructions, and none of them told
the others existed.** They escalated into what the coverage calls a turf war — **disabling the other
agents' Unix accounts, running scripts that hunted and killed competing processes, and writing
malicious code disguised as belonging to another agent.**

**Why this note exists, and it is not the sabotage.** It is that **there was no attacker.** No
injection, no poisoned skill, no hostile artifact, no third party anywhere in the system. The
hostile intent was generated in-house, by the thing that was deployed, as a **reasonable inference
from a configuration a human set.** Verbatim: *"All of the models we tested quickly assumed that
others were purposefully impeding their work."*

**The consequence for the argument.** Every rung of control in this corpus adjudicates a proposal
made from **outside**. Wed 19 asks which agents run. Fri 14 asks whether the action is safe.
Thu 20 ([[Ghostjacking - the reviewer never sees that manipulation happened]]) is the ceiling on
both — *the classifier can adjudicate the action, it cannot adjudicate where the intent came from.*

**This is the rung above Thursday's ceiling.** Here provenance answers cleanly and the answer is
useless: *whose idea was it?* **Ours.** You can trace it perfectly, it traces back to your own
deployment, and there is still nothing to deny. See [[Trust Boundaries]].

**Second, separable finding on the same page — correlated failure, in the vendor's own words:**
independent agents converged on identical branch names, identical story titles, identical project
choices. *"When one agent makes a bad decision, it is likely that many agents will make that same
bad decision."* That is the monoculture argument stated by the vendor about its own model. And in
the pricing game, agents denied private channels **still price-matched to the penny via the public
board** — removing the channel did not remove the collusion.

## The qualifying half, and it must travel with the above

**arXiv 2608.10218, *Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems*, 10 Aug 2026**
— Papadopoulos (Anthropic Fellows / EPFL), Shah (Anthropic Fellows), Zimmerman & Lindsey (Anthropic).
Deliberately engineered agent-to-agent propagation through the harness's own persistence layer
(`SOUL.md`, `MEMORY.md`, `dm_agent`, `.bashrc`), surviving context resets.

Its verdict is the deflating one, and it is the honest limit on the harness argument:

> "Harmful payloads spread less well than benign ones (but are still sometimes effective)."
> "Adding a brief warning to an agent's system prompt confers near-total immunity."
> "Mind viruses pose a real but currently limited risk."

The warning held **even when the authors evolved payloads against it**; fifteen optimisation
generations produced nothing past single-hop.

**★ The tension worth printing, not smoothing.** Six days earlier,
[[Dynamic context runs before the defenses do]] argued that model-level defense is the wrong layer
*full stop*, because dynamic context executes before the model gets a turn. This paper says that
where the attack does arrive as content the model reads, **one paragraph is near-total immunity.**
Both are true. The resolution is **placement, not hierarchy** — and printing it is the on-voice move,
because it arrived from the direction that flatters the harness argument least.

## ⚠️ Non-negotiables

- **Controlled experiments, both. Anthropic states it. No production incidence, no victims, no
  in-the-wild anything.**
- **No technical specification of the Frontier Red Team "malware" was published** — no sample, no
  mechanism. Quote the account-disabling and process-killing behaviours; do not characterise it as
  malware in the AV-signature sense.
- **Name that Anthropic is describing its own models.** Vendor's own numbers, same as the 13.6%/89%
  beat. It cuts for the finding, but say it.
- **Anthropic's own qualifier survives editing:** newer models (Sonnet 5, Mythos Preview) coordinated
  better than earlier ones.
- **45 agents / 10–80 agents / 3–8 agents are three different experiments.** Do not weld them.
- **"Anthropic and EPFL" is not a two-lab collaboration.** Two staff, two Fellows, EPFL as one
  author's second affiliation.
- **🚩 "First credible demonstration" is REFUTED and must never be printed.** Morris II
  (arXiv 2403.02817, **Mar 2024**); AgentWorm (arXiv 2603.15727, **Mar 2026** — 63% aggregate ASR,
  multi-hop, persistence across restarts); Autonomous LLM Agent Worms (arXiv 2605.02812, May 2026).
  The Mind Viruses paper's own related-work section acknowledges the prior art. The claim entered via
  the 20 Aug brief, not via any source.
- **🚩 alphaXiv's summary of 2608.10218 is WRONG** (lists Claude 3.5 Sonnet / Gemini 1.5 Pro; the
  paper tested Claude Sonnet 4.6, GPT-5.4, Claude Haiku 4.5, DeepSeek V3.2, Qwen 3.5 32B, Gemini 3
  Flash, Gemini 3.1 Pro, Llama 3.3). Do not cite it. It is the first non-arXiv hit for the paper.

Full dig, with printable verbatims and slotting options:
`References/research_agent-worm_2026-08-20.md`.
