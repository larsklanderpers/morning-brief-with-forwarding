# Research Note -- Warp's "2,000 PRs a month" and what the job becomes at factory volume

For: Mon 28 Two Thousand a Month · Depth: deep · Date: 2026-09-25

Note on method: page text was pulled with a fetch tool that returns extracted text, not raw HTML. Quotes marked "verbatim" were requested word for word and came back consistent across more than one pull, but check every quote you print against the live page before it goes out. Quotes keep the source's own contractions; typographic dashes inside quotes are rendered as "--".

## Bottom line

The thesis survives, but not on the 2,000 number. The strongest evidence is Warp CEO Zach Lloyd's own June 2026 post, which says outright that "the day-to-day job of the engineer is not to build that product directly -- it's to build the thing that builds that product." The "2,000 PRs a month" figure appears only in the episode title and show copy (Lenny's Podcast Network / How I AI), and I could not reach a transcript to confirm Lloyd said it, what counts as a PR, or how many of those PRs agents wrote. Warp's own published numbers are smaller and more careful: "over 300 PRs in the past week" (26 Aug) and "about 30% of our tasks" automated (18 Aug). The claim to print is "a CEO who says the engineer's job is now the factory," not "a team that ships 2,000 agent PRs a month."

## What's solid

- **The episode exists.** Show: How I AI (host Claire Vo), part of the Lenny's Podcast Network. Title: "How Warp ships 2,000 PRs a month with AI factories | Zach Lloyd (CEO, Warp)". Length 47 minutes. Released 21 Sep 2026 on Apple Podcasts, Spotify and the Lenny's Newsletter roundup. Sources (primary): Apple Podcasts episode page https://podcasts.apple.com/us/podcast/how-warp-ships-2-000-prs-a-month-with-ai-factories/id1809663079?i=1000790924004 ; Spotify https://open.spotify.com/episode/2TW2jWnVLGk1B2LJHKTQpP ; YouTube https://youtu.be/4_SHhSMHzNo (unreached, 429); Lenny's roundup post "How I AI: Meta's Muse review + How Warp ships 2,000 PRs a month with AI factories," 21 Sep 2026 https://www.lennysnewsletter.com/p/how-i-ai-metas-muse-review-how-warp
- **Guest and title.** Zach Lloyd, "co-founder and CEO of Warp" -- per the episode's own description on Apple and Spotify (primary: the show's listing). Warp's blog bylines him as "Zach Lloyd" with no title shown. LinkedIn was unreachable (robots.txt). Wikipedia says he founded Warp in June 2020 and previously led the Google Sheets team (secondary, background only). The episode description says he was "a principal engineer on Google Sheets."
- **The factory is called "Wilson."** Episode chapter "(02:35) Introduction to Wilson, Warp's AI software factory." Other chapters that matter for this piece: "(11:12) Engineering leader dashboard features," "(15:18) Code review transformation in AI-powered environments," "(17:08) Cost tracking per PR across different model configurations," "(18:47) LLM-as-a-judge scoring," "(20:02) Identifying and eliminating redundant tests," "(22:19) Self-improvement mechanisms from failed runs," "(28:33) Building cost-quality Pareto charts for model selection." Source: Apple episode page (primary).
- **What the job became, in Lloyd's own words.** Warp blog, "We are now factory engineers, not product engineers," Zach Lloyd, 18 Jun 2026 (primary): https://www.warp.dev/blog/we-are-now-factory-engineers-not-product-engineers . Verbatim lines are in Drop-in facts below. The post sets the metric as the share of changes shipped automatically "and at what cost," says it will "show up as COGS on the P&L," and treats every interactive agent session as "a failure to learn from."
- **Warp's own internal volume and automation share (smaller than 2,000).**
  - "At Warp we are currently automating about 30% of our tasks through our factories and expect this number to rise quickly in the next few months." -- Zach Lloyd, "Introducing Warp Factories," 18 Aug 2026 (primary): https://www.warp.dev/blog/open-infrastructure-for-building-a-software-factory
  - "...Warp's internal software factory, which has helped us ship over 300 PRs in the past week." -- Varoon Kodithala (Engineering), "Towards self-improving software factories," 26 Aug 2026 (primary): https://www.warp.dev/blog/engineering-self-improving-software-factories
