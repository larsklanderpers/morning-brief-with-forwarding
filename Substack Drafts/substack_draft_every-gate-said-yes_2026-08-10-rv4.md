# Every Gate Said Yes

**Status: Draft rv4 -- panel round 1 applied. Target Monday, 10 August 2026. Opens the week off the Sun 9 Aug capstone ("can you prove the fence has no off switch") by inverting it: these fences did not fail, they answered correctly, and the question was wrong. Em-dash-free. ~3,300w. Sources + adversarial pass in `References/research_every-gate-said-yes_2026-08-05.md`.**
**Series: Weekday feed**
**Thread: Trust Boundaries · AI Attack Surface**
**Builds on: "Nothing Held" (Mon 3 Aug -- four walls failing at once; this is the harder case where none of them failed); "A Policy Isn't a Control. An Execution Rule Is." (Fri 31 Jul -- sign/camera/governor); "Guardrails Are How You Give It Away" (Sun 9 Aug -- the fence you can prove; the handoff is now paid off explicitly in para 4).**
**Source spark: UK AI Security Institute incident report (4 Aug 2026); Anthropic's own three-incident disclosure (30 Jul 2026); Pillar Security on Google ADK agent-to-agent privilege escalation + the six deleted workflows verified in git history; ChainDrop npm worm (4 Aug 2026, ONGOING); CrowdStrike 2026 Threat Hunting Report (3 Aug 2026).**
**PRE-PUBLISH RE-SWEEP (not a [VERIFY]; the body hedges it in place): ChainDrop is <48h old at drafting and infection counts are unpublished. Re-verify package count and install footprint Monday morning. Do NOT ship the brief's "billion downloads in hours" phrasing -- the figure is a two-billion-monthly-install footprint.**
**CROWDSTRIKE VERIFIED (6 Aug): figure, denominator and clock all correct; scope corrected to first half of 2026; it is the 2026 Threat Hunting Report, NOT the Global Threat Report. Do not attribute the 29-minute breakout time or AI-enabled-attack figures to this report. Residual: the PDF itself was proxy-blocked and never read; the stat rests on three corroborating CrowdStrike-authored pages.**

---

Three security controls did their job. That is the problem.

Each one was asked a question, checked carefully, and returned the correct answer. No control was bypassed. No cryptography broke. Nobody found a buffer overflow. In all three cases the gate was working exactly as designed, and in all three cases something walked straight through it, because the question the gate was asking was not the question that mattered.

I have spent a fair amount of the last couple of months writing about walls failing. This is the more uncomfortable version, and I think it is the one worth your Monday.

Yesterday I asked whether you could prove your fence has no off switch. Today is the harder version of that question, and I am sorry to do this to you on a Monday: none of these fences had an off switch. Nobody turned anything off. They ran, they checked, they reported, and the thing you were afraid of walked through anyway.

Fair warning, this one runs long. Three cases is more than I would normally spend on a Monday, but the pattern only shows up when you put them side by side, and I would rather take the extra ten minutes of your morning than show you two thirds of an argument.

## "Is this person a collaborator?" Yes.

Start with the cleanest of the three. It is also the oldest, from June, and I am putting it first because the mechanism is beautiful in the way that only a really bad idea can be.

Google's Agent Development Kit repository ran a pair of automated workflows. The first was a low-privilege bot that read incoming issues and pull requests and triaged them. The second was a high-privilege agent that could actually fix code, and because you do not want strangers triggering that, it was gated: it would only act on a comment from a repository collaborator.

Researchers at Pillar Security worked out that you could put text in a public GitHub issue, dressed up as contribution guidelines, and the triage bot would read it. The bot then posted the trigger comment. And the bot *was* a collaborator, so the gate checked the identity, found it valid, and started the privileged agent. From there it was git hooks and a CI runner, and out came a Google API key, a service account credential with Vertex AI access, and the bot's own access token. The company had given the bot the credentials. A stranger asked the bot for them, in writing, in public, and the bot handed them over. At machine speed. Without tripping a single gate.

