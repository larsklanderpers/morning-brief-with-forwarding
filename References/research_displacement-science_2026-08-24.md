---
type: research-note
topic: AI labour displacement, treated as a measurement problem
date: 2026-08-24
requested-by: Lars, 24 Aug 2026 — "i really want to maybe spend some time talking about the
  displacement effects in more scientific terms when we have space in the runbook for it"
status: RESEARCH COMPLETE — no slot assigned. Placement proposed in §8, his call.
supersedes: nothing. EXTENDS research_story-candidates_2026-08-23.md §5, which audited the CLAIMS.
  This note audits the INSTRUMENTS. Read §5 of the 23 Aug note first; it is not repeated here.
inputs: BLS primaries (CES, CPS, JOLTS, benchmark articles, the April 2026 report to Congress) ·
  Budget Lab at Yale · Stanford Digital Economy Lab · NBER · Economic Policy · JPE · QJE ·
  AEJ:Macro · OECD Employment Outlook 2026 · Challenger Gray July 2026 · Indeed Hiring Lab ·
  ADP Research · Axios · darioamodei.com · a16z · ZipRecruiter Economic Research
news-peg: ⚠️ BLS preliminary benchmark revision, year through March 2026 — FRI 28 AUG 2026, 10:00 ET.
  Four days out. See §2.6. Challenger's August report follows Thu 3 Sep, 05:30 ET.
---

# Research Note — The Displacement Argument as a Measurement Problem

## Bottom line, in six sentences

**1.** The four instruments everyone quotes at each other measure four different quantities with no
shared denominator, so the "20x disagreement between serious institutions" is mostly not a
disagreement — Yale measures the occupational composition of the whole labour force, Stanford
measures one four-year age band against itself, Indeed measures vacancy postings, and ADP measures
separation flow rates.
**2.** Every error term I could quantify in the US statistical system is larger than the entire
seven-month AI-attributed layoff total: BLS's own published threshold says one month's change in
household employment must exceed **678,000** before the agency will call it real, against **112,713**
AI-attributed announced cuts across seven months.
**3.** On 7 Aug 2026 BLS revised away **103,000** jobs across two months; on 6 Aug 2026 Challenger
reported **112,713** AI-attributed cuts across seven. The correction was 91% the size of the
phenomenon and it landed one day earlier.
**4.** In every well-identified historical case — electrification, computerisation, industrial
robots, ATMs — the interval between a technology arriving and a displacement effect becoming
statistically visible was **one to four decades**, and the estimates that eventually appeared were
small.
**5.** There is, as of today, **no peer-reviewed identified estimate of LLM employment displacement
in existence**; the peer-reviewed literature contains one setting-specific *productivity* result,
and everything on employment is working-paper stage with the authors' own causal disclaimers attached.
**6.** Amodei's claim is **not refuted** — but it has spent its slack, and now requires roughly a
**fourfold sustained acceleration** in exposed-cohort job destruction for four years, which is a real
prediction with a checkable terminal test on a fixed date (§5).

**The piece this supports is not "the data says AI isn't taking jobs."** It is: *everyone in this
argument is reading a dial whose needle is thinner than its own tick marks, and almost nobody says so.*

---

## §1 The estimand problem — four instruments, four quantities, one denominator between them: none

The single most useful thing in this note. The four sources that get stacked into one paragraph in
every brief are not measuring the same object, and three of the four say so in print.

| Instrument | What it actually estimates | Population | Type |
|---|---|---|---|
| **Budget Lab at Yale** tracker | Rate of change in the **occupational composition** of the US labour force (dissimilarity index, percentage points), from CPS microdata | Whole civilian labour force | Stock, composition |
| **Stanford "Canaries"** | **Relative employment of ages 22–25** in high-exposure occupations vs the same cohort in low-exposure occupations | One four-year age band, one balanced ADP firm panel | Stock, interaction |
| **Indeed Hiring Lab** | Change in the **flow of new vacancies posted** on one job board, by occupation and advertised seniority | One job board's advertisers | Flow, demand intent |
| **ADP Research** | **Monthly separation flow rate** (quits + layoffs ÷ lagged employment) and the switcher/stayer pay gap | ADP private-sector payroll clients | Flow, fluidity |

**No two share a denominator.** Composition share / cohort headcount / vacancy count / separation
rate. They cannot corroborate each other and they cannot contradict each other.

### 1.1 ★★ The two labs are not disagreeing — they are the same statement seen from two ends

**Budget Lab, in print** (Gimbel, Kendall & Nunn, 7 May 2026):

> "the Bureau of Labor Statistics' Current Population Survey, our data source throughout this
> analysis, **is best suited to analysis of broad groups and somewhat underpowered for subgroup
> analysis**, like the 22–27 year old recent college graduates that have been a special focus in
> some AI labor market impact discussions. […] **If labor market effects of AI are currently limited
> to a narrow slice of the workforce, other datasets and research designs would be better suited to
> identify them.**"

Their footnote 10 makes it concrete: restricting to 22–27 year olds, *"relatively few occupations met
our sample size criterion of 50 observations per quarter."*

**Stanford, in print** (August 2026 revision, Fact 1):

> "**We find no evidence of widespread, economy-wide job displacement.**"
> "This aggregate stability is itself informative: claims of economy-wide AI-driven job losses are
> not visible in payroll data through June 2026."

**So: Yale says its instrument cannot resolve Stanford's subgroup, and Stanford says the economy-wide
number is a null. That is agreement, expressed twice.** Any piece that stages these two as opposing
camps is manufacturing a fight neither party is having.

### 1.2 ⚠️ Engine 8 for the provenance memory — ESTIMAND SUBSTITUTION

**New failure mode, and it is the sharpest thing the research turned up.** The Stanford headline
number changed *instrument* between versions, and the change is invisible in every secondary account.

| Version | Data through | Headline | **What the number is** |
|---|---|---|---|
| Aug 2025 (v1) | Jul 2025 | **13%** | Poisson event-study coefficient, firm-time fixed effects |
| 13 Nov 2025 (v2) | Sep 2025 | **16%** | Same estimator |
| 12 Aug 2026 (v3) | Jun 2026 | **19%** | **Raw descriptive "kept-pace" divergence, no controls at all** |

The authors say so themselves, and this is the printable verbatim:

> "Earlier versions of this study headlined regression estimates adjusting for firm-level shocks (a
> 13% relative decline as of July 2025 data; 16% as of September 2025 data). **We now emphasize the
> simpler descriptive divergence, which requires no modeling choices**: by this same measure, the
> kept-pace shortfall was 15% at the July 2025 data vintage and has since widened to 19% as of June
> 2026."

**❌ DO NOT PRINT "the estimate rose from 13% to 19%."** That charts two different instruments as one
trend line. The like-for-like sequence on the *descriptive* measure is **15% → 19%**. The
fixed-effects estimate is no longer headlined, and the reason is in the paper:

> "the firm fixed-effects estimates are **more sensitive** than the raw descriptive results."

**And in the same paper, the same effect, both signs of the story, Table 1, ages 22–25, quintile 5:**

| Specification | Coefficient (SE) |
|---|---|
| No controls | **−0.179 (0.036)*** |
| + college share | −0.091 (0.053)* |
| **All controls** | **−0.080 (0.057) — NOT SIGNIFICANT** |

**The effect loses statistical significance under the full control set, and the authors publish
that.** Ages 35–40 and 41–49 are ~0.00–0.03 and never significant — the age gradient is the paper's
strongest internal evidence, and both facts live in the same table. Print both or print neither.

### 1.3 ⚠️ Three attribution corrections the corpus needs

