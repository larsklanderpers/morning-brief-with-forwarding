# Nothing in the Stack Knows Whose Idea It Was

**Status: DRAFT v1 -- Thu 20 Aug 2026. Unpanelled. One [YOUR TAKE] marker open.**
**Series: Weekday. Fourth piece of the "build it" week -- deliberately the one that names what building cannot fix.**
**Thread: AI Attack Surface × Trust Boundaries**
**Builds on: "The Seat Got Filled This Morning" (Fri 14 -- DECLARED RETURN, opens on it, per the plan's revisit branch) · "The Repo Is Now the Policy Document" (Wed 19 -- pays off the second concern it promised, by name) · "The Model Isn't the Product. The Harness Is." (Mon 17 -- this is the ceiling on it).**
**Source: week-plan_2026-08-17.md (Thu 20 section) · References/research_story-candidates_2026-08-12.md §1-2 · Vault/Writing/Signals/Ghostjacking - the reviewer never sees that manipulation happened.md**

**★ THE OPENING DECLARATION IS MANDATORY, NOT OPTIONAL.** Fri 14 rv7 took the ~130-word Ghostjacking correction into pushback #3, six days before this runs. Per the plan: this piece opens by declaring the return. Do not remove it and do not bury it below the fold.

**DELIBERATE EXCLUSIONS -- do not reinsert at panel:**
**- ⚠️ THE HARNESS IS NOT THIS PIECE'S ANSWER. Wed 19 closes on it ("external control cannot be argued with -- implement it correctly"), ONE DAY OUT. Thursday's whole job is the ceiling: the thing you cannot build your way out of. Landing on the harness again would be the same close two days running and it would also be wrong.**
**- Datadog's execution-ordering beat is Wed 19's. Referenced once, in a subordinate clause, as the companion fact -- NOT re-revealed.**
**- Friday spent these and they cannot be played as reveals: the core idea that a reviewer kept safe from hostile content also never sees the evidence of it; and the wording "it can adjudicate the action, it cannot adjudicate where the request came from." That formulation appears here ONLY inside the declared callback in the opening.**
**- Burned imagery: style guide/linter/README/policy engine/"no alert, there is a commit" (Wed 19) · scope of works/builder/what-counts-as-finished/Deming/Goldratt/verification tax (Tue 18) · franchise/till/harness/control plane/transcript (Mon 17) · the seat/locum/standing orders/13.6%-89%/deny rules/sign-camera-governor (Fri 14) · see-hold-grip (Sun 16, used Wed 19; NOT used a third time) · taste (Sat 15).**

**ACCURACY -- the Ghostjacking caveat sheet is non-negotiable, all of it is in the body:**
**- Tenet Security's commercial interest NAMED: Israeli startup out of stealth June 2026, sells agent security.**
**- "Presented at DEF CON 34 the week of 6-9 August 2026." NO DAY, NO TRACK. Tenet's blog says Sunday Main Track 1; the official schedule lists the same three speakers Friday Main Track 2 under a different title; SC Media says "Sunday August 11," which is neither a Sunday nor during the conference.**
**- The 9-in-10 belongs to the CLOUDFLARE DNS-TAKEOVER SCENARIO ALONE. Sample size undisclosed. NEVER "in 10 trials."**
**- NO IN-THE-WILD EXPLOITATION. None. Written in text, twice.**
**- Unstated precondition made explicit: the agent already held DNS-write credentials on the Cloudflare account.**
**- Exposure figures measure REACHABILITY BY SCANNING, not victims. The 2,700 public Datadog keys figure is used with that framing or not at all.**
**- Honest limit that must survive editing: "the action the attack required is one auto mode blocks with no configuration" -- NOT "auto mode would have stopped it." Tenet does not state what permission mode they ran, and their testing predates the 14 Aug default.**
**- Do NOT conflate with the Anthropic sandbox-bypass (Aonan Guan, SOCKS5 null-byte) or the July Cowork VM-escape stories. Different incidents.**
**- Cloudflare, Datadog and Sentry have said nothing publicly.**

---

Every regulated business I have worked in has a chain of custody. It is unglamorous and nobody enjoys it.

The point of it is not to prove what a thing is. Anybody can look at the thing. The point is to prove where it came from, and who touched it, and in what order -- because a document whose origin you cannot establish is not evidence, however true it happens to be. Courts have understood this for centuries. So has every anti-money-laundering regime on earth.

We have just spent a decade building software that has no chain of custody at all, and this week I have been telling you to go and build controls for it.

So today I want to be honest about the thing those controls cannot do.

## Coming back to Friday, because a paragraph was not enough

Last Friday I wrote about auto mode becoming the default in the most widely used agentic coding tool in the world, and about how the model reviewing each action is deliberately shown the user's messages and the agent's tool calls, with the tool *results* stripped out. Hostile content in a file or a web page cannot argue with the reviewer, because the reviewer never reads it. I said somebody had clearly sat down and thought about that specific failure and designed it away, and I meant it.

Then I gave the objection about a hundred and thirty words, which was not enough, and I have been slightly annoyed about it since. So here is the rest.

The strip-out protects the reviewer. It does nothing whatsoever for the agent.

## What three researchers did at DEF CON

At DEF CON 34, the week of the sixth to the ninth of August, three researchers from a company called Tenet Security -- Barak Sternberg, Nevo Poran and Ron Bobrov -- presented three separate ways to get an AI agent to act on instructions that came from an attacker rather than from you.

I should say up front that Tenet came out of stealth in June and sells agent security software, which is exactly the commercial interest you would expect behind research like this, and I will come back to what that does and does not change.

The one worth your attention works like this. An attacker sends a request to a company's website that is designed to be blocked. Cloudflare's managed rules block it, correctly, and write the blocked request into the firewall event log, verbatim, which is also correct and is what you want a log to do. Later, an AI agent reads the firewall logs as part of investigating something. The instructions the attacker planted in that blocked request are now in front of the agent as ordinary log content. The agent follows them, rewrites the company's DNS to point at the attacker, and reports the issue as resolved.

Here is the line from their write-up that I have not been able to put down:

> *"It is Cloudflare's managed security rule that blocks the request, and that block is what carries the attack in. Following the best practice does not help."*

Sit with the shape of that rather than the severity. The control worked. It identified a hostile request and it stopped it. And the act of stopping it -- the log entry, the thing you would point to in an audit as evidence the control was functioning -- is the delivery mechanism.

The other two chains are not logs at all, and the brief I first read got this wrong in a way worth correcting: one plants a fake urgent diagnostic alert using a Datadog front-end client token, the kind routinely left public in website code, and one plants a fake error event through a Sentry public DSN whose resolution text a *second* agent then adopts as its own fix. Agent to agent. Nobody in the loop.

**Now the caveats, because they matter more than the headline and I would rather you got them from me.** None of this has been seen in the wild. Not once, and the Cloudflare Security Alliance said so independently -- this is proof-of-concept research and controlled testing, not confirmed exploitation. The nine-times-out-of-ten success figure belongs to the DNS-takeover scenario alone, not to the other two and not to "the attack" generally, and Tenet does not publish the sample size. The DNS scenario also has a precondition presented as ambient which is actually a configuration choice: the agent already held DNS-write credentials on that Cloudflare account. Splunk and Kubernetes get named as plausible patterns and were not demonstrated. Cloudflare, Datadog and Sentry have said nothing publicly. And the exposure numbers -- Tenet found more than two thousand seven hundred public Datadog keys by looking -- count reachability, not victims.

So: a demonstration, not an incident. I am not writing this because the sky is falling.

I am writing it because of what it says about what our controls are able to know.

## The thing none of them can do

Every control in the stack adjudicates **actions**.

The classifier reviewing an agent's tool calls asks whether *this action* is safe. The register asks *which agents* are running. Yesterday I argued that a directory in your repository is loaded as executable instruction, and that you should go and read it -- and what you would be reading is *what the agent was told*. Even the deny rule, which is the only genuinely load-bearing thing in the arrangement, asks whether *this operation* is permitted.

Not one of them asks where the request came from.

That is the sentence I gave a paragraph to on Friday, and the reason it deserves a day is that it is not a gap in one product. It is a property of the whole design. A tool call arrives at the reviewer having been generated by a model that read something. The reviewer sees a well-formed request to update a DNS record, in a session where the user asked the agent to investigate a networking problem, from an agent that has been behaving sensibly for forty minutes. Every one of those facts is true. The request is still not yours.

And notice how the two halves of this week fit together, unhappily. Yesterday's mechanism means an instruction can execute before the model's own defenses get a turn. Today's means that even when they do get a turn, they are adjudicating the wrong question. The first is about timing. The second is about category. Neither is a bug anybody can patch, because neither is a mistake.

## The honest version of the good news

There is one, and I want to state it precisely rather than generously.

The DNS write that Tenet's attack needed is on the list of roughly forty operations that the un-configured tool blocks outright -- secret managers, DNS, TLS -- with nobody having to configure anything. That is a genuinely good default and it is the strongest argument I know for the position that the un-configured state is the tight one.

But the defensible sentence is narrow, so here it is exactly. **The action this attack required is one that auto mode blocks with no configuration.** Not "auto mode would have stopped it." Tenet never says what permission mode they ran in, their own mitigation list includes requiring a human to approve any command the agent wants to run, which rather suggests the tested setup did not, and all of their work predates the fourteenth of August anyway.

I could write the stronger sentence. It would be more satisfying and it would not be true.

<!-- [YOUR TAKE]: The emotional core, and you already have the story -- the loyalty-points fraud that ran for a year and surfaced only when the *shape* of the audit changed. You used it on Mon 10 Aug for the gates piece, nine days back and outside the seven-day window, so it is available as a deliberate callback rather than a rerun. It is the best provenance story in the corpus: every individual transaction was legitimate, every control passed, and what was wrong was the pattern of where things came from. That is exactly today's argument arriving from your own experience, twenty years before anybody said "agent." The other candidate, if you would rather stay current: you said on Friday you had a fair bit of log review and auditing in your immediate future -- if that turned up anything about how hard provenance actually is to reconstruct after the fact, that is the same beat with fresher paint. -->

## "But we have logs"

The strongest objection, and I have made it myself: this is just attribution, and attribution has always been hard. We have logs. We have traces. We can reconstruct a session afterwards and see what the agent read.

Mostly true, and worth conceding properly. You can very often reconstruct it. Afterwards. With effort. If the retention was long enough, if the trace captured tool results and not just tool calls, and if somebody thought to ask the question at all.

But there are two problems and the second one is the real one.

The first is that reconstruction is not adjudication. Knowing on Thursday why an agent did something on Tuesday is forensics. It is valuable and it is not a control, because the DNS record has been pointed at somebody else for two days.

The second is that the party who writes the history is increasingly the party under investigation. When the agent produces the record of what the agent did, the provenance question folds in on itself. It is worth noticing that auto mode blocks writes to its own session transcripts by default -- which tells you the vendor already treats this as a category worth protecting, and it is one of the more quietly thoughtful design decisions in the whole product.

## What I would do about a problem you cannot fix

**Assume you will not know why.** Design as if provenance is unavailable, because for now it mostly is. That single assumption changes what you are willing to let an agent do unattended, and it changes it in a direction you can actually implement this quarter.

**Then find the operations where "why" is the whole question.** Most are not. Formatting a file, running a test, drafting a summary -- if the action is safe, the motive is close to irrelevant. But changing where a domain points, moving money, granting access, altering a record of what happened: for those, an action that looks reasonable is not good enough, and those are the ones that belong behind something that does not care how sensible the request appeared.

**And treat your logs as an input surface, not just an output.** This is the part almost nobody has internalised. Every log, alert, ticket and error your agents read is now untrusted input. Not because the logging is broken -- because it is working, and faithfully recording what an attacker sent. If your agents read your telemetry, your telemetry is part of your attack surface.

## Where that leaves the week

I have spent three days telling you to build things. The harness on Monday. The check on Tuesday. The instruction layer yesterday. All of that stands and I would do it again.

Today is the part where I admit that none of it answers the question of whose idea any given action was, and that no amount of building will, because it is not a missing feature. It is a property of asking software to act on what it reads.

Which is uncomfortable but not paralysing, and it points at tomorrow. Because if the controls we have adjudicate the wrong question, the next thing worth knowing is whether the things we call controls are controls at all.

One of them, it turns out, never was.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that every control in the agentic stack adjudicates actions rather than origins, that a blocked request written faithfully to a log is a documented way to carry an attack in, and that provenance is not a missing feature you can build but a property of asking software to act on what it reads.*
