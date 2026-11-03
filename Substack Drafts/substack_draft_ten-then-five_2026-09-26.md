<!--
DRAFT v1 -- Sat 26 Sep 2026 -- SATURDAY VARIATION (what it does for you) -- part 3 of the build series (Sat 12 bots, Sat 19 writing channel, Sat 26 the attention layer, LAYER ONE)
Working title: Ten, Then Five, Then Stop   (alts: "Caught Up!" / "The Prioritized Surface" / "A Bouncer for My Phone")
SATURDAY GATE: PASS -- human feature: a Teams catch-up app and home-screen widget he built for himself, capped at ten chats plus five, with fireworks when he is done.
Framing, HIS CALL 24 Sep: layer one. Each surface gets its own cap before anything ranks across them. The cross-source ranking Sat 19 promised is named as the next build, not delivered here.
Sources: his Codex transcript (24 Aug evening to 27 Aug evening PT), the two Android PR bodies, the Slack radar paste. Footing note: References\research_sat26-ten-then-five_2026-09-26.md
DO NOT PRINT (see research note): employer name, customer/chat names from the transcript, tenant/client/user IDs, signature hash, internal hostnames and paths, the Azure and Play test URLs, any tester email, PR numbers beyond a count.
Open [YOUR TAKE] slots: 4. Open [VERIFY]: 2. Neither ships.
-->

# Ten, Then Five, Then Stop

*Layer one of the attention build: a bouncer for every door, before anything decides who goes first.*

My phone has a bouncer now. It lets ten in, five more if I ask nicely, and then it closes the door.

Last Saturday I promised you the whole thing this week: one list, on my phone, pulling from Slack, Teams, every inbox, the help desk, open development issues, the Promise Tracker and my text messages, ranked so the critical stuff comes first and capped so the number never makes me want to hide in the corner. I said it deserved a few thousand words of its own. It does. It also turns out to deserve more than one Saturday, and I would rather show you the part that is finished and working than the part that is still a whiteboard.

<!-- [YOUR TAKE]: one or two lines, in your words, on why you split it -- e.g. that you tried to rank across all seven sources at once and it just rebuilt the flood somewhere else, or that you found each door needed its own rules before any ranking meant anything. Whatever is actually true. -->

So here is how it breaks down. Before anything can decide which item from which source matters most, **each source needs its own bouncer**: something that decides what is even allowed to reach me from that one place, how old is too old, and how many at a time. That is layer one. Ranking across all of them is layer two, and it is a coming Saturday. This week is the bouncer I built for Teams, and a quick look at the one for Slack.

## Why Teams, and why me

If you read last week, you know I love the Slack Catch Up widget on my iPhone. One unread item at a time, with a count of what is left, and you swipe through them. My problem was never Slack. **My problem was that Teams has nothing like it.** Teams has recaps for meetings, and they are good, but for the ordinary pile of unread chats there is no catch-up view, and a lot of the people I work with live in Teams rather than Slack.

