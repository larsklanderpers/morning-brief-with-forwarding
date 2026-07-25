# You Shipped It. Can You Explain It? Can anyone?

**Status: Draft (v1) -- target Tuesday, 14 July 2026**
**Series: Weekday feed**
**Thread: Shape of Work-to-Come · coding/practitioner ground truth**
**Builds on: Monday's "Now the Hard Part: The Seats That Can't Go Empty" (13 Jul). First of the week's load-bearing seats.**
**Source spark: r/cscareerquestions — "the real harm of AI coding isn't job displacement, it's that mid-level engineers can no longer explain what they built" (450 pts); Ethan Mollick, "Specs, not tricks" (One Useful Thing, 7 Jul).**

---

There's a particular kind of house that every electrician has a story about. Four owners deep, each one added something -- a circuit here, a subpanel there, a run of wire fished through a wall on a Saturday by a guy who was "good with that stuff." Every improvement worked. The lights came on. The house passed from hand to hand, and nobody wrote anything down, because why would you -- it works. Then one day a breaker won't stop tripping, an electrician opens a wall, and finds a knot of wire that no living person can explain, feeding something that goes somewhere that connects to a thing that should not, by any code ever written, be connected to it. And she stands there and says the sentence that costs you four thousand dollars: "I can't work on this until I understand what's actually going on here."

The house was functional the entire time. It was also, the entire time, accumulating a debt. The debt wasn't the wiring. The debt was that nobody could explain the wiring. And that debt sat at zero on every invoice until the day it came due in full.

I've been thinking about that house because the practitioners furthest into the AI-coding experiment are describing exactly it -- and it's the first of the load-bearing seats I promised you yesterday.

## The harm nobody priced in

The loudest debate about AI and software has been about jobs -- will the models replace engineers, how many, how soon. But the most interesting thread I saw this week wasn't about displacement at all. It was a room full of experienced developers, two years into building with these tools every day, arguing that the real damage is something quieter and more corrosive: mid-level engineers increasingly cannot explain what they built.

Not "didn't document it." Cannot explain it. The code was generated, it passed the tests, the pull request merged, the feature shipped -- and if you sat the author down and asked them to walk you through why it works, trace what happens when it fails, or defend the choice it makes on the fourth branch of some conditional, they couldn't. The artifact exists. The understanding never did. And because the thing runs, nothing flags it. There is no test for "the human who shipped this has no idea what it does." The build is green. The debt is invisible. It sits at zero on every invoice until the day someone has to change that code, or secure it, or explain to a regulator why it denied a particular person a particular thing -- and the only answer available is a shrug.

They've started calling it Comprehension Debt, and it is the truest new phrase I've heard this year. It behaves exactly like technical debt, except technical debt at least tends to announce itself -- the slow build, the flaky test, the module everyone's scared to touch. Comprehension Debt is silent by construction, because the code is often *good.* The model writes clean, plausible, working software. That's what makes it dangerous. Ugly code that doesn't work gets fixed. Clean code that works and that nobody understands gets shipped, and trusted, and built upon, until it is load-bearing in your business and opaque to your staff at the same time.

## Why this is more than a style complaint

Let me say plainly why I, of all the hats I wear, care about this one -- because it would be easy to file "engineers should understand their code" under craftsmanship and old-man-yells-at-cloud, and that's not where it belongs.

You cannot govern what you cannot describe. Every control you own -- every audit, every incident response, every "explain why the system did that" -- assumes there is a human somewhere who can reconstruct what the system actually does. When a breach investigation starts, the first question is *what does this code have access to and why.* When a regulator comes asking about an automated decision, the requirement, increasingly by law, is that you can describe in plain language what data fed it and how it decided. When something fails at 2am, the person on the call has to hold the whole path in their head well enough to find the break. Every one of those is a comprehension check wearing a different uniform. And Comprehension Debt fails all of them simultaneously, silently, in advance.

So the human who can still explain the system -- trace it, defend it, hand it off cleanly to the next person -- is not exercising a nice-to-have craft virtue. They are standing on a trust boundary. Their comprehension is the control. It's the last thing between "we run software that does what we intend" and "we run software that does *something,* reliably, and we've decided to trust it." That's the Editor and the Risk Steward I wrote about earlier this month, fused into one very hireable person: the taste to know what's worth understanding, and the discipline to refuse to ship past the edge of their own understanding.

It seems obvious to say, but a trust boundary defines everything within it. A skyscraper has a few hundred structural members an engineer can point to, stamp, and inspect. A mid-sized enterprise system has thousands of load paths nobody ever drew -- more of them every week, now that a model writes the beams and no one reads them. And unlike the building, you can't see which walls are holding the thing up. So when one of them turns out to be load-bearing and nobody knew it, you find out the way you always do: all at once, on the worst possible day.

## "Specs, not tricks"

Ethan Mollick put the constructive version of this better than I can, so I'll borrow it. His argument this month was that we've been thinking about these models all wrong -- treating them like a spellbook of clever prompts, when we should be treating them like capable, literal executors who need *management.* Goals. A definition of done. Quality bars. Tests. Specs, he says, not tricks.

Here's what that reframe quietly requires, and it's the whole point of today. You can only manage an executor whose output you can *inspect.* A manager who can't evaluate the work isn't managing; they're hoping. The entire "specs, not tricks" model -- the thing that makes AI a lever instead of a liability -- rests on a human at the end who can look at what came back and actually tell whether it's right. Take that human away, or let their skill atrophy until the output sails past unread, and you haven't delegated to the agent. You've abdicated to it. Those look identical on the day you do them. They are not remotely the same six months later, standing in front of the open wall.

## What to actually do

The move here isn't to stop using the tools. It's to protect comprehension on purpose, because it will not protect itself -- the entire gradient of these tools pulls toward generating faster than you understand.

Make "can you explain this" a gate, not a courtesy. If a change can't be walked through by the person submitting it, it isn't done, no matter how green the build is. Treat the ability to trace and defend a system as a first-class deliverable, the way you'd treat the feature itself. And when you're deciding who's valuable on a team where anyone can generate a hundred lines in a second, weight hard toward the person who can still tell you why the ninety-nine you threw away were wrong. When generation is free, understanding is the scarce input, and scarce inputs are where the value goes. This will have key operational impact: code reviews (and PRs) become more critical, knowledge transfer (lunch-and-learns or whatever they are in your business) becomes not just nice to have, but an actual *survival strategy*. And managers who trust senior engineers without understanding the work they are doing ("they've always been reliable in the past") when they don't necessarily understand anymore what that work is at the granular level, are knocking down walls in your house without you even seeing they have done so.

Tomorrow I want to follow this one step downstream, into the place Comprehension Debt does its ugliest damage: the approval. Because there's a moment, more and more, when a human clicks "approve" on something an agent produced -- and whether that click is a genuine control or a rubber stamp depends entirely on whether the person doing the clicking could have passed today's test.

You shipped it. That was the easy part, and it got easier. The question that decides whether you actually own your systems or merely host them is the old, unfashionable one: can you explain it?

---

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that in a world where anyone can generate the code, the person who can still explain it just became the most important hire on the team.*
