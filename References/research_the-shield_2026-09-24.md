# Research Note -- The Shield: what the antitrust waiver actually covers, and who is already suing
For: Thu 24 Sep, "The Shield" (AI growth) -- no draft yet · Depth: deep · Date: 2026-09-21 (written Mon 21 for Thu 24)
Builds on, does not repeat: `research_slowdown-positioning_2026-09-16.md` (the seating chart, Ferguson, Bessent, Zuckerberg, Nadella, Huang, markets). Read that for positions as of 16 Sep. This note covers the shield's text and what moved 16-21 Sep.

## Bottom line
The shield has text now, and the text is stranger than the debate about it. S. 5105 (Schiff-Banks, introduced **23 July 2026** as a China-distillation security bill) already contains a clause letting two or more companies "coordinate or enter into agreements" to delay or limit the "release, deployment, use, development, training, testing, or evaluation" of AI, on written notice to the Assistant Attorney General -- and the price-fixing / market-allocation carve-outs apply only to the information-sharing clause, not to the delay clause; the notice itself is withheld from FOIA "without discretion." Meanwhile the exposure the shield exists to remove stopped being hypothetical on **18 Sep**: four paid consumer subscribers filed a Sherman Act s.1 class action in N.D. Cal. seeking **treble damages** against Anthropic, OpenAI, SpaceXAI and Google, built entirely on the labs' own public statements. Washington's read is cool: Hawley and Cruz against, Ferguson "deeply suspicious," and DOJ's Associate AG saying labs could simply come in for a meeting and none has asked. **Trust level: high on the bill text and the complaint (both read at primary); medium on the DOJ remarks (paraphrase-heavy wire copy).** The two-liabilities distinction survives and sharpens: nothing in S. 5105 touches liability for what the models do, and the only live liability proposal in the Senate (Thune-Klobuchar-Cruz "duty of care") runs the other way.

## What's solid

**The bill (primary, govinfo, read raw text of Secs. 3-4):**
- S. 5105, *Collaboration on Adversarial Threats and Security Risks Act*, Mr. Schiff and Mr. Banks, introduced 23 July 2026. Purpose line: "To establish the applicability of antitrust laws to the sharing of artificial intelligence frontier model risks." House companion by Reps. Latta and Whitesides the same day. [govinfo.gov/app/details/BILLS-119s5105is] [schiff.senate.gov press release] [whitesides.house.gov/2026/07/23/...]
- **Sec. 3(a)(2), the pacing clause, verbatim:** "Two or more non-Federal entities to coordinate or enter into agreements for the exclusive purpose of reducing covered artificial intelligence security risks via delaying or otherwise limiting the release, deployment, use, development, training, testing, or evaluation of artificial intelligence, provided that the non-Federal entities submit to the Assistant Attorney General, before undertaking the proposed coordinated delay or limitation, written notice detailing the specific covered artificial intelligence security risk and the scope of the proposed restriction."
- **Sec. 3(c):** it is an **affirmative defense**; the entity claiming it carries the burden "by a preponderance of the evidence" that it acted "in good faith and for the exclusive purpose."
- ★ **Sec. 3(d)(1) -- the catch:** "Subsection (a)(1) shall not be construed to permit price-fixing, allocating a market between competitors, monopolizing ..., boycotting, or exchanges of price or cost information." **It names (a)(1), the information-sharing clause, only. The coordinated-delay clause (a)(2) carries no such carve-out.** (A summarising fetcher reported the carve-outs as applying to the whole exemption. The raw text says otherwise. Quote the text, not a summary.)
- **Sec. 3(d)(2):** private rights of action survive only for violations "that are not exempt under this section." So exempt pacing would bar a Buist-type treble-damages suit.
- ★ **Sec. 3(e):** the notice to DOJ, and anything derived from it, is "used solely for the purpose of section 4," "exempt from disclosure under section 552," and "withheld, without discretion, from the public." **The public never sees what was agreed to be slowed, or why.**
- **Sec. 4:** the only backstop is the Attorney General seeking an **injunction** -- if the entities fail the burden of proof, or if the AG shows the action is "reasonably likely to result in an overall increase in covered artificial intelligence security risks." No damages remedy for the government in the Act.
- The "covered AI security risk" definition is broad enough to carry pacing: it includes AI reducing developer oversight and autonomous self-improvement with dangerous consequences, alongside theft, weapons and infrastructure (summarised read; re-read the definition clause raw before quoting it).
- **Sunset / preemption:** none found in the text as read. ⚠️ That read was by a summarising fetcher; confirm by scanning the full text before printing "no sunset."

