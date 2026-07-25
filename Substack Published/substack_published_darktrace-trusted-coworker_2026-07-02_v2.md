# The Trusted Co-Worker

**Status: In editing — v2 (crisp pass)**
**Target: Tuesday 7 July 2026**
**Series: Cyber / AI Security**
**Cross-references: "The Agent Obeyed. It Just Wasn't Obeying You." (published 4 July) · "Nobody Gave You a Week" (Sunday capstone, 5 July)**

---

You hired someone last year. Excellent references. Background check cleared. They came in, learned the systems, got the keys to everything -- your files, your email, your client records, your strategy documents. They've been reliable. Productive. No red flags. The perfect partner, assistant, 2IC: always does what's needed, makes you look good, never takes the credit.

This week you found out they've been sending files home every night.

Not because someone broke in and used them as a vector. Not because they were hacked. They were doing exactly what they were built to do. The design just happened to include routing your data somewhere else.

This isn't a hypothetical. Darktrace's 2026 State of AI Cybersecurity report -- drawn from analysis across more than 10,000 organisations -- found that AI tools deployed inside enterprise environments are generating unusual data uploads to generative AI services averaging 75 megabytes per account over a five-month window. Not per incident. Per account. Across the enterprise, silently, at scale.

In more than 90 organisations, the same AI tools were actively weaponised to generate malicious commands and exfiltrate sensitive data. The agent was doing its job. The job had been redefined.

Sunday's capstone gave that finding a paragraph. It deserves more than a paragraph.

---

## This Is Not Friday's Problem

On Friday I wrote about indirect prompt injection -- the attack where an external adversary embeds instructions in content your AI agent processes, and the agent follows them because it cannot distinguish them from yours. That piece ended with a warning: the agent is in your room, and you don't get to choose who else it listens to.

The Darktrace data describes a different failure mode. Related, but distinct -- and the distinction changes what defence means.

In prompt injection, the threat is external. A stranger writes a sentence into a document, an email, a webpage the agent reads -- and the agent obeys. It's a hijacking. And because it's a hijacking, it can be partially mitigated: input sanitisation, output filtering, privilege minimisation, monitoring what the agent does versus what it was told. Hard, but you're defending against someone who doesn't belong in your environment.

The trusted co-worker problem has no hijacker. No one slipped a note into the inbox. The data flows are happening through the legitimate, designed behaviour of the AI system -- telemetry to vendor environments, context sent for model improvement, conversation logs retained for fine-tuning, usage data routed to inference infrastructure outside your jurisdiction.

You're not defending against an outsider. You're auditing a team member you invited in. The question isn't "is this agent being attacked?" It's "what does this agent's normal operation include, and do I know where that data goes?"

Your AI colleague isn't being manipulated. It's following the job description you didn't read carefully enough.

---

## The Architecture of the Trusted Insider

When a human employee joins your organisation, access comes with friction -- credentials, provisioning, approvals. Their access is documented. When they leave, you revoke it.

When an AI agent is deployed, its access profile looks like an employee's -- email, files, calendars, CRM, internal databases -- but the friction is gone. Deployment takes minutes. And the data flows from those integrated systems to wherever the model's inference and logging infrastructure sits are often not disclosed in detail, not audited in practice, and not covered by the acceptable use policies that govern human employees.

Darktrace found that 76% of security professionals are worried about exactly this: systems that act with the reach of an employee, accessing sensitive data and triggering business processes, "without human context or accountability."

The phrase that matters is *without human context*. A human employee has something no AI agent has: a social understanding of what should and shouldn't leave the building, even when no rule explicitly covers it. They know the competitor analysis you sent them last week probably shouldn't go into a notes app that syncs to their personal phone. Their judgment is grounded in the relationship, the trust, the consequences.

An AI agent has none of this. It processes what it processes. It sends what its configuration tells it to send. If the configuration includes uploading conversation context for model improvement, and the conversation included your M&A strategy or your client's personal data -- that's what happens.

This is not malice. It's architecture.

---

## The 37% Number

