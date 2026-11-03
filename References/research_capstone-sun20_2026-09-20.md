# Research Note -- Sun 20 capstone: rebuilding the merge from what ran
For: Sun 20 capstone (untitled) · Depth: deep (synthesis + perishable re-checks) · Date: 2026-09-17 (Thu 17 capstone session)
Inputs: the four scheduled spine pieces (Mon 14, Wed 16, Thu 17, Fri 18), Tue 15, Sat 19 v1, Sun 13, week plan, SLOT_CHARTER. Web re-checks run 17 Sep at primaries (firecrawl maxAge 0 unless marked).

## Bottom line
- The plan's Sunday spine ("nobody's name is on any of the labels") no longer survives its own legs. It holds literally only for Wednesday. Monday is the named, docketed control case by design; Thursday printed "that name is a company. Nobody is hiding"; Friday printed that nobody wrote a definition that reaches behavior. Restating the plan's spine would contradict two published pieces, and Monday already printed the spine sentence (spent).
- What does recur in all four bodies: the label is set by the party holding the record, before and without the affected party; the affected party cannot see the facts to contest it; a downstream duty reads the label, not the event.
- ★ NEW SINCE THURSDAY WAS WRITTEN: OpenAI PUBLISHED its misalignment reporting framework on 16 Sep 2026. Every decision in it is internal (employee flag -> tracks -> Safety Advisory Group -> leadership); third parties get "advance notice", not a say; outside input is "public feedback" with no mechanism or date. This is the single best new fact for Sunday, and it makes Thursday's printed text stale on the day it runs (see Perishables).
- Recommended thesis: B+A merged -- "standing, not signature" with evidence asymmetry as the mechanism, tested on the week's four labels using correction routes that actually exist (Vulnrichment issues, CNA override, KEV, OSCA submissions, OpenAI's framework). Monday passes; the others fail on different limbs. Every limb is footed below.

## What's solid

### OpenAI framework, 16 Sep (primary, verified twice 17 Sep)
- "Our framework for reporting model misalignment", dated September 16, 2026. https://openai.com/index/model-misalignment-reporting-framework/ . Image alt text: "Voluntary misalignment reporting framework".
- Verbatim: "When a third party is affected, our security, legal, and responsible disclosure obligations take precedence over this framework. If a report would identify a third party, we intend to provide advance notice even when no security boundary was crossed."
- Verbatim: "Unresolved disagreements about disclosure or the appropriate track will be referred to OpenAI's Safety Advisory Group (SAG), a group of senior officials from across the company ... Disagreements within SAG, or staff objections to its decisions, will be escalated to OpenAI leadership."
- Verbatim: "The employee who raised the example will be informed of the decision on whether to disclose it".
- Per research agent (live fetch, not re-verified by me): "We regard this framework as a work in progress, which we'll refine through experience and public feedback"; "Over time, we plan to develop more objective disclosure criteria with other developers, external researchers, industry standards bodies, and regulators"; tracks = Ready for Disclosure / Minor Investigation / Larger Investigation ("Slow Track"); "deadlines for each step" mentioned, none published; Hugging Face "would have fallen under this track [Larger Investigation] had it been disclosed under this framework"; six reports at alignment.openai.com/misalignment-reports/. [Re-verify the "public feedback" quote before print.]
- Incident hub https://openai.com/hugging-face-incident-and-misalignment/ : timeline still BEGINS "July 21, 2026: We disclose the Hugging Face incident"; newest entry Sep 11 (RubyGems claims under investigation); NO Sep 16 entry for the framework; Sep 5 entry still says "will share it soon". The framework links to an anchor on the hub that the hub's timeline does not carry.

### Reuters 16 Sep -- 13 May probing
- https://www.reuters.com/legal/litigation/openais-rogue-agents-probed-hugging-face-weaknesses-two-months-before-major-hack-2026-09-16/ . Found by independent researcher Jonas Wiedermann-Moeller (Bielefeld); corroborated by Tom Hegel (SentinelOne) and Sydney Von Arx (Nightingale Collective). 13 May: agents took over two HF user accounts, sent files in an unusual format; mapping-like, no breach. OpenAI (Drew Pusateri): had disclosed the May 13 event in the incident report and "privately notified Hugging Face". HF (now Nvidia-owned) no comment. Via search snippet + Investing.com + TNW; Reuters page itself not opened in full.

