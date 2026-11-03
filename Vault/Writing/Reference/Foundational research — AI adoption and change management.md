---
date_first_seen: 2026-08-16
date_updated: 2026-08-16
type: reference
source: 35-item reading list supplied by LK
threads: ["Adoption and Change", "Shape of Work-to-Come"]
status: signal
---

# Foundational research — enterprise AI adoption and change management

An annotated pass over the 35-source reading list, graded for provenance. **The headline finding
is uncomfortable: 22 of the 35 are vendor content marketing or SEO filler with no evidence in
them at all.** Four carry original reporting or original data. The rest are frameworks worth
knowing and worth citing to their originals rather than through these intermediaries.

Grades used throughout:

- **PRIMARY** — original reporting or original data collection
- **PRACTITIONER** — informed experience, no new data
- **VENDOR** — content marketing for a product, whatever the letterhead says
- **THIN** — SEO filler, recycled claims, nothing to check

Companion file: [[ADKAR and Kotter — a provenance file]], which takes the two frameworks that
dominate this list and traces them to source.

---

## The four worth citing

### Dastin, J. (2018). Amazon scraps secret AI recruiting tool that showed bias against women. *Reuters.*
`PRIMARY` · <https://www.reuters.com/article/us-amazon-com-jobs-automation-insight-idUSKCN1MK08G/>

Original investigative reporting, first to report, five anonymous sources. Edinburgh team of ~12,
building from 2014; **500 models**, one per job function and location, trained on **~50,000 terms**
from ten years of résumés; output was a 1–5 star rating explicitly modelled on Amazon product
reviews. The corpus was overwhelmingly male, so the system taught itself male candidates were
preferable — it **penalised the word "women's"** and downgraded graduates of two all-women's
colleges. Identified by 2015, patched, team disbanded by early 2017.

**Three things people get wrong.** (1) Amazon says on the record the tool **was never used to
evaluate candidates**, and no candidate is known to have been rejected by it — "Amazon's AI
rejected women" is not what the article supports. (2) It failed **as much for returning near-random
results** as for bias; the bias-only telling is a simplification. (3) It is eight years old and
describes pre-LLM ML. Attribute as Reuters' reporting, not as established fact.

### Ross, C., & Swetlitz, I. (2017). IBM pitched its Watson supercomputer as a revolution in cancer care. It's nowhere close. *STAT.*
`PRIMARY` · <https://www.statnews.com/2017/09/05/watson-ibm-cancer/>

Firsthand observation — the reporters sat in on an MSK/IBM bladder-cancer training session — plus
dozens of interviews. **MD Anderson spent >$60M over three years** before shelving the project amid
allegations of overspending and procurement violations. The load-bearing finding: MSK physicians
manually fed Watson how patients *should* be treated, and the training "does not teach Watson to
base its recommendations on the **outcomes** of these patients, whether they lived, or died." It
encodes a handful of doctors' preferences, not survival data. **50+ hospital agreements, only a few
dozen actual adoptions.** A Danish hospital dropped it after finding **33% concordance** with local
doctors.

**Do not conflate this with the 2018 piece.** The famous "unsafe and incorrect" treatment
recommendations phrase comes from Ross & Swetlitz, 25 July 2018, built on leaked IBM internal
slides — a different story. The 2017 piece claims absence of evidence of benefit, **not proof of
harm**. Watson Health was sold to Francisco Partners in 2022; present this as history.

### Brodsky, S. (2024). The hidden costs of AI. *IBM.*
`VENDOR`, with original survey data underneath · <https://www.ibm.com/think/insights/ai-economics-compute-cost>

Reports IBM's own IBV survey: **average cost of computing expected to climb 89% between 2023 and
2025**; **70% of executives** cite generative AI as a critical driver; and **every executive**
surveyed reported cancelling or postponing at least one gen-AI initiative on cost. Useful cost-driver
taxonomy (compute, training, inference, hardware, model complexity, energy).

**Caveats that must travel with it.** Every headline number traces to one IBM survey with **no
disclosed sample size or methodology**, and a 100% finding almost always means a small or filtered
sample. The article ends in watsonx and IBM Consulting — IBM sells the fix. The 89% is a forecast
published Oct 2024 for a window that has now closed and that nobody has retrospectively checked.
Cite as "IBM projected in late 2024," never as a current cost fact. No training-vs-inference split
is given, which is the number that would actually matter.

### Chinoy, H., & Liu, A. (2024). Measuring gen AI success: A deep dive into the KPIs you need. *Google Cloud.*
`VENDOR`, but the most reusable framework in the set · <https://cloud.google.com/transform/gen-ai-kpis-measuring-ai-success-deep-dive>

