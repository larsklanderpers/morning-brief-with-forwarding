# Write the Brief. Then Write the Check.

**Status: DRAFT v1 -- Tue 18 Aug 2026 (Diversion, ground game). Unpanelled. One [YOUR TAKE] marker open.**
**Series: Tuesday Diversion -- the lighter register, first run of the two-diversion week. Lightness is a state of being, not a length metric (Lars, 12 Aug). No word-count gate.**
**Thread: Practitioner / Coding Ground Truth · Shape of Work-to-Come**
**Builds on: "You Already Know What Wrong Sounds Like" (Sat 15 Aug -- the write-down-the-tell exercise; this piece names it and adds the missing half). Hands forward to Sat 22 Aug.**
**Source: week-plan_2026-08-17.md (v2) · Vault/Writing/Signals/Specification is the chokepoint - the evidence is mixed.md**

**DELIBERATE EXCLUSIONS -- do not reinsert at panel:**
**- The Anthropic 400k-session verified-success figure (~26-30%) belongs to Sat 22. Gestured at here, never printed. Do not add the number.**
**- Sat 15 owns the archetypes, AI FinOps, the Ramp x Revelio entry-level figure, and "taste" as a controlling image. None reused.**
**- see / hold / grip / sight radius (Sun 16) is burned through today. "Window" (Wed 12) is reserved through today. Neither used.**
**- Mon 17 runs concede-then-sharpen once. Not repeated here.**

---

Nobody renovates a bathroom by calling a builder and saying "fix the bathroom." You would not get what you wanted and you would have no grounds to complain about it.

What you send instead is a scope of works. What is being done, what it costs, what materials, what stays and what goes. And at the bottom, the part most people skim past and every builder reads twice: what counts as finished. Because that clause is the only reason the last ten percent of the job ever happens.

On Saturday I asked you to write down three things you would catch that a new hire would not, hand one of them to an agent without the tell, and watch it fail. A few of you did it and told me about it, which made my weekend. What I did not say, because the piece was about something else, is that the exercise has a name and a second half.

The name is specification. The second half is the one nobody writes.

## The half everybody already knows about

There is a genuine skill forming here, and the market has not settled on a name for it. Prompt engineering was the wrong name and is already curling at the edges as a job title. The thing that is actually scarce is more boring and more valuable: writing a brief clear enough that somebody -- or something -- executes it without coming back to you six times.

If you have ever written a decent handover document, or briefed an agency, or told a contractor what you actually wanted, you have done this. The shape does not change much:

**The goal, in one sentence, stated as an outcome rather than an activity.** Not "look at the customer data." What you want to be true at the end.

**The constraints.** What it cannot touch. What it must not change. Which systems are out of bounds and which are read-only. This is the section people skip and it is the section that prevents the expensive kind of mistake.

**What to do when it gets stuck.** Stop and ask, or make a reasonable call and flag it? Both are legitimate. Neither is obvious. If you do not say, you get whichever one the machine feels like today, and you will get a different one tomorrow.

**And what "done" looks like.**

That last one is where almost everybody stops writing, right at the moment it gets useful. "Done" gets written as a feeling. Make it good. Clean it up. Get the report into decent shape. Then the work comes back, it looks plausible, it is formatted nicely, it is confident, and you have absolutely no way of telling whether it is right.

## The half nobody writes

Here is the uncomfortable research, and I am going to give it to you straight because I think it is the most useful thing I have read all year about working with these tools.

A group called METR ran a proper randomized trial with sixteen experienced open-source developers, on two hundred and forty-six real issues, in mature codebases they already knew well. Not a benchmark. Their own repositories, their own work.

The developers using AI tools took **nineteen percent longer**.

That is not the interesting part. Before they started, they predicted the tools would speed them up by about a quarter. Fair enough, everybody is optimistic. But afterwards, having actually done the work and taken measurably longer at it, **they still believed they had been sped up by around twenty percent.**

Read that again. Experienced professionals, on their own code, could not tell which direction the needle had moved. Not "were unsure." Believed the opposite of what happened.

