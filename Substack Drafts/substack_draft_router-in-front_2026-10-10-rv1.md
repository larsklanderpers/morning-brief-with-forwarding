<!--
DRAFT rv1 (v1 + his 9 Oct 12:40 answers). v1, 9 Oct 2026 (Sat 10 day chat). Not paneled. Not scheduled.
Basis: his four Artemis-channel reports (26 Sep, 29 Sep, 5 Oct, 6 Oct; pasted 9 Oct) + his interview answers (capture_router-in-front_2026-10-10.md) + References\research_router-in-front_2026-10-01.md.
His rulings applied: the one wrong call = the 0.50 near-miss; Sun 4 Knight router = DELIBERATE one-clause callback; tuning detail out ("use case specific"); the bar is his, all four conditions; he has spot-checked the noise himself; Artemis named (spelling ARTEMIS).
Plan block was stale: his build is a KEY/noise scorer in shadow, NOT the four-lane action router and NOT live. Neither is claimed.
DO-NOT-PRINT honored: no sender, customer, inbox or job names; no TypeSafe multiples; nothing from Linas; no poster motive; no "live".
rv1 9 Oct: his spot-check findings placed (mechanics only); action "Give the unsure ones a second look" added from them; Decisions API aside added (footed at OpenAI primary, see comment); expansion to Zendesk/SLA/customer-summary/team bots placed in his words. OPEN for him: [YOUR TAKE] x4 (storm quote shaping; Artemis name; 0.50 reaction; Decisions capacity); [VERIFY] x2 (who wrote the reports; whether the bar predates the numbers) (who wrote the reports); one proposal flagged inline (the 136-alerts sentence, keep or cut under your "tweakiness" ruling).
-->

# The Router in Front

*Layer one of the attention build, continued: the first bouncer that has to use judgement, and why it is still on probation.*

My email has a new first reader. It has read more than six thousand messages since the end of September, and it has not been allowed to touch a single one.

That is on purpose. Think of a trainee umpire standing a step behind the real one (for my Aussie friends, picture the cricket version, though the baseball one works the same way). He calls every pitch under his breath. Somebody writes down how often his call matched the real one. Nobody's game depends on him, and nobody lets him make a call that counts until the notebook says he is ready.

If you read last Sunday's piece, you met a trading router that ran for forty-five minutes with nobody watching and nobody able to stop it. This one is a router too, a much smaller and much cheaper one, and it has spent two weeks being watched very closely and trusted with nothing. Two Saturdays ago I promised you we would go back to Grok Bot "next week". This is a week late, and I think it is better for the wait, because I can now show you the notebook.

## The storm

I get so many emails. I mentioned back in September that I work from three Outlook accounts and three Gmail accounts every day, and that the inbox bots in my Grok Bot family triage all of it, surface what I need to answer, and let me nominate a watch list so that the important senders reach me straight away. That was true, and it helped. It was not enough.

<!-- [YOUR TAKE] -- his words from the interview, placed as-is for him to shape. Drafter has not reworded them. -->
Inbox storms were a problem. Even with what Inbox Manager was doing, it was still overwhelming my ability to actually see the key emails. I still wasn't getting stuff prioritized sufficiently unless it came from one of my two partners, which was doing name matching, not actual qualification matching.

**Name matching, not qualification matching.** That is the gap. The bouncers I showed you two weeks ago are deterministic (the code follows fixed rules: this sender, this age, this cap, and nothing else), and I said at the time that judgement and ranking were "a different animal entirely". A rule that says "anything from my partners goes to the top" knows who matters. It has no idea what matters. A customer I have never heard from asking for something that has to happen by Tuesday looks, to a name match, exactly like a newsletter.

So the next bouncer had to read the message, not just the envelope. That is the first time in this build that something probabilistic (it makes a judgement call and tells you how sure it is, rather than following a rule) gets a vote on what reaches me. Which is exactly why it does not get a vote yet.

## A cheap reader that answers with a number

