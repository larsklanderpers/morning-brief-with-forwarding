# Somebody Repriced the Patch

**Status: DRAFT v1 -- FIRST DRAFT, NOT PANELLED. Friday, 4 September 2026. ~1,800 body words -- lighter on purpose, per his 2 Sep note that the back half of the week does not have to be long. Em-dash-free; zero contractions outside quoted speech; US spelling. ONE [YOUR TAKE] open. TWO [VERIFY] carried from the plan, both HANDLED BY OMISSION (see below) -- nothing in the body depends on either.**
**Series: Weekday feed (Friday) · Thread: Ad Hoc Regulatory × Shape of Defense. Ad Hoc Regulatory has been off since Fri 14 Aug -- three weeks -- and this rotates it back.**
**Source: References\week-plan_2026-08-31.md Fri 4 block (v3) · research_story-candidates_2026-08-16.md §3.5-3.8**

**✅ SOURCES, 2 Sep:** DBIR 2026 headline (31% exploitation as initial access) reconfirmed at Verizon's own landing page today; the 43-day median, the 26%-from-38% KEV remediation figure and the "more than 13,000 organizations" scope are the 16 Aug dig's verbatim quotes from the report and are used as quoted there. Microsoft hotpatch pricing ($1.50 per core per month, Azure Arc required, from July 2025) is Microsoft's own Windows Server blog of 24 April 2025 and its GA post; both are Microsoft primaries. Windows 10 ESU pricing ($61 year one, doubling, three-year cap) is the corpus's verbatim Microsoft quote.**

**⚠️ TWO [VERIFY] GATES, BOTH HANDLED BY NOT MAKING THE CLAIM:**
**1. BOD 26-02 is secondary-only (GuidePoint). The plan says "get the primary or describe it without the schedule." DESCRIBED WITHOUT THE SCHEDULE, and the body says in text that the description is from secondary reporting. No dates, no deadlines, no due-date claim -- so the CISA 403 gate is also not triggered.**
**2. Windows 11 hotpatch default-on (11 May 2026) is secondary-only. NOT USED. Hotpatch on Windows 11 Enterprise is described only as "included in the license," which is the footed part.**

**⚠️ WINDOW -- Thu 3 is one day back and is the piece's declared partner:**
**- Thu↔Fri signposting MANDATED: Thursday is the count, Friday is the invoice. Stated in the opener AND in the close, and the two registers are kept hard-separated on purpose (epistemic vs economic). The plan warns "Thu and Fri must not both be 'here is a number nobody produced'" -- this piece produces numbers that ARE produced, by Verizon and Microsoft, which is the point.**
**- NO grader-who-stopped-marking, NO 398/751, NO 42-vs-62, NO five-days-to-47 (Thu 3) · NO screen-share, recording, per-execution/per-process (Wed 2) · NO four eyes, rubber stamp, two columns (Tue 1) · NO runbook, fire door, 2.7%, safe harbour (Mon 31) · NO four questions, denominator-as-device, credit file (Sat 29) · NO chain of custody (banked) · NO ladder/rungs (Tue 25).**
**- NO concede-then-sharpen -- Thursday spent the week's one. The objection here (estate grew ~7.7x) is DISARMED IN TEXT as the plan requires, but as a straight rebuttal, not as a concession-then-turn.**
**- NIST's April withdrawal is referred to in ONE clause as yesterday's material, never re-derived.**
**- Controlling image: the storage unit whose rent doubles every year. Checked against the window: unspent.**
**- Theme licensed (his 30 Aug ruling): the close lands on the constraint being change control, asset ownership and downtime tolerance -- human decisions money does not move. In neither Monday's, Tuesday's, Wednesday's nor Thursday's words.**

**⚠️ DO NOT PRINT (checked, none present): the Windows Resiliency Initiative's "60% faster update adoption" (no denominator, no baseline, sells the license) · the edge-device MTTR figures (32 days median / 209-day average are DBIR 2025 -- do not blend years) · any claim that insurers are repricing on patch SLA (no primary found) · "from 1 July 2025" (written "from July 2025") · the Win11 default-on date · the Essential Eight as "48 hours for internet-facing" without the condition.**

---

While everybody argued about how fast the attackers were getting, the cost of being able to patch at all quietly became a line item. And the outcome is already measured.

Yesterday was the count -- the number that stopped arriving. Today is the invoice, because somebody noticed the number had stopped arriving before you did, and they have already worked out what to charge you for the consequences.

