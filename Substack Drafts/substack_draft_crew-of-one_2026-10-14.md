<!--
DRAFT v1 -- Wed 14 Oct 2026. Cyber spine, OPENS the week-of-12-Oct arc (plan label: THE COUNTERPARTY NEVER TIRES; never a header).
Source plan: References\week-plan_2026-10-12.md, Wed 14 block. Research: References\research_crew-of-one_2026-10-14.md (its DO-NOT-PRINT list binds every revision).
Exhibits: ARTEX (CrowdStrike primary, 7 Oct) + ReliaQuest (primary, 7 Oct), joined per his word 14 Oct ("joins for now ... replace it if ReliaQuest turns out to be the stronger point"). AA26-281A reframed as the OLD shape of a crew (contrast), not a second exhibit. GTIG at primary for point 3.
Opener kind: pop-culture heist film (everyday object/service, office document and courtroom are spent in the window).
Not panelled. Not delivered. Two [YOUR TAKE] slots open.
-->

# A Crew of One

*The most expensive part of an attack used to be the people. Two reports from last week say that part is getting cheap.*

The most expensive part of a heist was never the vault. It was the crew.

Heist films know this, which is why most of the first act of *Ocean's Eleven* is a recruiting drive. Danny Ocean gets out of prison with a plan, and then he spends reel after reel (and a fair chunk of somebody else's money) collecting a card dealer, a pickpocket, an explosives man, a pair of drivers, an electronics specialist and a retired con artist who needs talking out of retirement. Eleven people, each one with a cut to be paid, a schedule to keep and a mouth that might talk. The plan was the easy part. Assembling the people who could carry it out was the hard, slow, expensive part, and that cost is the reason most vaults never get robbed.

Security has quietly relied on that cost for a very long time. A great many of our defenses were never designed to stop a determined, well-staffed attacker; they were designed so that attacking us would take more people, more hours and more patience than we were worth. This week is about what happens when the party on the other side of an exchange stops getting tired, and today is the attack side of it: the crew is turning into a subscription.

Two reports from last week make the case, and a third, from Google, tells you what to do about it.

## Late September, South Korea

On 7 October, CrowdStrike (a security company that sells threat intelligence and detection, which you should know before weighing any of what follows) published its account of a run of intrusions against South Korean financial firms between late September and early October. The attacker used ARTEX, which CrowdStrike describes as "a recently released open-source agentic penetration testing (pentesting) tool developed in China." A penetration test is the break-in a company pays for, on purpose, to find its weak spots before somebody else does; an agentic pentest tool is software that runs that break-in on its own, asking a language model what to try next, trying it, reading the result and asking again.

CrowdStrike says the instance used DeepSeek's model as its primary engine, accessed through a reseller, with two other models filling in elsewhere. It does not say how many people were behind it. It calls them "the threat actor" throughout, assesses with moderate confidence that they are "likely a Chinese speaker and financially motivated," and makes one claim about what the tooling bought them: AI "can enable a financially motivated threat actor to conduct multiple intrusions within a short time span." Reuters, reporting on the same work, described a single suspect, and BleepingComputer reported that CrowdStrike may have found the person's identity, though CrowdStrike itself says those details are not reliable enough to confirm.

How it was found is the human part of the story. The attacker left folders open on a web server where anyone could browse them, and inside were the tool's configuration files and the notes from their AI coding sessions, including questions about where Korean breach data gets sold. For transparency, the coding assistant in those notes was Claude, which is the assistant I write and build with every day; per CrowdStrike, it was the attacker's notebook and research desk, not the engine that ran the intrusions.

How many people were affected is still moving. Reuters counts at least nine South Korean banks that have disclosed attacks, or been reported as targets, since late September; Shinhan Bank said about 25,000 customers' personal information was compromised, and KB Kookmin Bank said 119. CrowdStrike says the targets it tracked overlap with that reporting, without saying how many of them it can tie to this attacker.

One more detail. After the attacks were made public, the ARTEX developer closed the source and stopped updating it, according to BleepingComputer, and the existing code has already been turned into English- and Korean-language versions. Closing the door after the fact does not take back what has already walked through it.

