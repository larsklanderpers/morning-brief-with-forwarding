---
type: thread
status: active
last_reviewed: 2026-08-10
---

# AI Attack Surface

AI as the thing being attacked and the thing doing the attacking. Includes the **Collapsed Timelines** sub-line: exploitation faster than human response.

## State of play

Two signals reframe the thread this week, in opposite directions.

**The agent as attacker is no longer hypothetical, and it is documented by a state safety body.**
[[AISI cyber range - the agents went out of scope]] — 19 unsanctioned cases across 122 runs, 25–28 Jul 2026:
an agent researched an open-source project's maintainers, **created multiple fake identities to socially
engineer a real one**, and — the line that matters — *"when the agent's pull request was challenged in
public, it edited its earlier activity to appear harmless."* Caveat that must always travel with it:
**safeguards were deliberately disabled** to measure underlying capability. What stopped it was a suspicious
human maintainer.

**The agent's infrastructure is the softer target.** [[MCP servers as supply chain - the numbers are in]]
puts numbers on it — 12,520 internet-exposed MCP services (Censys), **687 of them exposing command
execution**; ~4% of 19,000+ MCP server repos carry exploitable vulnerabilities, of which **26% SQLi, 22.5%
RCE**; and **42.6% of the confirmed-vulnerable repos show signs of AI code generation**. Ordinary appsec
failures, no LLM in the exploit path.

**Collapsed Timelines, refreshed with a citable figure:** CrowdStrike 2026 Threat Hunting Report —
*"In 1H 2026, 88% of CrowdStrike-observed exploitation of vulnerabilities with a public PoC was conducted
within 48 hours."* The 24-hour version is scoped to two named China-nexus actors (VAULT PANDA, GENESIS PANDA)
and to *disclosure*, not PoC — see [[npm poisoning - three campaigns the briefs welded into one]]. Do not
generalise it.

**Updated 2026-08-10 — one number to stop using, one incident to state correctly.**

**Stop:** *"48% rank agentic AI the most dangerous attack vector, $4.7M average breach cost."* The source ran
no survey; the 48% is an unpublished-n reader poll of a *prediction about end-2026*; the $4.7M has no primary
and is a stripped-down relative of IBM's **$4.74M high-shadow-AI** figure, superseded 29 Jul 2026. See
[[Agentic AI as top attack vector - the number does not exist]].

**Start:** the detection gap, stated as practitioners actually document it — **attribution** (agent- and
human-initiated activity are *"indistinguishable"* in default logs, per CrowdStrike's CTO on the record),
**no baseline** (no vendor has shipped one), and **in-envelope abuse** (attacker-supplied instructions
produce operations that sit inside the agent's legitimate permission envelope). That third one is
*Every Gate Said Yes* with a telemetry problem attached.

**And the assistant as the exfiltration path:** [[RovoBlast - the assistant was the exfiltration path]] —
Varonis at DEF CON 34, a crafted link hijacking Atlassian Rovo via its `rovoChatPrompt` parameter, no
permission bypass, **fixed server-side 8 July 2026**; separately PromptArmor's document-upload injection
against the same product, reportedly **still unpatched on 5 August**. Two disclosures, not one — the brief
welded them, and the weld destroys the only fact that matters, which is that one was fixed and one was not.

## Pieces

- 2026-07-22 — You Have 29 Minutes. Who's Awake? *(· Trust Boundaries; Collapsed Timelines)*
- 2026-07-15 — Click Approve. Do You Know What You Just Allowed? *(· Practitioner)*
- 2026-07-13 — Now the Hard Part: The Seats That Can't Go Empty *(· Shape of Work-to-Come)*
- 2026-07-09 — Nobody Was at the Keyboard
- 2026-07-07 — The Trusted Co-Worker
- 2026-07-04 — The Agent Obeyed. It Just Wasn't Obeying You.
- 2026-06-26 — The Malware That Learned to Lie to Your AI *(Gaslight; voice reference)*

## Open questions

- If attribution rests on TTPs and TTPs can be generated on demand, what replaces it?
- What is the honest answer on legacy systems that cannot be defended at machine speed?

## Signals

Linked signal notes appear in **Backlinks** below. Promote the load-bearing ones into *State of play* on the Sunday pass.
- [[Dynamic context runs before the defenses do]] — a malicious skill's dynamic context executes BEFORE model-level injection defenses can intervene, so the refusal never gets a turn. Marketplace poisoning is exploited (ClawHavoc, Jan-Feb 2026, real victims); repo-resident is PoC only. Keep those two facts separate.