So on a Monday evening at the end of August I opened Codex (OpenAI's coding agent, which I use alongside Claude Code; I will come back to why) and typed more or less this:

> I really like the Slack "catch up" widget for iPhone. I would like to do something similar for Teams for our guys in the business, and something for Android as well if we can do it. I would like to proof of concept it for me on my logins and then go from there. I am basically looking for a thread summary on any conversations that are unread and then being able to mark them as read afterwards. Is that something doable?

That is the whole spec. I would suggest you notice two things about it. It says what I liked about an existing thing, rather than describing a feature from scratch. And it says **for me first, on my own logins**, before anybody else gets near it.

By Thursday evening it was on my phone, installed from Google Play, running against my real Teams account, with a widget on my home screen. Three evenings, a dozen saved checkpoints, one lost afternoon to a login screen, and one cable that was always upstairs.

<!-- [YOUR TAKE]: the "why Codex for this one" line. Sat 19 was built with Claude Code; this one was not. One honest sentence on why (the machine it lives on, the Microsoft side, habit, just wanted to see) keeps the piece from reading as a tool endorsement either way. -->

## First, prove the plumbing

The first thing we did was not build an app. It was prove that Microsoft would actually let an outside app do the three things I wanted: find my unread chats, read what was in them, and mark them read.

That turned out to be the right place to start, because the answer was a clean yes for one kind of conversation and a no for another. Microsoft's own API (Graph, the door every outside app uses to reach your Microsoft 365 data) keeps a per-person "last read" time on every chat, and its documentation tells you in so many words to compare that against the newest message to decide whether a chat is unread. It also has a single call, "mark chat read for user," that does exactly what it says. **Chats, yes. Teams channels, no.** Channels have no per-person read marker and no way to mark one read from outside, so a channel version would always drift out of sync with what Teams itself thinks you have seen. Chats first, then, and channels maybe never.

The proof was one real unread chat. We found it, read the five messages after my last-read time, wrote a short summary, marked it read, and then asked Microsoft again to make sure it was really gone from my unread list. It was.

I would love to tell you that took five minutes. It did not. Microsoft's Graph Explorer (the web page for trying these calls by hand) got itself into a sign-in loop where the permission screen popped up, I approved it, it bounced me back to the top, and I approved it again, around and around. I believe my exact words at the time were that it was "kind of making me mental." The fix, in the end, was a private browser window, because my normal one was holding onto a half-finished login from an earlier attempt. **If you try this and the login loops, go private before you go crazy.**

## Then, see it before you build it

Before writing any real code, I asked for a clickable mock: the real summary from that one chat, plus a couple of made-up cards, so I could swipe through and see how it felt. This is the step I would tell anybody to never skip, because it is where I made every decision that matters.

Once I had it in my hand, I knew exactly what I did not want. My reply, lightly cleaned up:

> I'd like to make sure that we cap this at not more than 10 chats in any sort of pop-up, and then we can refresh the chats every couple of hours or something. I don't want to get sucked into doing too much stuff here. If I'm going to do it, I'd rather sit down on Teams and do it... Let it load five more after the 10, so no more than 15 in any singular instance.

**The line in the middle is the one that mattered: if I am going to do it, I would rather sit down on Teams and do it.** That is the design principle for the whole attention layer, and I did not know it until I was holding the mock. The phone is not where I do the work. The phone is where I find out whether there is work I need to go and do, and clear the small stuff while I am standing in line. Anything that turns the phone into a second Teams has failed, however clever it is.

So the rules became:

- **Ten chats, then a button for five more, then it stops.** Fifteen is the ceiling in any one sitting. The app will not show you a sixteenth.
- **Refresh every couple of hours**, not every minute.
- **Nothing older than fifteen days.** I first said thirty or forty-five, then realized that if a chat has sat unread for more than two weeks it is not a catch-up item, it is an archaeology project. Anything older belongs in Teams search, not in a pop-up.

And one more, which I will not apologize for:

> put an exclamation point on the "caught up" and have it blow some fireworks for me so I get the positive reinforcement.

**It does. Every time I clear the batch, "Caught up!" and fireworks.** Laugh if you like. I am a grown man and a technology executive, and I have found that a two-second cartoon celebration does more to get me to actually finish the list than any amount of discipline has ever done.

<!-- [GRAPHIC]: screenshot of the "Caught up!" screen with fireworks mid-burst. Anonymize nothing needed if it is the empty state. -->

## Then, make it real, one step at a time

From there the build went up in small, boring steps, and each one got tested on my phone before the next one started:

**A live web page first.** Sign in with my normal work account, pull my real unread chats, show the cards, and make Open in Teams, Later and Mark read actually work. The summaries are built on the device itself, so for this first version no Teams content goes off to an outside AI service at all. <!-- [VERIFY]: confirm the Android build still summarizes on the device and does not call a cloud model. The transcript says the web POC and the Android live-read branch both generate summaries locally; confirm nothing changed after 27 Aug before this sentence ships. -->

**Then, on the phone's browser.** It went up on a free hosting plan, and I tested it in Chrome and Safari on my phone. Two things came out of that test: too many sign-in prompts, and I wanted it to follow my phone's dark mode. Both got fixed the same night.

**Then, an icon on my home screen.** A web page you can "add to home screen" so it opens like an app, with no address bar. Useful, and a good way to live with the thing for a day before committing to anything heavier.

**Then, a real Android app with a widget.** This is the part that finally matched the Slack experience: a tile on my home screen showing the newest catch-up item, and tapping it opens the app. It was written so the core rules (the ten-and-five, the fifteen days, the unread logic) live in shared code that an iPhone version can reuse later.

**Then, onto Google Play, for an audience of one.** Google has an internal testing track (up to a hundred named testers, invite-only, no public listing), and the first release went to exactly one person. Me. The build assistant caught that the default tester list was an existing thirteen-person group and stopped to ask before it shipped to all of them, which I appreciated more than I let on at the time.

<!-- [GRAPHIC]: the widget on the Fold's home screen (black background, gold logo -- confirm the logo is generic or crop it), and one catch-up card with the chat name blurred. -->

## The part I did not expect to care about

The piece I spent the most time on was not the list. It was **Mark read**, because it is the only button in the whole thing that changes something in Teams.

A few rules, all of which I would steal if I were building this again:

**It asks first.** The first time you mark something read, it asks you to confirm.

**It waits for Microsoft to say yes.** The card only moves on when Microsoft comes back with its "done" (a response that means exactly that and nothing else). Anything else, and the card stays exactly where it was.

**It will not guess.** If the phone is folded or rotated or interrupted in the middle and the app is not sure whether the mark went through, it checks before it lets you do anything else, rather than assuming.

**It checks for new messages first.** One catch it raised on day one: if somebody posts a new message after the summary is written but before you tap Mark read, Microsoft will mark that new one read too, and you will never see it. So it refreshes the chat right before it marks it.

**The widget cannot touch anything.** It shows you the newest item, and that is all. It holds no login and has no buttons that change anything. Android would happily let a widget do more than that; I chose not to, for the first version, because a button on your home screen that silently fails is worse than no button.

The first live test of Mark read was one chat I picked, on purpose, that did not matter. It worked on all eight checks the first time, and then I went back to using it like a normal person.

## And the one for Slack

Slack already has a catch-up view, so its bouncer is a different animal. <!-- [YOUR TAKE]: two or three sentences on what the Slack triage radar actually does -- what it pulls, how it decides what is urgent, where you read it. I have the deployment story below but not the product; this paragraph is yours. -->

The best story from building it is not about Slack at all. Everything went through, the new page was published, and when I clicked on the Slack view it took me somewhere else entirely, to a different report I already had. It turned out the new list of views had been published into a folder the web server was not actually serving yet, because a security change we had made a few days earlier was only half finished. The quick fix was obvious: publish the new list back into the old location, and it would all work in ten minutes.

**The build assistant would not do it, and told me why.** The old location was the thing the security change was meant to retire, and putting fresh internal data back into it would make the navigation work by quietly undoing the protection. So we stopped, took stock of what was actually in flight, and finished the security change properly first. That is the right call, and it is the kind of call I have watched good engineers get talked out of at eleven o'clock at night. It is worth building your setup so the tool has enough context to make it.

<!-- [YOUR TAKE] -- optional, and your call entirely: whether any of the radar-hub story is too close to work to print. It is written with no names, paths or systems. Cut the whole section to one line if you would rather keep it out. -->

## A normal day with it

Here is what a normal day looks like with it. I glance at the widget between meetings. If it shows something, I open it, read the summary, and do one of three things: open it in Teams because it needs a real answer, push it to later, or mark it read because the summary told me everything I needed. Ten of those take a couple of minutes. If there are more, I can take five more, or I can not. Then fireworks, and I put the phone away.

**The real win is the same one I told you about last week, from a different angle.** The problem was never the number of unread chats. It was that the number had no ceiling, so looking at it felt like signing up for all of it. Give it a ceiling, and a finish line, and a reason to reach the finish line, and I actually clear the list instead of avoiding it.

You do not need Teams for any of this. The pattern travels:

**Your email.** The ten newest unread messages from the people you have said matter, a one-line summary of each, and a finish line. Everything else waits for the desk.

**A family group chat.** Only the messages since you last looked that actually ask you for something, capped at five, with anything older than a week left alone.

**Your kids' school apps.** One tile, the three things due this week, nothing older, and a celebration when they are all done (they might even like the fireworks more than I do).

## Build your own bouncer

I want you to come out of this section thinking that the hard part was the thinking, not the code. The fuller set of prompts is at the bottom.

**Prove the plumbing with one real item.** Before any app, get your AI of choice to show you that the service will actually let you do all the things you want, on one real piece of your own data, and check the result a second way. If the one thing you care about (for me, marking read) is not possible, you want to know on night one.

**Ask for a mock you can touch.** A clickable page with one real example and a few fake ones. This is where you make your decisions, because you will not know what you want until you are holding it.

**Write the ceiling down before you write any code.** How many at once, how many more if you ask, how old is too old, and how often it refreshes. Mine are ten, five, fifteen days, and two hours. Yours will be different. Having them at all is the point.

**Put a finish line in it.** "Caught up!" plus something that makes you smile. Do not skip this one because it feels silly.

**Go up in small steps, and live with each one.** A web page, then a web page on your phone, then an icon on your home screen, then a real app. Most people can stop at the home-screen icon and be very happy.

**Make the one button that changes anything the most careful thing in it.** Confirm first, wait for a real yes, never guess, and keep it off your home-screen widget until you trust it.

What does it cost? The API side comes with a work Microsoft 365 account (personal Microsoft accounts cannot use these chat calls at all). The hosting I used for the web version is on a free plan meant for personal projects. Getting onto Google Play costs a one-time twenty-five dollars. The iPhone version is the expensive one: Apple's developer program is ninety-nine dollars a year, and you need a Mac to build it, which is why the iPhone version is next in the queue rather than done. And one honest catch for anyone thinking of doing this inside a company: Microsoft does not list this chat permission as needing an administrator's approval, but under the consent rules it has been rolling out since late last year, an app like this will usually need your IT department to say yes before anybody but you can use it. <!-- [VERIFY]: MC1163922 is footed only through a Microsoft Q&A answer, not a Microsoft Learn page. Re-read at a Microsoft primary before this sentence ships, or soften to "Microsoft has been tightening who can approve apps like this." -->

The time, for me, was three evenings, and the longest single stretch was a login screen and a missing USB cable.

## One door at a time

Last week I told you the fatigue was never from the volume that existed; it was from the volume I let into my field of view. This is the same lesson with a door on it. Every source I care about gets a bouncer of its own, with a list, a limit, and a closing time.

Next comes the harder part, the one that looks at all of the doors at once and decides who goes first. What would you put a bouncer on first?

---

**Addendum: the prompts, if you want to start from mine.**

*The opening ask. Name the thing you already like, and keep it to yourself first:*

> I really like [the existing thing] and I want something similar for [my service]. Prove it on my own account first. I want a short summary of anything unread and the ability to mark it read afterwards. Before building anything, check whether the service's own documentation actually supports finding unread items, reading them, and marking them read, and tell me which kinds of conversations it does and does not work for.

*The plumbing proof:*

> Using my own account, find one real unread conversation. Show me only its name and the time of my last read. When I pick one, read only the messages after that time, summarize them, and then mark it read. After that, ask the service again whether it is still unread and show me the answer. Store nothing.

*The mock:*

> Build me a clickable mock I can open in a browser: one card built from that real summary and two made-up cards, clearly labeled as made-up. Swipe through them, with Open, Later and Mark read buttons. Nothing should really be marked read from the mock.

*The ceiling. Put your own numbers in:*

> Show at most 10 items. After the 10th, offer a single "Load 5 more" button, then stop; never show more than 15 in one sitting. Ignore anything whose newest message is older than 15 days, and stop looking once you pass that point so an empty list comes back quickly. Refresh every two hours. When the list is empty, show "Caught up!" with a short celebration.

*The one careful button:*

> Mark read must ask for confirmation the first time. Refresh the conversation immediately before marking it, and if anything new arrived, update the summary and ask again. Only move to the next card when the service confirms success; on anything else, leave the card where it is and say what happened. If you cannot tell whether it worked, check before letting me do anything else. Never allow two taps to send it twice.

*The widget:*

> Add a home-screen widget that shows only the newest summary and the count. It opens the app when tapped. It holds no login and cannot change anything.

*The build steps, one at a time:*

> Take this one step at a time and stop for me to test after each: a local web page, then the same page hosted so I can open it on my phone, then installable to my home screen, then a native app. Save a checkpoint every time a step works.

---

*Thanks for reading. This series is going to run for a few more Saturdays, because the whole thing is bigger than one post, and I would rather show you what works than what I hope will.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that the unread count on your phone is only intimidating because it has no ceiling, and that three evenings with an AI coding agent will buy you one: ten items, five more if you ask, nothing older than two weeks, and fireworks at the end.*
