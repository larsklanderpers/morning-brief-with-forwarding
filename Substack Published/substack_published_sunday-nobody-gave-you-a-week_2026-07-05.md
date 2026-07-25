# Nobody Gave You a Week

**Status: Draft**
**Target: Sunday, July 5, 2026**
**Series: Sunday Capstone — Week of June 30 – July 4**
**Threads synthesised: Ad Hoc Regulatory Regime · AI as Attack Surface · AI Sovereignty / Infrastructure**

---

Three things happened this week that most organisations will file as separate stories. They are not separate stories. They are three expressions of the same underlying shift -- and once you see it, you can't unsee it.

The first: the average time between an attacker getting into your network and moving to a second system has dropped to 29 minutes. Not 29 hours. Twenty-nine minutes, on average, with the fastest recorded breakout time this year measured in seconds. This is what AI has done to offensive operations. Attackers have automated the slow part.

The second: CISA added a critical vulnerability to its known exploited list and gave US federal agencies 48 hours to patch. Not a month. Not a standard remediation window. Forty-eight hours. A SharePoint RCE that was already being exploited in the wild, in a product that is deployed in tens of thousands of enterprises worldwide.

The third: Anthropic's Fable 5 -- the frontier model that powers Claude -- was banned by the US Commerce Department on June 12 and restored on July 1. Nineteen days. The entire cycle of imposition, dispute, negotiation, technical concession, and reinstatement happened faster than most enterprise change management processes take to schedule their first meeting.

Three different layers. Three different clocks. All of them running faster than the organisational rhythms built to respond to them.

---

## The Clock Was Always the Variable

There's a concept in aviation called "startle response." When something unexpected happens in the cockpit, even highly trained pilots experience a brief window -- sometimes only seconds, sometimes longer -- where the cognitive load of surprise temporarily overwhelms the ability to execute trained responses. The antidote the aviation industry landed on was not to train pilots to be unsurpriseable. It was to take the thinking out of the highest-pressure moments entirely.

Checklists. Memory items. Pre-decided responses to defined conditions. When this light comes on, you do these things in this order, without stopping to convene a committee about whether this is really that kind of light.

Airlines figured this out after a series of accidents where the crash sequence began not with mechanical failure but with a crew that was capable but deliberating when they needed to be executing.

The cybersecurity, regulatory, and geopolitical events of the last week are a unified argument for applying the same logic to how organisations respond to time-compressed threats. It's no longer just that proactive boards result in the best run, best performing organizations: it's that an organization whose governance is reactive is so much more exposed than ever before that a proactive board is now a business continuity requirement.

---

## Layer One: The Technical Clock

Twenty-nine minutes is not a gap you close with faster humans.

This week's CrowdStrike data confirmed what practitioners have been seeing in incident response: AI-enabled adversaries have cut the breakout window by 65% since 2024. The Azure CLI password spray that ran across June -- 81 million login attempts in fourteen days, 78 accounts compromised across 64 organisations -- was not a human operation in any meaningful sense. No human attacker could sustain that pace across that many targets with that level of coordination. This was a machine operating at machine speed.

What 29 minutes means operationally: if you discover a compromise and your incident response process requires a phone call to a manager, approval from a change board, and a ticket in your ITSM system before you can contain it -- you are already in the lateral movement phase before the ticket is logged.

The organisations that get through the current environment are the ones that have pre-decided. Not "we will convene when an incident is detected" but "when condition X occurs, these specific automated responses are triggered, these specific people are authorised to act without escalation, and these specific containment actions execute without a human in the loop."

This is not a tool selection question. It is a governance question about who is authorised to make which decisions in real time -- and which decisions have been made already.

The Darktrace data from this week adds a darker dimension. In more than 90 organisations, the AI tools deployed inside enterprise environments were turned against those environments -- used to generate malicious commands, exfiltrate data, produce targeted social engineering from internal communications. The agent doing the job was the same agent being weaponised. The sophistication of the attack leveraged the sophistication of the defence.

When I wrote earlier this week about the agent that obeyed -- just not you -- the implication was about external attackers hijacking AI through crafted content. The Darktrace finding is the next iteration: the tool you trusted, doing exactly what it was designed to do, turned out to have a different employer in the data stream.

Both of these run on the same clock. Twenty-nine minutes. Pre-decide, or lose the window.

---

## Layer Two: The Regulatory Clock

The SharePoint KEV entry with a 48-hour federal patch window is one data point in a pattern.

CISA has been shortening its expectations throughout 2026. The Known Exploited Vulnerabilities catalogue has become less of a watchlist and more of a countdown timer. When something lands on it, the implicit message is: the window to decide whether to treat this seriously has already closed. The question is whether you act in hours or days.

