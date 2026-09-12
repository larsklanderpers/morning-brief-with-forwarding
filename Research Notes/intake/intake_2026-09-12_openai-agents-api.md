---
type: intake
date: 2026-09-12
source_url: https://www.youtube.com/watch?v=Sir59K8ZDPU (the only URL posted; the video is NOT about the Agents API, see below). Primary for the note's subject: https://openai.com/index/introducing-the-agents-api/
slack_permalink: https://lars-klander-personal.slack.com/archives/C0BVCSV0PJ5/p1789187915824589
slack_ts: "1789187915.824589"
slack_ts_note: "1789187930.996739"
lars_note: "let's put a research agent on the new Open AI Agents API and see what we figure out"
reactions: [mag]  # his words ("put a research agent on"), not an emoji reaction; no emoji on either message when processed
verdict: feeds a thread - Trust Boundaries (Machine Identity secondary); optional one-paragraph stage-2 beat for Sat 19 "The Control Plane I Built", his call at the extraction session
filed_to: References/research_openai-agents-api_2026-09-12.md; Vault/Writing/Signals/Managed agent harnesses - the vendor keeps the session.md (new); Trust Boundaries and Machine Identity hub lines returned to the parent tick to apply
---

# OpenAI Agents API (public beta, 10 Sep 2026), with the posted video "Why Agentic Systems Need Ontologies" (Frank Coyle, UC Berkeley)

Two Slack messages, 15 seconds apart, treated as one item: a YouTube link at 21:38:35 PDT on 11 Sep and
the note at 21:38:50. Arrived while intake was down; processed 12 Sep.

**The link and the note are about different things.** The video is a July conference talk on ontologies
as validators around agent loops; its demo uses a Claude tool-use loop and it never mentions OpenAI's
Agents API (which launched seven weeks after the talk was posted). The note is the instruction, so the
research went to the Agents API. The video is filed below as a related backgrounder, because its
argument lands on the same trust-boundary question the research surfaced.

## Extracted

### A. The video (the URL he posted)

- **Title:** Why Agentic Systems Need Ontologies: Frank Coyle, UC Berkeley
- **Channel:** AI Engineer (@aiDotEngineer), 636K subscribers
- **Published:** 22 Jul 2026, 21:18 long, 381,373 views and about 10K likes at fetch
- **Transcript: NOT reachable.** Firecrawl on the watch URL returned the description, chapter list and
  metadata but no transcript text (the page shows "Show transcript" as an unexpanded control). The
  description links an organiser page (`ai.engineer/talks/Sir59K8ZDPU-ontologies-for-agentic-systems`),
  which returned a **chaptered summary with timestamps, written by the organiser, not a verbatim
  transcript.** Everything below comes from the description and that summary. Nothing here is a claim
  about what Coyle said word for word.
- **Chapters:** intro (0:00); two lineages, agents and ontologies (2:21); neurosymbolic AI, guardrails
  around a probabilistic model (4:04); what an ontology is (5:23); building one, the expert-systems era
  (6:14); reusing taxonomies (7:55); RDFS and OWL, inference and constraints (9:12); agents, loops and
  how they break (12:12); a Claude tool-use loop with an ontology validator (14:22); Pydantic at the
  door, ontology at the ledger (17:47); errors an ontology catches that English cannot (18:52).
- **Argument (from the description and summary):** most agent failures (a second refund on the same
  order, a payout sent to the support desk instead of the buyer, an invented order status) are
  symptoms of a missing layer: a formal domain model sitting outside the model. Probabilistic
  reasoning inside, logic outside. Pydantic checks the shape of a proposed tool call; the ontology
  checks whether the result makes sense in the business (functional properties, disjoint classes,
  constrained values). The model proposes, application code executes, and a validator checks the
  result **before it is accepted**; inconsistent results go back to the model or to a human. Delay
  side effects until validation passes. Loops still drift, run on and burn tokens, so iteration needs
  explicit control.
- The talk's own demo is built on Anthropic's tool-use loop. It is a practitioner talk at a
  conference that sells sponsorships; no product is pitched in the summary.

### B. The Agents API (the subject of his note), from OpenAI's own pages, all fetched 12 Sep

- **Launch:** openai.com, "Introducing the Agents API", dated **September 10, 2026**. Public beta,
  "available... today to all developers". Tagline: build and run cloud agents with the Codex harness,
  fully managed by OpenAI. API changelog entry the same day.
