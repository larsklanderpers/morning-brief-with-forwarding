<!--
SUPERSEDED 3 Nov -- built from an earlier upload; current text is rv3+. DO NOT DRAFT FROM THIS.
DRAFT rv2 -- Tue 3 Nov 2026 (file keeps its 20 Oct date until it schedules). Changing Management. Function: SUPPORT.
Source: Lars's draft2 (uploaded 3 Nov, ahead of the Google Doc pass and of v1). Plan: References/week-plan_2026-11-02.md, Tue 3 Nov. TUESDAY GATE: PASS.
rv1 changes (3 Nov, mechanical, on his word): typos and dropped words; dates corrected to a 3 Nov run (AC Digest 19 Oct = "a couple of weeks ago"; Tue 13 = "a few Tuesdays ago"; Sat 10 router = "a few weeks ago"); Jev day count 45 -> 35 (Jev on his mail since end of Sep, per Sat 10); one sentence added to the Jev paragraph on his word (checks run on email first, then expanded; the question is the key). [YOUR TAKE] 3-5 removed: he confirmed the support-lead meeting happened and the draft describes it. Review appendix stays in the draft until final (his word); a copy is in Substack Drafts/notes_first-conversation_review-appendix_2026-11-03.md.
FOOTING: one outside source, AC Digest "Your AI Needs a Review Queue" (Marco Kotrotsos, 19 Oct 2026); commercial interest (TypeSafe makes Jev) named in text.
Lars's own contractions kept as written.
rv2 changes (3 Nov, reduced editor panel: Voice / Slop / Skeptic; safe fixes only): HIS text, typos/mechanics only -- "the Inbox" -> "the inbox" (Jev para); "would have serious" -> "would have a serious"; "inference based" -> "inference-based"; "for me, at least, pretty sure" -> "for me, at least; pretty sure"; comma after "while they were installing"; trailing space and two stray blank lines (removed [YOUR TAKE] slots) cleared. DRAFTER text -- header alt-text em-dash removed; "every time" cut from the added Jev sentence (clashed with "almost always" later); "the post does not mention" -> "the part of the post that is free to read does not mention" (only the free portion was read, 20 Oct); two negate-then-correct frames cut ("Your job ... is not to bring the answer", ", not an answer"); header "Prompts for the first sitting" -> "Two prompts to bring to the hour" (Tue 13 ran "Prompts for the next review"); close's "out of their head and onto the page" -> "written down" (repeated the Grade-separately paragraph). Review appendix re-appended after the footer on his word (3 Nov): REMOVE BEFORE SCHEDULING. Proposals for his text are in the panel report, not applied.
-->

# The First Conversation

![The First Conversation, by Lars Klander](<C:/vc-personal-projects/Morning-Brief-with-Forwarding/Substack Graphics/first-conversation-header-final.png>)

*Before AI changes how a function works, sit down with the person who runs it and agree how you will both know it got the job right. That conversation is an eval, and you do not need to be an engineer to run one.*

Most teams were told to start using AI this year. Very few were told how anyone would know whether it was doing the job right.

Think about a new cook on a restaurant line. Nobody good hands them the recipe book on day one and walks off. The head chef stands at the pass for the first few nights and tastes the plates before they go out: is it seasoned, is it hot, does it look like the dish on the menu. The recipe tells the cook what to do. The tasting tells both of them what "done" means, and it is the tasting that makes the cook trustworthy, not the recipe. Trust me, as a pretty iffy cook, I can promise you with confidence that the recipe alone does not make the meal.

Most AI rollouts I have seen hand the team the recipe book. Here is the tool, here is the training video, here is the license. Nobody stands at the pass. Nobody makes sure the recipe is even prepared or followed, let alone that the outcome is tasty and correct.

A few Tuesdays ago, I handed over one act, for one manager and one document: trace every claim in a review back to something you actually saw, or strike it. This week starts the run I promised then, function by function, and it starts with support. If you read the Saturday piece on my inbox router a few weeks ago, you will remember I said the help desk was coming on a Saturday. It moved here, because before it is a build, it is a conversation with the person who runs support, and that makes it a management question first.

