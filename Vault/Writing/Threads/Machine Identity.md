---
type: thread
status: active
last_reviewed: 2026-07-20
---

# Machine Identity

Agents and services as identities that authenticate, hold privilege, and outlive their purpose. The governance problem hiding inside the convenience.

## State of play

*Where this argument currently stands. Update when a piece ships or a signal changes the picture.*

## Pieces

- 2026-07-23 — Your AML Desk Already Knows How to Govern a Machine *(scheduled; · Clubs / AML)*
- 2026-07-08 — The Contractor Who Finished the Job and Kept the Keys

## Open questions

- Does existing KYC/AML machinery genuinely transfer to machine identity, or is that an appealing analogy that breaks under load?

## Signals

Linked signal notes appear in **Backlinks** below. Promote the load-bearing ones into *State of play* on the Sunday pass.
- [[Managed agent harnesses - the vendor keeps the session]] - 2026-09-12: no per-agent identity in OpenAI's Agents API docs. Delegated work is attributed only by a `subagent_id` on the turn record, subagents inherit the coordinator's MCP credentials, the agent can read its own executor key, and deleting a vault credential neither revokes the token nor stops a running session.
