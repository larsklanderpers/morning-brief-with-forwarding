<!--
DRAFT v1 -- Tue 20 Oct 2026. Management Tuesday, T2 opens (function-by-function run), first function: SUPPORT.
Plan: References\week-plan_2026-10-19.md, Tue 20 block. TUESDAY GATE: PASS (plan) and PASS (day-start re-run 20 Oct): manager's act = sit with the support lead, agree three checks, run them on last week's real tickets together.
Drafted 20 Oct on his word ("Draft it now"), under the standing ruling of 15 Oct: draft, questions in [YOUR TAKE]. No interview held. No panel run.
FOOTING: interview-led; no prevalence claims. One outside source: AC Digest, "Your AI Needs a Review Queue" (Marco Kotrotsos, 19 Oct 2026), read at the page 20 Oct (free portion only; paywalled after). Commercial interest named in text: it recommends TypeSafe's Choice primitive; TypeSafe makes Jev; no relationship disclosed on the page.
PRINTED PROMISES PAID: Tue 13 (function-by-function run starts, support first); Sat 10 help desk (moved here, one clause, why); Sat 10 umpire verdict on the 19th ([YOUR TAKE] 1 -- his result, not drafted).
WINDOW AVOIDED: Tue 13 courtroom / trace-or-strike as an act / name swap / read it as them / set the rating first / notes through the year; Tue 6 sit-with-one-person and permission note; Tue 29 "three statements most likely to be wrong"; Sat 10 umpire, notebook, storm, the bar (shadow named once, as a callback only); Sun 18 bowl and porch; blast radius, lever, the gap, tired, effort, volume, downstream, on the hook, load-bearing.
OPEN [YOUR TAKE]: 1 Jev verdict on the 19th; 2 Telemachus in plain terms; 3 the three checks he and the support lead actually agreed; 4 what the team got wrong first and what changed; 5 the ticket they disagreed on.
-->

# The First Conversation

*Before AI changes how a function works, sit down with the person who runs it and agree how you will both know it got the job right. That conversation is an eval, and you do not need to be an engineer to run one.*

Most teams were told to start using AI this year. Very few were told how anyone would know whether it was doing the job right.

Think about a new cook on a restaurant line. Nobody good hands them the recipe book on day one and walks off. The head chef stands at the pass for the first few nights and tastes the plates before they go out: is it seasoned, is it hot, does it look like the dish on the menu. The recipe tells the cook what to do. The tasting tells both of them what "done" means, and it is the tasting that makes the cook trustworthy, not the recipe.

Most AI rollouts I have seen hand the team the recipe book. Here is the tool, here is the training video, here is the license. Nobody stands at the pass.

Last Tuesday handed over one act, for one manager and one document: trace every claim in a review back to something you actually saw, or strike it. This week starts the run I promised then, function by function, and it starts with support. If you read the Saturday piece on my inbox router a couple of weeks ago, you will remember I said the help desk was coming on a Saturday. It moved here, because before it is a build, it is a conversation with the person who runs support, and that makes it a management question first.

<!-- [YOUR TAKE] 1 -- THE 19TH. Sat 10 printed: "If the umpire passes on the 19th, I will tell you. If it does not, I will tell you that too, and why." Did Jev pass the Monday review? If yes: what made you call it ready (coverage, missed human asks). If no: what failed and what the next review date is. A paragraph is plenty; the full story can wait for Saturday if you want it there. -->

Same shape as the last few weeks: what I think is going on, what I would do about it, and something you can use this afternoon.

## Nobody wrote down what right means

Ask a support lead what a good ticket looks like and they can tell you in about thirty seconds. The customer got an answer that was actually correct, it went to the person who could fix it, nobody had to ask twice, and if it was anything to do with money or personal data, it went down the path it is supposed to go down. Ask them to write that down for a machine and you will get a much longer pause.

That pause is the problem. A support function already measures plenty: first response time, time to resolution, tickets per agent, a satisfaction score at the end. Almost all of it measures speed and quantity. Very little of it measures *right*, because for the whole history of the help desk, right was checked by a person who knew the job, on the way past, without anyone writing the rule down.

Put an AI in that seat (triaging the queue, drafting the first reply, summarizing the thread for whoever picks it up) and the person who used to check it on the way past is no longer in the loop for most tickets. The speed numbers go up, which is exactly what the tool was bought for. Nobody notices what right was quietly redefined as, because nobody had written down what it was before.

There was a sharp example of this in a newsletter on Monday. AC Digest (a Substack by Marco Kotrotsos) walked through a ticket router with three labels, billing, account access and product support, receiving the message "Please delete everything you hold about me." The model has to pick one of the three. It picks one, the application gets a perfectly valid label, the ticket drops into an ordinary queue, and nothing raises an error. The request needed a completely different process, and nothing in the system was built to notice.