The reader is Jev. A couple of weeks ago I mentioned that TypeSafe put it into early access on 15 September. What makes it useful here is what it does *not* do: it does not write anything. You ask it a question, and it hands back a typed answer with a probability attached, in this case "how likely is it that this email is one I actually need to see", as a number between zero and one. No paragraph, no summary, no opinions about my inbox.

It is also very cheap. TypeSafe lists it at $0.042 per million tokens going in, and nothing for what comes out. I call it through OpenRouter (a service that gives you one account and one key for a lot of different AI models, and bills you per call), so the bill shows up somewhere I can see it.

The first test call was a made-up newsletter. Jev came back in about a third of a second, at a cost of roughly two thousandths of a cent, and put the chance that it mattered at 3%. Fine. A made-up newsletter is the easiest question there is. The real question was what it would do with six inboxes of my actual mail.

The work runs through my chief of staff in Grok Bot, which, as you may remember, I left named "Chief of Staff" back in September, because I am an engineer and I do not give things cutesy names. It is called Artemis now.

<!-- [YOUR TAKE] -- why the name. Sat 12 printed "I just left mine Chief of Staff ... I do not give things cutesy names, which I probably should work on." This is the payoff if you want it; one or two lines on why Artemis. Cut the paragraph above if you would rather not reopen it. -->

<!-- [VERIFY] -- who wrote the four reports? The 26 Sep report says "I've sent the result to Artemis", so the reporter may be a build agent reporting TO Artemis rather than Artemis itself. The draft below says "the reports I got" to stay neutral; fix to whichever is true. -->

## Shadow first

Here is the setup, and it is the part I would steal if I were you.

Every morning, Jev scores every new email across all six inboxes and writes the score down. A little later, Inbox Manager does its normal first pass, the way it always has, without looking at Jev's scores. Then the two get compared. Where Inbox Manager thought something mattered and Jev did not, or the other way round, that is a disagreement, and the disagreements are the whole point of the exercise.

Nothing acts on the scores. The mailboxes are read-only to all of this the entire time; Jev cannot archive, move, flag or reply to anything. If it is wrong, the cost of it being wrong is a line in a report.

That is shadow mode (running the new thing alongside the old one and recording what it would have done, without letting it do anything), and I have said in these pieces before that shadow first is simply prudent. It is a lot easier to say than to sit through, because the first week is humbling.

## The first week

The first comparison came back with Jev agreeing with Inbox Manager about half the time. On only twenty-seven emails that both had scored, so it was an early signal and not a verdict, but half is not a number you hand your inbox to.

What surprised me was *where* they disagreed. It was not Jev misreading emails. When I went through the differences, it was almost always the question. I had asked "is this a key email?", and I had a very clear idea in my head of what "key" meant, and it turns out I had never actually written that idea down. Jev was answering the question I asked. Inbox Manager was answering a slightly different one of its own. Neither of them was answering the one in my head, because nobody had ever been told it.

<!-- PROPOSAL (drafter, his call under the "tweakiness" ruling): keep this one example as the illustration of the shape, or cut it and let the paragraph above stand alone. -->
The clearest example was the automated job-failure alerts my systems send. The first version of the question marked every one of them as important, which is technically true and practically useless: a hundred and thirty-six of them in one day would have buried everything else I needed to see.

There was a fair amount of tweaking after that, and almost all of it is specific to my inboxes, so I will spare you the details. The pattern is the useful part: **most of the disagreements were about what I meant, not about what it read.** Each round of fixing the question taught me something about my own priorities that I had been carrying around as a feeling.

There was also one plain plumbing problem. For a stretch, only two of every twelve scheduled runs actually started. The model was fine; the clock was not. That is the other reason to run in shadow: you find the boring failures while they still cost nothing.

## The notebook

By the second week, the third version of the question had a clean week, and this is what the reports I got said about it.

