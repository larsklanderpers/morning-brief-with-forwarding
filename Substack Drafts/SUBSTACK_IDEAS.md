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

## 🔒 Locked — committed, awaiting draft

### "The Market Is Generating Its Own Facts" — and now its own standards body
**Thread:** Ad Hoc Regulatory Regime × AI Attack Surface · **Flagged by Lars 17 Aug 2026:** *"bang on, not sure when we get there, but definitely worth revisiting that with more attention."*
**Status:** LOCKED as a concept, deliberately NOT spent as a clause anywhere. Lars stopped the Wed 19 piece from burning it.

**The core.** In the agent-skill security space, every source has a product in the blast radius -- Koi, Antiy, Snyk, Island, Mitiga, CybeDefend, AIR. Unit 42 is the closest to disinterested and is still a vendor arm. And the load-bearing fact: **Niv Hoffman is both an AIR researcher on the "26,000 agents" demonstration AND an OWASP Agentic Skills co-lead.** So the taxonomy and the vendor research behind it are not independent of each other. The threat gets named by the people selling the fix, and then the naming becomes the standard everyone cites.

**Why it is a piece rather than an observation.** It is the same pattern already documented twice in this corpus, from two unrelated domains:
- `Vault\Writing\Signals\CLOUD Act Australia - the exposure predates the agreement.md` -- every appearance of the "US can reach Australian-stored data since Jan 2026" claim traced to companies selling sovereignty scoping, with a wrong date attached. Note's own line: **"the sovereignty market is generating its own legal facts."**
- `Vault\Writing\Signals\APRA CPS 230 voice AI vendors.md` -- same provenance problem, logged separately.
- Now a third instance where it has reached the *standards layer*, which is the escalation that makes it writable.

**The argument, in one line:** when the only people who understand a risk early are the people selling the remedy, the vocabulary of the field gets written by vendors, and a standards body staffed from that same pool launders the vocabulary into consensus. That is not fraud and nobody has to be acting badly for it to happen -- which is exactly why it works.

**What it needs before drafting:**
- Map the OWASP Agentic Skills Top 10 contributor list against employer, and establish how many are vendors in the space. Do NOT assert a proportion without doing this properly.
- Establish whether OWASP's own governance discloses commercial affiliation (it usually does) -- if it does, the story is structural rather than concealed, and the honest version is more interesting.
- Find the counter-example: a case where vendor-origin research was later independently confirmed or corrected. Without one the piece is one-sided.
- Check whether this has been written already, in security or in another field. The generalizable version (asbestos, tobacco, seatbelts, credit ratings) has a long literature; the AI-specific version may not.
- ⚠️ Be careful of the cheap version. "Vendors hype threats" is a column anybody can write. The interesting version is that the *definitions* are vendor-authored, which shapes what gets measured, funded and regulated for a decade.

**Sources to start from:** `References\research_poisoned-skills_2026-08-17.md` (the provenance findings are already collected there) · `Vault\Writing\Signals\Dynamic context runs before the defenses do.md` (§ Unspent) · the two CLOUD Act / CPS 230 signal notes.

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

### RESCUED from the superseded 17–23 Aug exploratory plan (parked 2026-08-08)
The 10–16 shaping (harness / repo-as-policy / prohibition / whose-job / diversion / capstone) is
being shifted onto 17–23, which supersedes `References\week-plan_2026-08-17.md` (status: EXPLORATORY
v0). Lars, 8 Aug: *"definitely do that, they are very sound ideas, I don't want to lose them."*
Three things from that plan are worth keeping and are parked here rather than lost:

- **"Nobody Can Triage 46,872 Bugs"** — AI-accelerated discovery broke the prioritisation heuristic.
  Chrome 149–151: 1,072 bugs then 370 more, **349 found by Google's own AI tooling**, more than the
  prior 23 updates combined; NVD at 46,872 CVEs in 2026. The sharpest beat: the vendor's own machine
  outpacing the vendor's own humans. Answer is blast radius, not faster triage. Callback to *A Policy
  Isn't a Control* (31 Jul) — sandboxing and least privilege are execution rules; severity ratings are
  the sign. **Skeptic-proof early:** more bugs found is good; the piece is "the heuristic broke," not
  "Chrome is broken." ⚠️ [VERIFY] the 46,872 figure and the per-release counts against NVD and Google
  release notes before drafting. Thread: AI Attack Surface → Trust Boundaries.
