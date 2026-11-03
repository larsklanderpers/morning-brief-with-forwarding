# The Repo Is Now the Policy Document

**Status: DRAFT v1 -- Wed 19 Aug 2026. Unpanelled. One [YOUR TAKE] marker open.**
**Series: Weekday. Third piece of the "build it" week.**
**Thread: Machine Identity × Practitioner / Coding Ground Truth**
**Builds on: "Which Agents Are Actually Running?" (Wed 12 Aug -- the register; this is its blind spot one week on) · "What It Can See, and What It Can Hold" (Sun 16 -- sight by function, DECLARED callback, first licensed use) · "Write the Brief. Then Write the Check" (Tue 18 -- instructions you choose to hand over; this is the ones nobody handed over).**
**Source: week-plan_2026-08-17.md (Wed 19 section, re-shaped 16 Aug) · References/research_anthropic-80pc_2026-08-16.md (primary pulled 16 Aug) · Claude Platform release notes, 7 Aug 2026 (verified verbatim 13 Aug).**

**DELIBERATE EXCLUSIONS -- do not reinsert at panel:**
**- THE REVIEW-BOTTLENECK ARGUMENT IS TUESDAY'S, one day out, with his own org cited: "the engineers who need to review things cannot keep up with the sheer volume our building engineers can now generate... review of the review." Goldratt / constraint relocation, "mistakes at scale", Deming Point 3 and the KPI/performance-objective/eval bridge are all Tuesday's. NOT re-run here. The Anthropic essay's own Amdahl's-law line and its 8x stat are therefore also OUT even though they were available -- they argue Tuesday's point a day late.**
**- Scope of works / builder / "what counts as finished" -- Tue 18, one day out. Hard burn.**
**- Franchise / till / head office · harness · control plane · transcript -- Mon 17, two days out.**
**- "You are going to build one whether you decide to or not" is Mon 17's close; the "nobody chose this" beat here is deliberately worded away from it.**
**- Section headers avoided by function: Tue 18's five, and the concession-section framings used Thu 13 / Fri 14 / Sun 16 / Mon 17.**

**ACCURACY -- all verified at the primary 16 Aug, research note in References:**
**- Primary is an ESSAY, not a report: "When AI builds itself," Marina Favaro and Jack Clark, anthropic.com/institute/recursive-self-improvement. The page carries NO publication date; 4 June 2026 is established from contemporaneous coverage. The widely-cited "5 June" is Tom's Hardware's date, not the essay's. Written as "in early June" for that reason.**
**- The figure is scoped to ANTHROPIC'S OWN codebase. "80% of production code" without the "its own" is false and several outlets print it that way.**
**- "As of May 2026" makes it three months old on publication. NEVER write "now".**
**- Footnote 3 carried in text: the residual 20% is NOT the human share.**
**- RSI/pause framing deliberately untouched: the essay says "recursive self-improvement is not inevitable" and asks for the OPTION to pause, triple-conditioned. Four outlets got this wrong. Not this piece's story and it would swamp the argument.**

---

Nobody has ever had a serious argument about a style guide. It is advice. You can ignore it on a Friday and no one dies.

Then somebody wires it into the build. Now it is not advice. Now it stops your release at four in the afternoon over a variable name, and the document nobody argued about is the document that decides whether you ship.

Nothing about the guide changed. What changed is that something started reading it and acting on what it found.

## What happened on the seventh of August

There is a line in the Claude Platform release notes from a fortnight ago that I have not seen anybody write about. Here it is in full, because the wording is the point:

> *"Claude Managed Agents sessions can now load skills from a GitHub repository. When a session mounts a repository, any skills in its root `.claude/skills` directory are discovered automatically at session start and available to the agent for that session."*

Read that as a governance sentence rather than a product sentence and it says something quite large. A named directory inside your repository is discovered automatically, at session start, and its contents become things the agent can do.

Not consulted. Not offered as context if somebody remembers to paste it in. **Discovered, automatically, every session.**

