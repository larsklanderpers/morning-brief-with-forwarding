# Nobody Was at the Keyboard

**Status: Draft — v2**
**Target: Thursday 9 July 2026**
**Series: Cyber / AI Security -- AI as Attack Surface**
**Cross-references: "The Agent Obeyed. It Just Wasn't Obeying You." (4 July) · "The Trusted Co-Worker" (7 July) · "The Contractor Who Finished the Job and Kept the Keys" (8 July)**

<!-- THREAD NOTE: This extends the AI as Attack Surface thread but flips the polarity of every prior piece. The Agent Obeyed / Trusted Co-Worker / Contractor were all about YOUR agent being turned against you. This one is about the attacker's OWN agent running the whole job with no human behind it. Same underlying property -- an LLM that acts without a human in the loop -- pointed outward instead of inward. That inversion is the piece. -->

---

For thirty years, the thing standing between a vulnerability and a catastrophe was a person. A skilled one. Someone who knew how to chain an exploit into access, access into movement, movement into money.

That person just became optional.

For all the time that I have been looking at, working in, and analyzing cyber security, one of the biggest defense points in everyone's favor was that it was very hard. There was a limited set of people with the skills to do these types of things. If you made the disincentive substantial enough or could fly under the radar well enough, then it wasn't worth it to an attacker to spend the time and energy on you. That was a level of protection in and of itself. If you had risen to a certain level where there were people who were looking at you but were non-state actors, you still had a relatively high level of confidence that your defense mechanisms would stand without issue. This belief that runs through the heart of the way cyber security has worked for at least two decades and probably longer has just been turned entirely on its head.

---

In late June, Sysdig's Threat Research Team documented something the industry has been bracing for and quietly hoping was further off: a ransomware attack executed end to end by an AI agent, with no human in the loop. They attribute it to a threat actor tracked as JADEPUFFER. A large language model handled the whole sequence itself -- initial access through a missing-authentication flaw in Langflow (CVE-2025-3248), then credential theft, then lateral movement, then encrypting and wiping the target's databases.

Not AI-assisted. Not a human running a model as a co-pilot. The model ran the operation. The human, if there was one at all, set the objective and walked away.

Read that again. Every stage of a ransomware attack that has historically required a skilled operator making judgment calls in real time -- pick the entry point, work out where you are, find the valuable data, decide what to encrypt -- was performed by software reasoning its way through, step by step, without a person deciding the next move.

---

## Why This Is the Line, Not Just a Faster Version of the Old Thing

It is tempting to file this under "attacks are getting faster." That misses what changed. Speed was already a problem. The CrowdStrike breakout-time numbers have been falling for years -- the window between an attacker landing and moving laterally is now measured in minutes. Automation made attacks fast a long time ago.

What JADEPUFFER removes is not time. It is the operator.

Automation follows a script someone wrote in advance. It is fast but brittle -- it does exactly what it was told and breaks the moment reality diverges from the plan. That brittleness has always been a defender's friend, because a canned attack fails in predictable ways. A human operator is the opposite: adaptable but expensive, scarce, and slow to train. The whole economics of serious intrusion rested on that scarcity. There are only so many people who can actually run a full-chain attack, and they cost money and take years to make.

An agent collapses that trade-off. It adapts like a human -- it can look at where it landed, reason about what it found, and decide what to do next -- but it costs like software and scales like software. You do not train it for years. You rent it for an afternoon. The scarce, expensive, judgment-carrying human at the centre of every serious attack was the ceiling on how many serious attacks could happen at once. That ceiling just lifted.

Just like with so many other skilled workforce concerns, the constraint on cyber crime was never really the tooling. It was always the labor to handle the tools. It was always the people who determined which tool was the right tool for the right problem. It was the fact that there were a limited number of people who could swing that particular hammer. You were able to defend against those things in part because the decision clock for how you address those things was longer because the number of people that an attacker could actually find to do this work was so very limited. The decision clock is not just compressed in this situation. It's been eliminated entirely.

---

## The Same Property, Pointed the Other Way

Regular readers will notice the machinery here is identical to the last three pieces -- it is just aimed outward.