On the topic of the inbox router and our friend Jev from TypeSafe and his ilk in the Decision API space, I have since embedded the classification engine concept into a number of things that we do in the business, not just the inbox. The performance of Jev has been reliable enough that we have also added it to a number of areas of the business. We have added classification to tickets, and to the determination of likelihood of match of issue to solution; to the necessity of a response from me to a technical issue from a partner, or if it can be as easily answered by a junior or even advanced engineer. We've also added it to the weighting of certain design decisions in building new products, to the evaluation of PR changes for accuracy, and to model routing criteria for cost. I ran the checks on the email first, and only expanded it once the classification held up there; what made it hold up was how good the classification question was, because a badly framed question is a bad rubric and gets bad answers. In short, it's proven itself, and we have used it, and for all those use cases, it's still so far cost me less than $100 after 35 days.

So, like I did with the Inbox Triage and Jev Router example, we're going to take a brief look at the help desk. Same shape as the last few weeks: what I think is going on, what I would do about it, and something you can use this afternoon.

## Nobody wrote down what right means

Ask a support lead what a good ticket looks like and they can tell you in about thirty seconds. The customer got an answer that was actually correct, it went to the person who could fix it, nobody had to ask twice, the ticket was responded to within the SLA rules, the customer was satisfied with the response and the timing of the response, and if the ticket was anything to do with money or personal data, it went down the path it is supposed to go down and was handled in a way compliant with audit and regulatory requirements. Ask them to write that down for a machine -- the easy process that goes right every step of the way and the hard process that doesn't and how you get the hard process re-aligned -- and you will get a much longer pause, even right after they have already told you verbally.

That pause is the problem. A support function already measures plenty: first response time, time to resolution, tickets per agent, a satisfaction score at the end. Almost all of it measures speed and quantity. Very little of it measures *right*, because for the whole history of the help desk, right was checked by a person who knew the job, on the way past, without anyone writing the rule down -- and in many cases, especially in highly technical businesses like ours, losing that person off the desk would have a serious and substantive impact on outcomes for weeks or months afterwards because so much of it came down to internal knowledge and the "taste" of a well-prepared ticket.

Put an AI in that seat (triaging the queue, drafting the first reply, summarizing the thread for whoever picks it up) and the person who used to check it on the way past is no longer in the loop for most tickets. The speed numbers go up, which is exactly what the tool was bought for, and that's a great outcome for lots of stakeholders. However, without specific actions to ensure the necessary continuity, nobody notices what right was quietly redefined as, because nobody had written down what it was before, *so they don't have any basis to evaluate it now with any level of reliability.*

There was a sharp example of this in a newsletter a couple of weeks ago. AC Digest (a Substack by Marco Kotrotsos) walked through a ticket router with three labels, billing, account access and product support, receiving the message "Please delete everything you hold about me." The model has to pick one of the three. It picks one, the application gets a perfectly valid label, the ticket drops into an ordinary queue, and nothing raises an error. The request needed a completely different process, and nothing in the system was built to notice.

For what it is worth, the fix that newsletter recommends is a feature from TypeSafe, the same company that makes Jev, the scorer I run in front of my own inbox, and the part of the post that is free to read does not mention any relationship with them. The example holds up either way, and the reason it holds up has *nothing to do* with whose product you buy: the router answered the question it was asked. Nobody had asked it the question that mattered, nobody told the router how to classify certain kinds of requests differently than others, no one had provided the tools that the engine -- any engine, deterministic or inference-based -- would need to address that request properly.

