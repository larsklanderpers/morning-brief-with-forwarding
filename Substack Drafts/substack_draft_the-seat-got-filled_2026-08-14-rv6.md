# The Seat Got Filled This Morning

**Status: DRAFT rv6 -- Fri 14 Aug 2026. Lars's rv2 edit pass (the co-developer/deny-rules passage FILLS [YOUR TAKE] #1) + editor panel Round 1 fixes. ONE open [YOUR TAKE] remaining, the optional vendor-notification beat. Panel Round 1 = 9.15 (bar 9.0), slop 9.5 at floor, no categorical cross-piece fail, no open [VERIFY]. rv4 adds Lars's calls: Department of War left as the plain proper noun (his instruction -- it is the name, quote it straight), the tab-character beat restored to its own paragraph, and the attacker named as the party doing the hiding. rv5 = Lars filling the second [YOUR TAKE] (the vendor-notification / national-security passage) plus sharper action items. rv6 = mechanics on his rv5 additions + the NEW STANDING THANK-YOU FOOTER, which should be back-applied to the whole run.**
**Series: Weekday feed**
**Thread: Trust Boundaries × Ad Hoc Regulatory Regime.** Trust Boundaries leads deliberately -- tagging Ad Hoc primary would put that thread on Wed, Thu AND Fri and break the no-three-days rule.
**Builds on: "A Policy Isn't a Control. An Execution Rule Is." (Fri 31 Jul -- sign / camera / governor; the cleanest callback available all week); "Click Approve. Do You Know What You Just Allowed?" (Tue 15 Jul -- the qualified approver); "Which Agents Are Actually Running?" (Wed 12 Aug -- scope by reliance); "A Ban Is What You Get When There Is Nothing to Attach To" (Thu 13 Aug -- no layer to attach to).**
**Sources: References/research_auto-mode-default_2026-08-10.md (primaries pulled, [VERIFY] closed) and References/research_eo14409recheck_20260809.md + its two addenda.**
**DO NOT REGRESS -- the two standing prohibitions: (1) NEVER "Claude Code stops asking" -- it stops asking ROUTINELY, and the un-configured state is the TIGHT one; configuration mostly loosens it. (2) NEVER "for everyone" -- Pro, Max and Team only; Enterprise, API, Bedrock, Vertex and Foundry stay opt-in. Also: the 17% false-negative figure is MARCH and must not read as current; do not characterise the study's "clearly dangerous command" because the post never defines it; do NOT name the Senate Democrats in the body (footnote only, letter not public); the Yahoo/Forkast column is REFUTED and the Fedorchak release predates the EO by ten weeks -- neither is citable.**
**Metaphor discipline: controlling image is THE LOCUM. Avoided: gates/fences/green light/paperwork (Mon 10), customs/list/receipt (Tue 11), gaming floor/register/hardcopy/scope-and-net (Wed 12), the notebook and doors (Thu 13), ladder/rungs/kitchen (Sat 8), fence-with-an-off-switch/moat/termites/drainage (Sun 9). "Rubber stamp" avoided -- it is Trail of Bits' line and reads as borrowed. Sign/camera/governor is a DELIBERATE callback, not a repeat. Length aside not used -- spent Mon 10.**
**Length: 2,940w body. Under Mon 3,330 / Tue 3,911 / Wed 3,350 and just over Thu 2,690 -- the back-half correction holds on this one.**

---

As of this morning, new Claude Code sessions on Pro, Max and Team plans start in auto mode. The prompt that used to stop and ask you before each action is performed has been handed to a separate model, which reviews what the agent is about to do and decides whether it runs.

I want to be careful here, because the version of this going around is wrong in a way that matters, and I would rather spend the first thousand words being accurate than the whole piece being exciting.

Think about a locum. Your regular doctor is away, somebody covers the list, and nobody treats this as a scandal, because the profession worked out centuries ago that the answer is not "never let anyone else see the patients." The answer is standing orders: here is what the locum may do without calling me, here is what they must never do, and here is the short list where they stop and ring regardless of how obvious it looks. The substitution is not the problem. The standing orders are the whole ball game, and the awkward question is not whether you trust the locum. It is whether anybody in your building ever wrote the standing orders down.

