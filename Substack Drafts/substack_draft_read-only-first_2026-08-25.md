# Read-Only First

**Status: DRAFT v1 -- target Tuesday, 25 August 2026. Diversion #1, ground game: short, operational, do-it-tonight. Register test is the optimistic take, per the standing rule that lightness is a state of being and not a length metric. ~1,425 body words. Needs the panel and one [YOUR TAKE].**
**Series: Weekday feed (Tuesday Diversion)**
**Thread: Practitioner / Coding Ground Truth · Shape of Work-to-Come**
**Builds on: Mon 17 Aug ("The Model Isn't the Product. The Harness Is.") -- declared in one line, desk-scale version of the system-scale argument. Tue 18 referenced in ONE clause and not re-run.**
**Source: References\week-plan_2026-08-24.md, Tue 25 block. Allie K. Miller quotes via Inc. (17 Mar 2026) and Fast Company (27 Apr 2026).**

**⚠️ WINDOW CHECK -- Mon 24 is the immediate predecessor and it constrains this piece more than the plan anticipated:**
**- Mon 24 OPENED BY ANNOUNCING ITSELF A DIVERSION ("A different kind of diversion today"). This piece is the actual scheduled Diversion and must NOT announce itself as one -- two in a row is a device. It opens cold and is light by behaviour instead.**
**- Mon 24 owns: the three-contractors-on-a-building-site analogy, Lord of the Flies / Hobbes, "introduce them," and the org-design frame. None reused.**
**- ⚠️ Mon 24's action section says "check that your instructions can all be true at once" -- INSTRUCTIONS. This piece is ACCESS. The two are adjacent and the distinction is stated in text so they do not read as one argument twice.**
**- Mon 24's close is a we-asked-the-wrong-question shape. Not reused here.**
**- Sun 23 owns "the parts on the bench" and "Bring the list." Sat 22 owns receipts. Fri 21 owns beliefs-with-good-reputations. None reused.**
**- Kitchen (Sat 8) and agent counts (Mon 27 Jul) avoided per the plan.**

**⚠️ ACCURACY -- the plan's do-not-print list is absolute and none of it appears:**
**- NO "34 agents." Her public figures are 7, 20 and 25 in different contexts, never 34.**
**- NO Stripe access. It appears in no primary and she argues the opposite.**
**- NO "do smart things" -- no evidence it is a real quote.**
**- NO "escalate only what needs her" -- appears in no primary source at all.**
**- NO Greg Isenberg video. It does not exist; the agent-workforce video is The Information's, at 1,524 views, not 29K.**
**- The two quotes used are the whole of what is documented, and both are carried with their source named in text.**
**- Her contractions inside quoted speech are HERS and are left exactly as spoken. The surrounding prose is uncontracted per his standing register.**

---

Nobody gives a new hire the production database on their first morning. Not because you distrust them -- because you have not watched them work yet.

You give them a read-only login. They spend a week reading code they did not write, sitting in meetings where they understand about half of it, and asking questions that are occasionally very good. Somewhere around the second week somebody says "give her commit access to the staging branch," and a few weeks after that she is shipping. Nobody wrote that ladder down. Everybody has climbed it.

Then we started hiring agents, and we skipped the entire thing.

## The rung the demos are shot on

Here is what I think happened, and it is not anybody's fault exactly. Every demonstration of an agent you have ever watched is shot on the top rung. The agent reads the ticket, writes the code, runs the tests, opens the pull request, and posts to the channel to say it is done. That is a good demo. It is also the most privileged configuration the software supports, and it is the first one most people try, because it is the one they were shown.

So the question people ask first is *what can this thing do.* Which is the wrong first question, and I say that as somebody who asked it in exactly that order.

The first decision is not what an agent is allowed to do. It is what it is allowed to **see**.

Last Monday -- the 17th, not yesterday -- I wrote about the harness at system scale: that the layer you actually own is the tools, the permissions, the sandbox and the deny rule, and that it is smaller than most people think. This is the same argument at desk scale, on a Tuesday, for one person with one agent and an hour to spare. Same idea, much smaller room.

## Four rungs, and where each one's mistakes end up

**Read-only.** It can look at everything and change nothing. Almost all of the value of an agent's first week lives on this rung, and almost nobody spends a week here. Point it at a codebase you inherited and ask it what the deployment path is. Point it at a contract and ask what the termination provisions actually say. Point it at last quarter's incidents and ask what they have in common. Every one of those is genuinely useful, and the worst case is that it is wrong and you notice.

