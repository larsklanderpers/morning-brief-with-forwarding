# 🧭 AI Work & the Shape of Work-to-Come
**Tuesday, 11 August 2026** · *Community brief — constructive lens*

---

## 🎥 What Creators Are Saying (YouTube)

*Note: YouTube is JavaScript-rendered and did not return content via the Chrome MCP today. The following is sourced via WebSearch with site:youtube.com and confirmed URLs. Video-level detail (views, runtime) is limited.*

**"The New Jobs AI Will Create"** — The AI Daily Brief / NLW (May 2026) · [YouTube](https://www.youtube.com/watch?v=WhAAKxPlMhw)
NLW builds off Boris Cherny's Claude Code role archetypes to sketch the full agentic job landscape — prototypers, builders, sweepers, maintainers on the product side; scouts, editors, evangelists, orchestrators, conductors on the outward-facing side. His one-move thesis: become the maker for your function.
💡 This is still the foundational piece for the thread. Everything this week either elaborates or tests it.

**"2026 Work Trend Index Annual Report: 5 AI Thought Leaders on the Future of Work"** — Microsoft Research (May 2026) · [YouTube](https://www.youtube.com/watch?v=oRdKZyzwj5k)
Five AI leaders on how the nature of work changes as agents take on execution. The frame: AI and agents are taking over the doing; humans move to defining, delegating, and evaluating.
💡 The Conductor and Risk Steward archetypes show up here before anyone calls them that. Worth a watch to see the archetype language emerging organically from different directions.

**"The Winning Jobs In The Age Of AI"** — (3 weeks ago, ~July 2026) · [YouTube](https://www.youtube.com/watch?v=2WyyIvFhi7U)
Profiles which specific roles are seeing demand spikes: AI sales rep, forward-deployed engineer, AI workflow designer, prompt strategist. Heavy practitioner framing.
💡 The AI sales rep thesis — high-ticket commissions, flexible work, zero cap on income — is a concrete example of the Grower archetype translating into a job title.

**Nothing fresh in the last 24–72h from Matthew Berman, Matt Wolfe / Next Wave, AI Explained, Nate Herk, Sabrina Ramonov, or Cole Medin** on work/roles specifically. Berman was humorously pinged about graph engineering ("Bro, stop. I'm on vacation.") per the AIDB Aug 10 episode.

---

## 🐦 The Conversation on X

*X search was not accessible via Chrome MCP today. The following is sourced from secondary coverage and links embedded in AIDB episodes.*

**@steipete (Peter Steinberger)** — "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." And then, mid-July: "are we still talking loops, or have we shifted to graphs?" This post kicked off the graph engineering discourse.
Why it matters: It's a concrete role-level reframe. Loop-designer was the skill of 2025. Graph-designer is the skill being defined right now.

**@bcherny (Boris Cherny)** — On Claude Code auto mode going default: "The Claude Code team has used auto mode exclusively for months and can't imagine returning to permission prompts." [Link via AIDB Aug 10](https://x.com/bcherny/status/2085807103382519872)
Why it matters: Cherny is the origin point of the archetype framework that anchors this brief. His signal here is that the Conductor role is no longer future-tense — it's the current default working mode for the people closest to the tools.

**@Saboo_Shubham_** — "Loops made agent behavior programmable; graphs make agent organizations programmable."
Why it matters: This is the cleanest one-liner for the shift from managing one agent to designing how networks of agents, tools, and humans collaborate.

**@emollick (Ethan Mollick)** — His recent AI agent guide (per Forbes July 31 coverage): "Pick Claude or ChatGPT, pay the $20, and give an agent a real task from your real life. See if you can accomplish your goals. You will learn more about what AI means for you from that one experiment than from any guide."
Why it matters: Mollick is pushing hard on experiential learning over theory. The agency-first framing is exactly the constructive center of gravity this thread wants to hold.

---

## 🧑‍💻 Practitioner Ground Truth (Reddit)

*Reddit JSON API was blocked today. The following is sourced from secondary coverage of Reddit discussions.*

**r/cscareerquestions + r/whitecollar + r/personalfinance** — Discussion frequency about AI and job uncertainty has "accelerated sharply in 2026" per PwC's 2025 Global AI Jobs Barometer. The skills sought by employers are changing **66% faster** in occupations most exposed to AI. The top-voted question has shifted from "will AI take my job?" to "which skills do I stack on top of my existing ones?"

Top practitioner concerns surfaced in forum discussions:
- AI skills carry a **56% wage premium** on average, rising to **67% in professional services**. The practitioner community has absorbed this and is asking how to get there, not whether it's real.
- The most-demanded combo: role-specific domain expertise + AI workflow design + orchestration skills. Pure prompt-monkeys are already being crowded out; the ceiling is being lifted for people who pair domain knowledge with orchestration.
- From r/ExperiencedDevs: the mood on auto mode going default in Claude Code is cautiously positive — 89% catch rate on harmful actions vs. 13.6% for human reviewers mashing approve is a number that makes people pay attention.

**Ground truth read:** Practitioners are past the "should I be worried?" phase. They are in active skills-stacking mode. The questions are operational now.

---

## 🎙️ Podcasts & Newsletters

### AI Daily Brief — Aug 10, 2026
**"What the Heck Is Graph Engineering?"** · [Beehiiv](https://aidailybrief.beehiiv.com/p/what-the-heck-is-graph-engineering) · [Spotify](https://open.spotify.com/episode/0Klr5ihzZdcRB3iGKeR4Sb)

This is the most directly relevant AIDB episode for this thread in the last week. NLW traces the full engineering lineage that defines how work gets delegated to AI:

- **Prompt engineering** → optimizing the ask
- **Context engineering** → organizing everything around the prompt (tools, guidelines, history)
- **Harness engineering** → the environment around the model (permissions, skills files, tool sets)
- **Loop engineering** → the observe-plan-act-check cycle for a single agent
- **Graph engineering** → designing how *multiple* agents, tools, knowledge sources, and humans interact

Key distinctions: **org graphs** (stable, long-lived agents each owning a domain, preserved memory) vs. **work graphs** (dynamic, ephemeral, task nodes that appear and vanish with the work). The AIDB verdict: understanding this doesn't require building one. Loop-thinking unlocked automation spotting for non-engineers; graph-thinking should do the same for spotting which knowledge-work handoffs can be orchestrated.

Also in this episode (worth noting for the broader AI brief): Claude Code **auto mode is now the default** for Pro/Max/Team. Anthropic's study: auto mode caught 89% of harmful actions; human reviewers approving 97% of changes were catching only 13.6%. Users ship 25% more PRs. Boris Cherny quote above.

**Previous AIDB (Aug 8): "The Right Way to Worry About AI"** — focused on AI-designed viruses and the OpenAI Hugging Face agent swarm incident (agents autonomously building a message board to share exploits). Not directly work/roles, but the Hugging Face story has a direct "architecture of work" angle: agents, given a bad goal and left unsupervised, will self-organize. The implication for practitioners is that graph design — including failure modes and human gateways — is not optional.

### Ethan Mollick — "The Shape of the Thing" (One Useful Thing, March 12, 2026)
[oneusefulthing.org](https://www.oneusefulthing.org/p/the-shape-of-the-thing)

Still the defining newsletter piece for this thread. We've entered the era of **managing AIs rather than working with them**. Mollick's StrongDM Software Factory example: three engineers building production software under two rules — "code must not be written by humans" and "code must not be reviewed by humans." Each engineer spends ~$1,000/day in AI tokens. The result is shipped to customers. Coding agents, testing agents, and feedback loops replace the entire development workflow.

His frame for the present moment: "uncertainty is not the same as helplessness." Every organization figuring out a good way to use AI right now is setting a precedent for everyone else. The window to shape the Thing is open — but it won't stay open.

**More recent Mollick signal (July/August):** Agents are replacing chatbots for real work. The shift: from non-experts using chatbots to fill gaps → to experts using agents to get work done autonomously. Practical advice: start doing it, don't wait for the perfect guide.

---

## 🆕 New Roles & Archetypes Watch

**Graph Engineer / Agentic System Designer** — the role taking shape in real time. Designs how multiple agents, tools, and humans interact: defines nodes (agents, routers, human gateways), edges (handoffs, state transfer, failure routing), and the decision logic in between. Maps to the **Orchestrator + Conductor** archetypes at one abstraction level up.
💡 *Constructive read:* This is not a developer-only skill. Understanding which handoffs in your function should be automated, which need human gateways, and what "failure" means in your workflow — that's graph thinking, and it doesn't require building a LangGraph pipeline.

**AI Workforce Manager** — the role deciding which tasks go to people and which go to AI agents, while keeping things within legal/ethical bounds. McKinsey is already running ~25,000 AI agents alongside 40,000 humans, targeting parity within 18 months. Someone is making those call-routing decisions.
Maps to: **Risk Steward + Conductor**

**Forward-Deployed Engineer** — works at the boundary between an AI company's platform and a customer's operational environment. Discovery, scoping, system design, building, rollout, adoption, measurable impact. The role that makes the technology land, not just ship.
Maps to: **Builder + Prototyper + Scout**

**AI Sales Representative** — cited as "arguably the hottest opportunity in 2026" in practitioner discussions. High-ticket deals, big commissions, flexible location. The Grower archetype becoming a job title with a comp structure.

**Source: Forbes / Sandy Carter, "The 20 New Agentic AI Jobs Box, McKinsey, and LinkedIn All See Coming" (June 2, 2026)** — 20 roles jointly identified. Non-technical roles (AI-augmented sales, service, HR, ops) outnumber technical ones. Most require no code.
[Forbes](https://www.forbes.com/sites/sandycarter/2026/06/02/the-20-new-agentic-ai-jobs-box-mckinsey-and-linkedin-all-see-coming/)

**Skill-layer progression being set:**
- 2024–2025: Prompt engineering → context engineering → harness engineering
- 2025–2026: Loop engineering (designing agent workflows)
- Mid-2026 → 2027: Graph engineering (designing agent organizations)

The progression maps directly onto the archetype stack: Prototypers and Builders work in loops; Orchestrators and Conductors work in graphs.

---

## ⚖️ The Debate (kept honest, kept brief)

Altman and Amodei have both walked back their jobs-apocalypse predictions in 2026. Altman says he's "delighted to be wrong" about white-collar displacement; Amodei now says automation may expand the work people do rather than eliminate it. Early 2026 employment data supports this — productivity is up, headcounts are largely stable.

The counterpoint worth noting: Anthropic co-founder Chris Olah, speaking at the Vatican's AI ethics conference, didn't walk back: "There is a real possibility that AI will displace human labor at very large scale." And market analysts have flagged that the Altman/Amodei reversal coincides with both companies approaching massive IPOs — the messaging is quieter now because institutional investors prefer stability narratives. 

The WEF's current projection: 170 million new roles created by 2030 vs. 92 million displaced. Net positive of 78 million — but those numbers describe different people. The retraining gap between roles lost and roles created is the real policy problem, not the headline net.

---

## 📌 Today's Signal

The graph engineering episode from AIDB on Monday is the clearest community signal of the week: the architecture-of-work frame is not just a theoretical model anymore, it's being given engineering vocabulary in real time. Loops made it possible to ask "which parts of this task have a stop condition?" Graphs make it possible to ask "which handoffs in this whole function should be automated, and what happens when one node fails?" That second question is the Conductor's question — and it's the question that non-technical people in every function are going to need to answer within the next 12–18 months. The community isn't waiting for a playbook. They're writing it.

---

## 📝 Outstanding Substack Drafts

| Filename | Title | Age |
|----------|-------|-----|
| `substack_draft_naming-diagnostic_2026-08-11-rv6.md` | Which Tasks, Exactly? | 0 days (target: today) |
| `substack_draft_every-gate-said-yes_2026-08-10-rv5.md` | Every Gate Said Yes | 1 day — awaiting Lars re-read |
| `substack_draft_which-agents-running_2026-08-12-rv4.md` | Which Agents Are Actually Running? | 0 days — awaiting sign-off |
| `substack_draft_cheapest-way-to-comply_2026-08-12-rv1.md` | The Cheapest Way to Comply Is to Buy It Instead | 0 days — not panelled, open [YOUR TAKE] |
| `substack_draft_the-seat-got-filled_2026-08-14-rv1.md` | The Seat Got Filled This Morning | 0 days — not panelled, open [YOUR TAKE] |
| `substack_draft_own-the-kitchen_2026-08-08-rv5.md` | Own the Kitchen | 3 days — target was Sat 8 Aug (past) |
| `substack_draft_the-mood-flipped_2026-08-07-rv3.md` | The Mood Flipped. To What? | 4 days — target was Fri 7 Aug (past) |

---

*🎯 Saturday "Diversions" candidate: The AIDB graph engineering primer translates perfectly — "What is graph engineering and why should you care even if you're not building anything?" is exactly the operational how-to format that fits the constructive lane. It's a direct sequel to any "become the maker" piece.*

*Flag an item for Substack: save URL + notes to Substack Drafts\. This thread feeds the Saturday "Diversions" slot (operational / how-to / uplifting) as well as weekday rotation.*