- **The human metric is interventions, not output.** Warp tracks "human interactions per PR." ChatPRD's episode page (Claire Vo's own site, 18 Sep 2026) describes it as counting interventions like "re-prompting in Slack, commenting on a Linear ticket, or correcting code in a review," with the goal to "drive this number down over time." Source: https://www.chatprd.ai/how-i-ai/inside-warps-software-factory (host's own recap page -- primary for what the episode covered, but these are the recap's words, not a transcript).
- **Review is the queue.** Warp's live open-source dashboard at https://build.warp.dev (primary, snapshot taken 25 Sep 2026) shows 1,809 issues in "Awaiting maintainer," 1,272 "Ready to implement," 44 "Implementing" and 55 "Reviewing." This covers the open-source Warp terminal repo only, not Warp's internal factory. It still shows the shape of the thesis: agents are not the constraint, the maintainer gate is.
- **Warp's cost per PR fell after swapping models.** "Using Benchmarks, we reduced Warp's internal factory cost per PR from $80 to $30." The WarpBench page gives a median cost per PR of $81.13 (26 Aug) and $19.06 (30 Aug), with task compliance up from 69% to 87% on a 30-task set drawn from Warp's Go/React server and Rust client. The primary implementation agent moved from "auto (genius)" routing to Grok 4.6. Source: WarpBench case study, Zach Lloyd, 2 Sep 2026 (primary): https://www.warp.dev/factories/benchmarks/warpbench . The companion launch post (3 Sep) is narrower: "reduce costs by 63% on certain types of tasks without impacting quality": https://www.warp.dev/blog/warp-factory-benchmarks
- **Microsoft Work Trend Index 2026, "Frontier Professionals" -- verified at primary, with a correction.** Report "Agents, human agency, and the opportunity for every organization," published 5 May 2026: https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization
  - Figure: 16% **of the AI users surveyed** (3,233 of 20,000). This is not 16% of workers.
  - Definition (verbatim): "Frontier Professionals use agents for multi-step workflows and building multi-agent systems. They routinely rethink workflows and identify where agents can augment or automate." Classification rule (verbatim): respondents qualified "only if they reported a combination of three distinct sets of behaviors: Advanced use of AI agents to complete complex or multi-step work; routine redesign of workflows to take advantage of what AI can do well; participation in structured, repeatable AI-enabled practices that can scale beyond individual use."
  - Sample: 20,000 full-time knowledge workers who use AI at work, in 10 markets (US, Brazil, Australia, India, Japan, France, Germany, Italy, Netherlands, UK). 20-minute online survey run by Edelman Data x Intelligence, 18 Feb to 20 Apr 2026. All self-reported.
- **Other named teams reporting agent throughput in their own words:**
  - **Stripe (Minions).** "responsible for more than a thousand pull requests merged each week" and "Though humans review the code, minions write it from start to finish." -- Alistair Gray, Stripe Dot Dev Blog, 9 Feb 2026 (primary): https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents (Part 2, 19 Feb: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2 ). Stripe is not selling an agent product, which makes it the least conflicted of the three named teams.
  - **AWS Kiro team.** "merged 1,000 pull requests in seven days. Over 120 a day, every one went through CI and review." Three full-time engineers built Kiro Crew, working with "nearly 500" community contributors. Role line (verbatim): "Every session still needs someone to define its goal, start it, watch for problems, judge its result, and decide what happens next. Doing those five tasks across 50 sessions becomes a full-time job." -- Zejiang (Joe) Guo, Bolin Chen, Zezhen Xu, Kiro blog, 18 Sep 2026 (primary): https://kiro.dev/blog/software-factory-1000-prs/