**The NDAA attempt (secondary, one outlet, but specific):** Banks and Schiff sought to add the exemption to the annual defense bill; it went into a manager's package with Wicker and Reed's approval but was not enacted; the NDAA itself stalled over the summer. Semafor, 16/17 Sep. [semafor.com/article/09/16/2026/senators-sought-to-add-ai-antitrust-exemption-to-defense-bill]

**The lawsuit (primary, the complaint PDF, read):**
- *Buist et al. v. Anthropic PBC*, N.D. Cal. (San Francisco), **3:26-cv-10693**, filed **18 Sep 2026**. Defendants: Anthropic PBC, OpenAI OpCo LLC, SpaceXAI, Google LLC. [complaint PDF via chatgptiseatingtheworld.com/2026/09/18/...] [Bloomberg Law docket confirmation]
- Plaintiffs: four individuals -- Charles Buist (FL), Cheyenne Hunt (CA), Christine Bullock (CA), Nick Spetsas (FL) -- paid consumer subscribers (three to all four products, Bullock to Claude only). Counsel reported as Trial Lawyers for Justice (Bloomberg Law).
- Class: "All persons in the United States who, from September 12, 2026 through the date on which the effects of Defendants' unlawful conduct cease, purchased directly from one or more Defendants a paid individual consumer subscription providing premium access to ChatGPT, Claude, Grok, or Gemini."
- One count, Sherman Act s.1; relief: **treble damages under Clayton s.4**, preliminary and permanent injunction under Clayton s.16, interest, fees.
- Theory, verbatim: "An agreement among competitors to reduce the quality of their products and the rate at which those products improve is an agreement to restrict output." And: "Plaintiffs challenge only what the antitrust laws forbid: an agreement among competitors about how fast their competing products will improve."
- ★ **Built from the labs' own mouths.** The complaint says the agreement was "proposed in public, accepted in public, and confirmed in public" (TNW's reading of para. 2): the 12 Sep essay as offer; Altman on 14 Sep that progress "should be slower than it otherwise could be" and that OpenAI would not wait for an exemption; Lehane on 15 Sep confirming weeks of talks; Hassabis's 14 July standards-body proposal. No leaked documents.
- ★ **The plaintiffs are not accelerationists.** Hunt: "we deserve real AI safety standards, not shady deals cut by an unaccountable cartel of billionaires in a back room" (LiveMint). The complaint disclaims any challenge to unilateral slowing, independent evaluators, safety research or petitioning Congress, including for an exemption (TNW). **The suit is a safety-side argument that a private pact is the wrong instrument.**
- Status: no defendant response as of 21 Sep; pleading stage.

**Washington's read, 15-21 Sep:**
- Hawley, 15 Sep: "There is absolutely no world in which I will consent to giving the most powerful companies in the history of the world -- a small group of three or four of them -- antitrust exemptions so they can what ... collude together? Absolutely no way that's happening." (The Hill tech newsletter, 16 Sep, read)
- Cruz, Senate Commerce hearing 15 Sep: "To watch AI CEOs saying, 'We're about to destroy the world, so give us control of the government so we can lock in our monopoly status and prevent any innovation from challenging us,' is just lunacy." (same)
- Ferguson: "deeply suspicious" of requests for relief; companies are "asking for barriers to entry" (Reuters/Leah Nylen via Insurance Journal, 21 Sep). His earlier "alarm bells" line is in the 16 Sep note.
- **DOJ, Associate Attorney General Stanley Woodward, Fordham, 17 Sep:** "To the extent that anybody at any of the frontier labs wants to come see us about a concern, they would get a meeting." "That meeting hasn't been requested." DOJ is weighing whether to update existing interagency guidance on cybersecurity cooperation. Wash. Examiner paraphrases him as saying cybersecurity cooperation "does not appear anticompetitive." [insurancejournal.com/news/national/2026/09/21/886227.htm] [washingtonexaminer.com/.../4732514/]
- Cruz on a possible Commerce markup: "working hard," but "the question is, do we get bipartisan agreement?" (secondary aggregator, ~20 Sep). No date announced.

