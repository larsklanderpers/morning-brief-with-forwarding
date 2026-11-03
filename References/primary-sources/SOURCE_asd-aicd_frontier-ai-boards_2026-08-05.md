---
type: primary-source-capture
captured: 2026-08-30
method: Claude in Chrome, cyber.gov.au page read directly (WebFetch is ROBOTS_DISALLOWED on cyber.gov.au -- browser, not proxy, same convention as the CISA 403 workaround)
document: Australian Signals Directorate with the Australian Institute of Company Directors,
  "Frontier AI cyber threat considerations for boards of directors"
url: https://www.cyber.gov.au/business-government/protecting-business-leaders/cyber-security-for-business-leaders/frontier-ai-cyber-threat-considerations-for-boards-of-directors
pdf: https://www.cyber.gov.au/sites/default/files/2026-08/frontier_ai_cyber_threat_considerations_for_boards_of_directors.pdf
closes: week-plan_2026-08-31.md Mon 31 [VERIFY] #2 (ASD quotes reached the plan via the 19 Aug extraction, not a fresh read)
---

# VERIFICATION RESULT -- all four corpus quotes CONFIRMED verbatim

| Corpus claim | Status | Exact page text |
|---|---|---|
| "can make cyber attacks faster, more effective, and easier to carry out" | ✅ VERBATIM | "It outlines how AI can make cyber attacks faster, more effective, and easier to carry out." (At a glance) |
| "may rapidly invalidate organisations' current risk tolerance" | ✅ VERBATIM | "This may rapidly invalidate organisations' current risk tolerance." |
| "are currently, and will continue to, fundamentally transform both offensive and defensive cyber capabilities" | ✅ VERBATIM | "Overall, frontier AI models are currently, and will continue to, fundamentally transform both offensive and defensive cyber capabilities." |
| "Organisations that fail to act now may be forced to accept greater business risk" | ✅ VERBATIM | "Organisations that fail to act now may be forced to accept greater business risk and exposure to losses from frontier AI threats." |
| AICD named as co-developer | ✅ CONFIRMED | Named in the Introduction, with its own paragraph describing its mission and focus |

⚠️ **STILL OPEN: the 5 August 2026 publication date is NOT shown on the page body.** The date came
from the 19 Aug dig. Do not print a specific publication date without confirming it from the PDF
properties or the page metadata. "Published in August 2026" is safe; "5 August" is not yet footed.

⚠️ The modal mixture the plan flagged is real and is exactly as described: hedged on outcomes
(can / may), unhedged on the underlying change (are currently, and will continue to).

---

# ★ THE MATERIAL THE PLAN DID NOT KNOW ABOUT: SIXTEEN THRESHOLD QUESTIONS

The plan says "your own signals directorate wrote down the questions." **It wrote down sixteen of
them, under the heading "What threshold questions should boards ask?"** This converts the Mon 31
beat from a gesture into something specific. Verbatim:

1. How vulnerable is our organisation to AI-enabled attacks?
2. What assumptions underpin our current risk assessments, and how might frontier AI threats invalidate those assumptions?
3. Have we reviewed our risk tolerance in light of frontier AI threats and is that risk tolerance still appropriate?
4. If frontier AI models were used to identify and exploit weaknesses across our organisation, what areas of our business would be most exposed?
5. Where could minor weaknesses in our systems and cyber supply chain be combined into a major cyber security incident?
6. Are there known weaknesses in our systems that could become materially more dangerous if identified and exploited at machine speed?
7. Are we relying on vendors and service providers without sufficient governance and oversight, including an understanding of their foreign ownership, control or influence?
8. Do we have visibility of the security and resilience posture of third and fourth-party suppliers within our cyber supply chain?
9. Do we have control over our cyber security fundamentals, such as adherence with a recognised cyber security framework?
10. What legacy technology risks are we carrying and do we have a plan to remediate these risks?
11. Are we delaying addressing any weaknesses due to a perceived low exposure or severity?
12. Would our cyber security operations remain effective if cyber attacks became more frequent, more targeted and more automated?
13. Can we keep the business operational during a serious cyber security incident?
14. If one of our critical systems was compromised, could we continue operating our most important services?
15. If attacks moved from taking days to hours, could we still detect and respond to them effectively?
16. Have our incident response and business continuity plans been updated and tested to capture frontier AI threats?

**Q11 is the sharpest one for Mon 31** -- "Are we delaying addressing any weaknesses due to a
perceived low exposure or severity?" -- because it is a governance question that lands directly on
the severity-function argument Thu 3 Sep is built on. A board being asked whether it is deferring on
perceived severity, in the same month NIST stopped issuing the severity score.

---

# ★ AND THE MATERIAL THAT BELONGS TO THU 3 SEP, NOT MON 31

Under "Reduce software vulnerabilities," the ASD's own prescription:

> "Applying security patches or updates within defined risk-based timeframes or, where operational
> impact is low, automatically."
> "Remediating or mitigating vulnerabilities exceeding defined risk thresholds within defined
> risk-based timeframes based on their severity and exposure."

**Note what is NOT there: a number.** No 48 hours, no two weeks, no 30 days. Like NIST SP 800-40,
the ASD deliberately prescribes a risk-based timeframe rather than a fixed window -- and it hangs
that timeframe on "severity," which is the exact word Thu 3 Sep argues nobody can now supply.
**This is a second signals-agency primary for Thursday's close and it was not in the plan.**

Also relevant to Thu/Fri: "Replace legacy systems" is a named short-term priority, and
"Restrict unnecessary privileges" explicitly includes AI agents -- "Personnel and services,
**including AI agents**, are granted the minimum access to systems required to undertake their
duties." That last one is an Australian government primary for the Tue 25 read-only argument,
arriving after Tue 25 shipped.

---

# The eight strategies, by horizon (verbatim headings)

**Immediate:** Secure attack surfaces · Reduce software vulnerabilities
**Short-term:** Replace legacy systems · Reinforce identity, credential and access management ·
Restrict unnecessary privileges · Prepare for cyber security incidents
**Medium-term:** Adopt AI for cyber defence purposes -- "Artificial intelligence is used for cyber
defence and is secure, controllable, human-supervised and used in an ethical and accountable manner."
**Longer-term:** Modernise for the future (Secure by Design / Secure by Default)

# What the document says about frontier AI capability (verbatim)

> "Frontier AI models present threats that have implications for cyber security operations. This
> includes their ability to: identify vulnerabilities and rapidly weaponise them; chain together
> multiple low severity vulnerabilities into high-impact compromises; perform malicious cyber
> activities with little to no human oversight."

⚠️ Note "chain together multiple low severity vulnerabilities into high-impact compromises" --
**a government primary arguing that the severity rating of an individual CVE is not the unit of
risk.** That is Thursday's argument, made by ASD, and it is stronger than anything currently in
the Thu 3 block.

# Close (verbatim)

> "Organisations that fail to respond to frontier AI threats leave themselves exposed. Boards should
> be pressing management to act now to ensure their organisations do not fall victim to current and
> emerging frontier AI threats, including by supporting targeted investments to enhance cyber
> security and resilience where appropriate."