- **The skeptical data, at primary:**
  - **Faros AI, "AI Engineering Report 2026: The Acceleration Whiplash."** Two years of telemetry from 22,000 developers across 4,000 teams. At high AI adoption: PR merge rate up 16.2% but deployments per week down 11.7%; incidents-to-PR ratio up 242.7%; median time in review up 441.5%; median time to first review up 156.6%; "Pull requests merged without any review, human or agentic, are up 31.3%"; code churn up 861%. Sources (primary): https://www.faros.ai/research/ai-acceleration-whiplash ; takeaways post, 12 Apr 2026: https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways ; PDF: https://pages.faros.ai/hubfs/AI_Engineering_Report_2026_The_Acceleration_Whiplash_Faros.pdf (PDF not opened).
  - **Faros AI, 2025 "AI Productivity Paradox."** 10,000+ developers, 1,255 teams: "98% more pull requests merged," "PR review time increases 91%," "154% increase in average PR size," and "No significant correlation between AI adoption and improvements at the company level." 23 Jul 2025 (primary): https://www.faros.ai/blog/ai-software-engineering
  - **CodeRabbit, "State of AI vs Human Code Generation."** 470 open-source PRs (320 AI-co-authored, 150 human-only): "10.83 issues per PR, compared to 6.45 for human-only PRs" (about 1.7x); security issues "up to 2.74x higher." 17 Dec 2025 (primary, but a vendor with a stake in the answer): https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report

## What's contested / watch out

- **2,000 versus Warp's own figures.** 300 PRs a week works out to roughly 1,300 a month. 2,000 a month is about 465 a week. Both can be true if 2,000 is total PRs (human plus agent) or a later run rate, but nothing I reached says which. Warp's own 18 Aug figure is "about 30% of our tasks" automated. If 2,000 is all PRs, agents alone may account for well under half. Do not write "2,000 agent-written PRs."
- **"Tasks" versus "PRs" versus "changes."** Warp's posts use all three words for different things: 30% of tasks, 300 PRs, percentage of changes shipped automatically. Stripe says "merged." Kiro says "merged." The 2,000 figure does not say merged.
- **The episode date is inconsistent.** ChatPRD (the host's site) dates its recap 18 Sep 2026. Apple, Spotify and Lenny's date the release 21 Sep 2026. Use 21 Sep as the public release date.
- **"35 minutes to PR / first human review 3.5 hours later."** These appear in the Lenny's roundup copy ("Wilson takes an average of 35 minutes to move from kickoff to pull request. The first human review arrives 3.5 hours later."). They are the show's words, not a verified Lloyd quote or dashboard screenshot. Usable only as "the show reported."
- **Every volume claimant except Stripe sells the factory.** Warp sells Warp Factories. Kiro is an AWS product and its post is about Kiro Crew. Their own throughput is also their product demo. Say so.
- **Stripe's two figures.** The blog says "more than a thousand" merged per week (Feb 2026). "Roughly 1,300 pull requests a week that receive no human assistance until review" comes from the How I AI episode with Steve Kaliski (Engineer at Stripe), 24 Mar 2026, via ChatPRD's recap page https://www.chatprd.ai/how-i-ai/stripes-ai-minions-ship-1300-prs-weekly-from-a-slack-emoji . The recap does not say merged. Use the blog number as the solid one.
- **Microsoft's category is self-reported and partly circular.** People are classified by what they say they do, and then shown to say positive things. A named critique makes this point (secondary: https://themicrosoftcloudblog.com/2026/05/2026-work-trend-index-evidence-check/ ). The base is AI users only.
- **Faros direction of effect.** Faros data are correlational across adoption bands, not controlled. Faros also sells engineering analytics.
- **Kiro "review."** The post does not say whether "review" was human or agent. Do not imply 1,000 human reviews.

## Couldn't verify

- **Lloyd saying "2,000 PRs a month" in his own voice, and what counts.** Lenny's episode page https://www.lennysnewsletter.com/p/how-warp-ships-2000-prs-a-month-with was UNREACHED (HTTP 429 on three attempts). YouTube was UNREACHED (429). No transcript was obtained, so there are no timestamped verbatim quotes from the audio. Unreached, not absent: the transcript likely sits on the Lenny's page.
- **Warp team size and engineering headcount.** Not stated in any Warp primary I reached. Third-party estimates (Tracxn, Latka) were not used.
- **Share of the 2,000 that is agent-authored, and review policy** (whether every factory PR gets a human review before merge). The June post's workflow lists "Human reviews specs" and "Human reviews code and verification output" as steps. That is design intent, not a measured rate.
- **Zach Lloyd's title on LinkedIn.** UNREACHED (robots.txt). His title comes from the episode's own listing.
- **Warp open-source repo merged-PR count.** GitHub Pulse was UNREACHED (robots.txt). I did not route around it.
- **X posts by Lloyd (@zachlloydtweets).** Found in search (the Factories launch thread, the "crawl, walk, run" post) but not opened. None surfaced mentioning 2,000.

## The economics

- **Warp's cost per internal factory PR:** about $80 down to about $30 (median $81.13 to $19.06 over four days in late Aug 2026), after moving the implementation agent to a cheaper model. Warp says quality held: compliance went from 69% to 87% on its 30-task benchmark, and the WarpBench copy says "with merge rate holding flat" (that last phrase is from AlphaSignal's report of the page; confirm it on the page). The benchmark run itself cost $2,130.57 and took 3 hours 46 minutes. Source: https://www.warp.dev/factories/benchmarks/warpbench
- **Illustrative only -- my arithmetic, not a sourced figure:** if 2,000 PRs a month were all factory PRs at $30, compute would be about $60,000 a month, or $720,000 a year. That is a few engineers' loaded cost, which is Lloyd's own COGS framing. If only about 30% are factory PRs, it is about $18,000 a month. Label clearly if used.
- **Lloyd's frame (verbatim):** "It's going to show up as COGS on the P&L." The June post frames factory spend as an ROI test: does a dollar of automation return more than a dollar of value (paraphrase -- quote only the COGS line).
- **Market pattern from the Warp product page (vendor claim):** "most orgs start around 20-30% of PRs fully automated, starting with simple tasks." Source: https://www.warp.dev/factories
- **The hidden cost is review.** Faros 2026 shows median time in review up 441.5% and incidents per PR up 242.7% at high adoption. The per-PR compute price leaves out reviewer hours and incident cost.

