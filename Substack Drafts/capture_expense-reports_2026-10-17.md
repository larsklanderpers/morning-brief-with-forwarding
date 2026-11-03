# Capture -- Sat 17 Oct 2026: expense reports with Claude as the import baseline (Expensify)

Week plan: `References\week-plan_2026-10-12.md` (Sat 17 block). IDEA_BANK S10 (TAKEN). Captured 9 Oct 2026 from his dictation in the week-plan chat. **His words, verbatim where quoted. Source material for the drafter, not copy.**

SATURDAY GATE: PASS -- human feature: his own 2.5 months of Expensify expense reports entered in about 1.5 to 2 hours using Claude as the import baseline.
Slot ruling 9 Oct: keep expense reports for Sat 17 ("Great, sounds like a good idea"); help desk proposed for Sat 24.

## Background (9 Oct, from IDEA_BANK S10)
- Expensify, used for "probably close on two decades"; as it added AI features it "actually gotten harder to use, not easier, for the way that I generally tend to manage my expenses."
- A month of expenses used to take "half a day to a day" ("some of that, of course, is my own OCD, but some of that is a limitation of the tool").
- Weekend of ~3-4 Oct: 2.5 months of reports in about 1.5 to 2 hours.
- OK to name Expensify: "I don't have a problem with calling it Expensify."

## What Claude did (9 Oct)
- "to aggregate all the data from all the places without me getting in the middle of it and attach descriptions and recommended accounting classes."
- Cascade: once he picked a class for a repeated merchant (Amazon), "it would just cascade through and apply it to all the other transactions from the same place."
- Trip report: one rule from him (transactions in that city; travel to or from it; anything acquired there while at that customer; any spend at that customer or its sister customer) and "It handled all that differentiation on its own from the expense statements."

## The inputs (9 Oct)
- Considered Plaid; "Ultimately, it really was cleaner to just export CSV files from the used cards and then have the system work through the CSV files."
- "I didn't want to use PDFs because PDFs are open to lots of errors, but I did use a transactional basis report."
- "it works entirely with read-only connections."
- Cash: "I don't typically use cash for any of this stuff, just so I have a tracking point for making sure that I have receipts and whatnot to give back to finance." Open questions for cash if it were a team tool: photo of the receipt? allowed to identify cash? a cap on cash per day? "All these things I kind of manage in my own context because it's me."

## The checks he kept before submitting (9 Oct)
- "I checked all the numbers, I ran all the totals, and I spot-checked for specific things that I knew needed to be there."
- "I reviewed the credit card statements in particular to make sure that there were no transactions that got missed out of the eligible corpus of transactions that the system worked from to build the expense report."

## What he would not trust it with (9 Oct)
- "At the moment, I don't know that I have anything that I wouldn't trust it with."

## What he would add next (9 Oct) -- the build's next layer, evals on the output
- **A range check on the monthly total.** Most reports are "built around recurring items" and "ordinary-course-of-business reports" that "fall within a specific range of numbers almost every month." The system should say: *"Hold on, this feels really low compared to what last month was. Is it possible we're missing transactions? Here's the transactions from last month that don't have a corollary this month, but did a billing model change? Did you intentionally cancel something? What might have happened differently?"*
- **A per-day ceiling on trip reports.** His example metric: average spend can't exceed $200 a day (room, car, food, everything else), so a 14-day trip shouldn't exceed $2,800, "independent of airline tickets, right, because airline tickets are such a difficult-to-predict number, you really can't tell." (The $200 is an illustrative threshold, not his actual policy -- treat as an example in the piece.)

## If he rolled it out to the business (9 Oct) -- optional closing beat, not the build
- Enforcing "the extract format and stuff that finance really needs" would need more thought about "where the problems would be."
- He would probably tie it to the phone: "particularly for Australians who pay for the vast majority of things with tap ... When the notification came through, it said, 'Is this an expense? Great, I'll grab it right now.'" Capture "at the transaction grain and watch a running total get built."
- Today's value, his line: "Right now, it's really just eliminating hours and hours of workflow from re-entering and recategorizing transactions that are already extant and documented."

## Drafter notes
- Format: prompts in the body (the trip-report rule as a worked prompt; the cascade instruction), fuller set as an addendum (range check and per-day ceiling as prompts too).
- Natural shape: the chore -> the inputs (CSV, read-only, why not PDF or Plaid) -> what it did -> the checks he kept -> the evals he would add -> (optional) the phone/tap version for a team.
- Arc tie (optional, do not bend): Expensify's rules were built for a person keying receipts; his side of the exchange stopped getting tired.
- Tier 0 bookend not required.
- DO-NOT-PRINT: the city, the customer and its sister customer; any amounts or merchants beyond Amazon unless he OKs them; the $200/$2,800 as his real policy.
- [VERIFY] before drafting: Expensify's current AI features as described on Expensify's own pages (one line at most, and only if the piece says what changed); nothing about Expensify's internals.
- DO NOT: Sat 10's umpire, storm, shadow, notebook, "the bar"; Thu 15's price argument.