- **What it is:** OpenAI runs the Codex harness as a service. "OpenAI manages sessions, orchestration,
  context compaction, and recovery while your application provides tools and chooses its execution
  environment." Four concepts: agent, environment, session ("a durable instance of an agent"), events
  and items. Beta header `OpenAI-Beta: agents=v1`.
- **Environment choice:** OpenAI-hosted sandbox, self-hosted (you run `codex exec-server`, which
  connects outbound to OpenAI), a sandbox partner (Blaxel, Cloudflare, Daytona, DigitalOcean, E2B,
  Modal, Oracle, Runloop, Vercel), or no environment at all.
- **Harness features named:** automatic compaction, tool search, programmatic parallel tool calling,
  MCP, custom functions, built-in web search, skills and plugins, multi-agent with subagents.
- **Pricing:** "There are no additional fees for using the Agents API": model tokens at the model's
  rates, OpenAI tools at standard rates, OpenAI-hosted sandboxes at standard container rates.
- **Data terms (overview page, verbatim):** "The Agents API currently supports data residency only in
  the United States and does not support Zero Data Retention (ZDR). Choosing a self-hosted sandbox does
  not make the Agents API ZDR-eligible." Data-controls table: `/v1/agents` application state retained
  **until deleted**, abuse-monitoring retention 30 days, not ZDR-eligible, not Eyes Off eligible, not
  used for training.
- **Security page (verbatim):** "Agent-generated code can access the files, credentials, and network
  available to its environment."
- **Subagents:** share the coordinator's filesystem ("Creating a subagent does not create another
  environment") and inherit its MCP tools and credentials.
- **Observability:** "Trace retrieval and external trace exporters are not part of the public beta
  API." Usage fields are best-effort, can be null, may change, and "are not a final bill".
- **Customer claims on the launch page (OpenAI-selected testimonials, unverified):** SafetyKit -60% cost
  per case; Hypha -86% failed agent responses from separating harness and sandbox; Ciridae eval score
  0.71 to 0.85 and 4x lower subagent latency; Nash running "thousands of long-running AI agents".
- **Context:** OpenAI's Assistants API was sunset on **26 Aug 2026**; the official replacement is the
  Responses and Conversations APIs, not the Agents API.

Full analysis, economics and the Anthropic and Google comparison:
`References/research_openai-agents-api_2026-09-12.md`.

## Lars's note

"let's put a research agent on the new Open AI Agents API and see what we figure out"

## Match

- **Week of 14 Sep:** nothing in the plan is about managed agent harnesses. **Sat 19, "The Control Plane
  I Built"** (part two of the published Sat 12 *Nine Bots and One Computer*) is the nearest, and it
  could use one optional stage-2 paragraph: the Agents API is the rent-the-harness version of the build.
  Two facts make it worth a sentence: its subagents share one filesystem and inherit credentials, which is
  the same one-computer design Sat 12 flagged in Grok Bot; and its usage fields cannot reconstruct the
  bill, where his own runner logs `cost_usd` per job. Not the spine, and the Sat 19 block already warns
  against infrastructure framing, so it is his call at the extraction session.
- **Thu 17, "Misalignment Is Not an Incident":** incidental find. OpenAI's 3 Sep API changelog ships a
  feature literally named "Misalignment monitoring", which "can trigger safety alerts or stop a
  conversation for review". So the label now has a product surface. Worth re-reading at primary in the
  Thu 17 re-verify pass. Whether it runs inside Agents API sessions is unverified.
- **Thread:** Trust Boundaries is the confident match. The finding is who holds the session record, and
  it sits between the existing Signals [[You cannot rent an audit trail]] and [[A black box recorder for
  agent actions]]. Machine Identity is secondary: there is no per-agent identity, subagents inherit
  credentials, and deleting a vault credential neither revokes the token nor stops a running session.
- **Killed claims:** none repeated. The Agents API's "self-hosted does not make it ZDR-eligible" line is
  **consistent with** the 17 Aug kill `self-hosted-sandboxes-carve-out` (Anthropic Managed Agents). The
  carve-out is wrong for both vendors.
- **Published or scheduled:** nothing contradicted.

## Provenance note

Nothing in any fetched page (the YouTube page, the ai.engineer talk page, OpenAI's launch post and nine
docs pages, the pricing, model, data-controls and changelog pages, Anthropic's and Google's pages, the
Hacker News thread) contained instructions addressed to me or to an agent. The Hacker News extraction
flagged four comments as addressed to an AI; on inspection they are ordinary questions between
commenters. Treated as data throughout. The YouTube transcript was not retrievable; no claim is made about
what the video says beyond the description and the organiser's summary.
