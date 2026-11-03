# Research Note — The three Saturday [VERIFY] items: Mollick, cost-per-accepted-task, AI FinOps

For: `substack_draft_what-wrong-sounds-like_2026-08-15-rv1.md` (Sat 15 Aug, Diversion) · Depth: deep · Date: 2026-08-12
Closes: all three open `[VERIFY]` blocks in that draft's header.
Related: `Vault\Writing\Signals\The archetypes converge on one shape.md` (the 2026-08-10 observation that raised all three), `Vault\Writing\Signals\Mollick - from working with AI to managing AI.md`

---

## Bottom line

**Item 1 flips from hedged to the strongest claim in the piece.** The domain-expertise finding is not Mollick's assertion and not a commenter's gloss — it traces to a **peer-style Anthropic research paper covering ~400,000 Claude Code sessions from ~235,000 users, Oct 2025–Apr 2026**, six named authors, published 16 Jun 2026. Mollick was reporting it. The draft currently under-claims: it can be asserted, with a primary, and the underlying number is *better* than the version in the draft. **But the specific lawyer-versus-engineer sentence must be cut** — that is a reader's comment on Mollick's post, not a finding, and it is exactly the failure mode logged in `feedback_brief_claim_provenance.md`.

**Item 2 splits in two, and the split is the story.** The *title* "Cost-per-Accepted-Task Analyst" **does not exist** — zero live postings, zero historical postings, zero named employers, across every board searched. It is a coinage. The *metric* is real, predates the podcast the brief credits it to, and traces back through McKinsey to an arXiv paper. So the draft's current hedge is right in spirit but wrong in mechanism: it hedges the volume when it should be disowning the title.

**Item 3 is the opposite problem — it is more solid than the draft assumes.** AI FinOps is a **formally recognised category in the FinOps Framework since 19 Mar 2026**, with certified training, a governing body under the Linux Foundation, and real postings at **Qualcomm ($155,400–$233,000), Singtel, Autodesk, New American Funding, ServiceNow, UKG**. It is dozens of postings, not hundreds, and the Foundation itself calls the work "adapting classic FinOps practices" rather than a new profession. That last fact is the most useful thing in this note for the piece's actual argument.

**Item 4 (BCG) verifies at the primary and needs one wording correction.** Plus there is an independent survey that reads the other way, and carrying it would strengthen the piece.

---

## ITEM 1 — The Mollick / domain-expertise claim

### What's solid

**The primary is an Anthropic research paper, not a Substack post.**
"How Claude Code is used in practice" — Zoe Hitzig, Maxim Massenkoff, Eva Lyubich, Shaoyi Zhang, Ryan Heller, Peter McCrory. Published **16 Jun 2026**. https://www.anthropic.com/research/claude-code-expertise

- Sample: **~400,000 interactive Claude Code sessions from ~235,000 users, October 2025 – April 2026.**
- Two success measures: *judged success* (a classifier decides whether the user accomplished their stated goal) and *verified success* (judged success **plus** verifiable evidence — git commits, passing tests, explicit user confirmation).

**The occupation finding, verbatim:**
> "In code-producing sessions, every one of the ten largest occupations in our dataset lands within seven points of software engineers" — in terms of their success.

**The expertise finding, verbatim:**
> "The more expertise a person exhibits in a session, the more likely it is that the session succeeds."

Novice-rated sessions: **15% verified success.** Intermediate/expert: **28–33%.** Overall verified success across all sessions: **~26–30%.**

**Expertise is explicitly task-specific, not credential-based.** The paper's framing: a senior engineer working in unfamiliar Rust is rated a beginner *for that task*. This is precisely the piece's argument, arrived at independently.

**Mollick's own line, verbatim, from "The Twilight of the Chatbots" (30 Jun 2026):**
> "The more domain experience someone had, the more successful they were in using Claude Code in that domain."
https://www.oneusefulthing.org/p/the-twilight-of-the-chatbots

Also from Mollick's text, and usable:
> "A quarter of OpenAI workers have at least four agents running at one time every week."

### CUT THIS — it is a comment, not a finding

**"A lawyer who's never written code was as effective as a software engineer working in an unfamiliar domain."** — This is from a **reader comment** on Mollick's post, by a user posting as *Scenarica*. So is **"AI doesn't replace professions. It makes professions porous"** (the commenter's actual wording is "The walls between 'coder' and 'non-coder' dissolve").

