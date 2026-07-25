# When Five Spy Agencies Agree, You Should Listen

Five of the world's most secretive intelligence agencies just told the world that AI will be able to beat their defenses within months. They don't say things like that unless they mean it. And even more importantly, they wouldn't admit it if they weren't scared of it.

The Five Eyes — the intelligence partnership between the United States, United Kingdom, Australia, Canada, and New Zealand — issued a joint statement this week warning that frontier AI models are improving fast enough to make the current generation of cybersecurity assumptions obsolete. Not in five years. Not in three. Months.

Before I dig into this any further, it's worth noting how unusual a joint Five Eyes public statement is — they rarely agree on what to have for lunch, let alone release coordinated public threat assessments. Despite having a "special relationship", the trust between these agencies, especially over the last few years, has... well, let's just say it's not as high as it used to be. So to come together and publicly admit that they are on the back foot — it's something of a big deal, and not just to the security professionals.

---

## The Statement They Didn't Have To Make

Intelligence agencies don't do public relations. They don't issue warnings because they enjoy public discourse. When they write something down and put five country seals on it, it's because the internal picture is alarming enough that they've decided the risk of *not* saying something outweighs the risk of tipping their hand.

The statement is blunt: AI "lowers barriers for malicious actors and increases the speed and complexity of attacks." The rapid pace of frontier AI development means your cyber risk assumptions — the ones your board approved, the ones your insurance underwriter rated, the ones your compliance team signed off on — can become outdated in months, not years.

That is not hedged language. That is as close to an alarm as a government advisory gets.

And what they did not say explicitly but they certainly implied is that this is not the future — if your cyber risk assumptions are more than a year old, you need to take them down off the shelf and dig in deep. You probably also need to add that review to your monthly systems agenda. The threat clock is no longer measured in years.

---

## The Anthropic Story (And Why the Headline Missed the Point)

You may have seen the headline: *Anthropic's AI broke into almost all NSA classified systems in hours.* It spread across every major outlet this week, and it's not quite right — but the reality is more interesting than the clickbait version.

What actually happened: NSA Director General Joshua Rudd briefed lawmakers on an authorized red-team exercise (a red-team exercise is a full-scope, simulated cyberattack designed to test an organization's security defenses and incident response capabilities). Anthropic's Mythos model was given permission, by the NSA itself, to probe its own classified systems for weaknesses. It wasn't a breach. It was a test. Think of it like a bank hiring a safecracker to test their vaults — and then being surprised when the safecracker opens the vault.

The Economist's original framing overstated the testimony. Anthropic's own account describes the flagged behavior as analyzing a codebase and fixing identified issues — not autonomous offensive intrusion.

But here's what *is* true, and it matters far more than the dramatic version: the U.S. government's response to the *test results* was to treat an AI model like a weapons system.

On June 12, the Commerce Department issued a directive barring every foreign national — including non-citizen employees at Anthropic itself — from accessing Fable 5 and Mythos 5. This is the **first time in history the United States has applied export controls directly to an AI model** rather than to the chips or hardware running it.

That's not a PR move. That's a government deciding that a commercial AI product is too dangerous to let out of the country.

We'll talk about the broader implications of export controls another day. What matters here is simpler: the Mythos test showed that a bad actor doesn't need months of persistent access to crack the important pieces — it can do it in hours. That single result changed the entire threat calculus. The models are already this capable, and they've been largely self-improving for the last 60 days. The uncomfortable position the intelligence community now finds itself in: Fable 5 needs to remain restricted because of what it can do offensively — but without it deployed defensively, no one is entirely certain how current systems would hold up against a sophisticated attack. *We need the most dangerous piece of software ever designed to protect us from its evil twin.*

---

## What "Months, Not Years" Actually Means

The Five Eyes advisory didn't just warn about AI-powered attacks in the abstract. It described a specific structural shift: the window between a vulnerability being discovered and it being exploited is collapsing.

We already saw this week that 28.3% of new CVEs are now being exploited within 24 hours of disclosure. AI is driving that acceleration — automated scanning, automated exploit generation, automated delivery. The human bottleneck in the attack chain has been removed.

Think of it this way. The traditional security model assumes that defenders have time — time to patch, time to detect, time to respond. That assumption is baked into every patch cycle, every incident response playbook, every SLA your security operations team has ever written.

AI doesn't take weekends off. It doesn't wait for the change advisory board to meet. It doesn't need to read the CVE description before it knows how to exploit it. And it either no longer requires a social engineering attack to get in, or it's so good at social engineering it doesn't even trigger the bot warnings in your system (see my Substack from the other day, "The Malware That Learned to Lie to Your AI", if you don't believe me).

---

## The Hollywood Version vs. What's Actually Coming

