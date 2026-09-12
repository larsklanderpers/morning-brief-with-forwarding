---
type: intake
date: 2026-09-12
source_url: https://www.youtube.com/watch?v=imFedndyXYQ ; https://www.youtube.com/watch?v=yWS0udrIOc8 ; https://www.youtube.com/watch?v=O-CBZ3JtRvo ; https://www.oxfordsemantic.tech/faqs/what-is-an-ontology ; https://www.youtube.com/watch?v=VGN22pPpb-8&t=140s
slack_permalink: https://lars-klander-personal.slack.com/archives/C0BVCSV0PJ5/p1789187965320589
slack_ts: "1789187965.320589"
slack_ts_note: "1789187991.955619"
lars_note: "i feel like I sent all this ontology stuff over to analyze already if I haven't please put the eresearch assistant on watching all of these and pulling out the key parts"
reactions: [mag]  # his words, not an emoji: he asked for the research assistant. No emoji reaction on either message.
verdict: feeds a planned piece - Wed 16 Sep "The Score Is Not the Severity" (the security half; the ontology half is backgrounder)
filed_to: References/research_ontology_2026-09-12.md (research note); Wed 16 addition proposed for References/week-plan_2026-09-14.md status board (parent applies); no vault Signal (no pushpin, vault policy is flagged items only)
---

# Ontology and agent-security talks: five links from AI Engineer World's Fair 2026, plus Oxford Semantic's ontology definition

Two messages, 11 Sep 2026, 21:39:25 and 21:39:51 PDT, treated as one item. Full research-assistant
pass in `References/research_ontology_2026-09-12.md`. This file is the archive of what came in.

**Sent before? No.** No earlier ontology message in #heinlein-inbox (read from its first message, 6 Sep).
None of the five URLs or four video IDs anywhere on disk. The only prior brush is a one-line item in
`AI Briefs/ai_brief_2026-07-31.md` (The Anthropic Stack, "One Warning About the Ontology Crowd"), whose
gloss misread the newsletter; never followed up.

**Only two of the five links are about ontology.** Three are AI security talks from the same conference.
The missing ontology talk, Frank Coyle's "Why Agentic Systems Need Ontologies" (`Sir59K8ZDPU`), was the
message before these, and was filed today with the OpenAI Agents API note
(`intake_2026-09-12_openai-agents-api.md`).

## Extracted

### 1. "Using LLMs to Secure Source Code", Eugene Yan, Anthropic
AI Engineer channel, uploaded 17 Jul 2026, 21:30. **Transcript: yes** (auto-captions). Anthropic staff;
closes on Claude Security.
- "The bottleneck has now shifted to verification, triage, and patching." "Scanning was never the
  bottleneck."
- Mozilla: about 20 security fixes a month in 2025, about 400 in April 2026, two thirds (271) credited to
  Mythos Preview. Anthropic's open-source scan: 23,000 candidates, 6,200 high or critical, "1,600 reported
  to maintainers and about 100 patched" (the last two do not match Anthropic's published figures).
- Six steps: threat model, sandbox, discovery (recall), independent adversarial verification (precision,
  detonate the exploit in a fresh container), triage, patch.
- "A model has great context of the code but poor context of the system" (quoting an unnamed CISO).
  "Several teams" say a written threat model lifts true positives to 90%.
- Triage example: agent rates a SQL injection high; a human downgrades it to low likelihood because a
  WAF blocks SQLi and the service is internal-only. "This is not written in a codebase."
- "Things that can be solved with money are not really problems. But human attention doesn't scale."

