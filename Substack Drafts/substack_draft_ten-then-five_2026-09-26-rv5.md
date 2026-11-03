<!--
DRAFT v1 -- Sat 26 Sep 2026 -- SATURDAY VARIATION (what it does for you) -- part 3 of the build series (Sat 12 bots, Sat 19 writing channel, Sat 26 the attention layer, LAYER ONE)
Working title: Ten, Then Five, Then Stop   (alts: "Caught Up!" / "The Prioritized Surface" / "A Bouncer for My Phone")
SATURDAY GATE: PASS -- human feature: a Teams catch-up app and home-screen widget he built for himself, capped at ten chats plus five, with fireworks when he is done.
Framing, HIS CALL 24 Sep: layer one. Each surface gets its own cap before anything ranks across them. The cross-source ranking Sat 19 promised is named as the next build, not delivered here.
Sources: his Codex transcript (24 Aug evening to 27 Aug evening PT), the two Android PR bodies, the Slack radar paste. Footing note: References\research_sat26-ten-then-five_2026-09-26.md
DO NOT PRINT (see research note): employer name, customer/chat names from the transcript, tenant/client/user IDs, signature hash, internal hostnames and paths, the Azure and Play test URLs, any tester email, PR numbers beyond a count.
rv3 = his rv1 + graphics + mechanics (25 Sep). rv5 = rv4 + his rulings of 25 Sep (promises, model names, Codex trim, radar trim, Instinct gloss, async line, $8 framing). rv4 = rv3 + panel Rd1 safe fixes (25 Sep): 3 drafter header renames, 1 drafter signpost, MC1163922 sentence rewritten to be true without the Q&A footing, on-device scope, 'awhile' x2, footer fifteen days. None of his words changed beyond mechanics. His [YOUR TAKE] slots all filled. Carried for the panel: MC1163922 consent claim footed only via Microsoft Q&A; 'Opus 5.5 came out this week'; '$4/month' account; 'Tomakin'; 'Soul' vs 'Sol'; 'Instinct'.
-->

# Ten, Then Five, Then Stop

*Layer one of the attention build: a bouncer for every door, before anything decides who goes first.*

My phone has a bouncer now. It lets ten in, five more if I ask nicely, and then it closes the door.

Last Saturday I promised you the whole thing this week: one list, on my phone, pulling from Slack, Teams, every inbox, the help desk, open development issues, the Promise Tracker and my text messages, ranked so the critical stuff comes first and capped so the number never makes me want to hide in the corner. I said it deserved a few thousand words of its own. It does. It also turns out to deserve more than one Saturday, so this week you get the part that is finished and working, and the whiteboard waits. I promise I will keep taking you through the design, but this one will run long enough by itself that these features alone will do it. 

If you read that first sentence in the previous paragraph, and do the level of counting that I try and stick to these days, that's *seven areas of focus.* Leave aside for the moment that pretty much every time management book worth its cost would tell you that's way too many items, my initial take on this (remember, I told you to "Be Ambitious!" even if this is not quite what I meant) was that I tried to rank across all seven sources at once and it just rebuilt the flood somewhere else and then puked it up all over my phone. My immediate first take was to recoil and say "whose idea was this, anyway?" Once I forgave myself for yet again having a reach that exceeded my grasp, when I dug back in, I realized that it was still a viable build, if a bit more work than I had maybe initially intended. Functionally, each door needed its own rules before any ranking I applied at the widget level meant anything. So, I had to design a bit to deal with the limitations of me, not the solution, and that required I slow down and rethink a bit how to attack it.

So here is how it breaks down. Before anything can decide which item from which source matters most, **each source needs its own bouncer**: something that decides what is even allowed to reach me from that one place, how old is too old, what priority is priority enough, and how many through that particular door at that time. That is layer one. Ranking across all of them is layer two, and it is a coming Saturday. This week is the bouncer I built for Teams, and a quick look at the one for Slack. 