The AI Work briefs of **31 Jul** and **1 Aug 2026** both carry the lawyer-vs-engineer sentence as though it were Mollick's data. The 1 Aug brief even prints the tell in a parenthesis — *"(Top commenter, 32 likes — this framing is sticking.)"* — and then the piece treats it as evidence anyway. **This is the fourth failure mode already logged: an opinion laundered by aggregation, one hop from being a fact.** The draft's current sentence — "a good accountant beats a mediocre engineer at getting useful work out of an agent pointed at accounting" — is a paraphrase of the comment, not of the study. Replace it with the study.

### What's contested / the caveat worth printing

**How "expertise" was rated is the load-bearing methodological question, and the answer half-undermines the claim and half-improves it.** The classifier inferred expertise from the session transcript, not from any credential or self-report. Verbatim, the three signals:

> "how precisely the user frames their directions, what they ask Claude to verify, and whether the user tends to correct Claude or Claude tends to correct the user"

There is real circularity here: precise framing and active correction are *behaviours that cause success*, so a measure built from them will predict success partly by construction. A careful reader will spot this.

**But making the concession is what strengthens the piece, and this is the same move as the 13.6% concession in the Friday research note.** What the study actually establishes is not "people with domain knowledge do better" — it is that **the observable behaviour predicting success is knowing enough to specify precisely and to correct the machine rather than be corrected by it.** That is a sharper statement of the Saturday thesis than the draft currently has, and it is exactly the "write down the tell and hand it over" section restated as a measurement.

**Selection caveat.** "Ten largest occupations within seven points" is measured **inside code-producing Claude Code sessions** — a population that has already self-selected into using an agentic coding tool. It does not establish that a randomly chosen lawyer equals a randomly chosen engineer. It establishes that *among people already doing this*, occupation stops predicting outcomes.

**The authors' own limitation, verbatim:**
> "We cannot measure real-world outcomes, like whether code written in a session is actually used or discarded thereafter."

and

> "classifiers remain challenging to validate at scale."

### The number the draft is missing

**Even expert sessions verify success only 28–33% of the time. Overall it is roughly 26–30%.** Two thirds to three quarters of sessions do not produce verifiable success at all. That is a far more interesting number for a CISO audience than the expertise gradient, it is from the vendor's own study of its own product, and it is the honest floor under the whole "agents do the work now" conversation.

---

## ITEM 2 — "Cost-per-Accepted-Task Analyst"

### Couldn't verify — because it does not exist

**Zero live postings. Zero historical postings. Zero named employers.** Exact-phrase searches for "Cost-per-Accepted-Task Analyst", "Accepted Task Analyst", "accepted-task analyst" and "AI cost per task analyst" returned nothing on LinkedIn, Indeed, ZipRecruiter, Greenhouse, Lever or Ashby, and nothing on the open web. Domain-restricted searches against the ATS providers returned nothing.

What the searches return instead is generic "Cost Analyst" SEO furniture — ZipRecruiter and Glassdoor salary pages, Indeed JD templates, Salary.com, PayScale, Betterteam. The nearest real-sounding item is an "AI Task Analyst" at a company called Matrices, surfaced only via the aggregator jobright.ai. Different title. Not a hit.

**The brief's own wording was honest and got lost in transmission.** The 10 Aug AI Work brief printed it as *"Cost-per-Accepted-Task Analyst (no standard title yet)"*. By the time it reached the archetypes note and then the draft, the parenthesis had fallen off. **The title is AIDB's descriptive coinage for a function, and the draft should say so rather than hedge the posting volume.**

### What's solid — the metric is real, and it is older than the podcast

**McKinsey/QuantumBlack, "Cost versus value: Managing agentic AI system performance", 8 Jul 2026** — the dominant primary formulation is **"cost per completed task"**, not "accepted":
> "The metric that matters is cost per completed task."
https://www.mckinsey.com/capabilities/quantumblack/our-insights/cost-versus-value-managing-agentic-ai-system-performance

The exact string "cost per accepted task" is rare. It appears in the AIDB episode the brief cites — **aidailybrief.ai/e/2026-08-02, "Everything You Need to Know About AI Tokens", Operator's Cut with Nufar Gaspar, host Nathaniel Whittemore, 2 Aug 2026** — verbatim:
> "Include retries, review, and every correction, then divide by accepted results — that's your cost per accepted task."