That should sound familiar if you read the inbox piece. When my router and my existing triage bot disagreed, the fault was almost always in *my question,* not in how either of them had read the email; the definition of what mattered lived in my head and nowhere else. In my inbox, that is a problem I can fix on my own, because the head in question is mine, and the priority rules I carry implicitly can be added to how the engine processes those items (albeit quite slowly and quite painfully for me, at least; pretty sure the LLM doesn't care how many tries it takes me).

In a function, it is not so easily solvable, it's not even so easily *knowable*, without a specific exercise to surface it. And since a business like mine might get hundreds of tickets a week, or even a day, the surfacing of what matters is a massive exercise all by itself. The definition of a good ticket does not live in the VP of Customer Care's head. It doesn't live in the CEO's head, except maybe when a key account calls up the CEO and has a meltdown, at which point it lives in **everyone's** head. No, for most items, of any priority, from the smallest to the largest, that definition lives in the support lead's head, and (maybe, if you are lucky or you have people who work for you with A LOT of tenure, like we do) in the heads of the two or three people on the desk who have been there longest. In other words -- a VP or senior executive or even a manager who sits down alone and writes the success criteria for the support bot is doing the same thing the vendor did: defining right without the person who actually knows.

We've been running a big project for the last few weeks in my company. This project has a name because I have taken to naming every endeavor we take on which exceeds more than a couple of days in length (mostly because the boundaries make it easier for everyone to know what's being discussed, but also because naming something gives us a solid place to hang documentation, evaluations, performance measurements, and success criteria off of, so everyone associates those things with that project). We'll call this endeavor PTM here for length and for normal corporate protection reasons. What really matters is that this is the first time, really, we have done a project of this size and scale in about 5 years, and because we have a different team now than we did then, I had the absolute luxury of being able to attack the project process in a slightly different way. Now, historically, for most of our big projects, I would do it myself, or I would have one or two senior engineers working with me if the size of the project was too big for me to handle it alone, in a timely fashion. There were a lot of reasons for this methodology but the single biggest was probably that we just didn't write enough things down -- all of our really key, fidgety details lived in the heads of the seniors, so we were the only ones the company could de-risk these projects with. It's probably obvious without me saying it but this is not a scalable model, by any stretch, and it's not really, at the end of the day, a *reliable* model because it's held up entirely by effort, not structure.

So, this time, with more resources at my disposal and a deeper bench of sharp, qualified people, we decided to shift gears and have the team do the installations and upgrades, because we felt they were ready. The original plan was that I would do one and they would watch, and then they would go off and do the rest themselves -- I gave them a recipe, and I expected them to cook it. But like most chefs writing something down for the first time, I forgot things in the recipe -- some thyme over here, a pinch of salt over there -- and almost immediately the deliverable set started to drift. So, we went back to the drawing board. I did five more presentations with the whole team shadowing me and asking me questions and the specific goal of trying to get everything we could into the runbooks, so they had the tools to deal with surprises. Then we changed the way of things so that we did the installation/upgrade in two parts, because we found it was much more risky if we tried to do it all at once as there was a core dependency that had to be achieved first in functionality and in time. Then, we did the shadow runs. Then the next week, we flipped it -- I remoted into all of the machines where the team was installing, while they were installing, and I had one of my screens laid out like the intro to the Brady Bunch or the Hollywood Squares, and THEY did the installations, but I watched them the whole way, I observed the taste of the deliverables, and we wrote a complete evaluation package for them to do at the end to verify that what was delivered tasted, looked, smelled, and was cooked, exactly to the specifications provided. And this process resulted in a far more successful rollout and a far more successful adoption for each of the impacted customers -- not because we radically changed anything we were delivering, but because we *completely* changed the way we delivered it.

## An hour with the person who runs support

So, especially in light of that ongoing experience and everything that I have learned doing it, notwithstanding everything *THEY* have learned, here is what I would do, and what I am proposing for every function in this run: before AI changes that function's week, the manager sits down with the person who leads it, and the two of them agree on three checks of the work now done by the team that can then be used to decide whether the AI's output is right. Then they run those three checks, together, on last week's real work, done by the team alone; then on Friday they run the same three checks, together, against this week's real work, from both the team and the new product solution.

That is an **eval** (short for evaluation: a test you run on what the tool *produced*, not on the tool itself), and give yourself props, because while it's easy to do with code, it's way harder to do with people. Engineers run them on code, processes, and solutions all the time, and the word makes them sound like engineering. They are not, or at least not only. An eval is the written-down version of the head chef tasting the plate, and the hard part has never been the tasting; it is agreeing what the dish is supposed to taste like. That part is a management job, and as importantly as anything else, wherever it can be, *it should be done before you start doing the work*, so that even if you change your mind over time, the drift has a known starting point, which gives you at least a reference point as everything changes.