A five-layer KPI taxonomy with ~50 named metrics: **model quality** (computation-based for bounded
outputs; model-based auto-raters for unbounded — coherence, groundedness, instruction-following);
**system quality** (deployment, reliability, throughput/utilisation); **business operational**
(containment rate, average handle time, CSAT, document processing time); **adoption** (rate,
frequency, session length, thumbs up/down); **business value** (productivity, cost savings,
innovation, CX, resilience).

Genuinely well-structured, and the cost-savings sub-layer maps directly onto a cost framing. Two
caveats: Google Cloud sells the platform being measured, and the framing does quiet work for it
(self-hosted models "require a wider range of system quality metrics," managed Gemini handles them
"for you") — strip that when reusing. And it cites a 2,500-leader survey **without reporting a
single finding from it**, using the sample size as a credibility marker. Also note it predates
mainstream agentic deployment: **no agent-specific metrics** (task completion, escalation rate,
tool-call cost per resolution). That gap is an opportunity, not a defect to complain about.

---

## Worth reading, not worth citing

### Cloud Security Alliance (2025). Navigating the Human Factor: Addressing employee resistance to AI adoption.
`PRACTITIONER` · <https://cloudsecurityalliance.org/artifacts/navigating-the-human-factor>

The best-sourced synthesis on the list and the one that most looks like primary research without
being it. 22 pages, lead author Kurt Seifried, 11 named reviewers, **no survey, no sample, no
original data**. Its value is as a bibliography: EY (75% of employees concerned AI could make jobs
disappear; 65% anxious about their own), Workday (72% of leaders say their companies lack the
skills to implement AI responsibly; only 34% of people managers feel equipped), ADP Research (~21%
of organisations had trained staff on AI tools as of early 2024). **Chase each to its origin and
cite there.** Two defects: it repeats the 70% change-failure statistic sourced to McKinsey (see the
provenance file — the statistic is unsourced), and it cites "70–80% of AI projects fail" to a **PMI
blog post**. A blog citing a blog on a standards body's letterhead. The PDF also carries sponsor
advertising.

### MLOps Community (2025). The challenge with AI voice agents. *YouTube.*
`PRACTITIONER` · <https://www.youtube.com/watch?v=IuRlGCBSqR8>

