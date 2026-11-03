# Research Note -- Fri 16 "Both Sides Automated" (BCBSA footing + the two-sided cost leg)
For: Fri 16 Oct 2026, `week-plan_2026-10-12.md` · Depth: deep (gap-close on top of `research_brief-desk-1_2026-10-10.md` §1) · Date: 2026-10-14

**Read with:** `research_brief-desk-1_2026-10-10.md` §1, which did the first primary read of the BCBSA PDF. This note re-reads every primary, corrects two errors in that note, and closes the gaps it left open: the AHA 5 Oct primary, the "costs more for both" overhead leg, the coding rule itself, and payer-side automation at primary.

## Bottom line
- **The BCBSA number is solid as BCBSA's claim, and weak as proof of AI.** It is in a 3-page, in-house, non-peer-reviewed white paper from the payers' trade association. The AI link is inferred from clinical discordance, never observed, and BCBSA's own conclusion says "may be linked."
- **The provider rebuttal is now footed at primary** (AHA blog, 5 Oct). It does not deny the coding rise. It argues the test is whether diagnoses are clinically supported, and it puts coding intensity at about 0.3 points of commercial spending growth.
- **"Costs more for both" is footable, but only from interested parties on each side,** plus one peer-reviewed policy brief that names the "coding arms race" and predicts "higher administrative friction." There is no neutral, quantified figure for the two-sided overhead. Say that in the sentence.
- **Best new find:** the ICD-10-CM rule itself. Abnormal lab findings "are not coded and reported unless the provider indicates their clinical significance," and when they are out of range "it is appropriate to ask the provider." That rule assumed a human coder with a finite day. BCBSA's fastest-growing codes are exactly the lab-derived ones. This is the rule the counterparty's model reads, at primary.

## What's solid (primaries re-read 14 Oct)