## Why Teams first

If you read last week, you know I love the Slack Catch Up widget on my iPhone. One unread item at a time, with a count of what is left, and you swipe through them. My problem was never Slack. Well, more accurately, my problem was never seeing those summaries from Slack. Part of what drove me to this pursuit was that if I go to my Slack widget right now, I've got 58 open conversations. One of the things that I liked best about the Slack widget was that it limited the asymmetric nature of comms with other people to me. The widget doesn't really enforce it, and so I'm kind of right back in the same place, where, again, as I noted above, the flood just comes flooding in through a slightly different pipe. **My bigger problem, in this particular context, was that Teams has nothing like it.** Teams has recaps for meetings, and they are good, but for the ordinary pile of unread chats there is no catch-up view, and a lot of the people I work with live in Teams rather than Slack. Most materially, our distributor partner is an exclusive Teams shop, and so when we do any sort of work together with them, we have to do that work in Teams. That creates a challenge when there are 10 installs going on at the same time, and I'm trying to top-level surf and make sure nothing's going sideways. 

So on a Monday evening at the end of August I opened Codex (OpenAI's coding agent, which I use alongside Claude Code; I will come back to why) and typed more or less this:

> I really like the Slack "catch up" widget for iPhone. I would like to do something similar for Teams for our guys in the business, and something for Android as well if we can do it. I would like to proof of concept it for me on my logins and then go from there. I am basically looking for a thread summary on any conversations that are unread and then being able to mark them as read afterwards. Is that something doable?

That is the whole spec as I originally wrote it. It's not a great spec by any imagination, but I knew (trust me on this one, and if you really want me to explain it, drop me a note, and I will) that Teams would be the toughest nut to crack in the entire 7-stage build, so I wanted to start with the hardest. I would suggest you notice two things about my super well-constructed prompt that I am almost embarrassed to share with you. It says what I liked about an existing thing, rather than describing a feature from scratch. And it says **for me first, on my own logins**, before anybody else gets near it. Some of that is no doubt ego -- I don't like showing prototypes around, it makes me stressed -- but more of that is knowing that the more variables we add to the mix, the harder it will be to trace down problems, the more we will have to deal with security containers, etc. My 7-layer dip was complex enough already -- adding single sign-on was one chip too many at this point.

> **PERSONAL TIP: One of the great things that AI lets you do is determine the distance to close of hard problems -- so if you are a procrastinator, as I can sometimes be, doing the hard one FIRST instead of LAST like might be your normal tendency lets you figure out the shape of how it needs to work, number one, but also lets you determine if it's even worth doing at all.**

Anyway, by Thursday evening it was on my Android phone, installed from Google Play, running against my real Teams account, with a widget on my home screen. Three evenings, working on it while waiting for other things to compile and finish, a dozen saved checkpoints, one lost afternoon to a login screen, and one cable that was always upstairs when I needed it downstairs (I was in a hotel at the time).

I mentioned above that I used Codex for this, and the reason has less to do with which tool is better than with which one I could stand to work with at the time. GPT-5.6 Sol was my daily driver in Codex, and Opus 5, the workhorse model in Claude Code, was wearing on me: verbose, strangely argumentative, and every so often telling me as fact things I knew were not fact. As much as I like the Claude Code harness (Boris Cherny and his team have done a heck of a job with it), and as much as I like working with my codebases from it, I was pretty close to walking away. For an "I'm irritated by this, and I want to do something about it" build that lives on one phone, Opus 5 always wanted a 20-layer security structure; Codex was happy to keep the architecture to a minimum. Opus 5.5 came out this week, and so far it is a lot less opinionated and a lot more functional, so I'm swinging back a bit. I'll share my deeper thoughts on it another day, once I have had more time to see if it holds.

None of that is a verdict on who is better. Parts of this solution were built in Codex, parts in Claude Code and parts in Cursor, and we will get to those in the coming weeks. A lot of this can be done from anywhere; it is mostly about what you get comfortable with.

## First, prove the plumbing

The first thing we did (Codex and I, and I do like to make sure the AI gets credit for doing a lot of the work, so you will see me describe this as "we" quite frequently) was *not* build an app. It was prove that Microsoft would actually let an outside app do the three things I wanted: find my unread chats, read what was in them, and mark them read after I finished. The idea of surfacing what was important and what wasn't needs to wait for a bit, because it implies judgment and ranking, and that is a different animal entirely from an automated structured delivery. Again, doing something deterministic -- where the code itself handles the routing and nothing more -- was a much lower barrier to entry than doing something probabilistic.

That turned out to be the right place to start, because the answer was a clean yes for one kind of conversation and a no for another. Microsoft's own API (Graph, the door every outside app uses to reach your Microsoft 365 data) keeps a per-person "last read" time on every chat, and its documentation tells you in so many words to compare that against the newest message to decide whether a chat is unread. It also has a single call, "mark chat read for user," that does exactly what it says. **Chats, yes. Teams channels, no.** Channels have no per-person read marker and no way to mark one read from outside, so a channel version would always drift out of sync with what Teams itself thinks you have seen. Chats first, then, became my goal, and channels maybe never.

The proof was one real unread chat. We found it, read the five messages after my last-read time, wrote a short summary, marked it read, and then asked Microsoft again to make sure it was really gone from my unread list. It was.

I would love to tell you that took five minutes. It did not. Not even close! Microsoft's Graph Explorer (the web page for trying these calls by hand) got itself into a sign-in loop where the permission screen popped up, I approved it, it bounced me back to the top, and I approved it again, around and around. I believe my exact words at the time were that it was "kind of making me mental." The fix, in the end, was a private browser window, because my normal one was holding onto a half-finished login from an earlier attempt. **If you try this and the login loops, go private before you go crazy.** Hopefully you will be luckier than me, I often run into this kind of thing because I put my toe into so many ponds.

## Then, see it before you build it

Before writing any real code, I asked for a clickable mock: the real summary from that one chat, plus a couple of made-up cards, so I could swipe through and see how it felt. This is the step I would tell anybody to never skip, because it is where I made every decision that matters. This is also the step that I would normally, historically, have skipped entirely because I was terrible at design and I always assumed that I would probably get somebody else to fix the frontend. I used to joke for years that all of my UIs look like they have been built with a crayon, so there's a natural hesitancy to doing this. How do I make it look? What if it looks like this? How do I make it look the way I want? What if it comes out the wrong colors?

The reality is, again, your friend in AI here is really experienced at doing this. As long as you pay attention to it and you say, "I don't want that slop," or "I don't really want blurple," then you can get what you want very quickly and very easily, and the AI will handle all the plumbing.

This has been one of the best things out of this entire product for me personally, at least: my ability to get involved with the UIs again and translate what I know people need into what people see (as opposed to having to go through two or three middlemen to get that done). 

Once I had it in my hand, I knew exactly what I did not want. And that is a critical element to keep in mind. In many cases, it's almost as important to identify what you don't want to see as it is to identify what you do. Every attempt, really, for this kind of thing is going to cost you a very minimal amount of money, and so it's worth pursuing to figure it out. By my rough count from the usage meter, the tokens I used in these first 3 days cost me all of about $8, so just keep that in mind. Anyway, my reply, lightly cleaned up:

> I'd like to make sure that we cap this at not more than 10 chats in any sort of pop-up, and then we can refresh the chats every couple of hours or something. I don't want to get sucked into doing too much stuff here. If I'm going to do that, I'd rather sit down on Teams and do it... Let it load five more after the first 10 if I request it, so no more than 15 in any singular interaction.

**The line in the middle is the one that mattered: if I am going to do that, I would rather sit down on Teams and do it.** That is the design principle for the whole attention layer, and I did not know it until I was holding the mock. The phone is not where I do the work. The phone is where I find out whether there is work I need to go and do, and clear the small stuff while I am standing in line, or sitting in the airport, or hanging out in the lounge room. Anything that turns the phone into a second Teams has failed, however clever it is, *because all it does is create another work surface for me, rather than the triage surface I was looking for.*

So the rules became:

- **Ten chats, then a button for five more, then it stops.** Fifteen is the ceiling in any one sitting. The app will not show you a sixteenth. Your number might be different. This number worked for me because, at peak load, it gave me a surface to deal with all the comms that I get every day. At non-peak load, it lets me see the empty notice box, which is a different kind of relief all in its own. 
- **Refresh every hour**, not every minute. Initially, I had this refreshing every minute because I was concerned I would miss something. Then again, I focused on it being a triage surface, not a work surface. Then I realized that anything that was so important that I didn't see it after an hour refresh could be handled with a phone call. If something needs an answer in under an hour, it should be a phone call; a message is asynchronous by nature, and it should not carry the expectation that I will answer it right away, especially while I am supposed to be not obsessing about things on my phone. I started off at a minute, then I ended up at a couple of hours, and now, after a fair bit of back and forth with it, I'm at an hour. 
- **Nothing older than fifteen days.** I first said thirty or forty-five, then realized that if a chat has sat unread for more than two weeks it is not a catch-up item, it is an archaeology project. Anything older belongs in Teams search, not in a pop-up.

And one more, which I will not apologize for:

> put an exclamation point on the "caught up" and have it blow some fireworks for me so I get the positive reinforcement.

**It does. Every time I clear the batch, "Caught up!" and fireworks.** Laugh if you like. I am a grown-ass man as my sister likes to say, and a very experienced technology executive, and I have found that a two-second cartoon celebration does more to get me to actually finish the list than any amount of discipline has ever done. Like I implied above -- I deserve the reinforcement when I can get it.

![The empty state: Caught up!](sat26-teams-caught-up-empty-state.png)
*The whole reward system, in one screen.*

## Then, make it real, one step at a time

From there the build went up in small, boring steps, and each one got tested on my phone before the next one started (this iterative process was particularly important with the Teams integration because the Microsoft Entra ID security model is a bit wonky if you aren't familiar with it, which I am not, so I needed to make sure I knew where something broke if and when it broke):

**A live web page first.** Sign in with my normal work account, pull my real unread chats, show the cards, and make Open in Teams, Later and Mark read actually work. The summaries are built on the device itself, so for this first web version no Teams content goes off to an outside AI service at all. As I said above, the deterministic model was the place to start. The summaries are great if I am 30 messages behind, but they rarely tell me anything new, and if the last message in the chain was "Got it!" then the summary is often not helpful in figuring out just what "it" was. Remember -- triage surface.

**Then, on the phone's browser.** It went up on a free hosting plan, and I tested it in Chrome on my Android and Safari on my iPhone. Two things came out of that test: too many sign-in prompts, and I wanted it to follow my phone's dark mode (or light mode if it switched). Both got fixed the same night. Both were reasonably quick to resolve. 

**Then, an icon on my home screen.** A web page you can "add to home screen" so it opens like an app, with no address bar. Useful, and a good way to live with the thing for a day before committing to anything heavier. That, then, was the sum total of day 1.

**Then, a real Android app with a widget.** This is the part that finally matched the Slack experience: a tile on my home screen showing the newest catch-up item, and tapping it opens the app. It was written so the core rules (the ten-and-five, the fifteen days, the unread logic) live in shared code that an iPhone version can reuse later. This was the majority of day 2, so I could check the surface and make sure it still worked for me, as intended, in the new configuration.

**Then, onto Google Play, for an audience of one.** Google has an internal testing track (up to a hundred named testers, invite-only, no public listing), and the first release went to exactly one person. Me. The build assistant caught that the default tester list was an existing thirteen-person group and stopped to ask before it shipped to all of them, which I appreciated more than I let on at the time. That, then, was day 3, and I ended up with a new component on my Android screen as a result.

![Three widgets on my home screen. Site name and logos blurred.](sat26-teams-widget-home-screen_anonymized.png)
*Mine is bottom left. More on the other two just below.*

FOR CLARITY: The component we are discussing is the one on the left in the second position. The top right is the native Slack component, since this is before the components were merged, that will look a bit different next time we talk about this; the top left is a Jira tracker provided by Atlassian. Needless to say, the Jira tracker is relatively useless for most purposes because 2100 items absolutely exceeds my focus limit. Even 49 items does. This one becomes one of the harder ones to deal with well because the debt just continues to accrue on it. That's a challenge we can talk about when we get to the integration.

## The only button that changes anything

Surprisingly for me, because I didn't really take enough time to get the design right, the piece I spent the most time on was not the list. It was **Mark read**, because it is the only button in the whole thing that changes something in Teams.

So, as far as learnings from that giant exercise go (so much work for such a small thing -- a metaphor for development work in general), a few rules, all of which I would steal if I were building this again and which I have actually added to my design flow for other items:

**It asks first.** The first time you mark something read, it asks you to confirm. Not every time. Just the first time on a fresh open. Just to make sure you aren't spacing out (which happens to me often).

**It waits for Microsoft to say yes.** The card only moves on when Microsoft comes back with its "done" (a response that means exactly that and nothing else). Anything else, and the card stays exactly where it was, and lets you know that it couldn't get the confirmation.

**It will not guess.** If the phone is folded or rotated or interrupted in the middle and the app is not sure whether the mark went through, it checks before it lets you do anything else, rather than assuming. Again, verification and evaluation of conditions are critical with a tool like this -- because a triage action that misreports causes all kinds of challenges downstream.

**It checks for new messages first.** One catch it raised on day one: if somebody posts a new message after the summary is written but before you tap Mark read, Microsoft will mark that new one read too, and you will never see it. So it refreshes the chat right before it marks it. That's a simple but subtle one, and exactly the kind of thing that *needs* to be identified in design because of the frustration factor; I missed it, which is disappointing, but not surprising. The good news was that the fix was de minimis, and so it was easier than I expected.

**The widget cannot touch anything.** It shows you the newest item, and that is all. It holds no login and has no buttons that change anything. Android would happily let a widget do more than that; I chose not to, for the first version, because a button on your home screen that silently fails is worse than no button at all, especially, as noted above, in a triage surface. It is expected that it will let you respond in the chain -- a triage surface that can take no action has problems of its own, too, so this is a logical iterative step, not an end state.

The first live test of Mark read was one chat I picked, on purpose, that did not matter if it cleared early. Once I verified the first, I handled the other seven that were outstanding right behind that one. It worked on all eight checks the first time, and then I went back to using it like a normal person would (i.e., not staring at the Teams window while I watched the widget to make sure everything was cross syncing).

## And the one for Slack

Slack already has a catch-up view, so its bouncer is a somewhat different animal from the Teams one, where my goal was to provide a surface that was interactive. As I noted above already, there's a Slack icon on there. The problem with that Slack icon is that it gives me every message that's out there. When I see that summary surface, I see 60 items, 70 items, it's a bad day, 100 items.

The goal with the Slack integration in my controlled views app was to actually limit that, right? To make sure that the stuff that was coming in there was actually with some level of urgency. It suppresses a number of things before it even gets started. It hides machine-generated notices. It hides things that are just kind of tracking objects that run in the background. It surfaces direct messages from my partners before anything else.

Once the direct messages have all been read, it surfaces based on ongoing projects that are organized into different categories, and it uses the categories as the basis for how it positions stuff. Again, highly deterministic at this point, not probabilistic yet, but gives me a control surface which is manageable, triage-facing, and makes sure that I don't spend all of my time surfing notices from one of our CloudWatch products instead of actually catching a note from my partner that we're supposed to have a call in 20 minutes. 

The best story from building it happened off to the side, in the web server. Everything went through, the new page was published, and when I clicked on the Slack view it took me somewhere else entirely, to a different report I already had. It turned out the new list of views had been published into a folder the web server was not actually serving yet, because a security change we had made to that particular item a few days earlier was only half finished. The quick fix was obvious: publish the new list back into the old location, and it would all work in ten minutes. 

**The build assistant would not do it, and told me why.** The old location was the thing the security change was meant to retire, and putting fresh internal data back into it would make the navigation work by quietly undoing the protection. So we stopped, took stock of what was actually in flight, and finished the security change properly first. That is the right call, and it is the kind of call I have watched good engineers get talked out of at eleven o'clock at night. It is worth building your setup so the tool has enough context to make the call and help you stick to it. Luckily, for you, not the kind of call you should need to make, as my assumption is that your basket of items is a greenfield, not a partially tracked brownfield.

Before I go on, it is worth showing you the surface all of this sits on, rather than talking in generics. You have probably worked out by now that I struggle with volume. At my desk, I manage it with a set of radars: 21 of them down the side of one screen, each one opening into its own detailed dashboard. I have spent the better part of a year on it, and when I am sitting down with the context to read it, it works. I can work right down through the issues.

On the phone, it is hopeless. There is too much volume, and it needs too much context to understand what you are looking at. What it is good for is handing an already-interpreted set to something smaller. Look at Slack Triage in the middle of the graphic: that translates pretty much directly into what goes onto the phone, just in a different format. I did not have to build that control layer twice.

![The radar hub, cut into three columns so it fits on one screen.](sat26-radars-hub_clean.png)
*The radars, trimmed to fit. Slack Triage is in the middle column, under Work Queues.*

The other thing here that gives you some context about where my head is at is this catchup deck, which is one of these components inside the dashboard. The catchup deck does a couple of things that are really important:

1. It adds, in addition to the done switch, a snooze switch that allows me to basically say, "Hey, don't prompt me about this for an hour or two, but don't forget it either."
2. It keeps me in a flow mode by limiting the number of things I can see at once, and it does that in a couple of different ways. The biggest piece is that it uses a sort of a stack deck, a card deck, as the means for controlling the flow of what I see, even in that structure.

The names are blurred on purpose. What I want you to look at is the countdown bar across the top. As each item is completed or snoozed, the bar runs down to zero, and then it takes some time to refresh, so you're not just sitting there running through countdown after countdown.

![The catch-up deck: one card at a time, then the list view. Repository and ticket names blurred.](sat26-catch-up-deck-triptych_anonymized.png)
*Deck 1, dealt at 8:04. Watch the countdown bar across the top as the cards go.*

## Between meetings

Here is what a normal day looks like with it. I glance at the widget between meetings. If it shows something, I open it, read the summary, and do one of three things: open it in Teams because it needs a real answer, push it to later, or mark it read because the summary told me everything I needed. Ten of those take a couple of minutes. If there are more, I can take five more, or I can not. Then fireworks, and I put the phone away. The Slack embedding is much the same though I was forced to increase the counts to handle it properly; more on that on a coming Saturday.

**The real win is the same one I told you about last week, from a different angle.** The problem was never the number of unread chats (I mean, it's definitely a problem, but it's not a problem that's under my control). It was that the number of unread, unaddressed items had no ceiling, so looking at it always felt like signing up for all of it. When I gave it a ceiling, and a finish line, and then gave myself a *reason* to reach the finish line, no matter how silly, I actually clear the list instead of avoiding it. 

NOTE: I try not to be super woo-woo, but a while back I created a couple of different affirmation tools -- one for me and my state of mind, one for being a good partner and a good man, and one for engineering affirmations about key things I like to keep in mind or items I have read that resonate with me. As the widget continues to expand, I intend for the fireworks screen to also contain a positive affirmation randomly selected from those items, just to make the endorphin boost that much better. Do you need to do this? Of course not. But I find it helps me keep things like this from being drudgery.

Regardless of my thoughts and notes and the complexities of what I am dealing with in my build, you do not need Teams for any of this. The pattern travels through *any* recurring item that you interact with, and provides structure and clarity to your management and interaction with that:

**Your email.** The ten newest unread messages from the people you have said matter, a one-line summary of each, and a finish line. Everything else waits for the desk.

**A family group chat.** Only the messages since you last looked that actually ask you for something, capped at five, with anything older than a week left alone. If you are like me, you prioritize the messages from your partner at the top of this particular list, and honestly, above *any* of the other items.

**My Keep In Touch Reminders.** One tile, reminding me to talk to a friend or family member whom I haven't in two weeks or more. Just a reminder to text, or call, to stay in touch. Again -- something for you to make sure you keep the important stuff near the top amongst the madness. 

Anything that has this type of recurrence can be used - a club you are a member of, your pickleball tournament crew, your kid's school work. All solid candidates, all easily done. We'll keep moving through the control surfaces as we go so you see more of how this works *for me* but there is a reason personal agents have really started to resonate. Maybe when we have the build to a completion point (or at least the first completion point), we can do a comparison to how Muse, and Instinct (an invite-only personal agent that lives entirely in iMessage), and Grok Bot do it, and I can use that to show why this was worth the effort to do it this way for me but might not for you. See how we're feeling about it in a few weeks.

## Build your own bouncer

I want you to come out of this section thinking that the hard part was the *thinking,* not the *coding.* That has, of course, always been true, but you still knew that sooner or later you were going to need to code. Now, not so much any more. That makes it even more intriguing in my opinion, and I think most people who have had the chance to dig in would agree. I am not sure if I have said it in these essays but it's certainly something I have said to the people around me: the cost of curiosity has gone down to almost nothing (because the time it takes to be curious has been so greatly reduced). Your ability to Be Ambitious! is like it has never been before, but you still need to take the steps.

Anyway, the fuller set of prompts is at the bottom. Final thoughts about this week just for your consideration:

**Prove the plumbing with one real item.** Before any app, get your AI of choice to show you that the service will actually let you do all the things you want, on one real piece of your own data, and check the result a second way. If the one thing you care about (for me, marking read) is not possible, you want to know on night one.

**Ask for a mock you can touch.** A clickable page with one real example and a few fake ones. This is where you make your decisions, because you will not know what you want until you are holding it.

**Write the ceiling down before you write any code.** How many at once, how many more if you ask, how old is too old, and how often it refreshes. Mine are ten, five, fifteen days, and an hour. Yours will be different. Having them at all is the point.

**Put a finish line in it.** "Caught up!" plus something that makes you smile. Do not skip this one because it feels silly.

**Go up in small steps, and live with each one.** A web page, then a web page on your phone, then an icon on your home screen, then a real app. Most people can stop at the home-screen icon and be very happy.

**Make the one button that changes anything the most careful thing in it.** Confirm first, wait for a real yes, never guess, and keep it off your home-screen widget until you trust it.

What does it cost? The API side comes with a work Microsoft 365 account (personal Microsoft accounts cannot use these chat calls at all). For clarity, I built and tested it against my work account, and then ran it again on a clean install against a separate Microsoft Teams Essentials account, kept entirely apart from the build, just to make sure that was enough. It is, and Teams Essentials runs $4 a month.

The hosting I used for the web version is on a free plan meant for personal projects. Getting onto Google Play costs a one-time twenty-five dollars. The iPhone version is the expensive one: Apple's developer program is ninety-nine dollars a year, and you need a Mac to build it, which is why the iPhone version is next in the queue rather than done. If you are on an iPhone, you can stick with the web-page-based model (that I talked about above) and it comes with the whopping cost of $0, and I would strongly recommend you consider it for a while, as it will let you know if the other money is worth it. 

And one honest catch for anyone thinking of doing this inside a company: Microsoft does not list this chat permission as needing an administrator's approval, but a lot of companies set up their Microsoft accounts so that ordinary users cannot approve an outside app at all, which means your IT department will usually need to say yes before anybody but you can use it. If you start, and you get stuck because the system is telling you it can't do it, that's probably why. 

The time, for me, was three evenings, and the longest single stretch was a login screen and a missing USB cable. Your time is likely to be longer; my time could easily have been shorter, had I not been making sure I was plumbing for where I wanted to go. Settle in knowing it might take a bit of work, and you will be fine regardless of the length, because it isn't going to be months.

## One door at a time

Last week I told you the fatigue was never from the volume that existed; it was from the volume I let into my field of view. This is the same lesson with a door on it. Every source I care about gets a bouncer of its own, with a list, a limit, and a closing time. Next week, a diversion from the diversion: we go back to Grok Bot and talk about it a bit more. On a coming Saturday after that, we apply this limit to the most constant feed in my business -- the help desk.

After that, since the inclusions are more of the same, comes the harder part, the one that looks at all of the doors at once and decides who goes first. This one required I put down the keyboard and pick up the whiteboard. I will try and see if I can get some representative graphics but I will not use my whiteboard photos for that -- too hard for everyone to try and read.

---

**Addendum: the prompts, if you want to start from mine.**

*The opening ask. Name the thing you already like, and keep it to yourself first:*

> I really like [the existing thing] and I want something similar for [my service]. Prove it on my own account first. I want a short summary of anything unread and the ability to mark it read afterwards. Before building anything, check whether the service's own documentation actually supports finding unread items, reading them, and marking them read, and tell me which kinds of conversations it does and does not work for.

*The plumbing proof:*

> Using my own account, find one real unread conversation. Show me only its name and the time of my last read. When I pick one, read only the messages after that time, summarize them, and then mark it read. After that, ask the service again whether it is still unread and show me the answer. Store nothing.

*The mock:*

> Build me a clickable mock I can open in a browser: one card built from that real summary and two made-up cards, clearly labeled as made-up. Swipe through them, with Open, Later and Mark read buttons. Nothing should really be marked read from the mock.

*The ceiling. Put your own numbers in:*

> Show at most 10 items. After the 10th, offer a single "Load 5 more" button, then stop; never show more than 15 in one sitting. Ignore anything whose newest message is older than 15 days, and stop looking once you pass that point so an empty list comes back quickly. Refresh every hour. When the list is empty, show "Caught up!" with a short celebration.

*The one careful button:*

> Mark read must ask for confirmation the first time. Refresh the conversation immediately before marking it, and if anything new arrived, update the summary and ask again. Only move to the next card when the service confirms success; on anything else, leave the card where it is and say what happened. If you cannot tell whether it worked, check before letting me do anything else. Never allow two taps to send it twice.

*The widget:*

> Add a home-screen widget that shows only the newest summary and the count. It opens the app when tapped. It holds no login and cannot change anything.

*The build steps, one at a time:*

> Take this one step at a time and stop for me to test after each: a local web page, then the same page hosted so I can open it on my phone, then installable to my home screen, then a native app. Save a checkpoint every time a step works.

---

*Thanks for reading. This series is going to run for a few more Saturdays, because the whole thing is bigger than one post, and I would rather show you what I know works than what I hope will.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that the unread count on your phone is only intimidating because it has no ceiling, and that three evenings with an AI coding agent will buy you one: ten items, five more if you ask, nothing older than fifteen days, and a small celebration at the end to help keep you going.*