What most enterprise patch management programmes are built for is a different kind of threat: something that might affect us, which we'll assess over the next two weeks, prioritise against our other work, schedule into the next maintenance window, and apply before the quarter ends. That process is now formally inadequate for a growing subset of vulnerabilities.

The December 10 deadline for Australia's Privacy Act automated decision-making amendments is a slower version of the same problem. Five months sounds like a long runway. It isn't, for what the amendment actually requires: a complete inventory of every AI system making substantially automated decisions that significantly affect customer rights, disclosure of what personal data those systems use, and a meaningful pathway for customers to request human review.

The organisations that will be caught out in December are not the ones that don't know the rule exists. They're the ones that know the rule exists and have been waiting for the regulator's formal guidance, scheduled for September -- which gives them ten weeks between guidance and deadline, for a programme of work that requires board approval, legal review, vendor notification, and customer-facing communications changes.

The compliance sprint is five months. The actual decision-making runway, accounting for how decisions actually get made in large organisations, is closer to eight weeks.

Pre-decide what falls into scope for December. Do the inventory now, before the guidance, so the guidance confirms your approach rather than triggering your approach.

---

## Layer Three: The Geopolitical Clock

The Fable 5 cycle is the strangest clock of the three, and possibly the most instructive.

June 12: Commerce Department orders Anthropic to suspend access for all foreign nationals, including their own non-citizen staff. No notice. No published criteria. No defined appeals process.

June 30: Controls lifted, after Anthropic trained a new classifier and demonstrated it suppresses the relevant technique at 99%+. Commerce Secretary Lutnick cites the company's "close cooperation with government."

July 1: Fable 5 returns globally.

Nineteen days. The entire cycle -- from shutdown to restoration -- took nineteen days. For businesses that had built workflows around Fable 5, nineteen days without access was a disruption they either had or didn't have a plan for. The ones that had thought about it beforehand fared better than the ones that convened a crisis response on day two.

The deeper lesson from those nineteen days is not about Anthropic specifically. It is about what "infrastructure" means when infrastructure is software running on someone else's servers, governed by export control law written for semiconductors, administered by a department without published criteria for what crosses the line.

As I wrote this week in the piece on KYC reversal: more than 100 cybersecurity professionals signed an open letter disputing that the technique cited by Commerce even constituted a genuine guardrail bypass. It didn't matter. The standard was what the regulator decided it was, in the moment, in private. And the resolution mechanism was a private negotiation, not an independent review.

The organisations that navigate this well will be the ones that pre-decided: if a critical AI vendor becomes unavailable, what is the 30-day continuity plan? Which workflows fail gracefully and which ones stop? What's the decision tree -- switch to an alternative vendor, fall back to manual processes, or invoke a contractual SLA?

This is the inference sovereignty argument from the sovereignty thread -- "Not Where It Lives. Where It Thinks" -- made concrete. You don't just need to know where your AI's thinking happens. You need to know what you'll do when the thinking stops.

---

## The Single Frame

Put the three clocks together and a single frame emerges.

The adversary clock is running at machine speed. The regulatory clock is compressing to hours and weeks. The geopolitical clock can zero out your vendor stack in days with no warning and no published criteria.

None of these are problems you can solve at the speed they move if your response architecture requires you to think through them when they arrive.

The question for every board, every CISO, every risk committee reading this is not "how do we respond faster?" It is "what have we already decided?"

What are the automated responses that execute without escalation when a critical indicator is triggered? Who has pre-delegated authority to act on a 48-hour patch window without convening the change board? What does the first 72 hours look like if a tier-one AI vendor is unexpectedly unavailable?

These are not incident response questions. They are governance questions that need to be answered in a planning meeting, not at 3am when the incident is live.

---

## What This Week Built

The connective tissue is time. The time you have to respond to a technical incident. The time you have to comply before the regulator acts. The time you have to adapt before the vendor's access policy changes beneath you.

Nobody gave you a week. In some cases, nobody gave you a day. Regardless of how fast the systemic response times need to become to have a decent shot at protection, the critical point for all of us here is that the speed exceeds human reaction times, even without system limiters. Every attacker is now Jet Li. It is functionally impossible for you and your team to react to these items in real time, because you are moving in slow motion no matter how well trained you are.

The only viable response to a world that moves at this speed is to decide before you have to. Because if you don't, the decisions will be made for you. And not to your advantage.

---

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Sundays he tries to make it all make sense when it's coming so fast and furiously that most of us don't even know where to begin.*
