# The Number Nobody Can Produce

**Status: DRAFT v1 -- FIRST DRAFT, NOT PANELLED. Thursday, 3 September 2026. ~1,700 body words -- lighter on purpose, per his 2 Sep note that the back half of the week does not have to be long. Em-dash-free; zero contractions outside quoted speech; US spelling. ONE [YOUR TAKE] open. ONE [VERIFY] carried from the plan and NOT triggered (see below).**
**Series: Weekday feed (Thursday) · Thread: Shape of Defense × Practitioner (Shape of Defense ADOPTED 30 Aug)**
**Source: References\week-plan_2026-08-31.md Thu 3 block (v3) · research_story-candidates_2026-08-16.md §3.1-3.4 · primary-sources\SOURCE_asd-aicd_frontier-ai-boards_2026-08-05.md**

**✅ THE SPINE IS FOOTED AT THE PRIMARY, 2 Sep.** NIST, "NIST Updates NVD Operations to Address Record CVE Growth," **15 April 2026**, nist.gov/itl/nvd. All four quotes verbatim from the page: "Submissions increased 263% between 2020 and 2025" · enrichment prioritised for KEV-listed CVEs, federal-use software, and EO 14028 critical software · **"Going forward, we will no longer routinely provide a separate severity score for those CVEs"** · backlogged CVEs published before 1 March 2026 moved to "Not Scheduled."**

**★ THIS IS THE WEEK'S ONE LICENSED CONCEDE-THEN-SHARPEN**, and it is used exactly once, on the Mandiant five-days-to-47 correction, where the concession CONVERTS into the thesis (the panic is partly bad statistics; the crisis is real and it sits on the defender's side of the ledger). Nowhere else in the piece and nowhere else this week.**

**★ PAYS MONDAY'S PRINTED PROMISE.** Mon 31 quoted ASD's threshold question -- *"Are we delaying addressing any weaknesses due to a perceived low exposure or severity?"* -- and said "I will come back to it on Thursday." Paid in the ASD section, declared in one clause.**

**⚠️ WINDOW -- Wed 2 is one day back, Sat 29 is five days back and OWNS a beat this piece needs:**
**- ⚠️ SAT 29 COLLISION, HANDLED AS THE PLAN v3 REQUIRES. Sat 29 ran, verbatim: *"Microsoft rates an exploit's likelihood in a single flat phrase with no drama attached; a company in the vulnerability business publishes the word 'wormable,' and that word travels."* That is this piece's vendor-severity beat. It is DECLARED in one clause ("I wrote on Saturday about...") and NOT re-derived. The weight goes onto the 42-vs-62 disagreement (a different claim: two vendors closest to the data disagree) and onto NIST, which is the actual news.**
**- NO screen-share, recording, per-execution vs per-process, "why you stopped" (Wed 2) · NO four eyes, rubber stamp, two columns (Tue 1) · NO runbook, escalation path, fire door, 2.7%, safe harbour, confident-vs-correct (Mon 31) · NO credit file, four questions, denominator-vs-noun as a device (Sat 29 -- the piece does denominator work but never names it as a check) · NO chain of custody (banked) · NO ladder/rungs (Tue 25).**
**- NO self-correction opening (Sat 29 owns it). The cold open is the arithmetic, as the plan specifies.**
**- Thu↔Fri signposting mandated: Thursday is the COUNT, Friday is the INVOICE. Stated in the close.**
**- Controlling image: the grader who stopped marking. Checked against the window: unspent.**

**⚠️ THE CISA [VERIFY] IS NOT TRIGGERED.** The plan gates "any due-date claim" on eyeballing KEV from a browser, because cyber.gov / cisa.gov returned 403 on every proxy path. This piece makes NO due-date claim and NO BOD 22-01 / BOD 26-02 claim. KEV is referred to only as the thing NIST now prioritises, which is NIST's statement, footed at NIST. PCI DSS 4.0 §6.3.3 is NOT cited. The Clop/Windchill perimeter counter-example from the 19 Aug dig is NOT used -- it depends on a KEV addition date and I would rather leave it than run it thin.**