It scored 5,408 emails across the six inboxes in fourteen runs, with no errors. The middle response time was about 155 milliseconds. The whole week cost about seventy-two cents. By my arithmetic that is a little over a hundredth of a cent per email, or about thirteen cents per thousand. If you want the capability-and-cost version, that is the entire first-pass read of my email for a week for less than a cup of coffee, and the honest note on it is that this is the router's cost only, not Grok Bot's or anything else's.

It marked about 4.5% of what it read as key, 238 emails in a week, and everything else as noise, most of it notifications and newsletters. That alone is the difference between a storm and a list.

And the number that matters: on the 1,477 emails both of them scored, it disagreed with Inbox Manager's blind call 6.2% of the time, after about 5.7% the week before. Some of that gap is Inbox Manager being wrong by a rule I had made since, which is a strange and rather nice thing to find in your own notebook.

**Now, the skeptic's line, which I would fire at myself if I did not:** agreeing with another bot is not the same as being right. Ninety-four percent agreement with Inbox Manager tells you Jev and Inbox Manager mostly see the world the same way. It tells you nothing about whether either of them sees it the way I do. So I went through what Jev had called noise myself.

<!-- HIS WORDS, 9 Oct (dictated), placed with mechanics only. "Jeff" in the dictation = Jev. Check "swarms" reads as you meant it. -->
Mostly, I found that there were swarms that would have been characterized differently if it were not for how Jev was sitting in the middle. I also found that I needed to add a secondary layer of evaluation for things once they got below a certain confidence score. Then I had to change the basis for how it was making its evaluatory decision to go along with the confidence score.

## The one wrong call

There was one moment in all of this that I keep coming back to.

The 0.5 line is the cutoff: score above it and an email counts as key, below it and it is noise. Partway through, there was a perfectly sensible-looking tweak on the table. Raise the line to 0.55, and a whole class of automated crash-report notices that kept sneaking over it would drop out. Tidy. Easy. One number.

It would also have thrown out a real person asking me for something. Her email scored *exactly* 0.50. Raise the line by five hundredths and a real request from a real person goes into the noise pile, and I never see it, and I never know I did not see it.

<!-- [YOUR TAKE] -- optional, one or two lines: what you thought when that one came up. -->

That is the expensive kind of miss. A newsletter I see by accident costs me four seconds. A person I fail to answer costs me something I may not get back. So the fix was not the dial. It was the question again: say plainly that meeting action items count, and that crash-report notices do not, and leave the cutoff where it is.

**When the tempting fix is to move the threshold, check what is sitting right on it first.** A cutoff is the bluntest tool in the box, and the thing it cuts is usually the thing you cannot see.

## The bar, written down before I needed it

So, is it live? No. Not yet, and I want to show you why, because the "why" is the part you can take home.

<!-- [VERIFY] -- timing: did you set the under-10% bar BEFORE the first comparison came in? The 6 Oct report says "the bar I've been using". If it came later, this paragraph and "I wrote the bar down before I looked at the numbers" below need rewording. -->
Before any of the numbers came in, I wrote down what "ready" would mean. Under ten percent disagreement with Inbox Manager, two weeks running. It has done that: 5.7%, then 6.2%. And on its own, that would be enough to switch it on.

It is not enough, so I added three more:

**No coverage gaps for a full week.** In two of the inboxes, floods of automated alerts have been cutting the morning fetch short, which means some mail gets no score at all. Mail with no score gets no first pass. That is the real blocker right now.

**Two weekly reviews on the current rules.** The question changed recently. Numbers measured on last month's question do not tell me much about this month's.

**No missed human asks.** In a spot-check of what Jev called noise, nothing should be a real person asking me for something. See above.

If the floods get fixed this week, the review on Monday the 19th is the earliest I would call it ready, and it is my call either way. Until then, the umpire keeps calling them under his breath.

The thing I would underline is the order. **I wrote the bar down before I looked at the numbers.** If you look first, every number starts to look like "good enough", because you want the thing you built to work. Writing it down first is how you stop yourself from grading your own homework on a curve.