## Drop-in facts

- "The goal of this factory is to ship an incredible product, but the day-to-day job of the engineer is not to build that product directly -- it's to build the thing that builds that product." -- Zach Lloyd, Warp blog, 18 Jun 2026. https://www.warp.dev/blog/we-are-now-factory-engineers-not-product-engineers
- "The job of every engineer is to improve the efficiency of their team's product factory." -- same post.
- "Every time we use an interactive agent ... we view it as a failure to learn from." (ellipsis: fetch elided text; confirm full sentence) -- same post.
- "It's measured by the percentage of all changes that are shipped automatically." -- same post.
- "It's going to show up as COGS on the P&L." -- same post.
- "At Warp we are currently automating about 30% of our tasks through our factories and expect this number to rise quickly in the next few months." -- Zach Lloyd, 18 Aug 2026. https://www.warp.dev/blog/open-infrastructure-for-building-a-software-factory
- "...Warp's internal software factory, which has helped us ship over 300 PRs in the past week." -- Varoon Kodithala, Warp, 26 Aug 2026. https://www.warp.dev/blog/engineering-self-improving-software-factories
- "Using Benchmarks, we reduced Warp's internal factory cost per PR from $80 to $30." -- Warp WarpBench case study, 2 Sep 2026. https://www.warp.dev/factories/benchmarks/warpbench
- "Though humans review the code, minions write it from start to finish." / "more than a thousand pull requests merged each week" -- Alistair Gray, Stripe, 9 Feb 2026. https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents
- "Every session still needs someone to define its goal, start it, watch for problems, judge its result, and decide what happens next. Doing those five tasks across 50 sessions becomes a full-time job." -- Kiro team (AWS), 18 Sep 2026. https://kiro.dev/blog/software-factory-1000-prs/
- "Frontier Professionals use agents for multi-step workflows and building multi-agent systems." 16% of AI users surveyed (3,233 of 20,000). -- Microsoft Work Trend Index 2026, 5 May 2026.
- "Pull requests merged without any review, human or agentic, are up 31.3%." -- Faros AI, 2026 report, 12 Apr 2026. https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways
- 1,809 issues "Awaiting maintainer" on Warp's own open-source build dashboard (snapshot 25 Sep 2026; the number changes live, so date-stamp it). https://build.warp.dev

