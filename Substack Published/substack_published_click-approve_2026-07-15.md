# Click Approve. Do You Know What You Just Allowed?

**Status: Scheduled (final) -- Wednesday, 15 July 2026**
**Series: Weekday feed**
**Thread: AI as Attack Surface × Shape of Work-to-Come · coding/practitioner ground truth**
**Builds on: Monday's "Now the Hard Part: The Seats That Can't Go Empty" (13 Jul); Tuesday's "You Shipped It. Can You Explain It?" (14 Jul) — the Comprehension Debt argument.**
**Source spark: Wiz's disclosure of "GhostApproval," an attack that subverts the approval/confirmation flow AI coding assistants use to gate agent actions (10 Jul cyber brief).**

---

Here is a control you have relied on your entire life without ever thinking about it. When a doctor writes you a prescription, a second person -- the pharmacist -- has to fill it. That second human isn't there for ceremony. They're there to catch the thing the first human missed: the interaction with the other drug you're on, the dose that's off by a decimal, the allergy in your chart. Two sets of trained eyes, and the second one exists specifically to say *no, not this one.* It's one of the oldest and best pieces of safety design we have, and it works for one reason and one reason only: the pharmacist actually knows pharmacology.

Now imagine a pharmacist who fills whatever's written, no questions, because reading each script closely is slow and the doctor's usually right. Nothing changes on the surface. The counter looks the same. The little consultation window is still there. Prescriptions still get a second signature. But the control is gone -- not removed, *hollowed.* It looks exactly like a safety layer and it is actually a delay wearing a lab coat. And you would not know the difference until the day the wrong two drugs go in the same bag.

I've been describing pharmacists. I've actually been describing the "Approve" button on your AI coding assistant, and a piece of research that should make everyone who ships software this way sit up. Very, very straight.

## What GhostApproval actually breaks

The security firm Wiz disclosed an attack method last week they've named GhostApproval, and the elevator version is this: it subverts the approval step that AI coding assistants use to gate their own actions.

If you haven't worked with these tools closely, here's the shape of the thing. A modern coding agent doesn't just suggest text anymore. It reads your whole repository, holds your context, and increasingly *acts* -- it wants to run a command, modify a file, install a dependency, push a branch. And because letting software do all that unsupervised is obviously dangerous, the vendors built in a human-in-the-loop gate: before the agent does something consequential, it stops and asks you to approve. That approval step is the safety design. It's the pharmacist. It is, in many shops, the *entire* control standing between "a helpful assistant" and "an unsupervised process with your credentials executing on your infrastructure."

GhostApproval goes after exactly that gate -- manipulating the flow so the human approves something other than what they believe they're approving. Think about what that means in terms you already have. The AI coding assistant has quietly become the most privileged insider in your building: it reads everything, remembers everything, and now executes. An attack that subverts its approval step is not a clever trick around the edges. It is the AI-native version of privilege escalation, aimed at the one place you were counting on a person to catch it. And here's the detail that should keep you laser-focused on the risk: most teams have no telemetry whatsoever on what their coding agent was actually asked to approve. There's no log of the click. The one control they're relying on is also the one they can't audit. This is particularly true if your developers are using frontier model harnesses or something bespoke; tracking the approval cycle is not in the design spec for them, and it's arguably one of the most critical developer evaluation tools you can have.

## The exploit is just automating what we're already doing for free

I could write the whole piece as a GhostApproval explainer, tell you to demand approval-flow telemetry from your vendors -- which you should -- and sign off. But that would miss the part that actually connects to this week, and it's the part that matters more than any single CVE.

*GhostApproval works because people approve things they don't understand.*

Sit with that, because the exploit is almost beside the point. An attacker had to build a whole technique to trick a human into approving something they didn't grasp -- and meanwhile, all day, every day, across every team using these tools, humans are *voluntarily* approving things they don't grasp. They're hitting approve because the diff is long, because the agent is usually right, because it's four o'clock, because reading it carefully would erase the very speed the tool was bought for. GhostApproval is just the automated, weaponized version of a hole we are already walking through on our own, cheerfully, dozens of times a day.

This is yesterday's argument arriving at its sharpest point. I wrote about Comprehension Debt -- the quiet accrual of software logic and dependencies that no one in your organization or out can explain. The approval gate is where that debt gets *cashed,* because an approval is a comprehension test with consequences attached. A human in the loop who cannot read what they're approving is not a control. They are a latency cost with a rubber stamp. They provide the *appearance* of oversight, which is worse than no oversight at all, because the org has now checked the "human reviewed it" box and moved on, believing a wall is there.

## A human in the loop is not the same as a *qualified* human in the loop

We talk about "human-in-the-loop" as if the phrase itself is the safeguard -- as if inserting a person, any person, at the decision point discharges the risk. It doesn't. HITL is only ever as strong as the human's ability to say a meaningful *no.* Put someone at the gate who can't evaluate what's passing through it, and you haven't added a control; you've added a delay and a false sense of security, and you've given the next auditor a checkbox that lies.

Which means the load-bearing seat here isn't "the approver." It's *the qualified approver* -- the person who can look at what the agent proposed, actually understand it, and withhold the click when it's wrong. That's the pharmacist who knows pharmacology. And building your process around that person means two things most teams haven't done. First, design the gate so a competent human *can* actually understand what they're approving: scoped actions instead of sweeping ones, readable diffs instead of thousand-line dumps, and yes, telemetry on what was asked and what was granted, so the one control you depend on is one you can also review. Second -- and this is the harder one -- make sure the person standing there is someone who *can* pass the test on the other end of the approval.

That second requirement raises a question this whole week has been circling toward, and I'm going to leave it hanging until Friday because it deserves its own day: qualified approvers are not born knowing what to refuse. Nobody hands you the judgment to withhold that click. It gets *grown* -- and we are, right now, busy dismantling the very pipeline that grows it. At speed, and well before the bill comes due -- which means most organizations won't understand the scope of the loss until long after they've taken the hit. Hold that thought.

## Tomorrow

Before we get to where these people come from, we have to look at what they're actually standing on. Tomorrow: the trust boundary itself -- the invisible line your whole architecture is quietly resting on -- made brutally, unforgettably concrete by a flaw that sat inside the Linux kernel for fifteen years and turns any user into root in about five seconds.

For today, the discipline is smaller and more uncomfortable. Go find every place in your shop where a human clicks "approve" on something a machine produced, and ask the honest question: could that person, on that day, have actually explained what they just allowed? Every place the answer is no, you don't have a control. You have a pharmacist filling whatever's written -- and you're about to find out what's in the bag.

---

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that "a human approved it" and "a human who understood it approved it" are different sentences, and only one of them is a safeguard.*
