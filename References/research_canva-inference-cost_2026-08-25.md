# Research note — Canva's AI inference cost disclosure and its remedies
**Compiled:** 25 August 2026
**For:** Lars Klander / Substack (cybersecurity · AI governance · cost-and-economics)

---

## Bottom line (five sentences)

In early August 2026 Canva told shareholders it had cut its 2026 revenue-growth forecast from about 30% to about 20% — a one-third cut — because the average cost of serving an AI task was, in CEO Melanie Perkins' words, "too high," and because the company had been "relying too heavily on frontier models." The remedy Canva claims is already delivered, not aspirational: roughly a **90% reduction in cost per AI task** since Canva AI 2.0 launched in April 2026, achieved principally by substituting in-house models (largely Leonardo.Ai lineage) for frontier-vendor APIs. That number is a **per-task unit cost**, not total spend — Canva also says users now create **3x more designs**, so the absolute inference bill almost certainly rose even as unit cost fell, and no primary source anywhere discloses Canva's total inference spend in dollars. The financial consequence is real and third-party-verifiable: Blackbird and AirTree marked Canva down from US$42bn to US$34.9bn on 14 August 2026, Canva's own independent valuer went to US$31bn, and the IPO slipped to 2027. The sovereignty hook exists but is thinner than it looks: Canva is a shareholder in and SEC-filing-named "lighthouse customer" of Australian sovereign-GPU neocloud Sharon AI, yet Canva's own product-level data residency still offers **only US and EU — not Australia** — which is the more interesting governance story.

---

## 1. What was actually announced

### 1a. The core disclosure — Canva's H1 2026 shareholder update (~3–5 August 2026)

**Channel.** This was **not** a press release, a blog post, or a keynote. It was a **shareholder/investor update**, leaked to and reported by *The Information* and the *Australian Financial Review*, then picked up by Startup Daily (5 Aug), AI Weekly (6 Aug), Fortune (12 Aug). Canva subsequently **confirmed the substance on the record by email to Fortune** (12 Aug). There is no Canva newsroom post about any of this — I checked canva.com/newsroom; the August items are Canva Grow 2.0, Canva Code 2.0, Gemini integration, and an "AI Vision Sydney 2026" recap. **This matters: the disclosure lives entirely in investor and journalist channels, never in Canva's own public-facing publishing.**

**Verbatim, attributable to Melanie Perkins (CEO & co-founder):**

> "This validated the demand, but also showed us we needed to reduce the cost of completing an AI task to support a broad rollout. Rather than broadly rolling out a product before the underlying economics were ready, we decided to slow the rollout while we rebuilt the architecture, reduced unit costs and strengthened the business model."
> — email statement to *Fortune*, published 12 August 2026

Also attributed to Perkins from the shareholder update (via Startup Daily, 5 Aug 2026), in fragments rather than full sentences:

> "average cost of serving an AI task was too high"
> "relying too heavily on frontier models"
> "deliberate decision to get the economics right"
> "This slowed our distribution and impacted our near-term growth"
> "While this is strong growth at our scale, we want to acknowledge it is below the ambitious goal"

Perkins also said user demand for the AI features had **"significantly exceeded"** projections (to *Fortune*, 12 Aug 2026).

### 1b. The figures Canva actually disclosed

| Figure | Value | Source | Status |
|---|---|---|---|
| 2026 revenue-growth forecast | cut from ~**30%** to ~**20%** | Shareholder update, Aug 2026 | Company-disclosed |
| Reported-quarter revenue | **US$921.9m**, +**25.2%** YoY | Shareholder update | Company-disclosed |
| ARR (end 2025) | **US$4bn** | Obrecht to TechCrunch, 18 Feb 2026 | Company-disclosed |
| Cost **per AI task** | down **~90%** since Canva AI 2.0 (April 2026) | Shareholder update; repeated by Perkins, Obrecht, and Blackbird's Rick Baker | Company-claimed |
| Design volume | **3x** more designs vs previous AI version | Shareholder update / Fortune | Company-claimed |
| Cash | **US$1.47bn** | Shareholder update | Company-disclosed |
| Profitability | profitable **9 consecutive years** | Shareholder update | Company-claimed |
| MAU / paid | **265m** MAU, **31m** paid | Canva, Feb 2026 | Company-disclosed |
| Feature slippage | some features **up to 6 months behind schedule** | The Information, via AI Weekly 6 Aug 2026 | Reported |

**Named in-house model economics** (from the shareholder update, reported by Startup Daily 5 Aug and Startup Fortune 13 Aug — two outlets, same underlying document, so treat as one source):

- **Lucid Origin** (image): **30x cheaper, 5x faster** than frontier alternatives
- **Image-to-video model**: **17x cheaper, 7x faster**
- **Proteus** (style transfer): **23x cheaper, 2x faster**

⚠️ These are **Canva's own unbenchmarked comparisons against unnamed "frontier alternatives."** No methodology, no named comparator, no third-party verification. Use as "Canva claims," never as fact.

### 1c. The second disclosure — Cliff Obrecht at Stripe Tour Sydney, 19 August 2026

Reported by Forbes Australia. This is the most quotable material and the most technically specific:

> "When we launched, or tried to launch, our AI product at Canva Create in April, we launched with a lot of frontier intelligence."

> "They were amazing at what they did, but they were also very expensive…"

> "To serve 200-plus million users, a very generous free AI product comes with a huge cost, and so we needed to get that cost down."

> "We've managed to do that by about 90 per cent, which means we can really scale it up now."

> **"The cost of good to serve a user has gone from cents per month to now many, many more cents per month."**