**Existing law already has shields -- and neither fits a private pace pact (primary, statute):**
- **NCRPA (15 USC 4301-4306):** joint ventures that file notice get their exposure cut from treble to **"actual damages"** (4303(a)). But 4301(b) excludes from "joint venture" any agreement restricting production "other than the production by such venture," restricting sale or licensing, or allocating a market. **Pacing each lab's own products is the excluded thing.** So the de-trebling shield on the books does not reach it.
- **Defense Production Act s.708 (50 USC 4558):** a full antitrust **defense**, civil and criminal, for voluntary agreements -- but only where the President (or delegate) initiates or supervises, the AG and FTC are consulted and sit in the meetings, transcripts and agreements are public (subject to FOIA exemptions), the AG finds the purpose cannot be met less anticompetitively, and agreements **expire after five years**. Business Model Analyst (21 Sep) makes the argument that this is the shield that exists: "A pace pact's legal value equals the government's fingerprints on it." [businessmodelanalyst.com/ai-slowdown-pact-antitrust-waiver-pace-frontier/]
- ★ **The contrast writes itself:** the existing shield buys immunity with a public record and government in the room; S. 5105's delay clause buys it with a sealed notice.

**The other liability, which the shield does not touch:**
- Nothing in S. 5105 addresses product, tort or consumer-protection liability for what a model does. It is antitrust only.
- **Thune-Klobuchar (with Cruz pushing a markup) would impose a legal "duty of care" on frontier developers**, and reportedly let the government block release of unsafe models. Politico, 15 Sep: "would impose a legal duty on AI companies to lessen the harm their models could cause." No bill text or number yet. [politico.com/news/2026/09/15/can-anyone-hold-back-the-ai-juggernaut-01075944]
- Neil Chilson (Abundance Institute, former acting FTC chief technologist), same piece -- the best line on the compliance-as-shield trap: "The worst possible outcome we could get is that we make a list of practices that we think make things safe, and then say: 'If you check all these boxes, you're going to be clear from any liability if things go wrong.'"
- Lina Khan (X, 13 Sep, via Politico): "Law enforcers already have authority to charge companies and their CEOs for creating and releasing dangerous, unvetted, or defective products."
- FRONTIER Act (Obernolte-Trahan, House, 23 July; OpenAI endorsed 16 Sep): tiered transparency, independent audits, incident reporting. Trahan: it gives the largest developers "a single, clear national standard." No liability shield or antitrust provision on the press release. **"Single national standard" hints at preemption; the release does not say it -- do not assert it.** [obernolte.house.gov press release]

**Politico poll -- now footed, and corrected:**
- POLITICO Poll by **Public First**, 13-15 Sep, **2,064 U.S. adults online, +/-2.2**. 63% say at least a "moderate" risk that advanced AI could destroy humanity (Harris voters 70%, Trump voters 60%). A plurality favors pausing development of more advanced models. [politico.com/news/2026/09/16/poll-ai-technology-risks-humanity-trump-voters-01078087]
- ⛔ **CORRECTION to the 16 Sep note: the 44-40 split is TRUMP VOTERS (2024 vote), not "Republicans."** Verbatim: "Trump voters are more torn: A 44% plurality prefer pausing development, only slightly greater than the 40% who say to keep going."
- Overall 48/31 and Dem 58-28 splits: **not seen at the primary** in this pass (charts are images). Use "a plurality" unless re-read.

**Anthropic Institute pace essay -- quotes now verified at the raw page:**
- [anthropic.com/institute/measuring-pace-of-ai-development], read directly 21 Sep. Verbatim: "As of August 2026, Claude 'leads' 26% of Anthropic's AI R&D work." "The share of work at or above 'AI collaborates' is above 90%." ~30,000 agents "at any one time in our most-used internal platform." "0.002% of them (about 1 in 47,000) were blocked." Highest-priority flags "approximately ~50 per week" to humans. And: "Safety research is hard to distinguish from capabilities research, and each developer will be tempted to draw the line generously. The burden of proof should sit with the developer to show that work is safety-related." Plus: "As the world considers pacing the frontier, we should do everything possible to minimize the gap between what frontier labs know and what the public knows."
- ⚠️ **Still undated on the page.** Secondaries cluster 17-19 Sep. Say "published last week," not a date.
- ⚠️ 6% / 12% safety-compute figures and the author names **not returned** in this pass -- unverified.