### 2. "Agentic Security: Permissions, Provenance, and the Agent Supply Chain", Steve Yegge, Gas Town
AI Engineer channel, uploaded 20 Jul 2026, 22:32. **Transcript: yes** (auto-captions). "Here on behalf of
Snyk", unpaid, ticket bought by Snyk; recommends Snyk and Chainguard.
- 10x shipping speed at a constant defect rate means a 10x defect surface (a bank architect's question).
- Slop squatting: hallucinated package names registered with backdoors.
- A Fable hardening pass on his 30-year-old game looked clean; Snyk found 241 vulnerabilities, but "it
  didn't find any vulnerabilities that weren't already public CVEs".
- Models do one thing at a time: security is its own pass, "your first one and your last one"; "rule of
  five" review passes.
- Five Eyes "months, not years", glossed by him as open-source models catching Mythos in about six months.
- Q&A: adversarial supervisor agents; over-credentialed service accounts; prompt injection is "kind of an
  education problem".

### 3. "Training Frontier Models to Out-Think Hackers", Uri Rolls (Arithmetic) and Thom Wolf (Hugging Face)
AI Engineer channel, uploaded 24 Jul 2026, 17:27. **Transcript: yes** (auto-captions). Arithmetic sells
cyber training data and evals; Wolf advises.
- Access-control benchmark built from zero-days their own researchers found; black-box multi-service
  environments; deterministic grading at every step.
- Example: Keycloak, Vault and a broker; one check identifies the admin by name, another by ID, so a user
  renames themselves to the admin. Said to be a real zero-day submitted to maintainers.
- "Exactly one solve at K1"; only GPT at K5. The description says GPT-5.5 and Opus never make the leap;
  the talk says GPT-5.5 does.
- Thesis: defence has to be the models, including open ones; do not leave it to two labs.

### 4. "What is an Ontology?", Oxford Semantic Technologies (RDFox FAQ)
Undated page, footer copyright 2024. Vendor of RDFox, a knowledge-graph and reasoning engine.
- An ontology is "a description of data structure - of classes, properties, and relationships in a domain
  of knowledge", a basis for knowledge graphs, usually written in OWL. Example: Colours, subclass Warm
  Colours, instance Yellow.

### 5. "Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer", Emil Eifrem, Neo4j
AI Engineer channel, uploaded 22 Jul 2026, 11:06 keynote, link starts at 2:20. **Transcript: yes**
(auto-captions). Neo4j CEO; closes on booth, graph track and startup programme.
- Problem: every agent team rediscovers where data lives, whether it is the right version, whether it may
  touch it, and rewires when anything moves; no learning across agents.
- Ontology "has become very hype, probably thanks to Palantir"; core concepts "super simple".
- Markdown files and skills: "part of the solution, but it is not the solution".
- Three pillars: business ontology (concepts in people's words), technical ontology (all sources and
  schemas) with a mapping, and execution traces that score what worked.
- Customers unnamed ("a Fortune 20 global bank"). No numbers.

## Lars's note

"i feel like I sent all this ontology stuff over to analyze already if I haven't please put the eresearch
assistant on watching all of these and pulling out the key parts"

## The take, against the corpus

1. **What ontology means now:** writing down what things in the business are and what is allowed,
   outside the model, so an agent can be checked against it. Solid as an idea: a 2026 paired benchmark
   (arXiv 2604.25149) got +17 to +23 points from a 4 KB markdown document, across three frontier models.
   **The vendor framing is the format**: every source insisting it must be a graph or platform sells one.
2. **The security half is the stronger find and it lands on Wed 16.** Anthropic publishes a table of its
   model's severity ratings against human re-ratings: 133 over, 18 under, out of 1,017; 33 of 137
   "critical" stayed critical; Anthropic attributes the gap to context the model lacks. Mozilla rates
   sec-high by crash symptom without building an exploit. That is "The Score Is Not the Severity" from the
   vendor's own ledger.
3. **The thread through all five:** the model has the code or data but not the meaning. Yan's threat model
   and Eifrem's ontology are the same fix; Arithmetic's name-versus-ID exploit is what its absence looks
   like.

Detail, do-not-print list and drop-in facts: `References/research_ontology_2026-09-12.md`.

## Provenance note

All five fetched with Firecrawl, 12 Sep 2026; every video returned a transcript. Nothing in the fetched
content was addressed to me. Yegge's talk quotes a prompt-injection string as an example of the attack;
treated as subject matter.