**The lead writes the checks; you ask the questions.** Your job in that hour is to keep asking "how would someone who was not here know that?" until each check can be answered yes or no by a stranger looking at a single ticket. "Was the customer happy?" fails that test. "Did the reply answer the question the customer actually asked, in the first message back to the customer?" passes it.

**Three, because you are going to run them by hand.** The temptation is to write twenty. Twenty checks is a policy document, and nobody reads a policy document against forty tickets on a Thursday afternoon. Three is enough to catch what matters most, and small enough that the lead will still be doing it in a month. You can add a fourth later, once one of the first three stops catching anything for several days in a row (a week is a good, round, knowable metric).

**One of the three is about what the bot was not built for.** Every one of these tools is built around the cases somebody thought of. The ticket that does not fit any of them (the deletion request, the legal threat dressed up as a billing complaint, the customer who is clearly in some kind of trouble) is where the damage happens, and it is the one check most teams leave out because it is the hardest to write. Ask the lead: "What is the ticket that would worry you most if it went down the normal path?" Whatever they say, that is check number three. For us, that check is almost always a regulatory one -- "what happens if someone calls in to complain that banned or self-excluded members are not being stopped at the boundary like they should be?"

**Run it on last week, not on next week.** Pull twenty or thirty tickets your team closed last week, where you already know how each one ended. Put the AI's version beside what your people actually did, and grade both against the three checks. You are not waiting for something to go wrong in production to find out what right means; you are finding out on work that has already been done and cannot hurt anyone what right actually looks like and where the variances in your definition intersect with delivered actual.

**Grade separately, then compare.** You and the lead each grade the same tickets without looking at each other's answers. Every ticket where the two of you disagree is a check that is not written clearly enough yet. Those disagreements are the most valuable thing the hour produces, because each one is a piece of the lead's judgement coming out of their head and onto the page. Rewrite the check until you both grade that ticket the same way.

None of this needs a line of code. The tickets are already in your help desk, every help desk I have used will export them, and any general-purpose assistant your company has approved can do the sorting and the first pass of grading (prompts below). The bot being evaluated can be anything: a triage router, a reply drafter, a summarizer. The conversation is the same.

What it costs is an hour of the support lead's time, an afternoon of yours, and the uncomfortable feeling of finding out how much of the job was never written down. The tooling, if you use an assistant to do the first pass of grading, rounds to nothing next to that. Set that against what it costs to find out from a customer, or a regulator, that a ticket went down the wrong path for six weeks and nothing raised an error.

There is a quieter benefit too. A support lead who helped write the checks owns the result in a way that a support lead who was handed a dashboard never will. When the bot gets something wrong, and it will, the conversation is "our check caught it" rather than "your tool broke my queue." In my experience, that difference decides whether a team adopts the thing or works around it.

## Two prompts to bring to the hour

Two to use today. Strip customer names and contact details before you paste anything, and use your company's approved tool.

The first turns last week's tickets into a starting list for the conversation. It is a list for you and the lead to argue with:

> *"Here are [20] support tickets my team closed last week, each with the customer's message, our reply, and how it was resolved. Do not judge them. First, list the decisions an agent had to get right on each ticket. Then propose no more than five checks that someone who was not there could answer YES or NO from the ticket alone, to tell whether it was handled right. For each check, name two tickets from this set where it would have made a difference."*

Take that list into the room, and let the lead cross things out. What survives, in the lead's words, is your three.

The second grades the bot's work against the three checks you agreed:

> *"Here are three checks my support lead and I agreed, and [30] tickets, each showing the customer's message, what the AI produced, and what our team actually did. For each ticket, answer each check YES, NO or CAN'T TELL for the AI's version, and quote the line that decides it. Do not fix anything and do not suggest better replies. At the end, list every ticket marked CAN'T TELL, and say which check was unclear."*

