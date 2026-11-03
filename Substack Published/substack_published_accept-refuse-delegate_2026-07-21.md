# Accept, Refuse, or Delegate: The Only AI Decision That Matters Now

**Status: Published -- Tuesday, 21 July 2026** (confirmed by Lars 26 Jul; reconciled from rv2, which is what actually ran. NOTE: rv3 in Substack Drafts\ is a LATER correction that was never published -- it sharpens the CPS 230 sentence from "CPS 230 cares about where the consequential inference runs" to the primary-source framing (material offshoring = service *performed* offshore, notify APRA before entering one). rv3 also splits the globe/atlas close into its own paragraph. Do NOT swap rv3 in here -- this file is the archive of what readers actually received.)
**Series: Weekday feed**
**Thread: Accept, Refuse, or Delegate (Co-Existence & the governance of judgment). Fuses with the Where-It-Thinks thread.**
**Builds on: Monday's "The Compliance Tool Nobody Ordered Just Shipped as a Model" (20 Jul); last week's HITL arc -- "Click Approve" (15 Jul), "You Shipped It. Can You Explain It?" (14 Jul), "The Loop Is Load-Bearing" (19 Jul).**
**Source spark: Ethan Mollick, "The Twilight of the Chatbots" / his forthcoming book *Co-Existence: The Next Phase of AI* (One Useful Thing); the 17 Jul AI signal -- "which categories of AI use cases are legally defensible in the cloud, and which require controlling the inference stack."**

---

The chatbot is dying. Not the technology -- the *posture.*

The era where AI was a clever helper you prompted, with a human sitting firmly at the center running the show, is closing. What replaces it is messier and a good deal more demanding, and the demand falls on exactly the muscle most organizations have not been training.

Ethan Mollick (the Wharton professor who has become the most-quoted sane voice on how to actually use these tools) has a name for the shift. His 2024 book, *Co-Intelligence*, put the human at the center and treated AI as a co-pilot -- smart, useful, firmly subordinate. His new one, *Co-Existence*, out this autumn, argues we are already past that. We now work alongside AI that is, in his words, "sometimes, but not always, better than you." And that one qualifier -- *sometimes but not always* -- is the whole ballgame. Because it means the decision in front of you is no longer the big, one-time "do we use AI." It is a small decision you now make dozens of times a day, per task: do I *accept* what it gave me, do I *refuse* it and do the work myself, or do I *delegate* the whole thing and walk away.

Anyone who has ever been promoted into managing people remembers the specific vertigo of it. The thing that got you the job -- doing the work yourself, well -- is suddenly the thing you have to stop doing. And the skill you have to learn, fast, under pressure, is which tasks to keep, which to hand over and check, and which to hand over and genuinely trust. Lean too far toward control and you micromanage the whole team to a standstill. Lean too far toward trust and you sign off on a disaster you never actually read. That judgment -- oversight matched to stakes -- *is* the job of managing. Mollick's argument, boiled down, is that this just became everyone's job, except the team you are now learning to delegate to, for good or ill, is a stack of agents rather than people.

## Three buckets

So sort your work into three buckets, honestly.

**Accept.** The output is good enough to use with a glance. Low stakes, easily reversible, cheap to be wrong. A first-draft email, a summary you will skim anyway, boilerplate you would have written yourself. You look, you nod, you move. A human is nominally present but barely load-bearing, and that is fine, because the cost of a miss is a shrug.

**Refuse, or verify.** You keep a qualified human in the loop who can say a meaningful *no.* High stakes, hard to reverse, someone's money or rights or safety on the line. This is last week's entire argument, arriving as a category: the approval that GhostApproval went after, the automated decision a regulator will one day ask you to explain in plain language, the diff whose author had better be able to walk you through it. The human here is not ceremony. The human here is the control.

**Delegate.** You hand the whole task to the agent and let it run without watching each step -- *but only* where you have decided in advance that accept-bucket rules hold at scale and the blast radius is contained. Delegation is not "I trust the machine." It is "I have pre-decided that if this is wrong, the damage is small and recoverable, so I am buying back my attention."

The skill -- the entire skill -- is putting each workflow in the right bucket. That is the decision. Everything else is execution.

## The bucket is also your compliance map

Here is what Mollick's frame quietly hands the regulated business, and it is the reason I am spending a weekday on a management idea instead of a threat.

That accept / refuse / delegate call is the *same call your compliance program has to make anyway.* The Privacy Act's automated-decision rules care about precisely one category: decisions that *significantly affect* a person. Those are refuse-or-verify, by law -- a qualified human who can explain the outcome, and a disclosure that says so. CPS 230 cares about where the consequential inference runs -- and the refuse-or-verify workloads are exactly the ones you want in a jurisdiction you can reach, on a stack you control, which was Monday's whole point. The delegate bucket -- the genuinely low-stakes, reversible work -- is where a frontier cloud API is perfectly fine, because nothing that touches a person's rights is riding on it.