## What's contested / watch out
- **Is there an agreement at all?** OpenAI (Lehane) says no waiver is needed and the talks are routine safety cooperation; the complaint says the public statements are the agreement. Musk's contribution was four words on social media and Google's an endorsement of direction (TNW). The complaint concedes effects on released products have not yet manifested and pleads the restraint as naked, market only in the alternative. **Present it as allegations, filed, unanswered.**
- **DOJ's position is paraphrase.** The only verbatim Woodward lines are the "meeting" quotes. "Does not appear anticompetitive" is the Examiner's paraphrase and is about cybersecurity cooperation, not pacing. Do not write "DOJ says pacing is legal."
- **Is S. 5105 "the pacing bill"?** It was introduced in July as an anti-distillation/China bill; WaPo's AI & Tech Brief (reposted by Banks, "A legal shield for pacing") reads its (a)(2) as the pacing vehicle. The text supports the reading; the sponsors' press releases frame it as China espionage. **Say both.**
- **Sacks, via Semafor:** "You have a basic obligation to make your products safe. Do not demand antitrust waivers or liability waivers in exchange for that." Usable -- note he himself pairs the two waivers, which is the conflation this piece untangles. ⛔ Title rule binds: **former AI czar / PCAST co-chair**, never current, never "White House advisor." Semafor calls him "Trump's former AI adviser."
- **Anthropic compute, $517B / 14.8 GW over 11 months since Oct 2025:** The Information's compilation (paywalled), relayed by DCD and Investing.com. One outlet's tally of public deals plus its own reporting; not an Anthropic disclosure. Hedge as "by The Information's count" or leave out.
- **Criminal exposure.** Output-restriction cartels are per se and can be criminal under Sherman s.1 in general doctrine, but nobody has suggested prosecution here. DPA 708's defense covers "civil or criminal" actions -- that is statute. Do not imply anyone faces criminal charges.

## Couldn't verify / unreached
- Semafor's full exemption language for the NDAA version (reported, not seen).
- Thune-Klobuchar-Cruz bill text -- not introduced; only reporting (Politico, Reuters via Seeking Alpha, Nextgov from 16 Sep note).
- MSN copy of "Thune, Cruz and Klobuchar move AI safety from voluntary pledge to legal duty" -- blocked by robots.txt; not routed around.
- The Hill's news story on the lawsuit (thehill.com/policy/technology/6099571) -- 403 to the fetcher; used the complaint itself instead.
- politicalwire.com (poll summary) -- the fetch proxy rate-limited it and said not to retry; used Politico's own page instead.
- Politico poll overall 48/31 and party splits other than Trump voters.
- Anthropic pace essay date, authors, 6%/12% figures.

## The economics
- **What the shield is worth is a multiplier.** Sherman/Clayton exposure is treble damages plus fees; NCRPA-style notice cuts it to actual damages; S. 5105 (a)(2) removes it entirely for exempt conduct and leaves only a government injunction. The Buist class is every paid individual subscriber to four products from 12 Sep on. The complaint pleads no dollar figure in what was read -- **do not invent one**; the point is the multiplier and the class size, not a number.
- **Who pays for the pacing if it happens.** The complaint's own economic claim: "A company that slows alone while rivals race ahead loses customers, revenue, talent, and technological leadership." That is the labs' motive for wanting coordination -- and the reason a coordinated slowdown lands on subscribers as slower product at the same price.
- **Who the shield moves the cost to.** With the shield, the cost of a wrong pacing call (too slow, or cover for incumbency) lands on customers and would-be rivals with no damages remedy and no public record; without it, it lands on the labs at three times actual loss. Ties to the week's arc: where the cost lands when the decision turns out to be wrong.
- **Liability as the alternative brake.** Khan, Chilson and the Thune-Klobuchar duty of care all price risk through liability for harm instead of permission to coordinate. Bessent's line (already printed Monday) belongs here -- **callback only, not re-quoted as fresh.**

