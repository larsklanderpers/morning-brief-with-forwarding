---
date_first_seen: 2026-09-12
date_updated: 2026-09-12
source: OpenAI, "Introducing the Agents API" (10 Sep 2026) and the Agents API docs; Anthropic, Claude Managed Agents (8 Apr 2026) and overview docs. Flagged by Lars in #heinlein-inbox, 11 Sep.
url: https://openai.com/index/introducing-the-agents-api/ (research: References/research_openai-agents-api_2026-09-12.md · intake: Research Notes/intake/intake_2026-09-12_openai-agents-api.md)
brief: ai
threads: [Trust Boundaries, Machine Identity]
beat: AI / Agent infrastructure / Audit
status: signal
used_in:
---

# Managed agent harnesses: the vendor keeps the session

**What happened.** On 10 Sep 2026 OpenAI put the Codex harness behind a public-beta **Agents API**. OpenAI
runs the agent loop, stores the session, compacts context and recovers failures; the customer picks where
commands execute (OpenAI's sandbox, their own machine, one of nine partners, or none). There is no harness
fee, just tokens plus container time. Anthropic shipped the same shape as **Claude Managed Agents** on
8 Apr. The managed harness is now a product category.

**Why it matters.** In both products **the session record lives with the vendor, outside Zero Data
Retention, and self-hosting the sandbox changes neither.** OpenAI, verbatim: "does not support Zero Data
Retention (ZDR). Choosing a self-hosted sandbox does not make the Agents API ZDR-eligible." Residency is
US-only. Application state is kept "Until deleted". And the part of the record the customer can pull is
thinner than the part the vendor keeps: "Trace retrieval and external trace exporters are not part of the
public beta API." Usage counts "are not a final bill".

This is the successor fact to [[You cannot rent an audit trail]]. You still cannot rent the record, but
you can now rent the loop, and renting the loop hands the record to the landlord. It also sharpens
[[A black box recorder for agent actions]]: the history is written by the harness operator, not by the
agent and not by you.

Two design facts make it this thread's and not just a launch:
- **Subagents share one filesystem and inherit the coordinator's MCP credentials.** "Creating a subagent
  does not create another environment." That is Grok Bot's one shared computer (Sat 12, *Nine Bots and
  One Computer*) in an enterprise API.
- **Containment is the customer's job, in the vendor's own words:** "Agent-generated code can access the
  files, credentials, and network available to its environment." Outbound network is on by default, and
  hosted stdio MCP servers require it. The agent can read the executor key. Deleting a vault credential
  "does not revoke the original tokens with their providers or stop a running session."

**Economics.** The runtime meter has converged at about eight to nine cents an hour across all three
vendors at the smallest size (OpenAI 1 GB sandbox $0.09/hr, Anthropic $0.08/session-hour, Google $0.085/
vCPU-hour). The tokens are the bill; the record is what you give up.

**Do not print:** that self-hosting is a ZDR carve-out, for either vendor (killed 17 Aug for Anthropic,
contradicted at primary for OpenAI 12 Sep); the OpenAI launch-page customer numbers as findings (they are
selected testimonials); any link between this harness and the July Hugging Face incident (no primary).

## Observations

- **2026-09-12** First seen via the 12 Sep AI brief and Lars's inbox note. Primaries read in full the same
  day; see the research note.

## Feeds

- [[Trust Boundaries]]: who holds the session record when the loop is rented
- [[Machine Identity]]: no per-agent identity; subagents inherit credentials; revocation is not deletion
- Related: [[You cannot rent an audit trail]], [[A black box recorder for agent actions]]
