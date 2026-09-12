# Research Note - Ontology for AI agents, and the five links Lars sent on 11 Sep
For: no draft (intake item, feeds Wed 16 "The Score Is Not the Severity") · Depth: deep · Date: 2026-09-12
Intake file: `Research Notes/intake/intake_2026-09-12_ontology-aie-talks.md`

---

## 0. What was actually sent, and whether it was sent before

**Not sent before.** Full read of #heinlein-inbox from the channel's first message (6 Sep) to now: no
earlier ontology message. None of the five URLs or four video IDs appears anywhere on disk (Research
Notes, References, Vault, AI Briefs, Daily Briefs, Substack Drafts, Substack Published, heinlein state).
Workspace-wide public Slack search for "ontology" and "oxfordsemantic" returned nothing (public
channels only; the Heinlein channels were read directly instead). Email forwarding was not checked.

The only prior touches are incidental:
- `AI Briefs/ai_brief_2026-07-31.md` carried The Anthropic Stack's "Five Repos, One Warning About the
  Ontology Crowd" as a one-line item. **The brief's gloss was wrong**: it read the title as the
  newsletter "pushing back against over-abstracted AI architecture". The actual text (fetched today)
  endorses the ontology lesson ("Agents are probabilistic. Businesses are not.") and is only wry about
  the semantic-web revival. Never followed up.
- `Research Notes/intake/intake_2026-09-06_brooks-anthropomorphising.md` uses "ontology" in the
  philosophical sense (Bryson). Unrelated.