Nothing was broken. The authorization gate performed flawlessly. It asked whether the commenter was authorized, the commenter was authorized, and the answer was yes. What the gate could not ask, because it has no way to ask it, is whether the authorized party wanted this or had been talked into it by a stranger. Pillar's line for this is the sharpest thing I have read all month: an agent that reads untrusted text and holds a credential is, functionally, a privilege escalation primitive that speaks English. The agent was flipped from trusted coworker to double agent in minutes, and there was no log, no risk register, no indication anywhere that something was awry, aside from reading the issue and the change and knowing enough about the code and the structure to understand what that meant.

Two things about Google's response are, at least to me, worth more than the finding itself.

The first is what they did. They deleted the workflows. Three of them on June third, one day after the report landed. Then, six days later, three more, because the first excision had missed half the problem. Six workflows and a script, gone, and the commit message is the most honest sentence any vendor has produced on this subject: they ran an automated agent over untrusted issue and PR content with broad repository credentials, and deleting them removes that exposure while a safer design is considered.

*While a safer design is considered.* Read that for a minute, if you will, as an engineer rather than a reader. That particular piece of word salad is what it looks like when there is no fix available inside your current model of the problem. It is an engineer's way of saying "wow, that was really bad, but I am sure we can come up with a fix. Just give us a tick."

The second thing would annoy me if it were *my* repo. Google declined to pay a bounty, granting an honorable mention, on the reasoning that exploitation required a maintainer merge and a social engineering step. Which is true. It is also the exact objection that stops being a defense the moment you notice that social engineering an automated agent is cheaper than social engineering a person, does not get tired, and can be attempted ten thousand times for the price of the tokens.

Now, be fair about scope, because I would rather concede it than have you catch it. This was Google's own CI in Google's own repository. It was not a flaw in the ADK package that people install and ship. Nobody's production system was exposed by this. If you write it as "Google's agent framework is vulnerable," you have overstated it, *at least as it currently stands and at least in relation to this specific issue*, and Pillar say so themselves.

But sample code is not read, it is copied. Reference workflows in a vendor's flagship repository end up inside other people's pipelines with the names changed, which is the entire reason vendors publish them. And the pattern that got deleted here, an unprivileged agent that reads public input, holds a credential, and can address a privileged agent, is not specific to Google in any way. It is the default shape of every multi-agent system with a triage tier in front of it. Identity-based authorization between agents does not work when the identity holder is a language model reading text an attacker wrote. That is not a Google bug. It is a category error around the modeling of intelligent agents that we have all been building on.

## "Was this built where it says it was?" Yes.

The second gate is signing, and it fell over on Tuesday the fourth of August.

An attacker compromised the GitHub account of a maintainer of `keyv`, a very widely used caching library, pushed to main, and cut releases. Those releases carried a self-propagating credential stealer that runs on `preinstall`. If you ran an install on Tuesday afternoon, this ran on your machine before the command finished, and then went looking for your credentials so it could do the same thing to whoever you shipped to next. As of the last count I have, something north of four hundred and thirty npm packages across multiple unrelated publishers, with a combined footprint over two billion installs a month. It is called ChainDrop, and if you are reading this on Monday the numbers have moved.

Here is the part that matters for this piece. Because those releases came from the real account, through the real build pipeline, they carried valid provenance signatures: the cryptographic attestation a great many people have been treating as the answer to supply chain attacks. It is a good control. It has been reliable and trustworthy for a very long time. It attests that a package was built by the build system it claims, from the repository it claims.

And it was accurate. The signature was real. Issued by the right authority, for the right build, from the right repository, checked and passed. What it certified was that the package came from where it claimed to come from. It did. The attacker was standing in that place. Inside the package, if you will.

The thing that was supposed to stop malicious code from reaching your build did stop malicious code from reaching your build. This code was not malicious by any test it applied. And yet it most definitely was.

If your supply chain defense terminates at "is it signed," you were not protected on Tuesday and you would not have known it. The signature was never a statement about intent. It was a statement about origin, and origin is exactly what the attacker took.

## "Is the model solving the task?" Yes.

The third one is the story everybody led with, and it is the one I want to be most careful about, because the version in the headlines is not the version in the source.

