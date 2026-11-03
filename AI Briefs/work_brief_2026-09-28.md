# 🧭 AI Work & the Shape of Work-to-Come
**Monday, 28 September 2026 (catch-up covering Mon 28 to Wed 30 Sep, written Thu 1 Oct)** · *Community brief - constructive lens*

---

## 🎥 What Creators Are Saying (YouTube)

**"The Real Risks of AI Agents"** - The AI Daily Brief / NLW (28 Sep, 8K views) · https://www.youtube.com/watch?v=fXRagdr-Q34
NLW works through recent OpenAI security incidents and the limits of agent permissions, and argues the bigger disruption is agents doing exactly what users ask, which can upend systems that quietly relied on human friction to work.
💡 Constructive read: A lot of our processes were held together by the fact that filling in the form was annoying. Take the friction away and someone has to design the guardrail on purpose, which is Risk Steward work any team running agents now owns.

**"I Tested OpenAI's Dots vs. Meta's Muse. What You Need to Know."** - Nate Herk (30 Sep, 148K views) · https://www.youtube.com/watch?v=BvvfZKKz4Yo
Herk puts OpenAI's new always-on Dots agent and Meta's free Muse through the same jobs a day after DevDay, framed for people building automation businesses.
💡 Constructive read: Two personal agents in one week means the question shifts from "should I have an agent" to "which one do I hand which job". Choosing the right worker for the task is the Conductor's first call, and it is now a consumer decision.

**"The BEST Jev Use Cases for AI Coding (Absolute Game Changers)"** - Cole Medin (30 Sep, 16K views) · https://www.youtube.com/watch?v=qwnJJMNGwgY
Medin answers viewers who found Jev's use cases impractical with four specific ways he uses the decision model to make coding workflows faster and spend fewer tokens.
💡 Constructive read: The novelty phase of Jev was "look, it outputs a yes or no". The practitioner phase is a builder slotting a cheap, fast judge into the loop where a slow, expensive one used to sit, which is how the Builder archetype actually gets leverage.

