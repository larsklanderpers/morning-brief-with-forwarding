**Status: DRAFT rv1 -- written for Sat 24 Oct 2026; he is finishing it 28 Oct (publish date his call). His Google Doc pass is ahead of this file once it starts. Drafted 23 Oct evening, on his word (Duet + Projects, Grok Bot between, personal-agent story). Not panelled. Not scheduled.**
<!--
DRAFT v1. SATURDAY DIVERSION (what it does for you). Independent of any arc. The 19-25 Oct spine was shifted to 26 Oct - 1 Nov on his word 23 Oct; this is the only piece for the 19 Oct week after Sun 18.
GATE: PASS (re-run 23 Oct). Human feature: his own three-agent stack -- Duet for the house and the small business, Grok Bot for the standing staff, Projects in Claude Code for the code -- with what each costs and what each will not do. Actions are try/install/brief, not audits. Watches: survey drift (kept to his stack, one section each, no spec tables); Straiker incident left OUT.
RESEARCH: References\research_sat24-duet-projects-grok_2026-10-23.md (primaries read 23 Oct).
HIS FACTS (23 Oct, chat): still on the Duet waitlist despite a Max account for over a year; on Cursor Pro pricing "at $100/month I think"; has run the new Projects and will write that section himself (drafting block left); small-business leg = his own business; still runs a COS bot plus child bots, now TWO COS bots (one for coding tasks and PRs, one for everything else), both talk to Freya ("my Chat Dot"), both talk to other bots in the business through a Slack-GitHub repo control plane whose primary communicator is the design team bot.
HIS RULINGS 28 Oct: (1) "Freya" confirmed (his ChatGPT dot). (2) He is on the $30 Premium tier (not Cursor $100); text updated. (3) Sat 10's child-bots promise: touched, NOT paid; the piece says so. (4) CORRECTION FORWARD for Sat 12 Sep's "twenty dollars a month" is in the Grok section, per standing rule 4.
OPEN: [YOUR TAKE] x3 + 1 [DRAFTING BLOCK] (Projects).
WINDOW AVOIDED: Sat 17 shoebox/accountant; Sun 18 bowl/porch/levers; Wed (deferred) house-sitter/keys/keyring; Thu (deferred) drugstore photo counter; Tue (deferred) head chef; Thu 8 room/hotel/hostel; Sun 11 "desks"; "approved", "delegate", "for free", "unmetered", "lever", "the gap", "reach", "downstream", "load-bearing". Controlling image: the band (music; not film/TV). Check: "band" not in recent window.
-->

# A Duet, and the Rest of the Band

*Anthropic launched an always-on personal agent last week. It is good news for a small business, and it walks into a stack that already has players in it.*

Anthropic named its new agent after a piece of music for two. That is a fair description of how it starts, and not quite how it ends up.

A duet is you and one other voice, trading lines, each listening to the other. It is a lovely format, and it is also not how most working music actually gets made. Once there is more than one song a night, you have a band: somebody keeping time at the back, somebody carrying the melody, somebody who only comes in for the solo, and one person at the front counting everyone in and deciding what comes next. Nobody in a good band plays every part. The skill is in who plays which part, and in everyone being able to hear each other.

Claude Duet, which Anthropic announced on 21 October, is a very good singer. It is also joining a stage where a lot of us already have a band playing, and the useful question for this weekend is not "should I get it" but "which part does it take".

So today is a check-in on three of them, in the order they matter to me: Duet for the personal and the small-business side, Grok Bot for the standing staff that runs in the background, and Projects in Claude Code for the developer side. What each one is, what it costs, what it will not do, and how mine talk to each other.

