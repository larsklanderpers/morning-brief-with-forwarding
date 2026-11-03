<!--
rv4 -- 17 Oct: his rulings on panel items (Max plan + ~$1.75 sampled token cost; harness de-identifies, data not trainable, readers strip their own; Plaid point = model learned to exclude non-business lines Plaid kept re-adding; 'this week'; all quick fixes applied; 'the truth is' cut). Mirrored in the Google Doc. Panel Rd1 9.0 on rv3; not re-panelled.

rv3 -- Sat 17 Oct 2026. EDITOR PANEL ROUND 1 run 17 Oct on rv2 (installed charter = Writing Flow snapshot, byte-identical). Round 1 on rv2: 8.65, slop categorical fail (drafter text). rv3 re-score: 9.0, slop 9.5, no open [VERIFY], footer full -- clears the bar; his call.
rv3 safe fixes only: opener analogy setup frame changed off Fri 16's "If you have ever ... you have already seen" (drafter v1 sentence; his "(in fact, that client might be you)" kept); three drafter headers renamed ("A shoebox, every month" -> "Half a day to a day"; "Read-only, and in CSV" -> "Getting the data out of the banks"; "Before I pressed submit" -> "Checking it against the statements", which was the third "Before ..." header in the window with Fri 16 and Sun 18); two drafter "That is the X" scaffolds varied; "experience" doubled and "reliable" tripled in drafter sentences fixed; frontier-models gloss added; CLAUDE.md gloss moved to the end of its paragraph; footer argument line "were always in" -> "most of the hours ... go to"; "---" separators restored to their own lines; one agreement fix in his text ("stop" -> "stops"); trailing spaces. No contraction of his touched. No em-dashes.
Proposals and rulings for him: see the Round 1 report (not applied to his text).
Prior status (rv2): his pass in the Google Doc https://docs.google.com/document/d/1Oq0qe9BX-VdiFF3CIxqHW3CnPqVTNUIhqA0YPhuxCFE/edit plus his 17 Oct rulings (security wording; Expensify alongside only; 80-90%; Plaid for one bank; OpenAI dot and Grok Bot marketplace = his observations; Expensify-never-asked line; "lose focus"; addendum synced; CLAUDE.md gloss; footer widened; prompts as code blocks). Google Doc NOT updated with rv3 changes.
Footer: full.
-->

# A Shoebox a Month

*Two and a half months of expense reports in about two hours, and the checks I kept before I pressed submit.*

I have used Expensify for close on two decades. I know it very well and I have worked with it through the pain of it for most of that time, simply because I couldn’t find anything better. A couple of weekends ago I did two and a half months of expense reports in about an hour and a half, maybe two, without Expensify, and I am not sure I will ever use it again.

Every accountant who does personal taxes has a client who shows up in April with a shoebox. Receipts, statements, a parking stub from somewhere, all of it in no order at all (in fact, that client might be you). The accountant does not start by making judgment calls about your storage methodology. She starts by sorting: this pile is travel, this pile is meals, this one goes with that one, and only once the shoebox is a stack of labeled piles does she sit the client down and ask the questions that actually need a human. The sorting is most of the hours. The questions are most of the value.

For most of those two decades, I have been both the client and the accountant, every month, and the sorting has been mine. Last Saturday I promised you the expense report build, and that the version I would walk you through uses no photos at all. This is that build. It is about as unglamorous as a build gets, yet it is crazy functional and it cut my time on task by somewhere between 80% and 90%.

## Half a day to a day

A month of expenses has usually taken me somewhere between half a day and a day. *"Some of that, of course, is my own OCD, but some of that is a limitation of the tool."*

The tool part is worth a sentence. As it has added AI features, it has, for me, *"actually gotten harder to use, not easier, for the way that I generally tend to manage my expenses."* This time I ran it only alongside, to compare against and to foot the numbers (total everything and check the totals agree); what I actually submitted came from sheets and reports Claude built. That is one user's experience over a very long time, not a review, and other people may well see it differently. It does not suit the way I work, which is: get every transaction from every card in one place, describe each one, put it in the right accounting class (the category finance uses to book it), and group the trips, the recurring charges of certain types, and the running client-facing costs.