## DO-NOT-PRINT

- **"Warp ships 2,000 agent-written PRs a month."** Unverified at primary. The figure is episode-title copy, and Warp's own numbers (300 a week, 30% of tasks) suggest most PRs may not be factory-made. At most: "a podcast episode billed as 'How Warp ships 2,000 PRs a month.'"
- **Any timestamped Lloyd quote from the episode.** No transcript was reached, so there is nothing verbatim from the audio.
- **"16% of workers use agents for multi-step workflows."** Wrong base. It is 16% of AI users surveyed, self-classified on three behaviors.
- **"31.3% more PRs merge without human review" (Faros).** Secondaries dropped "or agentic." The primary says "without any review, human or agentic."
- **"35 minutes to PR, 3.5 hours to first human review" as Lloyd's words.** This is show copy.
- **Stripe "1,300 merged PRs a week."** The merged figure at primary is "more than a thousand."
- **Warp headcount / "a team of N."** No primary.
- **Excluded by brief:** FDE statistics, "agent orchestrator as new middle manager," METR speed study. None are used here.

## Angles this opens

- **The job is the gate.** All three teams, in their own words, move the human to the ends of the line: spec in, judgment out. Lloyd says "build the thing that builds." Kiro lists "define its goal ... judge its result, and decide what happens next." Stripe says "humans review the code." What the line may produce is decided at spec and at merge. That is the thesis, and it survives -- on the words, not the 2,000.
- **The metric flip.** Warp measures "human interactions per PR" and wants it to go down. For a CISO, that is a governance metric wearing a productivity costume: every avoided interaction is also an avoided control point. Pair it with Faros's "merged without any review, human or agentic, up 31.3%."
- **COGS, not R&D.** If code becomes a variable cost that goes on the P&L like cloud spend, CFOs will manage it like cloud spend, and the $80-to-$30 swap shows who will be pushing on it.
- **Self-modifying lines.** Warp's observer agent proposes changes "to the factory itself," and Warp says it has "merged over ten self-improvement PRs in the last few days" (26 Aug post). Who approves a change to the machine that makes changes? That is change-management territory for the security audience.
- **Vendor-as-witness problem.** The loudest throughput numbers come from companies selling the line. Stripe is the clean control case.
- **Follow-up if Lars wants the 2,000 locked:** retry the Lenny's episode page (the transcript is usually embedded there) after the rate limit clears, or email Warp comms asking three things: merged or opened, share by the factory, and engineering headcount.

## ADDENDUM 25 Sep (episode access attempt, main session)