The way we imagine AI-enabled cyberattacks usually looks cinematic — rogue superintelligence, global infrastructure collapsing, lights going out. That framing is almost certainly wrong, and it's also dangerous, because it points attention in the wrong direction.

What's actually coming looks mundane. It looks like a phishing email that's perfectly tailored to you — your real name, your real company, your boss's actual writing style — generated in seconds and sent to ten thousand people like you simultaneously. It looks like an attacker probing your network for vulnerabilities faster than your team can read the morning alert digest. It looks like a credential stuffing campaign that adapts in real time based on what's working.

The scary version of AI attacks isn't the one in the movies. It's the one that looks exactly like everything you already deal with — just faster, cheaper, and with no human needing to be awake to run it.

It's important to understand that most hackers — even state-sanctioned ones — are in it for the money. The risk of things going sideways into crazy destructiveness is actually pretty low; they want the world's economies to keep running so they can siphon a couple of little percentage points off the top (a trillion here, a trillion there — pretty soon it's real money). They don't *want* mass destruction; what they really want is time on task so they can take advantage of every piece of information they can siphon. So the risk isn't WOPR, the risk is your small business having $0 in the bank account the day before payroll. The risk is your wire transfer going through while both accounts on either side get drained by the banking system itself, thinking it's doing the right thing. In many ways, the personal and business risk outweighs the existential risk by orders of magnitude.

---

## What The Advisory Actually Says To Do

The Five Eyes didn't just issue a warning. They included specific guidance, and it's worth reading — because it's deliberately not technical.

The advisory frames this as a **core business risk**, not an IT problem. It explicitly states that "breaches will occur" — resilience, not prevention, is the imperative. For boards that have been running on the assumption that the right security investment equals zero breaches, that sentence should end the meeting.

The recommendations:

**Limit access.** The simplest, least glamorous defensive move — reduce who can get to what. AI-enabled attackers are extraordinarily good at lateral movement (spreading from an initial entry point across a network). The smaller that initial foothold, the less damage they can do.

**Accelerate patching.** The advisory explicitly calls this out. Not "improve your patch process." Accelerate it. The 28.3% exploitation-within-24-hours figure is why. A patch cycle measured in weeks is a policy decision to accept significant risk on critical vulnerabilities.

**Integrate AI defensively.** This one is practical and urgent. Organizations using AI in their security operations are already detecting threats faster, catching anomalies earlier, and responding more quickly. The gap between organizations doing this and those not doing this is growing by the month.

**Treat cyber as a board-level accountability.** The advisory explicitly calls for empowering security leaders with authority and resources — not just budget, but decision-making power. Security teams that have to escalate through three layers of management before they can isolate a compromised system are not going to win in a fight where the attacker is operating autonomously.

---

## The Part Decision-Makers Need to Sit With

The Anthropic export control is the canary in the coal mine. When the U.S. government decides a commercial AI product is too powerful to share with foreign nationals — including the people who *built* it — that tells you something about the capability threshold we've crossed.

Five intelligence agencies issuing a joint statement tells you something about what they're seeing in classified channels that they can't say publicly.

And a 28.3% same-day exploitation rate tells you something about the math of defense at current speeds.

None of these are problems that get solved with last year's security strategy. The threat model has changed. The question for every organization right now isn't whether to respond — it's whether the response happens before or after the incident that makes it unavoidable.

It's a lot to sit with. But the math is simple: you don't need to be perfect, you just need to be harder to hit than the next target. Take down that cyber book off the shelf, turn to the deferred section, and start working through it. Defense in depth. Warning triggers. A patching cadence that actually matches the threat clock.

Stay safe. Stay secure. And make sure the bear has someone easier to chase.

---

*Sources: [CNN](https://www.cnn.com/2026/06/23/world/ai-five-eyes-warning-cyber-threat-intl-hnk) | [CBS News](https://www.cbsnews.com/news/ai-bypass-cybersecurity-systems-months-not-years-five-eyes/) | [NSA Statement](https://www.nsa.gov/Press-Room/News-Highlights/Article/Article/4523810/five-eyes-cyber-security-agencies-statement/) | [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-powerful-mythos-ai-reportedly-breached-almost-all-nsa-classified-systems-within-a-few-hours-during-red-team-test-report-sheds-more-light-on-the-u-s-governments-sudden-ban-on-the-flagship-models) | [Security Affairs](https://securityaffairs.com/194016/ai/anthropics-mythos-ai-broke-into-almost-all-nsa-classified-systems-in-hours.html) | [CyberScoop](https://cyberscoop.com/five-eyes-alliance-say-advanced-ai-hacking-models-months-away/) | [CSO Online](https://www.csoonline.com/article/4188049/change-your-cyber-risk-strategy-to-meet-ai-threats-five-eyes-countries-warn-csos.html)*

---
*Word count: ~1,150 words*