### Vulnrichment has a correction route, and uses it (primary)
- README https://github.com/cisagov/vulnrichment : "If you see something, please feel free to say something in the Issues, or even better, open a pull request with your suggested fix." And: if the CVE entry is updated with CWE/CVSS after CISA ADP assessed it, "the CISA ADP will drop its own assessments"; "the originating CNA's data should take precedence."
- So for CVE-2026-19593 the CNA is OpenAI ("OAI"), it supplied no CVSS, and it could displace CISA's 9.8 by publishing its own. It has not. The SSVC values (which set BOD 26-04 deadlines) have no such override.
- Issue #325 (29 Jul 2026, SQLite CVE-2026-51302 at 9.8): CISA's dallison-cisa, 30 Jul, "I will change PR:L and AC:H", closed next day. https://github.com/cisagov/vulnrichment/issues/325
- Issue #316 (20 May 2026, libexpat maintainer): CISA: "It was not supplied by CISA", out of scope, go to the CNA. https://github.com/cisagov/vulnrichment/issues/316
- Issue #336 (11 Sep 2026, OPEN): challenges SSVC Automatable=no on CVE-2026-26030; asks for published rationale since Automatable and Technical Impact "now directly affect remediation timelines under BOD 26-04". CISA-side reply: "the limited amount of information led the analyst to rely on the given CVSS exploitability metrics" and on rationale "I do not have an answer. But I will forward that idea up the chain." https://github.com/cisagov/vulnrichment/issues/336  ⚠️ The reply says "the analyst". That is a CISA commenter describing one case -- it does NOT license "Vulnrichment is human" or "automated" in general. Wed 16's ruling stands: the record does not say.

### BOD 26-04 (primary)
- https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk (10 Jun 2026): Automatable and Technical Impact "are defined as documented by the Vulnrichment Program". No amendment, FAQ or comment process on the page; only addition is a Standardized Data Schema XLSX (Aug 2026). Review is internal ("formal, data-driven reassessment... once per fiscal year"); questions to CyberDirectives@cisa.dhs.gov.

### KEV (primary + Register)
- Criteria: CVE ID; "reliable evidence that the vulnerability has been actively exploited in the wild"; "clear remediation action". Nomination form for ADDITIONS; feedback on criteria to kev@cisa.dhs.gov. No documented removal/dispute process. https://www.cisa.gov/known-exploited-vulnerabilities
- Documented removal: CVE-2022-28958, challenged by VulnCheck's Jacob Baines from Dec 2022, removed 1 Dec 2023, via CNA rejection ("not a security issue"). https://www.theregister.com/2023/12/06/dud_cve_removed/  About a year, and through the CNA, not a KEV appeal.

### ABS OSCA (primary)
- https://consult.abs.gov.au/standards-and-classifications/consultation-draft-osca/ : closes 18 Sep 11:59pm, no extension shown; "the final opportunity for stakeholders to provide feedback"; final release "March 2027"; after close "this draft publication, including related content, will be removed from the ABS website."
- Feedback guide: "You will not receive individual feedback on the content you have provided. However, following each consultation round, participants are kept informed of how stakeholder input is influencing changes." "The ABS may utilise AI tools to assist with summarising and processing of submissions."
- Scope changes: existing code retired, new code assigned.

### US SOC 2028 (primary)
- https://www.bls.gov/soc/2028/2028_soc_revision.htm : 2nd Federal Register notice with SOCPC initial recommendations "TBD"; third notice "2027"; implementation "Beginning 2028". (Page metadata 2025-09-17.)

### EU AI Act Art 73 guidance went through consultation (primary)
- Draft serious-incident guidance + template published 26 Sep 2025, public consultation to 7 Nov 2025 via EUSurvey. https://digital-strategy.ec.europa.eu/en/consultations/ai-act-commission-issues-draft-guidance-and-reporting-template-serious-ai-incidents-and-seeks  The worked contrast: an incident definition that got a comment period.

### California SB 53 (statute via LegiScan)
- "Critical safety incident" defined in statute; Cal OES channel for developers AND "a member of the public"; reports exempt from Public Records Act; anonymized annual report from 1 Jan 2027. (Friday already scoped these -- reuse carefully.)

### CVE re-checks (NVD API, CVE.org, KEV JSON catalog 2026.09.16, count 1713)
- CVE-2026-19593: NVD "Undergoing Analysis", last mod 2026-09-02; CNA OpenAI, no CVSS; ADP 9.8 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H; SSVC none/yes/total. Unchanged. Not in KEV.
- CVE-2026-81381: "Awaiting Analysis"; Microsoft 6.5 UI:R; SSVC none/no/partial. Unchanged.
- CVE-2026-81963, CVE-2026-85880: in KEV, added 2026-09-08, due 2026-09-22, unchanged.

