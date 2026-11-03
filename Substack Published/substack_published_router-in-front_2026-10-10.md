<!--
SCHEDULED -- Sat 10 Oct 2026, on his word 9 Oct 17:08 ("schedule it"). Source: rv10. He pushes to Substack himself.
SATURDAY DIVERSION (what it does for you). Gate PASS: human feature = the Jev router he built in front of his Grok Bot inbox bots, run in shadow, plus the shadow-trial recipe a reader can run.
Panel: Rd1 8.45 on rv7 (categorical fail: spending-cap action repeated Fri 9's "set the cap before the first run") -> Rd2 9.2 CLEARS on rv8 (Voice 9.5 / Slop 9.5 / Line 9.0 / Structure 9.0 / Skeptic 8.5 / Taste 9.0). rv9-rv10 = his rulings on all 13 panel items + sag trim; not re-panelled.
His rulings: one wrong call = the request at exactly 0.50 (sender never named); Knight router callback deliberate; tuning detail out; bar is his (4 conditions); spot-check found two customer forwards treated as volume = a fail by his rule; Artemis named + goddess roster (Athena/Frigg/Brigid); delete -> archive to "Failed Triage"; narrow first step (one notice type, reversible, logged); ID-photo use case = "considering, not proved out"; expense-photo = forward-looking; "email" house spelling; addendum label is STANDING.
Accuracy catches: plan block was stale (scorer in shadow, not a four-lane live router); Jev "three modes" was the Decisions API's (dropped); Sat 26 misquote "a different animal entirely" never shipped -> "not probabilistic yet"; Knight line matched to Sun 4 (97 unanswered warning emails); Jev text-only footed at TypeSafe ("not on images (yet…)"); Decisions API footed at OpenAI primary.
Printed promises: Sat 17 = expense reports; help desk "hopefully the 24th"; child bots vs direct bots "a coming Saturday" (IDEA_BANK S9, S10).
Footer gate: PASS (full footer, no placeholder). No open [VERIFY] or [YOUR TAKE].
-->


# The Router in Front

*Layer one of the attention build, continued: the first bouncer that has to use judgment, and why it is still on probation.*

My email has a new first reader. It has read more than six thousand messages since the end of September, and it has not been allowed to touch a single one.

That is on purpose. Think of a trainee umpire standing a step behind the real one (for my Aussie friends, picture the cricket version, though the baseball one works the same way). He calls every pitch under his breath. Somebody writes down how often his call matched the real one. Nobody's game depends on him, and nobody lets him make a call that counts until the notebook says he is ready.

If you read last Sunday's piece, you met a trading router that ran for forty-five minutes before anyone stopped it, after ninety-seven warning emails to its own staff had gone unanswered. This one is a router too, a much smaller and much cheaper one, and it has spent two weeks being watched very closely (by both me and my bots) and trusted with nothing. Two Saturdays ago I promised you we would go back to Grok Bot "next week". This is a week late, and despite the fact that the delay was purely for personal reasons, I think it is better for the wait, because I can now show you the notebook.

## The storm

Not that my problems are your problems, but I get ***so*** many emails. SO many. From what I can tell, an average day has between 50 and 100 *meaningful* emails (which might not sound like all that much but adds up even if every one only takes a minute to respond to, and they never only take a minute). That same day generally averages between 600 and 900 meaningLESS emails. Not really meaningless; that’s unfair. But system generated notices, things where I am watching solely for a pattern I am concerned the team has missed, etc. Emails that serve a purpose but only once that purpose threshold is reached, is maybe a cleaner way to think about it. Most days, they are just noise.

I mentioned back in September that I work from three Outlook accounts and three Gmail accounts every day, and that the inbox bots in my Grok Bot family triage all of it, surface what I need to answer, and let me nominate a watch list so that the important senders reach me straight away. That was true, and it helped. It was not enough. While the handful of important senders are being surfaced separately, and the ability to add other important senders has value, it's still too “me” dependent. And because of the limitations of how some of the remote control surfaces work -- particularly the Outlook surface, which limits the number of emails you can pull back from any given request to not more than 200 -- I was ending up in a situation where the volume of messages coming in when a notification-qualifying event started to kick off was so high that I was losing actual, material emails, not because I couldn’t process them, but rather because they were just never coming back from the request.

Inbox storms (what I call them, though I am pretty sure Grok coined the phrase) were a real problem. Even with what Inbox Manager was doing, it was still overwhelming my ability to actually see the key emails. I still wasn't getting stuff prioritized sufficiently unless it came from one of my two partners, which was doing name matching, not actual qualification matching (because saying “search for emails from John Doe in the last 24 hours” bypassed the volume failure that the other searches were getting from Outlook).

**Name matching, not qualification matching.** That is the gap. The bouncers I showed you two weeks ago are deterministic (the code follows fixed rules: this sender, this age, this cap, and nothing else), and I said at the time that they were "not probabilistic yet". A rule that says "anything from my partners goes to the top" knows who matters. It has no idea what matters. A customer I have never heard from asking for something that has to happen by Tuesday looks, to a name match, exactly like a newsletter.

So the next bouncer had to open the envelope and read the message. That is the first time in this build that something probabilistic gets a vote on what reaches me. Which is exactly why it does not get a vote yet.

***Note:*** *A* ***deterministic system*** *is like a calculator -- the exact same input always gives you the exact same result every single time -- whereas a* ***probabilistic system*** *is like rolling a die, where the same action leads to a range of possible outcomes based on chance, judgment, or inference. If you don’t live in these terms all the time like me, I know that distinction can be a bit hazy.*

## A cheap (and surprisingly sharp) reader that answers with a number

The reader is Jev. A couple of weeks ago I mentioned that TypeSafe put it into early access on 15 September. What makes it useful here is what it does *not* do: it does not write anything, it does not respond in paragraphs, it doesn’t give you back a bulleted list of choices. You ask it a question, and it hands back a typed answer with a probability attached, in this case "how likely is it that this email is one I actually need to see", as a number between zero and one. No paragraph, no summary, no opinions about my inbox or attempts to restate the contents of the email. Less work, faster, lower cost, and with far fewer hallucinations because it's working within a highly-bounded set of outcomes.

It is also very cheap. TypeSafe lists it at $0.042 per million tokens going in, and nothing for what comes out. I call it through OpenRouter (a service that gives you one account and one key for a lot of different AI models, and bills you per call), so the bill shows up somewhere I can see it.

The first test call was a made-up newsletter. Jev came back in about a third of a second, at a cost of roughly two thousandths of a cent, and put the chance that it mattered at 3%. Fine. It didn’t trip and fall over the first hurdle. But that test, while important and valuable, was the simplest possible rubric I could imagine. A made-up newsletter is just about the easiest question there is (though, I read A LOT of newsletters, so it was slightly more challenging in this situation, but only slightly). The real question was what it would do with six inboxes of my actual email.

The work runs through my chief of staff in Grok Bot, which, as you may remember, I left named "Chief of Staff" back in September, because I am an engineer and I am not in the habit of giving things cutesy names. It is called Artemis now. Some of this is what I said at the time -- that I should probably work on this, and anthropomorphize a bit more. A bigger part is that I now have a mono-agent in Muse (Muse runs a single personal agent rather than a family of bots; mine is named Athena), a dot in OpenAI (one of OpenAI's new always-on agents with its own cloud computer, named Frigg), my Chief of Staff in Grok Bot is named Artemis, and my voice interface agent in ChatGPT (who talks to all three of them) is named Brigid for reasons that, while obvious to me, may not be to anyone else. The pattern is clear -- the necessity is that when I talk to Brigid while I am in the car, I need to be able to say “get Frigg to do this and get Artemis to run this step off the brief and get Athena to pull back the weekend schedule with my partner” -- not run down the Agent in Muse and the dot in OpenAI and the Chief of Staff in Grok Bot each with their own communication methodology and control plane, etc. Names became necessary to manage the surface fan out effectively; and the names are all goddesses because I had a great love of mythology as a kid (and still do, clearly), and so the names are easy for me to remember, as a result.

Anyway, back to Jev and the way the bot structure works, because it’s material to how you build your own. The Jev router is not a feature of Inbox Manager. It is a bot of its own, a child bot sitting underneath Artemis and Inbox Manager, and I built it that way on purpose so that more than one bot can call it. When it reports, it is the router itself saying "I have done this", but if the report is coming to me, the report comes up through Artemis, like everything else does. If a bot is requesting a determination on something central to its work, the Jev Router bot returns to the calling bot with the response, and only once the work is complete, does the response come the whole way back to Artemis. I work hard at going through Artemis for everything rather than going back to individual bots, which is the whole point of having a chief of staff in the first place. The power of the Jev Router concept has proved itself out so well, in my opinion, at non-volume items, that I have also subsequently replicated that model into Claude, Frigg, and Athena (Muse was the hardest of the three; more on that if it turns out to be worth it).

There is a whole conversation to have about child bots versus bots you talk to directly, and we will have it on a coming Saturday. That’s more a shape-of-work, systems-thinking, management strategy kind of conversation, than just a straight “you should build this and try it” conversation.

## Shadow first

Here is the setup, and it is the bit worth lifting for your own use (otherwise, I wouldn’t be wasting your Saturday with it, you know?).

Every morning, Jev scores every new email across all six inboxes and writes the score down. A little later, Inbox Manager does its normal first pass, the way it always has, without looking at Jev's scores. Then the two get compared. Where Inbox Manager thought something mattered and Jev did not, or the other way round, that is a disagreement, and the disagreements are the whole point of the exercise.

Nothing acts on the scores. The mailboxes are read-only to all of this the entire time; Jev cannot archive, move, flag or reply to anything. If it is wrong, the cost of it being wrong is a line in a report. It is not a customer carrying around anger because they inadvertently got an inaccurate response.

That is *shadow mode* (running the new thing alongside the old one and recording what it would have done, without letting it do anything), and shadow first is simply prudent. I have said it before, and I will say it again: if there is a way for something to go wrong, inevitably, in my experience, it will go wrong. I go out of my way as much as I can on the front end to try and prepare for all the wrongness, so it doesn't necessarily come back and bite me quite as hard on the back end. However, it is a lot easier to say “stick to shadow mode” than it is to sit through it, because the first week is humbling.

## The first week

The first comparison came back with Jev agreeing with Inbox Manager about half the time. On only twenty-seven emails that both had scored, so it was an early signal and not a verdict, but half is not a number you hand your inbox to.

What surprised me was *where* they disagreed. When I went through the differences, the fault was almost always in the question, and hardly ever in how Jev had read the email. I had asked "is this a key email?", and I had a very clear idea in my head of what "key" meant, and it turns out I had never actually written that idea down *properly*. Jev was answering the question I asked. Inbox Manager was answering a slightly different one of its own. Neither of them was answering the one in my head, because neither of them has ever been provided with a clear rubric, just a generic “understand what I mean.” Now, when I say this was humbling, I don't necessarily mean it was humbling in the context of Jev or Inbox Manager or anything else. I mean it was humbling in terms of understanding that if the computer (which has been trained by me to respond to the things that I say) did not understand what I was talking about, then a human who I give an instruction to (with that same level of clarity or lack thereof, as the case may be) is even more unlikely to have any idea what it is that I wanted them to do. Which certainly explains a lot of things that I've seen with staff in the past 4 or 5 years.

The clearest example was the automated job-failure alerts my systems send. The first version of the question marked every one of them as important, which is technically true and practically useless: a hundred and thirty-six of them in one day (truly, in that particular case, it was in less than 2 *hours*) would have buried everything else I needed to see.

There was a fair amount of tweaking after that, and almost all of it is specific to my inboxes, so I will spare you the details. What generalizes is the pattern: **most of the disagreements were about what I meant, not about what it read.** Each round of fixing the question taught me something about my own priorities that I had been carrying around as a feeling.

There was also one plain plumbing problem. For a stretch, only two of every twelve scheduled runs actually started. The model was fine; the clock was not. That is the other reason to run in shadow mode: you find the boring failures while they still cost nothing.

## The notebook

By the second week, the third version of the question (if I am being generous; if I am not, it was probably more like the tenth version of the question, but it was the third “named” version of the question) had a clean week, and this is what the router's weekly review, passed up through Artemis, said about it. (It was the first weekly review that actually went out. The one scheduled the week before failed, because the script that writes it did not exist yet. Plumbing again.)

It scored 5,408 emails across the six inboxes in fourteen runs, with no errors. The middle response time was about 155 milliseconds. The whole week cost about seventy-two cents.

By my arithmetic that is a little over a hundredth of a cent per email, or about thirteen cents per thousand. Put another way, that is the entire first-pass read of my email for a week for less than a cup of coffee. That is the router's cost only, not Grok Bot's or anything else's.

It marked about 4.5% of what it read as key, 238 emails in a week, and everything else as noise, most of it notifications and newsletters. That alone is the difference between a storm and a list.

And the number that matters: on the 1,477 emails both of them scored, it disagreed with Inbox Manager's blind call 6.2% of the time, after about 5.7% the week before. Some of that gap is Inbox Manager being wrong by a rule I had made since, which is a strange and rather nice thing to find in your own notebook.

**Now, the skeptic's line, which I would fire myself if I did not call out for you:** agreeing with another bot is not the same as being right. Ninety-four percent agreement with Inbox Manager tells you Jev and Inbox Manager mostly see the world the same way. It tells you ***nothing*** about whether either of them sees it the way I do. So I went through what Jev had called noise myself.

It was not clean. I found two customer emails in there: forwards of system notices the customers had received, which Jev had treated as part of the volume rather than as a customer asking me for something. By my own rule further down, that is a fail, and it is one more reason this is not live yet.

Beyond those two, mostly I found that there were storms that would have been characterized differently if it were not for how Jev was sitting in the middle. I also found that I needed to add a secondary layer of evaluation for things once they got below a certain confidence score. Then I had to change the basis for how it was making its evaluation decision to go along with the confidence score.

The storms are worth a quick paragraph, because they are the clearest picture of what the router is for. Some of my company’s tooling at our customer sites sends a notice every time a particular thing happens at that site, and depending on how urgent and how specific that thing is, the notices may or may not be deduplicated (collapsed into one, so you get told once rather than every time). The particular one that was causing storms in week 1 is deliberately *not* deduplicated, because the thing it watches for is a genuine concern. In this case, though, it was firing for a reason that did not actually trigger the concern: about two hundred messages in roughly three hours, all about one action being taken, none of them a failure. Just notices.

That is a storm, and it does two kinds of damage. The obvious one is that it buries everything else. The less obvious one is the 200-message ceiling on the Outlook fetch I mentioned at the top: a storm eats the fetch, and the mail behind it does not get read at all. That is exactly the coverage gap I come back to below. Having Jev sitting in the middle as a decision engine, saying "do not pull these" or "ignore these", is what keeps a storm from swallowing the morning. Once it comes out of shadow, the plan is for it to archive those messages automatically into a “Failed Triage” folder which I will eyeball review at the end of each day, which change in flow will then speed up the transactional handling of an inbox that is, frankly, stupidly huge. (If you send me an email, and I don’t respond, pour one out for your friend buried under a flurry of correspondence, don’t think I am just ignoring you.)

## Because, as I said, there is always a wrong call

There was one moment in all of this that I keep coming back to.

The 0.5 line is the cutoff: score above it and an email counts as key, below it and it is noise. Partway through, there was a perfectly sensible-looking tweak on the table. Raise the line to 0.55, and a whole class of automated crash-report notices that kept sneaking over it would drop out. Tidy. Easy. One number. A very small adjustment. To a percentage of likelihood number that *felt* very low anyway (shouldn’t that confidence score be more like 80%? One would think, though there was a certain cold comfort in knowing that some things could ONLY be interpreted for meaning and value by me, because the rubric was not really knowable in advance.)

Unfortunately, that one minor modification that seemed very sound on first review would ***also*** have thrown out a real person asking me for something. Her email scored *exactly* 0.50. Raise the line by five hundredths and a real request from a real person goes into the noise pile, and I never see it, and I never know I did not see it.

That is the expensive kind of miss. A newsletter I see by accident costs me four seconds or maybe 15 if I take the time to archive it instead of deleting it. A person I fail to answer costs me something I may not get back. So the fix was not the dial. It was the question again: say plainly that meeting action items count, and that crash-report notices do not, and leave the cutoff where it is. And this is the part that is often difficult to manage well, especially as an engineer: the idea that the percentage should be sufficient is really, really attractive, for people who live in numbers; the idea that a *system* is *probabilistically* attaching that number is **still** hard for me to remember at an instinctive level, and so I have to watch it extra closely.

It’s the same lesson as the intern I keep serving up in these pieces as my example of what not to do, and the fault in that story was never really the intern’s. An intern can get everything right, but you have to stay vigilant, because the one thing they get wrong (simply because nobody told them, or gave them enough background to tell possibility A from possibility B) is inevitably the one thing you couldn’t afford for them to get wrong. That is the manager’s miss, not the intern’s. And unlike with the intern, you can’t teach it to **ask**, because the decision engine has no capacity to ask -- only to review and rate.

**When the tempting fix is to move the threshold, check what is sitting right on it first.** A cutoff is the bluntest tool in the box, and the thing it cuts is usually the thing you cannot see.

## What "ready" has to mean

So, is it live? No. Not yet, and the reasons are what you can take home.

Before the shadow run started, I did my homework (I know, right?) on mail that had already been handled. I took the calls Inbox Manager had already made, and the confidence scores attached to them, and set a baseline for what success and failure would look like for the router. Then I had Jev re-score mail Inbox Manager had already processed, and show me what it had called differently, how big the gaps were, and whether the percentage was high enough to matter. I went through what still qualified and what did not. There was a fair bit of review before I switched the shadow run on at all, and I still ended up changing the settings after the first couple of days, because I was still getting too much. I had been a little too conservative (because, like I said above, a cutoff ultimately becomes a very blunt tool, so I was hesitant to swing it too high. I needed to be more aggressive with it).

Out of that came the bar for "ready". Under ten percent disagreement with Inbox Manager, two weeks running. It has done that: 5.7%, then 6.2% (the first of those partly on the old question). And on its own, that would be enough to switch it on.

However, even though I wrote down that core bar first, once I had a chance to live in the rubric a bit (which is one of the other big benefits of shadow mode), I was able to determine that, in fact, it is ***not*** enough, so I added three more:

**No coverage gaps for a full week.** In two of the inboxes, floods of automated alerts were cutting the morning fetch short, which means some mail gets no score at all. Mail with no score gets no first pass. That is the real blocker right now, which has been addressed with the changes to the rubric as discussed, but won’t really be clear if it worked until I allow the agent to action the offenders instead of just viewing them. So there is an intermediate step before the full switch-on, and it is deliberately narrow: for the one storm-prone notice type only, Jev gets permission to move matching messages into the Failed Triage folder. Nothing else. Every move is logged, every move can be undone, I look at the folder at the end of the day, and everything else stays in shadow exactly as it is. If the morning fetch comes back complete for a full week with that in place, the condition is met; if a single real email lands in that folder, the permission comes straight back off.

**Two weekly reviews on the current rules.** The question changed during the evaluation period, which means results before the rules changed can’t really be used for making a determination on accuracy. Numbers measured on last month's question do not tell me much about this month's.

**No missed human asks.** In a spot-check of what Jev called noise, nothing should be a real person asking me for something. See above. And to be clear: a real person falling into a noise check is an IMMEDIATE FAILURE, regardless of how successful everything else might have been.

If the flood fix holds this week, the review on Monday the 19th is the earliest I would call it ready, and it is my call either way. Until then, the umpire keeps calling them under his breath.

The thing I would underline is the order. **The bar was set against mail I had already seen handled, before the live numbers came in.** If you look first, every number starts to look like "good enough", because you want the thing you built to work. Writing it down first is how you stop yourself from grading your own homework on a curve.

## A shadow trial anyone can run

You do not need Grok Bot for this, and you do not need six inboxes. The pattern travels to anything where you want something cheap to make a first call before you, or another tool, make the real one: your email, a support queue, the notifications from your kid's school, the group chat that never sleeps (on that topic, I wrote a scraper bot for Discord which our team is using on installations; it watches communications, then grades failure notices or help requests against the rubric, and takes action to escalate to me or to the senior commercial person if something hits the criteria. Another real world application of the scoring mindset at play). The fuller set of prompts that are worth really thinking through and trying to morph to your use case(s) is at the bottom.

**Replay the past first.** Before it sees anything new, have it re-score things your current process has already handled, and look at where it differs and by how much. That is where your baseline comes from.

**Run it beside what you already have.** Let the new judge score everything, let your current process carry on exactly as it is, and compare the two. Do not switch anything over on day one.

**Keep its hands off.** Read-only, for the whole trial. If it cannot move, archive or answer anything, then being wrong costs you a line in a report and a couple of cents at most with your decision API, and nothing more.

**Ask for a number, not an essay.** A score between zero and one is something you can compare, total and put a line through. A paragraph of reasoning is something you will skim. It's part of why LLMs present such a unique challenge for humans; it is nearly impossible for most people to not skim something that is longer than a couple of sentences, while a hard “NO” or a “70% likely to be wrong” will pull us up short, every time.

**Give the unsure ones a second look.** The score tells you how sure it is, not just what it thinks. Below whatever confidence you pick, send the item to a second check rather than trusting the first call, and make sure the question it is answering takes that confidence into account. And keep in mind -- the request is cheap enough that if a second rubric is appropriate when something falls below your confidence threshold, then that is worth doing.

**Set your bar before the live results.** What agreement rate, for how long, and what else has to be true. Mine has four conditions. Yours might have two. Having them at all is what matters.

**Look at what it threw away, yourself.** Agreement with another tool is not agreement with you. Sample the noise pile, and look hardest for a real person asking for something.

**Fix the question before you touch the dial.** When the scores look wrong, the first suspect is how you described what you wanted. The cutoff is the last thing to move, and only after you have checked what is sitting right on it.

**Put a spending limit on the key.** Yesterday I said to set the cap before the first run, not after the first invoice, and at this scale that advice is a single setting: whatever service you call it through, put a credit limit on the key before you start. Mine costs less than a dollar a week, even at my ridiculous email volume, and I still want the brake.

## A second reader, and a bigger field

Because I seem to suffer from a need to try new things all the time (Engineer FOMO), I have not only been playing with Jev. On 6 October, OpenAI opened its own version of the same idea to every developer in public beta: the Decisions API. It does the same basic job (you ask a narrow question, it gives back an answer with a probability attached, and you pay only for what goes in: $0.10 per million tokens, against Jev's $0.042), but it asks the question in a few more shapes. You can ask it whether something is true, have it pick one of a set of options you give it, or have it place something on a scale you define, from "cosmetic" to "fully blocked", say, and you can ask several of those in one call. Both companies make speed claims about their own products, and both are the sellers' numbers until your own notebook says otherwise.

The difference that matters to me most immediately is that the Decisions API can look at an image and score it, whether that is a yes or no, a rubric, or whatever else you set up. Jev only does text, at least for now; TypeSafe’s own launch post says its tool is “not on images (yet…)”. From a very real use case for my company, and some derivative use cases I can think of for me personally, that has legs. One of our products does an inference-based comparison of a photo of a driver’s license to a photo of the individual themselves (taken in real time). That second photo, then, has a number of different questions, which should be scored: is the photo the person in the driver’s license (percentage likelihood), is the photo of a live person (percentage likelihood), if the answer to either is less than 95% match, then a rubric that it looks at and says “too much light, your head is turned to the side, etc.” to feed back to the customer on why the processing failed. This type of interpretation right now costs us about $1 for each person compared; even though the Decisions API is more than twice as expensive as Jev is, it would do the photo comparison for, at most, a couple of cents, even after multiple resubmissions -- which, at 25,000 comparisons a month, starts to add up pretty quickly. To be clear, this is one thing we're considering, because it should be able to do it, but we haven't proved it out yet; and moving face matching and the live-person check onto a general-purpose model carries its own spoofing and biometric-privacy questions, which get answered before it goes anywhere near a customer.

From a personal use case, next Saturday we'll talk about some stuff that I've done with managing expense reports that has simplified my life and given me back more than a few hours in the work that I do.

The value of the Decisions API there is in the way I'm extending the expense report prompt set. The version I will walk you through next Saturday uses no photos at all; this part is forward-looking. The extension lets me upload a photo of a receipt or a screenshot of a transaction or what have you, and have it interpret that directly from the screenshot to say, "Is this a qualifying receipt? Does it meet the rubric?" etc., before it ever tries to process it and turn it into a transactional basis.

Whereas with Jev, I'd have to eat the processing first, then, from that output, that OCR output, hope that the output was accurate enough that Jev could make a proper decision. The applicability of the image processing into any sort of decision or scoring API is probably pretty substantial in our modern day, and I suspect I'll have more use cases for it in the future.

Which one wins is a question for another day. The more useful answer for me, right now, is that the idea works. Jev is good enough at reading my email that we are going to start putting it in front of other parts of the system, which is exactly why it was built as a child bot in the first place: the Zendesk ticket bot, the SLA bot (it watches our service-level deadlines), the customer summary bot and a couple of others. We are also playing with a team bot that sits across several people on the same account and reads design decisions, then makes a recommendation about which design makes more sense for which purpose.

Each of those starts in shadow too, a shorter one this time. Evaluation is a crucial step with anything AI at this point, and that step stays in for the foreseeable future.

## Still on probation

Six thousand emails, well under a dollar a week, one near-miss I will remember for a while, and a router that has not been allowed to touch a thing. That last part is not a failure of the build. It is ***the entire point*** of the current build.

On a coming Saturday (hopefully the 24th, depending on the continued length of shadow mode), we will take this to the help desk, the most constant feed in my business, and the ticket bot is where the second notebook starts. If the umpire passes on the 19th, I will tell you. If it does not, I will tell you that too, and why.

---

**Addendum: the prompts, if you want to start from mine.**

*The replay, before anything goes live:*

> Take the last [two weeks] of [email / items] that my current process has already handled, along with the decision and confidence it recorded for each. Re-score them with the new model, then show me every item it called differently, the size of each difference, and the overall disagreement rate. No sender names in the summary.

*The shadow setup:*

> I want to test a cheap scoring model as a first pass on [my email / my queue]. Every time new items arrive, have it score each one: the probability, from 0 to 1, that this is an item I personally need to see. Record the score, the item's date and its source. Do not change, move, archive, flag or reply to anything; treat every mailbox as read-only. My current process keeps running exactly as it does now and must not see the scores.

*The comparison:*

> Once a week, compare the scores against what my current process decided, on the items both of them looked at. Give me the agreement rate, how many items each called important, and a list of every disagreement with a one-line reason why you think they differed. No sender names in the summary.

*The question, written down:*

> Here is what "important to me" means: [a real person asking me for something; anything with a deadline from a customer; ...]. Here is what it does not mean: [automated alerts; receipts; newsletters; ...]. Rewrite the scoring question to say exactly this, show me the old and new versions side by side, and re-score last week's items with both so I can see what changed.

*The near-miss check, before touching the cutoff:*

> Before we change the cutoff from [0.5] to anything else, list every item from the last two weeks that scored within 0.05 of the new value, on either side. Tell me which of them were from a real person asking me for something.

*The noise sample:*

> Pick [50] items at random from what was scored as noise this week. Show them to me one at a time with the score, so I can mark any that I actually needed to see.

*The narrow first step, before the full switch-on:*

> For [one specific notice type] only, you may move matching messages into a folder called [Failed Triage]. Do nothing else to any message. Log every move with the score and the reason, make every move reversible, and stop immediately if I turn this off. Everything else stays read-only, exactly as in the shadow run. Each evening, show me what you moved.

*The bar:*

> Here are my conditions for switching this on: [under 10% disagreement for two weeks running; no unscored gaps for a full week; two weekly reviews on the current question; no real person's request in the noise sample]. Report against each one every week, and tell me plainly whether it is ready. The decision stays with me.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that the cheapest way to let an AI judge your inbox is to run it in shadow beside what you already have, and that when its calls look wrong the fault is usually in the question you asked rather than in how it read, so fix the question before you ever touch the threshold.*
