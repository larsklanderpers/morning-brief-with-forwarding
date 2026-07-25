# The Contractor Who Finished the Job and Kept the Keys

**Status: Draft — v2**
**Target: Wednesday 8 July 2026**
**Series: Cyber / AI Security — Machine Identity (new thread)**
**Cross-references: "The Trusted Co-Worker" (7 July) · "The Agent Obeyed. It Just Wasn't Obeying You." (4 July)**

<!-- THREAD NOTE: This seeds a new thread — "Machine Identity / Ungoverned Agents." Trusted Co-Worker asked what the agent does with its access. This piece asks a narrower, uglier question: who is tracking that the access exists at all, and who turns it off? Rotation is clean — Mon was regulatory (KYC), Tue was AI attack surface (Trusted Co-Worker), this opens fresh ground. -->

---

Every access badge in your building belongs to someone. Someone who was hired, who has a manager, who has a last day.

Except for the ones that don't. A service account stood up in a rush, its keys logged nowhere. A process shuttling data between two systems, wired together by someone a decade ago -- or last month -- that no one else knows exists, whose only inventory lived in that person's head and walked out the door when they left, or just got buried in the crush of *their* day to day.

And now, in the age of agentic AI, it isn't just a handful of API keys you can resolve with a quarterly token rotation, or accounts you can centrally force to reset; you now have thousands of agents that do work as individuals, and log that work as such, but that have no last day -- and only ever lose their connection when something more modern replaces them. And often, not even then.

---

Think about what happens when you hire a person. It is deliberately full of friction. A requisition. A manager who owns the decision. A start date. Credentials provisioned against an identity that lives in an HR system. A record that says this human exists, reports to that human, and has access to these things for this reason. And -- the part that matters most and gets the least attention -- a last day. When they leave, a process fires. Access is revoked. The badge stops working. The story has an ending.

Now think about what happens when you deploy an AI agent. Someone connects it to your email, your files, your CRM, your ticketing system. It gets an API key, or a service credential, or an OAuth grant with the reach of a senior employee. And then... nothing. No requisition. No manager of record. No start date anyone logged. No HR system that knows it exists. And critically, no last day -- because nobody defined when the project ends, and no process exists to revoke what was never formally granted. There is no subway station where good agents go to be retired. 

This week's brief surfaced a piece of analysis that names the gap precisely: identity lifecycle management -- the discipline that governs joiners, movers, and leavers -- was built entirely around humans. Humans with employment records, managers, and departure dates. AI agents have none of those attributes, yet they are being provisioned with credentials, keys, and access rights at a pace no offboarding process was ever designed to match.

Read that again. The tooling that is supposed to answer "who has access to what, and should they?" is structurally blind to the fastest-growing category of things that have access.

---

## The Problem Isn't New. The Scale Is.

Machine identities are not a 2026 invention. Service accounts, API keys, and system-to-system credentials have outnumbered human accounts in most enterprises for years -- by common industry estimates, dozens of machine identities for every human one. Security teams have quietly tolerated this because most of those identities were dumb. A service account that moves a file from A to B every night is a narrow, predictable thing. You can reason about it.

Even in a small business like mine, machine identities run to double or triple the human ones. Add the machine identities in installed locations and the number soars -- probably twenty times the human count, large enough that we run a dedicated customer identity management system purpose-built to garden them. In large enterprises, especially AI-forward ones, I'd argue the ratio is closer to 50 to one, or higher. And the real danger is that today, more and more people are building their own agents and propagating those identities -- where in the past, identity creation was deliberately limited to a handful of people, even in very large enterprises, precisely to guard against this outcome.

An AI agent is not that. The whole point of agent identities is that they are *not* dumb -- and to do the job well, an agent often needs not just a substantial set of identities but cross-platform, cross-environmental ones that aren't intuitively obvious for the "HR onboarding" bot. An AI agent holds one or more machine identities -- an orchestrator can hold many, so it can spawn an as-needed activity agent on the fly -- each with judgment, reach, and initiative. It reads across systems, decides what to do, and acts, with the access profile of a privileged insider and the governance profile of a forgotten cron job. *We took the least-governed identity category in the enterprise and handed it the broadest access.* That is the whole problem in one sentence. And in most cases we did it in under twenty-four months -- a window in which the enterprise, historically, was still choosing which tool to manage identity with. Yet again, the decision clock is compressed.

Tuesday's piece looked at what an agent does with that access -- the data that flows out through legitimate, designed behaviour. This is the layer underneath that. Before you can ask what the agent does, you have to be able to answer a more basic question: do you have a list of them at all? For most organisations right now, the honest answer is no.

---

## Joiner, Mover, Leaver — And Why Agents Break All Three

