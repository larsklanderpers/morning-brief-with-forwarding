# You Have 29 Minutes. Who's Awake?

**Status: Draft (v1) -- target Wednesday, 22 July 2026**
**Series: Weekday feed**
**Thread: Collapsed Timelines (cyber + agentic attack surface). Reconciles last week's HITL with attacker tempo, via Tuesday's three buckets.**
**Builds on: Monday's "The Compliance Tool Nobody Ordered Just Shipped as a Model" (20 Jul); Tuesday's "Accept, Refuse, or Delegate" (21 Jul); last week's "Click Approve" (15 Jul) and "The Loop Is Load-Bearing" (19 Jul).**
**Source spark: CrowdStrike 2026 breakout time 29 minutes (+89% AI-enabled adversaries); "Spirals" ransomware crew, intrusion-to-encryption under 24 hours; Sygnia, AWS foothold to full compromise in ~72 hours; identity attacks overtaking exploits as the top ransomware entry point; the Claude for Chrome extension-hijack flaw; Darktrace, 92% of security leaders worried about workforce AI agents (cyber briefs, 16-17 Jul).**

---

The average attacker now gets from first foothold to moving laterally through your network in twenty-nine minutes. Your incident bridge call takes longer than that just to convene.

Every building over a certain size has a sprinkler system, and the reason is not that the fire brigade is bad at its job. It is that fire spreads faster than any human response can physically arrive. So a century ago we made a decision that still sounds radical when you say it plainly: for one specific class of threat, the response has to be *automatic* -- pre-decided, machine-triggered, no human in the loop at the moment of action, because the moment is too short to fit one in. We did not fire the fire brigade. We moved the human's judgment *upstream*, into the design: where the sprinkler heads go, what sets them off, what they are allowed to soak and what they must never touch. The human still decides everything that matters. Just not in the thirty seconds while the fire is doubling.

Cybersecurity just crossed the line where it needs sprinklers. And last week I spent five days telling you to keep a human in the loop. So today I owe you a reconciliation, because on their face those two things are in a fight.

## The timelines collapsed

Look at what the last fortnight's reporting actually says, laid end to end. CrowdStrike's latest numbers put the average eCrime "breakout time" -- foothold to lateral movement -- at twenty-nine minutes, roughly sixty-five percent faster than two years ago, alongside an eighty-nine percent jump in attacks with AI assistance behind them. A newly named crew, "Spirals," ran a complete operation -- initial access, data theft, encryption -- in under twenty-four hours. Incident responders at Sygnia watched an AI-assisted actor go from a single AWS foothold to full environmental compromise in about seventy-two. And underneath all of it, the quiet structural shift: identity attacks have now overtaken vulnerability exploitation as the number-one way ransomware gets in.

That last one deserves the Hollywood-versus-reality treatment, because it is the whole misunderstanding in miniature. The cinematic hack is a hooded genius, a wall of green text, a progress bar racing a countdown. The real one is someone logging in with a valid credential they bought for the price of a coffee, and moving fast precisely because it is *mundane* -- no zero-day, no genius, just speed. They don't break in. They log in. And logging in is fast.

AI's genuine contribution to all of this is not some novel super-exploit. It is *compression.* The reconnaissance, the privilege mapping, the lateral movement that used to take a skilled operator a couple of weeks now takes a couple of days, because a machine does the tedious middle of the job. The kill chain did not get more clever. It got shorter. And a shorter kill chain breaks the arithmetic every mid-size security program was quietly built on: detect, triage, escalate, convene, decide. You cannot run that sequence in twenty-nine minutes. Nobody can.

## The new insider is an agent

There is a second front, and it is one this newsletter has been circling for a month. Darktrace's latest survey has ninety-two percent of security leaders worried about the security implications of AI agents spreading across their workforce -- and this month gave them a concrete reason. A disclosed flaw in Anthropic's Claude for Chrome extension could let a *different*, malicious extension installed alongside it puppet the agent -- simulate the clicks, trigger the actions -- and in doing so abuse the agent's legitimate access to Gmail, Docs, calendar, CRM.

Sit with the shape of that, because it is the agentic risk in one sentence: the agent's privileges *are* the attack surface. An AI agent gets provisioned like a piece of software -- quietly, by a team lead, with a checkbox -- but it behaves like an employee, holding real credentials and real access, minus every accountability structure we wrap around an actual hire. It is the Trusted Co-Worker I wrote about earlier this month, except now there is a documented way to make it act against you without it ever being "compromised" in the old sense.