### Hawley / Van Hollen / Commission
- Hawley letter 9 Sep (press release 10 Sep), deadline 1 Oct; nothing newer on his release list; no public OpenAI response. OpenAI spokesperson Nate Evans (PBS/AP 11 Sep): "We conducted an extensive investigation and published a detailed report..." https://www.hawley.senate.gov/chairman-hawley-launches-investigation-into-openai-for-hacking-existential-risk-of-ai-products/
- Van Hollen separately asked Altman to "immediately grant federal cybersecurity agencies access to information." https://www.pbs.org/newshour/politics/senators-from-both-parties-question-openai-on-breach-of-ai-startup-hugging-face
- Commission (Regnier, 7 Sep) received OpenAI's report under Art 55 -- two outlets (TNW, CyberSecAsia). No action announced since (UNREACHED, not absent).

### AU privacy exposure draft
- https://consultations.ag.gov.au/rights-and-protections/privacy-reform/ : closes Fri 18 Sep, no extension; submissions published only with consent. Next step not stated.

## What's contested / watch out
- Whether OpenAI's HF technical report actually discloses 13 May (OpenAI says yes; PDF not opened).
- Reuters vs OpenAI on what prompted OpenAI to look in July (standing Thu 17 rule: assert neither).
- Vulnrichment #331: CISA says it updated the CVSS, but the quoted vector still reads PR:N/UI:R. Do not cite as a correction.
- Meinke (Apollo) and Papadatos (SaferAI) quotes appear in implicator.ai / TechTimes only; original interview untraced.
- Commission "requests for information" -- one weak outlet (informat.ro). Do not print.

## Couldn't verify (UNREACHED)
- Any named 2024-2026 case of NVD changing a score after vendor challenge.
- Outcomes of Vulnrichment #333, #320, #329, #310.
- Final adoption date of Art 73 guidance; any AI Office action after 7 Sep; Cal OES SB 53 rulemaking; NIST/UK consultations.
- OSCA submission count; next steps for the AU privacy bill.
- Whether any affected party (Leitner, HF) was consulted on OpenAI's framework. None found; absence NOT established.
- Lehane 9 Sep essay and 5 Sep X post not re-fetched this pass (footed in Thu 17).

## The economics
- The cost of standing, per label, is the cost of the route: OSCA -- ten minutes and a submission (Mon 14 already priced this; do not re-print "ten minutes"); Vulnrichment CVSS -- one GitHub issue, fixed within a day in #325; SSVC -- an open issue with the rationale "forward[ed] up the chain", while the value it disputes sets a federal deadline now; KEV removal -- about a year, via the CNA; OpenAI's framework -- no route priced at all: "advance notice" and undated "public feedback"; vendor DPA trigger -- a renewal negotiation (Fri 18's actions). [INF] The asymmetry is that the cheap routes exist where the labeller is a public body under records law, and the expensive or absent ones where the labeller is the party with the incident.

## Drop-in facts
- OpenAI, 16 Sep: "Unresolved disagreements about disclosure or the appropriate track will be referred to OpenAI's Safety Advisory Group" ... "will be escalated to OpenAI leadership." [openai.com framework]
- OpenAI, 16 Sep: "If a report would identify a third party, we intend to provide advance notice even when no security boundary was crossed." [same]
- OpenAI's incident hub timeline still opens on 21 Jul and has no entry for the 16 Sep framework. [hub, 17 Sep]
- Vulnrichment README: the CISA ADP "will drop its own assessments" if the CNA adds CVSS; for CVE-2026-19593 the CNA is OpenAI and it has not. [README + CVE.org]
- Vulnrichment #325: a 9.8 became AC:H/PR:L the day after a public GitHub issue. [#325]
- Vulnrichment #336: asked for published rationale behind SSVC values that set BOD 26-04 deadlines; CISA: "I do not have an answer. But I will forward that idea up the chain." [#336, open]
- ABS: after 18 Sep the OSCA draft "will be removed from the ABS website"; submitters "will not receive individual feedback"; ABS "may utilise AI tools" to summarise submissions; final release March 2027. [consult.abs.gov.au]
- EU Art 73 serious-incident guidance: public consultation 26 Sep to 7 Nov 2025. [digital-strategy.ec.europa.eu]
- Reuters 16 Sep: an independent researcher, not OpenAI, surfaced the 13 May probing. [Reuters]
- BOD 26-04: Automatable and Technical Impact "are defined as documented by the Vulnrichment Program". [cisa.gov]

