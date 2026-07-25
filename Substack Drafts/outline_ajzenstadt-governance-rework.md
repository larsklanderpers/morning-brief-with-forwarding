# Outline: Reworking the 4 Levels of AI Governance — Australian Market Frame

**Reference:** Ajzenstadt / Limestone Digital — 4 Levels of AI Governance (@mardehaym)
**Original framework:** Interception → Control → Tracing → Impact Measurement
**Our angle:** That framework is sound engineering thinking. But it's written for CTO teams. Australian regulated industries already live these obligations — they just call them something else. And there's a fifth layer Ajzenstadt missed entirely.

---

## Working title options

- "You Already Have an AI Governance Framework. Your Regulator Called It Something Else."
- "Four Layers Is Not Enough: What Australian Regulated Industries Need to Add"
- "The AI Governance Framework Your Compliance Team Already Knows"
- "The CTO's Governance Framework Won't Satisfy APRA"

---

## Core argument / thesis

Ajzenstadt's 4 levels are correct — but they're scoped to internal AI operations (what your teams build). Australian regulated entities face a different test: their regulators want to see governance outcomes, not governance architecture. The translation layer — from technical controls to regulatory proof — is what most organisations are missing. And there's a fifth layer that Australian law requires that no international framework has yet named.

---

## Audience

- CROs, CCOs, Chief Risk Officers in Australian financial services, insurance, superannuation
- Heads of compliance and risk in gaming/clubs, health, and government
- Tech leaders who need to translate AI capability to board-level risk conversation
- NOT: developers or AI practitioners (that's Ajzenstadt's audience)

---

## Series / format decision

- Option A: Five-part series (one post per layer)
- Option B: Single long-form (2,500–3,500w) — strong as a Saturday long-form
- Option C: Reference card / framework post (shorter, more prescriptive — good for LinkedIn)

---

## Layer 1: Interception → **Gateway and Classification**

### Ajzenstadt's version
- Single LLM gateway — all AI traffic routes through one control point
- Prevents shadow AI; creates a policy enforcement choke point

### Australian translation
- Data classification has to happen *before* the model sees anything
- AUSTRAC parallel: you can't report what you haven't seen — threshold transaction reporting requires knowing what passes through
- APS 234 parallel: information assets must be identified before they can be protected
- The Privacy Act angle: APP 1 (open and transparent management) — you have to be able to describe to affected individuals what happens to their data before it hits a model

### What to flesh out
- Most Australian organisations haven't classified their data even *before* AI arrived — the gateway problem is downstream of a classification gap
- Retroactive risk: documents already indexed by Copilot, SharePoint data already in RAG pipelines — the gateway arrived after the horse bolted
- What "gateway" means in practice across on-prem / cloud / hybrid environments
- Example: a Clubs NSW member's gaming history, problem gambling flags, and behavioural data should never reach a cloud LLM — but does any club have a gateway that knows that? What's the RG obligation if it does?
- The shadow AI dimension: employees who bypass the gateway aren't a tech problem, they're a culture and training problem

---

## Layer 2: Control → **Authorisation and Meaningful Human Review**

### Ajzenstadt's version
- RBAC (role-based access control) + deterministic verifier gates
- High-risk AI actions require human sign-off
- Roles determine what the AI is allowed to do on your behalf

### Australian translation
- "Meaningful human oversight" — APRA's April 30, 2026 letter used these words; it's now the standard being enforced
- AUSTRAC parallel: the "tipping off" prohibition — a human decision-maker remains accountable even when AI generates the suspicion flag. The SMR is the human's document.
- Privacy Act December 10, 2026 amendments: APP 1.7/1.8/1.9 — if a decision is "substantially automated," disclosure obligations kick in even if a human nominally approved it
- The board layer: Ajzenstadt makes this a developer problem (RBAC). APRA makes it a board responsibility.

### Key tension to name
- Perfect RBAC ≠ meaningful review. You can have every technical control in place and still fail the APRA test.
- GhostApproval: the human who signs off on AI output they don't understand is worse than no human — it's false assurance
- APRA's four failure categories from the April 30 letter: governance, assurance, cyber, third-party risk — all four can coexist with a working RBAC system

### What to flesh out
- What does "meaningful" actually require in practice? (not just a checkbox)
- Who trains the approvers? What's their liability if they approve AI output they couldn't evaluate?
- Example: AI-assisted credit decisioning, insurance claims, or welfare benefit determination — the human approver carries the decision, even if they never understood the model's output
- The liability gap when AI gives a wrong recommendation and a human rubber-stamps it

---

## Layer 3: Tracing → **Audit Trail and Regulator-Legible Explainability**

### Ajzenstadt's version
- OpenTelemetry full audit trail
- Every AI action logged: what model, what prompt, what response, what version, what latency
- Technical completeness is the goal

### Australian translation
- Explainability under the proposed Privacy Act ADM amendments — affected individuals can request an explanation of why a substantially automated decision was made about them
- AUSTRAC: a suspicious matter report must articulate why a transaction triggered concern — if AI generated the flag, the audit trail has to support a human writing that explanation
- ASIC/AFCA: if an AI-assisted financial recommendation is disputed, the entire decision chain must be reconstructable — model version, inputs, outputs, who reviewed, what changed

