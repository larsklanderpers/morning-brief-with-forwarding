# The Model Isn't the Product. The Harness Is.

**Status: DRAFT v1 -- Mon 17 Aug 2026. Unpanelled. Two [YOUR TAKE] markers open.**
**Series: Weekday. Opens the "build it" week promised at the close of Sun 16 Aug.**
**Thread: Trust Boundaries x AI Sovereignty**
**Builds on: "Control You Can Locate" (Wed 5 Aug -- the harness as the wall that holds); "What It Can See, and What It Can Hold" (Sun 16 Aug -- the printed promise this piece pays).**
**Source: week-plan_2026-08-17.md (v2). All Anthropic documentation claims verified at the primaries on 13 Aug 2026 and quoted verbatim in the plan file.**

**DELIBERATE EXCLUSIONS -- do not reinsert at panel:**
**- Deny rules are Fri 14's ("The Seat Got Filled This Morning"): the four-lines ask, the trailing-slash bug, "a control nobody tests is a control nobody has," and sign/camera/governor. Three days out. Mentioned here once, in passing, as a thing already covered. NOT re-argued.**
**- see / hold / grip / sight radius is Sun 16's and is BURNED for today. Not used, not paraphrased.**
**- "window" is reserved through Tue 18. Not used.**
**- Concede-then-sharpen runs once here (the residency section) and once on Sat 22. No third anywhere this week.**

---

You can own the building, buy the equipment, hire every person in it, and still not own the numbers. Anybody who has run a franchise knows this in their bones.

The fryers are yours. The lease is yours. The staff roster is yours and the payroll comes out of your account. And every night the till reports to head office, because that was in the agreement you signed, on a page you skimmed, in a paragraph that was not hiding anything from you at all.

I have been arguing for three weeks that governance is something you build rather than something you receive. On Sunday I said that a guardrail you cannot point at in a system diagram is not a guardrail, and I promised that this week would be the part where we actually build one. So let's start with the thing you build first, and then let's be honest about how much of it is yours.

## The layer that was always the real product

On the fifth of August I wrote that the wall that failed was never inside the model. A model can talk its way around its own instructions. It cannot talk its way around a barrier that lives outside it and holds. The industry has a name for that barrier, and it is the harness -- the tool permissions, the sandbox, the approval that cannot be prompted away, the checks that run on what came back.

I said then that the wall that holds only protects you if you are the one holding it. That was the right sentence and I left half the job undone. I told you the harness was the thing that mattered. I did not tell you what is actually in it, or how much of it you are holding.

So here is the honest version. When people argue about which model to use, they are arguing about the least differentiated part of the stack. Models converge. They get cheaper roughly every quarter, they leapfrog each other on benchmarks nobody outside the labs can reproduce, and by the time your procurement cycle finishes the ranking has changed anyway. The model is the commodity. The harness -- what the thing is allowed to touch, what happens to what it produces, and where all of that is written down -- is the product. It is also the only part you can build.

Which is why it matters enormously what you actually get when you go and take it back.

## So I went and read the terms

Anthropic shipped Managed Agents this year: long-running agent sessions that hold their state on the vendor's side, resume after a pause, and keep going. It is a good product and it solves a real problem, which is that agentic work is long and brittle and falls over if nobody remembers what happened an hour ago. It is still in beta -- every endpoint requires a beta header with a date in the name -- and I want to be fair about that, because beta means the shape can still move.

Here is the part I went looking for, on the feature eligibility table, in the vendor's own documentation, in plain sight:

Managed Agents is **not eligible for Zero Data Retention. It is not eligible for a HIPAA Business Associate Agreement.** Neither of those is a policy choice somebody could reverse with a phone call. The reason given is architectural: *"Sessions are stateful resources; transcripts persist until you delete them."*

Read the shape of that rather than the words. Deletion is a customer action. It is something you have to remember to do, build a process around, prove you did, and be able to demonstrate to somebody who asks. It is not a retention posture. A retention posture is a thing the system does whether or not anybody is paying attention, which is precisely what makes it worth something to a regulator.

The overview page says the same thing in longer form: the service is *"stateful by design"*, and sessions *"store conversation history, sandbox state, and outputs server-side."*