The identity governance discipline rests on three events. Agents quietly break every one of them.

**The joiner.** A human joins and provisioning is an event -- documented, approved, attributable. An agent "joins" when a developer wires an integration on a Tuesday afternoon, or when a SaaS vendor ships an AI feature that quietly inherits the permissions of the account it runs under. There is no requisition, often no security review, and frequently no record that a new privileged actor now exists in your environment.

**The mover.** When a human changes roles, their access is supposed to change with them -- you add what the new job needs and, in theory, strip what the old one did. Agents accrete. A pilot integration gets extended, then reused for a second use case, then a third, each one adding scope. Nobody ever runs the "does it still need this?" review, because there is no role change to trigger one. The access only ever grows.

**The leaver.** This is the dangerous one. A human leaves and a process revokes their access -- imperfectly, but it fires. An agent's project ends and nothing fires at all. The credential lives on. The OAuth grant stays valid. The API key keeps working. Six months later you have a live, privileged identity, connected to your most sensitive systems, that no current employee remembers creating and no owner is accountable for. That is not a hypothetical risk. That is a standing one, accumulating in every environment that has deployed agents faster than it has governed them.

The contractor finished the job in March. It is July. The keys still work. And there is no one whose job it is to notice.

---

## Why Your Existing Tools Don't Catch This

The reasonable objection is: we have identity governance tooling. We have IGA, we have PAM, we have access reviews. Why doesn't that cover it?

Because those tools were architected around the human record. An access review asks a manager to certify that their reports still need their access. An agent has no manager to ask. A joiner-mover-leaver workflow keys off an HR feed. An agent is not in the HR feed. Privileged access management vaults human-adjacent credentials and rotates them on a schedule -- but an agent's OAuth token, granted through a self-service integration flow, may never touch the vault at all.

The gap is not that the tools are bad. It is that they answer a question -- "do this organisation's *people* have appropriate access?" -- that no longer covers the majority of the actors in the environment. You can run a flawless access certification campaign and still have thousands of ungoverned agent identities, because the campaign was never designed to see them.

This is the same pattern the last two pieces kept hitting: the control was built for a world where the actor was human, and the actor is no longer human.

---

## What Decision-Makers Should Actually Do

**Build the inventory before you build the policy.** You cannot govern what you cannot see. The first move is not a new tool or a new framework -- it is an honest census of every AI agent, integration, and non-human identity that holds access to a sensitive system, and who owns each one. Most organisations discover in this exercise that the number is far larger than anyone believed, and that a meaningful fraction have no owner at all. That discovery is the point.

**Give every agent an owner and an expiry.** The single most effective governance control is boring: every agent identity gets a named human owner and a review date, and no agent identity is created without both. An owner is someone accountable for whether the access is still needed. An expiry forces the leaver event that agents otherwise never trigger. If the project is still live at the review date, renew it deliberately. If nobody will own it, that is your answer.

**Treat agent credentials as privileged, and vault them accordingly.** An OAuth grant that can read every mailbox in the tenant is a privileged credential whether or not your PAM tool currently knows about it. Bring agent credentials into the same rotation, logging, and least-privilege regime you apply to human privileged accounts -- because their access profile is identical and their oversight, right now, is not.

**Make "who created this, and why" answerable.** Provisioning an agent should leave a record the way hiring a person does: what it is, what it can reach, who requested it, and what business reason justified the scope. This is not bureaucracy for its own sake. It is the difference between an environment you can reason about and a drawer full of keys that open doors you have forgotten you have.

---

## The Ghost on the Payroll

There is an old audit nightmare that predates all of this: the ghost employee. A name on the payroll that no longer corresponds to a person -- someone who left, whose record was never closed, whose salary keeps going out the door to an account nobody is watching. Auditors hunt for ghost employees because they are where fraud hides, and because their existence proves the offboarding process is broken.

The ungoverned agent is the security version of the ghost employee. It is an identity on the books that no current person owns, with access that no current process reviews, doing work that no manager signed off on. The difference is that a ghost employee just draws a salary. A ghost agent can read your email.

The uncomfortable question to sit with is not "are our agents secure?" It is simpler and worse: if I asked you today for a complete list of every AI agent with access to a sensitive system in your environment, *and who owns each one* -- could you produce it? And if you cannot produce the list, what exactly do you think you are governing?

---

*Sources: "Identity Lifecycle Management Wasn't Built for AI Agents" (The Hacker News, 3 July 2026); non-human identity ratio estimates drawn from industry NHI reporting and the author's own environment. Cross-reference: "The Trusted Co-Worker" (7 July) and "The Agent Obeyed. It Just Wasn't Obeying You." (4 July).*

*Lars Klander writes about cybersecurity strategy, policy, and emerging threats.*
