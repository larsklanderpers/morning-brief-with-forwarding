<!--
STATUS: rv2 = rv1 (his Drive pass + mechanics) + his five rulings of 8 Oct 00:23 PT applied.
RULINGS APPLIED: (1) two-dots line corrected to OpenAI's "in the future"; (2) Grok Bot "this week" -> "in the last few weeks"; (3) Gaspar bracket moved out of the quote into a restatement; (4) guess reworded as a stated guess; (5) Microsoft / specialist dots sentence added to "Set the rules". (6) Grok Bot secrets disclosure stays public on his word: "there is no good alternative for some secrets yet." Thu 8 Oct 2026 · AI growth · DELEGATED AUTHORITY arc, Thursday leg.
Plan: References\week-plan_2026-10-05.md. Research: References\research_thu08-its-own-computer_2026-10-08.md (DO-NOT-PRINT binds).
Mechanics applied silently: en-dashes -> "--"; its -> it's (x2); GPDR -> GDPR; "comfortable" -> "comfortable with,"; closed the open parenthesis after Astra.
Accuracy fix applied (draft, GREEN): "GPT Astra" -> "GPT-6 Astra" (OpenAI's launch page).
[YOUR TAKE] 2 (role he has seen form) DELETED by him: respected, not restored.
Not paneled.
-->

# A Room of Its Own

*OpenAI says its new agents each get a computer of their own. A month ago, that same promise from another vendor turned out to be a shared one.*

OpenAI says every one of its new agents (from its new "dots" product) gets a computer of its own. A month ago, another vendor made the same promise, and it did not hold up.

Think about the difference between a hostel and a hotel. In a hostel you get your own bunk, maybe a locker with a padlock, and you share the room with five strangers. Your stuff is yours right up until someone decides the padlock is optional. In a hotel you get a door, and the door has a lock, and the only people on the other side of it are you and whoever you let in. Both of them give you a bed for the night, and both of them will cheerfully describe it as "your room." Only one of them actually means it.

That distinction matters more than it sounds, and the hopeful version of it is the better story, because if the hotel is real, it changes what you can hand an agent. Not a task. A job.

## The hostel

On 12 September I wrote about Grok Bot, xAI's product for running a small fleet of named agents. xAI's own documentation carried the contradiction on a single page: a bullet headed *"Each Bot has a computer,"* sitting above a section headed *"Your Bots share one computer."* The second one was the truth. Your account gets one virtual computer (a machine that exists only in somebody's data center, rented by the hour), and every bot you create lives inside it.

That matters for a reason that has nothing to do with performance. If nine bots share one machine, then the files, the browser sessions and the logins that one of them can reach are, in practice, reachable by all nine. The boundary between them is good behavior, and nothing else. One bot's access is every bot's access. That is a hostel.

I did not think that made Grok Bot useless, and I still do not. I run it. I have secrets stored on the shared computer that I am not completely comfortable with, but I have made the considered decision not to do certain, specific things with Grok Bot because the secrets I was particularly conscious about I was entirely unwilling to put onto that shared virtual desktop. So, by its very nature of the design, it shaped what I was willing to give it, which was errands, and things I would trust a junior engineer with, not responsibilities I would have to a tech lead.

## The hotel, by OpenAI's own account

On 29 September, at its developer conference, OpenAI launched dots: always-on agents that sit inside ChatGPT and keep working after you close the app. The launch page is direct about where they live. In OpenAI's words, dots *"have their own cloud computer, learn from feedback over time, and can work towards your goals 24/7,"* and *"each dot works on its own cloud computer, while your computer and its contents stay separate unless you choose to connect it."*

That is a hotel claim. It says two things at once: the dot has a machine, and your laptop is not that machine.

The rest of the launch fills in the room. A dot can reach *"over 4,000 apps"* through OpenAI's plugins, which is OpenAI's word for connectors into the tools you already use. You can talk to it in ChatGPT, on a voice call, or in Slack and Microsoft Teams. OpenAI says the dot runs an automatic review over consequential actions, that its monitoring can *"pause or stop the dot's work,"* and that *"certain sensitive tasks, such as changing a password, always stay with you."* For business accounts, VentureBeat reports that admins can write rules that permit an action, require approval for it, or prohibit it outright, and can watch the dot's background work as it happens (yes, governance in place, natively, for business accounts -- so maybe they are starting to get their arms around that a bit).

Now, the caveat, because after September I am not taking anyone's word for "its own" on a product page. Nothing OpenAI has published says whether two dots on the same account get two machines or share one (though, in fairness, OpenAI says only that more dots are coming *"in the future,"* with no date attached, so that's still a bit of gray area, to be sure). The launch page says each dot works on its own cloud computer; that is the claim, and it is OpenAI's. The people writing the early explainers are working from the same page, and at least one of them says plainly that he has not had access to a dot yet.

That said, I made my own dot today. It was pretty easy and seamless. I tend to name my senior agents after goddesses (it makes it easy for me to remember who I am talking to, and since they ultimately all share a control surface, it makes it easier for me to address responses properly), so once she was up and running, I started asking some questions. Sadly, she couldn't answer any of them, and so I was ultimately unable to confirm the single computer/multi-computer model; however, she did confirm that at present there is no way to spin up a second dot, so I would guess in my case, at least, the question is academic.

## A task, then a job

So suppose the hotel is real. Why does a room of its own matter so much?

Because a task is something you hand over and wait for (and while this is fine for limited use cases, at scale, it's a whole different animal), and a job is something that keeps going when you are not looking -- and probably repeats itself multiple times, handles different inputs and outputs, and more. Everything that makes a job possible needs somewhere to live in between. A dot that is watching your pipeline for a customer who has gone quiet, or keeping a project page current as plans change, or chasing the three people who still owe you a sign-off, needs to hold onto files, keep a browser session open, remember where it got to, and pick up again at two in the morning without your laptop being awake. A chat window cannot do that. A machine can.

OpenAI is building around exactly that idea. Alongside dots it launched ChatGPT Space, a shared workspace for teams, and its description of how the two fit is telling: *"Dots work natively across files in Space. Wherever you work with your dot -- in ChatGPT, Slack, or Microsoft Teams -- you can also ask it to keep the page up to date as plans change."* That is not a person asking a question and getting an answer. That is a standing responsibility, and it only works if the thing holding it has its own place to keep its work. (I will note, in the interest of completeness, that Grok Bot in the last few weeks added working on your local computer to its list of items it supports, and also introduced the concept of Team Bots, which is similar to the premise of dots+Space. While both important expansions, the standard bot still shares a single virtual machine with the rest of the fleet.)

Brian Chesky (Airbnb's co-founder and CEO, for those of you who have only met the company through a booking and don't live in the tech space) made the same point from the other direction in an interview with TechCrunch last week, arguing that the industry still lacks *"a true operating system built for AI,"* one where AI sits *"at the kernel level"* (the core of the operating system) and agents interact with each other there. He is talking about the next layer up from where OpenAI is today. But the direction is the same: the agent is moving out of the chat box and into somewhere it can live, and perform tasks indefinitely, with only minimal human interaction.

And the economics are the part that makes this a growth story rather than a curiosity. OpenAI says *"your first dot is included in your Pro or Business Premium plan at no extra cost."* Pro is the $200-a-month individual plan. So for anyone already on one of those plans, a standing machine with a browser, a file system and connections into thousands of apps costs nothing extra this month. OpenAI has not published what a second dot costs, or how much heavy work the included one gets before you hit a limit, and that is worth watching (though they have published that dots use GPT-6 Astra as their "powered by" model). But the entry price for giving software a job, rather than a task, just went to the price of a subscription a lot of people already pay.

A note for my friends outside the US. OpenAI has told reporters that *"for Pro users, the eligible markets do not currently include the European Economic Area, Switzerland or the UK."* That exclusion is for the individual Pro plan; according to The Next Web, Business Premium accounts get dots in every region ChatGPT supports. OpenAI has not said why. My guess is that it is a GDPR compliance or AI Act compliance issue. For my Australian readers: Australia is not on that list, which means your staff can switch one on today.

## The person who keeps it right

Every one of these creates a job for a human too, and I think it is a good one.

Nufar Gaspar (a consultant who helps companies set up shared agents across teams) put it bluntly on The AI Daily Brief on 29 September. One of her signs that a team is not ready for a shared agent is that *"nobody will own and maintain the knowledge (the agent drifts within weeks, sometimes days)."* The knowledge she means is everything the agent works from and everything it produces, and once nobody owns it, it goes stale fast. Turn that around and you have a job description. Somebody has to keep the agent's instructions current, notice when its answers start to wander, decide what it is allowed to touch, and be the name people go to when it gets something wrong.

Harvard Business Review gave that person a title back in February. In a piece called *"To Thrive in the AI Era, Companies Need Agent Managers,"* Suraj Srinivasan and Vivienne Wei describe the role as part product manager, part operations lead: watching how agents perform, overseeing how they learn, and making sure people and agents work safely together (we have also, in these pages, described that role as "the Orchestrator"). Their example is Zach Stauber, a support agent manager at Salesforce, who describes his day this way: *"I start and end my day in dashboards, scorecards, and agent observability monitoring"* (observability meaning the tooling that shows you what a system actually did, not what it was supposed to do).

The internet is already full of headlines about "the fastest-growing job title of 2026," and I could not find a single number behind any of them. I have not found anyone actually counting these roles yet. What I can tell you is that the shape is consistent wherever I look, and that the most reachable version of it does not start with a new hire. It starts inside a job somebody already has. The operations lead who owns the support agent. The analyst who keeps the pricing agent honest. The executive assistant who knows which of the boss's bots is allowed to send email and which one is not.

That is the up side of the hotel. A machine of its own means the agent can carry a job, and a job needs a person who looks after it. Those are good jobs, and most of them will go to people who are already in the building.

## Before it moves in

If you are going to give an agent a room, there are a few things worth doing before it unpacks.

**Ask which room it is in.** Before you connect a dot, or any agent that claims a machine of its own, find out whether "its own" means one machine per agent or one per account. If the vendor will not say, assume the hostel, and decide what you connect on that basis. The answer changes what is safe to hand over, and it is a fair question to ask anyone selling you a coworker (and, like always, once you *know* what you intend to give it, write it down and document it so the key other people in your business also know what you are doing and have done).

**Name the person who keeps it right before you switch it on.** Not after it drifts. Gaspar's test is the cheapest piece of governance on offer: if you cannot write down a (real person's) name next to the agent, it is not ready to run unattended. That name is also the first thing anyone should read when they wonder why the agent did something.

**Set the rules where the apps are.** On business accounts, the controls for what a dot may do (permit, ask first, or never) sit with the same admin controls that already decide which apps your people can use. Use them. OpenAI also says it is *"working with Microsoft to integrate specialist dots with their enterprise governance and security controls"* (specialist dots being the ones a company sets up with their own identity and a dedicated job), so the tools your IT team already runs may end up being where those rules live. Start with read-only access to the things it needs to watch, and let it earn write access one app at a time.

**Give it one job, not ten.** A dot with a clear standing responsibility is easy to judge. A dot with ten vague ones is impossible to judge, and the person who owns it will not be able to tell you whether it is working.

None of that is exotic. It is what you would do for anyone who was about to get a key to the building and a login to everything, and on Sunday I will come back to why that is exactly the point.

## A job needs a home

The agent is getting a place to live, and that is what turns software that answers into software that carries something for you. If OpenAI's room is really its own, a lot of work that used to need a person checking in every few hours can now just keep going.

But the room is the claim, and the person who keeps it right is the condition. Find out which kind of room you are buying, put a name next to it, and then go give it a job.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that an agent with a computer of its own can carry a job rather than a task, but only once you know whose computer it really is and whose name sits next to it.*
