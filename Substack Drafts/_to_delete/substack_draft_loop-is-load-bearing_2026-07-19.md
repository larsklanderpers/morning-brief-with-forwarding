# The Loop Is Load-Bearing

**Status: Draft (v1) -- target Sunday, 19 July 2026**
**Series: Sunday Capstone — Week of 13–19 July, "The Load-Bearing Human"**
**Threads synthesised: Shape of Work-to-Come · AI as Attack Surface · Trust Boundaries · coding/practitioner ground truth**
**Builds on: "Now the Hard Part: The Seats That Can't Go Empty" (Mon) · "You Shipped It. Can You Explain It?" (Tue) · "Click Approve. Do You Know What You Just Allowed?" (Wed) · "The Boundary You Can't See" (Thu) · "Nobody Starts Senior" (Fri) · "There's Never Been a Better Time to Go It Alone" (Sat) · prior capstone "The Actor Is No Longer Human" (12 Jul)**

---

Last Sunday I told you the actor is no longer human, and I walked you through five empty chairs to prove it. The gatekeeper, the insider, the identity, the attacker, the substrate -- five seats a person used to fill, quietly vacated, while the governance stack kept addressing a human who wasn't coming back.

This Sunday I owe you the other half, because the empty chairs were the easy half. This week was about the seats that *cannot* go empty -- and what I found, walking through them one at a time, is that they aren't really five separate seats at all. They're one thing, standing in five places. Let me show you.

<!-- [YOUR TAKE]: If you want a personal opener instead — a moment this week where you watched a "human in the loop" turn out to be either the only thing that caught a failure, or a rubber stamp that caught nothing — this is the spot. -->

---

## Walk the wall

**Monday** named the frame. You cannot tell a load-bearing wall from a decorative one by looking at it -- they're the same wall -- and the feedback from knocking out the wrong one is delayed. Automate a role, watch nothing break, conclude the human was decorative. Sometimes true. Sometimes the structure is just working harder to cover the gap, and the sag is coming.

**Tuesday** found the first load-bearing seat: the human who can still explain the system. Comprehension Debt -- clean, working, generated code that no living person can trace or defend -- sits at zero on every invoice until the day someone has to change it, secure it, or answer a regulator for it. You cannot govern what no one can describe. The explainer isn't practicing craftsmanship; they're standing on a trust boundary.

**Wednesday** followed the debt to where it gets cashed: the approval. GhostApproval, the attack on AI coding assistants' approval gates, works because people approve things they don't understand -- and we didn't need an attacker for that; we do it voluntarily, dozens of times a day, because the diff is long and it's four o'clock. A human in the loop who can't read what they're approving is not a control. They're a latency cost with a rubber stamp.

**Thursday** went below the floorboards. GhostLock -- fifteen years in the kernel, five seconds to root, straight through the container wall the entire cloud economy is priced on. A trust boundary is only as real as the people who know it's there, and the person who can see the survey line where everyone else sees the fence is not in your tooling. The scanner is a rear-view mirror; the boundary-seer looks forward.

**Friday** asked where all these people come from, and answered it: they get grown, and nowhere else. Nobody starts senior. The explainer, the qualified approver, the boundary-seer -- every one of them is manufactured by the same pipeline we are currently dismantling because "AI does the junior work now." The tickets were never the product. The tickets were the flight hours.

And **Saturday**, the lighter turn that wasn't actually a departure: strike out alone with a stack of agents and you become every one of these seats at once. The solo operator's moat isn't the leverage -- everyone gets the leverage. It's the judgment concentrated into one disciplined human. Even a company of one has to build a loop and stand in it.

Five days, five seats. Now lay them side by side, the way I laid out the empty chairs last week, and look at what they have in common.

## One wall, five places

Every seat this week sits at a boundary. The explainer stands between "software that does what we intend" and "software that does *something,* reliably, that we've decided to trust." The approver stands between an agent's proposal and its execution. The boundary-seer stands between the architecture you think you have and the one you actually have. The Grower stands between the qualified humans you have now and the ones you'll need in five years. The solo operator stands at all of them, alone, with no one checking.