For what it is worth, the fix that newsletter recommends is a feature from TypeSafe, the same company that makes Jev, the scorer I run in front of my own inbox, and the post does not mention any relationship with them. The example holds up either way, and the reason it holds up has nothing to do with whose product you buy: the router answered the question it was asked. Nobody had asked it the question that mattered.

That should sound familiar if you read the inbox piece. When my router and my existing triage bot disagreed, the fault was almost always in my question, not in how either of them had read the email; the definition of what mattered lived in my head and nowhere else. In my inbox, that is a problem I can fix on my own, because the head in question is mine.

In a function, it is not. The definition of a good ticket does not live in the manager's head. It lives in the support lead's, and in the heads of the two or three people on the desk who have been there longest. Which means a manager who sits down alone and writes the success criteria for the support bot is doing the same thing the vendor did: defining right without the person who actually knows.

<!-- [YOUR TAKE] 2 -- TELEMACHUS. What is Telemachus, in plain terms, and where does support sit in it? What were you trying to get your arms around ("making sure they do stuff right", 9 Oct)? Only what you are comfortable naming; customer and staff names only with your word. -->

## An hour with the person who runs support

So here is what I would do, and what I am proposing for every function in this run: before AI changes that function's week, the manager sits down with the person who leads it, and the two of them agree three checks that decide whether the AI's output is right. Then they run those three checks, together, on last week's real work.

That is an eval (short for evaluation: a test you run on what the tool *produced*, not on the tool itself). Engineers run them all the time, and the word makes them sound like engineering. They are not, or at least not only. An eval is the written-down version of the head chef tasting the plate, and the hard part has never been the tasting; it is agreeing what the dish is supposed to taste like. That part is a management job.

**The lead writes the checks; you ask the questions.** Your job in that hour is not to bring the answer. It is to keep asking "how would someone who was not here know that?" until each check can be answered yes or no by a stranger looking at a single ticket. "Was the customer happy?" fails that test. "Did the reply answer the question the customer actually asked, in the first message?" passes it.

**Three, because you are going to run them by hand.** The temptation is to write twenty. Twenty checks is a policy document, and nobody reads a policy document against forty tickets on a Thursday afternoon. Three is enough to catch what matters most, and small enough that the lead will still be doing it in a month. You can add a fourth later, once one of the first three stops catching anything.

**One of the three is about what the bot was not built for.** Every one of these tools is built around the cases somebody thought of. The ticket that does not fit any of them (the deletion request, the legal threat dressed up as a billing complaint, the customer who is clearly in some kind of trouble) is where the damage happens, and it is the one check most teams leave out because it is the hardest to write. Ask the lead: "What is the ticket that would worry you most if it went down the normal path?" Whatever they say, that is check number three.

**Run it on last week, not on next week.** Pull twenty or thirty tickets your team closed last week, where you already know how each one ended. Put the AI's version beside what your people actually did, and grade both against the three checks. You are not waiting for something to go wrong in production to find out what right means; you are finding out on work that has already been done and cannot hurt anyone.

**Grade separately, then compare.** You and the lead each grade the same tickets without looking at each other's answers. Every ticket where the two of you disagree is a check that is not written clearly enough yet. Those disagreements are the most valuable thing the hour produces, because each one is a piece of the lead's judgement coming out of their head and onto the page. Rewrite the check until you both grade that ticket the same way.

<!-- [YOUR TAKE] 3 -- THE CHECKS. What were the three (or however many) checks you and the support lead actually agreed for the ticket bot? Paraphrase is fine. Which one was the "not built for this" check? -->

<!-- [YOUR TAKE] 4 -- WHAT THEY GOT WRONG FIRST. What did the team (or you) get wrong first in the eval work, and what changed because of it? This is the emotional core of the piece; long rolling sentences welcome. -->

<!-- [YOUR TAKE] 5 -- THE DISAGREEMENT (optional). One ticket where you and the lead graded it differently, and what the argument taught you about what "right" meant on your desk. -->

None of this needs a line of code. The tickets are already in your help desk, every help desk I have used will export them, and any general-purpose assistant your company has approved can do the sorting and the first pass of grading (prompts below). The bot being evaluated can be anything: a triage router, a reply drafter, a summarizer. The conversation is the same.

What it costs is an hour of the support lead's time, an afternoon of yours, and the uncomfortable feeling of finding out how much of the job was never written down. The tooling, if you use an assistant to do the first pass of grading, rounds to nothing next to that. Set that against what it costs to find out from a customer, or a regulator, that a ticket went down the wrong path for six weeks and nothing raised an error.