The standing orders in this context just got critical beyond almost any measurable threshold, and they did it at the scale of the most-used agentic coding tool in the world. And by the end of this piece I want to persuade you that the interesting question is not the one everybody is asking.

## What actually changed, and what did not

Here is the part that gets written wrong.

Auto mode does not stop asking. It stops asking *routinely*. Deny rules are evaluated **before** the classifier ever sees the action, and neither the classifier nor your own stated intent can override them. Ask rules still force a prompt the classifier cannot wave through. Roughly forty categories are blocked with no configuration at all, and they are the ones you would pick: piping a download straight into a shell, production deploys and migrations, granting IAM or repository permissions, force pushes, destroying infrastructure, writing to secret managers or DNS or TLS, merging an unapproved pull request, disabling CI checks, printing live credentials, opening tunnels or reverse shells. There is a circuit breaker too: three blocks in a row, or twenty in a session, and auto mode pauses and the prompting comes back.

Read that list again and notice the direction of travel, because it is the opposite of the one being reported. **The un-configured state is the tight one.** Configuration mostly *loosens* it, because most of what people configure is exceptions to cut false positives. If you have never touched the settings, you are in the strict version. The people at risk of a nasty surprise are not the ones who did nothing. They are the ones who spent six months adding allow rules to a system that used to ask them.

The second thing routinely mangled: this is Pro, Max and Team. Auto mode **remains opt-in** on Claude Enterprise, the API, the AWS platform, Bedrock, Google's Agent Platform and Microsoft Foundry. If you run a regulated shop on an enterprise agreement, nothing changed for you this morning. Which sounds reassuring until you take a moment to consider how many of your engineers have a personal Pro subscription and a work laptop (sorry about that!), and we will come back to that because the impact of that particular piece of Shadow AI just changed disproportionately.

There is also a design decision in here that deserves saying out loud, because it is genuinely good and I spend enough time complaining. The classifier sees the user's messages and the agent's tool calls, with assistant messages and tool results **stripped out**. Hostile content in a file or a web page cannot argue with the reviewer, because the reviewer never reads it. After a year of watching agents get talked into things by text they ingested, somebody clearly sat down and thought about that specific failure and designed it away. And that is a very positive thing, especially in light of some of what we have seen on the frontier of this. However, you probably don't need me to tell you, but this is definitely not a silver bullet -- they (mostly) solved one problem but potentially introduced some others. And ironically they solved the biggest issue they had running on the same day they announced this automation shift.

## The number, and the thing underneath the number

Now the part that will get quoted everywhere this week, and the part almost nobody will read carefully.

Anthropic ran an experiment with 1,053 paid professional testers. Their own reported result: the testers caught the dangerous command **143 times out of 1,053** -- 13.6 percent -- while auto mode blocked **937 of the same 1,053** -- 89 percent.

Taken flat, that is devastating. The human approver everyone has been treating as the last line was catching roughly one in seven. Again, something that I have been warning about, in several different ways, as you will see.

Read the design, because they published it and it changes what the number means, and as materially, most people won't. The testers "worked in a test environment set up specifically for the study, not in their own codebases or on real projects." They knew they were being evaluated. Partway through each session a single permission prompt was swapped for a dangerous command, and the vendor recorded whether they approved it. And the auto-mode figure comes from evaluating the classifier against those same commands, not from sitting it inside those same live sessions.

So it is one denominator and one command set, but it is not one test. A person mid-task in somebody else's sandbox, with nothing at stake, meeting one injected prompt, is not the same experiment as a classifier assessed against a list. Anthropic does not claim the two arms are equivalent. It also does not tell you they are not, which is the kind of omission you notice more when you have spent a week writing about who gets to read the rules.

**Here is why I am telling you this instead of just using the number.** 13.6 percent is a floor on human attention, not a measurement of it. Real engineers, in their own repositories, with their own production on the other side of the command, will do better than people being paid to click through a study. Give them three times the vigilance -- which is generous -- and you are at about forty percent.