None of that is hidden. None of it is a scandal. It is a documented consequence of a design decision that buys you something real. But it is a rung on the harness that you do not hold, and if you are in a regulated environment you need to know which rungs those are before you build on top of them.

## The part where I was wrong, and it is the important part

Here is where I need to correct something, because I had assumed the opposite and I suspect a lot of people reading this have made the same assumption.

Self-hosted sandboxes exist. You can run the execution environment on your own infrastructure. That has been available since May, it is a genuinely good piece of engineering, and it is exactly what somebody in a regulated environment reaches for when they want the workload inside their own perimeter. My assumption -- reasonable, widely shared, and wrong -- was that self-hosting was the carve-out. Bring the sandbox home and the retention problem goes home with it.

It does not. The eligibility note is explicit, and I am going to quote it exactly because paraphrasing it would soften it: the ineligibility *"applies to all Managed Agents sub-features, including Self-hosted sandboxes."*

The self-hosted documentation explains why, and this is the sentence that actually matters: *"Tool inputs and outputs still flow to Anthropic's control plane (where Claude runs) so the model can see results and determine what to do next."*

Of course they do. The model has to know what the tool returned or it cannot decide what to do next. That is not a loophole and it is not a compromise somebody made to save money -- it is the only way an agent can work at all. The compute moved to your building. The conversation did not.

**You move the compute and you do not move the transcript.**

I want to be scrupulously fair here, because there is a version of this paragraph that is cheap and I do not want to write it. Anthropic markets self-hosted sandboxes for compliance and data residency, and that marketing is accurate. Your code, your files, your internal endpoints, your network -- those genuinely stay where you put them. That is a real guarantee and it is worth real money. It is simply a different guarantee from the one about what is retained. Two different promises, both true, sitting on two different documentation pages.

The story is not that somebody lied. The story is the buyer who read the first page and assumed the second, signed off on the architecture review, and told their board the workload was contained. That buyer is not careless. That buyer read a vendor's compliance page and drew the inference a reasonable person draws.

<!-- [YOUR TAKE]: This is the spot for the insider vantage, and it is the piece's emotional core. Something like: what happens in a real procurement or architecture review when the residency page and the retention page say different things -- who in the room is reading which one, and who is going to be asked about it later. Your clubs / regulated-environment experience is the payload here (an AML or APRA-shaped reader knows exactly what "you have to remember to delete it" costs to operationalize). Long rolling sentences welcome; I will tidy grammar only. -->

## Where the model runs, and where the data sits

There is a related thing I need to correct in public, because I have said a version of it myself and it stopped being true about a week ago.

"You cannot control where the model runs" is dead. Strike it wherever you find it, including in things I wrote. There is now a per-request setting for it.

But look at what the setting actually offers, because this is the part that matters more than the headline. The inference geography accepts exactly two values: `global`, which means it may run anywhere available, and `us`, which means it runs on United States infrastructure. That is the entire menu. There is no EU. There is no Australia.

So for a non-US regulated buyer, the choice is "the United States" or "unspecified." Both of those are offshore. The control exists, it works, and it answers a question you were not asking.

And then there is the one that actually bites, which is not about inference at all. Where the data sits at rest is a separate setting, and the documentation is blunt about it: *"Currently, `us` is the only available workspace geo."* Then, in the next breath: *"Workspace geo is set when you create a workspace and can't be changed afterward."*

Sit with the second half of that. Not a default somebody forgot to change. Not a setting an administrator can go and fix on Monday morning. A decision your organization already made, permanently, on whatever afternoon somebody clicked through the setup, almost certainly without knowing a decision was being made at all.

There is a cost line here too, and it is worth having because the economics are usually where these arguments actually get settled. Pinning inference to the US is *"priced at 1.1x the standard rate across all token pricing categories"*, and each of those tokens *"draws down 1.1 tokens from your committed"* capacity. Residency has a meter on it. Ten percent is not a lot, and it is also not nothing at scale, and it is the first time I have seen the sovereignty conversation carry an actual number on the invoice rather than a hand-wave about enterprise pricing.

## The part you genuinely do run

I have spent two thousand words telling you what you do not hold, which is the East Coast in me and I make no apology for it. Now the other half, because there is a piece of this harness that is unambiguously yours, and it is the most literal example I have found of governance you build rather than governance you receive.

