<!--
DRAFT v1 -- Sun 18 Oct 2026 capstone. Drafted 16 Oct 2026 by the Sun 18 day chat ("Research, then draft", his word).
Research: References\research_sun18-please-take-one_2026-10-16.md (its DO-NOT-PRINT list binds every revision).
Pays off Fri 16's printed promise: "I will come back to what the better answer looks like on Sunday."
Merges: Wed 14 pt 1 (crew of one, called back via its own close), Thu 15 pt 3 (reading got cheap; deciding did not), Fri 16 pt 3 (the rule was the cheap part; callback only, not restated).
Opener kind: seasonal/neighborhood custom (new this window; not pop culture, gaming, heist, courtroom or office document).
Open [YOUR TAKE]: 2. Not panelled.
-->

# Please Take One

*All week, the rules kept turning out to be held up by how much effort it took to push on them. The better answer is not a smarter guard. It is changing what each attempt costs, pays and has to prove.*

Every October, a lot of American porches grow a bowl of candy and a hand-lettered sign. The sign says "Please take one."

(For my Australian friends: Halloween in the US is a serious neighborhood operation, and the unattended bowl is what people put out when they would rather not answer the door every four minutes.) The sign does almost none of the work. What keeps the bowl going until eight o'clock is that taking more than one costs a kid something small: a second of embarrassment, the chance a neighbor is watching, the walk back up the driveway for another go in a different mask. Most kids take one, maybe two. The bowl was priced for them.

Then somebody shows up with a pillowcase and tips the whole thing in. Nothing about the rule changed. The sign is still there, still polite, still perfectly clear. What changed is that one visitor did not find the extra effort expensive, and it turns out the rule never had anything else holding it up.

<!-- [YOUR TAKE]: Bowl house or door house? A pillowcase story from your own porch, or from taking your kids around? Real life only; leave this empty rather than let me invent one. -->

That pillowcase has turned up all week in different clothes. It was an attacker's crew collapsing into a model subscription on Wednesday, the forty pages you used to skim on Thursday, and a hospital bill and a loyalty program on Friday. Each time, a rule that looked like it was enforced by its wording was really enforced by the effort it took to push on it, and that effort now costs a few cents of compute. On Friday I said the reflex is to buy a bigger model of your own, and I promised to come back on Sunday with a better answer. It turns out to be less about models than you might expect.

## Priced for one at a time

The clearest statement of the problem I found this week came from GitHub (the site where a great deal of the world's open-source software is written and reviewed). In February, Ashley Wolf, who works with open-source maintainers there, wrote a post called *Welcome to the Eternal September of open source*. The title borrows an old internet joke: every September in the early 1990s a fresh batch of university students arrived on Usenet (the discussion boards that predate most of the web) and had to be taught the manners, until the commercial dial-up services opened the doors in 1993 and September simply never ended. Her version of that for 2026 is one line: *"The cost to create has dropped but the cost to review has not."*

The numbers behind that line are GitHub's own. *"In January 2023, developers merged about 25 million pull requests a month across GitHub. Today that number tops 90 million."* (A pull request is a proposed change to someone else's code; somebody on the receiving end has to read it and decide whether to accept it.) Keep in mind as you read that GitHub also sells Copilot, one of the tools writing a good share of those requests, so it sits on both sides of this particular bowl.

curl is the sharper version. It is a small piece of software almost nobody has heard of and almost everybody uses (if your phone, car or television has ever downloaded anything, there is a decent chance curl did the downloading). For years it ran a bug bounty: find a security flaw, report it, get paid. Over the life of the program it paid out more than $100,000 for 87 confirmed vulnerabilities. Daniel Stenberg, who leads the project, wrote in January that in earlier years *"somewhere north of 15%"* of submissions turned out to be real. Starting in 2025, that dropped *"below 5%."* In his words: *"Not even one in twenty was real."*