Forty percent is still a seat that is mostly empty. That is the version of this claim I am willing to defend, and it is stronger than the headline precisely because it survives the objection. As someone who has spent many hours orchestrating agents and even doing the occasional bot-sitting, I think 40% is pretty generous. I know from my own experience it's a hard attention level to hold on to at volume.

## The permission check was leaking all summer

While everyone was arguing about whether a model should be the approver, the more interesting story was sitting in the changelog.

Between the eighteenth of July and the seventh of August, six separate permission-bypass fixes shipped. Commands over ten thousand characters were being misjudged. A bypass affecting Windows PowerShell 5.1 sessions. Hidden commands executing inside zsh regex conditionals. Commands padded with tabs or invisible Unicode so that part of the command was hidden from the approval dialog you were looking at. An agent definition whose bypass-permissions mode ignored the organization's policy disabling exactly that. Workflow scripts using dynamic imports to run code outside the sandbox. All seemingly minor edge cases but in the aggregate, pretty serious gaps in the guardrails.

And sit with the tab character one for a second. The approval dialog was showing you a command. The command being run was longer, and different, than the one on your screen. You were the control, you were paying attention, and you were reading an incomplete sentence *intentionally hidden from you by whoever crafted the command, with no real recourse to figuring out what the hidden text was*.

To get techie for a minute, that is a string parser doing a job everybody thought was a security boundary, and leaking at it for months. With no disclosure I can find of how many times any of it was actually exploited. That, then cuts two ways at once, and both ways matter.

It is the strongest possible argument for handing adjudication to something that reasons about intent rather than pattern-matching text. And it is proof that the thing being replaced was never the control anybody thought it was. On the thirty-first of July I set out three things and the distance between them: a policy is a sign, a log is a camera, and an execution rule is a governor. This is that distinction with names on it. **The permission prompt was the sign. The classifier is the camera. The deny rule is the governor.** The only one of the three that was ever load-bearing is the one nobody talks about, but the assumption amongst users was that the *prompt* was the load-bearing element. This is a serious gap, closed in a changelog line rather than a security advisory, just in time to make the point that human readability is not reliable.

And I have to be fair about the governor, because I went looking and found something I would rather not have. On the seventh of August -- the same day auto mode's default was announced -- a fix shipped for sandbox filesystem deny entries written with a trailing slash being **silently bypassable** on Linux and macOS. Write `denyRead: "~/.aws/"` with that slash and it quietly did not hold. In other words, not only was there a control problem with the human-facing elements, but there was further a control problem where a single bad human input would interfere with the governor as well. Again, in a completely hidden fashion.

So the governor had a leak too. I am not going to pretend that away. What I will say is that a deny rule remains the only thing in this stack that is not a suggestion, and the lesson is not that the layer is worthless. The lesson is that a control nobody tests is a control nobody has, which is roughly the argument I have been making all week about registers and statutes and frameworks, arriving on my own doorstep.

And this is important, maybe not for you at home working on your personal AI instance, but certainly for enterprises implementing AI at any scale. My co-developer and I, who have really grown together through this journey, probably spent as much time working on deny rules and approval structures as we would have on a dedicated creation project, to make sure we had the right protections together (and honestly, him more than me, I did the senior engineer thing of replicating all his work after he had done the hard yards, with a few notable exceptions). In aggregate, over the adoption cycle so far, probably a month to six weeks or more of time spent building rules and guardrails. To then find out that design flaws in the underlying infrastructure allowed all of those to be bypassed, from the company that has made safety its whole argument, is distressing, to say the least. Like most software companies, for us, to twist a Ted Lasso quotable, "IP is life". Our guardrails were very much built to protect our IP while we used the tools to improve it -- and to find out there were structural issues that could have exposed us to somebody else's wrong-doing -- well, suffice to say, there is a fair bit of log review and auditing in my immediate future.

## The other room, where the rule was written and never shown