### The gap Ajzenstadt doesn't address
- Log completeness ≠ regulator-legible explainability
- A 40-line OpenTelemetry trace doesn't explain to a consumer or regulator why they were declined, flagged, or denied
- Inference sovereignty: if the trace lives in a US data centre, does it satisfy Australian regulatory requirements? APRA's concern: data residency ≠ inference sovereignty
- Language gap: devs log what happened; regulators want to know why it was *appropriate*

### What to flesh out
- The OAIC complaint scenario: what will they actually ask for when an ADM decision is challenged?
- Who is responsible for translating a technical trace into a regulatory explanation? (This role doesn't exist yet in most orgs)
- Example: an AI-driven fraud alert triggers an account freeze — the affected customer challenges it — what does AFCA need to see, and can your trace provide it?
- The model version problem: if the model was updated between decision and complaint, can you still reconstruct the original reasoning?

---

## Layer 4: Impact Measurement → **Compliance Outcome Accountability**

### Ajzenstadt's version
- AI usage mapped to business outcomes
- KPIs: delivery performance, model accuracy, latency, reduction in manual work
- "Did the AI help?" — measured in business efficiency terms

### Australian translation
- Compliance outcome measurement: not "did the AI work" but "did it work *without causing harm*"
- APRA's new push: not just that you have a policy, but that you can demonstrate it's working — the assurance failure category from April 30
- Clubs/gaming parallel: responsible gambling programs already do this — RG measures harm reduction outcomes, not just policy existence. AI governance should adopt the same frame.
- Privacy Act: if AI-assisted decisions are causing disproportionate adverse outcomes for specific groups, that's a systemic issue that has to surface in compliance reporting

### What Ajzenstadt missed
- Business value ≠ compliance value. An AI that improves NPS but misclassifies vulnerable customers has negative compliance ROI.
- Vendor concentration risk as a measurement dimension: your AI performance KPIs don't capture what happens when your model provider is acquired, changes terms, or has an outage
- The insurance sector parallel: APRA's prudential AI guidance is coming — "we have a governance framework" is not the same as "we can demonstrate it's working"

### What to flesh out
- What does a compliance-oriented AI KPI dashboard look like vs. a standard business performance dashboard?
- How do you measure *absence of harm* — especially when the harm is subtle (e.g., demographic bias in a scoring model)?
- The superannuation example: a fund using AI for member advice triage — the regulatory measure is member outcomes, not model latency. Whose job is it to measure that?
- Vendor dependency as a risk metric: concentration risk calculations already exist in APRA's framework — AI-as-a-service should be in them

---

## Layer 5 (missing from Ajzenstadt): **Enforcement Accountability**

### The gap
Ajzenstadt's framework governs how your organisation uses AI internally. It has nothing to say about what happens when your AI causes harm externally, or who bears regulatory accountability when the regulator comes knocking.

This is uniquely important in Australian regulated industries because:
- The Privacy Act, the Corporations Act, CPS 220, and AUSTRAC's AML/CTF Act all place *entity-level* obligations on regulated organisations — not on their AI vendors
- OpenAI, Microsoft, and Anthropic are not your regulator's counterparty. You are.

### Australian-specific obligations
- Director liability: the Corporations Act requires directors to exercise due care over material risks — AI is now a material operational risk for most regulated entities
- APRA CPS 220 (risk management): board-level accountability for the risk management framework, which now needs to include AI
- OAIC: if an APP entity's AI causes a notifiable data breach, the entity notifies — not the vendor. The vendor contract matters, but the obligation is yours.
- The forthcoming APRA prudential practice guide on AI: enforcement is not hypothetical — APRA has already cited governance failure as a finding in recent reviews

### What to flesh out
- Who owns the AI risk signature in Australian boardrooms today? (Most can't answer this clearly)
- The vendor responsibility gap: what your enterprise AI contract actually says vs. what you think it says about liability
- What a board-level AI risk attestation should look like — and what it looks like in practice today (usually: nothing)
- The discrimination complaint scenario: an AI-assisted lending decision triggers an ACCC/AFCA complaint — the liability trail leads to the lender, not GPT-4o
- Insurance question: are directors covered for AI-related governance failures under their D&O policies? (Most D&O policies haven't been tested on this)

---

## Close / CTA angles

- "The Ajzenstadt framework is the right starting point — but it stops at the org boundary. Australian regulated entities need to go further."
- Connection to the gaming floor piece: KYC already IS Layers 1–3 in practice — clubs have been doing this for twenty years and don't realise it
- Call to action: can your organisation demonstrate all five layers to your regulator today?
- The board question: does your AI governance framework have a named owner, a documented attestation process, and a complaints response procedure?

---

## Related pieces / backlinks

- Gaming Floor / KYC long-form: the parallel between AML/CTF obligations and AI governance layers
- Kill Switch: what happens when the regulator pulls the plug — enforcement accountability is the bridge
- Click Approve / GhostApproval: Layer 2 in practice — the human who can't evaluate what they're approving
- Not Where It Lives. Where It Thinks.: inference sovereignty as the gap in Layer 3's audit trail

---

## Research to do before drafting

- [ ] Pull APRA April 30 letter language on "meaningful human oversight" — exact quote
- [ ] Check whether CPS 220 has been updated to explicitly reference AI
- [ ] Find an Australian case study where an AI governance failure attracted regulatory action
- [ ] Check OAIC's current guidance on ADM — what does the complaints process look like pre-December 10?
- [ ] Confirm status of APRA prudential practice guide on AI (timeline?)
- [ ] Look at whether any Australian D&O insurer has issued AI-specific guidance
