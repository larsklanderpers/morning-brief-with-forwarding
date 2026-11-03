<!--
STATUS: v1, drafter only. Thu 8 Oct 2026 · AI growth · DELEGATED AUTHORITY arc, Thursday leg (feeds Sun 11 pt 3: onboarding is a manager's act).
Plan: References\week-plan_2026-10-05.md (Thu 8 block). Research: References\research_thu08-its-own-computer_2026-10-08.md (its DO-NOT-PRINT list binds).
RE-ANGLED on his word 7 Oct ("i like the plan. do it"): the up-side sequel to Sat 12 *Nine Bots and One Computer*. Working title "Its Own Computer" dropped because it restates the Grok Bot claim he took apart on 12 Sep. Title is his call.
OPEN FOR HIM: [YOUR TAKE] x2 -- (1) his dot test, 8 Oct: one machine per dot or one per account; (2) a role he has seen form around an agent.
OWED 8 OCT MORNING: Microsoft 7 Oct event re-sweep (one paragraph at most; correct Thu 1 forward if needed). Slot marked below.
Drafter choices for his review: hostel/hotel opener (not family -- Wed 7 and Tue 6 both opened at home; not historical; NOT bookended at the close); "delegate"/"contractor" vocabulary left to Wed 7 and Sunday; Decisions API left to Sat 10; Pro 500 left to Fri 9.
Not paneled.
-->

# A Room of Its Own

*OpenAI says its new agents each get a computer of their own. A month ago, that same promise from another vendor turned out to be a shared one.*

OpenAI says every one of its new agents gets a computer of its own. A month ago, another vendor made the same promise, and it did not hold up.

Think about the difference between a hostel and a hotel. In a hostel you get your own bunk, maybe a locker with a padlock, and you share the room with five strangers. Your stuff is yours right up until someone decides the padlock is optional. In a hotel you get a door, and the door has a lock, and the only people on the other side of it are you and whoever you let in. Both of them give you a bed for the night, and both of them will cheerfully describe it as "your room." Only one of them actually means it.

That distinction matters more than it sounds, and the hopeful version of it is the better story, because if the hotel is real, it changes what you can hand an agent. Not a task. A job.

## The hostel

On 12 September I wrote about Grok Bot, xAI's product for running a small fleet of named agents. xAI's own documentation carried the contradiction on a single page: a bullet headed *"Each Bot has a computer,"* sitting above a section headed *"Your Bots share one computer."* The second one was the truth. Your account gets one virtual computer (a machine that exists only in somebody's data center, rented by the hour), and every bot you create lives inside it.

That matters for a reason that has nothing to do with performance. If nine bots share one machine, then the files, the browser sessions and the logins that one of them can reach are, in practice, reachable by all nine. The boundary between them is good behavior, and nothing else. One bot's access is every bot's access. That is a hostel.

I did not think that made Grok Bot useless, and I still do not. I run it. But it shaped what I was willing to give it, which was errands, not responsibilities.

## The hotel, by OpenAI's own account

On 29 September, at its developer conference, OpenAI launched dots: always-on agents that sit inside ChatGPT and keep working after you close the app. The launch page is direct about where they live. In OpenAI's words, dots *"have their own cloud computer, learn from feedback over time, and can work towards your goals 24/7,"* and *"each dot works on its own cloud computer, while your computer and its contents stay separate unless you choose to connect it."*

That is a hotel claim. It says two things at once: the dot has a machine, and your laptop is not that machine.

The rest of the launch fills in the room. A dot can reach *"over 4,000 apps"* through OpenAI's plugins, which is OpenAI's word for connectors into the tools you already use. You can talk to it in ChatGPT, on a voice call, or in Slack and Microsoft Teams. OpenAI says the dot runs an automatic review over consequential actions, that its monitoring can *"pause or stop the dot's work,"* and that *"certain sensitive tasks, such as changing a password, always stay with you."* For business accounts, VentureBeat reports that admins can write rules that permit an action, require approval for it, or prohibit it outright, and can watch the dot's background work as it happens.

Now, the caveat, because after September I am not taking anyone's word for "its own" on a product page. Nothing OpenAI has published says whether two dots on the same account get two machines or share one. The launch page says each dot works on its own cloud computer; that is the claim, and it is OpenAI's. The people writing the early explainers are working from the same page, and at least one of them says plainly that he has not had access to a dot yet.

<!-- [YOUR TAKE]: his dot test, 8 Oct. What did he find -- one machine per dot, or one per account? How could he tell (the equivalent of the Grok Bot security logs)? This is the paragraph that decides whether the piece lands "hotel" or "hostel with nicer furniture". If the test is inconclusive, say so; that is a finding too. -->

## A task, then a job

So suppose the hotel is real. Why does a room of its own matter so much?

Because a task is something you hand over and wait for, and a job is something that keeps going when you are not looking. Everything that makes a job possible needs somewhere to live in between. A dot that is watching your pipeline for a customer who has gone quiet, or keeping a project page current as plans change, or chasing the three people who still owe you a sign-off, needs to hold onto files, keep a browser session open, remember where it got to, and pick up again at two in the morning without your laptop being awake. A chat window cannot do that. A machine can.

OpenAI is building around exactly that idea. Alongside dots it launched ChatGPT Space, a shared workspace for teams, and its description of how the two fit is telling: *"Dots work natively across files in Space. Wherever you work with your dot -- in ChatGPT, Slack, or Microsoft Teams -- you can also ask it to keep the page up to date as plans change."* That is not a person asking a question and getting an answer. That is a standing responsibility, and it only works if the thing holding it has its own place to keep its work.

Brian Chesky (Airbnb's co-founder and CEO, for those of you who have only met the company through a booking) made the same point from the other direction in an interview with TechCrunch last week, arguing that the industry still lacks *"a true operating system built for AI,"* one where AI sits *"at the kernel level"* (the core of the operating system) and agents interact with each other there. He is talking about the next layer up from where OpenAI is today. But the direction is the same: the agent is moving out of the chat box and into somewhere it can live.

And the economics are the part that makes this a growth story rather than a curiosity. OpenAI says *"your first dot is included in your Pro or Business Premium plan at no extra cost."* Pro is the $200-a-month individual plan. So for anyone already on one of those plans, a standing machine with a browser, a file system and connections into thousands of apps costs nothing extra this month. OpenAI has not published what a second dot costs, or how much heavy work the included one gets before you hit a limit, and that is worth watching. But the entry price for giving software a job, rather than a task, just went to the price of a subscription a lot of people already pay.

A note for my friends outside the US. OpenAI has told reporters that *"for Pro users, the eligible markets do not currently include the European Economic Area, Switzerland or the UK."* That exclusion is for the individual Pro plan; according to The Next Web, Business Premium accounts get dots in every region ChatGPT supports. OpenAI has not said why, so I will not guess on its behalf. For my Australian readers: Australia is not on that list, which means your staff can switch one on today.

<!-- MICROSOFT 7 OCT SLOT: re-sweep the morning of 8 Oct. One paragraph at most, only if the event put agents on a machine of their own in Windows (the previews pointed at local agents in the OS). If it changes anything Thu 1 printed, correct forward here in one sentence. Cut this slot if nothing landed. -->

## The person who keeps it right

Every one of these creates a job for a human too, and I think it is a good one.

Nufar Gaspar (a consultant who helps companies set up shared agents across teams) put it bluntly on The AI Daily Brief on 29 September. One of her signs that a team is not ready for a shared agent is that *"nobody will own and maintain the knowledge (the agent drifts within weeks, sometimes days)."* Turn that around and you have a job description. Somebody has to keep the agent's instructions current, notice when its answers start to wander, decide what it is allowed to touch, and be the name people go to when it gets something wrong.

Harvard Business Review gave that person a title back in February. In a piece called *"To Thrive in the AI Era, Companies Need Agent Managers,"* Suraj Srinivasan and Vivienne Wei describe the role as part product manager, part operations lead: watching how agents perform, overseeing how they learn, and making sure people and agents work safely together. Their example is Zach Stauber, a support agent manager at Salesforce, who describes his day this way: *"I start and end my day in dashboards, scorecards, and agent observability monitoring"* (observability meaning the tooling that shows you what a system actually did, not what it was supposed to do).

The internet is already full of headlines about "the fastest-growing job title of 2026," and I could not find a single number behind any of them. I have not found anyone actually counting these roles yet. What I can tell you is that the shape is consistent wherever I look, and that the most reachable version of it does not start with a new hire. It starts inside a job somebody already has. The operations lead who owns the support agent. The analyst who keeps the pricing agent honest. The executive assistant who knows which of the boss's dots is allowed to send email and which one is not.

<!-- [YOUR TAKE]: a role he has seen form around an agent, in his own team or a client's, or the one he would hire for first. The insider "we" view belongs here if he has it. -->

That is the up side of the hotel. A machine of its own means the agent can carry a job, and a job needs a person who looks after it. Those are good jobs, and most of them will go to people who are already in the building.

## Before it moves in

If you are going to give an agent a room, there are a few things worth doing before it unpacks.

**Ask which room it is in.** Before you connect a dot, or any agent that claims a machine of its own, find out whether "its own" means one machine per agent or one per account. If the vendor will not say, assume the hostel, and decide what you connect on that basis. The answer changes what is safe to hand over, and it is a fair question to ask anyone selling you a coworker.

**Name the person who keeps it right before you switch it on.** Not after it drifts. Gaspar's test is the cheapest piece of governance on offer: if you cannot write down a name next to the agent, it is not ready to run unattended. That name is also the first thing anyone should read when they wonder why the agent did something.

**Set the rules where the apps are.** On business accounts, the controls for what a dot may do (permit, ask first, or never) sit with the same admin controls that already decide which apps your people can use. Use them. Start with read-only access to the things it needs to watch, and let it earn write access one app at a time.

**Give it one job, not ten.** A dot with a clear standing responsibility is easy to judge. A dot with ten vague ones is impossible to judge, and the person who owns it will not be able to tell you whether it is working.

None of that is exotic. It is what you would do for anyone who was about to get a key to the building and a login to everything, and on Sunday I will come back to why that is exactly the point.

## A job needs a home

The agent is getting a place to live, and that is what turns software that answers into software that carries something for you. If OpenAI's room is really its own, a lot of work that used to need a person checking in every few hours can now just keep going.

But the room is the claim, and the person who keeps it right is the condition. Find out which kind of room you are buying, put a name next to it, and then go give it a job.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that an agent with a computer of its own can carry a job rather than a task, but only once you know whose computer it really is and whose name sits next to it.*