I want to be careful with this, because it is one study and it has limits its authors are the first to name. It does not show these tools fail to speed people up generally. It does not generalize past software. It says nothing about less experienced people, or unfamiliar codebases, and there may well be learning effects that only show up after fifty hours or more with a tool. I am not telling you to put it down.

I am telling you that the thing you cannot do reliably is judge, by feel, whether what came back was any good. And if that is true of a senior engineer looking at their own code, it is true of you looking at a market summary, a first-pass contract review, or a reconciliation.

Google's DevOps research found the same thing from a different angle: as AI adoption goes up, throughput goes up **and** delivery instability goes up, at the same time, in the same teams. They have a name for the cost, and it is a good one. The verification tax. One of their respondents put it better than any analyst has: *"I feel somewhat more productive, but it's at a cost. While I end up spending less time writing code, I spend more time babysitting the AI."*

So the chokepoint moved. It just did not move where everyone assumed. It did not land on writing the brief. It landed one step later, on knowing whether what came back is right.

## Which is why the check is the whole thing

A check is not a feeling about quality. It is something that comes back true or false without you having to squint.

It can be almost embarrassingly small. A test that runs. A number that has to reconcile to another number you already trust. A total that has to match last month's within a range you can state. A specific record you know the answer for, that you deliberately leave in the pile to see whether it gets handled correctly. A sentence you know should appear, or should never appear. A count that has to come out even.

The trick is that you have to write it **before** you see the output. Afterwards is too late, because by then you have read the thing, and it was fluent and organized and confident, and your judgment has already been quietly recruited. That is the whole mechanism behind the twenty percent. Nobody in that study was lazy. They were persuaded, by good-looking work, in a way that is very hard to feel happening.

Writing the check first is how you take that decision away from your future self, who is going to be tired and busy and pleased that the thing came back at all.

And once you have written one, you own something more valuable than the output. You own a way to tell. Which means you can hand that task over again next week without re-reading everything, and the week after that, and that is the point at which any of this actually starts saving you time rather than relocating it.

<!-- [YOUR TAKE]: The best version of this piece has one of your own here -- a real brief-and-check from your own work, described concretely. The obvious candidate is the editor panel: it is a specification with a numeric bar attached, which is exactly why it returns a verdict instead of an opinion. Whatever you pick, the payload is that YOU built the check and what it caught that you would have waved through. A short cost story works well here too -- a time you accepted good-looking work and paid for it later. -->

## Twenty minutes tonight

**Pick something you already hand over.** Not a new project. Something routine you have delegated before, to a person or to a machine, where you have a rough idea of what good looks like but have never written it down.

**Write the brief on one page.** Outcome, constraints, what to do when stuck. Fifteen minutes, and be blunter than feels polite -- machines do not take it personally and, in my experience, neither do most people once they realize you have removed the guesswork.

**Then write one check. Just one.** The single thing that has to be true for you to believe the result. If you cannot think of one, that is not a failure of imagination, it is the finding -- it means you have been accepting that work on vibes, possibly for years, and now you know.

**Then run it, and watch what the check catches.** It will catch something. It usually catches something small and specific and slightly humiliating, and that is exactly the thing you would have missed on a Thursday afternoon.

## What you have actually just done

You did not learn to prompt. You are not orchestrating anything. There is no platform involved and nobody had to approve a budget.

You took a piece of judgment that lived only in your head -- the standard you apply without articulating it -- made it explicit, and installed it somewhere it can run without you. That is the skill the market is currently fumbling toward a title for, and you can practice it tonight in your own function, on work you already own.

It is also, and I say this carefully, the thing that decides whether any of this is worth the money. Because the tools are going to keep getting better at producing plausible work, and getting better at that faster than they get better at being right.

On Saturday I want to show you a number that puts a floor under all of this, and it is from the vendor's own study of its own product. It is not a comfortable number. It is a lot less uncomfortable if you have spent the week writing checks.

Start with one.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that specification is only the visible half of working with agents, that the expensive half is knowing whether what came back is right, and that the evidence says experienced people cannot judge that by feel -- so the check has to be written down before the output arrives.*
