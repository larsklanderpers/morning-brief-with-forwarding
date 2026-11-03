---
type: thread
status: active
last_reviewed: 2026-08-07
---

# Supply Chain

Trust inherited from upstream — packages, maintainers, vendors, hardware. Promoted to active 2026-08-07: four verified signals in one week and a stated thesis.

## State of play

**Promoted 2026-08-07 — the thread is no longer thin, and it has a thesis: the trusted layer is the
primary attack surface.** Four verified signals landed the same week, and they share one architecture —
each target was chosen *because* it is trusted and holds privileged, automatic access.

- [[N-able N-central - the patch that did not hold]] — the MSP management plane, and **the incomplete patch
  was the way in**: CVE-2026-18577 is the failed fix for CVE-2026-18556. Persistence via a Cloudflare tunnel
  that survived revocation.
- [[TeamPCP - the security toolchain became the supply chain]] — Trivy, Checkmarx/LiteLLM and Bitwarden CLI
  across five weeks, each stage funded by credentials stolen in the last. Microsoft: *"Threat actors leveraged
  access from a prior incident that was not fully remediated."*
- [[npm poisoning - three campaigns the briefs welded into one]] — Mastra's SLSA provenance existed and its
  absence simply wasn't enforced; NullReceiver hides C2 in Ethereum recipient addresses; the keyv worm crossed
  organisations every 2–7 minutes while four vendors counted it four different ways.
- [[MCP servers as supply chain - the numbers are in]] — **40.55% of live remote MCP servers expose tools
  with no authentication** (Fudan, n=7,973), and of 119 OAuth-enabled servers, **all 119 were flawed**.

**The connective tissue is incomplete remediation**, not novel technique. N-able's hotfix 1, TeamPCP's
"prior incident not fully remediated", Mastra's dormant contributor token unrevoked for 16 months. That is a
better and less fashionable argument than "supply chain is hard."

**The counter-argument to hold honestly** (from the MCP note): every high-impact agentic incident so far ran
through *legitimate first-party servers*. Perfect supply-chain hygiene would have prevented none of them.
The defensible thesis is **we frame it as supply chain because that is the part we can actually govern this
quarter** — tractability, not incident share.

**Regulatory hook, fresh:** the **2026 Minimum Elements for an SBOM** (29 Jul 2026, CISA/NSA/FBI-led,
**co-sealed by ASD's ACSC**) adds required **author signatures and component hashes** — attestation and
integrity — and renames "Supplier Name" to "Component Producer" because the old term *"proved ambiguous in
practice"*. Nothing in it is AI-specific.

## Pieces

- 2026-06-26 — A Free GitHub Account Is All It Takes to Own Your Supply Chain *(draft, never published)*

## Open questions

- ~~Is this a standalone thread or a recurring mechanism inside AI Attack Surface?~~ Answered 2026-08-07: standalone. The AI-native cases (MCP, poisoned frameworks) are *instances* of inherited trust, not a separate phenomenon.
- Is the real argument **incomplete remediation** rather than supply chain? Three of four signals turn on a fix that didn't hold.

## Signals

Linked signal notes appear in **Backlinks** below. Promote the load-bearing ones into *State of play* on the Sunday pass.
- [[Dynamic context runs before the defenses do]] — a malicious skill's dynamic context executes BEFORE model-level injection defenses can intervene, so the refusal never gets a turn. Marketplace poisoning is exploited (ClawHavoc, Jan-Feb 2026, real victims); repo-resident is PoC only. Keep those two facts separate.
