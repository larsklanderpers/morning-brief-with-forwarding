# 🧭 AI Work & the Shape of Work-to-Come
**Sunday, 26 July 2026** · *Community brief — constructive lens*

---

## 🎥 What Creators Are Saying (YouTube)

**"AWS Veteran: How The New AI Software Development Life Cycle Works"** — Beyond Coding (3 days ago, 18K views)
URL: https://www.youtube.com/watch?v=0VugiUxDHr4
Heitor Lessa (11 years, 8 roles at Amazon) walked through his actual agentic workflow: humans write the spec and plan, agents execute, adversarial reviewers challenge every merge. His headline number: $5K/month per engineer in AI tooling — and the question isn't whether to spend it but how to govern what the agents do with it. He retired from "Opus" after a refactor cost 200M tokens; now runs a three-tier model stack (SOTA / mid / cheap) matched to task complexity. 32-chapter breakdown, from discovery spec through retro interviews with yourself.
💡 **Constructive read:** The human role didn't disappear in Lessa's shop — it moved to the top of the stack. Spec, plan, adversarial review, retro. If your job involves deciding what gets built and whether it worked, you just got more leverage, not less.

**"You're Not Behind (Yet): How to Build Your First AI Agent"** — Dan Martell (10 days ago, 209K views)
URL: https://www.youtube.com/watch?v=R4hoUYxxw70
Martell's AGENT framework: Automate, Give context, Execute, Nudge, Test. Framed as turning the repetitive, rules-based slice of any professional role into a system you own — freeing time for higher-judgment work. Comes with a free "AI Company Operating System" template.
💡 **Constructive read:** 209K views in 10 days on a how-to video signals that the "I want to build this" audience has crossed the chasm. The maker instinct is mainstream now.

**"Hermes Agent Fundamentals In 29 Minutes"** — Tina Huang (5 days ago, 129K views)
URL: https://www.youtube.com/watch?v=Dsdr6lsQ3Sw (approximate — channel confirmed)
Covers hardware choices for local agents, memory management systems, multi-agent frameworks, and open-source AI — the practitioner curriculum for running agents without a cloud subscription. "New" badge, high engagement.
💡 **Constructive read:** A 29-minute crash course getting 129K views is the community voting with its time on "learn to build" over "argue about whether to be scared."

**"The New Jobs AI Will Create"** — The AI Daily Brief / NLW (2 months ago, 8.8K views)
URL: https://www.youtube.com/@NLW — weekend long-read episode
NLW's framing: the AI jobs debate has wasted years asking which roles disappear; this episode asked the more useful question about what roles emerge. Directly seeded this thread's architecture-of-work model.
💡 **Constructive read:** The fact that this is NLW's highest-engagement recent work on jobs (vs displacement pieces) suggests the community is hungry for the constructive frame and not finding enough of it.

---

## 🐦 The Conversation on X

**@Salesforce** — flagged this week on new organizational structures:
> "New organizational roles will emerge to meet this requirement: AI operations officers and agent managers with authority over deployments and responsibility."
Why it matters: A Fortune 500 vendor articulating role titles (not vague "new jobs will emerge") is a signal that hiring frameworks are forming around agent governance. The title "agent manager" is starting to mean something concrete — the person who owns what a swarm of agents is allowed to do.

**X/Twitter search note:** Live search was inaccessible this run (Chrome tab dropped during Reddit fetch). Emollick (@emollick) posts not captured directly — see Newsletters section for Mollick's latest.

---

## 🧑‍💻 Practitioner Ground Truth (Reddit)

Reddit JSON was blocked from the sandbox environment this run, and the Chrome fallback tab dropped mid-session. **No Reddit data captured today.** Recommend checking r/ExperiencedDevs and r/singularity manually for the "Hermes agents" and "what should I learn" threads that are likely running hot this weekend given the volume of agent-fundamentals content this week.

---

## 🎙️ Podcasts & Newsletters

**AI Daily Brief — July 24: "Why AI Hasn't Increased Unemployment, According to Anthropic"**
URL: https://aidailybrief.ai/e/2026-07-24
Key source: Peter McCrory, Anthropic's head of economics. Three points:
1. AI is a **skill-biased, labor-augmenting** technology — it raises productivity for workers who use it, not a one-for-one job eliminator.
2. **"Weak links"** — essential tasks that are hard to improve — act as natural speed governors on both economic growth and displacement. You can't automate a 40-task workflow if tasks 12 and 28 require human judgment.
3. Doesn't expect unemployment noticeably higher a year from now because of AI. Caveat: if AI automates *innovation itself*, standard economic models hit singularities — that's the scenario he doesn't dismiss, just doesn't expect imminently.

**AI Daily Brief — July 19: "The Self-Driving Company"**
URL: https://aidailybrief.ai/e/2026-07-19
What happens when agents get woven into the fabric of an entire organization — including incidents, accountability, and what breaks. Framing the org as a system of agents (not just a team that uses AI tools) is the conceptual step forward here.

**Ethan Mollick — "The Twilight of the Chatbots" (June 30)**
URL: https://www.oneusefulthing.org/p/the-twilight-of-the-chatbots
Subtitle: "How work changes along the exponential." Mollick's thesis: chatbots are the transitional form — the real transformation is when AI is woven into workflows as an orchestrated layer, not a chat window. 734 likes. Timing: the "twilight" framing is showing up in the community's language now, about a month after publication — the lag is the tell.

