# Research Note -- The Party of Record (who carries the loss when a deployed model is wrong)
For: substack_draft_party-of-record_2026-09-21 · Depth: deep · Date: 2026-09-20
Method: local corpus first (thin: no prior insurance-exclusion or Illinois-liability footing; Bessent footed secondary in research_slowdown-positioning_2026-09-16.md), then three parallel web fan-outs (insurance market / law / buyer's ledger). No curl workarounds; unreached sources listed.

## Bottom line
The plan's test -- "somebody is repricing this now" -- PASSES, and the repricer is the insurance market, not the regulator. Since January 2026 ISO (Verisk) forms let any carrier strip generative-AI claims out of standard general liability; Berkley's "absolute" AI exclusion reaches any use of AI "by any person or entity" in D&O/E&O/fiduciary; and a separate, affirmative market (Armilla/Chaucer at Lloyd's, Munich Re aiSure, Testudo) now sells model-error cover as its own line and prices it off the model. At the same time the law is moving toward the deployer: California AB 316 removes "the AI did it" as a defense from anyone who "developed, modified, or used" AI, Colorado's replacement act shields developers from "off-label" deployer uses, and the AG actions that exist hit the organizations that used the tool. **Adoption of the exclusions is uneven and nobody has counted it** -- write "the door is being closed form by form", not "the market has shut".

## What's solid
- **ISO generative-AI exclusions, effective January 2026.** CG 40 47 (Coverage A and B), CG 40 48 (B only), CG 35 08 (products/completed ops). Verisk definition: "a machine-based learning system or model trained on data with the ability to create content or responses, including text, images, audio, video or code." -- Big I / IndependentAgent.com 21 Oct 2025; Insurance Journal 22 Jul 2026 and 17 Aug 2026; Business Insurance 7 Apr 2026. (Verisk primary returned no body text; SERFF unreached.) https://www.independentagent.com/vu_resource/verisk-to-roll-out-new-general-liability-exclusions-for-generative-ai-exposures/
- **Verisk does not know how many carriers have adopted them.** Joe Lam, Insurance Journal 22 Jul 2026: doesn't know "how many insurers are adopting them yet."
- **Berkley "absolute" AI exclusion (D&O / E&O / fiduciary):** bars "Loss on account of any Claim... based upon, arising out of, or attributable to... any actual or alleged use, deployment, or development of Artificial Intelligence by any person or entity." AI defined broadly as any machine-based system that infers outputs. -- Hunton Andrews Kurth, 28 May 2025 (secondary, direct quote of the form). https://www.hunton.com/hunton-insurance-recovery-blog/the-continued-proliferation-of-ai-exclusions
- **FT, 23 Nov 2025, "Insurers retreat from AI cover as risk of multibillion-dollar claims mounts":** AIG, Great American, W. R. Berkley sought approval to exclude AI liabilities; underwriter called outputs "too much of a black box"; Aon: carriers can absorb a $400m single loss, not an "agentic AI mishap that triggers 10,000 losses at once." FT itself paywalled; via TechCrunch 23 Nov 2025. AIG later said "no plans to implement them at this time." https://techcrunch.com/2025/11/23/ai-is-too-risky-to-insure-say-people-whose-job-is-insuring-risk/
- **Affirmative cover exists and is priced off the model.**
  - Chaucer/Armilla (Lloyd's), 22 Apr 2025: covers hallucinations, model drift, "deviations from expected AI behavior." Primary. https://www.chaucergroup.com/news/press-release-chaucer-co-develops-new-ai-insurance-product-with-armilla-ai
  - Armilla limits to $25m per organization (primary; page date ambiguous 2025/Jan 2026).
  - Chaucer/Armilla "Vanguard AI," 10 Feb 2026: standalone AI tower next to cyber/tech E&O. Chaucer's Piers Tuggey: AI exposure "starts to distort coverage lines it was never priced for." Primary.
  - Munich Re aiSure FAQ: premium set by "the quality of the model and its performance stability"; offers "Own Damages" cover for deploying companies. Primary. https://www.munichre.com/en/solutions/for-industry-clients/insure-ai/faq.html
  - Testudo (Lloyd's coverholder): $9.25m per insured (Fintech.Global 9 Mar 2026, secondary).
  - ElevenLabs / AIUC (12 Feb 2026, primary): insurance for enterprises using its voice agents covering "an AI agent providing incorrect information to a customer."
- **Underwriters now ask about the model.** Westfield Specialty, Business Insurance 7 Apr 2026: "What models are you utilizing? How were decisions made? What checks exist?"
- **Gallagher (Feb 2026, primary):** "one in five" insurance professionals said a client had an AI-related loss or claim in the past year, "with just over half covered fully by insurance." https://www.ajg.com/news-and-insights/features/ai-adoption-and-risk-benchmarking-2026/
- **Gallagher Re (Mar 2026, via Risk & Insurance, secondary):** US gen-AI lawsuits up 978% 2021-2025; companies deploying third-party AI "shouldering most of the risk"; vendor contracts "cap liability at 12 months of fees and offer no performance warranties."
- **California AB 316, Civil Code §1714.46, in force 1 Jan 2026:** a defendant that "developed, modified, or used" AI may not assert that the AI "autonomously caused the harm." (CalMatters / Baker Botts, secondary; leginfo blocked by robots.)
- **Colorado SB 26-189, signed 14 May 2026, effective 1 Jan 2027** (repeals and replaces SB 24-205, which never took effect): fault split by "relative responsibility"; "Developers are shielded from liability for off-label deployer uses"; clauses indemnifying a party for its own discriminatory acts are void. (Holland & Knight, secondary.)
- **Illinois SB 3444 (the bill OpenAI backed):** safe harbor for frontier developers from "critical harms" (100+ deaths, $1B+ property, CBRN) unless intentional or reckless, conditioned on publishing a safety protocol. Re-referred to Assignments 22 May 2026 = dead. Illinois enacted SB 315 instead (signed 6 Jul 2026, eff. 1 Jan 2027), no shield. ilga.gov bill status (primary); Fortune 17 Apr 2026. Anthropic called SB 3444 a "get-out-of-jail-free card" (Fortune).
- **Federal preemption draft (Great American AI Act discussion draft, 4 Jun 2026):** preempts state rules on development, "does not apply post-deployment" (DLA Piper). Not introduced.
- **AG actions against deployers:** Massachusetts v. Earnest Operations, 10 Jul 2025, $2.5M, the lender that used AI underwriting models (mass.gov primary). Pennsylvania / GEICO, 22 May 2026, the insurer that "utilized a tool with artificial intelligence features" in a cancellation; vendor unnamed; process remedy, no dollar figure (attorneygeneral.gov primary).
- **Vendor terms (primaries):** Anthropic Commercial Terms: "THE SERVICES AND OUTPUTS ARE PROVIDED 'AS IS'... ANTHROPIC DOES NOT WARRANT... OUTPUTS ARE ACCURATE, COMPLETE OR ERROR-FREE"; indemnity IP-only; cap = fees in prior 12 months. OpenAI Services Agreement (eff. 1 Jan 2026): indemnity IP-only; cap 12 months fees. Microsoft Customer Copyright Commitment: IP only, conditional on mitigations. **CAUTION: Fri 18 owns contract text. At most one line here.**
- **Costs landed on deployers:** Deloitte Australia refunded ~A$97,000 of an A$440,000 DEWR contract over AI-fabricated citations (Oct 2025; CFO Dive quoting DEWR). Charlotin database: 2,044 AI-hallucination court cases, 1,397 US, as of 19 Sep 2026 (primary). EY Responsible AI Pulse (Oct 2025, 975 large firms): 99% reported financial losses from AI-related risks; average ~US$4.4M (broader than output error; 2025 fieldwork).

## What's contested / watch out
- **How widespread the exclusions are.** Marsh's Greg Eskins (Business Insurance, 7 Apr 2026): market "restrained in taking any drastic actions." Gallagher's John Farley: "a few carriers." Lathrop GPM (Insurance Journal 17 Aug 2026) forecasts "rapid adoption... in most lines" -- a forecast. Testudo's "95% of carriers" is a vendor with an interest in the outcome; do not use as data.
- **Illinois regulators pushed back** on a gen-AI exclusion, "asking what real-world scenario" it was meant to capture (Beinsure 1 Feb 2026, secondary, no SERFF numbers).
- **Texas v. Pieces Technologies (2024)** targeted the VENDOR for accuracy marketing, not the four hospitals. Runs against the thesis; if used, use honestly.
- **Mobley v. Workday** lets claims proceed against the vendor as "agent." Runs partly against the thesis; the honest read is that liability is being argued on both sides, and the deployer is in the chair either way.
- **Colorado 2026 enforcement halt mechanism** (magistrate vs AG pause) -- sources disagree. Not needed.
- **Silent coverage:** policies without explicit exclusions may still cover (Insurance Journal Aug 2026).

## Couldn't verify
- **Any insurance claim paid or denied for AI model error.** None found (Shumaker, Fenwick cite none). Do NOT write that a claim has been denied.
- **A US ruling holding a deployer liable for chatbot output (2025-26).** None found. Do not claim a US precedent.
- **Bessent quote at primary.** Hearing confirmed at financialservices.house.gov (EventID 411218); written statement has no AI content; quote is oral, via FedScoop and Gizmodo only. Use as "reported by FedScoop" or attributed without implying transcript.
- SB 3444 text itself (ilga PDF blocked) -- the "does not shift to deployers" read is from summaries.
- Berkley form number / state filing dates (gridex.dev only).
- Any AI-specific rate increase or sublimit data for Jun-Sep 2026.
- ElevenLabs $50m limit (secondary only).

## The economics
- The vendor's exposure is capped at twelve months of fees and excludes accuracy. The deployer's exposure is uncapped and now, in general liability and management liability, potentially uninsured unless bought back.
- The buy-back is a new line: Lloyd's capacity at $25m per organization (Armilla), $9.25m (Testudo), priced off "the quality of the model and its performance stability" (Munich Re). The insurer is underwriting the model; the buyer pays the premium for a model it did not build and cannot inspect.
- Aon's framing gives the scale reason: one $400m loss is absorbable, 10,000 simultaneous losses from one agent failure are not. Correlated model error is why carriers carve it out.
- Gallagher: of AI-related client losses, only "just over half" fully covered.

## Drop-in facts
- Since January 2026, ISO form CG 40 47 lets a carrier remove generative-AI claims from a standard general liability policy. [Big I Oct 2025; Insurance Journal Jul 2026]
- Verisk told Insurance Journal in July it does not know how many insurers are adopting them yet. [IJ 22 Jul 2026]
- Berkley's exclusion bars claims arising out of "any actual or alleged use, deployment, or development of Artificial Intelligence by any person or entity." [Hunton, May 2025]
- Munich Re prices aiSure by "the quality of the model and its performance stability." [Munich Re FAQ]
- California, since 1 Jan 2026: a company that "developed, modified, or used" AI cannot argue the AI "autonomously caused the harm." [Civ. Code §1714.46]
- Colorado's replacement law shields developers from liability for "off-label deployer uses." [SB 26-189 via Holland & Knight]
- Pennsylvania's AG went after GEICO, the insurer that "utilized a tool with artificial intelligence features," not the tool's maker. [PA AG, 22 May 2026]

## DO-NOT-PRINT (binds every revision of this piece)
- Not that any insurance claim for AI error has been paid or denied.
- Not a US court ruling holding a deployer liable for chatbot output.
- Not "the market has shut / insurers won't cover AI" -- adoption is uncounted and uneven.
- Not Testudo's "95%" as data.
- Not SB 3444 as law, or as a transfer to deployers; it died, and it was a developer shield for catastrophic harms.
- Not Bessent's quote as from a transcript or his written statement.
- Not Moffatt (Fri 18 owns it). Not the EULA-at-scale line (Sun 20). Not an argument from contract text (Fri 18).
- Not the "$145,000 in sanctions" total (blogs only). Not the A$290,000 Deloitte figure.

## Angles this opens
- Fri 25 (What the Transfer Costs): the affirmative AI line is the thing the channel can resell or require; the exclusion is what lands on the MSP's own E&O.
- Thu 24 (The Shield): Bessent's "blank check on liability" and SB 3444 are the developer-side shield; Monday is the deployer-side bill. Keep the waiver out of Monday.