## Put one in front of your own

You do not need Grok Bot for this, and you do not need six inboxes. The pattern travels to anything where you want something cheap to make a first call before you, or another tool, make the real one: your email, a support queue, the notifications from your kid's school, the group chat that never sleeps. The fuller set of prompts is at the bottom.

**Run it beside what you already have.** Let the new judge score everything, let your current process carry on exactly as it is, and compare the two. Do not switch anything over on day one.

**Keep its hands off.** Read-only, for the whole trial. If it cannot move, archive or answer anything, then being wrong costs you a line in a report and nothing more.

**Ask for a number, not an essay.** A score between zero and one is something you can compare, total and put a line through. A paragraph of reasoning is something you will skim.

**Give the unsure ones a second look.** The score tells you how sure it is, not just what it thinks. Below whatever confidence you pick, send the item to a second check rather than trusting the first call, and make sure the question it is answering takes that confidence into account.

**Write your bar down before the first result.** What agreement rate, for how long, and what else has to be true. Mine has four conditions. Yours might have two. Having them at all is what matters.

**Look at what it threw away, yourself.** Agreement with another tool is not agreement with you. Sample the noise pile, and look hardest for a real person asking for something.

**Fix the question before you touch the dial.** When the scores look wrong, the first suspect is how you described what you wanted. The cutoff is the last thing to move, and only after you have checked what is sitting right on it.

**Put a spending limit on the key.** Whatever service you call it through, set a credit limit on the key before you start. Mine costs pennies a week, and I still want the brake.

## Still on probation

## A second reader, and a bigger field

I have not only been playing with Jev. On 6 October, OpenAI opened its own version of the same idea to every developer in public beta: the Decisions API. It does the same basic job (you ask a narrow question, it gives back an answer with a probability attached, and you pay only for what goes in: $0.10 per million tokens, against Jev's $0.042), but it asks the question in a few more shapes. You can ask it whether something is true, have it pick one of a set of options you give it, or have it place something on a scale you define, from "cosmetic" to "fully blocked", say, and you can ask several of those in one call. Both companies make speed claims about their own products, and I would treat both as the sellers' numbers until your own notebook says otherwise.

<!-- [YOUR TAKE] -- the "slightly different piece of capacity that I think has worth": which one, and what you would use it for. One or two lines; keep it an aside so the piece stays a working piece, not a survey. Footed at primary: developers.openai.com/api/docs/guides/decisions (question types predicate / choice / score; several per call; text and images; refusal answer; $0.10/M input, no output charge) and the 6 Oct public-beta post on community.openai.com. -->

Which one wins is a question for another day. The more useful answer for me, right now, is that the idea works. Jev is good enough at reading my email that we are going to start putting it in front of other parts of the system: the Zendesk ticket bot, the SLA bot, the customer summary bot and a couple of others. We are also playing with a team bot that sits across several people on the same account and reads design decisions, then makes a recommendation about which design makes more sense for which purpose.

<!-- PROPOSAL (drafter): if each of those new placements also starts in shadow, one clause saying so here would tie them back to the lesson. Only if true. -->

## Still on probation

Six thousand emails, well under a dollar a week, one near-miss I will remember for a while, and a router that has not been allowed to touch a thing. That last part is not a failure of the build. It is the build.

On a coming Saturday, we take this to the help desk, the most constant feed in my business, and the ticket bot is where the second notebook starts. If the umpire passes on the 19th, I will tell you. If it does not, I will tell you that too, and why.

---

**Addendum: the prompts, if you want to start from mine.**

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

*The bar:*

> Here are my conditions for switching this on: [under 10% disagreement for two weeks running; no unscored gaps for a full week; two weekly reviews on the current question; no real person's request in the noise sample]. Report against each one every week, and tell me plainly whether it is ready. The decision stays with me.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that the cheapest way to let an AI judge your inbox is to run it in shadow beside what you already have, write down what "ready" means before you look at the results, and fix the question before you ever touch the threshold.*