## Between commands

The second report is narrower, and to my mind it is the more unsettling of the two.

ReliaQuest (a managed detection and response company, meaning it watches customers' networks for them and gets paid to, so again, weigh accordingly) published a write-up on 7 October of a single server taken over in a customer environment. The way in was not clever. A job-submission feature on a web application server accepted work without asking for a login (no zero-day, no exotic exploit, just a door somebody forgot to put a lock on). From there the attacker ran code inside the application, found database credentials sitting in plain text in a configuration file, used them to get the database to run system commands, tried one privilege-escalation tool, watched it fail, tried a second one that worked, took full control of the machine, copied out the stored password data, and created two administrator accounts on the way out. When it cleaned up, it deleted one of them. The other was still there.

ReliaQuest says the whole thing took "under 24 hours." The number that stuck with me is a smaller one. The median time between commands was about six seconds, and about half of those intervals were five seconds or less. That is not a person reading output and thinking about it. ReliaQuest's assessment, with "high confidence," is that "AI agents driven by large language models (LLMs) carried out substantial portions of it," and it describes the rhythm plainly: "commands ran, results were evaluated, failures were corrected." On the same address that launched the attack, it found a live control panel for Cairn, an open-source platform for coordinating AI agents.

And then it says the honest thing: "We could not determine how many agents were involved, which model drove them, or to what degree a person approved individual actions."

That is the point. Nobody can tell you how big this crew was, because the size of the crew has stopped showing up in the evidence.

## A company with a payroll

For the contrast, look at the other advisory that landed the same week.

On 8 October, ten agencies across seven countries (the FBI, CISA and NSA, plus their counterparts in the UK, Canada, Japan, New Zealand and Spain, and for my Aussie friends, ASD's ACSC) put their names to a joint advisory about Integrity Technology Group. The advisory calls it "a China-based for-profit company with links to the Chinese government" that "employs individuals who support malicious cyber activity in different ways": some build or buy the tools, some acquire and host the infrastructure, some break into the networks. Its in-house scanner, MicroScan, "contains over 1,300 penetration testing scripts" and was in use "as early as 2017." Some of the access goes back to "at least mid-January 2021."

That is what a capable crew has looked like for most of my career. A company, with a payroll and a division of labor and years of patience, building its own tooling one script at a time, and backed by a government. The vulnerabilities on its list run from 2014 to 2023, and half of them are more than a decade old, which tells you something about how many of them are still sitting out there unpatched.

Now hold that next to South Korea. One attacker, if Reuters is right, with a borrowed open-source tool, a reseller's account for someone else's model, and a couple of servers whose directories they forgot to lock, running multiple intrusions against banks in the space of a few weeks. And next to ReliaQuest, where the crew could have been one person signing off on each step, or nobody signing off on anything, and the evidence cannot tell the difference.

Nobody has published what either of these operations cost, and I am not going to invent a number. What I can say is what they used, and none of it was a payroll.

<!-- [YOUR TAKE]: what it used to cost to staff the other side -- a pentest engagement you bought or ran (team size, weeks, the quote), or what it took in your career to stand up a red team. The economics land harder with your number than with mine. -->

## Where the effort used to be

So the first point is simple to state and uncomfortable to sit with: the work that used to need a crew now fits on a model bill and a few rented servers.

The second point is about what that does to the defenses you already have, because a surprising number of them were priced in effort.

Think about how most organizations decide what can wait. That old file server behind a forgotten firewall rule can wait, because finding it would take someone a week of poking around, and who would bother. The admin console with no login can wait, because it is on an odd port and nobody outside knows it is there. The patch for the 2016 bug can wait, because the attackers with the skill to use it are busy with bigger fish. Every one of those is a bet on the other side's patience running out before it gets to you. Few of them are written down as a control, but all of them are doing the work of one.

The Integrity Tech list is a museum of those bets. A 2015 FTP flaw, a 2016 web framework flaw, a 2019 VPN flaw: still worth a nation-state contractor's time in 2026, because somewhere they still work. Its first recommendation is as plain as it gets: "Disable unused services and ports." And the ReliaQuest server fell to exactly the kind of thing that used to be safe by being boring, a feature nobody thought anyone would find, found by something that does not get bored.

That is the shift. An agent working through a target at one command every few seconds does not decide your forgotten server is not worth the trouble. It does not knock off at four in the afternoon. It does not need a cut. The bets you made on the attacker's patience were reasonable when patience was expensive, and they are bad bets now.

(The same diligence runs on the other side of the wall too, as last week's piece on agents finding their way out showed. OpenAI has since apologized in writing for agents that got into Australian government systems: "We also should have handled our response better. We are sorry and working to do better in the future." Different problem, same machinery that keeps going.)

## Half of them run code

The third point is about the queue, and it comes from Google.

On 30 September, Google Threat Intelligence Group published an analysis of vulnerability disclosures through August 2026, and two of its numbers belong next to each other.

The first is about what AI finds. Of the vulnerabilities GTIG could identify as likely discovered by AI, "exactly 50%" lead to remote code execution (RCE, the class of bug that lets an attacker run their own commands on your machine, which is about as bad as it gets), against 26 percent across everything else. So about twice the rate. AI-assisted discovery also turns up proportionally fewer of the low-risk findings. The machines are not finding more noise; they are finding more of the bugs attackers actually want.

The second is about what gets used. Only 0.23 percent of vulnerabilities disclosed in 2026, roughly one in 431, have been seen exploited in the wild. But the ones that do get used get used fast. GTIG's example is a BeyondTrust remote-support flaw found by an AI research agent: one group was exploiting it within four days of public disclosure, and five more within seven.

Put those together and the old way of working the patch queue (sort by severity score, work down from the top, never get to the bottom) stops making sense. The volume of disclosures doubled between January and August, by GTIG's count. The share that anyone actually exploits stayed tiny. And the ones that matter are disproportionately the remote-code-execution kind that an attacker's agent can pick up and run with inside a week.

GTIG's own recommendation is to "transition from unprioritized mass-patching to threat-intelligence-driven triage," and to pair it with "automated, agentic remediation." I agree with the first half without reservation. On the second, know that Google sells exactly that (its CodeMender agent gets a mention in the same report), and judge the pitch on its merits.

## Sorting the queue by who is shooting

None of this asks you to buy anything new on Monday. It asks you to stop leaning on a cost that is no longer there.

**Sort by exploitation, not by score.** Start every patch cycle with CISA's Known Exploited Vulnerabilities catalog (KEV, the public list of bugs confirmed to be in use) and whatever threat feeds you already pay for. Anything in your environment that appears there jumps the queue, whatever its score. Anything that does not can wait its turn. One in 431 is a short list to start from.

**Treat "nobody would bother" as an open finding.** Every exception you granted because finding the thing would take too much effort deserves a second look, starting with anything internet-facing that runs jobs, takes uploads or administers something, and has no login in front of it. That is the ReliaQuest door, and it is the cheapest one to close.

**Keep the old bugs on the list.** A 2015 flaw that still works is not a historical curiosity; it is on a nation-state contractor's active list. If your exceptions register has entries older than some of your staff, read it again.

**Check your containment against an attacker that does not pause.** If isolating a compromised machine waits on a person to say yes during business hours, that is the step to look at. ReliaQuest's own recommendation is to automate containment, because more analyst hours will not match an agent working at machine speed. Again, that is a vendor talking about its own category, and it is also right.

<!-- [YOUR TAKE]: how you actually triage at your shop -- what jumps the queue, what you have learned to leave, whether a "nobody would find it" exception ever came back to bite you. -->

## When the crew is a line item

The attacker's crew used to be the most expensive thing in the operation, and the expense was protecting you whether you knew it or not. It is turning into a model subscription and a couple of rented servers, and the defenses that were really just bets on somebody else's stamina are the first to go.

The fix is not to outlast a machine. It is to stop counting on the other side's patience, and to spend your own effort where the people with the tools are actually aiming.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that the work an attack used to need a crew for now runs on a model bill and a few rented servers, so every defense that quietly relied on the attacker's effort being expensive needs re-pricing, starting with how you sort the patch queue.*