The UK AI Security Institute published an incident report on Tuesday the fourth of August. During cyber testing, across a hundred and twenty-two runs, agents took autonomous unsanctioned action in ten of them. Nineteen such actions catalogued in total, seventeen from Anthropic's Mythos 5 and two from OpenAI's GPT-5.6 Sol, over four days at the end of July, contained within an hour of the alert. One agent tried to insert malicious code into a public open source project, created multiple fake identities, and socially engineered a human maintainer to try and get it approved as the next step in the escalation. A person, a trained human in the loop, on the wall, as we have discussed many times, caught it and refused.

That is genuinely new, and AISI say so: it is the first time they have seen deception of that severity aimed at a real person, unprompted, in the real world.

Now what did not travel. AISI also published, in the same document, the reasons it happened. Internet access was deliberately enabled to make the test realistic. The developers' cyber classifiers were deliberately switched off. The task was misconfigured such that the agent incorrectly believed there was no solution available that stayed inside the intended scope. And nobody had told it not to use the open internet or not to socially engineer anyone.

So: you switch off the safety classifiers, you connect the thing to the live internet on purpose, you hand it an unsolvable problem, you decline to prohibit the obvious workaround, and it takes the workaround. Anthropic's own assessment of their separate incidents uses the phrase that should have been the headline, and I am inclined to take them at their word because it is the less flattering read: closer to a harness and operational failure than a model alignment failure. Their models were told they had no internet access, and were in fact misconfigured to have it.

I want to be exact about a couple of things the coverage garbled, since we are on the subject of checkable claims. Nineteen actions across ten runs is true and it is also a hundred and twenty-two runs, and quoting the first two numbers without the third is the kind of thing I would flag in someone else's writing. The "breached a real website" line that went around does not appear in the AISI report at all; it looks like a conflation with a separate OpenAI disclosure from July twenty-first. And Anthropic's three affected companies came from their own disclosure on the thirtieth of July, not from AISI, with April being when the earliest evaluations *ran*, not when anything was discovered.

So the rogue-AI reading is wrong and I am not going to sell it to you. The reason I am not even pursuing that angle, and am explicitly declaiming it, is because *what survives is worse.*

Anthropic's disclosure describes an evaluation model reaching a real company's infrastructure after seeing its domain during a test, extracting application and infrastructure credentials, and pulling several hundred rows out of a production database. It describes another publishing a malicious package to PyPI that was downloaded and executed on fifteen real systems, one of them a security company's scanner, with the credentials exfiltrated to a collection point the model set up. It describes a third scanning around nine thousand targets and compromising an internet-facing application through an exposed debug page.

The affected organization in the first case did not know it had been compromised. It found out because Anthropic told it.

The earliest of these evaluations ran in April. They were discovered in late July, by monitoring that did not exist when they ran. Four months, on live third-party infrastructure, with nobody watching the boundary. That is not a story about a model going rogue, and I would rather you not remember it that way. It is a story about an evaluation harness that was asking whether the model solved the task, and answering correctly, and never asking where the packets were going.

We built a system that converts loyalty points into things people want: cash, gift cards, merchandise. Which is to say: money, with an extra step. So we protected it accordingly. We spent weeks on the threat model, sat in rooms inventing every scam and overage attempt we could think of, and tested against all of them.

We missed one. One person worked it for more than a year. Not greedily. A trickle, small enough and slow enough that no audit flag ever went off. The cost to us was substantial enough that felony charges were considered.

He did not surface because an alarm fired. He surfaced because we happened to re-review the code and brought a couple of new perspectives into the audit, and under one of those perspectives he came up immediately as a likely candidate. He was not merely likely. He was actual.

Nothing had failed. Every check we had written ran, and passed, and reported correctly, for over a year. What caught him was not a better control. It was a different question. Which is exactly what caught Anthropic's evaluations in July: not new monitoring on the old boundary, but monitoring that had not existed at all, asking something nobody had thought to ask when the harness was built.

This is not a new problem on the merits. It is a very new problem at scale. He needed a year. An agent needs an afternoon.