Think about a storage unit. You put things in it because throwing them out felt like a decision and paying rent did not. The rent is small. Then one year the rent doubles, and the year after it doubles again, and at some point you realize the operator is not really in the storage business. They are in the business of pricing your reluctance to make a decision, and they have priced it correctly, because you are still paying.

That is what has happened to patching. Hold that image, because every number below is a version of it.

## The outcome, before the argument

Verizon's 2026 Data Breach Investigations Report covers *"more than 13,000 organizations."* Three of its findings belong next to each other.

Exploitation of a vulnerability is now the top initial access vector in breaches, at 31%, up from 20% the year before. That is a 55% increase in a single year, in the thing that patching exists to prevent.

The median time for full resolution of a vulnerability *"went up to 43 days, almost two weeks more than the previous year's 32 days."* Slower, in a year when everyone was talking about speed.

And then the one that I think is the most damning statistic in the whole conversation, because of who it is about:

> "Only 26% of critical vulnerabilities -- defined as being in the CISA KEV catalog -- were fully remediated by organizations in 2025, a drop from the previous year's 38%."

Sit with what that population is. The CISA Known Exploited Vulnerabilities list is the easiest patching problem in the world. It is pre-triaged. It is a short, human-curated list -- CISA added 245 items to it in all of 2025. Every entry is confirmed exploited, government-flagged, and comes with a deadline. It is the one population where nobody has to argue about severity, because a regulator already did.

On that population, across thirteen thousand organizations, completion fell from 38% to 26% in a year.

That is not a story about vulnerabilities being hard to find. It is a story about what happens after they are found, and it is measured.

## The repricing

Now the invoice, and I am going to give you the numbers straight because Microsoft did.

Hotpatching -- applying security updates without rebooting, which is the single biggest reason enterprises defer patches -- is included in the Windows 11 Enterprise license. On Windows Server 2025, the same capability is a subscription: **$1.50 per CPU core per month**, and it requires the server to be enrolled in Azure Arc, Microsoft's management plane, from July 2025. The ability to patch without downtime is now a metered feature with a management dependency attached.

Windows 10, which went out of support last October, can be kept receiving security updates under Extended Security Updates at **$61 per device for the first year**, and in Microsoft's own words *"the price doubles every consecutive year, for a maximum of three years."* So $61, then $122, then $244, and then nothing, because the operator has decided three years is long enough to price your reluctance.

Put those two next to each other and you have the storage unit. Microsoft priced the patch backlog and billed it to the laggard, at a rate that increases with lag.

And there is a third figure, from Microsoft's own Secure Future Initiative report, that tells you what the vendor thinks patching looks like at its own scale: *"about 3 million container vulnerabilities patched per month through automation."* Three million a month. That is Microsoft conceding, in a report about its own security posture, that at scale there is no human in the loop on patching. There cannot be. The number does not permit one.

None of this is wrong of Microsoft. It is a vendor charging for a capability that costs money to build and pricing end-of-life so that end-of-life actually ends. The observation is not that the bill is unfair. It is that the bill exists, it is arriving as infrastructure spend, and almost nobody is reading it as what it is, which is the cost of a security control.

## The regulator stopped racing, and I say that carefully

CISA's 2026 binding directive on this -- and I am working from secondary reporting here, because CISA's own pages have been refusing my requests for three weeks -- is not, as far as I can tell, a directive to patch faster. The reported shape of it is patch, then inventory what you have, then decommission the end-of-support edge devices, then replace them, then discover continuously.

I want to be honest about the sourcing, because it matters: I have not read the primary, I am not going to give you dates from a summary, and you should treat the sequence above as reported rather than confirmed. But if the reported shape is right, the direction is the interesting part. The regulator has moved from a speed target to a *stock* target. Stop trying to patch things faster. Stop having things that cannot be patched.

That is the storage unit again, from the regulator's side. Throw it out.

## Australia, and a correction to the version you have heard

The Essential Eight is usually described as requiring internet-facing vulnerabilities to be patched within 48 hours. That is not quite what it says, and the difference has become the whole story.

ISM-1876 requires 48 hours *conditionally*: when the vulnerability is *"assessed as critical by vendors or when working exploits exist."* Otherwise, under ISM-1690, the window is two weeks. So the 48 hours is a trigger, and the trigger fires on severity or on exploitation.

Now recall yesterday: the body that supplied severity for most vulnerabilities stopped in April. And recall VulnCheck's finding that, of the vulnerabilities which ended up being exploited in the first half of this year, nearly a quarter were being exploited on or before the day their CVE was published. Which means that for a meaningful share of the ones that matter, *"a working exploit exists"* is already true on day one.