And here is where Monday comes back around. Every agent you wire into your stack with delegated access is another door on the building. Controlling your own inference stack -- the whole argument for bringing the thinking home -- and scoping your agents tightly is not only a sovereignty play. It is a way of reducing how many doors that twenty-nine-minute clock has to go knocking on in the first place.

## The reconciliation

So, the fight. Last week: the loop is load-bearing, keep a qualified human in it. This week: the attacker moves in twenty-nine minutes and no human is that fast. Both are true. They do not actually contradict -- but only if you apply yesterday's three buckets to your own defense.

The moment of response is a *delegate* task, by necessity. Routine containment -- isolate the host, kill the session, revoke the token -- has to be automatic, because a human standing in *that* specific loop is not a control; they are latency, and the attacker is counting on it. That is the sprinkler, and installing it is not an abandonment of last week's argument.

Because the human stays load-bearing -- they just move *upstream*, to design time, where they can actually keep up. What is allowed to auto-contain, under what conditions? How big a blast radius is an automated isolation permitted to have before it needs a person? Which high-consequence, hard-to-reverse actions still stop and wait for a qualified *no*? That is the refuse-or-verify bucket, and it is the exact "qualified human at the boundary" from last week -- relocated to the one place fast enough to matter, the daylight hours when you design the system, rather than the three minutes when it is on fire. The pharmacist from "Click Approve" does not inspect every pill while the building burns. She designs the dispensing system so the dangerous combinations cannot leave the shelf in the first place.

Which tells you the failure mode to fear, and it is putting the human in the *wrong* loop. Two versions, both fatal. Park a person on routine containment and the sprinkler waits for a signature while the room fills with smoke -- too slow, by design. Or let automation make the high-consequence, irreversible calls nobody pre-authorized, and the sprinkler floods the server room because no one ever scoped what it was allowed to touch. The discipline is exactly Tuesday's: match the oversight to the clock *and* the stakes. Delegate the fast and reversible. Reserve the human for the consequential and pre-decided.

## What to actually do

**Inventory what can contain itself in seconds.** Segmentation, automated isolation, session kill, token revocation. Walk your response plan and mark every step that currently needs a human to click *during* the twenty-nine minutes. Each one of those is not containment; it is a notification with good intentions.

**Scope every agent like a privileged service account.** The Claude for Chrome lesson, generalized: an agent holding delegated access to email and CRM is a privileged insider, and it should be treated like one -- scoped to the minimum, monitored, and revocable in one motion. Not a productivity add-on you sprinkle across the org. A service account that happens to have a login.

**Move identity to the perimeter.** Identity is now the top ransomware vector, which means the return on phishing-resistant MFA, session monitoring, and identity threat detection just beat the return on another vulnerability scanner. They log in rather than break in -- so make logging in the hard part of the job.

**Pre-decide the containment policy, because that is your qualified human's real seat now.** The load-bearing human in security operations is not the one clicking during the incident; at twenty-nine minutes there is no time to click. It is the one who decided, in daylight, with a clear head, what the machine is allowed to do at 3am without asking. Staff *that* chair with your best judgment, and give it the authority to mean it.

Tomorrow I want to point all of this -- automate the routine, keep a qualified human on the consequential call, document in advance who is allowed to say no -- at a sector that has, quietly, been running exactly this playbook for years, long before anyone said the word "agent." The AML desk knows this dance. The clubs know it, and so do their cousins across the Pacific. That is Thursday.

For today, the uncomfortable question is not the one you have been trained to ask. It is not "were we watching." At twenty-nine minutes, nobody is watching fast enough, and pretending otherwise is how you end up with a notification where a control should be.

The question the next breach actually asks you is quieter, and it gets answered long before the breach arrives: *what did you decide, in advance and in daylight, that the building would do on its own?*

<!-- [YOUR TAKE]: Lars -- a war story here would be gold, yours or a client's: the gap between "we had a human review step" and "the human was asleep / it was 4pm / the diff was too long to read." That is the whole piece in one anecdote. -->

---

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that when the attacker moves in twenty-nine minutes, the human's job stops being to react and starts being to decide, in advance, what reacts for them.*
