# Substack Ideas & Backlog

Parking lot for piece ideas that aren't drafted yet — held concepts, raw candidates, and locked-but-unwritten pieces. When something here gets drafted, move it into a real draft file and add a row to `SUBSTACK_INDEX.md`.

**Status keys:** 🔒 Locked (committed, not yet drafted) · ⏸ Parked (good idea, waiting for the moment) · 💡 Raw (candidate, unsorted)

---

## 🔒 Locked — committed, awaiting draft

### "The Excuse Just Expired" (working title) — Herk course / SATURDAY DIVERSION #3
**Target:** Sat 25 Jul 2026 · **Thread:** The Shape of Work-to-Come · **Locked 14 Jul 2026**
**Source:** Nate Herk (YouTube: "Nate Herk | AI Automation"; runs the AI Automation Society on Skool), *Claude Code for Non-Coders (6 Hour Course)*, published **11 Jul 2026** — the same Saturday Diversion #1 ran. Free; 25+ chapters; arc: first prompt → files/APIs/permissions → skills & sub-agents → "second brain" → automations that run on their own in the cloud. ~52K views in 3 days (**verify count before publish** — YouTube bot-walled the automated check).
**Angle (locked):** demand signal first. Open on the 52K number in two declaratives ("Fifty-two thousand people took a six-hour course last week. Almost none of them can code."), read it as the adopted-vs-waited split resolving itself in public — nobody is waiting for their employer's training budget — then pivot operational: how to actually spend the six hours, mapping course modules to the eleven shapes (sub-agents = Conductor, second brain = your corner, cloud automations = last Saturday's company-of-one stack). One wry beat max on the fact that permissions and unattended cloud automations are Monday-material; the judgment layer stays yours.
**Callbacks:** "become the maker for your own corner" (7/11) · "the door is lighter -- go lean on it" (7/18) · pick up the 7/18 footer thread (readers replying with the smallest version of their idea: *you told me the idea; here's the six hours between you and v1*).
**Genre armor:** cite the wider free-manual wave — Carl Vellotti's "CC for Everyone" (free, taught inside Claude Code itself), Frontend Masters' free Claude Code course, the Maven "Claude Code for non-coders" cohort — so the piece is an on-ramp story, not an ad for one YouTuber.
**Gate before drafting:** Lars skims/vets the course first (chapter summaries prepared to speed this up).

**Recently promoted to draft:**
- **"The Actor Is No Longer Human"** (Sun 12 Jul capstone) — drafted 6 Jul → `substack_draft_actor-no-longer-human_2026-07-12.md`, tracked in SUBSTACK_INDEX.md. Frame: the week's five pieces are one story — the human vacated every role (gatekeeper → KYC, insider → Trusted Co-Worker, identity → Contractor, attacker → JADEPUFFER, substrate → sovereignty) and the governance stack still assumes a person is there.

---

## ⏸ Parked — hold until it resonates

*(Lars, 6 Jul: "I don't think people are entirely ready for this yet." Holding to see if next week's news makes them land harder.)*

### "The Patch You Never Heard About" — Supply Chain / Outsourced Trust
**Thread:** Supply Chain (extends the unpublished Cordyceps piece)
**Hook (from 5 Jul brief):** Microsoft silently patched the SharePoint RCE (CVE-2026-45659) with no CVE/advisory — and that same SharePoint vector is how DHS's HSIN intel-sharing platform got breached. Add SimpleHelp RMM (CVSS 10.0, one console into hundreds of clients) and ChocoPoC poisoning GitHub PoCs. Through-line: *the trust you outsourced — vendor changelogs, coordination platforms, managed-service consoles, public repos — is now the attack surface.*
**Why held:** audience not primed for the "map your outsourced trust" argument yet.
**What would make it resonate:** another high-profile silent-patch failure, a shared-infrastructure breach with attribution, or a supply-chain incident that hits a name readers know.

### Saturday long-form for the clubs / AUSTRAC audience
**Thread:** Machine Identity → Clubs (extends "The Contractor")
**Concept:** *Your AML program already knows how to govern non-human actors.* Clubs already run designated-service registers, audit trails, and meaningful-human-review — exactly the muscle agent governance needs. Land Wednesday's Machine Identity thread on the sector.
**Alternate:** a different clubs-sector angle if the machine-identity framing feels early.
**Why held:** same — hold until the Machine Identity thread has a published beat to build on and the sector angle is primed.
**What would make it resonate:** an AUSTRAC/APRA statement touching AI or agents, or a clubs-sector AI incident.

### Open-source AI Executive Order — tracking into "Control" week
**Thread:** Ad Hoc Regulatory Regime
**Status:** Active watch. Early-stage discussions on restricting Chinese open-weight models (possibly open source generally); officials deny an EO is drafted. Follows the June export directive that suspended Fable/Mythos.
**Sources:**
- [The Hill — Trump restrictions on private AI models turn attention to open source](https://thehill.com/policy/technology/5952253-trump-administration-ai-restrictions-opens/)
- [The Hill — Trump White House holds back new AI models, spurring confusion](https://thehill.com/policy/technology/5948098-trump-openai-ai-policy-confusion/)
- Politico: "Trump's AI flip-flopping could be a gift to China" — a16z stat: 80% of open-source developers worldwide build on Chinese models. Killer detail: restricting open weights doesn't remove the capability, it removes US visibility into it.
**Why held:** watching for EO draft or major public confirmation before committing to a piece. Perfect "Control" week material if something breaks.
**What would make it resonate:** an actual EO draft, a Congressional hearing, or another major model suspension.

### Office of AI (Australia) + 6.4x regulatory vacuum — pair piece
**Thread:** Ad Hoc Regulatory Regime × AU ecosystem
**Concept:** Two signals that belong together. (1) Australia is #1 of 121 countries in Claude usage at 6.4x population-predicted rate, up from 4.1x two months earlier — accelerating, not stabilising. 54.5% augmentation vs 51.4% global; tilted toward documents/education/knowledge work. NSW+VIC ≈ 70% of usage. (2) The world's heaviest per-capita AI user has no AI Act. Albanese created an Office of AI in PM&C (speech Wed 15 Jul, Sydney), pitched as a "single national framework" and "world first" — but obligations currently arrive piecemeal via APRA (CPS 230, live), OAIC (ADM, December), ACCC (2027). Usage is compounding at venture speed; the framework is being assembled ad hoc mid-flight. *6.4x is the number that makes the regulatory vacuum a story rather than an abstraction.*
**Sources:**
- [Anthropic — How Australia Uses Claude](https://www.anthropic.com/research/how-australia-uses-claude)
- [Mi3 — Australia ranks first among 121 countries, 6.4x expected rate](https://www.mi-3.com.au/07-07-2026/australia-ranks-first-our-121-countries-anthropic-usage-index-64x-expected-rate-less)
- [Forbes AU — Australia is the world's biggest Claude user](https://www.forbes.com.au/news/innovation/australia-is-the-worlds-biggest-claude-user-now-anthropic-wants-more/)
- [Capital Brief — Albanese creates Office of AI](https://www.capitalbrief.com/briefing/anthony-albanese-to-create-new-office-of-ai-under-his-departments-control-a19247a8-a8db-497e-b11f-49b052066d9e/)
- [The Conversation — Albanese takes oversight of AI under his wing](https://theconversation.com/view-from-the-hill-albanese-takes-oversight-of-governments-response-to-ai-under-his-own-wing-287494)
**The tension:** "single national framework" from the same government that chose sector-by-sector regulation over an AI Act. Is the Office of AI a framework or a front door bolted onto the ad hoc regime?
**Why held:** post-speech material being captured via daily watch task → `References\office-of-ai-watch.md`. Pair with "Control" week when the post-speech landscape settles.

---

## 💡 Raw — candidates not yet shaped

### Nadella's "Reverse Information Paradox" — ambient AI corporate moat erosion
**Thread:** AI Sovereignty / Trust Boundaries / NEW: Ambient AI Privacy drain (see below)
**Source:** Blog post published via X (@satyanadella), Sunday 12 Jul — coined "Reverse Information Paradox."
**Coverage:**
- [TechCrunch](https://techcrunch.com/2026/07/13/satya-nadella-has-issued-a-shocking-warning-to-companies-using-ai/)
- [The New Stack — best analysis](https://thenewstack.io/nadella-reverse-information-paradox/)
- [Business Today](https://www.businesstoday.in/technology/news/story/you-pay-for-ai-twice-satya-nadellas-reverse-information-paradox-raises-a-billion-dollar-question-542430-2026-07-12)
- [Business Standard](https://www.business-standard.com/technology/artificial-intelligence/satya-nadella-reverse-information-paradox-ai-risks-126071300520_1.html)
- [ppc.land — Nadella says using AI models forces firms to leak their own know-how](https://ppc.land/nadella-says-using-ai-models-forces-firms-to-leak-their-own-know-how/)
**Key:** Models learn from "exhaust" — prompts, tool use, especially corrections. Every correction distills institutional know-how to the provider. Asymmetry compounds: provider learns about customer continuously, customer learns nothing about what's done with it. His fix: a **"trust boundary" — a line across which nothing passes without consent**; inside it, data, traces, evals, adapted weights, and organisational memory accumulate to the company. Microsoft's CEO independently named Lars's week-of-13-Jul framing.
**Angle:** The piece that makes the ambient AI privacy drain series work. When the vendor's CEO warns you about this, that's the lede. Open on Nadella; close on the question he doesn't answer: what exactly is your enterprise Copilot agreement doing with your last six months of corrections?
**Strength:** Quotable validation from the most conflicted possible source. Strong candidate for "Control" week Tue slot.

### Ambient AI Privacy Drain — new thread candidate
**Thread:** NEW thread (sub-thread of AI Sovereignty, or standalone)
**Concept:** Not PII. Not a breach. Not an intentional upload. The slow, incidental, continuous disclosure of *how your business actually operates* through millions of micro-interactions — Claude in Slack, Copilot in Word and Excel, ChatGPT on the phone. 500 people's daily interactions paint a detailed picture of your operating model, approval chains, pricing logic, client patterns, and internal language. That's not a privacy problem — it's a competitive intelligence problem. Builds into a 4-piece series (see research session Jul 2026):
- Piece 1: The non-discrete disclosure problem (Nadella as anchor)
- Piece 2: The operational intelligence layer — what these tools actually see
- Piece 3: The legal gap — voluntary disclosure doctrine, *Trinidad v. OpenAI*, shadow AI
- Piece 4: What the trust boundary actually means (lands in AI Sovereignty)
**Why it's distinct from existing PII thread:** PII is about identifiable individuals. This is about institutional and competitive intelligence — the accumulated picture of how you think and compete, nobody's fault, nobody's single decision, never a discrete event.

### Claude Code sandboxed browser — vendor admission of prompt injection reality
**Thread:** AI as Attack Surface / Trust Boundaries
**Sources:**
- [9to5Mac — Anthropic highlights Claude Code's in-app browser](https://9to5mac.com/2026/07/10/anthropic-highlights-claude-codes-in-app-browser-on-the-desktop/)
- [Claude Code Docs — Week 28 release notes](https://code.claude.com/docs/en/whats-new/2026-w28)
**Angle:** Clean profile, no saved sessions, safety classifiers reviewing actions on external sites, user-controlled persistence. The vendor built the assumption "web content is untrusted input" into the architecture. When the vendor sandboxes its own agent, that's the admission the attack class is real and unfixed. Strongest possible callback to "The Agent Obeyed. It Just Wasn't Obeying You." (Jul 1). Good for an AI as Attack Surface beat or a Trust Boundaries short.

### The vanishing entry-level rung — Grower/Editor evidence (Quartz)
**Thread:** Shape of Work-to-Come (+ Coding/Practitioner, Load-Bearing Human)
**Source:** Quartz Leadership, "The vanishing entry-level rung" (Mon 20 Jul 2026). Full capture + archetype mapping + [VERIFY] stats in `thread_note_vanishing-entry-rung_2026-07-20.md`.
**Key:** Automating the entry rung saves a little now and starves the pipeline that grows managers (Grower) and the early-warning layer that catches broken things (Risk Steward). Redesign, not deletion: the junior role shifts from *do the task* to *check whether the machine did it right* (Editor). Payroll evidence — Brynjolfsson/ADP: 22–25 cohort in AI-exposed jobs down 16% vs older peers; software devs 22–25 down ~a fifth while 35+ grew; live dashboard decline sharpening to ~4%/yr **[all VERIFY vs primaries]**. Garman/AWS: "one of the dumbest things I've ever heard"; hiring ~11K grads after cutting ~14K. Edmondson/Chamorro-Premuzic on the manager pipeline.
**Use:** The Brynjolfsson/ADP anchor the McKinsey item below has been waiting to pair with — hard data under the Grower/Editor shapes. (1) Graft one cited line into Mon 27 Jul "Fifty Agents. Five Humans." (the 2–5 humans are survivors of this thinning). (2) Strong Sat 1 Aug Diversion candidate — the "keep the role, redesign it" resolution is operational + uplifting. Pairs with the Reddit "double down on technical skills" item (verification is the moat; juniors are where it's learned).

### McKinsey Agentic Organization + AI FinOps — Shape of Work evidence
**Thread:** Shape of Work-to-Come
**Sources:**
- [McKinsey — The agentic organization](https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era)
- [McKinsey — Six shifts to build the agentic organization](https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-organization-blog/six-shifts-to-build-the-agentic-organization-of-the-future)
- [Forbes — The 20 New Agentic AI Jobs Box, McKinsey, and LinkedIn All See Coming](https://www.forbes.com/sites/sandycarter/2026/06/02/the-20-new-agentic-ai-jobs-box-mckinsey-and-linkedin-all-see-coming/)
- AI FinOps: live postings at jobs.finops.org
**Key McKinsey specifics:** 2–5 humans supervising an "agent factory" of 50–100 specialized agents — that ratio IS the architecture-of-work thesis in one number. Orchestrator skill stack maps almost exactly to the archetype deck. AI FinOps as live job category: "every AI request, token, and model interaction must create more value than it costs."
**Use:** Institutional validation for Shape-of-Work-to-Come; cite in any piece on the orchestrator/conductor shapes. Strong Saturday Diversion candidate as its own operational guide.

### Encoded AI Governance (Ben Brook / Transcend)
**Thread:** Trust Boundaries / AI Sovereignty
**Sources:**
- [Help Net Security — A $2 trillion revenue shift hinges on AI data governance](https://www.helpnetsecurity.com/2026/06/16/ai-data-governance-revenue-shift/)
- [Transcend — AI governance recommendations](https://transcend.io/blog/ai-governance-solutions)
**Core:** governance must determine what data an AI system can use, for what purpose, under what conditions, on whose authority — **enforced automatically at runtime, inside the systems where data is processed.** Policies and model cards describe what *should* happen; executable controls in the data path determine what *does* happen and deny the operation before data leaves the store. Bridges to the Nadella trust-boundary argument: the boundary isn't a policy, it's a technical control at the point of data access.
**Use:** Operationalises the Trust Boundaries thread; good Fri slot in a week heavy on regulatory/sovereignty themes.

### **"The Auth Bypass of 2026" — OAuth / token theft**
ToddyCat's Umbrij reads corporate Gmail with a stolen token (no password, no MFA event) + FortiBleed (3 Jul brief). Cyber-identity beat; pairs thematically near the Machine Identity thread but distinct.

### AI agent supply chain
Fake agent "skill" reaching ~26,000 agents + AutoJack (one web page hijacks an agent to host RCE) (3 Jul brief). Bridges Supply Chain + AI-as-Attack-Surface.

### Cordyceps CI/CD supply chain
Draft exists (`2026-06-26_cordyceps-cicd-supply-chain.md`), never published — natural predecessor to "The Patch You Never Heard About."

### Mollick's *Co-Existence* framing shift — TRACK for Shape-of-Work-to-Come
New book *Co-Existence: The Next Phase of AI*, announced via One Useful Thing ("Co-Existence and the End of Co-Intelligence"); **launches 20 Oct 2026**. The shift: *Co-Intelligence* (2024) put the human at the center with AI as helper; *Co-Existence* is about working with AI that is "sometimes, but not always, better than you" — when to accept, refuse, or fully delegate. That's the load-bearing-human question at book scale. Announcement citable now; the Oct 20 launch is a natural piece peg (weekday framing-shift piece or Saturday review).

### AI as the gatekeeper of your audience
From the same Mollick announcement post: AI now stands "between your work and its audience" — writers/builders must optimize for AI recommenders, not just human readers. Could pair with the Evangelist/Scout shapes.

### Reddit — "Now is exactly the time to double down on technical skills"
**Thread:** Coding / Practitioner Ground Truth
**Source:** r/cscareerquestions, 801↑ / 325 comments — https://reddit.com/r/cscareerquestions/comments/1uv4hea/
Senior FAANG IC: deep technical knowledge is the moat because LLMs are confidently wrong 10–20% of the time and errors are getting harder to catch. Top counter: breadth wins. Both camps agree the job is now verifying and directing machine output. Good for a Coding/Practitioner beat or a Shape-of-Work piece on the false binary.

---

*Update this file whenever an idea is parked, promoted to draft, or killed. Mirrored to Google Drive: writings > substacks.*