None of that is hard. None of it is particularly special, either. All of it is re-entering and re-sorting things that already exist, in documented form, somewhere else. That is the shoebox. Getting them into Expensify requires then that I take all of those and re-enter them into Expensify’s form -- not mine -- in ways easier for Expensify to manage -- not me. From the outside, the categories and the forms were built around a person keying receipts in one at a time, just replicated into software, and on my side of the exchange, that entry person has been replaced by something that does not mind doing two and a half months at once.

## Getting the data out of the banks

The first decision was how the data gets to the model, and it matters more than it sounds.

I looked at Plaid (a service a lot of finance apps use to connect to your bank accounts and pull transactions automatically). For a specific bank, the Plaid connector was perfect. It worked great, super reliable, and in fairness to Expensify, it supports Plaid as well. Unfortunately, this then meant that I had to go through and delete a number of transactions that didn’t belong, which I had to do every month, and which there was no way for me to filter in bulk. Also, it categorized transactions based on the *vendors* read, not my history. So, with Expensify, using CSV became a necessity -- it was faster but then I ended up entering dozens or hundreds of transactions manually because there was no good way to filter. So, a solution designed to eliminate manual work actually created a disproportionate amount of manual work for me.

So I thought -- maybe I can whip something up that works more like I work. And just as a sideline -- that is one of the craziest things about using AI, that you can, with a plan, an idea to achieve, and a bit of effort, make software align with you, rather than you aligning to your software.

Anyway, for that one bank I stuck with Plaid, the same as I had with Expensify, because that bank's own CSV export kept inserting running totals and other junk into the file. Plaid still pulled in the transactions that did not belong, but this time the model dealt with them: once it knew a transaction was not a business expense (one of the family streaming subscriptions, say), it left it out the following month too, where Plaid in Expensify just kept putting it back and I kept taking it out by hand. But I wanted to try and bulk process everything else I could, and now that I had a rules kit that I could apply easily I thought that bulk loading other transactions might be more efficient. I tried Plaid for some of the other cards too, but it was not quite as reliable there; for everything except that one bank, the CSV was the better path, so *"Ultimately, it really was cleaner to just export CSV files from the used cards and then have the system work through the CSV files."*

I have referenced CSVs a couple of times, but in the event you are unfamiliar with them, CSVs (plain spreadsheet-style text files, one transaction per row) are about the most boring format there is, which is exactly why they work: every row is a date, a merchant, the merchant’s location, and an amount, and there is nothing for the model to misread. Plus, the lack of projected accounting categories made it far easier for me to keep the model working the way I wanted it to. This too is a big thing to remember about AI -- it will get confused, if you try and throw too much at it at once (just like most people), and so keeping your tasks controlled is often a better answer.