That is not five controls. That is one control -- **the human in the loop** -- load-bearing at five different points in the structure. And here's the inversion this week has been building to, the one that flips how most organizations currently treat it.

Almost everywhere I look, HITL is managed as *friction.* A speed bump. A compliance ritual to be satisfied with the cheapest available click, an approval step to be streamlined, a review gate whose success metric is how little it slows the pipeline. The entire managerial instinct of the last two decades -- optimize the process, remove the bottleneck -- points squarely at the human in the loop as the thing to minimize.

That instinct is now dangerous, because it optimizes for exactly the failure this week described five times. Minimize the loop and you get the hollow version of every seat: the approver who clicks without reading, the review that checks the box, the boundary nobody walks, the pipeline nobody funds. The wall is still drawn on the plans. It's just not holding anything -- and you've told the auditors it is. A hollowed control is worse than no control, because no one covers for a gap they believe is covered.

The loop is not friction that governance tolerates. The loop *is* the governance. It is the load-bearing wall standing at every trust boundary you own -- and last week's capstone is why this matters so much right now. The actor on the other side of your controls is no longer human. The actor *inside* the control -- the one element that can still say a meaningful no -- had better be, and had better be qualified.

## Design the loop like you mean it

So the capstone discipline this week is the inversion itself: stop asking how to minimize the human in the loop, and start asking how to **optimize** them -- deliberately, with budget, the way you'd engineer any other structural element. Four moves, one per seat.

**Put your most qualified humans at your highest-consequence boundaries -- on purpose.** Most organizations staff approval gates by availability: whoever's on rotation, whoever's cheapest, whoever clicked fastest last quarter. Walk your boundaries instead, rank them by blast radius, and staff them by qualification. The question for every gate is Wednesday's: can this person, on this day, actually explain what they just allowed? If the honest answer is no, you don't have a control there -- reassign the seat or redesign the gate until you do.

**Make the loop passable.** A qualified human still fails at an impossible gate. Scoped agent actions instead of sweeping ones. Readable diffs instead of thousand-line dumps. Telemetry on what was asked and what was granted, so the one control you depend on is one you can audit. If your approval flow can only be satisfied by rubber-stamping, the flow is the defect -- you designed a gate that selects for not looking.

**Pay the comprehension tax as you go.** Comprehension Debt compounds silently, and the loop is where it gets cashed. Make "can you walk me through it" a gate for shipping, make explanation a first-class deliverable, and treat the ability to trace and defend the system as the asset it now is. When generation is free, understanding is the scarce input -- fund it like one.

**Fund the wall's supply chain.** Friday's argument, one sentence: every qualified human in every loop was grown, and the growing takes years by its nature. The pipeline that manufactures your 2031 approvers is a structural dependency of every control you'll be running that year. Budget it like one, or accept that you've scheduled the wall's demolition for a date you don't get to choose.

## The chair, revisited

Last week ended with a warm chair -- the person we kept expecting to walk through the door, who turned out to be a process, a configuration, a memo. I stand by every word. Most of the seats really are empty now, and a lot of them should be; there's real freedom in that, and Saturday was about claiming it.

But walk the building one more time. A few of the chairs are still occupied, and this week showed you why: they were never really chairs. They were columns with a person wrapped around them. The one who can explain it. The one who can refuse it. The one who can see the line. The one who grows the others. Pull those humans out and the ceiling doesn't fall on Monday -- that's what makes it tempting -- it falls in the wet winter, all at once, with the org chart still showing a wall where a wall no longer is.

The machine's speed is real, and it's the best leverage any of us have ever held. But speed without a qualified no is just how fast you hit the wall you couldn't see.

The human in the loop isn't what slows the machine down. The human in the loop is what keeps the machine's speed from becoming the organization's undoing. That's not friction. That's the building standing up.

---

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. On Sundays he tries to make the week add up to something.*