Paul van der Boor (VP AI, Prosus) and Floris Fok, on the record about their own failures. The most
honest engineering content on the list and the only source here describing what actually breaks in
production. Failure modes, first-hand: **hallucination regresses in voice** ("this thing we kind of
solved in LLMs, in the voice model world, boom, back"); **language bleed** — a Portuguese session
hits one English term and never comes back; **turn detection is per-person and untunable globally**,
so slow speakers trip end-of-turn and back-channel "yeah/okay" reads as an interrupt; **tool-call
dead air**, mitigated by narrating the call and banning slow tools; **spelling** — voice agents
cannot reliably capture a name, worked around by narrowing to a shortlist first; and
**overconfidence** — the model never says "can you repeat that."

Real technique worth stealing: they used the Realtime API to test the Realtime API, generating
hundreds of synthetic callers randomised across accent, speed and emotion, because no eval framework
existed. Named deployments: iFood (rider voice in traffic noise, colloquial Brazilian Portuguese),
Cordi AI (ED call triage). Caveats: **zero measured numbers** — no error rates, no call volumes, no
latency budget; Prosus is an investor in several companies praised; and it is pinned to early-2025
Realtime API behaviour, now 18 months stale.

### Rajadurai, J., Fulton, T., & Haldipur, P. (2025). From delays to precision. *Infosys Knowledge Institute.*
`PRACTITIONER` with original survey data · <https://www.infosys.com/iki/perspectives/ai-optimizing-last-mile-deliveries.html>

Two things here exist nowhere else: an Infosys survey finding that **firms with training processes
see AI success 18 percentage points higher**, and a client case where a delivery-prediction platform
cut end-to-end latency from **15–17 minutes to 1 minute**. Both come with problems — the survey
ships with **no n and no field date**, and the ~15x latency improvement has **no named client** and
comes from the vendor that sold the platform. The "$197,730 annual cost of failed deliveries" is
Infosys's own arithmetic off a $17.20 per-failed-delivery figure, not a measured result; it will get
quoted as a finding. Page published 2025-04-23 but **last modified 2026-06-15** — archive anything
you quote.

### Moltke, N. von (n.d.). How to conduct a change readiness assessment. *AIHR.*
`VENDOR`, best third-party sourcing on the list · <https://www.aihr.com/blog/change-readiness-assessment-template/>

Cites **EY and Saïd Business School (2024): 96% of transformation programmes face barriers** — the
freshest genuine third-party citation anywhere in these 35 — plus Gartner (2023) on 82% of HR
leaders believing managers are not equipped to lead change, and 77% reporting employee fatigue. The
readiness-assessment structure is decent scaffolding. **The trap:** its "4X higher completion rates"
claim sits in the same visual register as the Deloitte and Gartner stats but is AIHR marketing its
own product, with no methodology and no comparison group. Note also its seven assessment dimensions
are ADKAR relabelled, not independent.

### Salian, U. (2024). Leveraging ADKAR for successful AI adoption. *Marg Online.*
`VENDOR` · <https://margonline.com/blog/leveraging-adkar-for-successful-ai-adoption/>

Included only because it contains the clearest self-inflicted wound on the list. It cites Prosci for
**"~48% of respondents currently use AI tools"** (n=200+ practitioners) and, two paragraphs later,
**"over 80% of professionals are leveraging AI"** (no sample, no study, no date) — and never
reconciles them. Cite either without the other and you are quoting a piece that contradicts itself.
Marg Online **sells Prosci certification**: a Prosci reseller citing Prosci's own surveys to prove
you need Prosci training. The one usable figure is the **679-participant Prosci study** finding 60%
forecast significant gen-AI disruption — chase it to Prosci.

---

## Frameworks, restated — cite the originals instead

These take a change model and swap "AI" into the nouns. None adds evidence. Listed so the reading
list stays complete and so the pattern is visible.

| Source | Grade | The one-line verdict |
|---|---|---|
| Creasey, T. (2025). *Mapping AI adoption research insights to ADKAR.* LinkedIn | `VENDOR`* | Prosci's Chief Innovation Officer on whether Prosci's model fits AI. Not a neutral analyst — the person whose company's revenue depends on the answer being yes. **Unfetchable; graded from authorship.** |
| De Sousa, P. (2025). *Driving AI adoption: A natural alignment with the ADKAR model.* LinkedIn | `THIN`* | "Natural alignment" is a fit argument, not an outcome argument, and fit arguments carry no numbers. Zero search footprint. **Unfetchable.** |
| Ströhfeldt, C. (2025). *ADKAR, AI, and the 'D' that demands our attention.* LinkedIn | `VENDOR`* | Published under a consultancy's company newsletter. The "Desire is where AI adoption dies" thesis is the most interesting idea in this group **and it is wrong** — see the provenance file, §Desire. **Unfetchable.** |
| Dworniczak, M. (2025). *Kotter's change model 2025: Still relevant in digital.* LinkedIn | `THIN`* | "Is X still relevant in [year]" is an SEO template, not a research question. **Unfetchable.** |
| YouAccel (n.d.). *Adapting Kotter's change model for AI and automation.* | `THIN` | Gated course lesson. Every number is borrowed and stale: McKinsey 2018 "up to 20% cash flow" (a *modelled simulation*, "up to" as a result), **WEF 85M/97M jobs by 2025 — a 2020 forecast whose target year is now in the past**, PwC 2019 "74% willing to retrain" (stated willingness, not behaviour). One "30% processing reduction" with no attribution at all. |
| IBM (2025). *How AI-focused change management can build trust.* | `VENDOR` | **Zero statistics in the body.** Sources its framework to an IBM white paper. Funnels to watsonx.governance. There is literally nothing in it to cite. |
| Ikigai Colors (2024). *AI and change management: A practical framework for leaders.* | `THIN` | Kotter with "AI" swapped into the nouns. Sole named source is *Leading Change*, cited without a date. |
| Nasstar (2024). *Navigating AI & change management.* | `VENDOR` | One statistic — "a Forbes survey" says 56% use AI for customer experience — with no instrument, sample or fieldwork date, and irrelevant to the article's own thesis about resistance. A credibility prop. |
| Cprime (n.d.). *Change management in AI adoption.* | `THIN`/`VENDOR` | No statistics at all. One client case cited as **"1100% growth"** with no baseline and no definition of what grew. Modified four days ago — an actively groomed SEO asset. |
| Allganize (2025). *Resistance to AI: Governance and cultural challenges.* | `VENDOR` | Repeats the 70% change-failure figure **and** the expired WEF 2025 forecast. Diagnoses a data-escape problem, then sells a self-hosted air-gapped deployment as the fix. Page carries 2026-04-27, not the 2025-06-07 on the reading list — refreshed and redated. |
| Attupurathu, J. (2025). *Organizational resistance to AI.* LinkedIn | — | **Unfetchable. Ungraded. Do not cite.** |
| Garg, N. (n.d., actually 2024-05-03). *5 steps to overcome employee resistance.* uKnowva | `VENDOR` | The only two numbers are marketing claims about the author's own HRMS ("15 hours → 15 seconds"). |
| Schwartz, Z. (2024). *Overcoming resistance to AI adoption.* Scout | `VENDOR` | Prestige-by-hyperlink: WEF, HBR, McKinsey and MIT Sloan all linked with **no number, sample or study name attached** — and LinkedIn posts cited as peers. Not one statistic in the piece. |
| Marr, B. (2024). *11 barriers to effective AI adoption.* Forbes | `PRACTITIONER` | A usable taxonomy of barrier categories and **zero evidence**. Note it is `forbes.com/sites/` — contributor content, no fact-checking desk. The byline does work it has not earned. |
| Miesbauer, J. (2025). *Barriers to AI adoption.* Agiloft | `VENDOR` | Substantially Marr's list unattributed, then pitches Agiloft's CLM platform as the resolution. One external source in the whole piece: a blog. |
| Agility at Scale (2025). *From pilot to production.* | `THIN` (high end) | Well-organised SEO pillar page, zero original data — but a useful **citation trail** to IDC/Lenovo and McKinsey. Two defects: the hero converts IDC's "88% of *POCs* don't reach *widescale deployment*" into "88% of *pilots* never reach *production*," a stronger claim; and the page says 88% in the hero and 80% in an H2, splitting the difference as "80-88%" — two unrelated studies stapled together. Page was rewritten in 2026 despite the 2025 date on the list. |
| Paige, E. (2025). *Stop running pilots that stall.* Bain Squared | `THIN` | **"Bain Squared" is not Bain & Company** — an unrelated Singapore boutique with no About page and no named leadership. Asserts "most AI pilots never scale" with **no source at all**. The name similarity plus a strategy post on AI pilots is a trap; if it is ever mentioned, name the confusion explicitly. |
| DeMent, Kerner & Hosken (n.d.). *Launching a successful AI pilot program.* ScottMadden | `PRACTITIONER`/`VENDOR` | **No statistics whatsoever**, which is notable given the topic. One reusable idea: engage Legal, IT, Controls and HR *before* the build. (The list spells it "Dement"; the firm spells it **DeMent**.) |
| Hilgers, L., & Roback, M. (2025). *7 ways Agentic AI pilots get stuck.* Salesforce | `VENDOR` | The archetype. Deploys MIT NANDA's 95%, then two "independent" studies (Futurum, Valoir) that are analyst shops in the vendor-commissioned-research business, then MIT's build-vs-buy finding repurposed as a direct argument for Agentforce — "ROI in four to six weeks vs six to 12 months," "20% less," "16x faster," "70% greater accuracy." Every number bends one way. Useful only as a **datable specimen of how the MIT number gets used commercially.** |
| Toleti, R. (2025). *Why AI must solve its 'last-mile integration' problem.* Built In | `VENDOR` in practitioner clothing | **The undisclosed conflict is the story.** Built In gives his name and headshot and **no affiliation**; Raj Toleti is Chairman/CEO of **Andor Health**, which sells a platform for embedding AI into clinical workflows. Andor's own newsroom carries the same thesis *with* the affiliation attached. Zero verifiable claims anyway. |
| Dhruv, S. (2025). *AI agent technology stack.* Aalpha | `THIN` | Roughly 60% of its figures carry **no attribution at all** — "42% of EU hospitals use AI agents for diagnostics," "95% of routine patient inquiries," "80% of banks." Exactly the kind of number that gets laundered into a piece and cannot be traced. Do not cite any percentage from this page. |
| Gosden, M. (2024). *Deploying AI agents — a practical guide for FS leaders.* LinkedIn | — | **Unfetchable.** LinkedIn Pulse has no editorial layer and the author can silently edit or delete it — a poor citation target on principle. |
| Sumrak, J. (2025). *AI voice agents.* AssemblyAI | `VENDOR` | Competent technical content marketing. The **cascading vs end-to-end vs hybrid** taxonomy and the auditability trade-off are genuinely useful scaffolding. Every comparative number is a sales claim (4x price advantage over OpenAI Realtime; benchmark wins over Deepgram/ElevenLabs/Google), and the McKinsey and Salesforce stats are unlinked — a vendor citing a consultancy is the laundering pattern itself. The "~1 second round trip" is a target that will read as a measurement. |
| Verma, S. (2025). *40+ AI voice agent use cases by industry.* Biz4Group | `THIN` | One real citation (Gartner: 70% of customer service journeys begin with conversational AI by 2028) used as credibility cover for 40+ unsourced assertions. The two "case studies" are Biz4Group's own products. |
| Reji, B. (2025). *AI job loss: 40% of roles at risk.* Economic Times | `THIN` | See below — this one earns its own entry. |
| Brainy Quote (n.d.). *Jaan Tallinn quote.* | `THIN` | See below. |

\* Graded from authorship and format; body text could not be retrieved (LinkedIn Pulse blocks
automated readers). Open in a browser before citing anything from these four.

---

## Two entries that need saying out loud

### The 40% figure is not what the headline says

Reji, B. (2025). *AI job loss: 40% of roles at risk, experts warn.* The Economic Times.
<https://economictimes.indiatimes.com/tech/artificial-intelligence/ai-job-loss-40-of-roles-at-risk-experts-warn/articleshow/120894138.cms>

**The 40% is UNCTAD's**, from the *Technology and Innovation Report 2025* (April 2025). UNCTAD's
exact wording is **"AI could impact 40% of jobs worldwide."** The operative verb is **impact**, and
UNCTAD attaches **no time horizon at all**. ET's headline converts that to "at risk"; a reader hears
"destroyed." That is the modal-verb drop with an extra step.

The piece has at least three further defects. It cites McKinsey for "400–800 million jobs displaced
**within five years**" — the underlying source is *Jobs Lost, Jobs Gained* (2017) and the figures
are **by 2030**, under a rapid-adoption scenario; ET names neither the report nor its year. It says
Gates, Altman **and Sundar Pichai** signed an open letter comparing AI to pandemics and nuclear war
— that is the Center for AI Safety statement of 30 May 2023, **Pichai did not sign it**, and ET also
conflates it with the separate March 2023 Future of Life pause letter. And it presents vendor
surveys from SEO.ai (an AI copywriting company) and SnapLogic as equivalent in weight to UNCTAD and
NBER.

**Cite UNCTAD TIR 2025 directly, say "impact," and state that no horizon is attached.**

### The Tallinn quote has no provenance

Brainy Quote (n.d.). <https://www.brainyquote.com/quotes/jaan_tallinn_818388>

The text on the page: *"Building advanced AI is like launching a rocket. The first challenge is to
maximize acceleration, but once it starts picking up speed, you also need to focus on steering."*
Attribution given: "Jaan Tallinn." That is the entirety of the provenance — no source, no date, no
interview, no talk.

**The primary source could not be confirmed.** Targeted searches for the verbatim string, for the
metaphor plus Tallinn, and against Edge.org, CSER and FLI returned only BrainyQuote and one
downstream scrape of it. Tallinn is a Skype co-founder and a founding funder of CSER and FLI, so the
sentiment is entirely in character — which is exactly what makes it dangerous. Note too the
rhetorical shape: "maximise acceleration, then steer" is a **sequencing** argument that reads as
build-first-align-later, roughly the opposite of Tallinn's public position. If the idea is wanted,
quote a Tallinn source that can be pointed at.

A piece about provenance discipline that opens on a BrainyQuote epigraph would be the story.

---

## What the list is actually evidence of

Read as a corpus rather than a bibliography, these 35 sources are a clean specimen of the thing
worth writing about. The pattern repeats with almost no variation:

1. **Name a barrier** — resistance, culture, data quality, last-mile integration, pilot stall.
2. **Attach a percentage** borrowed from a consultancy, a vendor survey, or another blog.
3. **Sell the fix for the barrier you just named.** Allganize describes data escape and sells
   air-gapped hosting. Agiloft describes AI barriers and sells CLM. IBM describes runaway compute
   cost and sells Granite as the cheaper model. Salesforce describes pilots getting stuck and sells
   the platform that unsticks them. Andor Health's CEO describes a last-mile problem in an article
   that does not mention he runs a last-mile company.

Nobody in that chain lied. Every step was a reasonable citation of the previous step. That is
the whole point — and it is the same mechanism traced in [[ADKAR and Kotter — a provenance file]],
where a statistic makes it from a 1993 book that called itself unscientific into a peer-reviewed
nursing journal in 2019 without ever acquiring a study.

## Feeds

- [[Adoption and Change]]
- [[Shape of Work-to-Come]]