The episode, guest, date and framing all check out as the brief described. But the *idea* predates it: the McKinsey piece is 8 Jul, and there is a personal engineering post on "cost-per-resolved-task" from **2 Jun 2026** (tianpan.co). So the podcast applied the "accepted" wording to an idea already in circulation. **Whether "accepted" specifically is Gaspar's coinage is not provable either way** — no pre-2 Aug use of that exact string was found.

### The McKinsey 60% — found, and it is not McKinsey's research

Verbatim, in two McKinsey publications:
> "About 60 percent of an agentic task's costs, in fact, are tied to refining answers."

and, in the 13 Jul companion piece:
> "the expensive part is not the first answer generated but the checking, repairing, and reverifying that follows."
https://www.mckinsey.com/capabilities/quantumblack/our-insights/is-that-ai-agent-worth-it-agentic-economics-and-the-modern-operating-model

**McKinsey's own footnote attributes it to an academic paper**, not to McKinsey research: Salim, Latendresse, Khatoonabadi & Shihab, *"Tokenomics: Quantifying Where Tokens Are Used in Agentic Software Engineering"*, **arXiv:2601.14470, 20 Jan 2026**. The paper's abstract: *"The iterative Code Review stage accounts for the majority of token consumption for an average of 59.4% of tokens."* https://arxiv.org/abs/2601.14470

Two caveats to print if used: the figure is **rounded up from 59.4%**, and it is measured on **agentic software-engineering workflows only**, not agentic work generally. The trail ends at a coding-agent token study, not an enterprise survey.

### Correction to a figure sitting in the 6 Aug brief

**The "agentic work costs 5–30x a simple chat" figure is misattributed to McKinsey.** McKinsey says something different in both directions: agentic tasks can consume **~1,000x** more tokens than chat (citing a Microsoft/Stanford finding), and separately there is a **factor-of-30 variation between runs of the same task** — which is variance, not a multiple over chat.

The 5–30x traces to **Gartner, March 2026**, reached only through vendor blogs (DoiT, 11 Aug 2026; Spheron, 16 Jul 2026, which cites a blog citing Gartner). **No primary Gartner document was reached — it is presumably paywalled. Treat 5–30x as unverified.** Not needed for Saturday, but it should not go into a later piece unchallenged.

---

## ITEM 3 — AI FinOps

### What's solid — considerably more than the draft assumes

**It is a formally recognised category with a governing body.** The FinOps Foundation is a Linux Foundation project. The sequence:

- **21 May 2025** — Framework adds "Scopes". **AI is not one of them** (SaaS, private cloud, data center).
- **3 Jun 2025** — "FinOps for AI" training series and certification launched. J.R. Storment, Executive Director: *"FinOps teams are being asked to manage accelerating AI spend...But the speed and complexity of the data makes this a moving target, and cost overruns in AI can slow innovation when not well managed."*
- **10 Oct 2025** — working group paper, *GenAI FinOps vs. Cloud FinOps*.
- **19 Mar 2026** — the **2026 Framework formally lists FinOps for AI as one of five Technology Categories**, alongside Public Cloud, SaaS, Data Center and Data Cloud Platforms. https://www.finops.org/insights/2026-finops-framework/

