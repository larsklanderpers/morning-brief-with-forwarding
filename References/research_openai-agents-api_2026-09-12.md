# Research Note: OpenAI Agents API (public beta, 10 Sep 2026)
For: no draft yet. Trust Boundaries thread; optional stage-2 beat for Sat 19 "The Control Plane I Built" · Depth: deep · Date: 2026-09-12

Commissioned by Lars in #heinlein-inbox, 11 Sep 21:38 PDT: *"let's put a research agent on the new Open AI
Agents API and see what we figure out."* Intake note: `Research Notes/intake/intake_2026-09-12_openai-agents-api.md`.

**Scope, five sub-questions.**
1. What exactly launched, when, and how it relates to the Responses API, the Agents SDK and the Assistants sunset.
2. What it costs, and whether a buyer can reconcile the bill.
3. Data handling: retention, ZDR, residency, and what self-hosting does and does not change.
4. Security surface: sandbox, credentials, MCP, subagents, identity, observability, prompt injection.
5. How it compares with Claude Managed Agents and Google's agent platform, primaries only.

**Local corpus first.** `AI Briefs/ai_brief_2026-09-12.md` carries it (Shipping with AI, sourced to Ken Huang's
Substack), and its summary checks out at primary on date, sandbox partners and "no separate fee". Nothing
else in the last 14 days of AI or Daily Briefs, and nothing in `References/`, on the Agents API. The corpus
does hold the Anthropic side: `week-plan_2026-08-17.md` verified Managed Agents' ZDR and self-hosting terms
at primary on 13 Aug, and killed the "self-hosted sandboxes remain the carve-out" claim (17 Aug). The
published Sat 12 piece *Nine Bots and One Computer* is the closest prior writing.

---

## Bottom line