Now put those two next to Thursday's piece, because Thursday's good news was real. Reading got cheap on our side too. A maintainer can have a model read every incoming request, and curl's team can have one sort the reports. But look at what did not get cheap on either side. Somebody still has to *decide*: merge this or not, pay this or not, trust this or not, and then live with the result. Thursday said the same about telling whether a machine wrote something; that cost did not fall either. The attempt got cheap. The judgment on the attempt did not.

That ratio is what all of these rules were quietly priced on. When trying cost about as much as deciding, the person deciding was protected by the fact that most people would not bother to try more than once. Most of curl's bad reports were not clever. They were plentiful. The real advantage of a counterparty that does not slow down is not that it is smarter than you; it is volume. And a rule that costs you something every time somebody tries it is a rule whose cost to you now grows with their volume, not yours.

## Sitting on the porch all night

The reflex, and I understand it, is to sit on the porch.

Cloudflare (a company that sits in front of a very large share of the websites you visit, filtering their traffic) tried it first. In March 2025 it announced AI Labyrinth, a feature that *"uses AI-generated content to slow down, confuse, and waste the resources of AI Crawlers"* (the automated programs that copy websites to feed AI models). By its own count, those crawlers were sending *"more than 50 billion requests to the Cloudflare network every day,"* or *"just under 1% of all web requests"* it sees. The trap was elegant: an endless maze of plausible but useless pages, on the logic that *"No real human would go four links deep into a maze of AI-generated nonsense."*

I like it. It is also a model pointed at a model, and it has the shape of Friday's arms race in miniature. Every crawler request that wanders into the maze costs Cloudflare something to generate and serve. Your costs rise with their volume, which is exactly the arithmetic you were trying to get out of.