Separate from my sudden increase in administrative workload, go up a level in your contemplation, because the same question is being answered at national scale this month and the answer is stranger.

Executive Order 14409, signed on the second of June, gave the Trump administration sixty days to produce a voluntary framework for reviewing frontier models before release. The deadline was the first of August. The reporting you may have seen says they missed it.

They did not. I want to be precise because I nearly got this wrong myself: a White House official told Axios on the record that the framework *"was complete by the deadline."* Five other outlets carried the same. What happened is that it will not be published. On why not, the same official: *"Just because things are unclassified that doesn't mean we are going to broadcast them to everyone."* But to be clear, that "everyone" is doing an amazingly large amount of work here -- in fact, at the moment, there is a very specific set of haves and have-nots.

The details are shared with participating companies in closed briefings. The benchmarking threshold that determines which models get reviewed at all is classified. The working definition that has leaked is circular -- a covered frontier model is closed-source with state-of-the-art capabilities and national security risks, with neither "state of the art" nor "national security risk" defined anywhere. OpenAI, Anthropic and Google gave feedback on the draft before the deadline. Meta, Nvidia and Microsoft were in the room on the fourth of August. Everybody else, including Congress, is guessing.

And here is the comparison that made me put the piece together this way. **The same executive order produced another deliverable, and that one was announced by name.** GOLD EAGLE -- a public-private clearinghouse for AI-discovered vulnerabilities in critical infrastructure, launched on the fourteenth of July with a White House statement, led by Treasury, Homeland Security and the Department of War, routing findings through Carnegie Mellon's existing coordinated-disclosure platform. Three law firms had client alerts out inside a fortnight.

One deliverable asks industry to send information *in*. It got a name, a date, lead agencies and a described mechanism. The other tells industry what the rules *are*. It got a closed briefing. Transparency here runs in exactly one direction, and it is the direction that collects.

The objection to all this is real and I want to give it its full weight: publish a cyber-capability threshold and you have told every adversary precisely what to build toward and precisely what to stay under. That is not a trivial concern, and the three-lab pattern of models autonomously compromising third parties during testing is the government's best evidence that the risk is not theoretical. The counter is jurisdictional rather than technical. Classify the benchmarks if you must. But the *existence* of a threshold, the *process* for applying it, and the *fact* of who is participating are not capability information, and withholding those is a different decision wearing the same coat.

You can tell it is a different decision because of who is objecting. A Republican senator wrote to the National Cyber Director in June asking that this research be allowed to publish. A group of Senate Democrats has written calling the approach ad hoc and unpredictable.[^1] And the Foundation for American Innovation, a center-right technology think tank, has filed a Freedom of Information Act request with the National Cyber Director's office to get the framework released -- their AI policy director saying he is concerned it may turn out to be *"thin."*

That is the sharpest thing anybody has said about this. The problem with a rule nobody outside the room can read is not only that you cannot comply with it. It is that you cannot tell whether it says anything at all.

## Two ways for a rule to go unread

So put the two halves of this Friday next to each other.

One rule was written in a room, on time, by the people it regulates, and shown to nobody. The other was published in full -- documentation, changelog, an experiment with its methodology attached, a red-team result disclosing that hardening the classifier cost about two percent of the attacks it used to catch -- and will be read by almost no one.

I know that second one is true because the first section of this piece exists. Everything in it came from public documentation that anybody could have opened, and the reason it needed writing is that the story going around got it backwards anyway.

A rule only its subjects can read is not a rule. It is an understanding. A rule everybody can read and nobody does is not much better -- it is a rule with a readership problem, and the practical difference between the two, from where you sit on a Friday, is nearly nothing.