OpenAI shipped the Agents API in public beta on 10 Sep 2026. It is the Codex harness run by OpenAI as a
service: OpenAI runs the loop, stores the session, compacts context and recovers failures, and you pick
where commands execute (OpenAI's sandbox, your own machine, one of nine partners, or none). There is no
harness fee, just tokens plus container time, and at any realistic workload the sandbox meter is about a
cent in the dollar. The model is the bill. **The terms are the story, not the features.** US-only data
residency. Not ZDR-eligible, even with a self-hosted sandbox. Session state held until you delete it.
Trace retrieval not in the public API. Usage fields that are "not a final bill" and cannot reconstruct
one. That is the same shape Anthropic shipped in April with Managed Agents, so the managed harness is now a
category, and in both products **the vendor keeps the session record.** Trust in the facts is high: all
of it comes from OpenAI's own pages, fetched live on 12 Sep. The customer performance numbers are
OpenAI-selected testimonials and unverified.

---

## What's solid

**What launched**
- **Launched 10 Sep 2026, public beta, all developers.** OpenAI launch post, dated September 10, 2026:
  "Agents API is available in public beta today to all developers." Also in the API changelog.
  [openai.com/index/introducing-the-agents-api](https://openai.com/index/introducing-the-agents-api/) ·
  [changelog](https://developers.openai.com/api/docs/changelog)
- **It is the Codex harness, hosted.** "The Agents API gives your application access to the Codex harness
  through an OpenAI-managed API. OpenAI manages sessions, orchestration, context compaction, and recovery
  while your application provides tools and chooses its execution environment."
  [Agents API overview](https://developers.openai.com/api/docs/guides/agents-api/overview)
- **Four concepts:** agent (model, instructions, tools, MCP servers), environment (optional sandbox),
  session ("a durable instance of an agent that works on tasks and responds to input"), events and items.
  Requests carry `OpenAI-Beta: agents=v1`. [overview]
- **Four environment options.** `openai_hosted` (OpenAI provisions a Linux sandbox), `self_hosted` (you
  run `codex exec-server`, which "registers with the API using an environment ID and a restricted API key"
  and connects outbound over WebSocket; "All connections are outbound"), nine named sandbox partners, or
  `none`. [architecture](https://developers.openai.com/api/docs/guides/agents-api/architecture) ·
  [self-hosted](https://developers.openai.com/api/docs/guides/agents-api/environments/self-hosted)
- **Harness features named at launch:** automatic compaction, tool search ("loads relevant tool
  definitions as needed"), programmatic parallel tool calling, MCP, custom functions, built-in web search,
  skills and plugins, vaults, multi-agent. [launch post]
- **Where it sits against its siblings.** OpenAI's own comparison table: Agents API = "OpenAI runs a
  managed Codex harness", state is "Saved session configuration, turns, and items", integration effort
  Low. Agents SDK = "The SDK runs inside your application", state in "Your storage and SDK sessions",
  effort Medium. Responses API = your application, effort High. **What is new against the Responses API is
  that OpenAI runs the loop and holds the state; what is new against the Agents SDK is that the loop leaves
  your process.** [Agents overview](https://developers.openai.com/api/docs/guides/agents)
- **The Assistants API is gone, and the Agents API is not its official replacement.** "The Assistants API
  was officially sunset on August 26, 2026, and is no longer available." The deprecations page names the
  replacement as "Responses API and Conversations API". Notice was given 26 Aug 2025.
  [Assistants migration](https://developers.openai.com/api/docs/assistants/migration) ·
  [deprecations](https://developers.openai.com/api/docs/deprecations)
- **Sandbox partners, named:** Blaxel, Cloudflare, Daytona, DigitalOcean, E2B, Modal, Oracle, Runloop,
  Vercel. [launch post; self-hosted page]

**Data handling**
- **US-only residency, no ZDR, and self-hosting does not change it.** Verbatim: "The Agents API currently
  supports data residency only in the United States and does not support Zero Data Retention (ZDR).
  Choosing a self-hosted sandbox does not make the Agents API ZDR-eligible." [overview]
- **Retention by endpoint.** Data-controls table, row `/v1/agents`: data used for training **No**;
  abuse-monitoring retention **30 days**; application-state retention **Until deleted**; ZDR-eligible
  **No**; Eyes Off and Safety Retention eligible **No**.
  [Data controls](https://developers.openai.com/api/docs/guides/your-data)
- **You delete it, or it stays.** "The Agents API retains session state so you can continue work across
  turns... You can delete sessions and published artifacts when you no longer need them." Files under
  `/workspace/outputs` become "immutable artifacts" that "remain downloadable after the sandbox expires".
  [overview] · [OpenAI-hosted sandboxes](https://developers.openai.com/api/docs/guides/agents-api/environments/openai-hosted)
- **Hosted sandbox lifetime.** An idle sandbox "can be deleted" after an hour without activity or
  keep-alives, and "This timeout isn't configurable." "Closing an event stream does not cancel the task."
  [OpenAI-hosted sandboxes]

**Security surface**
- **The environment is the blast radius, and OpenAI says so.** "Agent-generated code can access the
  files, credentials, and network available to its environment." Advice: isolate workloads in VMs,
  separate environments per user or workload, a dedicated OpenAI project per workload.
  [Sandbox security](https://developers.openai.com/api/docs/guides/agents-api/environments/security)
- **The executor key is readable by the agent.** "Agent-generated code can read the executor key, but the
  key only permits connecting environments. It cannot authorize any other API action." Keep the
  application key outside. [self-hosted; security]
- **Credential brokering is the customer's job.** "Keep third-party credentials outside the environment.
  Where possible, route requests through a credential broker." And "Injecting a stored secret into the
  environment still exposes it to agent-generated code." [security]
- **Vaults keep secrets from the agent, but only on OpenAI's side of the wire.** A vault lets the agent
  "use authenticated tools without receiving the secret values"; credentials bind to an MCP server URL.
  But "Vaults apply only to connections from OpenAI"; environment-origin HTTP MCP "does not use vault
  credentials"; stdio credentials "can be read by code running in the environment". And: "Deleting stored
  credentials does not revoke the original tokens with their providers or stop a running session."
  [Vaults](https://developers.openai.com/api/docs/guides/agents-api/tools/vaults) ·
  [MCP connections](https://developers.openai.com/api/docs/guides/agents-api/tools/mcp)
- **Network is open by default.** Hosted sandbox `network.access` default is `enabled` ("Allow outbound
  access. This is the default unless you inherit a template policy"). `restricted` takes 1 to 100 exact
  hostnames. **Hosted stdio MCP servers require `enabled`**, so using a stdio MCP means giving up the
  allowlist. [OpenAI-hosted sandboxes; MCP connections]
- **Remote MCP calls leave from OpenAI, not from you.** `connection_origin: "service"` is the default:
  OpenAI's service connects to the MCP server, so the server must be reachable from OpenAI. [MCP connections]
- **Subagents share one filesystem and inherit credentials.** "The coordinator and subagents share its
  filesystem. Creating a subagent does not create another environment." "Subagents inherit configured MCP
  tools, their credentials and allowed tools, and web search settings." Default `max_concurrent_subagents`
  is 6, excluding the coordinator. **This is the Grok Bot one-computer design from Sat 12, in OpenAI's
  enterprise API.** [Multi-agent](https://developers.openai.com/api/docs/guides/agents-api/multi-agent)
- **Identity is the project key, not the agent.** The application key needs `api.agents.read`,
  `api.agents.write` and `api.responses.write`. The executor key "must belong to the same organization,
  project, and user or service account that owns the session." In the pages read, work done by a delegated
  agent is attributed only by a `subagent_id` on the turn record ("A `null` subagent ID identifies
  root-agent work"). [security; self-hosted; observability]
- **The record you can pull is thinner than the record they keep.** "Trace retrieval and external trace
  exporters are not part of the public beta API." "Detailed trace retrieval is not available through an
  ordinary project API key. Dashboard trace endpoints require separate access and are not a supported
  customer API." "Command-output truncation is not reported."
  [Observability and usage](https://developers.openai.com/api/docs/guides/agents-api/observability)

**The comparators (primaries only)**
- **Anthropic, Claude Managed Agents.** Public beta, launched **8 Apr 2026**, "an Anthropic-managed harness
  with production infrastructure for state, memory, permissions, and scheduled execution." Priced at
  "Standard Claude Platform token rates... plus $0.08 per session-hour for active runtime." Environments:
  "an Anthropic-managed cloud sandbox, or a self-hosted sandbox on your own infrastructure." "Stateful by
  design", so "not currently eligible for Zero Data Retention or HIPAA Business Associate Agreement (BAA)
  coverage." Beta header `managed-agents-2026-04-01`.
  [claude.com/blog/claude-managed-agents](https://claude.com/blog/claude-managed-agents) ·
  [Managed Agents overview](https://platform.claude.com/docs/en/managed-agents/overview). The corpus
  already holds the 13 Aug primary check that the no-ZDR line applies "including Self-hosted sandboxes"
  and that "Tool inputs and outputs still flow to Anthropic's control plane" (`week-plan_2026-08-17.md`).
- **Google, Gemini Enterprise Agent Platform.** "Runtime and Sandbox environments, including Code
  Execution and Computer Use, are billed on Agent Compute (vCPU-hours) and Agent Memory (GiB-hours)."
  Agent Compute is free to 50 hours a month, then **$0.085 per vCPU-hour**; Agent Memory is free to 100
  GiB-hours, then **$0.009 per GiB-hour**.
  [pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing). Google's
  retention and residency terms were not fetched this pass.

---

## What's contested / watch out

- **"No additional fees" is true of the harness and misleading as a comparison.** OpenAI charges no
  harness fee, but its hosted sandbox bills at container rates: **$0.03 per 20 minutes at 1 GB**, which is
  **$0.09 an hour**, against Anthropic's **$0.08 per session-hour**. The runtime meters have converged on
  about eight to nine cents an hour at the smallest size, across all three vendors. Anyone framing this as
  "free harness vs Anthropic's runtime fee" is comparing the label, not the bill. Units differ (container
  size, session-hour, vCPU-hour), so say "about the same at the smallest configuration", not "identical".
- **The customer numbers are OpenAI-selected and unaudited.** SafetyKit ("60% reduction in cost per
  case"), Hypha ("reduced failed agent responses by 86%"), Ciridae ("0.71 to 0.85", "4x latency
  reduction"), Nash ("thousands of long-running AI agents"). All on OpenAI's own launch page. Wire coverage
  (Investing.com, which says its article "was generated with the support of AI", plus MarkTechPost, VKTR,
  Futu/Wallstreetcn, KuCoin) repeats them without independent test. **Name the commercial interest:**
  deepsense.ai had early access and sells AI implementation services; the nine sandbox partners sell the
  compute this API drives; OpenAI's IPO filing is reported as imminent (AI brief 19 Aug, secondary).
- **"Open-source foundation" is true of the code, not the record.** The harness is inspectable at
  `github.com/openai/codex`, but the running service, the session store and the traces are OpenAI's, and
  the traces are not retrievable through the public API. Reading the code does not give you the history.
- **The Assistants precedent is the lock-in lesson, not a claim about intent.** OpenAI's previous stateful
  managed-agent API ran in beta from its November 2023 launch (DevDay; launch date from memory, consistent
  with the Hacker News thread of 6 Nov 2023) until the 26 Aug 2026 sunset, a year's notice. Its objects were
  "retained indefinitely" unless deleted. The Agents API is also beta (`agents=v1`) and also stores state
  until deleted. Fair to say: the last one of these was retired, with a year's notice and a migration that
  practitioners on OpenAI's own forum called "not a 1:1 migration". Not fair to predict the same here.
- **Coverage framing the Agents API as the Assistants successor** is the reporters' framing. OpenAI's
  deprecations page names Responses and Conversations.
- **Subagent limits vary by page.** The launch post example sets `max_concurrent_subagents: 3`, the
  overview example 4, the multi-agent docs give a default of 6. A maximum was not stated in the pages read.
- **Practitioner read, Hacker News item 49649213** (340 points, 178 comments at fetch, 11 to 12 Sep).
  Themes: the ZDR exclusion called out as under-noticed; lock-in to a vendor's own models; some prefer
  running the SDK in their own sandbox; the self-hosted executor seen as the answer for keeping tool
  execution local, with the control plane still in OpenAI's cloud. **The comment text came through an
  automated extraction pass; paraphrase only, and re-read the thread before quoting anyone.**

## Couldn't verify

- **Whether the Agents API runs non-OpenAI models.** Every example uses `gpt-6-astra`. The tool-search page
  refers to "supported models and providers". No explicit statement either way was found.
- **Whether OpenAI's 3 Sep "Misalignment monitoring" applies inside Agents API sessions.** The changelog
  scopes it to "supported Responses API requests". Not established.
- **A prompt-injection section in the Agents API docs.** None appeared in the nine Agents API pages read
  (overview, architecture, OpenAI-hosted, self-hosted, sandbox security, MCP, vaults, multi-agent,
  observability). **This is a narrow absence, not a finding:** the Agents SDK guardrails page and the
  general safety pages were not read. Do not print "OpenAI's docs don't mention prompt injection."
- **The Codex repo's licence** was not re-checked this pass.
- **Google's retention, residency and ZDR terms** for its agent platform were not fetched.
- **Any link between this harness and the agents in OpenAI's July Hugging Face incident.** No primary
  connects them. Do not connect them in print.

---

## The economics

**The meter that matters is the model.** GPT-6 Astra lists at **$10 input, $1 cached input, $12.50 cache
writes, $50 output** per million tokens. Requests over **272K input tokens** are priced at **2x input and
cache, 1.5x output for the full request.** Batch and Flex are half price; fast mode is double.
[GPT-6 Astra model page](https://developers.openai.com/api/docs/models/gpt-6-astra)

**The hosted sandbox is small change.** Container rates: 1 GB $0.03, 4 GB $0.12, 16 GB $0.48, 64 GB $1.92
per 20-minute session per container, "billed by the minute, with a 5-minute minimum per session." Per hour
that is $0.09, $0.36, $1.44, $5.76. [pricing](https://developers.openai.com/api/docs/pricing)

**Illustrative, not measured** (assumptions stated; this is arithmetic on list prices). One agent turn
roughly the size of a Heinlein intake tick: 150K input tokens of which 100K cached, 15K output including
reasoning, ten minutes in a 1 GB hosted sandbox.
- 50K uncached input at $10/M = $0.50
- 100K cached input at $1/M = $0.10
- 15K output at $50/M = $0.75
- 10 minutes of sandbox at $0.03 per 20 minutes = $0.015
- **About $1.37 a turn, of which the sandbox is about 1%.** Cache writes excluded, because the API will
  not report them (below). At four turns a day that is roughly $5.50 a day or $165 a month on Astra at
  list price. One request that crosses 272K input tokens reprices the whole request.

**You cannot reconstruct the bill from the API's own usage fields.** Verbatim: usage "can be `null` when
unknown, and recorded counts may change as accounting arrives. Missing usage does not mean zero usage.
These counts are not a final bill." And: "The Agents API usage fields below do not expose a separate
cache-write count, so they cannot determine the exact model charge when that pricing applies." Astra has
cache-write pricing. **So on OpenAI's flagship model, the session's own accounting cannot give you the
exact charge.** [observability]

**The contrast with his own build.** Heinlein's runner shells out to `claude -p` under his login, so jobs
spend his subscription's usage window, and "each job's `cost_usd` is already logged"
(`heinlein/bot/README.md`), with logs kept locally for 14 days. The rented harness moves the loop, the state
and the trace to the vendor and returns a best-effort usage count.

**The three runtime meters, smallest configuration, list price:** OpenAI hosted sandbox 1 GB, $0.09 an
hour; Anthropic Managed Agents, $0.08 a session-hour; Google Agent Compute, $0.085 a vCPU-hour after 50
free hours. **The harness has been commoditised to about nine cents an hour. Tokens are the bill, and the
record is the thing you give up.**

---

## Drop-in facts (each with a source)

- OpenAI launched the Agents API in public beta on 10 September 2026, running "the same harness and
  infrastructure that powers Codex" as a service. [OpenAI launch post]
- "The Agents API currently supports data residency only in the United States and does not support Zero
  Data Retention (ZDR). Choosing a self-hosted sandbox does not make the Agents API ZDR-eligible."
  [Agents API overview]
- OpenAI's data-controls table lists Agents API application state as retained "Until deleted", and the
  endpoint as neither ZDR-eligible nor Eyes Off eligible. [Data controls]
- "Agent-generated code can access the files, credentials, and network available to its environment."
  [Sandbox security]
- Subagents share the coordinator's filesystem: "Creating a subagent does not create another
  environment." They inherit its MCP tools and credentials. [Multi-agent]
- "Trace retrieval and external trace exporters are not part of the public beta API." [Observability]
- Agents API usage counts "are not a final bill", and cannot determine the exact charge on models with
  cache-write pricing. [Observability]
- "Deleting stored credentials does not revoke the original tokens with their providers or stop a running
  session." [Vaults]
- OpenAI's hosted sandbox costs $0.03 per 20 minutes at 1 GB; Anthropic's Managed Agents runtime is $0.08
  per session-hour; Google's Agent Compute is $0.085 per vCPU-hour after 50 free hours a month.
  [three vendor pricing pages]
- The Assistants API was sunset on 26 August 2026; OpenAI names the Responses and Conversations APIs as
  its replacement. [deprecations page]
- Claude Managed Agents is "not currently eligible for Zero Data Retention or HIPAA Business Associate
  Agreement (BAA) coverage." [Anthropic Managed Agents overview]

---

## Angles this opens

- **Trust Boundaries, the main one.** Two vendors in five months have productised the agent loop, and in
  both the session record lives with the vendor, outside ZDR, whatever you do with the sandbox. It sits
  between [[You cannot rent an audit trail]] (the record is the moat, and you cannot rent it) and
  [[A black box recorder for agent actions]] (the party writing the record has an interest in it). The new
  fact: you now *can* rent the loop, and renting the loop means the record is theirs, partly visible to you
  and not exportable through the API. Filed as the Signal
  [[Managed agent harnesses - the vendor keeps the session]].
- **Machine Identity.** No per-agent identity in the pages read: a project key, a restricted executor key
  the agent can read, vault credentials bound to a URL, and subagents that inherit everything.
- **Sat 12 callback, and an optional Sat 19 beat (his call).** Sat 12's load-bearing spec was that Grok
  Bot's bots "share one computer". OpenAI's enterprise API has the same design for subagents. For Sat 19
  stage 2 ("here's how you build it"), one paragraph could name the rent-the-harness route and its price.
  Two sentences carry it: OpenAI's own showcase includes a Slack bot, so the managed version of his build
  exists; and his runner logs its cost per job while the rented one returns a count that "is not a final
  bill". The Sat 19 block warns against infrastructure framing, so this is at most a sidebar.
- **Thu 17 (incidental).** OpenAI's 3 Sep changelog ships a feature named "Misalignment monitoring" that
  "can trigger safety alerts or stop a conversation for review". The misalignment label now has a
  product surface with a stop action. Re-read at primary in the Thu 17 re-verify pass; it may sharpen or
  complicate the "research matter for papers" framing.
- **The video he posted (Coyle, ontologies).** The Agents API docs hand containment to the customer
  (brokers, allowlists, per-workload environments). Coyle's talk makes the same move one layer up: the
  harness validates nothing about your business, so a validator outside the model has to check a result
  before it counts. For Sat 19, his `reactions.md` is a five-value closed vocabulary and his RED gates are
  "delay the side effect until a human validates it": a small working ontology. Only if he wants it.

---

## Fetch log

All via Firecrawl, 12 Sep 2026. **Worked:** openai.com launch post; developers.openai.com Agents overview,
Agents API overview, architecture, OpenAI-hosted sandboxes, self-hosted sandboxes, sandbox security, MCP
connections, vaults, multi-agent, observability, data controls, pricing, GPT-6 Astra model page, changelog,
Assistants migration and deprecations (search snippets from OpenAI's own pages); Anthropic Managed Agents
overview and launch blog; Google agent platform pricing; Hacker News 49649213 (extracted, see caution);
YouTube watch page (metadata, description, chapters); ai.engineer talk page (organiser summary).
**Failed or partial:** the YouTube transcript did not come back. The data-controls page exceeded the tool
limit and was read from the saved file by grep, so only the rows cited were read. **No fetched page
contained instructions addressed to an AI or agent.**
