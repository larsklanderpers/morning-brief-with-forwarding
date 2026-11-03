---
date_first_seen: 2026-08-07
date_updated: 2026-08-07
source: Anthropic platform docs / Anthropic blog / Proofpoint
url: https://platform.claude.com/docs/en/manage-claude/inference-hooks
brief: ai
threads: [Trust Boundaries, AI Sovereignty, Co-Existence - Judgment]
beat: AI / Enterprise Controls / DLP
status: developing
used_in:
---

# Anthropic inference hooks — the first deny switch the customer holds

**What happened.** Beta for Claude Enterprise, **5 Aug 2026**. Every governed inference request is sent
to *"your organization's AI security server, an HTTPS service that the organization or its security vendor
operates"*, which returns allow or deny before inference begins. Named partners: Netskope, Palo Alto
Networks, Proofpoint, Zscaler.

**Why it matters.** For a regulated-industry operator this is the first vendor-supported point where the
*customer* — not the model provider — gets to say no, in line, before the prompt is processed. Every prior
control in this space was retrospective. That is a genuine change in where the boundary sits, which is why
it belongs to [[Trust Boundaries]] rather than to a product-news bucket.

## Verified 2026-08-07 — the docs contradict the brief in four places

Read the **platform docs**, not the blog; the blog is thinner and looser.

1. **It is not "every prompt and tool call."** *"Today the only hook event is `prompt`, which fires once
   per governed inference request, before inference begins."* There is no separate tool-call hook. In an
   agent loop each model call is its own request, so tool *results* get inspected on the next hop — but the
   mechanism is per-inference-request, not per-tool-event.
2. **It is ingress-only.** Nothing in either primary says model **output** is inspected. Calling it "DLP"
   invites the reader to assume both directions. **This checks what goes in, not what comes out** — the
   sharpest under-reported point in the story, and it undercuts the brief's own "silence-of-the-model
   attacks are in scope" line.
3. **5 seconds is a configurable default, not a fixed timeout**, and **the fail mode is a customer setting**:
   *"If your AI security server is unreachable, returns an error, or doesn't respond within the timeout, your
   organization's failure handling setting decides the outcome: block the request, or allow it to proceed
   without inspection."* Fail-open is a checkbox. That is the governance question, not the latency.
4. **Coverage gaps are stated plainly:** *"Inference hooks are not available on Amazon Bedrock or Google
   Cloud."* **"Voice mode is not covered."** For an Australian entity that has deliberately routed Claude
   through Bedrock for residency reasons, the control and the residency choice are **mutually exclusive today.**
   That is a piece on its own.

**Also:** the hook server sees *"transcript text, tool calls and their results, and text extracted from
attachments"* and *"never receives raw file or image bytes, system prompts, or Anthropic-internal context."*
Audit logging is **denials only** — recorded in the Activity Feed; no documented log of allowed requests.
Latency and pricing: **unquantified in both primaries** — the only number anywhere is Proofpoint's vendor
claim that added latency is "expected to be minimal." **[VERIFY] if a draft leans on it.**

## Is "first of its kind" fair? Narrowly yes — and name the interest

- **OpenAI's Compliance API is retrospective**: immutable append-only log events plus a stateful query API,
  16 partners consuming exported logs. **No inline blocking.**
- **Microsoft Purview DLP for Copilot does block in real time** — *"prevents Microsoft 365 Copilot and
  Copilot Chat from returning a response when prompts contain sensitive data"* — but it is Microsoft-native
  policy, not a customer-operated webhook returning a verdict, and *"updates to a DLP policy can take up to
  four hours to reflect."*
- Google: no equivalent customer-hosted inline hook found.

Fair framing: **first model provider to expose an inline allow/deny hook to a customer-operated server** —
not first inline DLP for AI. And per the standing rule: every corroborating "this is a big deal" source
(Proofpoint, Netskope, PANW, Zscaler, Check Point) **sells the server that plugs into it.**

## Observations

- **2026-08-07** — First seen. Lands the same week as [[AISI cyber range - the agents went out of scope]], which is not coincidence: the compliance case and the capability-without-guardrails case arriving together is itself the story the brief called correctly.

## Feeds

- [[Trust Boundaries]] — the boundary moves from vendor-internal filters to a customer-held verdict
- [[AI Sovereignty]] — but not on Bedrock or Vertex, so it does not compose with a residency strategy
- [[Co-Existence - Judgment]] — allow/deny is a judgment someone now has to encode
- [[You cannot rent an audit trail]] — you still cannot; denials are logged, allowed requests are not

## Open

- The fail-open setting is the whole argument. A control whose failure mode is "proceed without inspection" is a control that degrades silently under exactly the conditions that produce incidents. Ask any operator which way theirs is set — most will not know.