The CAN'T TELL list is the one to take back to the lead. Every entry on it is a check that needs another sentence.

There is a fuller set at the end, including a prompt for finding the tickets your categories do not cover.

## Next week, a different desk

Next Tuesday the run moves to another function, with the same hour and the same three checks pointed at different work. Support goes first because it is the most constant feed most of us have, and because when a support bot gets something wrong, a customer usually finds out before you do.

The bot can be wrong in more ways than anyone could list. Your support lead already knows the three that matter, and the whole point of the hour is to get those three written down before the tool is the only one looking.

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

---

## Draft review only -- 3 November 2026 -- remove before publication

These are header alternatives and suggested responses for Lars to consider. The article above and its three open [YOUR TAKE] markers are retained. Suggested language below is not a record of an interview or confirmation that a support-team exercise took place.

### Header alternatives

**Option 2: The Recipe’s Missing Something**

![Option 2: The Recipe’s Missing Something](<C:/vc-personal-projects/Morning-Brief-with-Forwarding/Substack Graphics/first-conversation-options-2026-11-03/header-option-2.png>)

**Option 4: Perfectly Filed. Entirely Wrong.**

![Option 4: Perfectly Filed. Entirely Wrong.](<C:/vc-personal-projects/Morning-Brief-with-Forwarding/Substack Graphics/first-conversation-options-2026-11-03/header-option-4.png>)

**Option 5: The Same Ticket, Two Verdicts**

![Option 5: The Same Ticket, Two Verdicts](<C:/vc-personal-projects/Morning-Brief-with-Forwarding/Substack Graphics/first-conversation-options-2026-11-03/header-option-5.png>)

All three images: 1200 x 630 pixels, generated with the built-in imagegen tool and checked after resizing. Prompts: `Substack Graphics/first-conversation-options-2026-11-03/generation-prompts.txt`.

4 November: Lars selected option 2. The titled final header, with byline Lars Klander, is embedded at the top of this draft and saved as `Substack Graphics/first-conversation-header-final.png` (1200 x 630, lettering and dimensions checked). Alternatives below remain for reference. Proposed reflection is under Lars's review; he will supply a real disagreement example after considering it.

### YOUR TAKE 3 -- the checks

**My reading:** You have already supplied the ingredients: correct answers, appropriate ownership, response deadlines, and exceptions involving money, personal data or banned/self-excluded members. I do not have a record of the exact checks you and the support lead agreed. The useful answer here would name what the bot actually does first (route, suggest a solution, or draft a reply), then give the checks appropriate to that output.

**Three candidate checks, inferred from your draft:**

1. **Right answer:** Does the proposed reply address the customer's actual question, with its technical recommendation supported by the approved solution or recorded evidence? For a router-only test, substitute: does the selected category match the issue described?
2. **Right next step:** Does the ticket record the owner and next action required by the agreed routing rule, within the applicable response deadline? For a router, score the assignment; score actual response timing separately from what the router produced.
3. **Right exception path:** Where the message describes an exception covered by the agreed escalation rules, does the record show that it entered that process? Your own banned/self-excluded-member example is the strongest concrete illustration. The check needs the actual trigger and required action written down; “regulatory issue” alone leaves too much interpretation.

Check three is the “not built for this” check. A fluent answer or tidy category cannot compensate for missing an exception. These are candidate headings: write the precise rule beneath each so a stranger can grade it from the ticket. Missing evidence should be CAN'T TELL, rather than an assumed pass.

**Suggested wording if you are describing your recommendation, rather than a completed meeting:**

> For our desk, I would start with three questions. Did the answer actually address the problem the customer brought us? Did the ticket get to the person who could take the next required action, within the time our process allowed? And did we recognize the cases that needed a different process altogether? That last one matters particularly in our business. A report about banned or self-excluded members getting past a boundary has to be recognized as that kind of problem before anyone congratulates the system for finding a plausible category for it. The work with the support lead is to turn each of those questions into something another person can check from the record, without needing to borrow the lead's memory.