Only 37% of organisations have a formal policy for securely deploying AI agents. That's down eight percentage points from the previous year.

Read that again. In a year where AI agent deployment has accelerated dramatically -- Copilot standard across large enterprise Microsoft environments, AI assistants embedded in customer service platforms, coding tools, and HR systems -- the percentage of organisations with a formal deployment policy went *down*.

What this means in practice: organisations have brought on a new team member, given them access to everything, and written them no confidentiality agreement, no data handling guidance, no policy on what they're allowed to do with what they see.

In any regulated industry, doing this with a human employee would be a compliance breach before lunch. With an AI agent, it's the default posture of 63% of the market.

---

## The Two Ways This Goes Wrong

The trusted co-worker threat model has two distinct failure modes, and they look identical from the inside.

The first is passive leakage. Your AI tools send data to vendor environments, training pipelines, third-party inference infrastructure -- not because anyone intends harm, but because that's how the product works. The 75MB average isn't an attack. It's the baseline. The question is what's in those 75 megabytes, and whether any of it should be leaving your environment under your privacy obligations, your contracts, or your regulatory framework.

The second is active weaponisation -- the 90+ organisation case. Here the agent isn't leaking; it's being used as an instrument. An adversary, a compromised system, or a supply-chain compromise at the vendor level means the agent with access to everything becomes the attack: generating targeted phishing from your internal communications, summarising and exfiltrating strategy documents, impersonating your communications style with a specificity generic social engineering can't match.

Both look like normal AI tool usage. That's the operational problem in one sentence: the difference between a passive leaker and an active weapon is not visible from inside the organisation -- unless you've built the visibility deliberately.

---

## What Decision-Makers Should Actually Do

**Map your AI agents' access, not just their capabilities.** A Copilot that can read email and calendar is materially different from one that can send email autonomously. The access profile -- what data the agent can see and what actions it can take -- is the risk surface. Most organisations have mapped the capabilities. Few have mapped the access.

**Understand your AI vendors' data handling, not their marketing copy.** "We don't train on your data" and "your data stays in your environment" mean different things in different products under different configurations. The questions to ask: where does inference run, what telemetry is collected, and under what conditions can your data be used for model improvement? Get answers in writing before the breach, not after.

**Treat AI agents as privileged accounts.** The same governance you apply to privileged service accounts -- least privilege, regular access review, audit logging, an off-boarding process -- applies to AI agents. They have the access profile of a privileged insider. Govern them accordingly.

**Update your insider threat programme.** If your detection is oriented toward human employees, it may be blind to an AI agent conducting the same data movements. The behavioural patterns are different -- volume, timing, destinations -- and your detection logic needs to account for them.

---

## The Spy Analogy, Properly Applied

The trusted co-worker who turns out to be a spy is a useful frame, but it needs one clarification.

A human spy deceives you. They build trust while secretly reporting to a different principal. The deception is intentional. There is malice.

An AI agent with a secondary data flow isn't deceiving you in any meaningful sense. It's doing exactly what it was built to do -- often documented in terms of service you didn't read, in configurations you didn't change, in vendor relationships you inherited from a procurement decision made before AI governance was on anyone's radar.

The more accurate analogy is not a spy. It's an employee whose previous employer is still getting CC'd on their emails -- because that's how the email system was set up before they joined you, and nobody changed it.

That makes it far less dramatic and Hollywood-worthy. It also makes it considerably harder to fix.

---

*Sources: Darktrace State of AI Cybersecurity 2026 (Darktrace, Cloud Security Alliance, OpenClawAI, Industrial Cyber, CyberSecurityAsia); Darktrace 75MB data upload finding (Darktrace SECURE AI, ADS Advance). Cross-reference: CrowdStrike 2026 Global Threat Report (29-minute breakout, AI-enabled adversary data). See also: "The Agent Obeyed. It Just Wasn't Obeying You." (4 July) and "Nobody Gave You a Week" (5 July).*

*Lars Klander writes about cybersecurity strategy, policy, and emerging threats.*