That last quote is the single most useful line in the whole corpus for a cost-and-economics writer, and I want to flag exactly why: **it is an admission that COGS per user went UP, in the same breath as the 90% cost-cut claim.** "Cents per month" → "many, many more cents per month" is Canva's own framing of a multiple-x increase in per-user serving cost, post-optimisation. The 90% figure and the "many, many more cents" figure are not in conflict — one is per task, one is per user, and volume ate the savings. Anyone printing the 90% without that pairing is printing half the story.

### 1d. What is journalist inference, not Canva disclosure

- **"Protecting profitability ahead of a 2027 IPO"** — Fortune's inference. Canva did not say this.
- **"Via routing changes"** — Dealroom's characterisation of the 90% cut. Canva has not described model routing anywhere I can find. See §2.
- **"ChatGPT competition"** as a co-cause of the downgrade — The Information's framing, echoed by Dealroom. Not in Canva's confirmed statements.
- **The valuation markdowns** are third-party fund marks, not Canva statements (see §4).

---

## 2. The remedies — tagged

| # | Remedy | Status | Date | Evidence quality |
|---|---|---|---|---|
| 1 | **Substituting in-house models for frontier APIs** | **SHIPPED** | Oct 2025 → Aug 2026 | Strong. Multiple primaries. |
| 2 | **Slowing / staging the AI rollout until unit economics work** | **SHIPPED** (it's the whole story) | April–Aug 2026 | Strong. Perkins on record. |
| 3 | **Rebuilding "the architecture"** | **CLAIMED SHIPPED, undescribed** | ~May–Aug 2026 | Weak. Zero technical content. |
| 4 | **Preferring retrieval/adaptation of existing library designs over fresh generation** | **SHIPPED** | reported 19 Aug 2026 | Medium. Single source (Forbes AU on Obrecht). |
| 5 | **Weekly unit-economics review of each AI tool** | **SHIPPED** (process, not tech) | reported 19 Aug 2026 | Medium. Single source. |
| 6 | **140-person AI research team building models in-house** | **SHIPPED** | reported 19 Aug 2026 | Medium. Single source. |
| 7 | **Leonardo.Ai acquisition as the model-building substrate** | **SHIPPED** | acquired 29 July 2024 | Strong. Businesswire primary. |
| 8 | **Investment in + consumption of Sharon AI GPU capacity** | **SHIPPED (investment); CONTESTED (inference workload)** | Dec 2025 investment; "major customer" by ~Feb 2026 | Mixed — see §6. |
| 9 | **Pricing/packaging shifting cost to users ("AI Pass," ~US$100/user/mo)** | **UNVERIFIED** | — | Weak. One secondary source. |
| 10 | **Model routing / cascading** | **NOT ESTABLISHED** | — | No Canva source. Journalist gloss only. |
| 11 | **Caching / dedup / batching / quantisation** | **NOT ESTABLISHED** | — | No source at all. |
| 12 | **On-prem / own GPU fleet / custom silicon** | **NOT ESTABLISHED** | — | No source at all. |

### Detail on the ones that hold up

**#1 — In-house models.** The strongest primary is Stef Corazza, Canva's Head of AI Research, quoted in diginomica (published 16 March 2026):

> "Initially, we were using an OpenAI model. We realized it was slow, very expensive. We developed our own model. It's like, two times faster and three times cheaper…"

> "…design, it's a very specific area, and so if you can fine-tune the model for the specific use case, you're massively outperforming them in quality, speed, and also in cost."

**Check the dates carefully — there is a chronology here worth using.** Corazza's "2x faster, 3x cheaper" is from **March 2026**. The shareholder-update claims of "30x cheaper" (Lucid Origin) and "17x cheaper" (image-to-video) are from **August 2026**. Either different models are being compared, or the comparators differ, or the improvement genuinely compounded ~10x in five months. Canva has not reconciled them. **Do not blend these numbers.**

The Canva Design Model itself launched **30 October 2025** (TechCrunch), not April 2026 — a distinction several secondary outlets get wrong. Canva AI 2.0, the agentic product built on top, launched **16 April 2026** at Canva Create.

**#3 — "Rebuilt the architecture."** This is Perkins' phrase and it is doing enormous unexamined work. Canva has published **nothing** describing what was rebuilt. See §3.

**#4 — Reducing generation volume at the product surface.** Per Forbes Australia's account of Obrecht's Stripe Tour remarks, Canva now prefers **adapting an existing design from its library over generating a new one**. This is the most interesting remedy in the list and the least covered: it is a *product-design* answer to an inference-cost problem — retrieval instead of generation. It also has a governance dimension nobody has written about (see §6).

**#9 — Pricing.** AI Weekly's summary of The Information mentions "AI Pass" at **US$100/user/month** and that "pricing and usage controls hadn't caught up with demand." I could **not** corroborate an AI Pass SKU on Canva's own pricing pages or newsroom. Treat as unverified. The verified pricing history is older: Canva raised Teams subscription prices in **September 2024**, explicitly citing AI features (Fortune, 3 Sep 2024) — that is a 2024 datapoint and must not be presented as a response to the 2026 cost crunch.

---

## 3. The engineering detail — and its conspicuous absence

**This is a finding, not a gap.** I searched canva.dev/blog/engineering comprehensively, including the `machine-learning`, `machine-learning-infrastructure`, `deep-learning`, and `infrastructure` tag pages.

- The **only** GPU-infrastructure post is *"Supporting GPU-accelerated Machine Learning with Kubernetes and Nix"* by Jonathon Belotti — **5 July 2022**. Four years old, pre-dates all of this.
- The `machine-learning` tag's most recent post is **21 June 2024** ("How we see groups in design").
- The most recent AI-adjacent posts are consumer-facing or recruiting-facing: "Behind the scenes of Canva's DesignDNA campaign" (24 Feb 2025), "Image replacement in Canva designs using reverse image search" (28 Jan 2025), and two posts about using AI in job interviews (11 June 2025, 20 Oct 2025).
- The most recent engineering post generally is "Session revocations at scale" (22 July 2026) — backend, not ML.

**There is no Canva engineering-blog post about inference cost, GPU utilisation, model serving, cost per request, or their ML platform, at any point during the period covered by these claims.** A company that says it cut per-task inference cost by 90% by "rebuilding the architecture" has published zero engineering detail about how. Every technical claim in this story is made in an investor update or from a conference stage, to audiences who cannot interrogate it.

The only genuine technical substance anywhere is Corazza's:
- Canva runs a single internal file format, **CDF**, across all media types: *"Everything that you see on a Canva platform, it's one file format called CDF…"*
- The models are **fine-tuned on that design corpus**, and trained with **reinforcement learning from observed user editing behaviour** in the editor: *"Our key competitive advantage is we generate editable, multimodal designs, all in one editor, and then we get direct feedback from our users, from that editor."*
- The output is **layered and editable**, not flat pixels — which is the actual technical reason a small specialist model can beat a frontier omni-model here.

No model sizes. No parameter counts. No GPU counts. No hardware. No latency figures. No serving stack. No utilisation numbers.

---

## 4. The financial frame

**Scale (company-disclosed).** US$4bn ARR at end-2025; US$500m of that from B2B (25+ seat accounts), growing 100%; 265m MAU; 31m paid users; US$1.47bn cash; profitable nine years running. Obrecht, Feb 2026: *"We're becoming an AI platform with a bunch of design tools. So you can think of it more like a cursor for design."*

**Gross margin: not disclosed.** Canva is private and has never published a gross margin. Anyone quoting one for Canva is estimating. This is precisely why the Figma comparison in §5 does the analytical work Canva's own numbers can't.

**Materiality — yes, demonstrably.** The clearest evidence is not a cost line, it is the valuation:

| Mark | From | To | Who | Date |
|---|---|---|---|---|
| VC fund marks | US$42bn | **US$34.9bn** (−US$7.1bn, −17%) | Blackbird + AirTree | 14 Aug 2026 (AFR, Rapaport & Smith) |
| Canva's own independent valuer | US$38.9bn | **US$31bn** (−US$7.9bn) | employee share issue valuation | Aug 2026 |
| Secondary market | — | **~US$30bn** | Hiive (broker) | 2026 |

Blackbird partner **Rick Baker**, on the record: *"They've now managed to bring down costs of serving AI by 90%."* — investor commentary corroborating the company line, from a party with an obvious interest in the mark holding up. **Name that interest if you use the quote.**

**IPO.** Pushed to **2027** (from an expected 2026), reported 17 Aug 2026, with AI cost restructuring cited. Canva declined to comment on valuation. **No S-1, no registration statement, no IPO-related regulatory disclosure exists.** Everything financial here is a leaked private shareholder update plus fund NAV marks.

**The unit economics, stated plainly.** Per-task cost down ~90%. Design volume up 3x. Per-user COGS up from "cents per month" to "many, many more cents per month." Growth guidance cut by a third. That is a company that won the engineering fight and still lost ground on the P&L, because demand elasticity ate the efficiency gain. It is the cleanest real-world instance I have found of Jevons paradox in inference spend at consumer scale.

---

## 5. The comparison set — Canva is representative, not exceptional

Two solid public-company primaries, both from the same fortnight, both saying the same thing:

**Figma (NYSE: FIG), Q2 FY2026 call, August 2026.** CFO **Praveer Melwani**, verbatim:
> "a clear set of tools to manage inference costs as adoption scales. We route across models based on task complexity, optimize across providers through our model-agnostic architecture."

> "We do not charge our customers for their usage of products that are currently in beta, and we bear the cost of inference without offsetting consumption revenue."

Figma is also *"beginning to bring first-party models trained on Figma's design corpus into specific design tasks"* to *"deliver comparable quality at lower cost and latency."* Numbers: revenue **US$370.1m**, +48%; gross margin **85%** (up 2.5pp); **free cash flow margin 14%**, down from a reported 27% in Q1, with Melwani naming *"costs related to our increased inference spend"* as the largest single variance. Note the modal precision — **"beginning to bring"** is not "has replaced."

**Duolingo (DUOL), Q2 2026 call, 5 August 2026.** CEO **Luis von Ahn**: Video Call inference cost fell from roughly **US$0.30 per call at launch to under US$0.01** — *"It is now under \$0.01 per Video Call. We don't see a loss in quality."* — attributed to *"a strategic shift to open-source large language models."* CFO **Gillian Munson**: *"We are seeing AI cost savings that will give us a bit structurally a better margin."* Full-year adjusted EBITDA margin guidance raised from ~25% to ~25.5%.

**Read across.** Figma is the near-perfect control: same category, same customers, same remedies (cross-model routing, provider optionality, first-party corpus-trained models), but public, so the numbers are audited. Duolingo shows the same playbook — flee frontier APIs for open weights — producing a **~30x** unit-cost improvement, which is the same order of magnitude as Canva's claimed 17–30x. **Canva's engineering claims are entirely plausible because two public companies independently report the same magnitude of gain from the same manoeuvre.** What makes Canva unusual is not the cost problem or the fix; it is that Canva let the cost problem visibly cut its *growth guidance* and its *valuation* — because as a private company it had no quarterly cadence forcing incremental disclosure, so it all landed at once.

I found no comparable hard inference-cost disclosure from Adobe, Notion, Shopify, or Zoom in this period. Do not include them.

---

## 6. The governance / sovereignty hook — real, but it cuts the opposite way

**What is solid.** Canva is an equity holder in and a named customer of **Sharon AI** (Nasdaq: SHAZ), an Australian "neocloud" whose explicit market position is **sovereign GPU compute in Australia**:

- Canva invested **US$23m** in Sharon AI's **US$103m pre-IPO convertible-note round, December 2025**; the notes converted in June 2026 to **406,000 shares at US$12.53**. Canva holds roughly **1%**. (Forbes Australia, Daniel Van Boom, 25 Aug 2026 — published today.)
- Sharon AI's **10-K for FY2025, filed 31 March 2026**, names **Canva as a "lighthouse customer"** with *"large, sophisticated AI and HPC requirements."* **This is an SEC filing — the single most legally-attested source in this whole note.** The same filing flags "significant customer concentration" as a risk.
- Sharon AI's Australian footprint: up to **54MW** secured from **NEXTDC** across Melbourne (M2, M3) and Sydney (S3, S6). A **50MW** expansion at NEXTDC M3 was announced **3–4 November 2025**, sized to house **20,000+ Nvidia B200/B300/GB300 GPUs**. As of 31 Dec 2025 only **411 GPUs** were actually live (43 A40, 192 L40, 160 H100, 16 H200), with 2,024 more (1,000 B200 + 1,024 B300) planned for 1H 2026. **The sovereign supercluster is mostly a construction schedule, not a running fleet.**
- The sovereignty framing is explicit and vendor-supplied. NEXTDC CEO **Craig Scroggie**: *"Sharon AI, in collaboration with Nvidia, is deploying sovereign, high-density GPU capacity engineered for AI at speed and scale."* Sharon AI CEO **Wolf Schubert** (13 Oct 2025): *"By combining SHARON AI's sovereign GPU cloud with the VAST InsightEngine we're creating the foundation for enterprises and government institutions to run cutting-edge AI workloads locally, securely, and without compromise."*
  **Commercial interest, stated: Sharon AI sells sovereign GPU capacity; NEXTDC sells the data centres; VAST Data sells the storage; Nvidia sells the silicon. Every sovereignty quote above is from a party paid to make sovereignty desirable.**

**What is NOT established — and this is the discipline point.** No primary source says **which Canva workloads run on Sharon AI, whether they are training or inference, or whether they run in Australia or Texas.** Forbes Australia, which broke the shareholding story today, explicitly does not say. On **20 August 2026** Sharon AI announced it had *"successfully delivered"* an AI cloud deployment across **multiple Australian data centres** for an unnamed *"global technology company with a major Asia-Pacific presence"* — contract value **~US$950m over five years**, revenue commencing Q3–Q4 2026, with James Manning quoted on execution. The inference that this is Canva is **strong but unconfirmed**, and I am not willing to assert it. If you want it, it is a phone call to Sharon AI IR, not a research finding.

**The genuinely publishable governance finding — and it is a better one.** Canva's *product-level* data residency, per its own help centre, is available **only for the United States and the European Union**, only on Enterprise/Campus/District plans, and covers designs, comments, media, folders, audit logs and search indexes. **Australia is not an available residency region for the Australian company's own customers.** Canva's own disclaimer, verbatim:

> "Data residency isn't a compliance solution. It can help support your internal data-hosting requirements, but you'll need to consult your legal or compliance team for guidance."

And the documentation **does not state whether generative-AI/ML processing is inside or outside the residency boundary at all** — the standard, and standardly unexamined, distinction between where data rests and where it is inferred over. For a piece about the December 2026 Australian Privacy Act automated-decision-making transparency obligations, that gap is the story: an Australian company, buying into Australian sovereign GPU capacity for cost reasons, that cannot offer Australian data residency to Australian customers, and whose residency documentation is silent on AI processing.

**The second-order sovereignty point, which nobody has written.** Remedy #4 — preferring **adaptation of existing library designs over fresh generation** — is a cost measure with a data-governance shadow. Retrieval-and-adapt means user-visible outputs are increasingly assembled from Canva's own corpus rather than synthesised. That changes provenance, changes what "generated" means for disclosure purposes, and changes what an ADM-transparency obligation would even have to describe. It is speculative as governance analysis but it is *your* speculation off a sourced fact, which is the safe form.

**Do not claim** that cost pressure is pushing Canva toward local or on-prem inference for sovereignty reasons. The evidence supports cost and capacity as the motive. Sovereignty is Sharon AI's sales pitch, not Canva's stated rationale, and Canva has never said a word about data sovereignty in connection with any of this.

---

## 7. SOLID / CONTESTED / UNVERIFIED

### SOLID — primary, on the record, safe to print
- Growth forecast cut ~30% → ~20% for 2026; cause given as AI serving cost. (Shareholder update, Aug 2026; confirmed by Perkins to Fortune 12 Aug 2026.)
- Perkins' "rebuilt the architecture, reduced unit costs" quote — verbatim, on the record, to Fortune, 12 Aug 2026.
- Obrecht's Stripe Tour Sydney remarks, 19 Aug 2026, including *"cents per month to now many, many more cents per month"* and the ~90% figure.
- Corazza's "2x faster, three times cheaper" than the OpenAI model they started on — diginomica, March 2026.
- Canva Design Model launched 30 Oct 2025; Canva AI 2.0 launched 16 Apr 2026.
- Leonardo.Ai acquired 29 July 2024 (Businesswire).
- US$4bn ARR, 265m MAU, 31m paid, US$1.47bn cash, nine years profitable.
- Blackbird/AirTree markdown US$42bn → US$34.9bn, 14 Aug 2026; internal valuer to US$31bn; IPO to 2027.
- Sharon AI 10-K (31 Mar 2026) names Canva a "lighthouse customer." Canva's US$23m stake, ~1%.
- Canva data residency = **US and EU only**, Enterprise-tier only, Australia not offered.
- Canva's engineering blog contains nothing on inference cost or model serving since 2022.
- Figma and Duolingo Q2 2026 inference-cost disclosures and quotes.

### CONTESTED — single-source, or company-claimed without verification
- **The ~90% per-task cost reduction.** Repeated by three parties (Perkins, Obrecht, Rick Baker) but all three trace to one internal Canva measurement. No definition of "task," no baseline, no methodology. It is a company claim, consistently repeated. Print it as such.
- **Lucid Origin 30x/5x, image-to-video 17x/7x, Proteus 23x/2x.** One underlying document, two outlets. No named comparator, no benchmark. Company claim.
- **"3x more designs."** Company claim, no baseline.
- **US$921.9m revenue, +25.2%.** Consistently reported but from a leaked private document; whether it is a quarter or a half-year is not resolvable from public sources. Flag the ambiguity if you use it.
- **The unnamed "global technology company with a major Asia-Pacific presence"** in Sharon AI's 20 Aug 2026 release (~US$950m/5yr, multiple Australian DCs) being Canva. Likely; unconfirmed.
- **"140-person AI research team"** and **weekly unit-economics reviews.** Single source (Forbes AU on Obrecht, 19 Aug 2026).
- **ChatGPT competition as a co-cause of the downgrade.** The Information's framing; not in Canva's confirmed statements.

### UNVERIFIED — do not print without further work
- **"AI Pass" at US$100/user/month.** One secondary source summarising a paywalled one. Not on Canva's pricing pages.
- **Features "up to six months behind schedule."** The Information, single source, uncorroborated.
- Whether Canva's Sharon AI consumption is inference or training.
- Whether it runs in Australia or Texas.
- Canva's gross margin, at any point. Never disclosed.
- Canva's absolute inference spend, in dollars, at any point. Never disclosed.
- Whether Canva's data-residency guarantee covers AI processing. Documentation is silent.

---

## 8. DO-NOT-PRINT LIST

1. **Any dollar figure for Canva's total AI inference bill.** I searched specifically for this. **No primary found.** No annual figure, no quarterly figure, no per-generation figure, no percentage of COGS or revenue. If you encounter one in circulation, it is fabricated or extrapolated. The absence is itself the story: Canva disclosed a *growth-rate consequence* and a *unit-cost improvement ratio* while disclosing **no absolute cost at all** — the classic shape of a disclosure engineered to be reassuring.

2. **"Canva cut its AI costs by 90%."** Wrong on two counts. It is cost **per AI task**, and total serving cost per user went **up** over the same window by Obrecht's own account. Always pair the two.

3. **"Canva moved its inference to Australian sovereign infrastructure."** Not established by any source. Canva is an investor in and named customer of a company that sells that; which workloads run where is unknown.

4. **"Canva built the world's first foundation model for design."** Canva's own newsroom superlative ("the world's first foundation model built to understand the structure, hierarchy, and complexity of real-world design"). Unverified, unverifiable as phrased, and Figma is doing materially the same thing. Cut it or attribute it explicitly as marketing copy.

5. **"AI costs wiped $10bn/$11bn off Canva's valuation."** Headline arithmetic combining different valuation marks set by different valuers on different dates against different baselines (US$42bn → US$34.9bn is the fund mark; US$38.9bn → US$31bn is the internal one; ~US$30bn is a secondary-market broker quote). Pick one pair, name the valuer, name the date.

6. **Canva's September 2024 Teams price rise as a response to the 2026 inference crunch.** That is a **2024** event. Chronologically impossible as a remedy for an April-2026 problem.

7. **"Canva uses model routing / caching / batching / quantisation."** No Canva source says any of this. Dealroom's "via routing changes" is a journalist's gloss. **Figma** says it routes across models — do not transplant Figma's disclosure onto Canva.

8. **Cryptobriefing.com's Canva/Figma piece** — it presents Canva's US$921.9m revenue figure inside a passage about Figma, and gives no attribution for its cost claims. Low-quality aggregator. Do not cite; I used it only to locate the Figma angle.

9. **Blending Corazza's "3x cheaper" (March 2026) with the shareholder update's "30x cheaper" (August 2026).** Different claims, five months apart, unreconciled by Canva.

10. **Any claim that Canva's 90% reduction is verified.** Every repetition, including Rick Baker's — an investor whose fund's mark depends on it — traces to Canva's own measurement.

---

## 9. Open questions worth a follow-up

1. **What is Canva's absolute inference spend?** The single most valuable unknown. Likely to surface only in an S-1 in 2027.
2. **What was "rebuilt" in the architecture?** Ask Canva PR directly, or wait for an engineering-blog post that four years of silence suggests will not come.
3. **Is the ~US$950m/5yr Sharon AI customer Canva?** One call to Sharon AI investor relations. If yes, that is a genuine scoop and a real sovereignty story: an Australian company committing US$950m to Australian sovereign GPU capacity as an inference-cost measure.
4. **Does Canva's data-residency guarantee cover generative-AI processing?** The documentation is silent. This is directly answerable by asking Canva, and directly relevant to the 10 December 2026 ADM transparency obligations. **This is the highest-value question in the note for your beat** — it is unanswered in public, cheaply answerable, and it is a governance question rather than a finance one.
5. **Why won't Canva offer Australian data residency?** Almost certainly infrastructure cost — and if so, it is the same cost story from the other end, which would be a very tidy close.
6. **How is Canva reconciling 3x → 30x cost-reduction claims five months apart?**
7. **Is "AI Pass" real?** Check Canva's enterprise pricing directly.
8. **Does retrieval-over-generation change Canva's disclosure obligations** under the incoming ADM regime? Genuinely novel; nobody has asked it.

---

## Source list

**Primary — Canva and named executives**
- Melanie Perkins, email statement to Fortune, 12 Aug 2026 — https://fortune.com/2026/08/12/canva-startup-growth-ai-costs-revenue-forecast-by-third/
- Cliff Obrecht, Stripe Tour Sydney, 19 Aug 2026, via Forbes Australia — https://www.forbes.com.au/news/innovation/canva-founder-says-ai-costs-down-90-per-cent/
- Stef Corazza, Head of AI Research, via diginomica, March 2026 — https://diginomica.com/how-canva-design-specific-foundation-model-edit-any-ai-generated-image
- Robert Kawalsky, Global Head of Product, via TechCrunch, 30 Oct 2025 — https://techcrunch.com/2025/10/30/canva-launches-its-own-design-model-adds-new-ai-features-to-the-platform/
- Cliff Obrecht to TechCrunch, 18 Feb 2026 — https://techcrunch.com/2026/02/18/canva-gets-to-4b-in-revenue-as-llm-referral-traffic-rises/
- Canva newsroom, Canva AI 2.0, 16 Apr 2026 — https://www.canva.com/newsroom/news/canva-create-2026-ai/
- Canva Help Centre, data residency — https://www.canva.com/help/data-residency/
- Canva Engineering Blog — https://www.canva.dev/blog/engineering/ (and ML/ML-infra tag pages)
- Businesswire, Canva to acquire Leonardo.AI, 29 July 2024 — https://www.businesswire.com/news/home/20240729977410/en

**Primary — regulatory filings and comparison companies**
- Sharon AI Holdings 10-K, FY2025, filed 31 Mar 2026 (names Canva as lighthouse customer) — https://www.stocktitan.net/sec-filings/SHAZ/10-k-sharon-ai-holdings-inc-files-annual-report-f1ee1855d7dc.html
- Sharon AI press release, 20 Aug 2026, unnamed global technology customer — https://www.prnewswire.com/news-releases/sharon-ai-successfully-delivers-ai-cloud-deployment-for-global-technology-customer-302856338.html
- Sharon AI / NEXTDC 50MW expansion, Nov 2025 — https://www.datacenterdynamics.com/en/news/sharon-ai-signs-50mw-data-center-lease-with-nextdc-in-australia/
- Sharon AI / VAST Data sovereign supercluster, 13 Oct 2025 — https://sharonai.com/press-releases/sharon-ai-and-vast-data-launch-insightengine-in-australia-as-sovereign-supercluster-goes-live-at-nextdc/
- Figma Q2 FY2026 earnings call transcript — https://www.fool.com/earnings/call-transcripts/2026/08/12/figma-fig-q2-2026-earnings-call-transcript/
- Duolingo Q2 2026 earnings call, 5 Aug 2026 — https://finance.biggo.com/news/US_DUOL_2026-08-05

**Secondary — used to locate primaries, labelled as such**
- Startup Daily, 5 Aug 2026 (closest account of the shareholder update) — https://www.startupdaily.net/topic/business/canva-cuts-revenue-forecast-by-a-third-as-it-tackles-high-ai-costs/
- Startup Daily, 17 Aug 2026 (valuation, IPO) — https://www.startupdaily.net/advice/business-strategy/canva-wipes-10-billion-from-its-valuation-putting-ipo-plans-in-doubt/
- The Next Web, 14 Aug 2026 (AFR fund markdowns) — https://thenextweb.com/news/canva-valuation-cut-ai-costs-blackbird-airtree
- AI Weekly, 6 Aug 2026 (summarising The Information) — https://aiweekly.co/alerts/canva-cuts-revenue-growth-forecast-on-ai-cost-blowout
- Startup Fortune, 13 Aug 2026 (named model multiples) — https://startupfortune.com/canva-slashed-its-2026-growth-forecast-after-ai-costs-blew-past-expectations/
- Forbes Australia, 25 Aug 2026 (Sharon AI shareholding) — https://www.forbes.com.au/news/innovation/canva-bet-millions-on-data-centre-play-sharon-ai-before-becoming-its-major-customer/
- Dealroom, Canva AI speedbump — https://dealroom.co/news/info-19trz12-canva-hits-ai-speedbump-on-costs-chatgpt-competition/
- Bird & Bird on the Dec 2026 ADM transparency obligation — https://www.twobirds.com/en/insights/2026/australia/australias-new-adm-transparency-obligation-oaic-signals-a-broad-reading-ahead-of-december-2026

**Paywalled, not directly read — flagged**
- *The Information* (original break, ~5 Aug 2026) and *Australian Financial Review* (Emma Rapaport & Paul Smith, 14 Aug 2026). Both reached only through secondary summaries. If any figure here is load-bearing for publication, these are the two to buy.

---

## ADDENDUM — 4 Sep 2026: the rollout hold, read as a decision rather than a cost story

Lars's framing on 4 Sep: *Canva held off its next product release because its revenue metrics were
inverted from its usage metrics.* That is the right shape and it needs one correction before it ships.

**The correction first.** Revenue did not fall. The reported figure is US$921.9m, **+25.2% YoY** —
strong by any standard. What fell was the **growth-rate guidance**, ~30% → ~20%, and the valuation
marks that priced the old guidance. So the honest inversion is: **usage up 3x, per-task cost down
90%, per-user cost up, growth guidance down a third.** Never "revenue fell." A reader who checks will
find a company growing 25% and stop trusting the piece.

**The decision, in sequence (all Canva's own words, via the shareholder update and the Fortune email):**
1. **April 2026** — Canva AI 2.0 launches on frontier-vendor APIs. Demand *"significantly exceeded"*
   projections; users create 3x the designs.
2. **The diagnosis, verbatim:** *"We were relying too heavily on frontier models. Several of our
   first-party models were not yet ready for release, and our pricing, consumption model and usage
   controls had not caught up with the outsized demand we were seeing."* — the three things that
   were not ready: the models, the price, and the meter.
3. **The decision:** *"Rather than broadly rolling out a product before the underlying economics were
   ready, we decided to slow the rollout while we rebuilt the architecture, reduced unit costs and
   strengthened the business model."*
4. **~Three months rebuilt** (B&T, 5 Aug) — in-house models substituted (30x / 23x / 17x claims,
   company figures, no benchmark), per-task cost down ~90%.
5. **The next release is now gated on unit economics, in writing:** *"We'll roll out Canva AI 2.1
   thoughtfully, expanding access as we continue to monitor quality, engagement and unit economics."*
   Obrecht at Stripe Tour Sydney, 19 Aug: they had to slow rollout *"whilst we get those costs in
   check."* Forbes AU corroborates the *weekly* unit-economics review of each AI tool (single source).

**Why this is the piece and not the 90% number.** Every SaaS growth model treats usage as the
leading indicator of revenue. Canva's own words say that in an inference product, usage became the
leading indicator of **cost**, and the company responded by treating *access* as the control
variable — expanding it only as the meter, the price and the models allowed. **A product release
held back not because it did not work but because it worked too well for the P&L.** That is the line,
and it is fully footed to Perkins.

**Three things that make it stronger, not weaker:**
- **The disclosure channel.** None of this is on Canva's newsroom or engineering blog. It lives in a
  leaked shareholder update, an email to Fortune, and a conference stage. Confirmed on the record
  by email (Fortune, 12 Aug) — so it is attributable, but the company chose not to publish it.
- **Figma did the opposite and paid the same.** Absorbed inference cost, kept shipping, FCF margin
  27% → 14% in a quarter, Q3 growth guide 48% → 36%. Two strategies, one bill. Canva is
  representative; being private just let the problem land all at once on the guidance.
- **"ChatGPT competition" as co-cause is The Information's framing**, not Canva's. Keep it out or
  attribute it as such.

**Do not print (additions to the 25 Aug list):** "revenue fell" · "Canva paused AI" (it slowed
*broad rollout* of one product line; 2.1 is rolling out) · ~~"AI Pass at US$100/user/month"~~ **(VERIFIED
later on 4 Sep — see below; now printable off the primary)** · any implication the rebuild is *finished* — Canva's own verb
is "continue to monitor."

**Still the best open question, unchanged:** does the data-residency guarantee cover generative
processing? Re-read canva.com/help/data-residency before drafting — the load-bearing sentence is a
web page.

Sources for this addendum: Startup Daily 5 Aug; B&T 5 Aug; Dealroom (citing The Information) 6 Aug;
Fortune 12 Aug; Forbes AU 19–20 Aug; Cryptobriefing 10 Aug (low-quality aggregator, used only for
the Figma numbers, which are cross-checked against the Fortune piece).

### 4 Sep, later — AI PASS IS VERIFIED. Lars supplied the primary. §2 #9 and the addendum's do-not-print are CORRECTED.

Primaries: https://www.canva.com/ai-pass/ (product page) · https://www.canva.com/help/ai-pass/ (help
centre) · https://www.canva.com/help/ai-top-ups/ (help centre). Fetched 4 Sep 2026.

**What it is, in Canva's own words.** A **per-person, monthly, auto-renewing add-on** at
**"USD $100 globally per person, per month"**, on top of Pro / Teams / Business / Nonprofits. It buys
"40x more AI with AI Pass" over Pro/Teams and "20x more" over Business, plus "Ultra AI features using
the latest AI models." Allowances for Standard, Premium and Ultra AI tools are **"shared from one
combined pool"**, and "some will consume more of your shared usage allowance than others." Resets on
the renewal date. **Excluded:** Free, Education, Enterprise, trials, prepaid, and App Store / Google
Play subscriptions.

**What happens at the limit.** "Canva will notify you as you approach your AI allowance limit."
Then: upgrade, or (Business only) buy a **top-up** — "a one-time, non-recurring purchase… equal to the
monthly AI allowance on Canva Business, to use within 30 days," which "expires and doesn't roll
over" — or "continue using premium features with short pauses." **"Short pauses" is throttling,
written as a feature.** And: "Your Canva monthly AI allowance only covers Canva's own AI tools."

**Why this is the third leg of the Perkins sentence.** She said "our pricing, consumption model and
usage controls had not caught up with the outsized demand." This page is all three arriving: the
price (US$100), the consumption model (a shared pool with tiered burn rates), and the usage control
(notify → pause → top-up). **The product held back in April ships behind a meter in September.**

**The number for the piece:** AI Pass is US$100 a month against a Pro seat that lists in the
mid-teens. **The AI add-on costs roughly six times the product it is added to.** Print it as a ratio
off the two list prices on the day; do not print a fixed multiple, because Pro pricing varies by
region and billing period.

**Discipline:**
- Neither page carries a publication or "last updated" date. **Do not write when AI Pass launched.**
  The 6 Aug AI Weekly summary of The Information already named the SKU and price, so it existed by
  early August at the latest; it may predate the shareholder update. Sequence claim: "by August,"
  never "in response to."
- "40x / 20x more AI" is Canva's ratio against an undisclosed base allowance. **No absolute allowance
  is published anywhere on the three pages.** Same shape as the 90%: a ratio with no denominator.
- "Enterprise excluded" is worth one clause: the tier that can negotiate is not on the meter.

---

## ★ RE-CHECK — 6 Sep 2026, pre-draft (mandated by the Wed 9 block: "the load-bearing sentence is a web page, not a filing")

All four pages fetched live 6 Sep 2026. **Nothing that the piece leans on has moved. One thing has been
added, and it closes a hole the 4 Sep addendum flagged.**

### canva.com/help/data-residency — UNCHANGED, and the silence holds

Re-verified verbatim, 6 Sep:

- **Regions: United States and European Union only.** Australia is still not an available residency
  region for the Australian company's own customers.
- **Tiers: Enterprise, Campus, District.**
- **Covers:** designs and comments, media files, folders, audit logs, search indexes.
- **Disclaimer, verbatim and unchanged:** *"Data residency isn't a compliance solution. It can help
  support your internal data-hosting requirements, but you'll need to consult your legal or compliance
  team for guidance."*
- **★ The page is still silent on AI/ML processing.** No sentence states whether generative or machine
  learning operations happen inside or outside the residency boundary. Checked 6 Aug, checked 5 Sep,
  checked again today. **The silence is three-for-three and it is the piece.**
- No "last updated" date on the page. Do not date it.

### canva.com/help/ai-pass — UNCHANGED on every load-bearing element

- **"AI Pass is USD $100 globally per person, per month."** Verbatim, unchanged.
- **"40x more AI with AI Pass"** over Pro/Teams/Nonprofits; **"20x more"** over Business. Unchanged.
- **Limit sequence unchanged:** *"Canva will notify you as you approach your AI allowance limit so you
  can plan your work accordingly,"* then upgrade, or top-up (Business only), or **"short pauses."**
- **Exclusions unchanged:** Free, Education, Enterprise, trials, prepaid, App Store / Google Play.
- **"Your Canva monthly AI allowance only covers Canva's own AI tools."** Unchanged.
- No publication or last-updated date. **Still do not write when AI Pass launched.** Sequence claim
  remains "by August," never "in response to."

⚠️ **One item NOT re-surfaced, and it is a fetch result, not a finding.** The 4 Sep quotations
*"shared from one combined pool"* and *"some will consume more of your shared usage allowance than
others"* did not come back in today's extraction. Per the standing absence rule, **a negative from a
single fetch of a long page is not evidence of removal** -- and the pricing page independently
describes a *"shared AI allowance"* across Standard, Premium and Ultra, which is the same mechanic. The
4 Sep quotes stand. If either is quoted verbatim in the draft, re-confirm it in a browser first.

### canva.com/help/ai-top-ups — UNCHANGED

- *"a one-time, non-recurring purchase you can add to your existing Canva Business plan"*, **Business
  only**, *"equal to the monthly AI allowance on Canva Business"*, *"Active for 30 days from purchase
  date"*, and *"If you don't use your top-up before 30 days, it expires and doesn't roll over."*
- **No price is published for a top-up.** Do not print one.

### ★★ NEW — canva.com/pricing now publishes the denominator, and the 4 Sep note said it did not exist

The 4 Sep addendum recorded: *"No absolute allowance is published anywhere on the three pages."* That
was true of the three pages it checked. **It is not true of the pricing page**, which was not in that
check. As of 6 Sep the pricing page carries:

| Tier | List price (annual billing) | AI allowance as published |
|---|---|---|
| Free | **"US$0 /year for one person"** | **"Up to 200 Standard AI uses or 20 Premium AI uses"** |
| Pro | **"US$180 /year for one person"** | "10x more AI than Canva Free (Standard, Premium, or Ultra AI)" |
| Business | **"US$250 /year per person"** | "20x more AI than Canva Free (Standard, Premium, or Ultra AI)" |
| Enterprise | **"Let's talk"** -- no price published | "20x more AI than Canva Free" |

Also on the page: **"AI Pass, available as an add-on to any Canva Pro or Business plan"**, a *"Save 16%"*
annual-versus-monthly indicator, and *"AI Pass add-on and AI top-ups available (extra cost)"* under
Business.

**Why this matters to the piece.** The 90% figure is a ratio with no denominator and the AI Pass "40x"
is a ratio with no denominator, and that shape was going to be an argument in the draft. **One rung of
that ladder now has a floor:** Free is 200 Standard uses, so the published ladder is Free 200 ->
Pro 10x -> AI Pass 40x on top of Pro. The argument survives but it must be made precisely -- the
denominator exists at the bottom of the ladder and nowhere else, and Canva still publishes no absolute
allowance for the paid tier anybody actually buys.

⚠️ **Do not print a multiplied-out number.** "AI Pass is roughly 80,000 Standard uses" is my arithmetic
across three ratios from two different pages, not a Canva disclosure. If the chain is used, it is
described as a chain and the arithmetic is shown, or it is not used.

### ★ THE RATIO, priced off two same-day list prices as the note requires

**AI Pass US$100 per person per month = US$1,200 per person per year, against a Canva Pro seat listing
at US$180 per person per year.** The AI add-on lists at **roughly six and a half times the annual price
of the seat it attaches to** (US$1,200 / US$180 = 6.67). Both figures read off canva.com/pricing and
canva.com/help/ai-pass on 6 Sep 2026, annual billing.

Print it as the ratio with both list prices named and the date attached, exactly as the 4 Sep note
directs -- **not** as a bare multiple, because Pro pricing varies by region and billing period and the
"Save 16%" indicator means the monthly-billed comparison is a different number.

### Additions to the do-not-print list

11. **Any multiplied-out absolute AI allowance for a paid tier.** The ratios chain across two pages and
    the result is arithmetic, not disclosure.
12. **A price for an AI top-up.** None is published.
13. **A launch date for AI Pass.** Still undated on every page.
14. **That the combined-pool wording was removed.** One fetch did not surface it. That is not evidence.

### Still unreached, unchanged

- **Does the residency guarantee cover generative processing?** Unanswered in public. Still the highest
  value question in the note, and the piece should say plainly that it asked and the documentation does
  not answer, rather than implying an answer.
- **Is the ~US$950m/5yr Sharon AI customer Canva?** Unconfirmed. Still a phone call, not a finding.
- **Canva's absolute inference spend.** No primary. Likely an S-1 item in 2027.