**What only you can supply:** Were these actually your checks, and what exactly did the exception rule require the bot to do? If the support exercise has not happened yet, keep “I would”; your real PTM experience already provides the evidence for why you recommend it.

### YOUR TAKE 4 -- what went wrong first

**My reading:** You have substantially answered this already in the PTM passage. You assumed one demonstration and a runbook transferred enough of your experience for the team to reproduce the outcome. The early drift exposed omissions in your instructions. You then did five more presentations with questions, expanded the runbooks, separated the work around a core dependency, ran shadows, and watched the team perform the installations themselves. That is much stronger than inventing a separate support-bot failure.

The emotional detail is your responsibility for the initial handover. The draft says you had a capable team and a deeper bench. It also says the earlier delivery model depended on the seniors keeping the fidgety details in their heads. The story gives you room to explain what it felt like to discover that some of the missing capability was actually missing documentation and shared criteria.

**Suggested reflective paragraph, based on that account -- your interpretation to approve:**

> What I got wrong first was how much of my own experience I thought I had managed to put into the instructions. I had a capable team, I had shown them the work, and I thought the runbook contained what they needed, but when the deliveries started to drift it became apparent that I was still supplying parts of the process from memory every time I did it myself. Those little decisions felt obvious to me because I had been making them for years, which was not much use to the person trying to follow what I had actually written. The additional sessions gave the team a chance to ask about those decisions while they could still see me making them, and watching them do the work afterwards showed us where the documentation still needed help. That was uncomfortable, because I had to examine the handover I had given them as closely as the work they were giving back to me.

**Placement:** Use a short reflection beside the existing PTM story, or fold it into that passage. Do not repeat the whole sequence at the open marker. Your inbox essay supplies corroborating context: you explicitly described realizing that vague instructions to the bots probably explained some past staff misunderstandings too.

**What only you can supply:** Did you initially think the team had missed something you had explained, before realizing it had never made it into the runbook? That would sharpen the scene if true. It is not established by the current text, so I have not put that reaction into the proposed paragraph.

### YOUR TAKE 5 -- the disagreement (optional)

**My reading:** I cannot recover a specific ticket you and the lead graded differently from the material available here. Do not force this slot. It is optional, and PTM already gives the piece a substantial personal example.

**Best memory prompt:** Think of a ticket where the proposed technical solution was reasonable, but the lead knew that its ownership, urgency, customer circumstances or exception status made that response insufficient. What did you each see in the same record? What information did the lead have that the written check did not? Which sentence did you add afterwards? This is a prompt to recall a real incident, not a claim that one occurred.

**If there is no support-ticket example, a grounded alternative:**

> The closest example I have already written about is from my inbox. Jev and Inbox Manager were making different calls because I had given them different, incomplete versions of what mattered to me. Going through those disagreements forced me to explain priorities that I had been treating as obvious. That is the reason I would spend time on the tickets where the manager and the lead disagree: I would want to find out what one of them knows that the check does not yet say.

This is a brief callback to an established experience, clearly distinguished from a support-lead conversation. My preference is to omit this optional slot unless you remember a particularly useful support example; the draft already makes the inbox connection earlier.

### Basis for these suggestions

- Your supplied draft2, especially the PTM installation account, support-quality criteria, and banned/self-excluded-member example.
- `Substack Published/substack_published_router-in-front_2026-10-10.md`, especially “The first week”: incomplete definitions of “key,” the two bots' disagreement, and your reflection on instructions to staff.
- `Substack Drafts/capture_router-in-front_2026-10-10.md`: supporting interview capture and your rulings. Its historical rollout status is not used to override your newer account here.
- `Writing Flow/feedback_lars_writing_voice.md`: preserve your personal responsibility, explanatory detail and longer reflective sentences.

The draft's opening editorial comment still describes v1 and five open slots. In this supplied draft2, the body already supplies the Jev update and PTM account; the three actual remaining YOUR TAKE prompts are 3, 4 and 5. The week board's older Google Doc summary differs from the supplied draft2 on Jev's status. This review follows the file you selected; no claim is made that the Doc has been synchronized.