Read that again, because it is the load-bearing sentence of the week. The categorization exercise I asked you to start yesterday and the accept / refuse / delegate decision Mollick describes are not two exercises. They are one. A single list that tells you what to automate, what to supervise, and what to bring home.

The sharpest way I saw it put this month: the question is no longer "cloud AI or local AI." It is "which of our use cases are legally defensible to delegate, and which require a qualified human and a controlled stack." Answer that once, properly, and you have done your December compliance homework and drawn your AI architecture in the same afternoon.

## The two ways to get it wrong

There are exactly two failure modes, and they are mirror images.

**Over-delegate.** You hand the high-stakes bucket to the agent because it is usually right and reading the output is boring. That is the rubber stamp -- the hollowed control from last week, the approver who cannot pass the test on the other side of the click. It is invisibly comfortable, because nothing breaks on the day you do it. The bill arrives in the wet winter, when the one decision you delegated and never should have turns out to be the one a regulator, or a court, or a customer's lawyer wants explained.

**Over-refuse.** You put a human gate on everything, including the reversible, low-stakes work, and you have thrown the leverage straight in the bin. Now you are paying frontier prices to have a qualified person babysit a summarizer. Worse is the compliance-theater version: a review step that exists mainly to be shown to an auditor, slowing every workflow and protecting none of them.

More than that, over-refusal is, in many ways, even worse than over-delegation -- and it gets far less attention. There is a tendency to emphasize the over-delegate danger, and no small part of that is because I think a lot of managers are micromanagers at heart. They've just trained themselves not to be, and they're worried about how far off the rails something can go without them watching it all the time. Overweighting that concern -- the fear of what happens if they step back and don't watch closely enough -- comes mostly from trusting their own taste judgment more than they trust the taste judgment of the people who work for them. I think that's a defensible position, though only partially.

The bigger problem with over-refusal, or over-gating, is that humans get tired. They get tired of doing the same task again and again, even when it isn't the same task but merely presents as one. Security people have a name for this: alert fatigue -- the numbness that sets in when you have to clear a hundred low-value alerts to find the one that matters, until you're waving them all through on autopilot. And the critical element is not always the first one back. In many cases it's the 25th of 200, and the 5th that day. Counting on a human to catch that one after you've marched them through the twenty-four (or two hundred and four) before it -- none of which carried any particular weight -- is a recipe for disaster, simply because of the way humans read and respond to patterns. It is why the SOC misses the single alarm that was real -- and it is exactly what over-gating does to your best approver.

Notice the shape of the fantasy underneath both. The cinematic version of "AI strategy" is a single, dramatic yes-or-no bet at a board offsite. The real thing is unglamorous triage -- a hundred small, correct bucket-assignments, made by people who understand the work. And because Mollick's models are "sometimes but not always" better, the buckets *move.* What was refuse-or-verify last year is accept this year; the seven models that shipped in the last ten days just nudged a whole column of your workflows toward delegate whether you have noticed or not. So this is not a one-time sort. It is a standing discipline, and treating it as a one-off is its own kind of miscategorization.

## What to actually do

**Sort by consequence, not by department.** Do not ask "should marketing use AI." Ask, of each individual workflow: if this is wrong and nobody catches it, who gets hurt, and how reversibly? That answer picks the bucket. The org chart is the wrong axis; blast radius is the right one.

**Write the bucket down, and name who owns the no.** For every refuse-or-verify workflow, name the qualified human at the gate -- and make sure they can actually pass the test, because a refuse bucket with an unqualified gatekeeper is just an accept bucket lying to your auditor. That was the entire lesson of "Click Approve": a human in the loop who cannot read what they are approving is not a control, they are a latency cost with a rubber stamp.

**Re-sort on a schedule.** The models moved seven times in ten days. Your buckets are not permanent, and the review is not optional. Put a quarterly re-sort on the calendar, or accept that you are governing this year's AI with last year's map -- and telling the regulator it is current.

Tomorrow, the refuse bucket meets an enemy Mollick does not spend much time on: the clock. When an attacker gets from foothold to lateral movement in twenty-nine minutes, "keep a qualified human in the loop" runs headlong into "no human on earth is that fast." Those two things have to be reconciled, and the reconciliation is this same three-bucket idea, pointed at your security operations. That is Wednesday.

For today, the work is quieter and harder than it sounds. Accept, refuse, delegate. Three words.

Sort your work into them honestly, and you will find you have built your AI strategy, your compliance map, and your risk register at the same time -- because, it turns out, they were always the same document. You just had not been asked to write it down before.

For most executives I talk to, this is the gap. They were trained to think enterprise-wide, to reach for the solution that if it is not one-size-fits-all is at least one-size-solves-most, even when it solves none of them well. That read doesn't work, anymore. The same people who spent a whole career becoming generalists now have to turn that on its head, because the generality itself has become the risk. A globe is a beautiful thing, and it will never once get you down a single street. So here is the only question that actually matters this week, and you answer it with your calendar, not your strategy deck: do you keep turning the globe, or do you finally break out the atlas?

---

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that the most important AI decision your organization makes is not which model to buy, but which of three buckets each piece of work belongs in.*