**Tracked channels:** Berman, Wolfe and YC this window are model-launch and robotics coverage (Sonnet 5.5, DevDay, Opus 5.5 game tests, Tensr's robot factory) with no work or roles framing. AI Explained has no upload since 24 Sep. Ramonov's run is short prompt tips. The three search pages were not re-scanned; the 26 Sep run found the upload-date sort no longer applies.

## 🐦 The Conversation on X

⚠️ Lane failed (1 Oct, about 09:10 local): Claude in Chrome loaded x.com but the browser window reported zero width, so the timeline and search results never rendered (profile header only, no posts). No X items this run; worth a manual look at @emollick and @nlw for 28 to 30 Sep.

## 🧑‍💻 Practitioner Ground Truth (Reddit)

⚠️ Lane partly failed (1 Oct, about 09:00 local): hot.json returned HTTP 403 for all four subs and Chrome blocks reddit.com. The weekly top RSS worked for r/singularity, r/artificial and r/ExperiencedDevs; r/cscareerquestions stayed rate-limited (HTTP 429). RSS carries no scores.

**r/ExperiencedDevs** - "Interviewed candidates for 'AI engineer' roles this week, my god is this really where our industry is going?" (26 Sep, score n/a) · https://www.reddit.com/r/ExperiencedDevs/comments/1wql3g2/interviewed_candidates_for_ai_engineer_roles_this/
A hiring lead whose team now writes nearly all code with Claude replaced the live-coding round with a new test: review an agent-generated PR flagged as high risk. The top replies argue the round should filter for competence first, since AI workflows are easier to teach a good developer than judgment is to teach an AI power user; one candidate reports being marked down for spending a 25-minute AI task on tests and checks instead of output.
💡 Constructive read: The interview is quietly catching up to the job. Reviewing the agent's PR is the Editor archetype as an assessment, and the candidate who lost points for building the checks shows hiring has not yet settled on whether it is buying speed or judgment.

**r/artificial** - "AI could force 11 million US workers into new careers by 2035" (29 Sep, score n/a) · https://www.reddit.com/r/artificial/comments/1wtbtoh/ai_could_force_11_million_us_workers_into_new/
The CNN story on McKinsey's new report drew a split thread: some called 11 million too low, while the most substantive reply argued that many jobs keep their titles but turn into something closer to systems engineering or agent orchestration, which is a career change by another name.
💡 Constructive read: The commenter found the quiet half of the story. A "marketer" in 2035 who spends the day directing agents has changed careers without changing business cards, and that reskilling is the part individuals can start on now.

**r/ExperiencedDevs** - "A lot of you all don't have an AI problem, you have a culture problem." (30 Sep, score n/a) · https://www.reddit.com/r/ExperiencedDevs/comments/1wu7e00/a_lot_of_you_all_dont_have_an_ai_problem_you_have/
Title only: the thread body did not load through RSS after two attempts. Paired the same day with "On the Jevons paradox, and why you are mistaken if you are convinced AI will increase demand of human software developers" (https://www.reddit.com/r/ExperiencedDevs/comments/1wtwhph/on_the_jevons_paradox_and_why_you_are_mistaken_if/), also unread.
💡 Constructive read: Flagged as signal, not substance: the practitioner forum spent midweek arguing about whether the pain is the tool or the team. Worth a read before anyone writes the "it's the culture" line, since the argument itself was not checked here.

## 🎙️ Podcasts & Newsletters

### The AI Daily Brief, 29 Sep: "How to Build Team Agents"
Source: The AI Daily Brief | [aidailybrief.ai](https://aidailybrief.ai/e/2026-09-29)
An Operator's Cut with Nufar Gaspar on moving from solo agents to shared team agents.
1. Four team-agent archetypes: expert, common work, bridge, and chief of staff. The expert agent targets the person who "can't take vacation" because only they know how pricing exceptions work.
2. Five design decisions decide whether a shared agent becomes infrastructure or sprawl: what it does, where it lives, what it knows, what it can touch, and how you run it. Plus three signs to wait: taste matters more than standards, no one owns the knowledge, or it adds more complexity than value.
3. The pattern is personal agents, then agent sprawl, then consolidated team agents with one owner; the episode cites Every taking about five months to go from an agent per employee to shared team agents.
💡 Constructive read: Every company has a single point of failure who answers the same questions all week. Turning that person's knowledge into a team agent, with that person as its named owner, is the "become the maker for your function" thesis aimed at the most frustrating bottleneck in the building.

**The AI Daily Brief, 30 Sep: "The Most Important New AI Tools from OpenAI DevDay"**
Source: The AI Daily Brief | [aidailybrief.ai](https://aidailybrief.ai/e/2026-09-30)
NLW counts more than 20 DevDay launches, including Dots (persistent agents on their own cloud computer), Space (natively multiplayer work), the Decisions API and GPT-6.1 Sol at about a third the cost of GPT-6 Sol, and reads them as confirming three trends: cheaper good-enough models, always-on agents, and work AI going multiplayer. The 28 Sep episode page returns 404; that day's video is under YouTube above.
💡 Constructive read: When the biggest lab's biggest event has no new direction, the direction is settled. The useful move for a reader is to stop waiting for the next launch and pick the one recurring team job to hand to a shared agent.

**Ethan Mollick / One Useful Thing** - nothing new in the 28 to 30 Sep window
Source: One Useful Thing | [The Overhang](https://www.oneusefulthing.org/p/the-overhang)
Latest in the window remains "The Overhang" (18 Sep). A new post, "The Dot and the Swarm", landed 1 Oct and belongs to today's brief.
💡 Constructive read: Nothing to add for the catch-up window.

**AI Chat Daily careers beat** - nothing fresh in the window; the latest items (CESifo, AT&T, a16z academy) were covered 26 and 27 Sep.

## 🆕 New Roles & Archetypes Watch

**The team-agent owner**
Source: The AI Daily Brief | [aidailybrief.ai](https://aidailybrief.ai/e/2026-09-29)
Gaspar's design rules give each shared agent one configuration and a named owner, and her "wait" signs include having no knowledge owner. That is a role description, even if no one is posting it as a job title yet; treat it as an emerging responsibility, not a hiring trend.
💡 Constructive read: Architecture-of-work map: Maintainer plus Editor, the person who keeps the team's ground truth current and decides what the agent is allowed to say. It is most naturally a promotion for the expert everyone already calls, not a new hire.

**The PR reviewer as the entry ticket**
Source: r/ExperiencedDevs | [thread](https://www.reddit.com/r/ExperiencedDevs/comments/1wql3g2/interviewed_candidates_for_ai_engineer_roles_this/)
One hiring lead's anecdote, not a market trend: the technical interview moved from writing code to reviewing a high-risk agent-written PR.
💡 Constructive read: If the test is review, the skill to practise is review. Anyone aiming at an AI engineer role can build that portfolio now by reading agent output critically and writing up what they would reject and why.

## ⚖️ The Debate (kept honest, kept brief)

**McKinsey: about 11 million US workers may need to change occupations by 2035**
Source: McKinsey Global Institute | [Workforce in motion](https://www.mckinsey.com/mgi/our-research/Workforce-in-motion-Skills-and-pathways-to-future-jobs-in-the-United-States)
MGI's report (published around 29 Sep, per CNN's same-day coverage) estimates roughly 11 million workers in declining occupations may need to switch, in a range of 6 to 16 million depending on adoption pace. That needs about 770,000 occupational switches a year, about 3.6 times the historical average; only about one in seven has a direct pathway; more than 75 percent sit in office and admin support, retail and sales, and transportation and logistics; lower-wage workers are 7.6 times more likely to need a switch. MGI's base case has automation reducing demand by 36 million jobs while growth adds 40 million, so the problem it describes is mobility, not scarcity. Figures are as summarised on MGI's own page and in coverage; the full report was not read this run.
💡 Constructive read: A bridge is only useful if people can find the on-ramp. The number to remember is not 11 million but one in seven: most people who need to move have no obvious next job, and McKinsey, which also sells workforce transformation consulting, is naming a pathways gap that employers and training providers can actually close.

## 📌 Today's Signal

The three days after the weekend's staffing story moved the conversation from the individual to the team. NLW's Gaspar episode makes the shared team agent concrete, with a named owner and the one colleague who can never take a holiday as the first use case, and OpenAI spent DevDay shipping multiplayer by default. Practitioners are adjusting at the edges: one hiring lead now tests whether you can review an agent's PR, not write the code. And McKinsey's 11 million puts a scale on the change while its one-in-seven pathway figure says where the work is: helping people find the next job, not just predicting which one disappears. In architecture-of-work terms, the Maintainer and Editor roles are getting a team-sized version. The practical move: find the question your team asks the same person every week, and make writing that answer down for an agent the first build.

---
*To flag an item for Substack: react 📌 on it in Slack, or save the URL and notes to Substack Drafts\. This thread feeds the Saturday "Diversions" slot as well as weekday rotation.*
