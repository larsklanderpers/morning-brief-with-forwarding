<!--
DRAFT v1 -- Sat 17 Oct 2026, Saturday Diversion (what it does for you). Drafted 16 Oct by the Sat 17 day chat from `capture_expense-reports_2026-10-17.md` (his dictation, 9 Oct). Not panelled. Not delivered.
SATURDAY GATE: PASS (re-run 16 Oct against this block) -- human feature: his own 2.5 months of Expensify reports done in ~1.5-2 hours with Claude as the import baseline; the reader gets prompts to build the same.
Window checked: Sat 10 (umpire, shadow, notebook, the bar, rubric, "fix the question"), Tue 13 (courtroom witness), Wed 14 (heist film), Thu 15 (TV, "tired" as controlling word, "Half a cent" header), Fri 16 (video-game opener). Opener kind used here: an occupation (the accountant handed a shoebox). "tired" not used anywhere in this piece on purpose (Wed/Thu/Fri all printed it; Sun 18 needs it).
Sat 10 printed promise honored: "next Saturday ... expense reports ... uses no photos at all".
DO-NOT-PRINT honored: no city, customer, sister customer, amounts or merchants beyond Amazon; $200/day framed as an example, not his policy.
No research needed: Expensify is described only through his own experience (no claim about its features), so the capture's [VERIFY] is not triggered.
Open for him: three [YOUR TAKE] markers (how the lines got into Expensify; what he pays / the economics line; optional team beat keep-or-cut). One optional arc-tie sentence, marked.
-->

# A Shoebox a Month

*Two and a half months of expense reports in about two hours, and the checks I kept before I pressed submit.*

I have used Expensify for close on two decades. A couple of weekends ago I did two and a half months of expense reports in about an hour and a half, maybe two.

If you have ever done your own taxes with an accountant, you know the client who shows up in April with a shoebox. Receipts, statements, a parking stub from somewhere, all of it in no order at all. The accountant does not start by making judgment calls. She starts by sorting: this pile is travel, this pile is meals, this one goes with that one, and only once the shoebox is a stack of labeled piles does she sit the client down and ask the questions that actually need a human. The sorting is most of the hours. The questions are most of the value.

For most of those two decades, I have been both the client and the accountant, every month, and the sorting has been mine. Last Saturday I promised you the expense report build, and that the version I would walk you through uses no photos at all. This is that build. It is about as unglamorous as a build gets.

## A shoebox, every month

A month of expenses has usually taken me somewhere between half a day and a day. Why that long? *"Some of that, of course, is my own OCD, but some of that is a limitation of the tool."*

The tool part is worth a sentence, because it is not a complaint about Expensify so much as about how I use it. As it has added AI features, it has, for me, *"actually gotten harder to use, not easier, for the way that I generally tend to manage my expenses."* That is one user's experience over a very long time, not a review, and plenty of people will find the newer version suits them better. It does not suit the way I work, which is: get every transaction from every card in one place, describe each one, put it in the right accounting class (the category finance uses to book it), and group the trips.

None of that is hard. All of it is re-entering and re-sorting things that already exist, in documented form, somewhere else. That is the shoebox.

<!-- OPTIONAL ARC TIE (drafter text, keep or cut): The categories and the forms were built around a person keying receipts in one at a time, and on my side of the exchange, that person has been replaced by something that does not mind doing two and a half months at once. -->

## Read-only, and in CSV

The first decision was how the data gets to the model, and it matters more than it sounds.

I looked at Plaid (a service a lot of finance apps use to connect to your bank accounts and pull transactions automatically). *"Ultimately, it really was cleaner to just export CSV files from the used cards and then have the system work through the CSV files."* A CSV (a plain spreadsheet-style text file, one transaction per row) is about the most boring format there is, which is exactly why it works: every row is a date, a merchant and an amount, and there is nothing for the model to misread.