Canonical scope definition, verbatim (https://www.finops.org/framework/technology-categories/ai/):
> "FinOps for AI focuses on addressing the cost complexity, faster development cycle, spend unpredictability, and the need for a greater degree of policy and governance to support innovation through allocation, forecasting, and optimization decisions that align consumption, investment, and business value."

**State of FinOps 2026** (published 19 Feb 2026; n = **1,192 respondents** representing **$83bn+ annual cloud spend**; 6th annual edition; 35% EMEA / 34% NA / 16% APAC / 15% S&C America):
> "Almost all the 1,192 survey respondents (98%) are managing AI spend, it has become the norm, up from 31% just two years ago."

> "FinOps for AI is now the top forward-looking priority, while AI value management is the #1 skillset teams are seeking to add."

**Live postings at named employers, verified on employer or governing-body domains:**

| Employer | Title | Detail |
|---|---|---|
| **Qualcomm** | Lead, Enterprise AI FinOps (San Diego) | **$155,400–$233,000.** *"Establish the AI-FinOps operating model: visibility, cost accountability, show-back, optimization cadences, and leadership reporting."* Requires knowledge of tokens, prompts, models, embeddings, RAG and inference workloads. |
| **Singtel** | AI FinOps Engineer – #AIDA (Singapore) | Posted **9 Aug 2026**. *"Maintain the centralized framework for tracking Azure consumption and GenAI token usage across projects, teams, and applications"*; *"Build dashboards and alerts to monitor real-time and forecasted costs, including anomaly detection for budget risks."* |
| **New American Funding** | Lead, AI FinOps & Consumption Governance | Posted 16 Jul 2026, closes 16 Aug 2026, on the Foundation's own board (jobs.finops.org). *"Own end-to-end visibility and control of all AI spend across NAF."* |
| **Autodesk** | Senior Cloud & AI FinOps Analyst (Denver / Novi) | Posted 6 Aug 2026. |

Also carrying AI-centric FinOps titles: **ServiceNow** (Staff FinOps AI Governance Lead), **UKG** (Staff AI FinOps Governance Lead), **Bayview Asset Management** (AI FinOps & Governance Lead).

**Volume, with the honest deflation.** Indeed US, exact quoted query `"AI FinOps"`, returns *"Browse 24 Ai Finops jobs"*. Of the ~15 results on page one, **only about six are actually AI-cost roles** — the rest are generic AI engineering jobs matching loosely (Microsoft, HP, Vertex Pharmaceuticals). **This is dozens, not hundreds.** Board counts are noisy and this one overstates by roughly half.

### What's contested — and this is the most useful finding in the note

**The Foundation's own documents undercut the "new discipline" framing.** From *GenAI FinOps vs. Cloud FinOps*: *"GenAI FinOps shares the core principles of Cloud FinOps (like consumption-based pricing and commitment discounts)"*, and the work is framed as *"adapting classic FinOps practices"*. The *FinOps for AI Overview* (updated 17 Feb 2026) is blunter still:
> "Many AI services fall into the categories of spending you are already tracking"

> "Basic Price * Quantity = Cost equation still applies."

That is the governing body saying: **extension, not new profession.**

**The data standard still cannot represent the unit.** FOCUS is the technical substrate of FinOps. The FOCUS 1.3 launch (Dec 2025) says: *"Future FOCUS versions will deepen support for cloud and SaaS billing while expanding to additional spending scopes, including data center and AI."* FOCUS 1.2 handles tokens only as generic *"virtual currency"* (prepaid credits), not AI consumption semantics. Even at FOCUS 1.4 (ratified 4 Jun 2026) the working group is undecided — Shawn Alpay, director of data engineering at the FinOps Foundation: *"When it comes to AI and tokens in that realm, you're starting to talk about per user … per session, per request, per operation — and the farther down this ladder you go, the larger the cardinality."* They are *"actively weighing whether to create a net-new observability dataset or integrate with existing frameworks such as the OpenTelemetry project."*

**A discipline whose billing standard cannot yet represent its core unit is early.** That sentence is available to the piece as-is.

**Titles bundle rather than separate.** Autodesk's real posting is "Senior Cloud **&** AI FinOps Analyst" — one analyst covering both. That is the signature of scope creep on an existing role, not a new labour market.

### Couldn't verify

- **Cargill "AI Platform FinOps Sr. Engineer"** — the careers.cargill.com URL now resolves to the careers homepage and it appears on no aggregator. A LinkedIn job ID exists but LinkedIn blocks fetching. Probably genuine but closed. **Do not cite as live.**
- **State of FinOps 2026 field dates** — not published. Sample size and publication date are documented; the collection window is not. The survey is also self-selecting from the Foundation's own community, which skews toward organisations already doing FinOps. The 98% figure should be read as "98% of people already in FinOps roles", not 98% of enterprises.
- **Aggregator contamination.** The "Autodesk FinOps Product Owner" lead came only via Lensa/BeBee, located in Tallahassee, and does not appear on Autodesk's own Workday board; a parallel listing appeared via techmap in Des Moines. One scraped copy had the employer name replaced with the literal string "reputed company". **Any count drawn from aggregators is inflated.**
- **Practitioner skepticism** — essentially none found, across r/FinOps, r/devops, Hacker News, LinkedIn and the IBM Cloudability community. **The absence is itself the finding, and it is a caution:** the AI FinOps discourse is produced almost entirely by the Foundation and by vendors (CloudZero, Finout, nOps, Kion, Cloudchipr, Revenium, USU). Even Forrester's FinOps X recap is promotional. **No independent labour-market data on AI FinOps roles exists.**

### The accurate sentence

Do not write "AI FinOps is a hiring market." Write:

> AI FinOps is now a formally recognised category within the FinOps Framework — the FinOps Foundation made it one of five Technology Categories in March 2026 and certifies training for it — and a small number of large employers including Qualcomm, Singtel and Autodesk are hiring dedicated roles at real salaries. But this is dozens of postings, not hundreds; the Foundation itself describes the work as "adapting classic FinOps practices" rather than a separate discipline; and the FOCUS billing standard that underpins FinOps still does not cover AI consumption data.

Short form: **a recognised specialism with an emerging hiring signal, not yet a distinct job market.**

---

## ITEM 4 — The BCG figures

### What's solid

Primary: **BCG press release, 3 Jun 2026**, "AI Is Reshaping Jobs Faster Than Companies Are Reshaping Work". https://www.bcg.com/press/3june2026-ai-reshaping-jobs-faster-than-companies-reshaping-work

Sample, verbatim: *"global survey of 11,749 workers across 14 markets and a broad range of industries"*.

**One wording correction the draft needs.** The headline is:
> "42% of regular AI users Among Frontline Employees Report Saving a Full Workday **or More** Through AI per Week"

The draft says "at least a full working day", which is correct — keep it. But the subgroup must stay explicit in the sentence itself: **regular AI users among frontline employees**, not "people who use these tools regularly in frontline roles" doing the work of a subordinate clause. It is a subgroup of a subgroup.

The guidance figure, verbatim, with a bonus clause the draft is not yet using:
> "66% report they get limited or no guidance on what to do with that time, **and more than half don't redirect it into strategic work**"

That second clause is stronger than the draft's current inference. It is not "the time is probably being reabsorbed" — BCG measured it.

The management figure, verbatim:
> "nearly half (47%) report spending more time managing and directing AI than doing the work itself"

Note "**report**". The draft's insistence that *say* is doing real work in that sentence is correct and should stay.

**BCG did not publish field dates, question wording, or the 14 markets.** Flagged previously in the archetypes note on 7 Aug; still true.

### The independent counter-datapoint worth carrying

**Section, "The AI Proficiency Report"** (published Jan 2026; fielded **26 Sep – 3 Nov 2025**; n = **5,000 knowledge workers** at companies with 1,000+ employees), reported by eMarketer 9 Mar 2026:

> "68% of AI-using employees in the UK and North America save 4 hours or less per week from AI"

This is a genuinely different read of the same phenomenon — but note it is **not the same population and not the same period**: all AI-using knowledge workers, fielded ~8 months before BCG's release, versus BCG's regular-user frontline subgroup. It does not refute the 42%; it locates it. **Carrying one sentence of it would inoculate the piece against the obvious objection** — that "save a workday" is a headline built on a favourable slice.

---

## The economics

The through-line across all three items is a cost story the piece can use in one paragraph.

**The metric moved because the cost structure did.** Cost-per-token was the right metric when the work was one call. It stopped being the right metric when ~60% of an agentic task's tokens go to checking, repairing and reverifying the first answer (arXiv:2601.14470, via McKinsey). At that point the meaningful denominator is not *what was generated* but *what was accepted* — and **somebody has to decide what "accepted" means**. That decision is not a finance decision. It is a domain judgment, priced.

That is the whole Saturday argument arriving from the accounting side: the market has invented a metric that **cannot be computed without a domain expert in the loop**, and it is now hiring people to compute it at $155k–$233k. The seat is real. The title is not.

**And the cheapest control is again the unclaimed one.** Anthropic's own 400k-session study puts verified success at 26–30%. The organisations spending on tokens are paying full price for a 70% miss rate, and the single variable the study can find that moves it is whether the person at the keyboard knows enough to specify precisely and correct the output. That capability costs nothing to deploy and cannot be bought from a vendor.

---

## Drop-in facts

- "In code-producing sessions, every one of the ten largest occupations in our dataset lands within seven points of software engineers" — Anthropic, *How Claude Code is used in practice*, 16 Jun 2026 (~400,000 sessions, ~235,000 users, Oct 2025–Apr 2026)
- "The more expertise a person exhibits in a session, the more likely it is that the session succeeds." — same
- Novice sessions: 15% verified success. Intermediate/expert: 28–33%. Overall: ~26–30%. — same
- Expertise was inferred from the transcript via three signals: "how precisely the user frames their directions, what they ask Claude to verify, and whether the user tends to correct Claude or Claude tends to correct the user" — same
- "We cannot measure real-world outcomes, like whether code written in a session is actually used or discarded thereafter." — same, limitations
- "The more domain experience someone had, the more successful they were in using Claude Code in that domain." — Ethan Mollick, *The Twilight of the Chatbots*, 30 Jun 2026
- "A quarter of OpenAI workers have at least four agents running at one time every week." — same
- "The metric that matters is cost per completed task." — McKinsey/QuantumBlack, 8 Jul 2026
- "About 60 percent of an agentic task's costs, in fact, are tied to refining answers." — McKinsey/QuantumBlack, 8 Jul 2026, citing arXiv:2601.14470 (which reports 59.4%, on software-engineering workflows only)
- "Include retries, review, and every correction, then divide by accepted results — that's your cost per accepted task." — Nufar Gaspar, AI Daily Brief Operator's Cut, 2 Aug 2026
- "Many AI services fall into the categories of spending you are already tracking" / "Basic Price * Quantity = Cost equation still applies." — FinOps Foundation, *FinOps for AI Overview*, updated 17 Feb 2026
- FinOps for AI became one of five Technology Categories in the FinOps Framework on 19 Mar 2026
- "Almost all the 1,192 survey respondents (98%) are managing AI spend, it has become the norm, up from 31% just two years ago." — State of FinOps 2026, 19 Feb 2026
- Qualcomm, "Lead, Enterprise AI FinOps", $155,400–$233,000: "Establish the AI-FinOps operating model: visibility, cost accountability, show-back, optimization cadences, and leadership reporting."
- "66% report they get limited or no guidance on what to do with that time, and more than half don't redirect it into strategic work" — BCG, 3 Jun 2026
- "68% of AI-using employees in the UK and North America save 4 hours or less per week from AI" — Section, *The AI Proficiency Report*, n=5,000, fielded 26 Sep–3 Nov 2025

---

## What the draft should do

1. **Replace the hedged Mollick paragraph with the Anthropic study**, asserted rather than hedged, and **cut the lawyer-versus-engineer comparison** — it is a reader's comment. Add the circularity caveat in one sentence, because it converts into the piece's own thesis.
2. **Consider adding the 26–30% verified-success number.** It is the strongest single fact in this note and nothing else in the week uses it.
3. **Disown the title rather than hedge the volume.** "Cost-per-Accepted-Task Analyst" has no postings anywhere; the brief's own "(no standard title yet)" got lost in transmission. The metric is real and older than the podcast.
4. **Upgrade AI FinOps and then immediately undercut it in the Foundation's own words.** Named employers at real salaries, dozens not hundreds, and the governing body calling it "adapting classic FinOps practices". The undercut is more interesting than the upgrade.
5. **Keep the BCG caveats, add "more than half don't redirect it into strategic work"** (measured, not inferred), and consider one sentence of the Section counter-figure.

## Angles this opens

- **The 26–30% verified-success rate is a piece on its own**, and it is a Trust Boundaries piece rather than a Shape-of-Work one: the vendor published the miss rate for its own agent and nobody read it. Pairs with the 13.6% / 89% asymmetry in `research_auto-mode-default_2026-08-10.md` — same vendor, same disclosure habit, same silence in response.
- **"A discipline whose billing standard cannot yet represent its core unit"** connects straight to the Wednesday register argument: the scope of the instrument decides what it can ever see. FOCUS cannot see tokens; the NSW register cannot see supplier AI. Same failure, two domains. Worth a note before it gets spent casually.
- **The provenance chain on the lawyer/engineer sentence** — comment → brief → signal note → draft, in eleven days — is the cleanest worked example of the laundering failure mode yet, and it happened inside this pipeline. Belongs in `feedback_brief_claim_provenance.md`.