- **Spotify for Creators episode page** (the link he sent): robots-disallowed to the fetcher. Unreached, not absent. Not routed around.
- **Lenny's episode page** (lennysnewsletter.com/p/how-warp-ships-2000-prs-a-month-with): 429, unreached.
- **Lenny's roundup post** (lennysnewsletter.com/p/how-i-ai-metas-muse-review-how-warp): reached. **No transcript.** Read through a summarising fetcher, so nothing here is verbatim-safe. What it carries:
  - Lloyd is described as "co-founder and CEO of Warp" (show copy; still not confirmed at Warp's own site).
  - Warp Factories turns Slack requests into tracked, tested, merged PRs; the factory system is called "Wilson"; ~35 minutes average from kickoff to PR.
  - The efficiency metric they use is **"human interactions per pull request"**. Useful for Monday, and it is theirs.
  - **Code review remains the bottleneck (~3.5 hours to first human review).** ⚠️ The review-bottleneck argument is the Aug coding sub-arc's (Write the Brief / Read-Only First / Score the Catch). Monday may cite the number, never re-run the argument.
  - The roundup does **not** state or validate 2,000 outside the title.
- **Status of the 2,000:** still show-title only. Needs Lloyd on air (his listen, or YouTube captions) before print.


---
## RULING 26 Sep 2026 (his word, day-start chat)
- **Lloyd says 2,000 on air.** He listened. The DO-NOT-PRINT on 2,000 is LIFTED for the episode claim: print it as said on the episode, not as a figure from Warp's own publications, and keep what it counts (opened/merged, agent/human) marked as unstated.
- **Pending, his:** the Grok AI / "Potato" author's 2,500 figure. Unfooted; not printable until he supplies the source.
- **Added source:** Mollick, "The Overhang," oneusefulthing.org, 18 Sep 2026, fetched at primary 26 Sep (overhang definition; taste quote).

---
## ADDENDUM 26 Sep 2026 -- the 2,500 figure, footed (he supplied the source in #heinlein-inbox)

Full note: `Research Notes\intake\intake_2026-09-26_poteto-2500-prs.md`. Permalink in its frontmatter.

- **Who.** **Lauren Tan, @poteto** (X display name "lauren"). Her own bio, verbatim: "Grok @Bot at
  @SpaceXAI. Shipping with cursor.com/marketplace/cu... React compiler core team, prev cursor, meta,
  netflix". She wrote pstack and Dr. Eggbot, both named in the published Sat 12 piece.
- **Where and when.** Her own X post, 21 Sep 2026 15:01 UTC,
  https://x.com/poteto/status/2102050467505430555 , publishing a 38-minute talk video. Verbatim, first
  line: **"here's how i shipped 2,500 PRs last month to production"**. The talk was made for Cursor
  Compile London and she released it herself after missing the event.
- **What it counts.** Pull requests, "shipped ... to production", one month (posted 21 Sep, so August
  2026 on the reading; she does not date it). **Not** stated: merged, agent-written vs hers, her own
  work vs her team's, or any denominator.
- ⚠️ **Her own figure is 2,000 on Cursor's schedule.** `cursor.com/compile/london` (primary, fetched
  26 Sep) lists the same talk as **"I Shipped 2,000 PRs Last Month"**, event 16 Sep. 2,000 on Cursor's
  page, 2,500 in her post five days later, one month of work. **If the number prints, the split prints
  with it.** A volume claim that moves 25 per cent in five days is a headline, not a measurement, which
  is nearer Monday's thesis than the figure is.
- ⚠️ **Quote provenance.** x.com returned 402 to the fetch tool and the xcancel mirror returned 451.
  The wording above came from `api.fxtwitter.com`, an X API mirror returning the post's own text field:
  one remove from x.com. **Check it against the live post before it prints.**
- ⚠️ **Standing rule 2 applies, as it does to Warp and Kiro.** She works on Grok Bot at SpaceXAI, ships
  pstack on the Cursor Marketplace, and the talk was commissioned by Cursor. Her throughput is her
  product demo. Name that in the sentence. **Stripe remains the clean control case.**
- ⛔ **The rest of her talk is not footed and the best of it is out of bounds anyway.** The 38-minute
  video was not watched. Secondaries describe a trust hierarchy that puts human code review last as the
  bottleneck, plus a "Control Glass" CLI, a "Feature Map", a "Gardener" role and a Michelin-kitchen
  framing. Two problems: none of it is at primary, and the review-bottleneck argument is the Aug coding
  sub-arc's, which the Mon 28 DO NOT list rules out. Same rule as Warp's 3.5 hours: cite a number, never
  re-run the argument.
- **Repetition flag for the day chat.** She is in the published Sat 12 piece and behind Sat 19. Monday
  would be her third appearance in a fortnight.
- **Her earlier figures stay barred as fact** (12 Sep intake): "roughly 2,000 PRs a month personally",
  "hundreds of PRs a day", "100-1000x". The 2,500 prints as something she said, dated and attributed,
  never as measured throughput.
- **@poteto (Lauren), X, 21 Sep 2026 15:01 UTC:** "here's how i shipped 2,500 PRs last month to production" (talk prepared for Cursor Compile London). Read at the post 26 Sep. Self-reported; what it counts is unstated; employer NOT established (his recollection: Grok AI) -- do not print an affiliation until confirmed.
- **RULING 26 Sep 22:31, his word:** @poteto (Lauren) works at SpaceXAI. Printable as his word.
