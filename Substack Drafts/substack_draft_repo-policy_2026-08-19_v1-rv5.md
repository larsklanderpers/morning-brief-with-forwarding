# The Repo Is Now the Policy Document

**Status: v1-rv5 -- Wed 19 Aug 2026. Panel Round 5 = 9.5 (bar 9.0), slop 9.5 at floor, no open [VERIFY], **PRE-PUBLISH GATE CLEARED**. Body ~2,900w.**
**rv5, two changes, both at Lars's direction:**
**a) ★ HARNESS CALLBACK ADDED -- he was right that the piece pointed at it and did not pick it up, and that readers would notice. Built from his own wording ("the harness you choose or build", "external control", "stay focused on implementing it correctly"). Placed immediately after the Datadog ordering beat, which is where the reader feels the gap. Declares the callback to the week's opening argument (Wed 5 Aug via Mon 17: "a model can talk its way around its own instructions, and it cannot talk its way around a barrier that lives outside it and holds"). Closes with the qualification that keeps the piece honest: reading what your agents read is necessary, and it is not the only place to defend. NOTE: kept to GENERIC "external control" rather than naming deny rules -- those are Fri 14's, five days out and inside the Seat 5 window, and naming them would re-argue rather than call back.**
**b) DATADOG GATE RESOLVED WITHOUT A CHORE. The verbatim sentence in rv3/rv4 was The Hacker News quoting Datadog (ThreatsDay, 6 Aug), and Datadog's article body would not render for the research pass. But Datadog's OWN title and meta description carry the substance directly -- "how malicious Claude Code skills can abuse dynamic context commands to execute before model-level prompt injection defenses can intervene" -- so the point is now stated in Lars's prose, attributed to Datadog, without presenting a sentence he has not read as a quotation. Nothing is lost and there is no outstanding gate.**
**Datadog primary, for the record: Nick Frichette and Ryan Simon, "Malicious Coding Agent Skills and the Risk of Dynamic Context," 11 May 2026 -- https://securitylabs.datadoghq.com/articles/malicious-skills-supply-chain-risks-in-coding-agents-with-dynamic-context/**
**AVAILABLE, NOT USED (both on-subject, neither needed): CSA AI Safety Initiative, "Agent Context Poisoning: SKILL.md and the New AI Supply Chain Attack Surface," 6 May 2026 -- the closest thing to a disinterested corroboration. And CybeDefend, "Instruction File Injection: AGENTS.md and CLAUDE.md," Aug 2026 -- most on-point of all and a vendor selling the remedy, so it would need naming as such.**
**PRIOR STATUS: v1-rv4 -- Wed 19 Aug 2026. Register raised on the malicious beat at Lars's direction ("the statement was tongue in cheek but sure, let's make it more serious again"). Panel Round 4 = 9.45 (bar 9.0), slop 9.5 at floor, no open [VERIFY]. Body ~2,740w.**
**rv4 CHANGES, three, all in the malicious/exploited beat:**
**a) The pivot into it no longer hedges its way in. "It's easy to see how this could be malicious, and I want to be precise..." -> "The malicious version of that is not hypothetical, and it deserves to be stated precisely rather than reached for." The original wording was calibrated to a joke that is no longer in the text.**
**b) BLAST-RADIUS BEAT ADDED, and it is built out of his own anecdote rather than new research: a shared standards skill is mounted in every repo the team works in, so one line reaches every session on every branch until somebody notices, and nothing raises its hand when the instructions change. Closes on "There is no alert for this. There is a commit." This is the beat that makes the piece land for a regulated reader and it needed no new sourcing.**
**c) The landing keeps his wry register but carries the cost again, which is what makes it serious rather than a shrug: "...It was me being helpful on a Tuesday, and it still cost me a week, and I was looking directly at it the whole time." The last clause is the point -- he had every advantage and it still took a week.**
**NOTE ON THE ORIGINAL JOKE: "look, mom, a whole new type of prompt injection attack!" was tongue-in-cheek, per Lars 17 Aug. It is gone, and the research it triggered stands on its own -- so the exchange was net positive even though the joke did not survive it.**
**PRIOR STATUS: v1-rv3 -- Wed 19 Aug 2026. rv3 REFRAMES THE MALICIOUS BEAT on verified research (`References/research_poisoned-skills_2026-08-17.md`, 17 Aug). Panel Round 3 = 9.4 (bar 9.0), slop 9.5 at floor, no open [VERIFY]. Body ~2,610w.**
**⚠️ THE FRAMING LARS ASKED FOR DOES NOT SURVIVE, AND THE TRUE VERSION IS BETTER. "A new type of attack, already exploited less than two months ago" fails four ways: (1) NOT NEW -- named and tracked since the first week of Feb 2026, with an OWASP Agentic Skills entry (AST01 Malicious Skills). (2) The real in-the-wild event is **ClawHavoc, 27 Jan - 4 Feb 2026** on ClawHub -- six and a half months back, not two. (3) EVERY in-the-wild case is a PUBLIC MARKETPLACE. Repo-resident poisoning -- the piece's actual subject -- is **proof of concept only**. (4) The ~26,000 figure is NOT AN ATTACK: AIR ran that campaign itself with a benign payload, its own write-up is titled "How We Hijacked 26,000 Agents With One Instagram Ad," and AIR sells a managed skills marketplace. NOT PRINTED.**
**WHY THE TRUE VERSION IS STRONGER: the gap between "exploited in a public market" and "not yet published in your own repo" IS the piece's thesis. It lets him say the exploited case required somebody to browse and choose, and his case requires nobody to do anything at all.**
**ADDED, and it is the best find in the dossier: Datadog's point that this class of instruction can execute BEFORE the model sees the skill, so model-level injection defenses never engage. That strengthens the structural argument rather than the threat argument.**
**⚠️ PRE-PUBLISH GATE (not a [VERIFY]; the piece does not hang on it): the Datadog post's BODY was gateway-blocked during research -- title, date (11 May 2026) and authorship verified, body not read directly. Read it before this ships and confirm the wording, or cut that paragraph. Precedent: the Tue 4 Aug Brooks spot-check.**
**CUT ON THE RESEARCH: AutoJack -- not a skills story at all (browsing-agent-to-localhost-MCP chain in AutoGen Studio) and Microsoft says it does not work on current builds. Mitiga's PromptLogger (Aug 2026) is the freshest and most on-point item and therefore the most tempting; the underlying report is not publicly locatable, so it is deliberately NOT used.**
**HELD FOR LATER, worth a piece of its own: every source in this space has a product in the blast radius, and Niv Hoffman is BOTH an AIR researcher on the 26,000 demo AND an OWASP Agentic Skills co-lead -- the taxonomy and the vendor research are not independent. That is the "the market is generating its own facts" pattern from the CLOUD Act note, and it is a 24-30 lead, not a clause here.**
**CVE detail available if wanted: CVE-2025-59536, Claude Code <1.0.111, CVSS 8.7 -- described in the body without the identifier to keep the prose light.**
**PRIOR STATUS: v1-rv2 -- Wed 19 Aug 2026. Lars's _v1 edits kept in full. Editor panel Round 1 = 8.85, Round 2 = 9.3 (bar 9.0), slop 9.5 at floor, no open [VERIFY]. Em-dash-free. Body ~2,390w.**
**[YOUR TAKE] CLOSED by Lars at _v1 -- the shared standards skill, the onboarding skill he accidentally taught a cloud configuration, and the week he could not work out why every agent kept skewing away from their own standards. It is the piece's threat model arriving as a lived cost rather than a hypothetical, and it lifted Taste and Voice a full point between rounds. Untouched except for one paragraph break at the anecdote-to-extrapolation turn and two mechanical fixes.**
**PANEL FIXES AT rv2 (4):**
**a) STRUCTURE -- his new signpost promised TWO concerns and the piece only pays off one. Rather than add a beat it does not need, the second is now explicitly handed to Thu 20, which is the provenance-of-intent piece and was always going to carry it. Converts a structural debt into a forward reference, and the existing close already lands it.**
**b) SEAT 4 -- "a whole new type of prompt injection attack" is contestable and his own backlog refutes it: `SUBSTACK_IDEAS.md` carries a fake-agent-skill item from the 3 Jul brief (a poisoned skill reaching a reported ~26,000 agents, plus AutoJack). Reworded to "a new front door for a very old attack" with the novelty disclaimed in his own register, and the bet placed on inattention rather than malice -- which is the more defensible and more interesting claim. ⚠️ The ~26,000 figure is brief-sourced, NOT primary-verified, so it is deliberately NOT printed. If he wants it in text it needs a research pass first.**
**c) Mechanics, silent: "THere" -> "There", "its also" -> "it is also".**
**d) One paragraph break inserted at "Imagine then" -- readability only. No words cut, no clauses compressed, per the Prime Directive on his rolling sentences.**
**HELD, his call: body is ~2,390w against Mon 4,192 and Tue 3,530. It reads lean rather than thin now that the anecdote is in, and I would rather ship it short than pad it. Flagging so the choice is his, not mine.**
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

