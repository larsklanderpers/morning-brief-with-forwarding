---
date_first_seen: 2026-07-20
date_updated: 2026-09-20
source: "@emollick · @0xCodila (Heinlein inbox) · AI brief 2026-09-20"
url: https://x.com/emollick/status/2073248523215089825
brief: work
threads: [Shape of Work-to-Come, AI Sovereignty, Co-Existence - Judgment, Trust Boundaries]
beat: Future of Work / Agent Architecture
status: signal
used_in:
---

# Two competing visions for agentic routing

**What happened.** Mollick lays out the architectural fork: a smart frontier model acting
as router and delegating downward, versus a local lightweight model calling up for help
when it needs to. He leans frontier-first — "start with a smart AI planner, let it
delegate on its own."

**Why it matters.** This is a plumbing decision that determines which human role survives.
If the frontier model orchestrates, the human moves up to Conductor — setting objectives
and interpreting outputs, never touching tool calls. If routing stays local, the human
stays closer to Orchestrator, managing the machinery. Worth noting the sovereignty
collision: frontier-first routing means the planning layer — which sees everything —
is the part that leaves your building. The privacy-optimal architecture and the
capability-optimal architecture point opposite ways.

## Observations

- **2026-07-20** — First seen. The sovereignty tension is mine, not Mollick's; he is arguing capability.
- **2026-09-20 (Heinlein inbox)** - **The local-router side of the fork shipped, and the fork is no longer hypothetical.** TypeSafe AI's **Jev** is a "System One" model: it returns typed answers with calibrated probabilities instead of text, for routing, tool selection, classification and escalation. SDK `@typesafe-ai/sdk`, already on Vercel's AI Gateway and OpenRouter, with a LangChain classifier integration. Mollick leaned frontier-first in July; this is the other branch with a product behind it. ⚠️ **Nothing here is footed at a primary - typesafe.ai was not fetched.** Speed and cost multiples in circulation ("up to 193.6x faster, 444.6x cheaper", rounded by secondaries to 200x/400x) are **TypeSafe's own evaluations, no independent benchmark**, and our own corpus disagrees on the launch date (`ai_brief_2026-09-20.md` says 15 Sep per Generative Programmer; MarkTechPost says 19 Sep). Do not print either. Details: `Research Notes\intake\intake_2026-09-20_jev-grokbot-router.md`.
- **2026-09-20, the part that makes it a Trust Boundaries item.** The story reached Lars as **@0xCodila's seven-step install thread** (19 Sep, ~254K views, 4,486 bookmarks): mint a TypeSafe API key, have Grok Bot store it, have Grok Bot install the SDK on the Agent Computer, add a `jev-usage-router` skill that fires before browser, research, retry or extra-bot calls. **The routing layer arrives as a credential and an install handed to the agent on the one shared machine** - the same shape as [[Managed agent harnesses - the vendor keeps the session]]. ★ **And the twist worth keeping: steps 6 and 7 are genuinely disciplined** (shadow mode first, read the logs, go active only on trust, a named kill switch, humans keep irreversible actions) **inside a thread whose closing instruction is "install it as soon as possible". The care is in the recipe; the framing is what travels.** The poster links his own repo and a deep dive; whether he is paid or affiliated is undisclosed either way.

## Feeds

- [[Shape of Work-to-Come]] — which archetype the plumbing selects for
- [[AI Sovereignty]] — the router sees everything, so where it runs is the whole question
- [[Co-Existence - Judgment]] - and, from 20 Sep, the judgement-model reading: if the machine returns "72% likely", the scarce skill is knowing which decisions are worth escalating
- [[Trust Boundaries]] - added 2026-09-20: the local router installs *inside* the agent's boundary, with a credential it holds

## Open

- Strong piece candidate: the routing decision as a sovereignty decision nobody is framing that way. Crosses two threads cleanly.
- **Sharper since 20 Sep, and it is a different piece from the one above:** the small local router is the privacy-optimal branch *and* it arrives by telling people to hand a key to a bot. **The architecture that keeps your data in the building is being installed by the least careful available method.** Unspent.
- ⚠️ **Slot caution, not a piece caution.** Sat 19 promised a return to Grok Bot on a *later* Saturday and Sat 26 is already committed to the attention widget. This is not Sat 26 material.