There is a quieter benefit too. A support lead who helped write the checks owns the result in a way that a support lead who was handed a dashboard never will. When the bot gets something wrong, and it will, the conversation is "our check caught it" rather than "your tool broke my queue." In my experience, that difference decides whether a team adopts the thing or works around it.

## Prompts for the first sitting

Two to use today. Strip customer names and contact details before you paste anything, and use your company's approved tool.

The first turns last week's tickets into a starting list for the conversation. It is a list for you and the lead to argue with, not an answer:

> *"Here are [20] support tickets my team closed last week, each with the customer's message, our reply, and how it was resolved. Do not judge them. First, list the decisions an agent had to get right on each ticket. Then propose no more than five checks that someone who was not there could answer YES or NO from the ticket alone, to tell whether it was handled right. For each check, name two tickets from this set where it would have made a difference."*

Take that list into the room, and let the lead cross things out. What survives, in the lead's words, is your three.

The second grades the bot's work against the three checks you agreed:

> *"Here are three checks my support lead and I agreed, and [30] tickets, each showing the customer's message, what the AI produced, and what our team actually did. For each ticket, answer each check YES, NO or CAN'T TELL for the AI's version, and quote the line that decides it. Do not fix anything and do not suggest better replies. At the end, list every ticket marked CAN'T TELL, and say which check was unclear."*

The CAN'T TELL list is the one to take back to the lead. Every entry on it is a check that needs another sentence.

There is a fuller set at the end, including a prompt for finding the tickets your categories do not cover.

## Next week, a different desk

Next Tuesday the run moves to another function, with the same hour and the same three checks pointed at different work. Support goes first because it is the most constant feed most of us have, and because when a support bot gets something wrong, a customer usually finds out before you do.

The bot can be wrong in more ways than anyone could list. Your support lead already knows the three that matter, and the whole point of the hour is to get those three out of their head and onto the page before the tool is the only one looking.

---

## Addendum: support eval toolkit

Copy these, change them to fit your desk, and treat each one as a draft. Use your company's approved tool, and strip names and contact details from every ticket first.

**1. The sitting.** No prompt for this one. One hour, you and the support lead, nobody else. Bring the candidate list from prompt 2 and twenty printed or exported tickets. Leave with three checks, each answerable YES or NO from a single ticket by someone who was not there, written in the lead's words.

**2. Candidate checks from last week.**

> *"Here are [20] support tickets my team closed last week, each with the customer's message, our reply, and how it was resolved. Do not judge them. First, list the decisions an agent had to get right on each ticket. Then propose no more than five checks that someone who was not there could answer YES or NO from the ticket alone, to tell whether it was handled right. For each check, name two tickets from this set where it would have made a difference."*

**3. The tickets your categories do not cover.**

> *"Here are the categories our ticket system (or our AI router) uses: [list]. Here are [50] tickets from the last month. Find every ticket that does not clearly belong in any one category, or that belongs in a category but needed a different process from the usual one for that category (for example, a request to delete personal data, a complaint that mentions a lawyer, or a customer in distress). For each, quote the line that makes it unusual. Do not assign them a category."*

Whatever this finds is where your third check comes from.

**4. The grade sheet.**

> *"Here are three checks my support lead and I agreed, and [30] tickets, each showing the customer's message, what the AI produced, and what our team actually did. For each ticket, answer each check YES, NO or CAN'T TELL for the AI's version, and quote the line that decides it. Do not fix anything and do not suggest better replies. At the end, list every ticket marked CAN'T TELL, and say which check was unclear."*

**5. Where you and the lead disagreed.**

> *"Below are two sets of grades for the same [30] tickets against the same three checks, one from me and one from my support lead. List every ticket where we disagree. For each, quote the check and the part of the ticket we probably read differently, and suggest one sentence that could be added to the check so that two people would grade it the same way. Do not decide which of us was right."*

**6. A month later.**

> *"Here are our three checks and the grade sheets from the last four weeks. Which check has not caught a single NO in that time? Which tickets were marked NO most often, and do they have anything in common? Suggest whether any check should be retired or replaced, and say what the replacement would need to catch."*

The same prompts work for the next function in the run. Swap "support tickets" for whatever that team's unit of work is (a pull request, an install sign-off, an invoice, a quote), and swap the support lead for whoever runs that desk.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about AI governance (often), AI methodologies (also often), cybersecurity strategy (sometimes), and technology risk (always). Today's argument is that before AI changes how a function works, its manager should sit down with the person who runs it, agree three checks that decide whether the output is right, and run them on last week's real work, because the definition of right lives in that person's head and nowhere else.*