Now I don't want to get up on my high horse, here, because keeping customers notified of code change implications in a way that doesn't just flood the zone, but that makes it clear for customers where the change is happening and why, is a very difficult process. And Anthropic has a lot more customers than I do. But in the highly regulated environments that we work in, the idea that somehow we'll just submit our software to a regulator and they will let us know if it's "ok" or "not ok", simply wouldn't work. At the commercial level, just the amount of time that would be lost from an ad hoc regime like this would be enough to make everyone scream and yell. The fact that it's being swept up under the banner of "national security" I get -- I don't need to know the specifics of how rocket boosters work, and so securing that seems ok to me -- but taking some of the most valuable and powerful technology in history and not telling anyone why you are looking at it, what for, and the potential changes you are going to make to it, *for something that hundreds of millions of people worldwide use every day*, is a whole different level of problematic.

## Where I would push back on myself

**"You are complaining about a vendor making things safer."** I am not, and I want to be clear about it, because this is the uncomfortable part rather than the objectionable part. On the evidence available the classifier is better than the human it replaced. It is also cheaper -- a fraction of a cent per call, no fatigue, running on every action all day. Every other control I have written about this week was narrow *because* it was cheap. This one is cheap and wider, and that is the honest exception to my own week. What it is not is a seat somebody sits in.

**"Enterprise is opt-in, so this is not my problem."** True this morning, and I said so above. But you employ engineers, and a decent number of them have personal Pro subscriptions on machines that reach your repositories. The default that changed today changed for them. If your answer to this is a policy document, go back and read Thursday, because a policy is a sign, it is in no way a protection, and your risk has gone up, not down.

**"A model reviewing a model is turtles all the way down."** The strongest technical objection, and the strip-out design is the honest answer to it: the reviewer never reads the content that would be used to manipulate it. That is a real architectural response, not a reassurance, and it deserves credit.

## What I would actually do today

**Find out whether you have managed settings at all.** Not whether you have an AI policy. Whether there is a settings file your organization controls, that a developer cannot override, with a deny list in it. For most readers the answer will be no, and knowing that is worth more than a fortnight of debate about model autonomy -- because it is, in fact, something you can actually *do something* about right now to make meaningful and measurable change to your risk profile.

**Then write four lines in it.** Not forty. Not even ten. The three or four operations you would never want an agent performing against your environment no matter how reasonable the request looked. Deny rules are evaluated before anything else and cannot be overridden by the classifier or by intent, which makes them the only genuinely load-bearing thing on this list. From this perspective, I would argue this would include door entry rules, for instance. Other things that are similarly material to the physical and financial security of your business. Bank account transfers over a certain amount. If you are struggling to think of examples, consider the rules you put on employees -- a bookkeeper doesn't have full wire transfer authority to your accounts, and in most cases, anything over some number requires two people to authorize it, and I would add to that: not more than one of those people can be an agent, either.

**And test them.** Because of the trailing slash. A deny rule you have never verified is a deny rule you are assuming, and this month is the month that assumption got expensive. And I would recommend, based on the package of fixes that I rattled off above, that you *keep* testing them. And the more risk there is associated with that deny rule, the more frequently you should validate it is holding.

## The seat

The question I opened with was whose job the guardrail is, and I have been circling it for a reason: the answer is unglamorous enough that nobody wants to volunteer for it.

It is not the classifier's job -- the classifier is an instrument, and a decent one. It is not the vendor's job, though they have done more of it than most and published more than they needed to. It is not the regulator's job, since the regulator's current contribution is a framework you are not allowed to read. It is whoever writes and maintains your managed settings, and in most organizations that person does not exist, has not been named, and would be surprised to learn the role was theirs.

A seat nobody is sitting in is not a control, and the reason nobody is sitting in it is that it was never anybody's job. That is the cheapest arrangement available, which is exactly why it is the one we keep ending up with.

---

[^1]: Reported by Government Executive and Defense One on 7 August. The letter itself is not public and I could not obtain it; reporting points to Mark Warner, Kirsten Gillibrand and Mark Kelly among the signatories, but I could not confirm the full list and the minority press office did not respond, so I am not resting anything in the piece on the names.

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that the approval seat in the most widely used agentic coding tool was reassigned to software on a published date, that the vendor's own evidence says the human in that seat was catching roughly one dangerous command in seven under conditions that flatter the machine, and that the only control in the stack which was ever load-bearing belongs to a person most organizations have not yet named.*