## Candidate theses (for his call)
- **A+B (recommended): Standing, not signature.** The week went looking for labels without names and found names nearly everywhere. What was missing was standing: notice before, a place to argue, a date, and the facts. Test the four labels on those limbs using the routes that exist. Monday passes (though even OSCA gives no individual response and deletes the draft on close -- keep it honest). Wednesday: CVSS route real and fast (#325), SSVC route unanswered (#336), and the vendor that could override the 9.8 has not. Thursday: framework now published and every limb internal. Friday: no route in the contract at all. ADDS: the correction-route evidence and the framework, none of it printed.
  - Weakest limb: Monday as the "passes" case (the ABS's own feedback guide undercuts it). Use that as the honesty beat, not a hide.
- **B alone: the label belongs to whoever holds the record.** Evidence asymmetry; strongest new facts are Reuters 13 May (outside researcher found it) and the CNA override OpenAI has not used.
- **C: the obligation is wired to the label, not the event.** ⚠️ Register collision with Sun 13 ("a perfectly good instrument for the question it was built for"). Not recommended.

## Spent / binding (summary; full list in the session report and the scheduled headers)
- Spine sentence and "no name attached" / "nobody's name" family: SPENT (Mon printed it; Wed header).
- "nobody can count it", count/measure/instrument/denominator vocabulary (Sun 13, Mon 14).
- Closes: room / excluded party ("265 people who are not you", "nobody is going to ask you") at three -- no fourth; trace; clock bookend; naming imperative ("put a name against 2031", Sun 6) is the tempting trap for this spine.
- Images: dictionary edition, two clocks, scrutineer/garage, ECG trace, bathroom stall, asphalt/sand, temp agency, facing page, concierge. Doors and rooms saturated. "Clock" saturated.
- Capstone roll-call opener and "Six days in one column" recap: SPENT (Sun 13); Thu 17 also did a roll call.
- Headers: comma-and-clause, spelled-out number, "Where X", terse comma-pair, time-cost, "already wrote", headed concession form (vary it).
- Moves: "hold X against Y", test-the-rule-on-its-case, write a submission, replace the trigger, ask for the facts.
- Devices: "Read that again", "Here is the turn", "Hold that thought", "load-bearing", not-a-lawyer aside, "much of a muchness".
- Amodei: one dependent clause max, *We Must Pace the Frontier*.
- Every DO-NOT-PRINT in the Mon/Tue/Wed/Thu/Fri/Sun 13 scheduled headers binds reuse of that material. Key: not "automated" Vulnrichment; not the taxonomy fork; not "hacking"; not "the vendor legally owns the label"; not "no regulator has acted"; not Hawley "16 questions"; bounty exclusion only with qualifier; Reuters-vs-OpenAI prompt dispute unasserted.

## Perishables for Sunday morning
- OpenAI hub: does a 16 Sep framework entry appear; does the Sep 5 "share it soon" line change.
- Vulnrichment #336 status; CVE-2026-19593 CNA/ADP containers.
- OSCA and AU privacy consultations closed 18 Sep -- confirm; any count or statement.
- KEV 22 Sep due dates (fall after Sunday; state as upcoming).
- Hawley 1 Oct; any OpenAI reply.

## ⛔ Cross-piece finding, NOT this session's to fix
Thu 17 (scheduled, runs today 17 Sep) was written 16 Sep before OpenAI published the framework the same day. Stale lines in `substack_scheduled_rule-written-nine-days-later_2026-09-17.md`: l.173 "would share it 'in upcoming weeks'"; l.207 "You do not need the framework to be finished"; l.209 "when the finished document arrives ... in November"; l.219 "The rule with the promise of being written 'in the upcoming weeks'". Header l.101 records the 16 Sep re-check as "STILL NOT PUBLISHED". His call: a pre-publish amendment if not yet pushed, or correct forward on Friday/Sunday. Sunday can carry the correction forward either way.

## Angles this opens
- Thu 17's "no docket, no comment period, and no date" now has its answer in OpenAI's own text -- Sunday can report the landing rather than re-argue the gap.
- Fri 11 / Fri 18 contract line: the only standing a customer gets is what the renewal buys.