**BCBSA white paper** -- [Hospital Coding Intensity Analysis: Major Bowel Procedures](https://www.bcbs.com/media/pdf/BCBSA-AI-Coding-Intensity-Whitepaper.pdf), Sep 2026 (released 24 Sep). Authors Birkmeyer, Wennberg, Kamons, Chalker. **Interest: BCBSA is the payers' trade association; the paper ends by promoting "the Blue System's unique data assets."**
- "We estimate the added cost to the Blue System at about $942 million over two years."
- "Compared with 2023 baseline rates, hospitals classified 55,158 additional cases as complex. Those cases generated $653 million in incremental reimbursements at an average of $11,800 per excess complex case." Secondary-diagnosis shifts "account for 70% of the incremental inpatient coding intensity costs."
- Complex DRG share: 37.5% (Q1 2023) to 39.8% (Q4 2025). The series is noisy: it peaked at 40.1% in Q1 2025.
- Bowel DRGs 329-331: MCC share 20.2% to 22.7%; non-complex share 36.6% to 32.8%; $60.8M.
- Fastest-growing bump codes are lab-derived: E87.20 acidosis, E87.1 hyponatremia, D62 acute posthemorrhagic anemia. "Many of these diagnoses can be derived from single laboratory values or routine observations, making them particularly well-suited for detection by modern RCM technology." "Ambient listening for observation codes and laboratory data mining appear to be contributing."
- Discordance, 2025, top 25% growth hospitals vs others: complex 75.6% vs 65.0%; ICU 11.5% vs 13.2%; anemia rate 13.7% vs 9.9%; transfusion among anemia cases 16.9% vs 19.3%; median LOS 4.0 both.
- **The AI attribution, verbatim:** the rise "coincides with hospitals adopting new AI-assisted billing software"; "When AI is used to identify abnormal tests, it may be set to flag *all* tests that have results outside of the normal range"; "suggests that the higher rate of anemia is a result of AI-driven coding"; conclusion: AI-enabled RCM tools "may be linked to over $650 million."
- Chalker (BCBSA SVP product and data science) to Reuters, 24 Sep, via [PYMNTS](https://www.pymnts.com/?p=4229952): "If patients are truly sicker, we'd expect to see more treatment."

**AHA response, primary** -- [Better Information, Better Care: How Coding Supports Today's Complex Patients](https://www.aha.org/news/blog/2026-10-05-better-information-better-care-how-coding-supports-todays-complex-patients), AHA News blog, Molly Smith and Jen Holloman, 5 Oct 2026. **Interest: AHA is the hospitals' lobby.**
- "BCBSA's analysis insinuates conclusions about AI-enabled coding without reviewing the underlying medical records."
- "the appropriate test for whether a patient has been correctly coded is not whether reimbursement increased."
- "the absence of an additional procedure does not establish that a diagnosis is invalid."
- AHA's own arithmetic: inpatient coding intensity contributed about **0.3 percentage points** to total commercial spending growth. (That is AHA's derivation from BCBSA's March brief, which it reports attributed about 1.8 of a ~9-point per-member inpatient cost rise to coding intensity.)
- Points at payers' own coding in Medicare Advantage: the OIG audit of BCBS of Alabama (below) and a DOJ suit against Anthem.

**AHA fact sheet** -- [Artificial Intelligence and Coding Intensity](https://www.aha.org/fact-sheets/2026-07-31-fact-sheet-artificial-intelligence-and-coding-intensity). **Dated 31 Jul 2026, displays "August 2026"** (correction to the 10 Oct note, which gave 24 Aug).
- Accusations "are unsubstantiated."
- "some insurers are using automated tools to partially deny claims, forcing providers to engage in burdensome and costly appeals." "these plans want it both ways."
- "more than $1 trillion" a year on administrative functions (Sahni et al., *Health Affairs Scholar*, Nov 2023). No dollar figure for the cost of appeals.

**The rule both models read** -- [ICD-10-CM Official Guidelines, FY2026](https://ftp.cdc.gov/pub/health_statistics/nchs/publications/ICD10CM/2026/ICD-10-CM-October-2025-Guidelines.pdf), Section III (effective 1 Oct 2025; CDC/NCHS host it, approved by the Cooperating Parties: AHA, AHIMA, CMS, NCHS).
- An "other diagnosis" is reportable when it requires "clinical evaluation; or therapeutic treatment; or diagnostic procedures; or extended length of hospital stay; or increased nursing care and/or monitoring."
- "Abnormal findings (laboratory, x-ray, pathologic, and other diagnostic results) are not coded and reported unless the provider indicates their clinical significance. If the findings are outside the normal range and the provider has ordered other tests to evaluate the condition or prescribed treatment, it is appropriate to ask the provider whether the abnormal finding should be added."
- Note: AHA itself co-approves these guidelines. Both sides' arguments are arguments about this paragraph. BCBSA's discordance test is the five-criteria test; AHA's "clinically supported" is the "provider indicates" clause.

**Payer-side automation, at primary or named source**
- **CMS WISeR** ([CMS model page](https://www.cms.gov/priorities/innovation/innovation-models/wiser)): 1 Jan 2026 to 31 Dec 2031; NJ, OH, OK, TX, AZ, WA; technology companies use "AI and machine learning" for prior-auth review of a preselected list (skin substitutes, nerve stimulator implants, knee arthroscopy for OA). Vendors are paid a percentage of the spending averted. "All recommendations for non-payment are determined by appropriately licensed clinicians." **This is the government buying the payer-side model, paid on denials avoided.**
- **Cigna E/M downcoding** from Oct 2025 (level 4-5 reduced one level unless documentation supports it), cited in the npj brief (below) and via TMA in the 10 Oct note.
- **Cigna PxDx** (older, rules-based not AI): ProPublica, 25 Mar 2023, "more than 300,000 claims over two months in 2022," "1.2 seconds of review per claim on average." Cigna "categorically disagree[s]." Via [Becker's](https://www.beckerspayer.com/uncategorized/cigna-physicians-deny-claims-en-masse-without-reading-them-propublica-report/). Use only as the pre-AI baseline of automated review, and say it was an algorithm, not AI.
- **OIG A-07-22-01207** ([highlights](https://www.oig.hhs.gov/documents/audit/11519/A-07-22-01207_highlights.pdf)), Mar 2026: BCBS of Alabama MA contract H0104, 247 of 271 sampled enrollee-years had diagnosis codes the records did not support; at least $7M overpayment for 2018-2019; BCBSAL did not concur. **This is a Blue plan on the other side of the same game** (MA risk adjustment, not commercial DRGs; do not merge them).

**The arms race, peer-reviewed** -- Dai, Kvedar, Polsky, [Policy brief: ambient AI scribes and the coding arms race](https://pmc.ncbi.nlm.nih.gov/articles/PMC12738533/), *npj Digital Medicine* 8:780, 24 Dec 2025 (Johns Hopkins / MGH-Harvard).
- "these tools can increase billing and risk-adjustment coding intensity, prompting payer responses such as downcoding and risk-score recalibration."
- Riverside Health (VA): 11% rise in physician wRVUs, 14% rise in HCC diagnoses per encounter (their ref 5).
- "late adopters may end up missing the temporary upside yet practicing under a lower baseline set after everyone else's gains have been priced in."
- "in commercial FFS markets, employers and workers bear higher premiums until plans lower fees or downcode."
- "an arms race that ends with higher administrative friction, payer pushback, and little improvement at the bedside."

**Cost to both, from inside the fight**
- HCA CFO Mike Marks, Jefferies Healthcare Services conference, Nashville, 15 Sep 2026 ([Becker's](https://www.beckerspayer.com/payer/hca-cfo-on-claims-ai-were-behind-the-payers/)): "They've been working really hard on their version of AI in their claims shop." / "The administrative cost that they have and that we have to administer all of these claims is enormous." / "we do have the opportunity to help each other here."
- Marji Karlin, CRO, NYC Health + Hospitals, Becker's Revenue Cycle conference, Sep 2026: a "rock 'em, sock 'em robot" fight in which "nobody's going to win" ([Becker's](https://www.beckerspayer.com/?p=28862), quoted there).
- Ben Kornitzer, MD, Aetna CMO, Becker's podcast, Jul 2026: urged the industry to resist framing it as "an agentic bot war" (paraphrase plus quoted phrase, same Becker's piece).

## What's contested / watch out
- **"Two years" vs three years of data: resolved, not an error.** Data runs Q1 2023 to Q4 2025; 2023 is the baseline; the $942M is the cumulative increment over 2024-2025. AHA's blog itself calls it a "cumulative two-year total." Becker's flagged it as inconsistent; it is not. Do not repeat the Becker's critique.
- **The $942M vs the $650M.** $942M is total incremental inpatient coding-intensity cost; ~$653M is the secondary-diagnosis share (70%) that BCBSA links, "may be linked," to AI. If the piece says "AI cost the Blues $942M," that overstates BCBSA's own paper. Safe phrasing: BCBSA puts the added cost at about $942M over two years and says AI tools "may be linked" to more than $650M of it.
- **Scale.** AHA's 0.3-point figure and the 37.5% to 39.8% move are both small. The piece's point is the mechanism and the escalation, not the size; let the reader see the size is disputed.
- **Denial cost to hospitals: $19.7B a year** -- [Premier](https://www.beckershospitalreview.com/?p=240478) (21 Mar 2024; 516 hospitals; 2022 claims; $43.84 per denial; 54.3% of private-payer denials eventually overturned). **Interest: Premier sells revenue-cycle and denial-management services.** Usable only named, dated and with the interest stated.
- **CAQH Index 2025** ([executive report](https://index.caqh.org/hubfs/Index/CAQH_IndexReport_2025_Executive%20Report_v6.pdf)): $75B on administrative transactions; about $3.39 electronic vs $8.03 manual per provider transaction; "more than half of health plans and about one-quarter of providers use AI." CAQH is plan-founded; the AI-adoption gap is the useful bit (it matches Marks's "behind the payers") but name the source.
- **Becker's "hospitals say they're losing"** is qualitative only; no denial-rate data in the piece.

## Couldn't verify -- DO NOT PRINT (carried from 10 Oct, re-checked 14 Oct)
- Chalker's "completely one-sided blood bath" and Abridge's "dystopic future": still AI Chat Daily only; PYMNTS's Reuters-sourced write-up carries neither.
- Kodiak "revenue leakage +25%"; CVS/Aetna "$20B AI spend": single-source.
- "63% use AI in revenue cycle": no named survey.
- The npj figure for Riverside is the brief's citation of its ref 5; the underlying Riverside source was not opened. Attribute to the npj brief, not to Riverside.
- No neutral, quantified figure for the combined two-sided overhead exists in anything reached. **Never write that the exchange "costs both sides $X."**

## The economics
- The coder's cost to find a codeable lab value used to be a human minute per chart. BCBSA's codes are the ones where that minute fell to near zero: "derived from single laboratory values." Each excess complex case was worth about $11,800 to the hospital.
- The payer's counter is also priced per claim, and the government now pays the vendor a share of what it averts (WISeR). Each side's model is paid by the size of the other side's loss.
- The overhead lands on both ledgers (Marks: "enormous"), the premium lands on employers and workers (npj), and the early adopter's gain becomes everyone's new baseline (npj). That last line is the cleanest footing for Fri pt 2, "the exchange pays twice."

## Drop-in facts
- BCBSA estimates the added cost to the Blue System "at about $942 million over two years," and says AI billing tools "may be linked" to more than $650 million of it. [BCBSA white paper, Sep 2026; payer trade group, not peer-reviewed]
- Top-growth hospitals coded anemia 38% more often than peers, yet transfused fewer of those patients: 16.9% vs 19.3%. [BCBSA]
- "Abnormal findings ... are not coded and reported unless the provider indicates their clinical significance." [ICD-10-CM Official Guidelines FY2026, Section III]
- "the appropriate test for whether a patient has been correctly coded is not whether reimbursement increased." [AHA, 5 Oct 2026; hospitals' lobby]
- "The administrative cost that they have and that we have to administer all of these claims is enormous." [HCA CFO Mike Marks, 15 Sep 2026]
- "an arms race that ends with higher administrative friction, payer pushback, and little improvement at the bedside." [Dai, Kvedar, Polsky, npj Digital Medicine, Dec 2025]
- CMS's WISeR pays its AI prior-auth vendors a share of the spending they avert. [CMS, model page]

## Angles this opens
- **Sun 18 footing, pt 3 "the rule was the subsidy":** the ICD-10-CM abnormal-findings paragraph is the cleanest exhibit of a rule that assumed the other side would not bother. "It is appropriate to ask the provider" is fine at a human's query volume and a different rule at a model's. Hand this to the Sunday chat; Friday should use it once, lightly, and not argue Sunday's point.
- **Collision guard for Fri:** WISeR's pay-on-averted-spend is a pricing-unit fact and sits close to Fri 9's meter and definition. Use it as "each side's model is paid by the other side's loss," never as "whoever sets the unit."
- **His loyalty and rewards seat** has no outside footing in this note by design; it is his. The structural parallel to listen for in the interview: a rule (an earn rule, a redemption rule, a claim rule) that assumed the member would not read every edge, and what the operator's counter-model costs.
