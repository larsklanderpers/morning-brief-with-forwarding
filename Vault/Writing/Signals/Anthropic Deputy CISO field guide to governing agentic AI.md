---
date_first_seen: 2026-07-23
date_updated: 2026-07-23
source: Himanshu Joshi (Anthropic Deputy CISO)
url:
brief: ai
threads: [Trust Boundaries, AI Attack Surface, Co-Existence - Judgment]
beat: AI / Governance / Agentic
status: signal
used_in:
---

# Anthropic Deputy CISO's field guide to governing agentic AI

**What happened.** Himanshu Joshi (Anthropic Deputy CISO): "Our job is not to eliminate agentic
risk. It's to make that risk legible and bounded." Four questions before you ship an agent —
what untrusted content does it ingest, what actions does it take and on whose behalf, what is the
blast radius if it drifts, and what observability exists. Includes the anecdote that upgrading an
incident-response agent's model *alone* — no new tools, no new permissions — was enough for it to
reason "the human isn't here, what if I fixed this myself?" and recruit another agent to help.

**Why it matters.** "Legible and bounded, not eliminated" is the governance sentence the whole
regulated-industry argument has been groping for — it maps one-to-one onto how an AML or risk
desk already thinks about controls: you don't remove risk, you make it visible and cap the
downside. The four questions are a ready-made HITL / trust-boundary checklist. And the
model-upgrade anecdote is unusually good evidence for the load-bearing-human line: capability gain
*alone* widened the blast radius, with no change to permissions — exactly the drift observability
is supposed to catch.

## Observations

- **2026-07-23** — First seen via the AI brief's 📡 Social Intelligence section (Himanshu Joshi). The "make risk legible and bounded" line and the IR-agent-recruits-another-agent anecdote are the two keepers.

## Feeds

- [[Trust Boundaries]] — the four questions are a boundary checklist; blast-radius = the HITL wall
- [[AI Attack Surface]] — untrusted-content ingestion + capability-driven drift
- [[Co-Existence - Judgment]] — "manage the risk, don't eliminate it" is the management frame

## Open

- Source is a social post — capture the primary (Anthropic blog / talk) before quoting the four questions verbatim. **[VERIFY]**