"The Agent Obeyed" was about an attacker slipping instructions into content your agent reads, and the agent following them because it cannot tell your authority from a stranger's. "The Trusted Co-Worker" was about your agent's legitimate, designed behaviour routing your data somewhere you did not intend. Yesterday's piece was about agent identities accumulating access nobody governs. Every one of those is the same underlying fact: an LLM that reads, reasons, and acts without a human verifying each step.

JADEPUFFER is that exact property with the polarity reversed. In the earlier pieces, the ungoverned autonomous agent was yours, and the danger was what it did inside your walls. Here the ungoverned autonomous agent belongs to the attacker, and the danger is that it does not need a skilled person behind it to come through your walls. Same engine. One is idling in your environment; the other is being driven at you. The property that makes agents useful is the property that makes them dangerous, and it does not care which side of the firewall it is on.

---

## What Actually Changes for Defenders

The instinct will be to reach for a new product. Resist it long enough to get the model right, because the wrong mental model here leads to spending on the wrong things.

**Assume attack progression at machine speed, and plan response around it.** The comfortable assumption behind most incident response plans is that there is a human on the other end -- someone who sleeps, hesitates, makes mistakes, and takes hours between stages. An agent-run attack compresses initial access to data destruction into a window that may be shorter than your detection-to-response cycle. If your plan assumes you will notice, convene, and decide before the damage is done, that assumption needs testing against an adversary that does not pause.

**Close the doors an agent can walk through unattended.** JADEPUFFER's entry point was a known missing-authentication flaw in an exposed service. Autonomous attackers are, for now, opportunistic -- they succeed against the unpatched, the exposed, and the misconfigured, because those are the paths an agent can traverse without cleverness. The unglamorous discipline that has always mattered -- patch the internet-facing known-exploited vulnerabilities, kill the exposed admin interfaces, enforce authentication everywhere -- matters more, not less, against an attacker that scales.

**Detect behaviour, not operators.** Signature-based and human-pattern-based detection assumes an adversary with human tempo and human habits. An agent's activity may not match the timing, sequencing, or tooling your detection logic expects. The organisations that hold up will be the ones alerting on what is happening -- anomalous data access, mass encryption behaviour, credential use out of pattern -- rather than trying to fingerprint who is doing it.

**Do not overreact to one data point, but do not dismiss it.** This is one documented case. It is not yet the dominant attack pattern, and anyone selling you "AI ransomware protection" this week is ahead of the evidence. But the direction is not ambiguous, and the economics point one way. Treat this as the proof of concept that tells you where to invest over the next few budget cycles, not as a reason to panic-buy this quarter.

---

## The Grind Was Always the Point

There is a cinematic version of the hacker that has done real damage to how organisations think about defence -- the lone genius, the scarce prodigy, the person whose rare skill is the whole threat. It made attacks feel like something that happened to other, more interesting companies. If the danger is a genius, and no genius is bothering with you, you feel safe.

JADEPUFFER is the end of that comfort. The genius has been distilled into something you can rent, and it will happily spend its afternoon on a target no human operator would have considered worth the hours. The defence, ironically, has not changed at all -- it is the same patient, unglamorous grind it always was: know what you expose, close what you do not need, watch what your systems actually do. The difference is that the excuse for skipping the grind, the belief that you were too small or too dull to draw a skilled attacker, just stopped being true.

The attacker no longer has to be skilled, or fast, or relentless. The software handles all of that for them. So the only question left is whether you are, and whether your skills are sufficient not only to the challenge itself but to the speed and repetition. The attacker is the steam drill. You are John Henry. How will you adapt?

---

*Sources: "AI Agent Runs First Fully Autonomous Ransomware Attack" -- JADEPUFFER via Langflow CVE-2025-3248 (The Hacker News / Sysdig Threat Research Team, July 2026). Supporting context: CrowdStrike breakout-time reporting; Darktrace State of AI Cybersecurity 2026. Cross-reference: "The Agent Obeyed. It Just Wasn't Obeying You." (4 July), "The Trusted Co-Worker" (7 July), "The Contractor Who Finished the Job and Kept the Keys" (8 July).*

*Lars Klander writes about cybersecurity strategy, policy, and emerging threats.*