The standard has a trigger. The trigger has quietly become the default. And the two-week window most organizations think they are working to is, for the vulnerabilities that actually get used against people, increasingly a window that closed before they read the advisory.

## The objection, and why it does not survive the list

The strongest pushback to everything above is fair and I want to give it its full weight: I have shown you tooling and completion rates standing still while the estate exploded. Qualys puts the growth in vulnerability instances at roughly 7.7 times over four years -- with the caveat that Qualys sells vulnerability management and has an interest in that number being large. If the numerator grew nearly eightfold, absolute patching effort may have risen sharply while both ratios fell. Maybe the teams are heroic and the denominator is just impossible.

That would be persuasive if the 26% were measured against the whole estate. It is not. It is measured against the KEV list -- 245 additions in a year, every one pre-triaged, flagged and dated. If completion on 245 hand-picked items fell from 38% to 26% across thirteen thousand organizations, estate growth is not the constraint. You do not fail to patch 245 things because there are too many things.

You fail to patch them because of change control. Because nobody owns the asset. Because the system it runs on cannot be taken down without a business decision that nobody wants to be the one to make. Because it is on a certified build that cannot be touched without a recertification. Because the person who understood it left.

None of which is a budget line, and none of which money alone moves. Which is exactly why the answer is architectural rather than financial, and why the invoice, once you read it correctly, is telling you to change the shape of the estate rather than to spend more on patching the shape you have.

This challenge presents itself very interestingly in the gaming space because of the 24/7 nature of business. Your ability to do system outages is very limited in this space. As Tim Stanley said many years ago, running IT and gaming is like changing the engine of a Formula One car while it's driving around the track, and that is the challenge here. That is, to some extent, what the vendors are counting on: that patch maintenance at any sort of aggressive timeline schedule is virtually impossible.

Submitting yourself to it, through something like Azure that happens in the background without any sort of outage structure, becomes not just a nice thing but an absolute necessity. Every minute that the floor is offline costs the company business.

Add to this the fact that usually when you have an outage in an IT space, it's not just IT advising the rest of the business of the fact that there's an outage happening. In gaming, that exercise is just as much about IT seeking approval from the rest of the business for the outage to be acceptable during those time frames and to make sure operational line staff know that it's down, and that certain activities -- like cage/credit -- might not be available. The blast radius of any outage is substantially expanded.

This whole thing costs money. For a lot of my customers, what I see is that they've adopted older platforms like Citrix Windframe, and they are maintaining those platforms because it allows them to sidestep the entire patch methodology. They patch in one place, and then when you log in from wherever your end-state terminal is, you don't have a permanent desktop. You don't have an attack surface. There is one central surface, which is what manages all of the end units, and that surface is what defines everything else that happens. 

## Three decisions, which is what a manager actually takes away from this

**Buy down the class, not the vulnerability.** Hotpatching, automatic patch rings, and the elimination of anything end-of-support are not three projects. They are one decision to stop paying per-vulnerability for a problem that arrives per-month. The $1.50 per core is cheap against the downtime it removes; the ESU doubling is a countdown telling you which class to retire first.

**Own the severity function, because it is no longer supplied.** Yesterday's piece was about the word "critical" going missing upstream. Today's is what it costs when it does: without your own severity function, you cannot tell which 26% you are completing, and the Essential Eight trigger fires on a judgment nobody in your building is making. Somebody has to be named. *It will not be the scanner.*

**Treat the patch-servicing bill as a security budget line, because that is what it is.** The invoice is arriving as infrastructure spend -- licences, subscriptions, Arc enrolment, ESU -- and it is being approved by people who think they are buying uptime. They are buying a control. The place this gets teeth is NIS2 Article 20(1), which makes management bodies responsible for approving cyber risk-management measures and states that they *"can be held liable for infringements."* In that world, the 43-day median is not a metric. It is the number that becomes evidence.

That is the invoice. Somebody worked out that the expensive part of security was never the finding, it was the deciding, and they priced the deciding. And the priced the not deciding even higher. You can pay the rent that doubles, or you can make the decision the rent was standing in for.

The storage unit does not care which. It just keeps sending the bill.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that while everyone argued about attacker speed, the cost of being able to patch became a line item -- $1.50 a core, $61 doubling yearly -- that the outcome is already measured at 31%, 43 days and a fall from 38% to 26% on the easiest list in the world, and that the constraint the numbers reveal is change control and ownership, which money alone does not move.*