## Drop-in facts (each with a source)
- S. 5105 lets two or more companies agree to delay or limit "the release, deployment, use, development, training, testing, or evaluation of artificial intelligence" on written notice to the Assistant Attorney General. [govinfo BILLS-119s5105is, Sec. 3(a)(2)]
- That notice is "withheld, without discretion, from the public." [same, Sec. 3(e)(3)]
- The bill's bar on price-fixing and market allocation is written to cover "Subsection (a)(1)" -- the information-sharing clause -- only. [same, Sec. 3(d)(1)]
- *Buist v. Anthropic PBC*, N.D. Cal. No. 3:26-cv-10693, filed 18 Sep 2026, one Sherman s.1 count, treble damages sought, four named plaintiffs, class of U.S. paid individual subscribers since 12 Sep. [complaint]
- "An agreement among competitors to reduce the quality of their products and the rate at which those products improve is an agreement to restrict output." [complaint]
- "To the extent that anybody at any of the frontier labs wants to come see us about a concern, they would get a meeting ... That meeting hasn't been requested." -- Associate AG Stanley Woodward, 17 Sep [Reuters via Insurance Journal]
- "There is absolutely no world in which I will consent to giving ... a small group of three or four of them -- antitrust exemptions so they can what ... collude together?" -- Sen. Josh Hawley, 15 Sep [The Hill]
- The NCRPA cuts antitrust recovery for notified joint ventures to "actual damages" -- but excludes ventures that restrict production other than the venture's own. [15 USC 4303(a), 4301(b)]
- DPA s.708 gives a civil and criminal antitrust defense only for government-initiated voluntary agreements with the AG and FTC in the room, public records, and a five-year expiry. [50 USC 4558]
- POLITICO Poll (Public First, 13-15 Sep, 2,064 adults, +/-2.2): 63% see at least a moderate risk AI destroys humanity; Trump voters split 44% pause, 40% continue. [politico.com, 16 Sep]
- "Safety research is hard to distinguish from capabilities research, and each developer will be tempted to draw the line generously." [Anthropic Institute, undated, read 21 Sep]

## DO-NOT-PRINT (binds every revision of Thu 24)
1. "Republicans 44-40" -- it is Trump voters.
2. "DOJ says pacing is legal" or any Woodward quote beyond the two verbatim lines.
3. "The bill bars price-fixing" without saying the bar is written for the sharing clause only.
4. "No sunset" as fact until the full text is scanned.
5. Any dollar figure for the Buist damages.
6. "Criminal" exposure for anyone in this story.
7. The FRONTIER Act "preempts state law."
8. Bessent's "creators are liable" as fresh (Monday printed it). SB 3444 (Monday).
9. Carried from Tue 15 / the 16 Sep note: the Sacks METR-independence claim in any form; Sacks as current anything.
10. The Anthropic essay's date; its 6%/12% compute figures; the $517B figure as Anthropic's own disclosure.
11. Do not build the piece on the Amodei essay (Tue 15 owns it). The complaint's use of it is quotable as the complaint's.

## Angles this opens
- **The spine, in one line:** the labs asked for a shield against the cost of coordinating; four subscribers filed for that cost three days later; and the text that would grant it seals the record while the only shield on the books requires one. Exposure for coordinating is not liability for what the models do -- and the one Senate proposal on the second kind adds liability rather than removing it.
- **Pays Monday's printed promise directly** ("Thursday takes up the shield being negotiated in Washington"): the shield is S. 5105 (a)(2) and its NDAA attempt.
- **Tuesday boundary holds:** none of this is the electorate or the county meeting. The poll is the only crossover; use it once or not at all (Tue 22 cites midterm politics, not this poll -- grep before use).
- **Sun 27 capstone leg:** the shield is the cleanest instance of the week's mechanism -- the cost of being wrong moved away from the party that made the call.
- **Watch before Thursday:** any defendant response in *Buist*; a DOJ guidance update; a Commerce markup date; bill text for the duty of care.

---

## ADDENDUM, 23 Sep 2026 -- footing for his rv1 release-cadence payload (added by the Thu 24 chat after the panel flagged it unfooted)

**All of it checks out. The project's own briefs were behind, not him.**

- **Claude Opus 5.5 -- released Tue 22 Sep.** Anthropic's own page (`anthropic.com/claude-opus-5-5`), Reuters ("Anthropic unveils Claude Opus 5.5", 22 Sep) and TechCrunch (22 Sep, 9:30 PDT). Reuters: performance comparable to Fable 5.1 while *"costing 40% less to run than its predecessor"*. TechCrunch, from the announcement: **Sonnet 5.5 and Haiku 5.5 "in the coming weeks"**, and Opus 5.5 is Anthropic's first release since Amodei embraced pacing. Platform docs list $4/$20 per MTok.
- **GPT-6 Sol and GPT-6 Luna -- released Tue 22 Sep**, about an hour after Opus 5.5 (Simon Willison, 22 Sep; OpenAI announcement; TechCrunch 11:00 PDT; Reuters). **Half the price of their GPT-5.6 equivalents**: Sol $2/M in, $10/M out; Luna $0.10/M in, $0.50/M out. TechCrunch describes them as cut from the same cloth as Astra (GPT-6 Astra shipped 3 Sep), which carries his "based on the Astra model".
- **Grok 4.7 -- released Mon 21 Sep** (`x.ai/news/grok-4-7`), **$2/$6 per million, the same rates as Grok 4.6** (x.ai; VentureBeat; Cursor forum). His "same price right now as Grok 4.6" is correct. ⛔ From a **Thursday 24 Sep** run it is **three days ago**, not two.
- **Gemini 3.8 Live and 3.8 Live Extended Thinking -- 15 Sep** (`ai_brief_2026-09-16`). "Last week" holds from 24 Sep.
- **All of these post-date the 12 Sep pacing essay.** The "All after" sentence stands.