**Ethan Mollick — "An Opinionated Guide to Which AI to Use" (July 23, Summer 2026 Edition)**
URL: https://www.oneusefulthing.org/p/an-opinionated-guide-to-which-ai-b22
728 likes in 3 days. Not directly about jobs, but the practitioner audience is using it to decide which tools to bet their workflow on — tool selection is now a professional skill in itself. Scout archetype in action.

---

## 🆕 New Roles & Archetypes Watch

**AI Operations Officer / Agent Manager** (Salesforce, this week)
The title is crystallising. "Authority over deployments and responsibility" — that's the Risk Steward + Conductor combination from the architecture-of-work model. Not a new department: an existing manager who now owns a portfolio of agents rather than a portfolio of people.
→ *Archetype: Conductor + Risk Steward*

**Human Planner in the Agentic SDLC** (Heitor Lessa / Beyond Coding, 3 days ago)
The AWS veteran's workflow separates cleanly into human-owned stages (discovery, spec, plan, retro) and agent-owned stages (execute, test, merge). The Planner role is explicit — it precedes every agent invocation. "Humans plan first, agents come second" is becoming a design principle, not just a preference.
→ *Archetype: Builder + Orchestrator*

**"AI Decider"** (Dutch Startup AI TV, circulating this week)
A role jumping from 26% to 76% representation in job postings — the person inside a non-tech function who has authority to approve or block AI-generated decisions before they execute. Shows up in finance, legal, HR. The organizational answer to the "who's responsible when the agent is wrong?" question.
→ *Archetype: Risk Steward*

**AI Skills Embedded in Non-Tech Roles** (Indeed / Euronews, July 24)
In France and the UK, 54% of AI-labelled job titles are now *outside* tech occupations. AI-exposed roles are evolving 66% faster than non-exposed ones. AI-specific vacancies: from <3% of all job openings in January 2023 to **16% by July 2026**. This is the quantitative backbone of the "become the maker for your function" frame — it's already happening, across functions.
→ *Archetype: Scout + Editor, spreading across every function*

---

## ⚖️ The Debate (kept honest, kept brief)

The CEO consensus is fracturing, and that's actually information. Amodei (Anthropic) still says up to 50% of entry-level white-collar roles will be eliminated. Altman (OpenAI) said this week he's "delighted to be wrong" — less impact on entry-level workers than he'd predicted. AWS CEO Matt Garman: jobs will *change*, not disappear. Sierra's Clay Bavor: Gen Z workers most adept AI users are some of his strongest employees. Indeed Hiring Lab: entry-level postings down 6% year-over-year, but can't attribute that to AI alone. Anthropic's own economist: no material unemployment rise expected in the next year. The empirical picture: "no clear aggregate signal yet" for the workforce overall, with the sharpest pressure on workers aged 22–25 in highly AI-exposed occupations. The honest read is that the transition is real but slower and more uneven than either the alarmists or the optimists predicted.

---

## 📌 Today's Signal

The conversation this week moved a step further from "will AI take my job?" toward something more useful: **where does the human sit in the new system, and what do they own?** The answers are getting concrete. Lessa's SDLC puts humans at planning and adversarial review. Salesforce is naming the role that owns agent governance. Indeed's data shows that AI skills are already majority non-tech — meaning the integration isn't a future event, it's the current hiring market. Anthropic's own economist offers the most useful reframe: AI is labor-augmenting, and "weak links" — the tasks that resist automation — are what determine the pace. Find your function's weak links, own them, and build the system around them. That's the architecture-of-work model in practice.

---

## 📝 Outstanding Substack Drafts

| Filename | Title | Target / Status |
|---|---|---|
| `substack_draft_capstone-model-hard-part_2026-07-26-rv5.md` | The Model Was Never the Hard Part | Jul 26 (today) — HELD pending CPS 230 corrections |
| `substack_draft_excuse-expired_2026-07-25_v2-rv1.md` | The Excuse Just Expired | Jul 25 — past due, Saturday Diversions |
| `substack_draft_feeding-them_2026-07-28-rv1.md` | Every Correction You Make Is Feeding Them | Jul 28 — rv1 awaiting Lars's read |
| `substack_draft_execution-rule_2026-07-31-rv1.md` | A Policy Isn't a Control. An Execution Rule Is. | Jul 31 — rv1 clears bar (9.3), awaiting Lars's read |
| `substack_draft_bring-it-home_2026-07-24-rv2.md` | Bring the Model Home | Jul 24 — past due, CPS 230 corrected, awaiting Lars's read |
| `substack_draft_accept-refuse-delegate_2026-07-21-rv3.md` | Accept, Refuse, or Delegate | Jul 21 — past due, CPS 230 corrected, awaiting Lars's read |
| `substack_draft_aml-desk_2026-07-23-v1.md` | Your AML Desk Already Knows How to Govern a Machine | Jul 23 — past due |
| `substack_draft_29-minutes_2026-07-22-rv1.md` | You Have 29 Minutes. Who's Awake? | Jul 22 — past due |

---

*Flag an item for Substack: save URL + notes to Substack Drafts\. This thread feeds the Saturday "Diversions" slot (operational / how-to / uplifting) as well as weekday rotation.*