- Work briefs (13, 22, 26 Aug) mention knowledge graphs as a job-title signal (Graph Engineer,
  Context-Supply-Chain Manager, Ng's DeepLearning.AI course). Unrelated to these links.

**Only two of the five links are about ontology.** All four videos are from the AI Engineer channel
(AI Engineer World's Fair, July 2026). Three of them are AI security talks, not ontology talks:

| # | Link | What it is | About ontology? |
|---|---|---|---|
| 1 | imFedndyXYQ | Eugene Yan (Anthropic), "Using LLMs to Secure Source Code" | No. Security |
| 2 | yWS0udrIOc8 | Steve Yegge, "Agentic Security: Permissions, Provenance, and the Agent Supply Chain" | No. Security |
| 3 | O-CBZ3JtRvo | Uri Rolls (Arithmetic) and Thom Wolf (Hugging Face), "Training Frontier Models to Out-Think Hackers" | No. Security |
| 4 | oxfordsemantic.tech FAQ | "What is an Ontology?" | Yes |
| 5 | VGN22pPpb-8 | Emil Eifrem (Neo4j), "Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer" | Yes |

**The missing ontology video is in the adjacent message.** Lars posted
`youtube.com/watch?v=Sir59K8ZDPU` at 21:38:35, one message earlier, and it is **Frank Coyle (UC
Berkeley), "Why Agentic Systems Need Ontologies"**, the most-watched of the set (381,373 views at fetch).
That link was filed today with the OpenAI Agents API note
(`Research Notes/intake/intake_2026-09-12_openai-agents-api.md`), which already flags that the video is
not about the Agents API. It belongs with this set. Summarised from its description in section 1.6 below.

**Probable trail.** Latent Space's "Ontologies Are So Back" (Richard MacManus, 30 Jul 2026) cites
exactly three of these: the Coyle talk, the Eifrem keynote, and the Oxford Semantic definition, which it
quotes verbatim. The security talks sit beside them in the same conference playlist. Inference, not
fact.

---

## Bottom line

"Ontology" in the 2026 agent conversation means **writing down what things in a business are, how they
relate and what is allowed, outside the model, so a probabilistic agent can be checked against it.**
That idea is solid and is getting independent measurement: a 2026 paired benchmark found that a 4 KB
hand-written business-semantics document lifted text-to-SQL accuracy 17 to 23 points across three
frontier models, and model choice stopped mattering. **What is vendor framing is the format**: every
source that says the written-down context must be a graph, an ontology product or a semantic-layer
platform sells one (Neo4j, Oxford Semantic/RDFox, Palantir, the Snowflake-led Ossie consortium,
data.world). The more useful find for Lars is on the security side of the batch: **Anthropic publishes
a severity-agreement table showing its model's severity calls against human re-ratings, and the model
over-rated 133 times and under-rated 18 times out of 1,017, with only 33 of 137 "critical" calls
surviving as critical.** Anthropic's own explanation is missing context. That is Wednesday's piece.

---

## 1. Source by source

### 1.1 Eugene Yan (Anthropic), "Using LLMs to Secure Source Code"
- **Channel:** AI Engineer. **Uploaded:** 17 Jul 2026. **Length:** 21:30. **Views at fetch:** 563.
- **Transcript:** YES (auto-captions; errors such as "Entropic" for Anthropic, "mess preview about 271"
  for Mythos Preview, 271).
- **Commercial interest:** Anthropic staff. Closes on Claude Security, Anthropic's blog and its open-
  source harness repos. Every number in the talk is Anthropic's or a partner's.
- **Key parts:**
  - Claim: finding bugs is no longer the bottleneck; *"The bottleneck has now shifted to verification,
    triage, and patching."*
  - Mozilla numbers (checked at primary, see 2). Anthropic's open-source scan: 23,000 candidates, 6,200
    high or critical, **1,600 reported, about 100 patched**. **Those last two do not match either
    Anthropic snapshot** (22 May: 530 high/critical disclosed, 75 patched; 26 Aug dashboard: 2,300
    disclosed, 421 patched). Possibly an intermediate figure, or 1,587 valid true positives misremembered.
  - Six-step workflow: threat model and sandbox (setup), then discovery (optimise recall), independent
    adversarial verification (optimise precision, verifier never sees the discovery reasoning,
    detonates the proof of concept in a fresh container), triage, patch. "It all looks like a machine
    learning pipeline."
  - Threat model: *"A model has great context of the code but poor context of the system,"* attributed
    to "one CISO", unnamed. "Several teams" report a written threat model lifts true positives to 90%.
    **Anecdote, unnamed teams, no data shown.**
  - **The triage example is the exhibit.** Agent rates the SQL injection high impact, high likelihood.
    Human reviewer downgrades to low likelihood because a web application firewall blocks SQLi and the
    service is internal-only. *"How would the model know this? This is not written in a codebase."*
  - Severity calibration is an organisational problem: product and security engineers "may not agree on
    what high severity is"; write the rules down once so the agent can use them.
  - *"Things that can be solved with money are not really problems. But human attention doesn't
    scale."* *"Scanning was never the bottleneck."*
  - Prompts: with each model step-change he cuts prompt size "by maybe about 50%". Personal practice.

### 1.2 Steve Yegge (Gas Town), "Agentic Security: Permissions, Provenance, and the Agent Supply Chain"
- **Channel:** AI Engineer. **Uploaded:** 20 Jul 2026. **Length:** 22:32. **Views at fetch:** 2,895.
- **Transcript:** YES (auto-captions; "Sneak" for Snyk, "Tessell" probably Tessl).
- **Commercial interest:** *"I am here on behalf of Snyk today. I am not getting paid for this talk"*;
  Snyk bought his conference ticket. Recommends Snyk and Chainguard by name. Says he advises "Tessell"
  on agent oversight. Author of a vibe-coding book and the Beads task tracker.
- **Key parts:**
  - A bank's chief security architect: if code ships 10x faster at a constant defect rate, the defect
    surface is 10x. **An arithmetic identity, not data.** Yegge adds that the rate will get worse. Opinion.
  - Slop squatting: a model hallucinates a package name, an attacker registers it with a backdoor, tests
    pass. His "graphy 123" is a hypothetical, not a case.
  - Google's test platform learned bugs have a "half-life of urgency"; security bugs do not, so surface
    them at the moment of writing, now to the model.
  - **The 241:** a Fable hardening pass on his 30-year-old game "looked pretty good"; Snyk then found 241
    vulnerabilities. **Same talk, his words: *"it didn't find any vulnerabilities that weren't already
    public CVEs."*** So these were known CVEs, almost certainly in dependencies (inference), not novel
    code flaws the model missed. The video description drops that qualifier.
  - "Rule of five": models need four or five review passes; they do one thing well at a time, so
    security is its own pass, "your first one and your last one".
  - Five Eyes "months, not years": he glosses this as open-source models catching Mythos, polls the room,
    and lands on "about 6 months". **His gloss, not the advisory.** Lars's published 27 Jun piece read the
    same phrase as the exploit window collapsing, which is what the advisory supports. No contradiction
    with the published piece; just do not adopt Yegge's reading.
  - Q&A, useful for Machine Identity: agents running 24/7 need adversarial supervisor agents; "do they
    really need all those credentials on that service account?"; non-engineers will "spin up a bunch of
    agents with way too many permissions". Prompt injection: "kind of an education problem"; predicts
    agentic-security roles inside companies.
  - Also: refresh family code words against voice/video deepfake scams; "Congress was given secret demos
    of draining bank accounts" (hearsay, "I heard").

### 1.3 Uri Rolls (Arithmetic) and Thom Wolf (Hugging Face), "Training Frontier Models to Out-Think Hackers"
- **Channel:** AI Engineer. **Uploaded:** 24 Jul 2026 (datePublished 23 Jul PDT). **Length:** 17:27.
  **Views at fetch:** 1,811.
- **Transcript:** YES (auto-captions; the benchmark's name is garbled, "Masov", so not recorded).
- **Commercial interest:** Rolls founded Arithmetic, which builds cyber training data and evals for
  models. Wolf co-founded Hugging Face and advises Arithmetic. The open-weight-models-for-defence thesis
  suits both. They invite collaborators to their data.
- **Key parts:**
  - Thesis, stated as optimistic: attack economics have shifted (a skilled attacker with a Mythos-class
    model can hit many targets at once); the defence has to be the models themselves, including open ones.
    Wolf: the danger is relying on "two company that everyone knows here".
  - Benchmark scoped to access control (they cite it as number one on the OWASP list; Broken Access
    Control is A01 in the OWASP Top 10, general knowledge, not re-fetched). Humans find their own zero-days
    in widely used open source, wrap them in black-box multi-service environments, grade every step
    deterministically.
  - **The example is an identity-semantics bug:** a chain of Keycloak, Vault and a broker where one check
    identifies the admin **by name** and another **by ID**, so a low-privileged user renames themselves to
    the admin and inherits the privilege. Said to be a real zero-day submitted to maintainers.
    **Unverified; do not print the details.**
  - **The talk contradicts its own description.** Description: GPT-5.5 and Opus "never make that logical
    leap". Transcript: "exactly one solve at K1", only GPT at K5, and "GPT 5.5 is the only model that's
    able to make this leap" in the zoomed environment.
  - Wolf: ARC-AGI-3 models score "one to two%". His figure, not checked.
- Relevance to ontology: none by design. By accident, the example is exactly what an ontology is for: two
  components holding different definitions of who the admin is.

### 1.4 Oxford Semantic Technologies, "What is an Ontology?" (RDFox FAQ)
- **Publisher:** Oxford Semantic Technologies (Oxford University spinout). **Date:** none on the page;
  footer copyright 2024. **Fetched:** OK.
- **Commercial interest:** sells RDFox, a knowledge-graph and semantic-reasoning engine; the page is
  wrapped in "Get started for free" calls to action. The page's own news feed carries a Samsung press
  release about Galaxy S25 features "built on technology from Oxford Semantic Technologies", with an image
  filename referencing a Samsung acquisition. Ownership not re-checked this pass.
- **Key parts:** an ontology is *"a description of data structure - of classes, properties, and
  relationships in a domain of knowledge"* that serves "as a basis for instances of knowledge graphs".
  Usually written in OWL. Example: Colours, subclass Warm Colours, instance Yellow. Calls RDF, RDFS and
  SKOS "widely adopted ontologies", which is loose: RDF is a data model and RDFS/SKOS are W3C
  vocabularies. **This is the definition Latent Space quotes.** It is short, correct in outline and
  written to lead into a graph product.

### 1.5 Emil Eifrem (Neo4j), "Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer"
- **Channel:** AI Engineer. **Uploaded:** 22 Jul 2026. **Length:** 11:06 (keynote). **Views at fetch:**
  53,872. Lars's link starts at 2:20, the "problem" section.
- **Transcript:** YES (auto-captions, clean).
- **Commercial interest:** Neo4j CEO. The substrate he prescribes is his product category. Closes on
  booth P3, the graph track and the Neo4j startup programme ("free credit"). Customers cited are unnamed:
  "a Fortune 20 global bank, a massive tech platform company based here in the Bay Area, and a leading
  fintech".
- **Key parts:**
  - Problem, with a bank account-opening agent: every team rediscovers where data lives across "a
    hundred databases" plus Snowflake, Databricks and S3; decides whether it can trust the version and
    whether it may access it; rewires every agent when a source moves (a DRY violation); and "when your
    agent wakes up tomorrow, it's not smarter than it was today".
  - *"Ontology... more recently it's become very hype, probably thanks to Palantir"*; "the core concepts
    are actually super simple".
  - Markdown files and skills are "part of the solution, but it is not the solution"; quotes himself on
    the Latent Space podcast: "You cannot vibe code with just markdown files."
  - **Three pillars:** a business ontology (customers, accounts, checks, in people's words, "you don't say
    f_name"); a technical ontology (all data sources, their metadata and schemas) with a mapping between
    the two; and **execution traces** (what the agent tried, whether it worked, scored) so the layer learns
    bottom-up. Trust is then known "top-down by some kind of human curated knowledge... an administrator of
    some sort" and bottom-up from traces.
  - Slogan: "thin agents on a smarter shared substrate". **No numbers anywhere in the talk.**

### 1.6 (Adjacent message) Frank Coyle (UC Berkeley), "Why Agentic Systems Need Ontologies"
- **Channel:** AI Engineer. **Published:** 22 Jul 2026. **Length:** 21:17. **Views at fetch:** 381,373.
- **Transcript: NO** (the scrape returned the page and description only). Filed under
  `intake_2026-09-12_openai-agents-api.md`. **Worked from title, description and chapter list only.**
- **Description, not his words:** most agent failures (a second refund on the same order, a payout to the
  wrong party, an order status of "probably shipped") come from one missing layer, "a formal ontology
  sitting outside the model as logical guardrails". Neurosymbolic: probabilistic reasoning inside, logic
  outside. Ontology = typed entities, relationships and constraints in RDFS and OWL. Wrap a Claude
  tool-use loop in a validator: Pydantic checks the proposed call's types, the ontology checks the result,
  only then act. Chapter titles include "Pydantic at the door, ontology at the ledger" and "The errors an
  ontology catches that English cannot".
- Latent Space quotes him defining an ontology as "data as graphs" and an OWL axiom as "a rule a machine
  enforces". Second-hand.

---

## 2. What "ontology" means in the current agent conversation

Five senses are in use, and sources slide between them:

1. **The formal one.** Classes, properties, relationships and constraints, written in W3C standards (RDF,
   RDFS, OWL, SKOS). Oxford Semantic's definition; Coyle's RDFS/OWL. Twenty-plus years old.
2. **The semantic layer.** Agreed business definitions and metrics ("Monthly Active Users" means one
   thing) so any tool, including an agent, computes the same answer. The Open Semantic Interchange, now
   **Apache Ossie (Incubating)**, describes itself as "an open specification for both semantic layer and
   ontology"; repo opened Nov 2025; 17 launch partners grown to 50+; working groups on Metric Language,
   Catalog and **Ontology**; contributors from Snowflake, Salesforce, Databricks, dbt Labs, RelationalAI,
   GoodData and Honeydew (Snowflake blog, 8 Jul 2026).
3. **Palantir's Ontology.** Not a data model but "a system designed to represent the *decisions* in an
   enterprise, not simply the data": data, logic, action and security in one model. Objects and links are
   "the nouns", actions "the verbs". Agents act only through actions governed by the same access controls
   as humans; by default AI can only *stage* actions for human review, and the customer chooses "which
   trusted, well-worn AI processes can automatically close the action loop without human review". Each
   agent "can be considered a new team member, who is gradually granted a wider purview" (Palantir blog,
   28 Apr 2026).
4. **Neo4j's ontology-based semantic layer.** Business ontology plus technical metadata catalogue plus a
   mapping plus execution traces, as a shared substrate for many agents (Eifrem).
5. **The guardrail.** An external rule set the agent's proposals are validated against before they act
   (Coyle; The Anthropic Stack: "a harder boundary around what the model's allowed to decide").

**What they share, and what the security talks share with them:** the model sees the code or the data
but not the meaning the organisation attaches to it. Yan's threat model is the same move made for
security ("the threat model is really just a document"; "you can think of the threat model as just
synonymous with context"). Arithmetic's exploit is what the absence looks like: two components with
different definitions of "admin". **That is the thread connecting the five links, whether or not Lars
meant it.**

---

## What's solid

- **Written-down business semantics measurably improve LLM data answers.** Sequeda, Allemang and Jacob
  (data.world), arXiv 2311.07509, 13 Nov 2023: GPT-4 zero-shot on an enterprise insurance SQL schema,
  **16%**; posed over a knowledge-graph representation (ontology plus mappings), **54%**.
  Rumiantsau and Fokeev, arXiv 2604.25149, 28 Apr 2026: 100 questions over a retail dataset in
  ClickHouse, Claude Opus 4.7, Claude Sonnet 4.6 and GPT-5.4, paired single-shot: a **4 KB hand-authored
  markdown document** of measures, conventions and disambiguation rules lifts accuracy **+17 to +23
  points** (45.5-50.5% without, 67.7-68.7% with); "model choice within tier does not" matter. Both are
  primaries, fetched.
- **The revival is real as a conversation.** Latent Space (30 Jul), The Anthropic Stack (31 Jul), the
  AIE keynote slot, Ossie's ontology working group, Palantir's April post. That is a trend in what
  practitioners and vendors talk about, not evidence of adoption.
- **Mozilla, at its own primaries.** Firefox 150 fixed **271** vulnerabilities found with Claude Mythos
  Preview (blog, 21 Apr 2026). Mozilla fixed **423** security bugs in April; the monthly chart runs in the
  **20-30 range through 2025**, 60-70 in Feb and Mar 2026 (Mozilla Hacks, 7 May 2026). Of the 271: 180
  sec-high, 80 sec-moderate, 11 sec-low. So "20x" is roughly right at the bottom of the 2025 range and
  about 14x at the top, and 271 of 423 is 64%, the "two thirds" Yan cites.
- **Anthropic's scan, at its own primaries.** 22 May: Mythos Preview estimated **6,202** high or critical
  out of **23,019**; 1,752 of those assessed by six external firms; **90.6%** valid; **62.4% (1,094)
  confirmed high or critical**; a high or critical bug takes on average **two weeks** to patch.
  Dashboard as of **26 Aug 2026**: 26,153 candidates, 5,008 reviewed, 91.4% valid, **2,300 disclosed
  across 392 projects, 421 patched**, 462 identifiers (177 CVE, 285 GHSA). Includes 1,278 findings
  reported directly at maintainers' request that "may contain false positives".
- ★★ **Machine severity against human severity, published by the vendor** (dashboard "Severity
  agreement", n = 1,017 findings that completed triage, Claude's initial rating in rows, the external
  firm's in columns):

  | Claude said \ Firm said | critical | high | medium | low | total |
  |---|---|---|---|---|---|
  | critical | 33 | 85 | 6 | 13 | 137 |
  | high | 14 | 765 | 17 | 10 | 806 |
  | medium | 1 | 3 | 51 | 2 | 57 |
  | low | 0 | 0 | 0 | 17 | 17 |

  85.2% exact agreement, 97.1% within one band (arithmetic re-footed from the cells). **The model rated
  higher than the humans in 133 cases and lower in 18.** Of 137 "critical" calls, **33 (24%)** stayed
  critical. Anthropic's explanation, verbatim: *"Project maintainers often apply project-specific severity
  rules that Claude does not have access to at run time, so what one maintainer rates as critical another
  may rate as low. The external security research firms incorporate that context, which is why their
  assessments tend to be lower."*
- **Mozilla's severity is a rule, not a test.** *"We also generally don't build exploits to see whether a
  bug could be used by an attacker in the real world. We classify sec-high based on predictable crash
  symptoms."* And: is a sec-high bug a practical exploit? *"Not necessarily."* (Mozilla Hacks FAQ.)

## What's contested / watch out

- **Graph versus document.** Eifrem: "you cannot vibe code with just markdown files". The 2026 paired
  benchmark got its whole effect from a markdown file. One dataset, 100 questions, a preprint, author
  affiliations not checked; but it is the most recent controlled test found and it cuts against the
  vendor framing. The 2023 data.world result used GPT-4 and a graph; its authors' company sells a
  graph-based data catalogue. dbt Labs reports 83% on the same benchmark via its semantic layer on "a
  subset of eight addressable questions" (search result only, not fetched; dbt sells the semantic layer).
- **Maintenance is the known failure mode.** Latent Space: maintenance and keeping ontologies current is
  "why the 1990s and 2000s vision for a 'Semantic Web' ... never took off". Proposed fix (an X post): let
  the agent maintain the ontology. That puts the thing checking the agent under the agent's pen. Nobody
  has shown it works.
- **Overall agreement is high; the disagreement is at the top.** Any use of the severity table must say
  85.2% agreement before saying 24%. The story is direction and band, not general unreliability.
- **Two kinds of "machine severity".** Wednesday's CISA-ADP 9.8 is automated enrichment; Anthropic's is a
  model's pre-triage estimate. Same mechanism class, different pipelines. Do not merge them.
- **Arithmetic's model claims** conflict between the description and the talk (see 1.3).

## Couldn't verify

- Yan's "1,600 reported, about 100 patched" (matches neither Anthropic snapshot).
- Yan's "several teams" and the 90% true-positive figure from a written threat model (no data shown).
- The Keycloak/Vault name-versus-ID zero-day (speakers' claim; no advisory located; not searched hard,
  to avoid printing an unpatched bug).
- Yegge's "about six months" to open-source parity with Mythos (his gloss and a room poll).
- Neo4j's unnamed Fortune 20 bank and other customers.
- **Any cost figure for building or maintaining an enterprise ontology.** None of the sources gives one.
- Oxford Semantic's current ownership (the page implies Samsung; not re-checked).
- The Gartner "over 40% of agentic AI projects cancelled by 2027" line, which ontology vendors attach to
  this pitch. Already flagged in the corpus as the worst-sourced number in its category
  (`Vault/Writing/Signals/The AI pilot-failure numbers do not survive scrutiny.md`). Keep it out.

## The economics

- **Finding got cheap; fixing did not.** Anthropic's funnel: 26,153 candidates, 5,008 human-reviewed,
  2,300 disclosed, 421 patched (26 Aug). Two weeks average to patch a high or critical. Mozilla: "over 100
  people contributed code" to the April effort. Yan: money scales the scanner, "human attention doesn't
  scale". The cost has moved from discovery to triage, and triage is where severity gets decided.
- **Ontology's cost is authoring and upkeep, and nobody prices it.** Eifrem's case is avoided rework
  (every team re-wiring every agent). The 2026 benchmark says the cheap end, one 4 KB document, captures a
  large gain. The expensive end (graph platform, mappings, traces) is sold on scale and governance, not
  on measured accuracy beyond the document.
- **Yegge's 10x:** faster shipping at a constant defect rate multiplies the surface. An identity, useful
  as framing, not as a finding.

## Drop-in facts (each with a source)

- Of 1,017 vulnerabilities Anthropic's models rated before human triage, the model rated severity higher
  than the external security firm 133 times and lower 18 times; 33 of its 137 "critical" ratings stayed
  critical. [red.anthropic.com/2026/cvd, counts as of 26 Aug 2026]
- Anthropic, on why: maintainers "apply project-specific severity rules that Claude does not have access
  to at run time." [same]
- Mozilla does not generally build exploits to rate a bug; it classifies sec-high "based on predictable
  crash symptoms". [hacks.mozilla.org, 7 May 2026]
- Firefox security fixes ran 20-30 a month through 2025 and hit 423 in April 2026; 271 came from Claude
  Mythos Preview. [blog.mozilla.org 21 Apr 2026; hacks.mozilla.org 7 May 2026]
- As of 26 Aug 2026 Anthropic had disclosed 2,300 open-source vulnerabilities across 392 projects; 421
  were patched. [red.anthropic.com/2026/cvd]
- A 4 KB hand-written document of business definitions raised three frontier models' text-to-SQL
  accuracy by 17 to 23 points; with it, which model you used stopped mattering. [arXiv 2604.25149]
- Palantir describes its Ontology as a system to represent "the decisions in an enterprise, not simply
  the data", and treats each agent as "a new team member, who is gradually granted a wider purview".
  [blog.palantir.com, 28 Apr 2026]
- Yan: "A model has great context of the code but poor context of the system." (Quoting an unnamed
  CISO.) [AI Engineer, 17 Jul 2026, 6:06]

## Angles this opens

1. ★★ **Wed 16, "The Score Is Not the Severity".** The severity table is the counter-exhibit the piece
   lacks: the one place a machine severity rating has been published beside a human re-rating, the error
   runs one way (up), it concentrates at "critical", and the vendor names the cause as missing context.
   Pair with Mozilla's rule-based sec-high and Yan's WAF/internal-only downgrade. Wednesday's thesis is
   "nobody assigned that score"; this is what happens when somebody checks.
2. **Machine Identity.** Arithmetic's example (admin identified by name in one check, by ID in another) is
   identity semantics as attack surface. Palantir's "new team member... wider purview" is the vendor
   answer to Yegge's over-credentialed service accounts. Both unverified in detail; framing only.
3. **Trust Boundaries.** The ontology revival is a boundary argument: Coyle's validator and Palantir's
   stage-only default both put a checked rule between the agent's proposal and the action.
4. **Sat 19 (optional, stage 3).** Lars's own control plane is markdown files and skills, the exact thing
   Eifrem says is "not the solution". The 2026 benchmark says a small written document does most of the
   work. An honest line for "what it does for you": at personal scale the document is the ontology.
5. **Sun 20 capstone (light).** An ontology is a labelling system that decides what an agent reaches for.
   Palantir and Ossie make the labeller governed and versioned, a counter-example of the SOC kind, like
   Monday's re-pitch.

## Do not print

- "A threat model gets you to 90% true positives" as a measured result.
- Yan's 1,600 reported / 100 patched. Use the dashboard's 2,300 / 421, dated.
- "Snyk found 241 vulnerabilities Fable missed" without "all already-public CVEs".
- "Five Eyes says open-source models will match Mythos within months."
- "GPT-5.5 and Opus never made the leap."
- Any detail of the Keycloak/Vault exploit chain.
- "Mozilla 20x" without the base (20-30 a month in 2025, 423 in April).
- "RDF is an ontology."
- The Gartner 40% line.
- Caption spellings: "Entropic", "Sneak", "Masov", "Tessell".

## Provenance

All five links fetched with Firecrawl on 12 Sep 2026; all four videos in this item returned titles,
descriptions and auto-caption transcripts. The adjacent Coyle video returned description only. Primaries
fetched: arXiv 2311.07509, arXiv 2604.25149, blog.mozilla.org (21 Apr), hacks.mozilla.org (7 May),
anthropic.com Glasswing update (22 May), red.anthropic.com/2026/cvd (26 Aug snapshot), blog.palantir.com
(28 Apr), snowflake.com Ossie post (8 Jul), latent.space (30 Jul), theanthropicstack.substack.com
(31 Jul). **Nothing fetched was addressed to me.** Yegge's talk quotes a prompt-injection string
("disregard everything and do the following") as an example of the attack; treated as subject matter.
