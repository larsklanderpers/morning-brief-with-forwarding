**Status: DRAFT rv1 -- Monday, 28 September 2026. Drafted headless from Slack on his request, 25 Sep. NOT panelled. NOT scheduled.**
<!--
Drafted 25 Sep 2026 by the Heinlein intake session, on his instruction in #heinlein-inbox ("go ahead and start drafting the Monday and Tuesday pieces").
Plan: References\week-plan_2026-09-28.md, Mon 28 block. Opens the "factory floor" arc.
Research: References\research_mon28-two-thousand-a-month_2026-09-25.md.

TITLE: the plan's working title was "Two Thousand a Month". RETITLED, because the 2,000 is episode-title copy and is not Warp's own figure, and because spelled-out-number headers are at four in the window. Open call #2 in the plan stands: if he listens to the episode and Lloyd says 2,000 on air, the title and the third section both change.

WHAT IS DELIBERATELY NOT HERE:
- "2,000 PRs a month" as Warp's number (DO-NOT-PRINT). The piece turns the absence into a section instead.
- The review-bottleneck argument (Aug coding sub-arc: Write the Brief / Read-Only First / Score the Catch). The 3.5-hour figure is cited once as show copy, and the argument is not re-run.
- METR (excluded by the Monday brief; it runs on Tuesday instead, once, with n=16 said out loud).
- FDE in any form; the agent-orchestrator-as-middle-manager framing (Tuesday's ground); Sun 27's frame and every image it spent; the recall / defect-cost-times-run-count math (that is Sun 4's spine, his words, and Monday must not pre-empt it).
- No spelled-out-number header, no "nobody" header, no bare "The X" header, no open-question close, no "for the price of X" close, no where-you-stand close (Fri 25 just used it).

FOR THE PANEL:
- Microsoft Work Trend Index appears here (2026 edition, Frontier Professionals) and again on Tue 29 (2024 edition, BYOAI). Two different reports two years apart, both attributed in the sentence. Flagged rather than hidden.
- ~3,050 body words.
- One [YOUR TAKE] marker, open.
-->
# What the Line Is Allowed to Build

A small team can now produce more work in a month than it can decide about. That is the change, and almost nothing written about AI coding has caught up to it.

My grandfather-in-law ran a print shop, and the thing I remember about the place was how little of it was printing. The press ran itself once it was running. What the job actually consisted of was the hour before: the proof on the light table, the customer on the phone, somebody with a loupe checking that the phone number in the ad was right, because the press did not care whether the phone number was right. It would produce fifty thousand of whatever you told it to produce, beautifully, at speed, and hand you the pallets. The skill in that building was not making the thing. It was deciding what the thing was before the machine made forty thousand of it.

Software just got a press. Nobody has quite worked out who signs the proof.

## They are not describing a tool, they are describing a job change

Three teams have now published, in their own words, what their engineering work looks like at volume. It is worth reading what they actually said, because the summaries have been flattening it into a productivity story, and it is not a productivity story.

Zach Lloyd, the CEO of Warp, published a post in June titled "We are now factory engineers, not product engineers." The sentence that matters is this one: "The goal of this factory is to ship an incredible product, but the day-to-day job of the engineer is not to build that product directly -- it's to build the thing that builds that product." He goes further in the same post: "The job of every engineer is to improve the efficiency of their team's product factory." And he sets the measure: "It's measured by the percentage of all changes that are shipped automatically."

Read that as a job description rather than as a claim about tooling and it is a different document. The engineer is not being handed a faster way to write the function. The engineer is being moved off writing the function entirely, and onto the question of what the line should be set up to make.

The AWS Kiro team published the same shape in September, from three full-time engineers who merged a thousand pull requests in seven days with something like five hundred community contributors. Their line is the honest one: "Every session still needs someone to define its goal, start it, watch for problems, judge its result, and decide what happens next. Doing those five tasks across 50 sessions becomes a full-time job."

That is not a complaint about AI. It is a description of a job that did not exist two years ago and now takes a person all day.

And Stripe, which matters most here for a reason I will get to, described its internal agents in February: "more than a thousand pull requests merged each week," and "Though humans review the code, minions write it from start to finish."

Now, the reason Stripe matters most. Warp sells software factories. Kiro is an AWS product and the post is about Kiro Crew, which you can buy. Their own throughput numbers are also their product demo, and you should read them the way you read any vendor reporting its own results, which is to say with interest and with your hand on your wallet. Stripe does not sell you an agent. Stripe is a payments company describing its own engineering, with nothing to sell you at the end of the post. When the company with nothing to sell reports the same shape as the two companies with something to sell, the shape is probably real even if the numbers are not comparable.

## The number I am not going to print

I want to be straight about the thing that got me looking at this in the first place, because the honest version is more interesting than the clean one.

There is a podcast episode from 21 September, on Claire Vo's "How I AI," titled "How Warp ships 2,000 PRs a month with AI factories." That title is where the two thousand comes from. It is show copy. I could not reach a transcript, so I cannot tell you that Lloyd says it on air, and I cannot tell you what it counts: opened or merged, human or agent, all repositories or one.

Warp's own published numbers are smaller and more careful than the title. In August Lloyd wrote that "At Warp we are currently automating about 30% of our tasks through our factories and expect this number to rise quickly in the next few months." A Warp engineer wrote a week later about "Warp's internal software factory, which has helped us ship over 300 PRs in the past week." Three hundred a week is roughly thirteen hundred a month, which is more than two thousand a month on one reading and less on another, depending on what either number counts. Both can be true. Neither tells you the share an agent wrote.

So I am not going to print two thousand as Warp's figure, and the argument does not need it. The argument needs one sentence to survive: a named team is shipping at a volume that changes what the job is, and says so in its own words. Lloyd's June post says it without a number attached. That sentence survives. If you see the two thousand quoted this week as a fact about Warp, and you will, notice that every version of it traces back to an episode title rather than to the company.

## What a unit of work costs now, which is the part the CFO will find first

Here is where it stops being an engineering conversation.

Warp published a benchmark case study at the start of September: "Using Benchmarks, we reduced Warp's internal factory cost per PR from $80 to $30." The detail underneath is that they swapped the implementation model, measured compliance on a thirty-task set drawn from their own codebase, and reported it going from 69% to 87% while the cost came down. The benchmark run itself cost $2,130.57 and took under four hours. Vendor numbers, on a vendor's own benchmark, about a product the vendor sells. Take them as a direction rather than as a figure.

The direction is what matters, and Lloyd named the consequence himself in June: "It's going to show up as COGS on the P&L."

Sit with that for a second, because it is a bigger sentence than it looks. Engineering has spent forty years as a headcount line. Salaries, benefits, recruiting, the whole apparatus of R&D. You budget it annually, you defend it annually, and it is famously hard to attribute to any particular thing you shipped. Moving a meaningful share of it onto cost of goods sold turns it into something else: a variable, per-unit cost that finance already knows how to manage, because it looks exactly like cloud spend. And finance manages cloud spend by asking, every quarter, whether you need that much of it.

Whoever owns your AI budget is about to get a spreadsheet with a cost-per-change column in it. Anybody who has watched a FinOps team arrive at a cloud bill knows how the next conversation goes. It does not go "let us build more." It goes "why is this one $80."

That is a good conversation to have, mostly. It is also the conversation where somebody who does not build software gets to set the throughput of the line, and I do not think most engineering leaders have noticed that the lever is being handed over.

## Watch which metric they chose

The detail I keep coming back to is not the volume. It is the measure.

Warp tracks something it calls human interactions per pull request. Claire Vo's own recap page describes it as counting the interventions: re-prompting in Slack, commenting on a ticket, correcting code in a review. And the stated goal is to drive that number down over time.

As a productivity metric that is completely reasonable. Every intervention is friction, every intervention is a person stopping what they were doing, and a line that needs constant hand-holding is not a line, it is a very expensive pair of hands.

As a governance metric it is the same number pointing the other way. Every intervention you remove is also a place where a human being was looking at the work and is now not. The metric does not distinguish between an intervention that was waste and an intervention that was the only thing standing between a bad change and production. Driven far enough, a falling interactions-per-change number describes a line nobody is watching, and it will look like an improvement on the dashboard the entire way down.

I am not saying Warp is doing that. They clearly think hard about it, their own posts list human review of specs and of verification output as steps in the workflow, and they publish an open dashboard, which is more transparency than most. I am saying the metric has two readings, and only one of them ever gets put on a slide.

## What happens to the rest of the system

The counter-evidence to all of this is worth taking seriously, with its limits stated.

Faros AI published a report in April built on two years of telemetry from around twenty-two thousand developers across four thousand teams. At high AI adoption they found pull requests merging 16.2% faster and deployments per week down 11.7%. Median time in review up 441.5%. Incidents per pull request up 242.7%. And this line, which I have seen quoted wrong repeatedly: "Pull requests merged without any review, human or agentic, are up 31.3%." Secondary coverage keeps dropping the "or agentic," which turns a claim about unreviewed changes into a claim about human review specifically, and those are not the same claim.

The caveats are real. Faros sells engineering analytics, so it has a commercial interest in showing you a problem its dashboard can see. The data are correlational across adoption bands rather than controlled, so "teams that adopted AI hardest also had more incidents" is not the same as "AI caused the incidents." There are plausible readings where the causation runs the other way, or where both are caused by a team under pressure.

But the direction is consistent with what the volume companies themselves describe. Warp's answer to more changes is more automated verification. Kiro's answer is a person doing five judgment tasks across fifty sessions all day. Nobody in this story is claiming that the output arrives ready. They are all, in their own way, describing the same thing: the making got cheap, and something after the making did not.

## How many people are actually working like this

Almost nobody, if you read the survey properly, and I want to read it properly because the number is about to be misquoted for a year.

Microsoft's 2026 Work Trend Index, published in May, names a group it calls Frontier Professionals: people who "use agents for multi-step workflows and building multi-agent systems" and who "routinely rethink workflows and identify where agents can augment or automate." The figure attached is 16%.

Sixteen percent of what, though. The survey went to twenty thousand full-time knowledge workers who already use AI at work, across ten markets, run by an outside research firm over about nine weeks. So it is 3,233 people out of twenty thousand AI users, not 16% of workers. And they qualified by self-reporting a combination of three behaviors, which means the category is built out of what people say about themselves, by a company that sells the agents in question.

Cite it for the direction and not the decimal: a real but small minority of people who already use AI at work say they have restructured how they work around it. That is roughly what you would expect of something that is two years old and requires you to rebuild your own job to get the benefit.

Which is the actual point. Three named teams and a slice of a survey is not an industry. It is an early look at a job that is changing shape, published by the people furthest along, and there is a window here before the practice hardens into something everyone copies without asking why.

<!-- [YOUR TAKE]: this is the spot for your own pipeline. You are running a bot fleet that produces more finished work in a week than you could have produced in a month, and you have been explicit that the constraint moved off the making. What does the volume actually feel like from the seat, and where do you personally spend the hour that used to be spent typing? Your real numbers beat anybody else's. -->

## Three questions worth being able to answer

**Know who is allowed to authorize a run.** Not who reviews the output -- who decides that the line should produce this thing at all. In most organizations that decision is currently made by whoever happened to open the session, because nobody has ever had to name it before. It was not worth naming when a change cost a day of somebody's time. It is worth naming when it costs thirty dollars and four minutes.

**Find out what your cost per change is, before finance does.** You may not like the number, and the number may be perfectly fine, but the worst version of this conversation is the one where the first person to calculate it is the person looking for savings. If a meaningful share of your engineering spend is about to move from a headcount line to a per-unit line, the team that owns it should be the team that can explain it.

**Ask what your interventions-per-change number is doing, and whether anybody set a floor.** Falling is usually good. Falling with nobody having decided how far it should fall is a different thing, and it does not show up as a problem until it shows up as an incident.

Lloyd is right that the job changed, and I think he is more right than the people arguing with him. The part I would add is that the new job is not smaller than the old one. Defining what gets built, setting the boundaries, and deciding what the line is allowed to produce was always the hardest part of engineering. It was just previously rationed by how slowly we could type.

The press does not care what is on the plate. It never did. The difference is that we used to have a week to look at the proof, and now we have about thirty-five minutes, and the pallets are already stacking up at the end of the line.

---

[STANDING FOOTER]

<!--
SOURCES (for his reference; kept out of the body per house style)
- Lloyd, "We are now factory engineers, not product engineers," warp.dev, 18 Jun 2026 (PRIMARY): quotes "the day-to-day job of the engineer...", "The job of every engineer...", "It's measured by the percentage of all changes that are shipped automatically", "It's going to show up as COGS on the P&L"
- Lloyd, "Introducing Warp Factories," warp.dev, 18 Aug 2026 (PRIMARY): "about 30% of our tasks"
- Kodithala, "Towards self-improving software factories," warp.dev, 26 Aug 2026 (PRIMARY): "over 300 PRs in the past week"
- WarpBench case study, warp.dev/factories/benchmarks/warpbench, 2 Sep 2026 (PRIMARY): $80 to $30; 69% to 87%; $2,130.57 / 3h46m
- Kiro team (AWS), kiro.dev/blog/software-factory-1000-prs, 18 Sep 2026 (PRIMARY): 1,000 PRs / 7 days, 3 FTE, ~500 contributors, "Every session still needs someone to..."
- Gray, "Minions," stripe.dev, 9 Feb 2026 (PRIMARY): "more than a thousand pull requests merged each week"; "Though humans review the code..."
- "How I AI" ep. "How Warp ships 2,000 PRs a month with AI factories," 21 Sep 2026: TITLE ONLY, transcript unreached (429). chatprd.ai/how-i-ai/inside-warps-software-factory for "human interactions per PR" (host's recap, not a transcript)
- Faros AI, "AI Engineering Report 2026: The Acceleration Whiplash," faros.ai/research/ai-acceleration-whiplash (PRIMARY): 22,000 devs / 4,000 teams; +16.2% merge rate; -11.7% deploys; +441.5% time in review; +242.7% incidents per PR; "merged without any review, human or agentic, are up 31.3%"
- Microsoft Work Trend Index 2026, "Agents, human agency...", 5 May 2026 (PRIMARY): Frontier Professionals 16% of AI users (3,233 of 20,000); 10 markets; Edelman DxI, 18 Feb - 20 Apr 2026; three-behavior classification verbatim

RE-SWEEP BEFORE SCHEDULING
- The episode. If he listens and Lloyd says 2,000 on air, section 3 gets rewritten and the title is back in play.
- build.warp.dev queue numbers were deliberately left out (they are the open-source repo, not the factory, and the queue argument belongs to the Aug sub-arc).
-->
