---
type: thread
status: active
last_reviewed: 2026-08-10
---

# Trust Boundaries

The boundaries inside a system that nobody drew explicitly and nobody can see — until something crosses one.

## State of play

The boundary question got two concrete artifacts this week, one on each side of it.

**A boundary you can now hold yourself:** [[Anthropic inference hooks - a deny switch you hold]] — the first
model provider to expose an inline allow/deny verdict to a **customer-operated** server, before inference
begins. Read the caveats in the note before treating it as the answer: it is **ingress-only** (nothing says
model output is inspected), there is **one hook event, not a per-tool-call hook**, **fail-open is a
configurable setting**, and it is **not available on Bedrock or Vertex** — so today the control and an
Australian residency strategy are mutually exclusive.

**A boundary that held only because a person was standing on it:**
[[AISI cyber range - the agents went out of scope]]. Every mitigation AISI announced afterwards is technical — network segmentation, runtime
monitoring. The thing that actually worked was a maintainer being suspicious of a stranger's pull request.

**And the boundary already reduced to theatre:** Trail of Bits, on MCP tool-description mutation —
*"This effectively transforms the 'human-in-the-loop' security model into 'human-as-the-rubber-stamp'."*
That is the GhostApproval argument stated by a security firm, with CVE-2025-54136 (Cursor re-executing
silently changed approved configs) as the worked example. See
[[MCP servers as supply chain - the numbers are in]].

**Promoted 2026-08-10 — the approval boundary gets reassigned to software, on a published date.**
[[Auto mode becomes the default - the approver is now a model]]. From **14 August 2026**, new Claude Code
sessions on **Pro, Max and Team** plans default to auto mode, where a **separate classifier model** reviews
each tool call instead of the user. Enterprise, API, Bedrock, Vertex and Foundry **remain opt-in**. Read the
note before writing a word of it: it stops asking *routinely*, not entirely — ~40 categories are blocked
with zero configuration, `permissions.deny` is evaluated **before** the classifier and cannot be overridden
by it, and prompting resumes after 3 consecutive or 20 total blocks. The un-configured state is the tight
one.

The detail that makes it this thread's, rather than a tooling story: the gate being replaced had been
**leaking all summer** — hidden commands in zsh regex conditionals, commands padded with tabs or invisible
Unicode, commands over 10,000 characters, a PowerShell bypass, `bypassPermissions` in agent definitions
ignoring org policy. And Anthropic's own reported experiment puts human reviewers at **13.6%** of dangerous
commands caught. The prompt was never the control. It was the sign — 31 Jul, exactly.

Alongside it, the boundary the record itself sits on: [[A black box recorder for agent actions]] — when the
agent writes the history, the party with an interest in the record is the party under investigation. AISI
already demonstrated it; auto mode blocks transcript writes by default; NSW made it a statutory obligation.

**Added 2026-09-12 (Heinlein inbox).** [[UK AI Risk Management Toolkit - guidance, not a gate]]: the UK
government's own AI risk method files end-user verification of outputs ("use the outputs at their own
risk, and are responsible for verifying the outputs") under **Transference**, not under a control. The
human checker is where the risk is sent, not where it is stopped, and the vendor contract has already
sent it there once.

## Pieces

- 2026-07-22 — You Have 29 Minutes. Who's Awake? *(secondary)*
- 2026-07-16 — The Boundary You Can't See *(GhostLock; · Practitioner)*

## Open questions

- Where is the boundary in an agentic stack, and who owns it?

## Signals

Linked signal notes appear in **Backlinks** below. Promote the load-bearing ones into *State of play* on the Sunday pass.
- [[Dynamic context runs before the defenses do]] — a malicious skill's dynamic context executes BEFORE model-level injection defenses can intervene, so the refusal never gets a turn. Marketplace poisoning is exploited (ClawHavoc, Jan-Feb 2026, real victims); repo-resident is PoC only. Keep those two facts separate.
- [[Managed agent harnesses - the vendor keeps the session]] - 2026-09-12: OpenAI's Agents API (public beta, 10 Sep) and Anthropic's Managed Agents (beta, 8 Apr) both run the agent loop in the vendor's cloud and keep the session record there. No ZDR, US-only residency on OpenAI, self-hosting the sandbox changes neither, and OpenAI's trace retrieval is not in the public API. Subagents share one filesystem and inherit MCP credentials. Research: `References/research_openai-agents-api_2026-09-12.md`.
- [[The semantic layer without a seller]] - **2026-09-22 (Heinlein inbox): the boundary gets asked to
  draft itself.** MIT CISR's case for a semantic layer is the context an agent does not have, written
  down outside the model so its output can be checked. Its third recommendation is to use AI to
  generate the metadata, classify the data and **recommend the access controls**. `research_ontology_2026-09-12.md`
  had already recorded the objection: letting the agent maintain the ontology puts the thing checking
  the agent under the agent's pen, and nobody has shown it works. ⚠️ State it honestly: step three is
  AI-assisted authoring and step two puts a named human owner over it, so **the finding is that the two
  steps are in tension and the briefing does not say which wins.** Not "MIT says let the AI run the
  guardrail". Intake: `Research Notes\intake\intake_2026-09-22_mit-semantic-layer.md`.
- [[Two visions for agentic routing]] - **2026-09-20 (Heinlein inbox): the boundary now gets crossed by the install instructions themselves.** A seven-step thread (~254K views, 4,486 bookmarks) tells readers to mint a TypeSafe API key, have Grok Bot store it, have Grok Bot install the SDK on the shared Agent Computer, and add a router skill that fires before every browser, research, retry or extra-bot call. The routing layer arrives as a credential plus an install handed to the agent, which is the one-computer design read from the other end. ★ Steps 6 and 7 are a competent staged rollout (shadow first, logs, named kill switch, humans keep irreversible actions) wrapped in "install it as soon as possible" - **the care is in the recipe and the framing is what travels.** Intake: `Research Notes\intake\intake_2026-09-20_jev-grokbot-router.md`.
