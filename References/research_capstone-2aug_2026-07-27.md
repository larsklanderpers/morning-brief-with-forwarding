# Research Note — the 2 August peg, and the OAIC enforcement clock
For: `substack_draft_capstone-control-design_2026-08-02` (Sunday capstone) · Depth: deep · Date: 2026-07-27

## Bottom line

**The capstone's publication-day peg as written in the week plan is wrong, and the correction makes the piece stronger.** The week plan says "the EU AI Act becomes fully applicable Sunday 2 Aug — the day this publishes." It does not. The Digital/AI Omnibus deferred the high-risk obligations by sixteen months to two years, and what actually lands on 2 August is the *transparency* layer -- tell people they are dealing with AI. That is a sign, not a governor, which is Friday's exact distinction arriving in the one jurisdiction everybody points to as the grown-up. Second finding: the OAIC's final ADM guidance has **not** landed -- still consultation -- so the standalone clubs piece still has nothing to hang on. But the enforcement material that has surfaced is better suited to the capstone anyway, and it produces a striking inversion: Australia's binding automated-decision obligation lands 10 December 2026, a **full year before** the EU's deferred high-risk rules.

## What's solid

### The EU AI Act 2 August 2026 date -- what moved and what didn't

- **High-risk obligations deferred.** Stand-alone Annex III systems: **2 August 2026 -> 2 December 2027**. High-risk AI embedded in Annex I regulated products: **2 August 2026 -> 2 August 2028**. Consistent across [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/), [Travers Smith](https://www.traverssmith.com/knowledge/knowledge-container/eu-agrees-to-delay-key-ai-act-compliance-deadlines/), [Pinsent Masons](https://www.pinsentmasons.com/out-law/news/law-delaying-eu-high-risk-ai-rules-finalised), [Freshfields](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/eu-ai-act-unpacked-34-the-final-digital-omnibus-on-ai-key-amendments-to-the-a-102nber), [Latham](https://www.lw.com/en/insights/ai-act-update-eu-resolves-to-change-rules-and-extend-deadlines).
- **2 August is NOT cancelled.** The **Article 50 transparency obligations** apply from 2 August 2026 as originally scheduled -- disclosure when an AI system interacts with a person, and marking of AI-generated or manipulated content. Source phrasing worth keeping: *"2 August 2026 is not cancelled"* -- the deadline narrowed rather than disappeared ([Innovaiden](https://www.innovaiden.com/insights/eu-ai-act-august-deadline-moved-digital-omnibus)).
- **One carve-out inside that.** Article 50(2) machine-readable marking of AI-generated content is deferred to **2 December 2026** for systems already on the market before 2 August 2026. Systems placed on the market from 2 August onward comply immediately.
- **New prohibited practices from 2 December 2026**, including nudifier and CSAM-generating systems.
- **Penalties unchanged:** up to EUR 35M or 7% of global turnover for prohibited practices; up to EUR 15M or 3% for other obligations including high-risk and transparency duties.
- **Why it moved:** industry pressure. Multiple outlets frame it plainly -- ["EU to delay 'high risk' AI rules until 2027 after Big Tech pushback"](https://www.aol.com/articles/eu-delay-high-risk-ai-124536847.html).

### The OAIC picture

- **Final ADM guidance has NOT landed.** The OAIC's own page is still titled ["Consultation on Guidance for Transparency in Automated Decision Making"](https://www.oaic.gov.au/engage-with-us/consultations/consultation-on-guidance-for-transparency-in-automated-decision-making). The week plan's watch item ("instant clubs-audience piece when it lands") has **not** fired. Do not write the standalone yet.
- **The obligation itself is unchanged and binding: 10 December 2026.** APP entities must disclose in their privacy policy which substantially automated decisions their systems make about people.
- **Enforcement posture is the new material.** Per `AI Briefs\ai_brief_2026-07-26.md` citing Pinsent Masons: the OAIC is reinforcing **"Notice is not consent"**; an **APP 1.4 privacy-policy sweep is already underway**; non-compliant firms face the regulator's "recently expanded regulatory toolkit." Lars's own brief flags it: the OAIC "has explicitly moved from guidance mode to enforcement posture... building a case file, not issuing warnings."
- **Public-opinion leading indicator:** the OAIC's 2026 Australian Community Attitudes to Privacy Survey shows a substantial majority reporting heightened sensitivity to AI use of personal information (`ai_brief_2026-07-25.md`, via IAPP).
- **The UK third leg** (`ai_brief_2026-07-25.md`): the UK has forced cloud providers to answer *directly* to financial regulators -- reaching through the customer to the provider. Lars's own strategic take: "Australian APRA (CPS 230) and the EU are watching; this framework will propagate."

## What's contested / watch out

- **Exact in-force status of the Omnibus.** Pinsent Masons (6 Jul 2026) reported the text finalised by Parliament and Council but "awaiting formal publication in the Official Journal," taking effect "in the coming days." `ai_brief_2026-07-26.md` says "EU AI Act Omnibus Regulation entered into force — July 2026." That is almost certainly right, but it is a brief citing the Commission rather than the Official Journal itself. **Re-confirm OJ publication before printing a bare "is in force"** -- or write it as "finalised in July" and sidestep the question.
- **"Fully applicable" is now a phrase to avoid entirely.** It was never precisely right and it is now actively wrong. Say which obligations, on which date.
- **"Notice is not consent"** reaches us through Pinsent Masons via the brief, not from an OAIC primary document in this pass. Attribute to the OAIC's consultation position rather than quoting it as a published OAIC line, or pull the primary before quoting.

## Couldn't verify

- Whether the OAIC has signalled a date for the final ADM guidance. Nothing in this pass.
- Whether the Omnibus changed anything about GPAI (general-purpose AI model) obligations, which had their own August 2025 start. Not examined -- out of scope for the capstone, but do not assert anything about GPAI timing without checking.

## The economics

Penalties are the cost side and they did **not** move: EUR 35M or 7% of global turnover for prohibited practices, EUR 15M or 3% for transparency and high-risk breaches. So the EU deferred the *obligation* by sixteen months while leaving the *price of getting it wrong* exactly where it was. That is worth a sentence: the bill did not get smaller, the invoice date did. Pair with the Vault keeper phrase already in the week plan -- firms that have not made the design decision are accruing **"governance debt that converts to penalty exposure."**

## Drop-in facts (each sourced)

- "Stand-alone high-risk obligations moved from 2 August 2026 to 2 December 2027; high-risk embedded in regulated products, to 2 August 2028." [Gibson Dunn / Pinsent Masons / Travers Smith]
- "2 August 2026 is not cancelled." What survives is Article 50 -- the obligation to tell people they are dealing with AI. [Innovaiden]
- "Up to EUR 35 million or 7% of global turnover" -- penalties unchanged by the deferral. [Innovaiden]
- The delay followed Big Tech pushback. [Reuters/AOL syndication]
- Australia's automated-decision disclosure obligation binds from **10 December 2026** -- a year before the EU's deferred high-risk rules. [OAIC; Wednesday's piece]
- OAIC: "Notice is not consent"; APP 1.4 sweep already underway; "recently expanded regulatory toolkit." [Pinsent Masons via `ai_brief_2026-07-26.md`]
- The UK now makes cloud providers answerable directly to financial regulators. [`ai_brief_2026-07-25.md`]

## Angles this opens

- **The peg gets better.** Original: "a designed framework switches on the day this publishes." True version: the most designed framework anybody has written put a date on the hard part, then moved it sixteen months under industry pressure -- and what lands on 2 August is the requirement to *tell people*. A disclosure duty. **A sign, not a governor** -- Friday's exact distinction, arriving in the jurisdiction everyone holds up as the adult in the room.
- **The four-jurisdiction spine, all verified:** the EU designed it and deferred the enforcing half; the UK reached through to the provider; the US shelved four attempts, then cabled allies that there is no kill switch while Congress drafted one; Australia declines to classify at all and makes you determine and defend materiality yourself (CPS 230), with a hard 10 December date for automated decisions. Four designs, one week.
- **The inversion worth leading on:** the country Wednesday called framework-less has a binding obligation landing a **year earlier** than the EU's high-risk rules. "No framework" turned out to mean "no framework yet, and an obligation on a hard date regardless."
- **CPS 230 as the thesis in a prudential standard.** APRA declines to classify your vendor; materiality is functional and the determination is yours to make and defend. That IS "control is not a default, it is a design decision," written by a regulator. Lets Lars land the 21 July CPS 230 imprecision in a clause -- evidence for the argument rather than a second correction box (the 24 July piece already ran the formal one).