For about two years the argument about repositories and AI has been that documentation shapes behavior -- that if your conventions are written down clearly, the agent tends to follow them, and if they are not, it invents something plausible. That was a real observation and it was also soft. Tendencies. Nudges. The sort of thing you could describe to a risk committee without anyone reaching for a pen.

This is not that. This is a filesystem path that loads.

The repo is not *like* a policy document. A directory in it is loaded as executable instruction, on a schedule you do not control, by a process nobody has to remember to trigger.

## Who is writing the code, and the sentence underneath it

In early June, Anthropic published an essay called *When AI builds itself*, by Marina Favaro and Jack Clark. Most of the coverage went after the alarming half, which I am deliberately going to leave alone -- it is a bigger story than this one and it would swallow the argument I actually want to make. What I want is a sentence from the middle.

First the number everybody quoted, in its own words:

> *"As of May 2026, more than 80% of the code we merge into Anthropic's codebase was authored by Claude."*

Two things about that, and both matter more than the number.

It is **Anthropic's own codebase**. Not the industry's, not yours. A good number of outlets printed it as "80% of production code" and dropped the possessive, and that is a materially different claim about a materially different set of buildings. And it is *as of May*, which makes it three months old as you read this, so it is a floor rather than a reading.

The second thing is a footnote almost nobody picked up, and it is more honest than the headline deserved:

> *"Our >80% figure measures the share of lines merged to production that can be attributed to Claude. This is a more conservative measurement in two ways: our attribution pipeline has gaps, and the lines not attributed to Claude include auto-generated code and other artifacts that were not hand-written by humans either."*

So the remaining twenty per cent is not the human part. Some of it is machinery of a different kind. I appreciate them writing that down; most companies would have let the round number stand.

Now the sentence I actually came for:

> *"humans supply the goal, but they no longer need to supply the method."*

Sit with the second clause. If the human is not supplying the method, the method is coming from somewhere. It is not being invented from nothing on each request. It is being assembled out of whatever the thing can see when it starts work.

And here is what I find genuinely remarkable about that essay. It is thousands of words on software increasingly written by software, from the company furthest along on it, and it does not mention conventions, repository documentation, instruction files, or skills. Not once. I went looking specifically and came back empty.

The essay describes the goal moving to the human and the method moving to the machine, and never asks where the method comes from.

## The good news half, and it is real

I want to be balanced here, because there is a version of this that is genuinely encouraging, and it lands on an argument I made on Sunday.

On Sunday I said that every governance instrument has two independent properties -- how far it can see, and how hard it can hold -- and that sight is never chosen directly. You choose what the instrument is *for*, and the scope falls out of the purpose. I said the reason AUSTRAC ages well is that it attaches to a designated service rather than to a technology: it does not care what you built the service out of.

A repository convention has exactly that shape. It does not say "when using tool X, do Y." It says "in this codebase, database migrations are never run from application code." That constraint is scoped by *what is being done*, and it therefore survives the tool changing underneath it, which in this field is roughly every quarter. Write it once and it holds across a model swap, a vendor swap, a framework rewrite.

That is the best-aged governance artifact most organizations own and nearly none of them know they own it. It costs nothing. It lives where the work happens instead of in a policy library nobody opens. And unlike almost everything else I have written about this month, you can point at it in a system diagram, because it has a path.

I would like to stop the piece here. I cannot.

## The part that should worry a governance person

Ask the ordinary question. **Who approves a change to that directory?**

In every organization I have looked at, the answer is: whoever can approve a change to the repository. It is a pull request. It is reviewed the way a documentation change is reviewed, which is to say quickly, by somebody scanning for typos, with the reviewer's real attention reserved for the code in the same branch.

So the control layer -- the thing that determines what an agent will and will not do inside your codebase -- has the change-control of a README and the operational force of a policy engine. Those two facts are supposed to belong to different objects. They do not belong to different objects anymore.

