# 🧭 AI Work & the Shape of Work-to-Come
**Saturday, 24 October 2026** · *Community brief - constructive lens*

---

## 🎥 What Creators Are Saying (YouTube)

Tracked channels: AIDB's 23 Oct episode was a cyber story (see Podcasts). Berman's "Who is local AI really for?" (23 Oct) is a tooling video, not a work one. AI Explained's latest uploads are on lab security. Ramonov and Herk had nothing new on work. Matt Wolfe's channel page could not be read (Chrome blocked the extraction). Detail below comes from video descriptions, not transcripts. The standing search pages surfaced only items already covered (DW Shift, IBM) or older evergreen videos.

**"Run Your AI Software Factory Like a Real Engineering Org (Here's How)" - Cole Medin (23 Oct, about 10K views)**
Source: YouTube | [Link](https://www.youtube.com/watch?v=tNKmMhiOw9w)
Medin says his agent "software factory" works on solo projects but breaks at team scale, because every agent needs to know who owns the code, what has to pass before it ships and when a person signs off. He wires it into Port, which feeds agents ownership and standards before they plan, grades the codebase Bronze to Gold, and turns a failing check into an approved issue the factory then fixes. Port sponsored the video, so the platform choice is a paid placement.
💡 Constructive read: A kitchen with ten robot cooks still needs a pass where the head chef calls who plates what and when it leaves. The skill on show is not prompting, it is writing down ownership and the definition of done so the agents can read it, which is the Maintainer and Risk Steward work any senior engineer already does, now made machine-legible.

**"This Is How You Should Actually Make Launch Videos" - Y Combinator, Startup School (23 Oct, about 21K views)**
Source: YouTube | [Link](https://www.youtube.com/watch?v=v12aSIZIXUs)
Farza Majeed, founder of Hey Clicky and previously Buildspace, argues a launch video does not need a five-figure production budget and lays out his playbook for making short launch videos a routine part of shipping rather than a one-off event.
💡 Constructive read: The founder who used to hire an agency now runs the camera, the edit and the post, which is "become the maker for your function" applied to marketing. The Evangelist archetype stops being a department and becomes a habit you practise every time you ship.

**"Top 3 AI Predictions For The Future" - Varun Mayya (22 Oct, about 138K views)**
Source: YouTube | [Link](https://www.youtube.com/watch?v=n1gXOdLLTz4)
Mayya, who runs a company working with Indian enterprises, revisits his 2024 predictions, scores what he got right and wrong, and lays out where he sees jobs and skills heading over the next few years based on what he says he is seeing in client work. The video is sponsored by Gamma.
💡 Constructive read: A forecaster who grades his own homework in public is worth more than one who only ever predicts. The useful habit for any reader is the same one: write down what you expect your role to look like in a year, then check it, because the people who adapt fastest are the ones keeping score.

---

## 🐦 The Conversation on X

Claude in Chrome was connected. The three standing searches returned low-engagement or off-topic posts (the "become the maker" query mostly matched Marvel comics); one search returned a blocked extraction. The substantive work signal is Mollick's.

**@emollick (Ethan Mollick) - "labs will be tempted to enter finance and biotech directly" (23 Oct)**
Source: X | [Link](https://x.com/emollick/status/2113681838611087572)
Mollick argues that as the gap grows between the models labs keep internally and the ones they release, OpenAI and Anthropic will be increasingly tempted to use that edge themselves by entering new markets, especially finance and biotech. In a follow-up he says this would not require training on customer data, which the labs say they do not do, only the recognition that competing directly pays more than selling the capability. About 41K views and 177 replies at time of check. It is his prediction, not a reported plan.
💡 Constructive read: When the toolmaker can also build the house, the contractors who survive are the ones who own the client relationship and the local knowledge the toolmaker does not. For anyone in finance or life sciences, the move is to deepen the domain judgement and the customer trust, because the raw capability is the part that is getting commoditised.

---

## 🧑‍💻 Practitioner Ground Truth (Reddit)

⚠️ Lane failed, about 12:15 UTC: the Reddit JSON endpoints returned HTTP 403 for all four subreddits, and Claude in Chrome refused reddit.com ("not allowed due to safety restrictions"). This is the third day running. No Reddit signal in this brief.

---

## 🎙️ Podcasts & Newsletters

**AI Daily Brief - "The AI vs AI Battle for the Internet" (23 Oct, about 5.8K views)**
Source: The AI Daily Brief | [Link](https://www.youtube.com/watch?v=8R8FUxRn7fY)
The aidailybrief.ai page for 24 Oct returns 404, so this comes from the YouTube description. Three points: a critical PHP vulnerability as a sign that cyber is becoming AI against AI; the Railway and OpenCode breaches; and the case that coordinated agent swarms may decide who wins on defence. Headlines include Anthropic's Claude Duet launch and Walmart opening its store to third-party shopping agents. Mostly a cyber episode; the work angle is the defender's job shifting to running agent teams.
💡 Constructive read: Defence has always been a staffing problem, too few analysts for too many alerts. If the attacker brings a swarm, the defender's job becomes conducting one, which is a new and learnable skill rather than a lost cause.

**One Useful Thing - nothing fresh in the last 24 to 72h**
Source: One Useful Thing | [Link](https://www.oneusefulthing.org/p/30-months-on-the-exponential-in-charts)
Mollick's latest post is still the 20 Oct Co-Existence launch piece, covered on 21 Oct. His X feed carries this week's work signal instead (see above).
💡 Constructive read: Launch week is when an author is busiest talking and quietest writing; the short posts are where the new thinking shows up first.

---

## 🆕 New Roles & Archetypes Watch

**The public on-ramp: New York's AI Jobs Institute**
Source: Office of the Governor of New York | [Link](https://www.governor.ny.gov/news/governor-hochul-announces-launch-ai-jobs-institute-prepare-new-yorkers-jobs-future)
Governor Hochul announced on 22 Oct an AI Jobs Institute in Long Island City, Queens, run by the workforce nonprofit Pursuit, with $10 million in public investment (including $3.06 million from Empire State Development) and a goal of training up to 40,000 New Yorkers by 2032. Backers listed include Google.org, OpenAI, Anthropic and Wells Fargo. Construction starts this winter, with full occupancy expected mid-2027. The 40,000 figure is a target, not an outcome, and two of the named backers sell the AI being trained on.
💡 Constructive read: Every big shift in work eventually gets its trade schools, the way the electrification era got its vocational colleges. A state building the on-ramp before the job data forces it to is the right order of operations; the test is whether graduates land in roles, which we will not know until 2028 at the earliest.

**The agent-team engineering manager: ownership and gates as the new spec**
Source: YouTube, Cole Medin | [Link](https://www.youtube.com/watch?v=tNKmMhiOw9w)
Medin's team-scale factory (see YouTube) makes explicit a role that has been forming for weeks in this brief: someone who decides which agent owns which code, what gates a change must pass and when a human signs off. Yesterday's harness engineer was one person tuning one agent; this is the same job across a team of them. Practitioner demo, sponsored, one data point.
💡 Constructive read: This is the Orchestrator archetype growing an org chart. The engineers who already write good CODEOWNERS files and clear definitions of done are halfway to the job; the rest of the skill is learning to write those rules for a reader that never gets tired and never asks a clarifying question.

---

## ⚖️ The Debate (kept honest, kept brief)

**American Express to cut about 3,500 jobs while profit rises 28%**
Source: AI Chat Daily | [Link](https://www.aichatdaily.com/ai-careers/american-express-cut-about-3-500-jobs-prepares)
Per AI Chat Daily's report of the 23 Oct earnings call, American Express will cut about 3,500 jobs, roughly 4.5% of staff, as third-quarter net income rose 28% to $3.71 billion. CFO Christophe Le Caillec framed it as reducing management layers and widening spans of control "so that we can automate and take advantage of AI." The company has not said which functions are affected. The earnings transcript itself was not read. It follows Barclays' 5,000 cuts, covered on 22 Oct.

**Pantheon: AI is costing more than 10,000 US jobs a month**
Source: Fortune | [Link](https://fortune.com/2026/10/23/ai-is-killing-10000-plus-jobs-per-month-and-9-of-jobs-are-at-risk/)
Fortune reports (23 Oct) that Pantheon Macroeconomics' Samuel Tombs and Oliver Allen estimate AI-exposed sectors are losing jobs at more than 10,000 a month, a figure in the same range as Goldman's estimate that hiring in the most exposed industries is running about 10,000 below trend (covered yesterday). Fortune also notes construction jobs rising on data-centre building. These are analyst estimates from sector tracking, not attributed layoffs, and the Pantheon note was not read.
💡 Constructive read: Two banks in one week cutting middle layers while profits rise tells you where the pressure lands first: the manager whose job was passing information up and down. The response is to own an outcome rather than a relay point, because a role defined by what it decides is much harder to flatten than one defined by what it forwards.

---

## 📌 Today's Signal

This week's conversation is converging on one question: who owns the work once agents do it. Medin's factory needs written ownership and gates before it can scale past one person; Mollick warns the labs may stop renting capability and start owning markets; and AmEx is removing the layers whose job was coordination. Read through the architecture-of-work lens, coordination by relay is shrinking while coordination by design, the Orchestrator who sets the rules and the Risk Steward who signs off, is growing. Pantheon's monthly figure keeps the debate honest, and New York's institute is a reminder that the on-ramp is being built. The practical read for a Saturday: pick one process you touch and write down who owns it and what "done" means, because that document is the job description for the work that is coming.

---
*To flag an item for Substack: react 📌 on it in Slack, or save the URL and notes to Substack Drafts\. This thread feeds the Saturday "Diversions" slot as well as weekday rotation.*
