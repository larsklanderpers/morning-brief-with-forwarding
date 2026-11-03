---
date_first_seen: 2026-08-07
date_updated: 2026-08-07
source: METR / DORA 2025 / Stack Overflow 2025 / Stanford (Denisov-Blanch)
url: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
brief: work
threads: [Practitioner - Coding Ground Truth, Shape of Work-to-Come, Co-Existence - Judgment]
beat: Future of Work / Engineering Productivity
status: developing
used_in:
---

# Specification is the chokepoint — and the evidence is more interesting than the claim

**What happened.** r/ExperiencedDevs sentiment in the 7 Aug work brief: senior engineers are gaining
leverage, not losing jobs, and *"the chokepoint is shifting from implementation to specification — writing
the brief the agent executes correctly is now the hard skill."* Treat that as **the hypothesis being
tested**, attributed as sentiment. Reddit is not data. Here is what actually is.

## The strongest study cuts *against* the optimistic version

**METR RCT, 10 July 2025.** 16 experienced open-source developers, **246 real issues** in mature repos
(22,000+ stars, 1M+ LOC). Developers using AI tools took **19% LONGER**. They predicted a 24% speedup
beforehand — and **still believed AI had sped them up by 20% afterwards.**

**That perception gap is the most quotable finding in this whole area**, and it is the specification thesis
turned inside out: if experienced developers cannot tell whether the tool helped them on their own codebase,
the skill being tested is not writing the brief — it is **measuring the outcome.**

METR's own limits, which should travel with the number: it does **not** show AI fails to speed up developers
generally; don't generalise beyond software; doesn't apply to less experienced devs or unfamiliar codebases;
possible learning effects past 50 hours of tool use.

## DORA names the mechanism

**Google / DORA State of DevOps 2025:** **90% of tech professionals now use AI at work**, **80%+ report
increased productivity**, and **30% have little or no trust in AI-generated code.** The core finding is a
paradox — higher AI adoption correlates with **both increased throughput AND increased delivery
instability.** DORA's term for the cost is the **verification tax**.

The line to keep, from a DORA respondent:

> *"I feel somewhat more productive, but it's at a cost. While I end up spending less time writing code,
> **I spend more time babysitting the AI**."*

**That is BCG's 47% stat spoken by an engineer.** See [[The archetypes converge on one shape]].

## Where the leverage story does hold up

**Stanford, Denisov-Blanch, 100,000+ developers** (ongoing; conference talks and writeups —
**no peer-reviewed paper found, flag it**). Gains vary by *context*, not by tool:

- Greenfield low-complexity **+30–35%**; greenfield high-complexity **+10–15%**
- Brownfield low-complexity **+15–20%**; **brownfield high-complexity +5–10%, some teams negative**
- Popular languages +10–20%; niche languages (Clojure, Haskell, Elixir) minimal or negative
- Median team **~+10%** — but the **gap between top- and bottom-quartile teams widened to nearly 4x**

**That 4x spread is the leverage story, properly stated.** Not "seniors gain, juniors lose" — *the same
tool produces a 4x difference in outcome depending on who points it at what.* One 350-engineer case study:
more PRs shipped, **maintainability −9%, rework up 2.6x, effective output flat.**

**Stack Overflow 2025** (33,662 responses) supplies the texture: **84% use or plan to use AI tools** (up
from 76%), only **3.1% "highly trust" accuracy** while **46% actively distrust**; the top frustration is
**"AI solutions that are almost right, but not quite" (66%)**, and **45% say debugging AI code takes
longer.** Positive sentiment fell from 70%+ to **60%**.

## The honest synthesis

The chokepoint has moved, but not to specification — it has moved to **verification**. Writing the brief is
the visible half; the expensive half is knowing whether what came back is right, and the evidence says
experienced people are **bad at judging that even about their own work**. That reframes the archetype list:
the **Sweeper, Editor and Risk Steward** aren't consolation roles for people who can't orchestrate — they
are where the measured cost actually sits.

## Observations

- **2026-08-07** — First seen as Reddit sentiment. The verification research inverts it into something better and more defensible. Pairs directly with [[Remote Labor Index - the 2.5% is nine months stale]]: RLI measures end-to-end delivery, METR measures perceived-vs-actual speed, DORA measures the throughput/stability trade. Three different instruments, same finding — **the gap is at the end of the task, not the start.**

## Feeds

- [[Practitioner - Coding Ground Truth]] — the thread's best empirical set to date
- [[Shape of Work-to-Come]] — the archetypes, re-ranked by where cost actually lands
- [[Co-Existence - Judgment]] — verification *is* the judgment
- [[Entry-ladder compression]] — a 4x team spread is a different inequality story than a seniority one

## Open

- **Do not use the "Agent Orchestrator $260k–$420k" comp band.** Chased to source (The AI Career Lab, 25 Apr 2026): the range attaches to **"AI Agent Architect,"** the phrase "Agent Orchestrator" never appears, there is **no disclosed methodology** — no dataset, no sample, no survey — and no corroboration exists. Single-source, method-free, mis-titled. If a comp number is needed, pull it from levels.fyi or postings directly.