I want to be careful not to make this sound like sabotage, because that is the least interesting version and the least likely. The realistic failure is duller and much more common. Somebody adds a skill during a sprint because it unblocks them. It is useful, so it stays. Nobody writes down that it is now part of how the organization builds software. Eighteen months later it is load-bearing, it is in every session, and the person who wrote it has left.

That is not an attack. That is Tuesday, everywhere, for two years.

And notice what this does to the register. Last Wednesday I argued that most organizations cannot say which agents are actually running, and that the ones with a register mostly registered what they operate rather than what they rely on. This is the next layer down and it is worse, because an agent inventory at least has a row per agent. Nobody keeps an inventory of what those agents *read on the way in*.

<!-- [YOUR TAKE]: This is the spot for your own repo, and it is the piece's emotional core. The honest version of the question I just asked, applied to you and your co-developer: what is actually in your instruction files and skills directory today, when did each thing go in, who could change it without either of you noticing, and is any of it now load-bearing in a way neither of you would have chosen deliberately? The Friday-14 passage worked because you named a real cost you had already paid. Same register. Long rolling sentences welcome; I will tidy grammar only. -->

## "That is just configuration"

The strongest objection, and I have heard a version of it from people I respect: this is configuration. Configuration has always shaped behavior. A CI pipeline, a linter config, a feature flag, an IAM policy -- all of these have decided outcomes for years, all sit in version control, and nobody demands a governance committee for a `.eslintrc`.

Fair, and I will take most of it. This is a difference in degree rather than kind, and anybody selling it as an entirely new category of risk is selling you something.

But degree is where governance lives. A linter config constrains a narrow, mechanical, checkable thing, and when it is wrong the build breaks loudly and somebody fixes it in ten minutes. An instruction the agent reads at session start shapes *judgment* -- what to attempt, what to leave alone, when to ask -- across work that a person did not specify and will not read line by line. When that is wrong it does not break the build. It ships, plausibly, at volume.

The second objection is better: none of this is a vulnerability, and nothing here has gone wrong that anybody can point to. Correct. I am not describing an incident. I am describing an object that acquired a new job without anybody updating its paperwork, which in my experience is the state most things are in about eighteen months before somebody writes an incident report about them.

## Three commits and a conversation

**Go and read your own instruction files, today, as a governance document rather than as developer notes.** Whatever yours are called -- an agents file, a claude file, a skills directory, a contributing guide the agent happens to read -- open them and ask what an agent would conclude it is permitted to do. Most people have never read them in that register. It takes twenty minutes and it is uncomfortable in a useful way.

**Then run the blame.** Every line in there arrived on a date, in a commit, from a person, for a reason that made sense that week. You are looking for the ones nobody remembers, the ones that arrived to unblock something specific and never left, and anything that reads like a permission rather than a preference.

**Then decide whether that path deserves a different review than the code beside it.** I am not going to tell you it does, because that depends on what you build and who your regulator is. I am going to tell you that in most organizations nobody has made the decision either way, and that not deciding is itself a decision that somebody will eventually have to defend.

**And put one named person on it.** Not a committee. The person who has to be asked before that directory changes. If you take one thing from this week, it is that a control with nobody's name on it degrades into a suggestion at a rate that would surprise you.

## What you are actually looking at

The uncomfortable thing about all of this is how little of it was decided. Nobody sat in a meeting and resolved that a directory in a source repository should become the instruction layer for the software their business runs on. It arrived in a release note, in August, between a bug fix and a performance improvement.

Tomorrow I want to look at the limit of all this, because there is one and it is hard. You can read what the agent reads. You can change it, review it, put a name against it. What nothing in the stack can currently tell you is *why* it did what it did -- whose idea any given action actually was.

For today the smaller point will do. Something in your building is reading a file and acting on it.

Go and find out what the file says.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that a directory in your source repository is now loaded as executable instruction at session start, that this makes it the best-scoped governance artifact most organizations own and the worst-governed one, and that it currently has the change-control of a README and the operational force of a policy engine.*