**⚠️ DO NOT PRINT (checked, none present): "median time to exploit is five days" (it is an AVERAGE, over 138 already-exploited, and 47 untrimmed) · "time to exploit has gone negative" unqualified · "Patch Tuesday volumes tripled" (January was 113 -- month variance) · "23% of vulnerabilities are exploited before disclosure" (the denominator is 495 vulns first observed exploited, not all vulns) · "only 0.24% are ever exploited" (time-censored) · NIST SP 800-40 mandates 30 days (it prescribes none) · any KEV due date.**

---

Your patch policy says critical vulnerabilities get fixed within thirty days. Somebody should ask it what a critical vulnerability is.

Not rhetorically. Literally: who decides, using what, and where does the word come from before it lands in your ticketing system with a deadline attached. Because the answer used to be "somebody else, for free," and as of the middle of April it is not.

I want to walk through the arithmetic before I make any argument about it, because the arithmetic is the argument.

## August, counted twice

Microsoft's August Patch Tuesday fixed 398 vulnerabilities. Or 751. Both numbers are correct, and which one you got depends on who you read.

Tenable counted 398, with 42 rated critical. The Zero Day Initiative counted 398, with 62 rated critical. Same list, same month, same 398, and a twenty-vulnerability disagreement about how many of them were critical, because one shop derives severity from CVSS and the other uses Microsoft's own severity ratings, and those are different instruments that happen to share a word.

Senserva, pulling directly from Microsoft's own machine-readable CVRF feed, counted 751. The difference is Azure Linux entries that ship no knowledge-base article, which the human-readable roundups skip and the feed does not.

Microsoft itself publishes no total.

So the two vendors sitting closest to the data agree on how many vulnerabilities there were and cannot agree, by nearly fifty percent, on how many were critical. And the vendor that shipped the patches declines to say. That is one month, from the most heavily scrutinized patch cycle on earth, before we get to anything hard.

## The rate

The first half of 2026 produced 35,364 CVEs. That is more in six months than any full year before 2024. Project it forward and you land somewhere around 72,000 for the year, which works out to a new one roughly every seven and a half minutes, around the clock, including the minutes you are asleep.

Nobody triages that by hand. Nobody ever did. What made it survivable was that a public body sat between the flood and your ticket queue and attached a severity score to each one, so that "critical" meant something before it reached you.

## On 15 April, the grader stopped marking

NIST runs the National Vulnerability Database, which is where that score came from. On 15 April it published a notice, and the notice is the reason this piece exists.

Submissions to the database, it says, *"increased 263% between 2020 and 2025."* In response, enrichment -- the analysis that produces the severity score -- is now prioritized only for three groups: vulnerabilities on CISA's Known Exploited list, vulnerabilities in software the federal government uses, and vulnerabilities in software designated critical under a 2021 executive order. Everything else drops to the lowest priority.

And then the sentence that should be pinned above every patch policy in the country:

> "Going forward, we will no longer routinely provide a separate severity score for those CVEs."

The backlog of anything published before 1 March 2026 was moved to a category called *"Not Scheduled."* Not delayed. Not queued. Not scheduled.

Read your patch policy again. If it says "critical," and it was written any time before April, it was written on the assumption that somebody upstream would keep supplying the word. For the long tail of vulnerabilities -- which is to say, most of them -- that assumption has been formally withdrawn, in writing, by the body that used to supply it.

The severity function did not disappear. It moved. It is now yours.

## The number everyone quotes, and what it actually says

Here is where I have to be fair to the other side of this, because the most-repeated statistic in the entire attacker-speed conversation does not say what people think it says, and I would rather correct it than lean on it.

You have heard that attackers exploit a new vulnerability within five days. That figure is Mandiant's, and it is real. It is also an **average**, not a median, and its denominator is 138 vulnerabilities that were already known to have been exploited -- which is to say, it measures how fast the ones that got exploited got exploited, not how fast vulnerabilities in general do. And in the same paragraph, which almost nobody quotes, Mandiant says that without trimming a handful of extreme outliers *"the average grows from five to 47."*

Five days is a trimmed mean over a pre-selected population. Forty-seven days is the same data with the trimming removed. Both are honest. Only one of them travelled.

So some of the panic is bad statistics. I want to say that plainly, because it is the kind of thing this newsletter exists to say.

And then I want to say the thing that survives the correction, because it is worse than the number that did not.