**Still open in that block, and his to rule on:**
1. *"the cost per task estimated by the labs"* -- what is footed is **list price** (Opus 5.5 40% cheaper to run than Opus 5; Sol/Luna at half their 5.6 equivalents), not a lab-published cost per task. Recast to list price and it is solid.
2. *"the models providing the majority of used inference in the West"* -- unfooted. Nearest support is OpenAI's share of **OpenRouter developer spend** (`ai_brief_2026-09-17`), which is one routing platform, not Western inference. Narrow or cut.
3. *"the early vibe check on all four models"* -- five families are named above it.
4. **Meta's Muse "delayed for months"** -- the delay is footed twice at secondary (AIDB summaries, 18 Sep briefs); the duration and the reason are motive attribution and are not.

**Airline profits, his aside -- a live catch.** Bureau of Transportation Statistics: US scheduled passenger airlines reported an **after-tax net gain of $16 million for Q2 2026**, *down* on Q2 2025, on a pre-tax operating profit of $3.0 billion. Individual carriers carry the claim (Delta $2.0 billion pre-tax for the June quarter; United a Q2 revenue record of $17.7 billion), the industry does not. Name a carrier and a number, or drop the quarter.

**Added 23 Sep, closing a drafter [VERIFY]:** the complaint does carry the essay's own antitrust acknowledgment. Per the complaint PDF (read 21 Sep), Amodei *"acknowledged the antitrust problem,"* and his essay stated that government mediation would be helpful and that the government would need to issue *"a narrow waiver for certain kinds of safety conversations."* Quotable as the complaint's characterization, not as the essay.

**Added 23 Sep, on his ruling:** Meta's Muse delay is footed at Zuckerberg's own reply to the pacing essay (X, 15-16 Sep, via AP/Click2Houston), already recorded in `research_slowdown-positioning_2026-09-16.md`: Meta held Muse back for months, *"We didn't call for everyone else to do this before we would."* The duration and the reason are his from the primary; the earlier motive-attribution flag is withdrawn.

**Owed by him, 23 Sep:** his reference for the DPA s.708 precedent uses (pandemic supply agreements; the April 2026 DOE nuclear fuel consortium). He ruled the block accurate and it ships on his word; file the reference here when it arrives.

**DPA s.708 -- CLOSED 23 Sep by HIS OWN sourcing. His paragraph replaces the drafter's, and these are his primaries:**
- Statute: 50 USC 4558 -- https://www.govinfo.gov/content/pkg/USCODE-2024-title50/html/USCODE-2024-title50-chap55-subchapIII-sec4558.htm
- Pandemic: DOJ published the required finding for FEMA's pandemic healthcare-supply agreement, 17 Aug 2020 -- https://www.govinfo.gov/content/pkg/FR-2020-08-17/html/2020-18006.htm · FEMA implementation notice (plans covering tests, drugs, medical devices, medical gases), 28 May 2021 -- https://www.govinfo.gov/content/pkg/FR-2021-05-28/pdf/2021-11278.pdf
- Nuclear fuel: DOJ Antitrust Division approves the DOE consortium's UPDATED voluntary agreement and related plans of action, 23 Apr 2026, expressly invoking s.708 -- https://www.justice.gov/opa/pr/antitrust-division-approves-department-energy-defense-production-act-consortiums-updated
- ⛔ **April 2026 is the approval of an UPDATE, not the consortium's creation.** Any later revision that says "created" or "formed" is wrong.
- ⛔ **Four wording corrections that bind every revision:** the defense is conditional, never a "full defense"; government initiation and active supervision are required; DOJ/FTC participation is mandatory at development meetings but optional at implementation meetings, where a federal employee must attend; public disclosure carries specified exemptions. Participants bear the burden of establishing the defense.