**Write, but to a scratch space.** Now it can produce something. In a place where wrong output costs nothing -- a branch nobody merges, a folder nobody reads, a copy of the spreadsheet rather than the spreadsheet. The value of this rung is that you find out what its output actually looks like at volume, which is a different question from whether one sample impressed you.

**Write to the real thing.** Now a mistake is a mistake. This is the rung where you need the habit I wrote about last week -- knowing in advance what would count as the work being right -- because from here on you are the only thing between its output and somebody else's Monday.

**Act outward.** Send, pay, post, provision, deploy. The rung where a mistake stops being yours and becomes somebody else's problem, usually a customer's. Very little needs to live here. A surprising amount of software will put you here by default if you accept the setup screen without reading it.

The rungs are not a maturity model and I am not going to draw you a diagram. They are four different sizes of blast radius, and the only real question is whether you know which one you are standing on right now. Most people cannot answer that about the agent they used this morning.

<!-- [YOUR TAKE]: The lightest and best spot for you, and this is the piece's ground truth. Which rung are your own agents actually on -- at Player Elite and in your own writing pipeline? The honest answer is more useful than the prescription, especially if it is "higher than I would recommend to somebody else, and here is why I made that trade." Your onboarding experience is the other half: you have hired and onboarded real people, so the new-hire ladder above is yours to make specific. A first-person "I skipped straight to the top rung and here is what it cost me" would land harder than anything else in the piece. -->

## Her other rule, the one that does not go on a slide

The clearest version of this practice I have found belongs to Allie K. Miller, who writes and speaks about applied AI for a very large audience and runs a lot of agents in her own work. Her rule, in her own words, is about as plain as advice gets:

> "You're not going to give it email access... start with read-only access and then earn trust, figure out what is working."

*Earn trust.* Not "assess risk," not "conduct an evaluation." The same phrase you would use about a person, and used deliberately.

Her second rule gets quoted far less often, and I think that is because it is not aspirational enough to put on a slide:

> "Sometimes these things don't work... you just kind of have to say, 'Okay, it's broken now. I'll come back to it in an hour.'"

No recovery architecture. No incident process. No framework. She tolerates the breakage, because she has arranged things so that breakage is affordable. That is the whole trick, and it is worth more than any diagram: the reason she can be relaxed about an agent falling over is that she never put it somewhere where falling over is expensive.

Which is the optimistic reading of this entire subject, and I think it is the correct one. The reason to start read-only is not that agents are dangerous. It is that starting read-only is what lets you stop worrying about them.

## Write down what has to be true

Here is the one piece of process, and it is a sentence, not a program.

**Before you promote an agent a rung, write down what had to be true for it to earn that.** Not a feeling. Not "it's been good lately." A specific thing you looked at: *it summarized eleven incident reports and I checked four of them line by line and it got all four right.* Then promote it.

**Then write down what would send it back down.** This is the half everybody skips, and it is the half that matters when you are tired. Deciding in advance what a demotion looks like means you will actually do it, instead of explaining to yourself at 6pm on a Thursday why this particular failure was an exception.

**And do it per task, not per agent.** The same agent can sit on the top rung for drafting and the bottom rung for anything that touches a customer. We do this with people without thinking about it -- the new analyst who is trusted completely with the model and not at all with the client call. There is no reason to be less nuanced with software than we are with each other.

Note what this is not. Yesterday's piece was about making sure your agents' *instructions* can all be true at once. This is a different axis entirely: not what you told it, but how much of the world it can reach. You can get the instructions perfect and still hand the thing far more reach than the job needs.

## What to do tonight

Pick one agent you actually use. Not a hypothetical -- one you used this week.

Work out what it can currently see and what it can currently change. That will take you about ten minutes and it is very likely to surprise you, because for most people the answer is "whatever the default was." Then ask whether the last three things you actually asked it to do needed that much reach. If they did not, turn something off and see whether you miss it.

That is the whole exercise. You will either discover that you are over-provisioned, which you can fix in about a minute, or you will discover that you are exactly where you should be, which is worth knowing too. Either way you will be able to answer the question that almost nobody can answer right now, which is a good place to be standing on a Tuesday.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that the first decision about an agent is what it can see rather than what it can do, that four rungs of access map to four sizes of mistake, and that starting read-only is what lets you stop worrying about the thing.*