**(a) "Seniority-biased technological change" is NOT Indeed's term or finding.** In the Indeed piece
it appears once, as a hyperlink to someone else's paper: Hosseini Maasoum & Lichtinger (Harvard),
SSRN 5425555, 31 Aug 2025, last revised 6 Jun 2026 — résumé data on 65 million workers at 280,000+
firms. Indeed is *citing it as a possibility that survives their rebound finding*, not asserting it.
**Any attribution of the phrase to Indeed Hiring Lab is wrong.** (The Harvard paper independently
finds the same mechanism as Stanford's Fact 4 — slower hiring, not more separations — from
completely different data. That corroboration is real and is worth more than the phrase.)

**(b) ADP does not claim to be measuring AI, at all.** The 24 Feb 2026 "dynamism" piece contains no
AI identification strategy; its entire AI content is one sentence noting that these sectors "have
made headlines." Richardson's own caveat is that the sign is ambiguous: *"low turnover could signal a
healthy labour market that is in balance, or it could portend a stagnant market."* **Putting ADP in a
list of "AI measurements" does work the source refuses to do.** Also: the phrase **"low-hire,
low-fire" is not in the Feb 2026 piece** — it is from ADP's 14 Oct 2025 post. Do not attach the quote
to the wrong date.

**(c) The two labs are keyed to different vintages of the same vendor index.** Budget Lab's usage
series is the **Anthropic Economic Index, March 2026 report** (cited in their repo as "Massenkoff et
al. (2026)"). Stanford's main results use the **March 2025** AEI release, with later releases only in
an appendix. So the vendor-supplied input is not merely shared — it is shared *inconsistently*.

### 1.4 The one place the four instruments genuinely agree, and it is the mechanism

Stanford Fact 4: the gap *"operates primarily through reduced hiring of young workers rather than
increased separations."* Harvard/résumé data, independently: *"driven primarily by slower hiring
rather than increased separations."* ADP: separations at a nine-year low. Indeed: posting growth
concentrated in senior roles (**71% of the net increase May 2025 → May 2026**).

> **Four datasets, one mechanism: the adjustment runs through the hiring margin at the junior end.
> Separation-rate instruments are structurally blind to it, and a hiring freeze and a healthy labour
> market produce nearly identical aggregate statistics for about two years.**

⚠️ Indeed's own base-effect caveat, routinely dropped: software postings **remain ~27.5% below their
pre-pandemic level** even after the rebound. And Indeed publishes **no coefficient, no standard
error, no confidence interval and no regression table** — "statistically significant" is asserted in
prose against scatter plots. Say so rather than manufacturing a number.

---

## §2 The power problem — the instruments cannot resolve the effect, and they are getting worse

This is the spine of the piece and it is arithmetic, not opinion.

### 2.1 The inputs, all primary, all current

| Quantity | Value | Source, date |
|---|---|---|
| Total nonfarm employment, Jul 2026 SA | **158,858,000** | BLS Employment Situation Table B-1, 7 Aug 2026 |
| AI-attributed announced cuts, Jan–Jul 2026 | **112,713** | Challenger July report, 6 Aug 2026 |
| CPS 90% significance threshold, monthly employment change | **±678,000** | BLS `cpssigsuma.htm`, July 2026 |
| CES 90% CI, monthly change | **±122,000** | BLS Technical Note, 7 Aug 2026 |
| CES mean absolute revision, 1st→3rd (2003–) | **51,000** | BLS `cesnaicsrev.htm` |
| Actual May 2026 revision, 1st→3rd | **−109,000** | same |
| May + June 2026 combined revision | **−103,000** | Employment Situation, 7 Aug 2026 |
| Final March 2025 benchmark, SA | **−898,000** | Employment Situation, 11 Feb 2026 |
| Routine annual benchmark (BLS's own 10-yr average, 0.2%) | **±318,000** | BLS `cesbmart.htm` |
| JOLTS total separations, Jun 2026 | **5,351,000** | JOLTS Table 3, 4 Aug 2026 |
| JOLTS layoffs & discharges, Jun 2026 | **1,766,000** | JOLTS Table 5, 4 Aug 2026 |

### 2.2 The arithmetic

```
112,713 / 158,858,000  =  0.071%  =  7.1 basis points of US nonfarm employment
112,713 / 7 months     =  16,102 announced AI-attributed cuts per month  =  ~1.0 bp/month
```

| Error term | Magnitude | vs 112,713 (7 months) | Detectable? |
|---|---|---|---|
| CPS 90% threshold, 1 month | 678,000 | **6.0× larger** | **No** |
| CES 90% CI, 1 month | 122,000 | **1.08× larger** | **No** |
| CES actual May 2026 revision | 109,000 | **0.97× — equal** | **No** |
| Routine annual benchmark (0.2%) | 318,000 | **2.8× larger** | **No** |
| Final March 2025 benchmark | 898,000 | **8.0× larger** | **No** |
| 2025 full-year growth revision (584k → 181k) | 403,000 | **3.6× larger** | **No** |
| One month's gross separations | 5,351,000 | **47× larger** | — |

**Every error term exceeds the entire seven-month effect.** Against normal churn: seven months of
AI-attributed layoff *announcements* equal **2.1% of a single month's** US job separations, and
**0.30%** of separations over the same seven months — roughly **a day and a half of ordinary
involuntary layoffs**.

### 2.3 ★★ The two releases, one day apart — the best paragraph available

> **6 August 2026:** Challenger reports **112,713** AI-attributed job cuts across seven months.
> **7 August 2026:** BLS revises away **103,000** jobs across two months.
> The correction was **91%** the size of the phenomenon, it covered two-sevenths of the period, and
> it arrived the next morning.

### 2.4 ★★ BLS says this itself, to Congress, in writing

From the *Report to the Appropriations Committees on Modernizing the Current Population Survey*,
**April 2026**. All verbatim, all printable:

> "**At current sample sizes, a net change of fewer than 50 survey responses could move the headline
> unemployment rate by 0.1 percentage point.**"

> "For example, 20 years ago the CPS could detect that an over-the-month change in the unemployment
> rate as small as 0.18 percentage point was statistically significant, **while now it would take two
> months of data before one could determine that this same change is statistically significant.**"

> "This greatly reduces the ability of the CPS to measure granularity and impacts measures of the
> labor force for subgroups, including demographic groups."

The sample is **60,000 eligible households — the same as in 1981, against a population up 61%.**
BLS prices the fix at ~$60m a year and warns that proceeding without it "would put CPS estimates…
at considerable risk."

**Fifty households out of sixty thousand move the number the entire argument is conducted in.**

### 2.5 The instruments are corroding, and it is documented, not inferred

- **CPS response rate: 86.4% (Feb 2016) → 65.9% (Feb 2026).** November 2025 hit **64.0%, a series
  low.** CES response rate: **60.0% (Jan 2016) → 43.3% (Jan 2026)** — fewer than half of sampled
  establishments now respond.
- **October 2025 does not exist.** BLS, verbatim: *"There are no CPS estimates for October 2025. CPS
  data were not collected for October 2025 due to the lapse in appropriations and were not collected
  retroactively."* Cancelled outright that season: JOLTS, the October Employment Situation, CPI,
  PPI, Real Earnings, Import/Export Prices, State Employment and Unemployment.
- **⚠️ The stated confidence interval widened 42% in one step.** The Technical Note's household figure
  for the monthly change in unemployment went from **±300,000 (through 9 Jan 2026)** to **±425,000
  (11 Feb 2026 onward)**, and the unemployment-rate CI from ±0.2pp to ±0.3pp, on identical
  conditioning. **This is under-reported everywhere and it is checkable in the BLS archives.**
- **CPI collection suspended entirely in Lincoln NE, Provo UT and Buffalo NY**, and ~15% of the
  sample suspended on average across 72 other areas. BLS's stated reason: *"To align survey workload
  with resource levels."*
- BLS has been without a Senate-confirmed Commissioner since August 2025 (Wiatrowski acting).
  ⚠️ Confirmed to 20 Jan 2026 from BLS's own page; **current status unverified from a BLS primary —
  do not assert it as of today without re-checking.**

### 2.6 ⚠️⚠️ THE NEWS PEG — FRIDAY 28 AUGUST 2026, 10:00 ET

**The preliminary benchmark revision for the year through March 2026 releases in four days.** It does
not exist yet; the BLS announcement page still points at last year's. Prior prints:

| Benchmark year | Preliminary | Final | Prelim→final gap |
|---|---|---|---|
| Mar 2024 | **−818,000** (21 Aug 2024) | **−598,000** | **220,000** |
| Mar 2025 | **−911,000** (9 Sep 2025) | −862,000 NSA / **−898,000 SA** (11 Feb 2026) | 49,000 |

**Note the second-order point, which is better than the first-order one:** the 2024 preliminary
overstated the final by **220,000 jobs — twice the entire AI-attributed total.** The correction to
the correction is bigger than the thing being argued about.

**Do not forecast the 28 Aug number.** But the piece should be written so that it can absorb it, and
if it lands large it is the cold open. Challenger's August report follows **3 Sep, 05:30 ET**.

### 2.7 The honest caveats — these make the argument stronger, not weaker. Keep all three.

1. **It is not a like-for-like comparison, and saying so is the credible version.** 112,713 is an
   announcement tally scraped from press releases, not an estimate produced by either survey. The
   defensible claim is **not** "AI displacement is smaller than the error bars." It is: *an effect of
   this magnitude, if it existed as a net change in employment, could not be detected by these
   instruments.* That is a statement about the instruments. It holds whether the effect is real or not.
2. **The Challenger figure's own error is larger, and unquantified.** No sampling frame, no
   confidence interval, no revision policy, no reconciliation to separations, multi-year plans booked
   entirely at announcement, and a "reason" field populated by executives Challenger himself says
   have an investor-relations motive to name AI. **A number with no error bars is not more precise
   than one with wide ones. It is less.** ⚠️ **And this is a research finding, not a gap in the
   search: Challenger publishes no methodology statement of any kind.**
3. **Net employment is the wrong place to look anyway.** If the mechanism is suppressed hiring (§1.4),
   none of this arithmetic tests it. JOLTS hires were 5.3m in June 2026; Challenger reports announced
   hiring plans **up 25% YoY**.

### 2.8 ★ Challenger's own words, and they are the best line in his dataset

> **"Naming AI in a layoff announcement can win over investors while pushing current and prospective
> employees away. That's why the messaging has swung from hedging to aggressively citing it."**
> — Andy Challenger, July 2026 report, 6 Aug 2026

> "Hiring has also increased over last year by 25%, so while **AI is shifting the labor market, it is
> not dismantling it.**"

> "Tech remains the center of gravity for this year's cuts, and **AI is still the reason companies
> give**."

> "As regulations start to take shape, companies will be even more careful in their announcements,
> **which would make tracking the impact of AI on jobs more opaque.**"

**The reason given, not the reason. And the man who publishes the number says it is not dismantling
the labour market, and predicts his own instrument will get worse.**

---

## §3 The historical base rate — how long displacement takes to become visible

**This is the section that makes the piece scientific rather than sceptical.** It answers a question
almost nobody in the argument asks: *how long has this ever taken?*

| Technology | Arrival | Window needed for a credible identified estimate | Elapsed before visibility |
|---|---|---|---|
| **Electrification** | First central station 1882; <5% of factory mechanical drive electrified in 1899 | 50% diffusion ~1919–20; TFP acceleration measured **1919–29** | **~40 years** |
| **Computers / IT** | Commercial computing 1960s–70s | Solow's paradox 1987, two decades in; software J-curve "began in the 1990s and ha[s] not waned" as of 2017 | **20–40+ years** |
| **Routine-biased change (ALM)** | Computerisation from the 1960s | Data span **1960–1998** | **38 years of data** |
| **Industrial robots** | Robot stock quadruples **1993–2007** | Outcomes **1990–2007**, long differences; JPE publication **2020** | **17-year window, 30 years to publication** |
| **ATMs** | Installed from the **1970s** | Tellers-per-branch falls **1988–2004**; total teller employment still rising in 2015 | **~30 years, aggregate sign POSITIVE throughout** |
| **LLMs** | ChatGPT **Nov 2022** | Best identified estimate covers **2 years**; best descriptive series covers **43 months** | **~3.75 years total** |

### 3.1 The quotes worth printing

**Paul David, AER 1990** — peer-reviewed, and the canonical statement:

> "In 1899 in the United States, electric lighting was being used in a mere 3 percent of all
> residences… the horsepower capacity of all electric motors installed in manufacturing
> establishments in the country represented less than 5 percent of factory mechanical drive."
> "It would take another two decades, roughly speaking, for these aggregate measures of the extent of
> electrification to attain the 50 percent diffusion level."
> "…factory electrification did not reach full fruition… before the early 1920s. **This was four
> decades after the first central power station opened for business.**"

**Acemoglu & Restrepo, JPE 2020** — the canonical *identified* displacement estimate, and note how
small it is after all that:

> "One more robot per thousand workers reduces the employment-to-population ratio by **0.2 percentage
> points** and wages by **0.42%**."

⚠️ Two-tier structure, frequently misquoted: **0.2pp / 0.42% are the AGGREGATE effects** net of
commuting-zone spillovers; the *local* effects are roughly double (0.39pp / 0.77%). Writers citing
0.39 and 0.2 as competing numbers are quoting two estimands from one paper. **A fourfold increase in
robot stock over 14 years, a 17-year outcome window, and the coefficient is two-tenths of a
percentage point.**

**Bessen on ATMs** — the base rate for "automating a task ≠ eliminating the job":

> "ATMs increased the demand for tellers because they reduced the cost of operating a bank branch…
> Fewer tellers were required for each branch, but more branches meant that teller jobs did not
> disappear."

Verified figures: tellers per urban branch **20 → 13, 1988–2004**; bank branches in urban areas
**+43%**; full-time-equivalent tellers **+2.0% per annum since 2000**.
⚠️ **DO NOT PRINT** "teller headcount rose until roughly 2007" or the ~500k→~550k figures **attributed
to Bessen** — they are not in either Bessen primary. Cite BLS OES directly, or use his
tellers-per-branch and branch-growth numbers, which carry the argument on their own.

### 3.2 The sentence this licenses

> **A commentator in 1985 looking at fifteen months of ATM data would have had exactly nothing to
> work with — and would have been wrong in both directions at once.**

**The defensible claim:** in every well-identified historical case the lag was one to four decades,
and the estimates that eventually arrived were small. A fifteen-month-old argument about LLM
displacement is not merely premature; it is asking for a category of evidence that has never once
been available on that timescale for any prior technology.

### 3.3 ★ Three ways this argument is wrong, and the piece must carry them

**Do not let the panel smooth these out. They are the difference between an argument and a posture.**

1. **"Nothing yet" is not "nothing ever," and the strongest source for that is the null result
   itself.** Humlum & Vestergaard **retitled their own paper** from *"Large Language Models, Small
   Labor Market Effects"* to *"Still Waters, Rapid Currents"* precisely to stop it being read that
   way. Their closing line: *"Technological change reshapes work well before it surfaces in earnings
   or hours."* Flat aggregates over churning structure is exactly what year three of a general-purpose
   technology is supposed to look like.
2. **Diffusion speed may genuinely be different this time, and that cuts both ways.** Electrification
   needed capital re-embodiment — rebuilt factories, new layouts, replaced machinery. That is what
   took forty years. LLM diffusion needs a browser tab, and **69% of firms report using AI** (Yotzov
   et al., NBER 34836, Feb 2026, ~6,000 executives across four countries). **But the counter-evidence
   is in the same paper:** those executives use AI **1.5 hours a week**, and **nine in ten report no
   own-firm impact** on employment or productivity — while predicting a **−0.7%** employment effect
   over the next three years. High adoption with shallow use is not fast diffusion, and the
   complementary-investment bottleneck the J-curve describes is organisational, not physical.
3. **A hiring-margin effect concentrated in one cohort is exactly what aggregates are slowest to
   see.** If §1.4 is right, the aggregates could stay calm for years while something real happens.
   The Danish data bounds this — ruling out early-career employment effects greater than one-fifth
   of an FTE per workplace — **but Denmark in 2024 is not the US in 2026.**

> **★ The Yotzov finding is its own paragraph: the same executives report no measured past effect
> and forecast a large future one. That gap, from the firms' own mouths, is the anticipation
> mechanism in one dataset.**

---

## §4 What the causal literature actually contains — which is much less than the argument assumes

### 4.1 ⚠️ THE HEADLINE FINDING, and it should probably be the piece's thesis sentence

> **There is no peer-reviewed identified estimate of LLM employment displacement in existence.**

The peer-reviewed literature on generative AI and work consists, as of August 2026, of essentially
**one setting-specific productivity estimate**: Brynjolfsson, Li & Raymond, *"Generative AI at Work,"*
**QJE 140(2), 8 April 2025** — 5,172 customer-support agents, staggered DiD, **+15% issues resolved
per hour**, with less-skilled workers improving ~30% and the most skilled seeing small declines in
quality. **It is a productivity result and makes no employment claim.** ⚠️ The 15% figure is routinely
laundered into a displacement claim. (Cite **15%** from the QJE version; working papers said 14%.)

Everything on *employment* is working-paper stage, and both leading papers disclaim the causal reading.

### 4.2 The two working papers that matter, and how to cite them

**Humlum & Vestergaard — ⚠️ THE TITLE AND THE NUMBER HAVE BOTH CHANGED.**
Current: *"Still Waters, Rapid Currents: Early Labor Market Transformation under Generative AI,"*
**NBER WP 33777, issued May 2025, revised March 2026.** Not peer-reviewed.
*"Large Language Models, Small Labor Market Effects"* is a **superseded title**, and the widely-quoted
**"rules out effects larger than 1%" is the May 2025 number only.** The current version says **2%**,
because the horizon extended to two years. **Citing "1%" cites a withdrawn number under a withdrawn
title.**

Design: two adoption surveys (Nov–Dec 2023, Nov–Dec 2024), **11 exposed occupations, ~25,000 workers,
~7,000 workplaces**, linked by social security number to Danish administrative records; DiD using
employer-wide chatbot policies as quasi-experimental variation.

| Outcome | Bound |
|---|---|
| Worker earnings, pooled DiD | precise null; rules out effects **> 2%** |
| Worker earnings, dynamic DiD | rules out **> 3%** |
| Workplace total employment | rules out **> 2%** |
| Early-career employment | rules out **> one-fifth of an FTE** |
| Monthly job churn | rules out **> 0.5% of employment** |

Mechanism: average time saving **2.8% of work hours**; **80% of adopters reallocate saved time to
other tasks**; only **3–7% of time savings pass through to earnings**; **8.4%** report new
chatbot-created tasks; **97.7% of adopters report zero earnings impact.**
Their own timescale caveat, printable: *"productivity J-curves suggest even transformative
technologies often take longer than commonly recognized to generate measurable economic effects."*

**Stanford "Canaries"** — see §1.2. **Not peer-reviewed; SIEPR working paper, no NBER number.** Their
disclaimers are emphatic and any use must carry one:

> "**We caution that this work does not estimate a causal impact of AI**: these are descriptive facts,
> and ongoing work is needed to determine how much they are caused by the spread of generative AI
> rather than merely correlated with it."
> "We interpret these facts as **early, descriptive indicators — canaries in the coal mine — rather
> than causal estimates**."

And their three self-identified problems, which are the ones a DiD design would have to rule out and
which they do not claim to have ruled out: **divergent pre-trends predating ChatGPT**, particularly
around COVID; **attenuation when controlling for occupational education**; and the divergence being
**more pronounced in the ADP panel than in national survey benchmarks**. Sample caveats: the panel
over-represents manufacturing, wholesale, larger firms, **and high-AI-exposure occupations**, and
balancing conditions on firm survival.

### 4.3 The macro ceiling — Acemoglu, and the fight is about arithmetic, not capability

**"The Simple Macroeconomics of AI," *Economic Policy* 40(121), Jan 2025 (online 6 Aug 2024). PEER
REVIEWED.** ⚠️ **Cite 0.66%, not 0.71%** — 0.71% is the April 2024 working paper only; every version
from May 2024 including the published article says 0.66%.

| Quantity | 10-year estimate |
|---|---|
| TFP, baseline | **0.66%** (~0.06–0.07%/yr) |
| TFP, adjusted for hard-to-learn tasks | **< 0.53%** |
| GDP | **0.93%–1.16%** (upper bound 1.4–1.56%) |

The framework is Hulten's theorem applied to tasks: `d ln TFP = (average task-level cost saving) ×
(GDP share of tasks impacted)`. Parameters: **19.9%** of US labour tasks exposed; **23%** of those
profitably automatable within 10 years; product **4.6%** of all tasks; average labour cost saving
**27%** from experimental studies, **15.4%** after adjusting for labour share.

> **The gap between 0.66% and Goldman's 7% is not a disagreement about what AI can do. It is a
> disagreement about aggregation.** Acemoglu is not forecasting — he is showing that *given the
> microeconomic estimates the optimists themselves cite*, the arithmetic cannot deliver large macro
> numbers.

⚠️ No 2025–26 quantitative revision found. Acemoglu/Autor/Johnson, *"Building Pro-Worker Artificial
Intelligence,"* NBER 34854, Feb 2026, is conceptual and contains **no updated estimate**.

### 4.4 ★ Autor is not applying his own framework to LLMs, and that is a story

Autor, Levy & Murnane (QJE 2003) is the foundational routine-biased-technological-change result —
and it took **1960–1998, thirty-eight years of data**. But Autor's own LLM piece (*"Applying AI to
Rebuild Middle Class Jobs,"* NBER 32140, Feb 2024) argues a **different mechanism**: computers
democratised *information*; AI might democratise *decision-making*, extending "the relevance, reach,
and value of human expertise." His own hedge, which is the honest register the piece should borrow:

> **"My thesis is not a forecast but an argument about what is possible."**

**The man who built the framework everyone reaches for is not reaching for it.**

### 4.5 ★★ The OECD sentence, in full — and the dropped clause is the load-bearing one

**OECD Employment Outlook 2026, published 7 July 2026, Ch.1 §1.3.** The corpus carries a fragment;
here it is with the context, and the context changes it:

> "Many young entrants to the labour market have become more likely to be unemployed. **The
> unemployment gap between young college graduates and the working age population has been widening
> since before the pandemic in all countries analysed.** Young entrants without a graduate degree
> have also recently seen their unemployment gap increase in a few countries. **So far, the role of
> recent advances in large language models (LLM) in explaining the difficulties facing young people
> appears to be limited.** Instead, young labour market entrants may have been particularly
> vulnerable to the recent weakening of labour markets, as well as long-term changes in technology
> and skill needs."

**"Has been widening since before the pandemic" is the clause that never survives quotation, and it
is the one that matters: the youth graduate unemployment gap predates ChatGPT by years.** Keep the
OECD's own hedge "So far" — do not smooth it.

⚠️ **And name the tension rather than resolving it:** OECD (European job-postings data) says LLMs
explain little of the youth problem; Stanford (US ADP payroll) finds a large and widening young-worker
gap. Both are defensible readings of different data in different labour markets, and **neither is a
causal estimate.** That tension *is* the honest state of the evidence, and it is more interesting than
either finding alone.

---

## §5 The forecasts as falsifiable propositions

### 5.1 ⚠️ The corpus has Amodei's claim slightly wrong in four places

| Corpus / brief version | Status |
|---|---|
| "entry-level white-collar **jobs**" | ✅ **Confirmed.** Axios, 28 May 2025, and Amodei ratified the noun himself in Jan 2026: *"displace half of all entry-level white collar jobs in the next 1–5 years."* The strong headcount reading is his |
| Window May 2025 → May 2030, ~15 months in | ✅ Confirmed. He re-endorsed the window unchanged in Jan 2026, so **the clock does not reset** |
| **"10–20% unemployment" is Amodei's** | ❌ **NO — it is Axios's prose.** It appears nowhere in quotation marks. His only direct figure is a scenario sketch: *"Cancer is cured, the economy grows at 10% a year, the budget is balanced — and 20% of people don't have jobs."* Axios appears to have compressed a GDP figure and a joblessness figure into one range. **Treat the 50% leg as his; treat the unemployment range as attributed-but-not-quoted** |
| "CNBC remark, ~27 Jan 2026 — 'unusually painful'" | ⚠️ **Misattributed.** No CNBC interview; CNBC was *reporting on* his own ~20,000-word essay *The Adolescence of Technology*. And **"unusually painful" modifies the TRANSITION, not jobs**: *"the short-term transition will be unusually painful compared to past technologies, since humans and labor markets are slow to react and to equilibrate"* |
| Forbes 21 Feb 2026 "doubled down" | ⚠️ **UNVERIFIED — original inaccessible (403).** Underlying occasion appears to be a BBC interview in which he restates the timeline but **not the 50% figure. Cut it or attribute as "reported, original not accessed"** |
| "5 May 2026 briefing: 90/10 quote" | ✅ **Confirmed verbatim.** Anthropic financial-services press briefing, lower Manhattan, **onstage with JPMorgan's Jamie Dimon**, invoking Jevons |
| "5 May 2026: 'intrinsic property' + wage insurance + UBI" | ❌ **WRONG EVENT.** Those are from *"Policy on the AI Exponential,"* darioamodei.com, **June 2026** |

### 5.2 ★★ And the corrected sequence is a better story than the one the brief tells

**On 5 May 2026 he argued the optimistic Jevons case onstage with Jamie Dimon. In June he wrote that
enduring job loss may be "an *intrinsic* property of the technology" and called for wage insurance
and UBI.** Those are in tension, one month apart, both on the record, both his.

**That is the story — not "he walked it back," which is false, and not "he doubled down," which is
unverified.** The 23 Aug note's printable formulation still stands and should be reused:

> *"Altman conceded in Sydney on 26 May that his entry-level forecast was wrong. Amodei has never
> retracted his; he re-framed. Three weeks later both companies filed confidentially to go public."*

⚠️ **Altman date note:** 26 May 2026, **virtual** appearance with Commonwealth Bank CEO Matt Comyn at
a Sydney conference — he was not physically there. Several outlets misprint 27 May. All four of the
corpus's Altman quotes verify. His stated reason for updating is unusually concrete and worth having:
he tried auto-answering his own Slack and email with AI, it failed, and he concluded the "human part"
resists substitution.

⚠️ **And the commercial-interest arrow points the other way here.** Both concessions land days after
OpenAI's IPO filing — the incentive is to **de-risk** the narrative, not to hype it. Print the
sequence, never the causation (standing rule from 23 Aug).

### 5.3 ★★ The falsifiability arithmetic — the piece's payoff

**Denominator, built from one internally consistent source** (BLS CPS Table 11b, 2025 annual averages
— note BLS flags these as 11-month averages, October excluded owing to the shutdown):

| SOC major group | Total employed | % aged 20–24 | 20–24 count |
|---|---|---|---|
| Office & administrative support | 16,444k | 9.3% | 1,529k |
| Business & financial operations | 10,173k | 4.9% | 499k |
| Computer & mathematical | 6,711k | 5.7% | 383k |
| **Total** | **33,328k** | | **2,411k** |

**Entry-level white-collar denominator ≈ 2.4 million**, against a 33.3 million all-ages white-collar
universe. (Assumptions to state if printed: uniform density within CPS age brackets, which
*understates* 22–24 and makes 2.4m a floor; three SOC groups is a defensible but not unique
operationalisation; occupation-based, so it counts young people *in* these jobs, not "recent
graduates" as such.)

**The test:**

```
Claim: −50% over a window closing May 2030.
Elapsed: ~15 of 60 months = 25.0% of the window.
Linear path ⇒ 50% × 0.25 = 12.5% reduction by now ⇒ ~−300,000 jobs.
```

**Observed, three readings, and they do not agree:**

| Reading | Observed | Linear prediction | |
|---|---|---|---|
| All 22–25 year olds (Stanford, Nov 22 → Jun 26) | **−1.9%** | −12.5% | 6.6× short |
| Two most AI-exposed quintiles | **−11%** | −12.5% | **close to on-track** |
| Counterfactual "kept-pace" gap | **−19%** | — | exceeds it |

**Three corrections cut the flattering reading down, and all three are real:**

**(a) Window mismatch, and this is the big one.** Stanford's −11% runs **Nov 2022 → Jun 2026, 43
months**. Amodei's claim starts **May 2025**. Only ~13 of those 43 months fall inside his window.
Pro-rated: **~3.3pp of in-window decline**, ~0.26pp/month — corroborated independently by the gap
measure widening 15% → 19%, i.e. **4pp over ~13 months. The honest in-window figure is 3–4pp, not
11pp. Most of the exposed-cohort decline predates the forecast and therefore cannot be evidence for
it.**

**(b) Denominator mismatch.** "Two most exposed quintiles of 22–25 year olds" is not "entry-level
white-collar." It includes exposed non-white-collar work and **excludes the entry-level white-collar
employment sitting in less-exposed quintiles, which grew ~10%.**

**(c) Level vs counterfactual.** The 19% is a **shortfall against a counterfactual**, not a decline in
a level. Amodei's claim is a level claim. **Conflating the two is the single most common error in the
commentary on this paper and the piece should name it.**

**VERDICT: NOT REFUTED. Still live — but only on a convex, back-loaded path, and that path now
carries a demanding, stateable commitment.**

| Reading | In-window so far | Still needed | Required rate | Acceleration |
|---|---|---|---|---|
| Exposed quintiles | 3.3pp (0.26pp/mo) | 46.7pp | **0.99pp/mo** | **≈3.9×** |
| All 22–25 | 0.6pp (0.044pp/mo) | 49.4pp | **1.05pp/mo** | **≈24×** |

Even crediting the **entire** 43-month −11% as if it all fell inside the window — maximally generous,
and wrong — still requires **≈3.2× sustained acceleration for four years.**

> **The claim survives, but it has spent its slack. It can no longer be satisfied by a continuation
> of present trends. It now requires a discontinuity — roughly a fourfold sustained acceleration in
> exposed-cohort job destruction, beginning soon and holding for four years. That is a real
> prediction, and it is falsifiable.**

**Be fair to it in the draft.** A back-loaded path is a legitimate structure for a diffusion claim,
not a dodge — adoption genuinely is S-shaped, and Amodei's own stated mechanism (*"humans and labor
markets are slow to react and to equilibrate"*) **predicts** a slow start. He is entitled to that.
The people calling it "a complete fantasy" at the 25% mark are making a stronger claim than their
evidence supports.

**The terminal test, and it is the close:**

> **Employment aged 22–25 in office/administrative support, business/financial operations and
> computer/mathematical occupations, at ~1.2 million against a ~2.4 million May-2025 baseline, in
> May 2030. It is in CPS Table 11b. Anyone can check it, on a fixed date, without asking permission.**

Interim checkpoints: **decisive against by ~mid-2027** if the Stanford exposed-quintile decline stays
near 0.26pp/month through four more quarterly revisions; **decisive for from ~2027** if it exceeds
~1pp/month over three consecutive quarters *and* spreads beyond 22–25 into 26–35.

### 5.4 a16z — name the interest on both sides, symmetrically

**David George, *"The 'AI Job Apocalypse' Is a Complete Fantasy,"* a16z, 6 May 2026.** ✅ Verified.
Its line: *"unhelpful marketing, bad economics and worse history."*

⚠️ **Correction to the 23 Aug note, and it matters.** That note characterises a16z as "a synthesis of
four papers, one of which is the Yale work cited beside it." True — but the four sources are
**stronger than that framing implies**: NBER WP 34984; Atlanta Fed WP 2026-3; US Census CES 26-25;
Budget Lab at Yale (16 Apr 2026). **Three of four are government or NBER working papers, independent
of a16z.** The double-counting problem is real when a16z appears in a source list *beside* Yale. The
synthesis itself is not the weak part — **the categorical headline is.** "Complete Fantasy" is doing
more work than four studies of a fifteen-month window can support.

**And name the interest on both sides.** a16z holds large positions in private AI companies whose
valuations depend on enthusiastic adoption *without* the regulatory response a displacement panic
would invite. Amodei's book benefits from AI being understood as civilisationally powerful. **Both men
are paid to be right about the same technology in opposite directions.** That is the fair statement,
and it is more useful than sneering at one of them.

### 5.5 ★ The "57% of employers" claim — PRIMARY FOUND, and it survives

**ZipRecruiter Economic Research, *"More Jobs, Higher Bar: The 2026 AI Employer Report,"* published
29 July 2026.** Survey of **1,000+ verified talent-acquisition professionals and hiring managers**,
fielded **11–18 June 2026**.

> "57% of employers say they expect more productivity from their workforce because of AI."

**Standing rule §2 does not fire.** ZipRecruiter is a job marketplace, **not an AI-productivity
vendor** — it does not sell the tooling the statistic implicitly endorses, and its revenue depends on
hiring volume, which a displacement narrative would hurt. ⚠️ **But attribute it as EXPECTATIONS, never
as measured productivity.** Self-reported employer sentiment, self-administered online panel, no
published response rate.

**★ And two figures from the same report are better for the entry-level thesis than the 57% is:**
**38%** automated basic data entry away from entry-level roles; **31% raised experience requirements
for entry-level jobs.** That second number is the hiring-margin mechanism (§1.4), self-reported by
the employers doing it.

---

## §6 Do-not-print, consolidated

1. ❌ **"Stanford's estimate rose from 13% to 19%."** Two different estimators. Like-for-like is
   **15% → 19%** on the descriptive measure. (§1.2)
2. ❌ **"Seniority-biased technological change" attributed to Indeed Hiring Lab.** It is Hosseini
   Maasoum & Lichtinger, SSRN 5425555. Indeed cites it. (§1.3a)
3. ❌ **ADP presented as an AI measurement.** It contains no AI identification strategy and the
   source declines the interpretation. And **"low-hire, low-fire" is from 14 Oct 2025, not 24 Feb
   2026.** (§1.3b)
4. ❌ **"Humlum & Vestergaard rule out effects larger than 1%"** under the title *"Large Language
   Models, Small Labor Market Effects."* Withdrawn number, withdrawn title. It is **2%**, and the
   paper is *"Still Waters, Rapid Currents."* (§4.2)
5. ❌ **Acemoglu's TFP figure as 0.71%.** Published, peer-reviewed value is **0.66%**. (§4.3)
6. ❌ **Acemoglu & Restrepo's 0.39pp and 0.2pp as competing estimates.** Local vs aggregate, same
   paper. (§3.1)
7. ❌ **"Teller headcount rose until ~2007" or ~500k→~550k attributed to Bessen.** Not in his
   primaries. (§3.1)
8. ❌ **"Amodei predicted 10–20% unemployment"** as a quotation. Axios's prose, not his words. (§5.1)
9. ❌ **"Unusually painful" as a CNBC remark about jobs.** It is from his own essay and modifies the
   **transition**. (§5.1)
10. ❌ **The "intrinsic property" / wage-insurance / UBI material dated to 5 May 2026.** June 2026,
    different document. (§5.1)
11. ❌ **The Forbes 21 Feb 2026 "doubled down" piece as a source.** Original inaccessible. Cut or
    attribute as not-accessed. (§5.1)
12. ❌ **Brynjolfsson/Li/Raymond's +15% as evidence of displacement.** It is a productivity result and
    makes no employment claim. Cite **15%**, not 14%. (§4.1)
13. ❌ **The OECD sentence without "has been widening since before the pandemic"** and without its own
    "So far." (§4.5)
14. ❌ **"57% of employers report higher productivity."** They **expect** it. (§5.5)
15. ❌ **Any forecast of the 28 Aug benchmark number.** It does not exist yet. (§2.6)
16. ⚠️ **BLS Commissioner status after 20 Jan 2026** — unverified from a BLS primary. Re-check or omit.
17. ⚠️ **Do not print "AI displacement is smaller than the error bars."** The defensible form is
    *"an effect of this size could not be detected by these instruments."* (§2.7)

**Carried forward and still live from `research_story-candidates_2026-08-23.md` §10:** the
115K-tech-layoffs kill (#31–38 block), "both walked back" (false — only Altman), the truncated 90/10
quote, BCG's *"not intended to be an unemployment forecast,"* the 2.5x figure not being BCG's, and
Yale being counted twice when a16z appears beside it.

---

## §7 What is genuinely NEW here, versus the 23 Aug dig

The 23 Aug note audited the **claims**. This note audits the **instruments**. Six things are new:

1. **The estimand map** (§1) — the four instruments measure four quantities. Nobody has written this.
2. **Estimand substitution as a provenance engine** (§1.2) — a research team changing which estimator
   it headlines, invisibly, between versions. This is **engine 8** and it belongs in the memory.
3. **The noise-floor arithmetic** (§2) — the 6.0× and the 91%-in-one-day, from BLS primaries.
4. **BLS telling Congress its own instrument is going blind** (§2.4) — the "fewer than 50 survey
   responses" line, and the 42% CI widening in Feb 2026 that appears to be unreported anywhere.
5. **The historical lag table** (§3) — one to four decades, every time, with the small coefficients
   that eventually arrived.
6. **The falsifiability arithmetic on Amodei** (§5.3) — the ~4× acceleration requirement and the
   fixed-date terminal test in CPS Table 11b.

---

## §8 Placement — proposed, not decided

**This week is closed.** Mon 24, Tue 25 and Sat 29 are all signed off and in Scheduled (Mon 24 has
now been reconciled to Published — see the session report). The Oasis stand-down leaves no drafting
slot before 31 Aug, and I would not want one: **the piece is better after 28 Aug and after 3 Sep**,
because both dates put fresh primaries in its hands.

**Week of 31 Aug is fully assigned** and I do not recommend displacing anything in it.

### ⚠️ The collision that has to be designed around, and it is a real one

**Thu 3 Sep — "The Number Nobody Can Produce"** already runs a count argument: *"patch critical within
30 days" written against a number nobody can produce.* A displacement piece built as *"a claim
written against a number nobody can produce"* is **the same skeleton ten days later** and would be a
categorical cross-piece fail.

**The distinction is real and must be load-bearing in the spine, not a hedge in one line:**

> **Thu 3 Sep: nobody produces the number.**
> **This piece: four organisations produce four numbers, precisely, and none of the four instruments
> can resolve the effect being argued about — because they are not measuring the same thing.**

Absence of a count versus **resolution, power and estimand**. Different failure, different register.
If the draft ever reaches for "nobody can count it," it has drifted into 3 Sep's piece and should be
pulled back to the dial-and-tick-marks frame.

### The recommendation

**Sunday 13 September — capstone slot.** Reasons, in order:

1. **It is a heavy synthesis piece and the capstone register is where those live.** Six sections, an
   arithmetic spine, a historical table and a falsifiable close. It will not fit a weekday.
2. **It carries the 28 Aug benchmark and the 3 Sep Challenger print** with ten days to absorb both.
3. **It is ten days clear of Thu 3 Sep**, outside the Seat 5 seven-day window, which makes the
   collision above manageable rather than fatal.
4. **The thread rotation works:** Shape of Work-to-Come × Judgment, which last carried a capstone on
   6 Sep and would otherwise rest three weeks.

**Fallback: Friday 11 September.** The Friday register in this pipeline is explicitly *the
arithmetic*, which fits §2 exactly. Costs: it sits inside 3 Sep's seven-day window (worse collision),
and it would need cutting to roughly half length, which would take out §3 or §5 — and those are the
two sections that make it science rather than scepticism.

**Not recommended: any slot before 31 Aug** (nothing is open and both news pegs are unfired), or
**7 Sep** (CPS 230 has that lead and it is the right lead).

### The spine, if it runs

> **Cold open:** the two releases, one day apart (§2.3). Or, if 28 Aug lands large, the benchmark
> itself — an instrument revising away more jobs in one stroke than the entire phenomenon it is being
> asked to measure.
> **Beat 1:** the four instruments, four quantities, no shared denominator (§1). The argument
> everyone is having is not an argument.
> **Beat 2:** the arithmetic. 6.0×. Fifty households out of sixty thousand (§2).
> **Beat 3:** the instruments are corroding — response rates, the missing October, the CI that
> widened 42% while nobody noticed (§2.5).
> **Beat 4:** how long has this ever taken? One to four decades, every time, and the coefficients
> that eventually arrived were two-tenths of a percentage point (§3).
> **The turn, and it must be here or the piece is a debunk:** none of that means nothing is
> happening. Four datasets agree on a mechanism — the hiring margin at the junior end — and it is
> precisely the mechanism aggregates are slowest to see (§1.4, §3.3).
> **Close:** the terminal test. 1.2 million against 2.4 million, CPS Table 11b, May 2030. Not an
> opinion, a date (§5.3).

**[YOUR TAKE] needed in two places, and I would not draft either:**
1. **The practitioner's version of the hiring-margin finding.** Has he watched the junior rung close
   from the inside — hiring plans quietly not renewed rather than anyone being cut? That is the beat
   where the piece stops being about statistics.
2. **The governance parallel, which is his home ground and nobody else's.** This is the same failure
   as a control whose evidence cannot resolve the thing it certifies — an instrument reporting a
   clean number at a resolution below the effect. He has written that argument four times about
   compliance. **This is that argument about macroeconomics**, and the transfer is the reason the
   piece belongs to him rather than to an economics writer.

---

## §8.5 ⚠️ RESOLVED 29 AUG — all three releases landed, and two of this note's moves are DEAD

**See `research_bls-week_2026-08-29.md` (and `research_bls-benchmark_2026-08-28.md`, written on the
day, which reached the same benchmark figure independently). Read this section before drafting
anything above.**

### What landed

| Release | Result |
|---|---|
| **CES preliminary benchmark, yr to Mar 2026** (Fri 28 Aug) | **−79,000 (−0.1%), NSA.** About a QUARTER of BLS's own 10-yr average. Prior year was −911,000 |
| **Worker Displacement 2023–2025** (Thu 27 Aug) | Long-tenured displacement **up ~29%**; share reemployed at equal-or-better pay **fell ~62% → ~49%** |
| **Employment Projections 2025–2035** (Thu 27 Aug) | The three SOC groups this note uses **GROW +279,500 (+0.78%)** over the decade |

### ❌ TWO MOVES IN THIS NOTE ARE NOW REFUTED. Do not draft them.

1. **"Fourth consecutive LARGE downward benchmark" is dead.** −79,000 is roughly 9% of last year's
   final. The narrower "fourth consecutive *negative*" survives only with "preliminary" attached and
   the magnitude collapse acknowledged in the same breath.
2. **The "benchmark dwarfs the AI effect" device is dead for 2026.** It ran **8.08×** last year. It
   runs **0.70×** this year — the wrong way. §2.6's cold-open framing goes with it.

### ⚠️ And one sector fact cuts against the thread

**Information — the most AI-exposed supersector — was revised UP 87,000 (+3.0%)**, the largest
percentage revision in the table in either direction. Professional and business services revised down
only −76,000 (−0.3%). The downward revisions sit in retail and education/health. **Never write "even
the benchmark shows the white-collar sectors were overstated."**

### ★★ But the argument is STRONGER, on better evidence

Three replacements, all of which rest on instrument design and BLS's own words rather than on a
number that just moved 91% the wrong way:

1. **The benchmark's point estimate is smaller than its own historical error.** −79,000 against a
   2024 preliminary-to-final miss of **220,000** — an error band roughly **2× the entire claimed AI
   effect** (112,713). BLS calls the figure "a preliminary measure of the **total error**" and, unlike
   last year, **offers no decomposition at all.** The instrument reports a residual and declines to
   attribute it.
2. **★★ THE STRONGEST RESULT IN THE WHOLE THREAD — the Displaced Worker Survey cannot record an AI
   reason.** Its complete closed-response set: *plant or company closed down or moved · insufficient
   work · position or shift abolished · seasonal job completed · self-operated business failed · some
   other reason.* **No technology category. No automation category. No AI category. No
   causal-mechanism dimension at all.** A job eliminated by a language model is coded **"position or
   shift abolished"** — the same bin as offshoring, restructuring, PE cost programmes and ordinary
   reorganisation. That bin is **44.4% of long-tenured displaced workers**, the largest of the three.
   **No sample size fixes a missing question.** BLS mentions AI, automation and technology **zero
   times** in the release and technical note.
3. **BLS says the third instrument is non-diagnostic, in writing.** The projections programme declined
   to model AI's productivity effects because doing so *"would be highly speculative"* and uncertainty
   *"remains very high."*

**The reframed thesis, and it is better than the one this note was built on:**

> *Three federal instruments reported on AI-era labour displacement in a single week. The benchmark's
> point estimate is smaller than its own historical error, so it cannot resolve an effect of 112,713.
> The displacement survey has no technology, automation or AI response category, so it cannot record
> one at all. And the projections programme states in writing that it declined to model AI because
> doing so would be "highly speculative." The instruments are not disagreeing about AI displacement.
> They are structurally incapable of measuring it — and this week two of the three said so in their
> own words.*

### ⚠️ Three honest counterweights the draft must carry

- **The DWS results are not null.** Long-tenured displacement rose ~29% and reemployment-at-equal-pay
  fell from ~62% to ~49%. **Something real happened to displaced workers.** The claim is that the
  instruments cannot *attribute* it — not that nothing occurred. Blur that and the piece reads as
  denial rather than methodological critique. The instrument's silence is **not** evidence the effect
  is small.
- **BLS DOES name AI in prose, twelve times, in both directions** — so "the instruments say nothing
  about AI" is not sustainable for Release 3. The sustainable version: **BLS makes qualitative,
  hedged, directional judgements about AI while explicitly declining to quantify it.** Note the
  asymmetry in its own verbs: AI *"is expected to support"* demand (confident) but *"may dampen"* it
  (hedged).
  ❌ **DO NOT PRINT "BLS says AI will cut 752,100 office jobs."** BLS says *"automation tools,
  including those powered by AI"* are *"likely to reduce"* demand for *"several"* occupations in that
  group. A named subset of a broader category, an unspecified subset of occupations, a hedged verb.
- **⚠️ §5.3's DENOMINATOR NEEDS RECONCILING.** BLS projects the three SOC groups this note uses to
  size "entry-level white-collar" **growing +279,500 (+0.78%)** over 2025–2035, with composition
  shifting clerical → analytical. That is a **compositional** story, not a contraction one. Reconcile
  it before publishing, because §5.3's arithmetic leans on that population.

### ★ Two spare arguments this hands the piece

- **Scale mismatch, in BLS's own tables:** the **top ten fastest-declining occupations lose ~78,400
  jobs combined over TEN YEARS** — less than the seven-month Challenger figure of 112,713. Word
  processors lose 13,900 over a decade; telephone operators 1,000; patternmakers 300. **Percent-change
  rankings are not magnitude rankings**, and a decadal-average instrument cannot adjudicate a
  seven-month announcement count.
- **The declining-occupation roster is the pre-AI automation roster** — word processors, typists,
  switchboard and telephone operators, data entry keyers — declining on trend for twenty years.
  Nothing on it is AI-specific and nothing on it is new.

### ⚠️ Watch item

BLS shipped a **new AI-exposure data product** alongside the projections — an official federal AI
taxonomy. **It measures exposure, not displacement, and will be misreported as a displacement
forecast within weeks.** Get ahead of it.

---

## §9 Open [VERIFY] and standing re-checks

- **[VERIFY]** BLS preliminary benchmark, year through March 2026 — **releases FRIDAY 28 Aug 2026,
  10:00 ET** (National *and* State/Area, both 10:00). Verified against the BLS August 2026 release
  schedule, 25 Aug. ⚠️ **It is a FRIDAY. The 25 Aug work brief printed "Thursday Aug 28" — the date is
  right and the weekday is wrong.** Blocks the cold open if that framing is used.
- ★★ **TWO MORE BLS RELEASES THAT WEEK, BOTH THURSDAY 27 AUG, 10:00 ET, AND BOTH MISSED BY EVERY
  BRIEF — they are more directly on-topic than the benchmark is:**
  - **Worker Displacement, 2023–2025** — the Displaced Worker Survey. This is *the* federal
    instrument that measures displacement by name, on a biennial cycle, and a fresh vintage lands
    three days from now. **It has to be in the piece.** Check what it says about reason-for-job-loss
    categories and whether "technology" or "automation" is separable at all — if the official
    displacement instrument cannot code an AI reason, that is §2's argument arriving from inside the
    statistical system.
  - **Employment Projections and Occupational Outlook Handbook, 2025–2035** — BLS's own ten-year
    occupational projections. Whatever BLS projects for the office/admin, business/financial and
    computer/mathematical groups **is the official counterfactual** against which Amodei's 50% claim
    can be scored (§5.3 uses those same three SOC groups). A ten-year projection published inside
    his five-year window is the cleanest available comparison.
- ⚠️ **Consequence for placement (§8): the research window now opens Thu 27, not Fri 28.** Three
  releases in two days, then Challenger on 3 Sep. The Sun 13 Sep recommendation still holds and gets
  stronger — it is the first capstone slot clear of all four.
- **[VERIFY]** Challenger August report — **3 Sep 2026, 05:30 ET.** Do not print an August AI-attributed
  figure before it. ✅ **A scheduled task is set for this one** (created 29 Aug, bound to his machine).
- **[VERIFY]** BLS Commissioner status as of the drafting date.
- **[VERIFY]** Forbes, 21 Feb 2026 — original inaccessible. Cut or attribute as not-accessed.
- **[VERIFY]** January 2026 CPI publication-changes notice — URL 404'd on retrieval. Omit or re-source.
- **Re-check before drafting:** whether a **fourth** NBER revision of WP 33777 has appeared past March
  2026. The 2% bound is stable across the two revisions I have, so nothing turns on it — but the
  title and number have already changed once and that is the failure mode.
- **Retrieval note for whoever drafts this:** `hiringlab.org` and `hiringlab.indeed.com` both
  redirect-loop to ordinary fetchers, as the corpus flagged. A stealth-proxy scrape of
  `www.hiringlab.org` reaches the primary. The Budget Lab tracker page renders "Loading…" to every
  scraper — **its methodology is only legible from the GitHub source repo** (`tracker.yaml`,
  `current-update.md`), which is also where the Anthropic Economic Index dependency is confirmed.

---

## Appendix — triage of the 24 Aug story candidates

Checked against `SUBSTACK_INDEX.md`, all August drafts, Published, Scheduled, and the 12/14/16/17/19/23
Aug dig notes. **Two of eleven carry genuinely new ground.**

| # | Candidate | Verdict | Note |
|---|---|---|---|
| 1 | CrowdStrike 2026 THR | **FULL REPEAT** | Marked SPENT (Mon 10 Aug) in the 17 Aug note. Do-not-print already stands on the 29-minute/AI-attack figures |
| 2 | ShinyHunters / "Questal" | **FULL REPEAT — 3rd outing** | Demolished in 23 Aug §1. **The misspelling is still there** — "Questel SAS" — which is the tracer dye proving no primary was opened. Already allocated inside the Sat 29 piece |
| 3 | Collapse of the Trust Perimeter | **PARTIAL** | CVE-2026-68820 is a standing do-not-print as characterised (EoP, local, CVSS 7.0 — not an RCE), now on its **third regeneration**. **N-central and the Snowflake GitHub Actions flaw return zero corpus hits** — the only unspent legs, both unverified |
| 4 | MCP roadmap controversy | **★ NEW** | Only candidate whose subject has no prior coverage. MCP exists in the corpus purely as attack surface. Drop the HN vote counts — engagement artefacts, not evidence |
| 5 | Open-weight models close the gap | **FULL REPEAT + live refutation** | The 19 Aug note is *entirely* this item and is the corpus's specimen for citation-laundering. **BenchAlign is an affiliate-funded aggregator that runs no evaluations. And the corpus verified GLM-5.3; today's brief says 5.2 — a regression** |
| 6 | One curl command and a Google search | **★ PARTIAL, leaning NEW** | The class is worked, but 17 Aug's scope verdict was *"every documented in-the-wild case is a public marketplace or registry."* **Google-ranked docs impersonation on a vendor-hosted domain falls outside that taxonomy.** Verify the publisher first |
| 7 | Four basic questions (LexisNexis) | **PARTIAL — device is spent** | Four-questions is the device in 08-12, 08-17, 08-23 and 08-29. **A fifth would be a categorical cross-piece fail** — 08-29 already logged an rv5 categorical fail on exactly this. Also a webinar, i.e. a marketing asset |
| 8 | Trust infrastructure vs pace | **FULL REPEAT** | All three legs covered 08-03, 08-10, 08-13, re-dug 19 Aug. ⚠️ "The December Privacy Act amendments" is **singular — one obligation, 10 Dec 2026** |
| 9 | FDE / OpenAI $280K | **PARTIAL — headline numbers killed** | **"800%" is Jan–Sep 2025 data, retired from live use.** The one real new measurement entered the corpus yesterday |
| 10 | Meta-skills consensus | **FULL REPEAT — 4th regeneration** | Killed 14 Aug (*"no evidence base. Cut, don't hedge"*), regenerated 17 and 23 Aug. The legitimate version is already allocated to the 6 Sep capstone |
| 11 | Displacement front-loaded in tasks | **FULL REPEAT — but see this note** | The brief's "closing hypothesis" **is Stanford's Fact 4**, published four days before the brief printed. **"57% of employers" now has a primary** (§5.5) |

**★ The structural finding, and it is the same one the 17 Aug note made:** three of today's eleven —
#2, #10 and #11 — are killed claims regenerating for the third or fourth time, and **all three were
killed or re-killed in yesterday's dig.** The do-not-print list lives in `References\` and
`briefing_agent.py` does not read it. That is a plumbing defect, not a judgement defect, and it is
now costing a triage pass every morning.