I did not use PDF statements despite that being the easiest path. Why not? *"Because PDFs are open to lots of errors"* -- a model reading a PDF is effectively reading a picture of a table, and a picture of a table is where a 7 becomes a 1 and a line gets skipped. I did, however, generate my CSVs from a transactional basis report (the card issuer's list of individual transactions, rather than the statement summary), because that is the grain the expense report needs anyway.

And *"it works entirely with read-only connections."* The model doing the sorting only ever works from the exported files, so it cannot move money, change a card setting or submit anything on my behalf; the worst it can do is get a line wrong in a draft that I am about to check. Which, as we will get to, I do.

One more thing a security-minded reader will ask, and fairly: where does the transaction data go? My data is set up so that it cannot be used for training, and my own harness (the custom setup I run my agents through) strips out the identifiable details before anything reaches the model. That stripping is part of my setup, not part of the model; if yours does not do it, strip the identifiable stuff yourself before you hand anything over.

On top of that, I used computer use (letting the model drive a browser and click through a site the way you would) for this, which I did with Claude, though I generally find ChatGPT’s computer use better, and so I trained the agent exactly how to get the CSV report for each of the accounts I wanted it to process, did it the first time, and then let the agent replay it to pull the other months of data we needed. That agent is a different matter from the model doing the sorting, because it is signed in to the bank, so I watched it the whole way through the first time, and the procedure it replays does nothing but sign in, download and sign out. This alone will save me major time next month, as that part of the process alone could take one to two hours *just to get the transactional data*. Before I even started, it was taking that long to gather up my shoeboxes. Once trained, I went to get a coffee and say hi to my partner, and by the time I got back to my desk, the work was done for all of the banking endpoints needed. Next month, it will do it at 7 am on the day we are going to run it, before I ever even *sit down at my computer*, and I will spend my time solely in review, not so much in aggregation.

The stack, for the record, is Claude, but I would expect any of the current frontier models (the top-end models from the big AI labs) to handle this; nothing here depends on a feature only one of them has. An OpenAI dot (one of OpenAI's always-on agents with its own cloud computer) could orchestrate the whole process and is worth trying right now since, according to OpenAI's own people at a recent meetup I attended, it doesn’t use extra tokens to do so. The Grok Bot marketplace has a bunch of expense report bot templates in it, but I don’t find the task training functionality to be quite as reliable as I do with the big 2, so for now, they are my preferred methodology.

## What it actually did

The biggest job, once the time-consuming collection of the data was finished, was *"to aggregate all the data from all the places without me getting in the middle of it to attach descriptions and recommended accounting categories."* So the sorting is done before I sit down: every card's export combined into one list, each line given a plain-language description and a suggested category, with the category rubric getting more reliable with each expense categorized.

*Recommended* is the important word. As always, with anything, the model suggests; I decide. And the deciding turned out to be much less work, because of one behavior in particular.

**Amazon, and everything after it.** Once I picked a class for a merchant that shows up over and over (Amazon is the obvious one for me), *"it would just cascade through and apply it to all the other transactions from the same place."* One decision, made once, applied to every matching line. If you have ever sat and assigned the same category to the same merchant forty times in a row, you know exactly why that matters. And even more useful -- it figured out that if the Amazon charge was more than $100 then it was likely an asset purchase; if the items within it were less, then it was likely an education (books) purchase. So not only is it a classification tool; it's a smart(er) classification tool. When more than a third of all transactions in a month’s report come from a relatively non-transparent transaction set, smart categorization becomes super-valuable (and speedy). Next month: I will take the time I saved by not having to collect all the data myself and figure out how to give it a connection to my Amazon account (no purchases!) where it can foot transaction amounts from the cards directly to transactions in the order book and ensure the matching is even more reliable.

Here is the instruction, more or less as I would give it now:

```
Here are CSV exports from [my cards] for [these months]. Combine them into one list. For each transaction, write a short plain description and recommend an accounting class from this list: [your classes]. Where you are unsure, say so rather than guess. When I set the class for any merchant, apply the same class to every other transaction from that merchant, of a similar type, and show me what you changed. Maintain records of changes and categorizations in a place where your CLAUDE.md can load it next time we do expense reports and improve its classification every time.
```

Those last two sentences are the ones I would not leave out. A cascade that you cannot see is just a mistake that copies itself. A classification that doesn’t improve over time is wasting the benefits of using inference in the first place. (A CLAUDE.md, if you have not met one, is a plain text file of standing instructions that Claude reads at the start of every session in a project, so whatever you tell it to keep there carries over from one month's run to the next.)

## A trip report from one instruction

The part that surprised me was the trip.

I had a trip to a customer in the window, and the trip report is where I have always lost the most time, because "what belongs to the trip" is a judgment call on nearly every line. So I gave it one rule. Anything in that city. Any travel to or from it. Anything I bought there while I was at that customer. Any spend at that customer, or at its sister customer. *"It handled all that differentiation on its own from the expense extracts."* And it even came back and asked me where the plane flight was (it had been on a previous report; the trip had been planned nearly three months ahead). In close on two decades, Expensify never once asked me how I had gotten to another city.

Think about what that rule asks for. Some of those lines are in the city but not on the trip dates. Some of them are on the trip dates but in another city on the way. Some might be the flight, booked weeks earlier from home (not in this case, though there was a change and another flight in the middle that had its own application). A person sorting that by hand does it line by line, and gets slightly worse at it as the afternoon wears on. The model read the rule once and applied it to every line in the same way. It was done before I had a chance to lose focus, let alone the context of the job.

Again, the prompt is almost depressingly simple:

```
From the combined list, build a trip report for my trip to [city] from [date] to [date]. Include: any transaction in [city]; any travel to or from [city]; anything bought there while I was at [customer]; any spend at [customer] or [related customer]. Exclude everything else. For each line you include, give me the reason in a few words. For everything you exclude, list them all in one place so that I can double-check them. Then list separately anything you were unsure about.
```

The "give me the reason" clause is what makes the output checkable. A line that says *in the city, during the trip* is easy to agree with. A line whose reason does not hold up jumps off the page. This used to be something I did entirely by hand, and every item in the window had to be evaluated by me for applicability (neither the business nor my personal life stops when I am on a trip, so there are things having nothing to do with it that fall within the same window).

## Checking it against the statements

I did not take any of this on trust, and I would not ask you to either.

*"I checked all the numbers, I ran all the totals, and I spot-checked for specific things that I knew needed to be there."* The spot-check is the underrated one: you know there was a hotel, so is the hotel there? You know there was a flight, so is the flight there, and is it on the trip?

The check I would call the most important is the one against the source. *"I reviewed the credit card statements in particular to make sure that there were no transactions that got missed out of the eligible corpus of transactions that the system worked from."* A model that sorts well can only sort what it was given. If an export was short a week, or a card was left out, everything built from it looks perfectly tidy and is still wrong. So the statements are the ground truth, and the expense report gets reconciled against them, not the other way round.

Is there anything I would not trust it with? Honestly, *"at the moment, I don't know that I have anything that I wouldn't trust it with."* Trusting it and checking it are two different jobs, and I still do the second one. The checks are, if it's not clear from the above, as much about what isn’t there as they are about what is.

## Where I am taking it next

The checks I do by hand are exactly the checks I would like the system to do first, so that what reaches me is already questioned. Two of them are next.

**Ask what went missing.** Most of my reports are built around recurring items, ordinary-course-of-business stuff that falls within a fairly predictable range almost every month. So the system should notice when a month does not. What I want it to say, roughly, is: *"Hold on, this feels really low compared to what last month was. Is it possible we're missing transactions? Here's the transactions from last month that don't have a corollary this month, but did a billing model change? Did you intentionally cancel something? What might have happened differently?"* The reconciliation check becomes a question the system asks me before I ask it.

**Put a ceiling on a day.** For trip reports, a per-day limit catches the line that does not belong. As an example only: say average spend cannot exceed $200 a day (room, car, food, everything else), so a fourteen-day trip should not run past $2,800. Leave the airfare out of that sum, *"because airline tickets are such a difficult-to-predict number, you really can't tell."* The number is yours to pick. The point is that the system flags the trip that blows through it, and tells you which days did it.

Neither of these is clever. Both of them are the kind of check a good bookkeeper does without being asked, and both are cheap to bolt onto what already works.

And, because I can never leave well enough alone:

**What else can we connect it to to make it more accurate?** My business partner and I had a chat this week to discuss the fact that we needed to change the way we accounted for inference costs versus the way we account for software and tool subscriptions versus the way we account for other types of subscriptions like internet and telephony. Adding additional classifications and criteria is a very straightforward process from here, and even more importantly we can go back and recategorize all the history as well, in minutes.

## If the whole team did this

This is my own build, for my own expenses, and *"all these things I kind of manage in my own context because it's me."* A team version raises questions mine does not have to answer. What does finance actually need the extract to look like? What happens with cash -- a photo of the receipt, a cap on cash per day, is cash allowed at all? (I do not use cash for any of this, precisely so that I have a tracking point for every receipt I hand back to finance.)

If I did roll it out, I would probably put it on the phone. *"Particularly for Australians who pay for the vast majority of things with tap"* (for my American friends still thinking the whole Apple Pay thing is going to blow over: tapping a card or phone at the register, which is how almost everything gets paid for here), the moment to capture an expense is the moment the payment notification comes through. *"Is this an expense? Great, I'll grab it right now."* Capture at the transaction, and watch a running total build through the month, instead of a shoebox at the end of it. Several different types of expense products in the market have tried to get to this, but our business rules are unique enough that it makes more sense to bespoke it here since we can do it at speed, rather than shoehorning what we need to deal with into someone else’s model of operations.

## Hours back

Two and a half months of the old way would have been somewhere between ten and twenty hours of my life. This took about two, and most of those two were spent on the part that should have been mine all along: deciding, and checking, rather than collecting, and sorting.

I did not track the cost directly at the time, so I went back and sampled it: priced by the token (tokens are the chunks of text a model reads and writes, and what usage is billed by), the whole run came to about $1.75, all in. I am on Claude's Max plan, which is the more expensive tier, so in practice it used a very small fraction of my available inference (the model's compute, which a plan rations out), and I continue to run somewhat light against that total anyway. So for me, the sole cost was of curiosity. Of course, your mileage may vary, but if you have the opportunity to simplify, you should probably consider it. And if your company requires you to use a product like Expensify, then consider using your model-based solution to pre-capture, and then just import it all into the product at the end of the month.

*"Right now, it's really just eliminating hours and hours of workflow from re-entering and recategorizing transactions that are already extant and documented."* That is not a grand claim, and it does not need to be one. The shoebox gets sorted before I sit down, and I get my Saturday back. At the end of the day, getting that time to spend with my family instead of sorting shoeboxes is worth something completely out of proportion to the token cost. I suspect the same is true for most everyone.

---

**Addendum: the prompts, if you want to start from mine.**

*Combine and describe:*

```
Here are CSV exports from [my cards] for [these months]. Combine them into one list, sorted by date. For each transaction, write a short plain description and recommend an accounting class from this list: [your classes]. Mark any line where you are unsure, and say why. Do not drop or merge any transaction.
```

*The cascade:*

```
When I set the class for any merchant, apply the same class to every other transaction from that merchant, of a similar type. After each change, show me the list of lines you updated so I can confirm them. Maintain records of changes and categorizations in a place where your CLAUDE.md can load it next time we do expense reports and improve its classification every time.
```

*The trip report:*

```
From the combined list, build a trip report for my trip to [city] from [date] to [date]. Include: any transaction in [city]; any travel to or from [city]; anything bought there while I was at [customer]; any spend at [customer] or [related customer]. Exclude everything else. For each line you include, give me the reason in a few words. For everything you exclude, list them all in one place so that I can double-check them. Then list separately anything you were unsure about.
```

*The source check:*

```
Here are the statements for the same cards and the same period. Reconcile them against the combined list. List every transaction that appears on a statement but not in the list, and every line in the list that does not appear on a statement. Give me the totals for each card from both sources side by side.
```

*Ask what went missing:*

```
Compare this month's report with the last [three] months. If the total is outside the usual range, say so. List every recurring transaction from earlier months that has no match this month, and for each one, ask me whether it was cancelled, moved to another card, billed differently, or missed.
```

*The per-day ceiling:*

```
For this trip report, my limit is [$X] per day for everything except airfare. Total the non-airfare spend, divide it by the number of trip days, and tell me whether it is over. If it is, show me which days and which lines pushed it over.
```

*The phone version, if you want to try it:*

```
When I forward you a payment notification, ask me one question: is this an expense? If yes, record the date, merchant, amount and a suggested class, and show me this month's running total. If no, do nothing.
```

*The collection agent (if you use one; watch it the whole way through the first time):*

```
I am going to show you, once, how to download the transaction report for [account] as a CSV. Watch each step and write it down as a procedure. From then on, use only that procedure: sign in, download the transaction report for [date range], save it to [folder], and sign out. Do not click anything else, change any setting, or start any payment or transfer. If a page looks different from the procedure, stop and ask me.
```

*Re-sort the history when the classes change:*

```
I have added these classes: [new classes, and what belongs in each]. Go back through every report since [date] and propose a new class for any transaction that now fits one of them better. Show me every proposed change before you make it, and record the new rules in CLAUDE.md for next time.
```

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that most of the hours in an expense report go to collecting and sorting rather than deciding, and that a model, with an agent fetching the exports, can now do both, learn your categories as it goes, and leave you only the decisions and the checks.*