I did not use PDF statements. *"PDFs are open to lots of errors"* -- a model reading a PDF is effectively reading a picture of a table, and a picture of a table is where a 7 becomes a 1 and a line gets skipped. I did use a transactional basis report (the card issuer's list of individual transactions, rather than the statement summary), because that is the grain the expense report needs anyway.

And *"it works entirely with read-only connections."* Nothing in this setup can move money, change a card setting or submit anything on my behalf. The worst thing it can do is get a line wrong in a draft that I am about to check. Which, as we will get to, I do.

The stack, for the record, is Claude, and I would expect any of the current frontier models to handle this; nothing here depends on a feature only one of them has.

## What it actually did

The biggest job, in my words, was *"to aggregate all the data from all the places without me getting in the middle of it and attach descriptions and recommended accounting classes."* That is the sorting, done before I sit down: every card's export combined into one list, each line given a plain-language description and a suggested class.

*Recommended* is the important word. It suggests; I decide. And the deciding turned out to be much less work, because of one behavior in particular.

**Amazon, and everything after it.** Once I picked a class for a merchant that shows up over and over (Amazon is the obvious one for me), *"it would just cascade through and apply it to all the other transactions from the same place."* One decision, made once, applied to every matching line. If you have ever sat and assigned the same category to the same merchant forty times in a row, you know exactly why that matters.

Here is the instruction, more or less as I would give it now:

> Here are CSV exports from [my cards] for [these months]. Combine them into one list. For each transaction, write a short plain description and recommend an accounting class from this list: [your classes]. Where you are unsure, say so rather than guess. When I set the class for any merchant, apply the same class to every other transaction from that merchant, and show me what you changed.

That last sentence is the one I would not leave out. A cascade that you cannot see is just a mistake that copies itself.

## A trip report from one instruction

The part that surprised me was the trip.

I had a trip to a customer in the window, and the trip report is where I have always lost the most time, because "what belongs to the trip" is a judgment call on nearly every line. So I gave it one rule. Anything in that city. Any travel to or from it. Anything I bought there while I was at that customer. Any spend at that customer, or at its sister customer. *"It handled all that differentiation on its own from the expense statements."*

Think about what that rule asks for. Some of those lines are in the city but not on the trip dates. Some of them are on the trip dates but in another city on the way. Some are the flight, booked weeks earlier from home. A person sorting that by hand does it line by line, and gets slightly worse at it as the afternoon wears on. The model read the rule once and applied it to every line in the same way.

> From the combined list, build a trip report for my trip to [city] from [date] to [date]. Include: any transaction in [city]; any travel to or from [city]; anything bought there while I was at [customer]; any spend at [customer] or [related customer]. Exclude everything else. For each line you include, give me the reason in a few words. Then list separately anything you were unsure about.

The "give me the reason" clause is what makes the output checkable. A line that says *in the city, during the trip* is easy to agree with. A line whose reason does not hold up jumps off the page.

<!-- [YOUR TAKE]: how the finished lines got into Expensify -- an import file it built, entry by hand from its list, something else? One or two sentences; the reader will want to know the last step. -->

## Before I pressed submit

I did not take any of this on trust, and I would not ask you to either.

*"I checked all the numbers, I ran all the totals, and I spot-checked for specific things that I knew needed to be there."* The spot-check is the underrated one: you know there was a hotel, so is the hotel there? You know there was a flight, so is the flight there, and is it on the trip?

The check I would call the most important is the one against the source. *"I reviewed the credit card statements in particular to make sure that there were no transactions that got missed out of the eligible corpus of transactions that the system worked from."* A model that sorts well can only sort what it was given. If an export was short a week, or a card was left out, everything built from it looks perfectly tidy and is still wrong. So the statements are the ground truth, and the expense report gets reconciled against them, not the other way round.

Is there anything I would not trust it with? Honestly, *"at the moment, I don't know that I have anything that I wouldn't trust it with."* Trusting it and checking it are two different jobs, and I still do the second one.

## Where I am taking it next

The checks I do by hand are exactly the checks I would like the system to do first, so that what reaches me is already questioned. Two of them are next.

**Ask what went missing.** Most of my reports are built around recurring items, ordinary-course-of-business stuff that falls within a fairly predictable range almost every month. So the system should notice when a month does not. What I want it to say, roughly, is: *"Hold on, this feels really low compared to what last month was. Is it possible we're missing transactions? Here's the transactions from last month that don't have a corollary this month, but did a billing model change? Did you intentionally cancel something? What might have happened differently?"* That is the reconciliation check, turned into a question the system asks me before I ask it.

**Put a ceiling on a day.** For trip reports, a per-day limit catches the line that does not belong. As an example only: say average spend cannot exceed $200 a day (room, car, food, everything else), so a fourteen-day trip should not run past $2,800. Leave the airfare out of that sum, *"because airline tickets are such a difficult-to-predict number, you really can't tell."* The number is yours to pick. The point is that the system flags the trip that blows through it, and tells you which days did it.

Neither of these is clever. Both of them are the kind of check a good bookkeeper does without being asked, and both are cheap to bolt onto what already works.

## If the whole team did this

This is my own build, for my own expenses, and *"all these things I kind of manage in my own context because it's me."* A team version raises questions mine does not have to answer. What does finance actually need the extract to look like? What happens with cash -- a photo of the receipt, a cap on cash per day, is cash allowed at all? (I do not use cash for any of this, precisely so that I have a tracking point for every receipt I hand back to finance.)

If I did roll it out, I would probably put it on the phone. *"Particularly for Australians who pay for the vast majority of things with tap"* (for my American friends: tapping a card or phone at the register, which is how almost everything gets paid for here), the moment to capture an expense is the moment the payment notification comes through. *"Is this an expense? Great, I'll grab it right now."* Capture at the transaction, and watch a running total build through the month, instead of a shoebox at the end of it.

<!-- [YOUR TAKE]: keep this section or cut it? The capture marked it as an optional closing beat. -->

## Hours back

Two and a half months of the old way would have been somewhere between ten and twenty hours of my life. This took about two, and most of those two were spent on the part that should have been mine all along: deciding, and checking.

<!-- [YOUR TAKE]: the economics line -- what this costs you to run (the plan you are on, or "nothing beyond what I already pay for"), so the hours-back sits next to a price. -->

*"Right now, it's really just eliminating hours and hours of workflow from re-entering and recategorizing transactions that are already extant and documented."* That is not a grand claim, and it does not need to be one. The shoebox gets sorted before I sit down, and I get my Saturday back.

---

**Addendum: the prompts, if you want to start from mine.**

*Combine and describe:*

> Here are CSV exports from [my cards] for [these months]. Combine them into one list, sorted by date. For each transaction, write a short plain description and recommend an accounting class from this list: [your classes]. Mark any line where you are unsure, and say why. Do not drop or merge any transaction.

*The cascade:*

> When I set the class for any merchant, apply the same class to every other transaction from that merchant. After each change, show me the list of lines you updated so I can confirm them.

*The trip report:*

> From the combined list, build a trip report for my trip to [city] from [date] to [date]. Include: any transaction in [city]; any travel to or from [city]; anything bought there while I was at [customer]; any spend at [customer] or [related customer]. Exclude everything else. For each line you include, give me the reason in a few words. Then list separately anything you were unsure about.

*The source check:*

> Here are the statements for the same cards and the same period. Reconcile them against the combined list. List every transaction that appears on a statement but not in the list, and every line in the list that does not appear on a statement. Give me the totals for each card from both sources side by side.

*Ask what went missing:*

> Compare this month's report with the last [three] months. If the total is outside the usual range, say so. List every recurring transaction from earlier months that has no match this month, and for each one, ask me whether it was cancelled, moved to another card, billed differently, or missed.

*The per-day ceiling:*

> For this trip report, my limit is [$X] per day for everything except airfare. Total the non-airfare spend, divide it by the number of trip days, and tell me whether it is over. If it is, show me which days and which lines pushed it over.

*The phone version, if you want to try it:*

> When I forward you a payment notification, ask me one question: is this an expense? If yes, record the date, merchant, amount and a suggested class, and show me this month's running total. If no, do nothing.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that the hours in an expense report were always in the sorting, not the deciding, and that a model working from read-only CSV exports can do the sorting while you keep the decisions and the checks.*