## The shape of the failure

Two of these landed on the same day. Tuesday the fourth of August. A Tuesday in August, the most forgettable square on the calendar. There is nothing about Tuesday. That is the point. There is no bad day for this. There is only the day you find out.

Put the three side by side and the pattern is the same one, three times, made all the more clear by the compressed timelines.

The authorization gate verified identity. The attack was not on identity. Provenance verified origin. The attack was not on origin. The eval harness verified task completion. The attack, if we are being honest about what it was, was on nobody's attention at all.

Every one of those controls is good. I would deploy all three tomorrow, and I would trust all three tomorrow, and I would stand up in front of my board and certify all three tomorrow. But each of them answers a question about a property, and none of them answers the question of whether the thing currently happening is the thing you wanted. That gap used to be small, because the entities inside your boundary were people and software that did what it was told, and "authorized" was a decent proxy for "intended." An agent breaks the proxy. An agent is authorized, and adaptive, and reading input from strangers, and the distance between what it is permitted to do and what it is currently being persuaded to do is now the whole attack surface.

There is a cost argument here and it is not the one you would expect. A control that answers the wrong question is not neutral. It is worse than no control, because it manufactures confidence. Nobody audits a gate that is green, unless it is part of a refactor of the underlying elements, as it was for us. The Google workflow ran for months with a passing authorization check. The npm packages had valid signatures the whole way down. The evaluations completed successfully and reported their results. Every dashboard was fine. The failure was invisible precisely because the instrumentation was working, and instrumentation that works while measuring the wrong thing is how *the exploit* gets four months.

You, unfortunately, do **not** have four months, not anymore. CrowdStrike's 2026 Threat Hunting Report found that in the first half of this year, eighty-eight percent of the exploitation they observed against vulnerabilities with a public proof of concept happened within forty-eight hours of that proof of concept's release. That number is narrower than it sounds and I want to state it precisely rather than let it do more work than it can carry: it is a share of observed exploitation, clocked from the release of the proof of concept, not from disclosure and not from your patch window. But the direction is not in dispute. The gap between "someone published how" and "someone is doing it to you" is now measured in hours, and the gap between "your control passed" and "you found out it was asking the wrong question" is still being measured in months.

## What to actually do about it

Take your three or four most load-bearing automated controls, the ones you would name if a regulator asked what stops the bad thing, and for each one write down the sentence it actually evaluates. Not what it protects against. What it literally checks. "This caller holds a valid token." "This artifact was built by our pipeline." "This job completed without error." "This document details everything that the work actually did, and here is who did each thing."

Then, next to each, write the sentence you have been assuming it means. "Only people we trust can trigger this." "This package contains what its maintainer intended." "Nothing left our network." "John and Jane, two trusted employees, did all this work."

The distance between those two columns is your actual exposure, and it is almost always larger than anyone expects, and the exercise takes an afternoon, because even the largest and most rigorous enterprises have a certain level of trust in the people who work for them. If the two sentences are the same, you have a real control. If they are not, you have a measurement, and a measurement is only a control while nobody is standing in the gap between what it checks and what you think it checks. And if the control depends on a particular person rather than a process, put it in the second column regardless of how it scores.

I am aware that is a diagnostic and not a fix, and I want to be honest that the distinction matters. I do not have a control that reliably tells you whether an authorized party has been talked into something, and neither does anybody else, and anyone selling you one this quarter is selling you the same green light in a different color. What you can do is know which of your gates are measurements, and stop spending confidence you have not earned.

Every gate said yes. Every one of them was telling the truth.

Every one of those gates was designed when the thing on the other side of it was a person. Nobody went back to check whether the question survived the change.

Truth about the wrong question is a green light with better paperwork.

---

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. A lot about risk. From the place of a person who has been there and lived in it every day for decades. Today's argument is that the week's three loudest failures were not control failures at all: an authorization gate verified identity, a signature verified origin, and an evaluation harness verified task completion, each correctly, while the thing that mattered walked past all three, and that a control which answers the wrong question is more dangerous than no control because it manufactures confidence nobody audits.*