I am not sure that anyone has ever had a serious argument about a style guide (though I am pretty sure there are more than a few former interns with trauma about them). Regardless, it is advice. You can ignore it on a Friday and no one dies.

Then somebody wires it into the build. Now it is not advice. Now it stops your release at four in the afternoon over a variable name, and the document nobody in engineering argued about is the document that decides whether you ship.

Nothing about the guide changed. What changed is that something started reading it and acting on what it found.

## What happened on the seventh of August

There is a line in the Claude Platform release notes from a fortnight ago that I have not seen anybody write about (which doesn't mean they haven't, but I certainly haven't seen it from a governance perspective). Here it is in full, because the wording is the point:

> *"Claude Managed Agents sessions can now load skills from a GitHub repository. When a session mounts a repository, any skills in its root `.claude/skills` directory are discovered automatically at session start and available to the agent for that session."*

Read that as a governance sentence rather than a product sentence and it says something quite large. A named directory inside your repository is discovered automatically, at session start, and its contents become things the agent can do.

Not consulted. Not offered as context if somebody remembers to paste it in. **Discovered, automatically, every session.**

For about two years the argument about repositories and AI has been that documentation shapes behavior -- that if your conventions are written down clearly, the agent tends to follow them, and if they are not, it invents something plausible. That was a real observation and it was also soft. Tendencies. Nudges. The sort of thing you could describe to a risk committee without anyone reaching for a pen.

This is not that. This is a filesystem path that loads.

The repo is not *like* a policy document. A directory in it is loaded as executable instruction, on a schedule you do not control, by a process nobody has to remember to trigger. There are two concerns here. The first is what it means for governance when the skills directory is not explicitly considered but implicitly loaded, and that is today's piece. The second is what it means for managing deliberate or malicious instructions sitting in any affected inference set, and that one is big enough to need its own day, so I will come to it tomorrow.

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

My colleague and I use these items quite heavily. He is far better at standards than I, so we use a shared standards skill (even above linting, a means and methodologies skill, to be more clear) in every repo we work in. This is a very common use case for developers. But, because LLMs like to be so helpful, I inadvertently added a specific configuration having to do with a very specific use case to the onboarding skill (call it a cloud configuration vs. an on-premise configuration), and then every piece of code I worked on post that accidental update kept coming back with cloud-facing methodologies and for more than a week I couldn't figure out why the agents kept skewing in a direction so out of whack with our standards.

Imagine then, if the configuration was much quieter, and only came into play when a repo was accessing a specific type of action that you only used every couple of years, and I wasn't paying attention when someone else used the skill. The malicious version of that is not hypothetical, and it deserves to be stated precisely rather than reached for.

Poisoned skills are not a thought experiment. In late January, attackers uploaded hundreds of hostile skills to ClawHub, OpenClaw's public skill market. Koi Security audited all two thousand six hundred and thirty-two listings and found three hundred and forty-one of them malicious, three hundred and thirty-five from a single campaign. Antiy's write-up describes users being socially engineered into installing them, at which point the code ran on their machines. Palo Alto's Unit 42 disclosed five more live ones at the end of June. So this is real, it has actual victims, and it has been tracked as a named class since February -- there is an OWASP entry for it now.

But look at the shape of every one of those cases. They are all a public market. Somebody browsed, chose, and installed. **The version I have just described to you is the one nobody has published yet: a poisoned skill sitting inside a company's own repository, loaded because it is simply there, chosen by nobody this morning.** That one exists so far as a working proof of concept, built by researchers who did not have to work very hard, alongside one patched flaw in which Claude Code could be talked into running code from a project before the user had accepted the trust prompt.

And consider what the blast radius actually is, because it is not one developer having a bad week. A shared standards skill is mounted in every repository the team works in. One line in it reaches every session, on every branch, for as long as nobody notices -- and nothing in the stack raises its hand when the instructions change. There is no alert for this. There is a commit.

And there is a detail in the research that bothers me more than the malice does. Datadog's security researchers, writing in May about exactly this problem, describe how a malicious skill can abuse dynamic context to execute *before model-level prompt injection defenses can intervene.* Sit with the ordering. The instruction does not get argued with and refused. It runs, and then the defenses wake up in a world where it has already run.

That points somewhere, and I would rather point at it than let you find the gap yourself.

If the hostile instruction is inside the context before the model reads anything, then the model is the wrong place to be mounting a defense. Which is the argument this week opened on, and I am going to repeat it because it keeps being the answer: a model can talk its way around its own instructions, and it cannot talk its way around a barrier that lives outside it and holds.

So the answer to this, as with so many other AI-related things, is the harness -- the one you choose, or the one you build. A poisoned or drifted skill can instruct an agent to do something. It cannot make an external control agree to it. That protection does not get overrun this way, provided it is genuinely implemented and genuinely tested, which is the only part anybody ever skips. So stay focused on implementing it correctly. Everything in this piece is an argument for reading what your agents read, and none of it is an argument for making the reading the only place you defend.

Which is why I would still put my money on inattention rather than malice. My cloud configuration was not an attack, and nobody was targeting me. It was me being helpful on a Tuesday, and it still cost me a week, and I was looking directly at it the whole time.

## "That is just configuration"

The strongest objection, and I have heard a version of it from people I respect: this is configuration. Configuration has always shaped behavior. A CI pipeline, a linter config, a feature flag, an IAM policy -- all of these have decided outcomes for years, all sit in version control, and nobody demands a governance committee for a `.eslintrc`.

Fair, and I will take most of it. This is a difference in *degree* rather than *kind*, and anybody positioning it as an entirely new category of risk is selling you something (and I am most certainly not).

But **degree** is where governance lives. A linter config constrains a narrow, mechanical, checkable thing, and when it is wrong the build breaks loudly and somebody fixes it in ten minutes. An instruction the agent reads at session start shapes *judgment* -- what to attempt, what to leave alone, when to ask -- across work that a person did not specify and will not read line by line. When that is wrong it does not break the build. It ships, plausibly, at volume.

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