Inference hooks. You point the platform at a server that you operate, and every governed prompt is held -- before inference begins -- until your server returns a verdict. Not logged afterward. Not reviewed in a dashboard on Thursday. Held, in the request path, waiting on a decision made by software that runs on your infrastructure and answers to you.

Your server sees the transcript text, the tool calls and their results, and text pulled out of attachments. It does not see raw file bytes, system prompts, or the vendor's internal context. Verdicts are allow or deny and nothing else -- you cannot rewrite a prompt or redact it on the way through, which is a real limitation and I would rather you heard it from me than discovered it in week three. There is a five second default timeout. It is Enterprise-only, it is beta, it excludes voice and a few other paths, and it is not available if you are coming through Bedrock or Google Cloud.

That last set of limits matters, and not in the direction you would expect. Because this is Enterprise and signed-in only, it does nothing whatsoever for the person running a personal subscription on a work laptop, which is a population I flagged on Friday and which has not gotten smaller. So this is not a general answer. It is a specific, powerful control for a specific tier.

Now here is the sentence that made me want to write this piece.

**Whether the hook fails open or fails closed is your setting.**

The vendor ships the mechanism. You decide whether it is actually a control. Set it to fail open, and on the day your verdict server is slow or down or misconfigured, every prompt sails through and the system keeps working beautifully and nobody files a ticket, because from the outside a control that is not holding looks exactly like a control that has nothing to stop. You will be able to point at it in the system diagram. It will be in the architecture doc. It will have a box and an arrow and a name.

I will come back to that on Friday, because it turns out to be the whole week's problem in miniature.

## Where I would push back on myself

The sharpest objection to everything above is that I have described the ordinary condition of buying anything. Every vendor relationship has terms. Every managed service holds something you would rather it did not. You do not get to outsource the operation and keep all of the control, and grown-ups have known this since the first payroll bureau. Welcome to procurement.

That is fair, and I will concede most of it. I am not claiming vendors are hiding things -- I found every fact in this piece in public documentation, in under an hour, with no special access, and I have quoted it rather than characterized it precisely because none of it needed a leak.

What is different is the gap between where the marketing sits and where the constraint sits. The residency story is on the page you are shown during evaluation. The retention story is on a feature eligibility table you reach by following a link from a footnote. Both are true. Only one is in the room when the decision gets made. That is not deception, but it is an architecture of attention, and the effect on a busy buyer is indistinguishable from one.

And the second objection, which is better: none of this stopped anybody from shipping anything. Correct. It should not. The point of knowing which rungs you hold is not to refuse to climb.

## What I would actually do this week

**Write down your harness, on one page, in four columns.** What the agent can touch. What happens to what it produces. Where that is retained and for how long. And who at your organization can change each of those. Most people I know can fill in the first column immediately and stall on the third. The stall is the finding.

**Then go and read the eligibility page for whatever you are actually running.** Not the product page. Not the security overview. The table with the yes and no columns in it, for the specific features you have turned on, including the ones you turned on because they solved a problem in a sprint eight months ago. This takes about twenty minutes and it is the cheapest thing on this list.

**Check what geography your workspaces were created in, and stop looking for the setting to change it.** If it is fixed at creation, then the remedy is not configuration, it is a new workspace and a migration, and that is a project with a budget rather than a checkbox. Better to learn that now than in the middle of a due diligence questionnaire.

**And if you have hooks available to you, find out which way yours fails.** One question, one answer, and it tells you whether you have a control or a diagram.

## What this is really about

The reason to know all of this is not so you can be disappointed. Every one of these products is genuinely good, the documentation is genuinely honest, and I would rather work with a vendor that publishes an eligibility table with a "No" in it than one that publishes a brochure.

The reason is that you are going to build a harness whether you decide to or not. Some of it you will assemble deliberately. The rest of it will be assembled for you, out of defaults you never saw, on afternoons nobody remembers, and it will work perfectly well right up until somebody asks you to describe it.

The building is yours. The equipment is yours. The staff are yours.

Go and find out where the till reports.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that the model is the commodity and the harness is the product, that self-hosting moves the compute without moving the transcript, and that the parts of your harness you do not hold are documented in public on pages nobody reads during an evaluation.*