## What survives, and it is on your side of the ledger

VulnCheck tracked 495 vulnerabilities that were first observed being exploited in the first half of 2026. Of those, 23.43% were exploited on or before the day their CVE was published. Not before the patch. Before the *identifier*. Nearly a quarter of the ones that ended up mattering were being used against somebody before the number that lets you search for them existed.

The median gap between a CVE being published and being added to CISA's exploited list fell from 120 days to 80 in the same period.

And Mandiant, in the same report as the five-day figure, has a number that I think is genuinely the most important one on the beat. In 2022, the hand-off from initial access to a secondary threat group -- the moment a foothold gets sold or passed to whoever does the real damage -- took more than eight hours. In 2025 it took twenty-two seconds.

Eight hours to twenty-two seconds is not a speed story. It is an automation story, and it is happening on the attacker's side of the fence while the defender's side just lost its severity scores.

I wrote on Saturday about the way a vendor's adjective travels further than a vendor's number, and I am not going to rerun it. The point today is one level down: even when you strip the adjectives out and look only at the counts, the counts disagree, the body that used to arbitrate them has stopped, and the people who exploit the gap have automated the part of their process that used to take a working day.

## Your own signals directorate said it before I did

On Monday I quoted one of the ASD's threshold questions for boards and said I would come back to it. This is the coming back.

The question was: *"Are we delaying addressing any weaknesses due to a perceived low exposure or severity?"*

Read it now, knowing that the body which supplied "severity" for most vulnerabilities stopped doing so in April. The question is not really asking whether you are lazy. It is asking whether you are deferring work on the basis of a rating, and who produced the rating, and whether that rating still means anything for the vulnerability in front of you.

Two other things in the same document are worth having next to it. The first is the ASD's description of what frontier AI does to the attacker's side: it can *"chain together multiple low severity vulnerabilities into high-impact compromises."* That is a national signals agency saying, in a document written for boards, that the severity rating of an individual vulnerability is no longer the unit of risk. Three lows can be a critical. No scoring system in circulation rates them that way.

The second is what the ASD actually prescribes for patching, and it is notable for what it does not contain. Vulnerabilities are to be remediated *"within defined risk-based timeframes based on their severity and exposure."* No number. Not 48 hours, not two weeks, not thirty days. A risk-based timeframe, hung on severity -- the exact word that has just stopped arriving from upstream.

That is not a gap in the ASD's document. It is the ASD telling you, without quite saying so, that the timeframe and the severity are yours to define, and that a policy which borrows both from somewhere else is a policy that borrows its risk tolerance from somewhere else too.

<!-- [YOUR TAKE]: Your patch policy, your severity function, your industry. What does the word "critical" actually mean inside Player Elite's change control -- who assigns it, from what, and what happens to a vulnerability on a regulator-certified gaming platform where patching means recertification? The 42-vs-62 problem is abstract until somebody in your team has to pick one. And the human beat: the person who used to have a score handed to them and now has to produce one. That is the week's theme landing on a specific job. Real process, no names. -->

## So who, inside your building, gets to say "critical"

Not "what framework do you use." Who. A person, or a named function, with the authority to attach the word to a vulnerability and the standing to defend the attachment when the auditor asks why this one got thirty days and that one got two.

If the honest answer is "whatever the scanner says," then find out where the scanner gets it. For a growing share of what it flags, the scanner is now inheriting a score that was assigned before April, or a vendor's score, or nothing dressed up as something. That is not the scanner's fault. It is arithmetic about what is upstream of it.

If the honest answer is "nobody, we just patch everything," then that is a real answer, it is expensive, and tomorrow is about what it costs.

Because here is what a patch policy actually is, once the word "critical" stops being supplied from outside. It is a statement of how much risk you are prepared to carry, for how long, on the say-so of whom. That used to be somebody else's judgment, delivered free, on a schedule. As of April it is a judgment your organization has to make for itself, and most organizations have not noticed that the delivery stopped.

Today was the count. Tomorrow is the invoice, because somebody has already priced this, and it was not you.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that "patch criticals within thirty days" is written against a number nobody can produce, that August's Patch Tuesday was counted three different ways by the vendors closest to the data, and that on 15 April NIST stopped routinely supplying the severity score every such policy silently depends on.*
