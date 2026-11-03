---
date_first_seen: 2026-08-12
date_updated: 2026-08-12
source: Tenet Security (DEF CON 34) / SecurityWeek / Cloud Security Alliance
url: https://tenetsecurity.ai/blog/ghostjacking-attacks-agentic-kill-chain/
brief: cyber
threads: [AI Attack Surface, Trust Boundaries, Machine Identity]
beat: AI / Agentic / Prompt injection
status: developing
used_in:
---

# Ghostjacking — the reviewer never sees that manipulation happened

**What happened.** Tenet Security (Barak Sternberg, Nevo Poran, Ron Bobrov) presented
three injection chains against AI agents at **DEF CON 34, week of 6–9 Aug 2026**.
Companion work "Agentjacking" (Sentry-only) published 17 Jun 2026.

**Commercial interest:** Tenet is an Israeli startup out of stealth **June 2026** that
**sells agent security**. Name it in any use.

## The three chains — and only one of them is a log

The brief's "Cloudflare/Datadog/Sentry logs" is wrong three ways over.

| Vector | What is actually injected |
|---|---|
| **Cloudflare** | A **blocked WAF request**, recorded verbatim in firewall event logs. The agent reads it, rewrites the company's DNS to point at the attacker, and **reports the issue as resolved.** |
| **Datadog** | A **fake "urgent diagnostic" alert**, planted using a public front-end client token. Not a log the app wrote. |
| **Sentry** | A **fake error event** via public DSN, whose "Resolution" text a *second* agent adopts as its own fix. Agent-to-agent. |

Splunk and Kubernetes are named as plausible patterns only — **not demonstrated**.

## The line worth quoting — better than the success rate

> "It is Cloudflare's managed security rule that blocks the request, and that block is
> what carries the attack in. Following the best practice does not help."

> "It worked 9 times out of 10 against Claude Code. Every request had already been
> blocked. The domain was taken over anyway."

> "A Datadog key meant only for a website's front end is routinely left public. We
> found more than 2,700 of them just by looking."

## The caveats that must travel with it

- **The 9/10 belongs to the Cloudflare DNS-takeover scenario alone** — not to Datadog,
  not to Sentry, not to "the attack" generally.
- **Sample size undisclosed.** Tenet uses "9 out of 10" and "90% success rate"
  interchangeably, which reads as a rate. **Never write "in 10 trials."**
- **Permission mode is unstated.** The words *permission, auto-approve, bypass,
  allowlist, human-in-the-loop, default settings* appear nowhere on the page. Tenet's
  own mitigation list includes *"Require a human to approve any command the agent wants
  to run"* — which suggests the tested setup did not. **Anyone asserting "default
  configuration Claude Code" is going beyond the source.**
- **Unstated precondition:** the agent already held DNS-write credentials on the
  Cloudflare account. Presented as ambient; it is a configuration choice.
- **No in-the-wild exploitation. None.** CSA: *"reflects Tenet Security's
  proof-of-concept research and controlled testing rather than confirmed active
  exploitation at scale."*
- **The exposure figures measure reachability found by scanning, not victims** —
  2,700+ public Datadog keys, 2,388 orgs with injectable DSNs. Aggregators (rankiteo,
  techjournal, cryptika, gbhackers, cryptobriefing) blur this. Unusable.

**Date trap.** Tenet's blog says Sunday 9 Aug Main Track 1; the **official DEF CON
schedule** lists the same three speakers on **Friday, Main Track 2**, under a different
title — *"Your WAF Blocked Us, That Was The Exploit"* — and "GhostJacking" appears
nowhere on the DEF CON page. SC Media says "Sunday August 11," neither a Sunday nor
during the conference. **Write "presented at DEF CON 34 the week of 6–9 August 2026."
Assert no day, no track.**

**Do not conflate** with SecurityWeek's "Anthropic Silently Patches Claude Code Sandbox
Bypass" (Aonan Guan, SOCKS5 null-byte, timeline disputed) or the July Cowork VM-escape
stories. Different incidents. Anthropic is the **only** confirmed responder to Tenet —
a Claude Desktop sandbox escape *"confirmed by their security team, and patched before
this talk,"* no CVE. **Cloudflare, Datadog and Sentry have said nothing publicly.**
Tenet's own hedge: *"Everything was reported, and where fixable, fixed."* Log-reading
injection is arguably not patchable by a log vendor at all.

## Why it matters — the argument, not the attack

This is the counter to the strip-out defence in auto mode, and it is the sharpest
formulation available:

> **Stripping tool results out of the reviewer's context removes the manipulation from
> view. It also removes the evidence that manipulation happened. The classifier can
> adjudicate the action. It cannot adjudicate where the intent came from.**

The strip-out protects the *reviewer*. It does nothing for the *agent*. Poison what the
agent reads and it emits a tool call that, from the classifier's deliberately narrowed
view, looks like a reasonable next step in the task the user actually asked for.

**And this supports the deny-rule thesis rather than denting it.** The DNS write the
attack needs is on auto mode's **zero-configuration block list** ("secret managers or
DNS or TLS"). **Honest limit:** the defensible sentence is *the action the attack
required is one auto mode blocks with no configuration* — **not** *auto mode would have
stopped it*. Tenet does not say what mode they ran, and their testing predates the
14 Aug default.

## Feeds

- [[Auto mode becomes the default - the approver is now a model]] — direct collision; see Fri 14 Aug
- [[AI Attack Surface]] — the agent's input surface, not the model
- [[Trust Boundaries]] — a boundary that filters content but not provenance
- [[Capability restated as certainty]] — PoC-to-fact drift in the secondaries

## Open

- **The provenance of intent is a piece.** Every control in the stack adjudicates
  actions; none adjudicates why an action was proposed. Sits directly against the
  orphaned *"the model isn't the product, the harness is"* — week of 17 Aug.