- **Eliza Filby's trust-erosion caution beat** — the counterweight to any week that mostly argues for
  adoption: AI surveillance erodes workplace trust, shadow AI runs because official channels feel
  monitored, and the generational split is millennials-see-productivity vs Gen-Z-fears-concentration.
  Her line: the real threat is that "AI is really replacing human conversations"; her prescription is
  reclaiming the time for mentorship. Credit her by name. ⚠️ [VERIFY] the ~80% shadow-AI figure and pin
  her source before use. (Fuller entry already above under *External read to mine*.)
- **Wage-premium figure discipline** — a brief carried **28–56%** against the standing Aug 6 instruction
  to use **PwC 2026's 62%** as primary. Pin ONE figure and ONE source across any week that touches it,
  or the run contradicts itself in public.


### External read to mine — Eliza Filby, "Why Elon Musk is wrong about AI and the future of work" (trust erosion + the generational lens)
**Source:** Dr Eliza Filby, *It's All Relative with Dr Eliza Filby* (Substack), 31 Jul 2026 — https://drelizafilby.substack.com/p/why-elon-musk-is-wrong-about-ai-and (Lars: "outstanding, very interesting take, lends itself well to caution"; flagged 1 Aug 2026)
**What it is:** a generational historian's rebuttal to the Musk / tech-titan "AI = abundance" utopia. Her argument: the abundance framing misses what's actually happening on the ground -- AI is eroding workplace TRUST and human connection. Three-part frame: (1) **AI surveillance** -- new monitoring of emails/meetings/tone erodes trust and morale; (2) **Shadow AI** -- ~80% of workers use unofficial AI tools because official channels feel monitored and impersonal [VERIFY the 80% + her source]; (3) **declining acceptance** -- Gen Z skeptical despite (or because of) fluency; millennials see productivity, Gen Z fears wealth concentration + job insecurity. Distinctive line: the real threat isn't job displacement, it's that "AI is really replacing human conversations." Prescription: reclaim the freed-up time for **mentorship**, not more work.
**Why it's on our threads (candidate):**
- **Direct cousin of Tuesday "Tooling People Up."** Her "reclaim time for mentorship / AI is replacing conversations" is Tuesday's agency/judgment/human-in-the-loop argument from the trust-and-connection side. Natural Tuesday-thread callback or follow-up.
- **Same FOIL move as the week's Altman beat.** Tech-titan optimism (Musk abundance / Altman liberty) vs. the ground truth. Filby-on-Musk pairs cleanly with our Altman-on-liberty: they name the upside and miss what it's actually doing to people.
- **The caution beat (Lars's read).** The surveillance / trust-erosion downside of AI deployment -- a needed counterweight in a week that mostly argues FOR adoption. Good "one beat of caution" material, or a standalone "the trust cost of AI at work."
- **Feeds Shape-of-Work-to-Come + the entry-ladder thread.** Her generational split (millennials vs Gen Z, wealth-concentration fear) complements the "eating our young / rebuild the rung" material and this week's concentration theme.
- **Trust Boundaries / ambient-privacy overlap.** Surveillance-erodes-trust + Shadow AI rhyme with "Every Correction You Make Is Feeding Them" and the ambient-drain series.
**Possible move:** a mid-week Co-Existence/Judgment or Trust-Boundaries piece on the *trust cost* of AI at work (surveillance + shadow AI + the mentorship reclaim), crediting Filby by name; or a single caution beat folded into a Shape-of-Work piece. If used: verify the "80% shadow AI" figure and pin her sources; she's a generational historian (Inheritocracy), so lean on the generational lens as the distinctive angle.

### External read to mine — "Should You Actually Use AI for This?" (decision tree + tacit knowledge)
**Source:** *The Second Opinion on AI* by "The Undercover Consultant," 25 Jul 2026 — https://thesecondopiniononai.substack.com/p/should-you-actually-use-ai-for-this (Lars liked the piece + its embedded decision-tree chart/graph work; flagged 1 Aug 2026)
**What it is:** an 11-question decision tree that routes a "should we use AI here?" request to 12 outcomes — and **5 of the 12 involve no AI at all** (not-a-project-yet / fix-the-foundation-first / clear-security-first / get-an-owner-first / just-write-a-rule). The "critical split" is whether there is one objectively correct answer. Objective path -> write a rule / classic ML / build the agent / build agent WITH GUARDRAILS. Subjective path -> copilot it / keep the human in the loop. Invokes Polanyi's "we know more than we can tell" (tacit knowledge resists automation).
**Why it's on our threads (research candidate):**
- Clean decision-tree/quadrant artifact — a model for a Diversion / operational how-to ("when NOT to use AI"), and a good dataviz reference to hold onto.
- "Build agent WITH GUARDRAILS" = the Harness paradigm ([[research_five-agent-engineering-paradigms]]); "keep the human in the loop" = Tuesday "Tooling People Up." This piece is the *decision layer* sitting above both.
- Anti-hype hook that fits the adoption-over-hype taste: most "AI projects" are unglamorous data/process work in disguise (5/12 endings need no AI).
- **Polanyi / tacit knowledge** is the deep thought-work worth a research dig — it underwrites the "judgment and agency can't be fully automated" argument running through Shape-of-Work + Co-Existence/Judgment.
**Possible move:** a Saturday Diversion "Should you actually use AI for this?" with our own version of the decision tree (credit the original), or a shorter callback beat inside a Co-Existence/Judgment weekday. Put research onto the Polanyi angle, and build our own graphic if we run it.

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
⚠️ CORRECTED 17 Aug 2026 after verification (`References/research_poisoned-skills_2026-08-17.md`). The "~26,000 agents" item is **NOT an attack**: AIR ran that campaign itself with a benign payload -- its own title is "The Story of Skills: How We Hijacked 26,000 Agents With One Instagram Ad" -- and AIR sells a managed skills marketplace. The figure is unconfirmed by anyone else (The Hacker News, 23 Jun 2026, says so explicitly). DATE TRAP: filed here as "3 Jul brief"; the event is **22-25 Jun 2026**. **AutoJack is dead** -- not a skills story (browsing-agent-to-localhost-MCP chain in AutoGen Studio), and Microsoft says it does not work on current builds. THE REAL STORY IN THIS SPACE: **ClawHavoc, 27 Jan - 4 Feb 2026** on ClawHub, with confirmed victims -- Koi Security audited all 2,632 listings and found 341 malicious, 335 from one campaign; Antiy CERT documented ClickFix-style social engineering and code execution on users' machines. Unit 42 disclosed five more live skills 23 Jun. Named class since Feb, OWASP AST01 Malicious Skills. Used in Wed 19 Aug. STILL UNSPENT AND WORTH A PIECE: every source here has a product in the blast radius, and one OWASP Agentic Skills co-lead is also an AIR researcher on the 26,000 demo -- taxonomy and vendor research are not independent.

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


### **"Open Is Not Local" — the gap between free weights and a model you can actually run**
**Thread:** AI Sovereignty (Model Sovereignty) · Diversions candidate
**Added:** 26 Jul 2026 (from the Sunday story-candidate brief + verification pass)
**Core:** Kimi K3's weights are free on 27 Jul. Serving them needs ~1.4 TB of fast GPU memory, roughly 18 x 80GB accelerators minimum, Nvidia Blackwell or AMD MI400 only, with Moonshot recommending a 64+ accelerator supernode. Local inference caps at ~131K context on day one while the 1M window stays a cloud feature. So the realistic operators are inference providers, the clouds, and a few very large enterprises — not a registered club. "Open" and "local" have quietly come apart.
**Ruling 26 Jul (Lars):** quantisation is this piece's RESOLUTION, not its problem — "they can get there with quants of other models for the vast majority of what they need, and I have no doubt a quant of kimi k3 is not far away." The honest version is *the flagship is not local, but you do not need the flagship* — not *open weights are a mirage*. Write it that way or not at all.
**Why it's a piece:** same shape as every governance gap he writes — the right exists on paper, the capacity to exercise it is distributed unevenly. And it has a constructive answer, which makes it Diversion-shaped rather than another threat: the model you will actually run is the 30-70B tier that fits a node you can buy, and that tier moved *because* K3 moved. Pairs with OpenWorker + Cisco Antares below.
**Detail + sources:** `References\research_kimi-k3-weights_2026-07-26.md`

### **Andrew Ng's OpenWorker — "data stays on your machine" as the headline feature**
**Thread:** AI Sovereignty · Shape of Work-to-Come · Diversions
**Source:** [MarkTechPost, 23 Jul 2026](https://www.marktechpost.com/2026/07/23/andrew-ng-just-released-openworker-an-open-source-local-first-desktop-ai-coworker-that-returns-finished-deliverables-instead-of-chat/)
**Core:** MIT-licensed local-first desktop agent (Ng + Rohit Prasad). Returns finished deliverables rather than chat, 35 connectors, Ollama support, data stays on the machine.
**Why it matters:** not the product — the *product language*. First mass-market tool to put data residency in the headline instead of the footnote. Evidence the local-first argument crossed from developer niche into consumer positioning, and Ng's reach will mainstream it fast. Also a live Mollick "twilight of the chatbots" datapoint: deliverables, not a chat window.

### **Cisco Antares — self-hostable security SLMs**
**Thread:** Trust Boundaries · AI Sovereignty
**Source:** Cisco AI Blog (via 26 Jul AI brief)
**Core:** Family of open-weight small models purpose-built to localise where in a codebase a vulnerability actually lives. Deployable on-premises.
**Why it matters:** a new category — a major vendor shipping self-hostable *security* models. For financial services and government clients who cannot route codebase analysis through a cloud API, this is the architecture the sovereignty thread has been arguing toward, arriving from a name procurement already trusts. Pairs with the Fri 31 Jul execution-rule argument and is a concrete "small model you can actually host" against the K3 headline.

### **IBM / Migrato split inference — PII on-prem, the rest to cloud**
**Thread:** AI Sovereignty · Clubs / AML
**Source:** IBM (via 26 Jul AI brief)
**Core:** Bank account numbers and other PII stay on-premises for local inference; only selected non-sensitive work goes to cloud, with GDPR/PII/PHI detection in the path.
**Why it matters:** this is the hybrid architecture "Bring the Model Home" argues for, shipped as a named product by a vendor a board recognises. Split inference stops being a compromise and becomes the demonstrable-to-a-regulator template. Strongest single citation available for the hybrid recommendation.

### **Anthropic has no EU data residency option** — ⚠️ `[VERIFY]` BEFORE USE
**Thread:** AI Sovereignty · Ad Hoc Regulatory Regime
**Source:** TechInsider, citing a "widely-cited GDPR review" (via 26 Jul AI brief) — soft, single-origin, secondhand
**Core (claimed):** Claude has no EU data residency, so any EU enterprise on the API owns the cross-border transfer lawful basis itself.
**Why it's tempting:** it would land on **2 Aug**, the day the EU AI Act becomes fully applicable and the day the capstone publishes.
**Why to hold:** the sourcing is a review-of-a-review, and vendor residency offerings change fast. Verify against Anthropic's own trust/privacy documentation before it goes anywhere near the capstone. Do not print it on this sourcing.

### **"Build your own research server for $5 a month" — the hedge framing**
**Thread:** AI Sovereignty · Diversions
**Source:** Smart Prompts for AI (via 26 Jul AI brief)
**Core:** On-device AI framed as a hedge against price hikes and platform lock-in, with a practical local-inference build.
**Why it matters:** the framing, not the build. For regulated buyers the risk was never only privacy — it is vendor dependency. An API price spike or a sanctions-driven interruption can strand a workflow overnight, and that is a CFO argument, not a compliance one. Sharpen and own it; it is the missing economic leg of the sovereignty thread.

---

*Update this file whenever an idea is parked, promoted to draft, or killed. Mirrored to Google Drive: writings > substacks.*

---

## 💡 Added 10 Aug 2026 — from the Monday story candidates (post-verification)

Vault notes in `Vault\Writing\Signals\`; verification in `References\research_story-candidates_2026-08-10.md`.
Fri 14 / Sat 15 / Sun 16 intake is recorded in `References\week-plan_2026-08-10.md`. What follows is what does
**not** belong to this week and should be held for 17–23 or later.

### 🔒 "The Rule Nobody Reads" / auto mode — **CLAIMED FOR FRI 14 AUG.** Not parked. See the week plan.

### ⏸ "Capability, Restated as Certainty" — the modal verb that goes missing
**Thread:** Ad Hoc Regulatory Regime, or **Diversions** (probably Diversions — more useful, less lecture)
**Note:** `Vault\Writing\Signals\Capability restated as certainty.md`
**Core:** six claims from one morning's briefs, taken to primaries. Five failed, four the same way — a source
says something *can* happen and the summary hands you something that *is* happening. Plus two cousins: a
prediction restated as a ranking (48% "believe agentic AI *will* be the top vector by end-2026" → "rank it the
most dangerous"), and a figure detached from the comparison that gave it meaning ($4.74M for high-shadow-AI
orgs, whose entire finding is the $670K delta against $4.07M — and which measures shadow AI, not agents).
**Why it's a piece:** it is his own three-times-written argument — the control that answers correctly, the
register that is honest and incomplete, the ban that arrives because there is nothing to attach to — applied
to the evidence base his readers make decisions on. And it is *demonstrable* rather than asserted.
**The ending is already written:** `References\research_shadow-ai-global-stats_2026-08-10.md`, on his own
LinkedIn post — *"the post's own thesis is that unverified numbers quietly become known facts that other things
get built on. The post is currently an instance of it."*
**Needs:** one worked example a reader can do in ninety seconds. The $4.74M → $670K delta is the candidate.
**Why parked, not scheduled:** the self-implicating version is strong but it must not become a piece about the
newsletter. Wants a week where it is the Saturday, not a weekday.

### ⏸ South Australia's royal commission — teeth that cannot bite
**Thread:** Ad Hoc Regulatory Regime × Shape of Work-to-Come · **Note:** `Vault\Writing\Signals\SA royal commission into AI.md`
**Core:** announced 10 Aug. Three commissioners (unnamed, international search), ~$3M, starts **October 2026**,
reports **by 1 July 2027**. The *Royal Commissions Act 1917* (SA) compels attendance and production, gaol up to
three months for refusal, no rules of evidence — **and the findings bind nobody.** SA's own 2016 Nuclear Fuel
Cycle RC had its central recommendation abandoned. Against NSW's register — which has no compulsory power and
*does* bind agencies — it is a clean pair: **the instrument with teeth cannot bite; the instrument that binds
cannot see.** Reports as the federal AI standards bill is expected in parliament (early 2027).
**Why parked:** **terms of reference are 4–6 weeks out (mid-to-late September).** That is when this becomes
writable in detail. Diary it. Australia's first, **not the world's first**.
**Nearer-term use:** the counter-example in the Sun 16 capstone. Already noted there.

### ⏸ Anthropic's 1.4 GW and the copyright ask
**Thread:** AI Sovereignty × Ad Hoc Regulatory · **Note:** `Vault\Writing\Signals\Anthropic Australian capacity tender and the copyright ask.md`
**Core:** AFR off tender documents — 1.4 GW of Australian data-centre capacity, **US$15bn (≈A$21.6bn)**, 1 GW
live by end-2027, procured not built. AFP off **Treasury's FOI'd briefing notes** — investment recorded as
contingent on copyright clarity, with the **"long tail"** of small rights holders as the stated obstacle;
officials rejected it; Anthropic declined to comment. Australia has refused a TDM exception repeatedly.
**Why it's a piece:** sovereignty negotiated in a Treasurer's briefing pack rather than a press release, and
the artefact is the government's own note. Albanese's "Anything less, is theft" is the on-record counterweight.
**Why parked:** wants the tender outcome (which providers won) or the National Cabinet result. **Cut the
"same play in the EU and UK" line** — no documented basis for Anthropic specifically.

### ⏸ The token gray market — sovereignty arriving via expense claim
**Thread:** AI Sovereignty × Trust Boundaries · **Note:** `Vault\Writing\Signals\Token gray market - the operator can read every prompt.md`
**Core:** Okta (4 Aug) and Unit 42 (6 Aug). Resellers at **5–15% of official per-token price**, stocked by
fraudulent signups, abused startup credits ($25K–$100K) and stolen developer keys, routed through reverse-proxy
"transfer stations". Okta: *"the service provider has full visibility into prompts, as those prompts must be
forwarded to a model."*
**The honest line, and it is better than the scare:** nobody has shown prompts *are* harvested — and Permiso
documented that `oai-reverse-proxy` **defaults to not using a key if invocation logging is enabled**. The market
has engineered around the only instrumentation that would produce evidence. Scale is hobbyist (881 users).
**Pairs with:** the Filby trust-erosion / shadow-AI caution beat below, and
`References\research_shadow-ai-global-stats_2026-08-10.md`. Between them there is a full shadow-AI piece whose
argument is *the numbers you are being shown do not measure what you think, and neither does the silence.*
**Do not cite SecurityWeek** — no such article found. Cite Okta and Unit 42.

### 💡 "Your Team Will Believe the Layoff Headline Over Your Roadmap" — companion to the Filby caution beat
**Source:** Nate's Newsletter, ~10 Aug 2026. **Thread:** Shape of Work-to-Come
**Core:** staff are not asking whether AI works; they are asking what happens to them if it does. The
leadership/frontline communication gap as a material business risk — the human-side version of *name which
tasks move to AI, or your team writes that list themselves, badly.* Slots straight into the parked **Eliza
Filby** trust-erosion beat above; between them the caution piece has both halves (surveillance erodes trust,
and silence lets the worst available narrative win). ⚠️ framing, not a finding — no data behind it.

### 💡 Held, deliberately: the on-prem cost argument
`Vault\Writing\Signals\Private AI cost parity - the break-even does not survive arithmetic.md`.
The "$8–12K box, parity in 3–6 months above 50K queries/month" claim **fails** — vendor content both sides, no
working shown, ~33 months before power against real August 2026 API pricing, and the 50,000 figure appears in
neither source. **This kills the tempting "the cost excuse expired too" follow-up to
[[Compliance deadlines converge with open-weight parity]].** What survives and is worth building on instead:
the hardware band (a ~$10K box *can* serve a 70B at Q4), **per-seat licensing crossover at 100–150 users**, and
vendor dependency — the *"missing economic leg"* already parked further up this file. If that piece gets
written, it needs an independent TCO source, and none currently exists.

---

## 🗄️ Retired — decided against, do not re-bench

### ~~"Open Weights From the House That Closed Them"~~ (gpt-oss) — RETIRED 5 Sep 2026
**Thread was:** AI Sovereignty (Model Sovereignty) · Ad Hoc Regulatory Regime
**History:** proposed as Wed 19 Aug in `week-plan_2026-08-17` v0. Benched from 17-23 Aug, benched again
in 24-30 Aug with a "decide by 31 Aug" deadline, then flagged as overdue five more times across the
31 Aug and 7 Sep plans. **Lars's call, 5 Sep 2026: "retire it."**

**The thesis was:** OpenAI shipping Apache 2.0 reasoning models kills the last procurement objection —
*we can't get a name-brand model on-prem* — and now you can.

**Why it is retired, written down so nobody revives it on merit a sixth time.** The thesis was spent
four times, twice of them *before the bench entry was even written*:
- **"Where It Thinks" (20 Jul, published)** — the procurement half, already in print: gpt-oss is *"the
  white flag on the idea that the model itself is the moat,"* and gpt-oss and Inkling are *"Western,
  permissively-licensed, cleaner-lineage options built precisely for the buyer who needs a provenance
  story they can defend to a lawyer."*
- **"KYC Reversal" (7 Jul, published)** — carried the Apache 2.0 fact.
- **"Control You Can Locate" (5 Aug, published)** — the whole located-control frame, plus the
  open-weights-is-not-open-source honesty caveat.
- **"Own the Kitchen" (8 Aug, published)** — the headline move, verbatim: *"The firm most associated
  with keeping the kitchen locked just handed a lot of people the recipe. For anyone who wanted the
  familiar brand but on their own hardware, that was the last excuse gone."*

⚠️ **And "Control You Can Locate" refutes it outright:** *"for the heavily-regulated shop, the keep is
rarely bare open weights on a box in the server cupboard — that strips away the very accountability the
regulator came for."* The bench thesis claims gpt-oss kills the procurement objection; his own
published text says bare open weights is **not** what a regulated buyer wants. Drafting it would put
him against himself and a procurement reader would catch it.

**The transferable lesson:** a bench item that "survives on merit" every review is not evidence it is
alive. Nobody was re-reading the published set. **Check a bench thesis against `Substack Published\`
before renewing it, not just against the current week.**

---

## ⏸ Parked — the live successor to the gpt-oss piece

### "The Third Condition" (working title) — the licence layer nobody checks
**Thread:** AI Sovereignty (Model Sovereignty) · Ad Hoc Regulatory Regime · Diversion-shaped
**Added:** 5 Sep 2026, on retiring the gpt-oss piece. **Earliest slot: week of 21 Sep.**

**The core, and it is already half-verified in the corpus.** "Open" has three separate conditions —
**downloadable, runnable, and legally usable for your specific business model** — and the third is the
one procurement never checks. Four models, four different legal answers:
- **GLM-5.3** — Z.ai held the weights on 14 Aug (*"As we scaled post-training, cyber capability
  developed faster than we expected"*) and **shipped them 28 Aug under a bespoke licence**, not the
  open licence it had been on. The weights came out; the *terms* changed.
- **Kimi K3** — the $20M gate binds **Model-as-a-Service operators only**; §4 expressly carves out
  internal use. **A bank or a club self-hosting internally is not caught.** The SaaS reselling it is.
- **Qwen** and **Muse Glimmer** — Apache 2.0, no gate.
- **gpt-oss** — Apache 2.0, no gate.

**The reader skill:** before you deploy an open-weight model, read clause 4, not the headline. Ask
which of the three conditions you actually have.

⚠️ **The trap to avoid, and it would be our own engine-7 failure.** There is **no "open weights are
closing" trend** and the piece must not imply one. The only ledger found (28 Aug 2026) records **three
instances ever** — GLM-5.3 (held two weeks, shipped), gpt-oss (delayed 2025, shipped), Llama 4 Behemoth
(unreleased, **no safety reason given**, only "still training") — and its own finding is that stated
reasons are rare and most apparent delays were pre-disclosed schedules. **The spine is the licence
layer, not the tap.**

⚠️ **Adjacency gate.** *"Somebody else's terms"* is the spine of the week of 7 Sep, and Thu 10 Sep is
vendor-controlled access gates on closed models. This is the same move on a different actor. **Do not
run it within two weeks of Thu 10.** Stronger if a second licence change lands first.

**Distinct from ["Open Is Not Local"](#) above** — that is a *hardware* piece whose resolution is
quantisation. This is a *legal* piece. Do not merge them.

**Sources to start from:** `References\research_kimi-k3-weights_2026-07-26.md` ·
`References\research_story-candidates_2026-08-23.md` §7.3 (licence text re-verified from primary) ·
`References\research_story-candidates_2026-09-05.md`