Three and a half months later, the same company changed the price instead. On 1 July 2025, Cloudflare started asking new customers by default whether they wanted to let AI crawlers in at all, and launched what it calls pay per crawl. A crawler that wants a page gets back *"an HTTP 402 Payment Required response, accompanied by a crawler-price header"* (402 is a status code the web's standards set aside decades ago for payments and then mostly left unused). The site owner picks one of three answers: allow, charge, or block.

To be clear about the interest here: Cloudflare would very much like to be the toll booth for that payment, and it is selling both the maze and the gate. But the fact that one company tried both, in that order, inside four months, is the most useful thing I can point you at. The first approach matched the other side's effort with its own. The second changed what each attempt costs.

## Changing what the bowl costs

When I went looking for institutions that had already re-priced a rule rather than buying a bigger guard, I kept finding the same four moves.

**The first is to take the prize off the table.** curl's bounty officially ended on 31 January. *"We no longer offer any monetary rewards for security reports – no matter which severity."* Stenberg considered the obvious alternative, charging reporters a small fee to submit, and turned it down: the payment handling, the chargebacks, and the risk of keeping out exactly the legitimate researchers he wanted to hear from. The cash had become the thing that made a bad report worth sending. Take the cash away and a machine-written report earns its sender nothing. GitHub went halfway in May with its own security bounty, citing new tools *"including AI"*: a working proof of concept is now required, and findings that are valid but low-impact earn swag rather than money.

**The second is to charge for the knock.** That is Cloudflare's 402, and it is also the idea behind Anubis, a free, open-source tool that a number of sites put in front of their pages. Before the page loads, your browser has to solve a small math puzzle (proof of work, in the jargon). For one visitor it is a second of a laptop fan. For a crawler asking for a million pages it adds up fast. It worked well for a while, and then Codeberg, a non-profit code-hosting site that used it, posted in August 2025: *"It seems like the AI crawlers learned how to solve the Anubis challenges."* Which is the honest lesson of the second move. If you price the attempt in compute, you have set a price the well-funded side can simply pay. The price has to be in something the other side is short of.

**The third is to move the gate to proof.** At the end of October last year, arXiv (the free archive where most new computer-science research is posted before, or instead of, formal publication) said that review articles and position papers *"must now be accepted at a journal or a conference and complete successful peer review"* before its computer-science section will take them. It was receiving *"hundreds of review articles every month,"* many of them *"little more than annotated bibliographies,"* and it said plainly that *"Generative AI / large language models have added to this flood."* Asked whether this was a policy change, arXiv answered *"Technically, no!"*: those papers were never formally part of what it accepts, and moderators had been sorting them by hand. What changed is where the gate sits. Instead of a volunteer reading every submission, the submission has to arrive carrying something effort alone cannot cheaply produce, which is someone else's completed review. GitHub's proof-of-concept rule is the same move.

**The fourth is to ration by party.** In June, GitHub gave repository owners a way to cap how many pull requests a user without write access can have open at once, with a bypass list for contributors they already trust. Its announcement includes a line I did not expect: *"Pull requests opened by Copilot or another AI agent will count toward your limit."* GitHub's own product counts against GitHub's own cap. I do not read that as hypocrisy. I read it as a company that knows which side of the ratio it has to fix, even when its own tool is on the other side of it.

There is a fifth that I described on Friday without calling it this. The randomization we built into reward logic at my company, so that members (or their agents) cannot predict what will happen on a given day, is a re-price too: it makes each attempt to game the program less certain to pay. And like every one of these, it cost us something to build and costs us something to run.

<!-- [YOUR TAKE]: Of the four (remove the prize, charge for the knock, move the gate to proof, ration by party), which would you reach for first in loyalty, and why? Has your company, or a customer, tried a per-member or per-day cap on offers? What did the honest members say? -->

## The kid with one hand out

Every one of those moves charges somebody honest. curl's genuine researchers lost their bounty. A first-time contributor with three good fixes can hit GitHub's cap. Anubis makes every reader's laptop do a little work. Friday's honest gamer pays for the anti-cheat in the install and the occasional false ban. I have not found a version of this that costs the honest party nothing, and I would distrust anyone who tells you they have.

What separates a good re-price from a bad one is where the cost lands as volume goes up. The honest party makes a handful of attempts. The other side makes thousands. A small charge per attempt, a cap per party, a prize that only pays out on proof: each of them is close to trivial at one attempt and ruinous at ten thousand. That is the shape you are after. A counter-model does the opposite. It costs you something every time it runs, so your bill rises with their volume, and Friday was a full piece on where that ends. A rule re-priced the right way flips which side's costs move.

On Wednesday I said you will not outlast a machine. You do not have to. You only have to make its ten-thousandth attempt cost it more than its first, and make your own cost stay roughly where it was.

## Before the bowl goes out

**List the rules that cost you something every time someone tries.** Every claim your team reviews, every application it reads, every return it inspects, every report it triages, every promotion it honors by hand. Next to each, write down roughly what one attempt costs the other side today, in minutes and dollars. Where their number has fallen to cents and yours has not moved, that is your list, and it is usually shorter than you fear.

**Pick the lever before you pick a model.** For each rule on the list, ask which of the four moves fits: remove the prize, charge for the attempt, move the gate to proof, or ration by party. Buy the counter-model only where none of them does, and when you do, go in knowing your costs will now rise with theirs.

**Price it in something they are short of.** Compute is cheap for the other side, which is exactly why Anubis stopped working at Codeberg. Look instead for things that do not scale for them: an identity with a history behind it, money that has to be accounted for somewhere, a reputation they can lose, or a review somebody else had to do first.

**Walk your best ordinary customer through it.** Before the new rule goes live, run your most valuable, most ordinary member, customer or contributor through it on paper. If they would notice it as more than a minor nuisance, the price is sitting in the wrong place, and you are about to charge the kid with one hand out for the kid with the pillowcase.

## One per visitor

The sign on the bowl was never the rule. The walk back up the driveway was, and that walk now costs a fraction of a cent.

You can spend every October on the porch with a model of your own and a bigger bill each year. Or you can change what is in the bowl, and how much comes out at once, so the pillowcase is not worth carrying up the driveway.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that the rules this week kept failing because they were priced on the other side's effort, and the better answer than a counter-model is to re-price the rule itself so the cost of trying rises with the other side's volume while yours stays flat.*
