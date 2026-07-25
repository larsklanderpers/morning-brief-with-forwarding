# Research Note — Four [VERIFY] claims from the 20 July vault signals
For: vault signals (FINRA / CPS 230 / Replit / AI wage premium) · Depth: deep · Date: 2026-07-20

## Bottom line

Two of the four claims survive with caveats; two do not survive in the form the briefs stated
them. The **CPS 230 "data residency covers inference"** line is a vendor gloss — the primary
standard never uses the words *AI*, *inference*, or *data residency*, though a precisely-stated
version of the argument is actually stronger. The **"28–56% AI wage premium"** is stale and
conflated, and the entry-level half of it points the *opposite* way to how the brief used it:
PwC's own data shows AI-exposed entry-level roles **growing 35%** since 2019 while other
entry-level roles shrank 10%. **FINRA** is solidly documented as a flawed model — but the
critique is concentrated in free-market think tanks, so use it knowingly. **Replit's numbers**
are real and primary-sourced, but the headline metric is lines of code and every quality
measure is self-reported by the company selling the product.

---

## What's solid

- **CPS 230 defines offshoring by where the service is physically performed, not where the provider sits.** Verbatim from the standard: *"Material offshoring arrangement means a material arrangement where the service provided is undertaken outside Australia. Offshoring includes arrangements where the service provider is incorporated in Australia, but the physical location of the service being provided is undertaken outside Australia."* — [APRA CPS 230](https://www.apra.gov.au/standards/cps-230)
- **Entities must notify APRA *before* entering a material offshoring arrangement**, "including in circumstances where data or personnel relevant to the service being provided will be located offshore." — [APRA CPS 230](https://www.apra.gov.au/standards/cps-230)
- **Material service providers are defined functionally**: "those on which the entity relies to undertake a critical operation or that expose it to material operational risk." No vendor categories are enumerated anywhere in the standard. — [APRA CPS 230](https://www.apra.gov.au/standards/cps-230)
- **FINRA's accountability gap is documented by an SEC Commissioner, not just outside critics.** Hester Peirce: FINRA "wields governmental powers without the procedural and disclosure requirements by which a government regulatory agency would be constrained." No APA notice-and-comment, no FOIA, no congressional appropriations oversight, no cost-benefit requirement. — [Forbes / Broughel](https://www.forbes.com/sites/jamesbroughel/2026/07/19/does-the-ai-industry-need-its-own-finra/)
- **FINRA is a monopoly by construction** — formed in 2007 from the NASD/NYSE regulatory merger, leaving a single self-regulator with no competitive discipline. — [Forbes / Broughel](https://www.forbes.com/sites/jamesbroughel/2026/07/19/does-the-ai-industry-need-its-own-finra/)
- **Replit's figures, from the primary post** (Amjad Masad + Scott Kennedy, 16 Jul 2026): 5.8x lines of code contributed early January → late June; **2.9x holding a consistent cohort of authors** to remove the hiring effect; team doubled while per-engineer rate tripled; code review latency flat with **30% of human PR review time saved**; PR reversion rates and incidents opened flat; hardest escalated support tickets closed 60% faster. — [Replit](https://replit.com/blog/self-driving-company)
- **PwC 2026: AI skills wage premium is 62%**, up from 57% the prior year, ranging 16% (government/public sector) to 118% (consumer markets). Jobs requiring AI skills growing 69% vs 9% for the overall market. Based on 1bn+ job ads across 27 countries. — [PwC 2026 Global AI Jobs Barometer](https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-jobs-barometer.html)
- **PwC 2026 on entry level:** AI-exposed entry-level roles are 7x more likely to require traditionally senior skills (judgement, leadership, face-to-face). **Those "seniorised" entry-level roles grew 35% since 2019 while other entry-level roles shrank 10%.** Based on 2.4m US entry-level jobs. — [PwC](https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-jobs-barometer.html)

---

## What's contested / watch out

- **"CPS 230 classifies voice AI vendors as material service providers."** Not in the standard. CPS 230 is principles-based; a voice AI vendor is material *if and only if* it underpins a critical operation or creates material operational risk. Every brief entry from 25 June onward traces to the same four commercial sources — [Trillet](https://www.trillet.ai/blogs/voice-ai-data-residency-requirements-by-region) (voice AI vendor), [Brightlume](https://brightlume.ai/blog/data-residency-ai-workloads-australian-compliance-sovereign-deployment) (sovereign deployment consultancy), RyderAI, and [Lorikeet](https://www.lorikeetcx.ai/articles/ai-support-australian-data-residency-guide) — all of whom sell the remedy. No APRA guidance, no law-firm client alert, no regulator statement.
- **Commencement dates are being conflated.** CPS 230 applied from **1 July 2025**. The *amended* CPS 230 and CPG 230 (targeted amendments for non-traditional service providers) commence **1 July 2026**, and 1 July 2026 is also the deadline for pre-existing material arrangements to be brought into line. The briefs' "CPS 230 takes effect 1 July 2026" is wrong as stated. — [APRA](https://www.apra.gov.au/standards/cps-230), [Norton Rose](https://www.regulationtomorrow.com/2026/05/apra-finalises-targeted-amendments-to-cps-230-operational-risk-management/), [McCullough Robertson](https://mccullough.com.au/2026/05/01/cps-230-compliance-countdown-material-service-providers-and-what-must-be-fixed-before-1-july-2026/)
- **The FINRA critique is ideologically sourced.** The sharpest version comes from Mercatus (free-market, Koch-funded) and POGO; Broughel is a Mercatus-affiliated author. The facts he cites — Peirce's dissent, the FOIA/APA exemptions, the 2007 merger — are checkable and hold up. The *conclusion* ("use voluntary standards bodies instead") is a policy preference, not a finding. Cite the mechanism, not the verdict. — [Mercatus](https://www.mercatus.org/research/working-papers/financial-industry-regulatory-authority-not-self-regulation-after-all), [POGO](https://www.pogo.org/policy-letters/pogo-letter-to-congress-calling-for-increased-oversight-of-financial-self-regulators)
- **The proposal isn't only Hassabis.** Forbes reports the **Trump administration** is weighing a FINRA-like body to vet advanced models pre-release. That reframes the story from "lab CEO floats idea" to "administration considers it, and a lab CEO is publicly supportive" — a materially different piece. — [Forbes](https://www.forbes.com/sites/jamesbroughel/2026/07/19/does-the-ai-industry-need-its-own-finra/)
- **Replit's methodology has three named weaknesses.** (1) The headline productivity metric is **lines of code** — a notoriously poor proxy, and agents write verbose code. (2) All quality measures (reversion rate, incidents opened, MTTM) are **internal and self-reported**; nothing is externally audited. (3) The post is co-authored by the CEO of a company selling the agent product, and states that every chart in it was generated by the agent under evaluation. The 2.9x consistent-cohort figure is the honest part — they explicitly removed the hiring effect. — [Replit](https://replit.com/blog/self-driving-company)
- **"28–56%" is a stale range.** 56% was the PwC **2025** figure (itself up from 25% in 2024); the current number is 62%. The 28% low end is unattributed in the brief chain — likely a different study (Lightcast has published a lower AI-skill premium) but it is not sourced, so do not present 28–56% as a single finding.

---

## Couldn't verify

- **"Only 6% wage premium at entry level, over 70% at senior."** This is the figure that would most sharply support the entry-ladder argument, and it is **not in the PwC press release**. It appears only in secondary write-ups ([Pebblous](https://blog.pebblous.ai/blog/ai-raises-the-bar-for-entry-level-jobs/en/), [SUCCESS](https://www.success.com/ai-skills-wage-premium-demand-2026)) with no page citation. It may well be in the full Barometer report — worth pulling the PDF before using it. Until then, treat as unverified.
- **Whether APRA has said anything about AI or inference specifically.** Grep of the full standard text returns zero hits for "artificial intelligence", "inference", or "data residency". CPG 230 guidance was not separately retrieved; if APRA has addressed AI it would be there or in cloud-risk guidance, not in the standard.
- **The "28%" low end of the wage premium range.** No source found in the brief chain or in search.

---

## The economics

The sharp cost framing here is on the Replit side, and it is the part nobody is quoting.
Replit reports **churning a seven-figure SaaS contract** because an internally-built
replacement was better, and separately that two vertical tools they evaluated — alert
triage/root-cause, and automated penetration testing — came back with *similar or worse*
quality at **10x the cost** of running the same job on their internal agent. That is a
build-vs-buy inversion with a number attached, and it generalises further than the
productivity stat does: the marginal cost of building an internal tool has fallen below the
marginal cost of procuring one. For a regulated-industry reader, that is also a governance
problem — shadow internal tooling with no vendor assurance, no DPIA, and no exit plan.
— [Replit](https://replit.com/blog/self-driving-company)

On the regulatory side: EU AI Act exposure reaches **€35M or 7% of global turnover**, above
GDPR maxima; the Australian Privacy Act ADM penalties reach **AUD 50M, 3x benefit, or 30% of
adjusted turnover**. Those are the numbers that make the local-inference capex argument, and
both are already in the corpus.

---

## Drop-in facts

- "FINRA wields governmental powers without the procedural and disclosure requirements by which a government regulatory agency would be constrained." — SEC Commissioner Hester Peirce, quoted in [Forbes](https://www.forbes.com/sites/jamesbroughel/2026/07/19/does-the-ai-industry-need-its-own-finra/)
- CPS 230, verbatim: *"Material offshoring arrangement means a material arrangement where the service provided is undertaken outside Australia."* — [APRA](https://www.apra.gov.au/standards/cps-230)
- CPS 230 contains **no mention of artificial intelligence, inference, or data residency**. (Verified by full-text search of the standard.)
- Replit: **2.9x code output per engineer** over a consistent author cohort, early January to late June 2026, with team headcount doubling. — [Replit](https://replit.com/blog/self-driving-company)
- Replit: an internally-built alert-triage tool matched a commercial vertical product's quality **at one tenth the cost**. — [Replit](https://replit.com/blog/self-driving-company)
- PwC 2026: AI skills wage premium **62%**, from **16% in government** to **118% in consumer markets**. — [PwC](https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-jobs-barometer.html)
- PwC 2026: AI-exposed entry-level roles **grew 35% since 2019**; other entry-level roles **shrank 10%**. — [PwC](https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-jobs-barometer.html)
- PwC's Pete Brown: *"AI is removing some of the routine work that once acted as an apprenticeship, while increasing demand for judgement, leadership and adaptability much earlier in careers."* — [PwC](https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-jobs-barometer.html)

---

## Angles this opens

**1. The vendor-sourced regulation problem.** The CPS 230 finding is a piece in itself, and it
is squarely Lars's beat: the compliance narrative that regulated firms are acting on was
written by the vendors selling the remedy, and it has been repeating through his own briefs
for a month without a primary source. That is *Ad Hoc Regulatory Regime* with a first-person
hook — he caught it in his own pipeline. It also sharpens rather than weakens the sovereignty
argument, because the real mechanism (offshoring defined by place of performance, with
mandatory prior notification to APRA) is a harder obligation than "residency."

**2. The entry ladder is being seniorised, not removed.** PwC's data cuts against the
prevailing narrative and against the framing in *Nobody Starts Senior* (17 Jul): AI-exposed
entry roles grew 35% while non-exposed entry roles shrank. The story is not that the bottom
rung disappeared — it is that the bottom rung now demands judgement, and nobody has rebuilt
the apprenticeship that used to produce it. That is a callback-and-correct piece, which is a
strong move in the *Shape of Work-to-Come* thread and more honest than restating the doom line.
