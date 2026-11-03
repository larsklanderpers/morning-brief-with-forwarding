# Research Note — Shadow AI global statistics (LinkedIn post sourcing)
For: LinkedIn post "shadow AI is a symptom, not the disease" (10 Aug 2026) · Depth: deep · Date: 2026-08-10

## Bottom line

All five numbers are real and all five are traceable to a named study — but **only one of the five means what the post says it means.** Four of them are shares of a *filtered* population (employees who already use AI at work) or of *organizations*, and the post restates them as shares of the whole workforce. One of them — Singapore — is a straight transposition error that came from a Sophos executive's own byline, and the primary Sophos whitepaper contradicts it.

The paragraph that does the real work — *"Five regions. Same number, roughly. Somewhere between half and three quarters of your workforce is already doing this"* — is the part that does not survive. Those five percentages have **three different denominators** between them (AI-using employees, all employees, organizations), so they cannot be stacked. The convergence is an artifact of the stacking, not a finding.

There is an unusually good version of this problem: the post's own thesis is that unverified numbers quietly become known facts that other things get built on. The post is currently an instance of it. That's a real asset if you want to use it.

---

## What's solid

- **UK — 71% / 51%.** "New Microsoft research reveals that 71% of UK employees have used unapproved consumer AI tools at work, and 51% continue to do so every week." Censuswide for Microsoft, October 2025 fieldwork, **n=2,003 UK employees aged 18+**, published 13 Oct 2025. **Base is all employees surveyed — not filtered to AI users.** This is the only one of the five where "% of employees" is the correct denominator. [Microsoft UK Stories, 13 Oct 2025](https://ukstories.microsoft.com/features/rise-in-shadow-ai-tools-raising-security-concerns-for-uk/)
  - *Caveat:* the sample is quota'd, not nationally representative — minimum 500 from large businesses (250+ employees) and 500 from the public sector, plus sector boosts in financial services, retail, education and health. Those are exactly the employers most likely to have a formal AI policy to breach. Say "2,003 UK employees surveyed by Censuswide for Microsoft," not "UK employees" flat.

- **US — 44% and 46%, but on the AI-user base.** KPMG International + University of Melbourne, *Trust, attitudes and use of artificial intelligence: A global study 2025*. 48,340 respondents, 47 countries, fieldwork **Nov 2024 – mid-Jan 2025**, published 29 Apr 2025. US n=1,019. The figures: "44% used AI in ways that contravene policies and guidelines"; "46% uploading sensitive company information and intellectual property to public AI platforms." [Global report PDF](https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2025/05/trust-attitudes-and-use-of-ai-global-report.pdf) · [KPMG US release](https://kpmg.com/us/en/media/news/trust-in-ai-2025.html)

- **India — 72% and 81%, same study, same base.** "72% used AI in ways that contravene policies and guidelines"; "81% relied on AI output at work without evaluating its accuracy." [KPMG India snapshot PDF](https://assets.kpmg.com/content/dam/kpmg/xx/pdf/2025/02/trust-attitudes-and-use-of-ai-india-snapshot.pdf)

- **APJ — 58% and 35%, as hypotheticals.** BCG, *AI at Work 2025: Is Asia Pacific Leading the Way?*, fieldwork July 2025, published 29–30 Oct 2025. Press release verbatim: "Fifty-eight percent of APAC respondents say they would use AI even without company approval" and "35% would bypass restrictions to do so." [BCG press release](https://www.bcg.com/press/30october2025-asia-pacific-leads-ai-adoption) · [BCG publication](https://www.bcg.com/publications/2025/ai-at-work-is-asia-pacific-leading-the-way)

---

## What's wrong — fix before publishing

### 1. The KPMG base. This is the big one.

Figure 44 of the global report ("Inappropriate and complacent use of AI at work") carries the printed base note:

> **"Base: Employees who intentionally use AI at work (n=18,898)"**

Every workplace-risk item in that study — contravening policy, uploading sensitive data, not checking accuracy, passing AI work off as your own — was asked **only of employees who already use AI at work.** Not of all workers.

The US snapshot proves it arithmetically: **only 37% of US employees intentionally use AI at work**, yet 44% "contravene policies." 44% cannot be a share of all workers when only 37% of workers touch AI at all. Run the multiplication and the real figure is **roughly one in six US employees (~16%)**, not 44%.

Same for India: the India snapshot reports ~two-thirds of Indian employees intentionally using AI at work, against 81% relying on output without evaluating accuracy. 81% of a 67% population is ~54% of employees.

So "44% of workers use AI tools without authorization" is not what KPMG found. It's ~44% of the AI-using minority.

**Also:** attribution should be **KPMG International and the University of Melbourne** — Melbourne is the academic partner and it's their methodology. And the wording drifts: the item is "used AI in ways that **contravene policies and guidelines**," which covers prohibited *uses* and non-disclosure, not just unsanctioned *tools*. "Use AI tools without authorization" is KPMG US's press-release gloss, not the questionnaire.

### 2. Singapore is a transposed pair of numbers. Cut or correct.

The Sophos whitepaper's Singapore country page (p.19) reads, verbatim:

> "% of organisation using business AI tools such as ChatGPT, agentic AI, co-pilots: **88%**"
> "% of organisations with a formal AI strategy: **79%**"
> "Level of unauthorised AI tool usage (shadow AI): **60%, another 14% unsure**"

The post has it backwards. **79% is the AI-strategy figure, not the unauthorized-tools figure.** Unauthorized tool use in Singapore is **60%** (74% if you count the "unsure").

The error came from a [May 2026 Frontier Enterprise op-ed](https://www.frontier-enterprise.com/shadow-ai-the-insider-risk-growing-in-singapore/) bylined by Aaron Bugal, Sophos's own APJ Field CISO, which swapped the labels — and which contradicts itself two paragraphs earlier by correctly saying "Singapore had one of the highest levels of shadow AI at 60%." A Sophos executive writing under Sophos's name is exactly the kind of source that reads as primary to anyone checking casually. It isn't.

Three further problems with the attribution:
- **"Sophos, 2026" is wrong.** It's the 5th edition, **August 2025**, fieldwork June 2025 by Tech Research Asia. No 2026 edition exists. The 2026 date is the op-ed's, not the research's.
- **The base is organizations, not employees** — and the respondents are IT and security staff, not the general workforce. Singapore n=105 (total n=926 across Australia, India, Japan, Malaysia, Philippines, Singapore).
- The population isn't filtered to AI adopters the way the post implies.

[Sophos APJ whitepaper, Aug 2025 (Singapore p.19)](https://assets.sophos.com/X24WTUEQ/at/2prbj4bsqxkgp5mrn48gcthv/sophos-future-of-cybersecurity-apj-2025-wp.pdf)

### 3. BCG: "even if their company said no" overstates the question.

The underlying chart is titled *"How respondents would react if their organization did not formally provide access to GenAI tools or support their use."* The 58% option is "Would use GenAI tools on my own, without formal support from my organization."

That's **non-provision, not prohibition.** "Their company said no" is a materially stronger claim than what was asked. BCG's own press-release gloss ("without company approval") is already looser than its chart; the post stretches the gloss further.

The 35% has a separate problem: it's a **role-level** figure, not an APAC-wide one. The chart ("Share of respondents who would use AI tools even if not authorized by the company") splits: frontline employees 30%, managers 35%, leaders 35%. "Over a third would actively bypass a block" reads as an overall behavioral finding; it's a hypothetical attitudinal item, and the third-plus applies to managers and leaders.

Also worth knowing: the "4,500+ employees across nine APAC markets" headline is an **aggregation of two surveys** — the APAC instrument is N=2,516 across seven markets, with Japan (n=1,012) and India (n=1,031) borrowed from the global wave.

Both figures are "would," not "have." They measure stated intent, not behavior.

### 4. Microsoft's 51% — use their construction, not yours.

Microsoft never states whether 51% is 51% of all employees or 51% of the 71%. Their phrasing ("71% have used ..., and 51% continue to do so every week") reads as two parallel shares of the same population and all downstream coverage takes it that way — but they don't confirm it. If it were 51% of the 71%, the true figure is 36% of employees. **Quote Microsoft's construction verbatim** rather than writing "more than half do it weekly," which commits you to a reading Microsoft didn't make.

---

## The denominator problem, stated plainly

This is the thing to fix structurally, not stat by stat:

| Region | Figure | What it's actually a share of |
|---|---|---|
| US | 44% | employees **who already use AI at work** (~37% of US employees) → ~16% of workforce |
| APJ | 58% | survey respondents, **hypothetical** ("would," if AI weren't provided) |
| Singapore | 60% (not 79%) | **organizations**, reported by IT/security staff |
| UK | 71% | **all employees surveyed** ✅ |
| India | 72% / 81% | employees **who already use AI at work** (~67% of Indian employees) |

Three denominators, one hypothetical, one wrong number. "Five regions, same number, roughly" is produced by the stacking.

---

## Couldn't verify

- **Whether the 46% (US, sensitive data upload) appears in any primary document.** It's in the KPMG US press release only — not in the US country snapshot, not in the US summary report. It's KPMG's own number so it's citable, but there's no methodology page behind it.
- **The exact India sub-sample.** KPMG publishes country totals (1,001–1,098 per country) but no country-level sub-base for the AI-user filter. India's AI-using subset is roughly n≈470–500 by inference. Also, extractions returned both 67% and 71% for India's "intentionally use AI at work" — don't cite that specific number without re-checking.
- **The global "contravene policies" figure.** PDF extraction returned 44% in the executive summary and 47% at Figure 44. The country-level US 44% and India 72% are unaffected, but don't cite a *global* contravention figure without re-checking the page.
- **Whether Microsoft's 51% is of all employees or of the 71%.** See above.

---

## Drop-in facts (verified, ready to use verbatim)

- "71% of UK employees have used unapproved consumer AI tools at work, and 51% continue to do so every week." — Censuswide for Microsoft, n=2,003 UK employees, 13 Oct 2025. [link](https://ukstories.microsoft.com/features/rise-in-shadow-ai-tools-raising-security-concerns-for-uk/)
- Among US employees who intentionally use AI at work (37% of US employees), **44%** have used it in ways that contravene their employer's policies and guidelines, and **46%** have put sensitive company information or IP into public AI platforms. — KPMG International + University of Melbourne, US n=1,019, fieldwork Nov 2024–Jan 2025. [link](https://kpmg.com/us/en/media/news/trust-in-ai-2025.html)
- Among Indian employees who intentionally use AI at work, **72%** have used it in ways that contravene policies and guidelines and **81%** have relied on AI output at work without evaluating its accuracy. — same study. [link](https://assets.kpmg.com/content/dam/kpmg/xx/pdf/2025/02/trust-attitudes-and-use-of-ai-india-snapshot.pdf)
- "Fifty-eight percent of APAC respondents say they would use AI even without company approval"; "35% would bypass restrictions to do so." — BCG *AI at Work*, fieldwork July 2025, published 30 Oct 2025. [link](https://www.bcg.com/press/30october2025-asia-pacific-leads-ai-adoption)
- **60%** of Singapore organizations report employees using unauthorised AI tools, with another **14% unsure** — against **79%** that have a formal AI strategy and **88%** that use business AI tools. — Sophos, *The Future of Cybersecurity in APJ*, 5th ed., Aug 2025, Singapore n=105. [link](https://assets.sophos.com/X24WTUEQ/at/2prbj4bsqxkgp5mrn48gcthv/sophos-future-of-cybersecurity-apj-2025-wp.pdf)
- APJ-wide comparator: 46% of organizations are already experiencing employees using unauthorised AI tools, another 12% don't know. — same Sophos report.
- Global base note, quotable: **"Base: Employees who intentionally use AI at work (n=18,898)"** — Figure 44, KPMG/Melbourne global report. This is the sentence that reframes every "% of workers use AI without permission" headline in circulation.

---

## Angles this opens

- **The post is an example of its own thesis.** It argues that unverified AI-adjacent numbers become "known facts" that get built on — and it was itself assembled from a vendor executive's op-ed that transposed two figures from his own company's whitepaper. The strongest version of this piece doesn't hide that; it opens with it. "I wrote this paragraph, then I checked it" is a far better hook than five percentages in a row, and it earns the closing question rather than asserting it.
- **The denominator problem *is* the provenance problem.** The post's current weak point and its actual argument are the same thing. Nobody transposed the Singapore numbers maliciously — a Field CISO misread his own report's country page, a trade outlet published it, and it became citable. That's the mechanism, in miniature, with a named example.
- **Callback to the naming-diagnostic piece** (scheduled 11 Aug): that draft already carries a "DO NOT LIFT without an independent sweep" flag on the MIT NANDA 95% figure and the 44%-of-Gen-Z-sabotaging figure. Same failure mode, two pieces running back to back — worth checking they don't both lean on unswept stats in the same week.
- **Ties to the [[Brief Claim Provenance]] pattern** — vendor-manufactured facts and stale creator-sourced stats, both present here.