One confession before we start. I have had a Max account (the top tier of Claude's consumer plans) for over a year, and I am still on the Duet waitlist like everyone else. So the Duet section is what the thing is and what I am going to hand it first, and the other two are what I actually run.

## The one I am still waiting for

Anthropic's own description is simple: Duet is "a new app where Claude works as a proactive agent," and "we built Claude Duet for professionals and small business owners with more on their plates than they can track." It is a standalone app on iOS and Android, and on claude.ai.

The parts that make it different from the Claude you already chat with:

It runs on "a virtual machine with its own browser, so it doesn't require your laptop or phone to be on." Each morning "it sends you a short brief on the most important items across your connected apps," and it "checks your connected accounts every few hours, because checking nonstop would use up your plan's limits much faster." (I like that they said the quiet part out loud. Background work still costs something, and they are pacing it.) It also "carries over your memory, skills, and connected apps from your Claude account," so it does not start from scratch.

The connectors at launch are Gmail, Google Calendar, Google Drive, Slack, QuickBooks, HubSpot, Docusign and Calendly, with purchases going through Stripe, Link or Shop Pay on "a one-time card that only works for that purchase." For my Microsoft-shop friends, the help page is blunt: "Microsoft 365 isn't available yet."

Anthropic's own small-business examples are the giveaway for who this is really for: check QuickBooks or Stripe "for unpaid invoices and draft reminders," "prepare and run payroll in Gusto," chase HubSpot follow-ups, send Docusign agreements. One of its named testers is a restaurant group with "about 110 employees" using it for "accounting, customer support, and marketing." That is not a developer toy. That is the back office of a small company.

**The never list is the feature.** Before it "sends a message, makes a payment, signs a document, or deletes anything, it shows you exactly what it's about to do and waits for your approval." Fine, every agent says something like that. The part I would actually build a small business on is the next bit: "Some actions are off-limits even with your approval, such as trading securities, moving money between accounts, or accessing someone else's account." And it is "instructed never to share" sign-in credentials, full card and bank account numbers, or government ID numbers, "even if you ask."

Read that again, because it is unusual. A yes button gets pressed at 11pm by someone who wants to go to bed. A capability that is not there cannot be talked into anything, by you, by a distracted bookkeeper, or by a cleverly worded email it reads at 6am. For a small business, where the person saying yes is usually also the person doing four other jobs, that is worth more than any feature on the list.

It also has limits worth knowing before you get excited. "You can't choose a model." "You can't watch Claude Duet work in its browser or take over the browser." It "doesn't make phone calls or send text messages to other people," it "can't see all of your projects or the files on your computer," and Anthropic itself says personal errands, like booking tickets, "aren't quite as strong." The 1Password sign-in that got announced alongside it (where the agent asks for a saved login, you say yes on your own device, and the password goes to the browser without ever passing through the model) is "coming soon," not live.

**What it costs.** During the research preview it is "included with the Pro and Max plans at no extra cost," US only, through a waitlist, and not on Team or Enterprise yet. It uses your plan's usage limits, and "work it does in the background, like the morning brief and check-ins, also counts, so you may reach your limits sooner." New users get "one full limit reset," good until 30 November. So the honest price is: twenty dollars a month on Pro if you already pay it, and the real cost is how much of your allowance you are willing to let it spend while you sleep.

<!-- [YOUR TAKE]: the first three things you will hand Duet in your own business when the invite lands, and why those. (Invoices? Follow-ups? The morning brief across Gmail and Slack?) And one thing you would never give it, even with the never list. Customer names only with your word. -->

If you are on the list too, here is where I would start, using Anthropic's own suggestions as the floor:

```
Every morning, tell me the five things in my inbox and calendar that actually need me today, and draft replies for the two that are just waiting on a yes or no. Do not send anything.
```

```
Check Stripe for unpaid invoices older than 14 days and draft a polite reminder for each one for me to review. Group them by customer and show me the total outstanding.
```

## The staff in the background

Duet is the singer. Grok Bot, in my house, is the rhythm section: the part you stop noticing because it is always there.

I wrote about Grok Bot at length on 12 September, and the first thing to do is correct forward on price, because it changed. On 12 October the company behind it (the x.ai pages now carry the SpaceXSI name, since xAI joined SpaceX in February) folded Grok, Grok Bot, Cursor and X Premium into one plan called the X Subscription. The tiers are Free, Plus at $8, Premium at $30, Super at $100 and Ultra at $200, and "Grok Bot is included with Premium, Super, Ultra, Teams, and Enterprise." So the "about twenty dollars a month" I printed in September is now **thirty dollars a month** for anyone signing up fresh. If you were already on SuperGrok, Cursor or X Premium, "nothing changes." Usage is a shared pool that "covers Chat, Imagine, Voice, and Bot," refreshing weekly, with top-ups billed at token cost.

I am on the $30 Premium tier myself, so that is the real number, for me and for anyone signing up today.

The architecture has not changed, and it is still the reason I use it. Each Bot is a standing agent on a cloud computer ("Every Grok Bot shares one persistent cloud computer," with isolation "per user, not per Grok Bot"), and xAI describes exactly the shape I run: "A chief of staff sits on top, with a specialist for each lane." Routines give a Bot "a standing responsibility that runs on a schedule or in response to an event." There is a practical ceiling of "roughly 50 Bots per account and six per group chat," which, at thirty-something bots, I can see from here.

Here is how mine has grown since September. I still run a chief-of-staff bot with child bots underneath it, and Jev still sits in front of the inbox. But I now have **two** chiefs of staff: one for coding tasks, pull requests and everything that touches a repo, and one for everything else. Both of them talk to Freya, my ChatGPT dot (OpenAI's always-on agent). And both of them talk to the other bots in the business through a control plane built on Slack and a GitHub repository, where the busiest voice on the line is not either chief of staff. It is the design team bot.

<!-- [YOUR TAKE]: why two chiefs of staff instead of one -- what broke, or got crowded, with one. And why the design team bot ended up being the main voice on the Slack/GitHub plane. This is the part of the piece only you can write. -->

I promised on 10 October that we would have the whole conversation about child bots versus bots you talk to directly on a coming Saturday. This is not that piece; it is the floor plan. That one still owes you the why.

If you want to try the shape without building thirty of anything:

```
You are my chief of staff. Each morning at 7, read my inbox and calendar, and hand anything about invoices to the Finance bot and anything about scheduling to the Calendar bot. Post a three-line summary of what you handed to whom in our group chat. Do not reply to anyone outside the business without asking me.
```

## The one that writes the code

The third part of the band is the one that only comes in for the solo, and on a development team, the solo is most of the set.

First, a naming trap, because Anthropic has made one. There are now two things called Projects. The classic one, in the regular Claude chat, is still essentially a folder: instructions and files that every conversation in it can see. The new one, which launched in beta on 17 September, lives in **Claude Code** (at claude.ai/code, in the desktop app and in the mobile app, but "not in the terminal CLI, the VS Code extension, or the JetBrains plugin"), and it is a different animal. When I say Projects for the rest of this section, I mean the new one.

Anthropic describes it as "one ongoing conversation where Claude coordinates a stream of related work," which "starts a thread for each task." The threads run in the cloud, and "cloud threads keep going after you close your laptop." A thread can watch a pull request "with auto-fix turned on," which means it "pushes fixes when CI fails, addresses review comments." You can schedule work that runs as threads in the project, and you can now push a thread down to your own machine if it needs something local. New projects run every thread on Opus at high effort by default.

A project carries your repositories, files, instructions (up to 16,000 characters), its own memory file, and the `CLAUDE.md` from each repository (the plain text file of standing instructions Claude reads at the start of every session). And then, in the line that made me laugh out loud, Anthropic tells you to "brief Claude in the project the way you'd brief a chief of staff." Everybody, it seems, has landed on the same org chart.

The limits: GitHub.com only (not GitHub Enterprise Server, GitLab or Bitbucket), 200 new threads a day, Pro and Max plans only, and "A project belongs to one user. You can't share a project." It counts against the same plan limits as everything else, and "on a Pro plan in particular you should expect to reach your limit sooner." Anthropic is also honest about the obvious weakness of running lots of threads on one codebase: when two of them touch the same code, "the overlap is resolved as a merge conflict just like any other PR."

<!-- [DRAFTING BLOCK -- LARS]: what you have run in a new Project, on which repo, and what actually happened. Suggested beats, use or ignore: what you briefed it with; what a thread did while the laptop was closed; the first PR it fixed on its own (CI or review comments); where it went wrong, or where two threads collided; how it relates to your coding chief-of-staff bot on Grok (does one hand to the other, or do they split the work?). -->

A starter brief, close to the shape of Anthropic's own sample:

```
This project covers [repos]. Goal: [one sentence]. Start a thread per repo. In every thread, run the tests and the linter before opening a PR, and watch the PR until CI is green. Do not merge, force-push, or change CI configuration without asking me. Post a short daily note of what each thread did.
```

## How the band hears itself

Put the three side by side and the first thing you notice is how much they have converged. All three are always-on agents on someone else's cloud machine. All three sell the same org chart, a chief of staff over specialists. And all three pay for their background work out of the same pool you use for everything else, which is the economics line nobody puts on the launch page: Duet is no extra cost on Pro or Max, Projects is no extra cost on Pro or Max, Grok Bot starts at $30 for a new subscriber, and in every case the agent that works while you sleep is drawing down the allowance you will want on Monday morning.

The second thing you notice is that none of them talks to the others out of the box. Duet will not take a hand-off from a Grok bot. A Grok bot cannot open a Claude Code thread. A Project cannot be shared, even with another agent of yours. What all three can get at, one way or another, is Slack and GitHub: Duet has a Slack connector (with limits), Grok's team bots get their own Slack handles and work in GitHub, and Projects lives on GitHub repositories. Which is, not by accident, what my control plane is built on. If you want your agents to be a band rather than three soloists playing different songs, give them one place where they can all hear the count.

And the third thing is where each one should sit. Duet is the voice you talk to and the one that touches your customers' inboxes and your invoices, so it is the one with the never list, and it should be. Grok, for me, is the standing staff, many small bots doing one job each, mostly unwatched. Projects is the one you point at a codebase and leave running overnight. They are not competing for the same part.

## This weekend

**Get on the list, and pick the first chore.** Join the Duet waitlist with the email on your Claude account and, when it asks, say what you would hand off first. Pick something boring and frequent, like invoice reminders or the morning inbox sweep, so you can tell within a week whether it is earning its keep.

**Give one bot one routine.** If you have Grok Bot (or any agent with a scheduler), give exactly one bot one standing job on a schedule, and have it post what it did somewhere you will see it. One job, one bot, one place to read the result. Add the second only when the first has been boring for a week.

**Brief one Project as if it were a new hire.** If you write code and you are on Pro or Max, open a new Project in Claude Code against one repository, write the brief you would give a capable contractor on day one (what the goal is, what to run before every PR, what never to touch), and let one thread run while you go do something else.

**Choose where they meet.** Before you add a third agent, decide where they will all report: a Slack channel, a repository, a shared document. It matters less which one you pick than that there is exactly one.

## Counting it in

A year ago the choice was which assistant to use. Now the choice is which part each one plays, and who counts everyone in, and that is a much better problem to have.

Duet is a good singer, and for a small business the never list may be the best thing about it. Just make sure, when it finally lets you in, that it joins the band rather than starting a second one.

---

**Addendum: the prompts, if you want to start from mine.**

*Duet, the morning sweep:*

```
Every morning, tell me the five things in my inbox and calendar that actually need me today, and draft replies for the two that are just waiting on a yes or no. Do not send anything.
```

*Duet, the invoice chase:*

```
Check Stripe for unpaid invoices older than 14 days and draft a polite reminder for each one for me to review. Group them by customer and show me the total outstanding.
```

*Duet, the meeting brief (Anthropic's own example, lightly extended):*

```
Pull together a one-page brief on [company] before my [time] meeting: what they do, anything in my email or Drive about them, and the last thing either of us promised the other.
```

*Grok Bot, a chief of staff with two specialists:*

```
You are my chief of staff. Each morning at 7, read my inbox and calendar, and hand anything about invoices to the Finance bot and anything about scheduling to the Calendar bot. Post a three-line summary of what you handed to whom in our group chat. Do not reply to anyone outside the business without asking me.
```

*Grok Bot, one routine:*

```
Every weekday at 4pm, check [source] for [the one thing you care about], and post a two-line note in [channel]: what changed today, and whether anything needs me. If nothing changed, say so in one line.
```

*Projects in Claude Code, the starter brief:*

```
This project covers [repos]. Goal: [one sentence]. Start a thread per repo. In every thread, run the tests and the linter before opening a PR, and watch the PR until CI is green. Do not merge, force-push, or change CI configuration without asking me. Post a short daily note of what each thread did.
```

*The meeting place, for any of them:*

```
When you finish a task, post one line in [channel or repo file]: what you did, what you handed to another agent and which one, and anything waiting on me. Read the same place before you start, and do not redo anything another agent has already marked done.
```

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about AI governance (often), AI methodologies (also often), cybersecurity strategy (sometimes), and technology risk (always). Today's argument is that the new always-on agents are converging on the same shape, so the useful decision is no longer which one to use but which part each one plays in your stack and where they all meet, with Claude Duet's hard never list making it the right voice for a small business's money and inbox.*
