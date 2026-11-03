---
date_first_seen: 2026-08-06
date_updated: 2026-08-06
source: NSW Department of Customer Service / NSW Office for AI (primary documents)
url: https://www.digital.nsw.gov.au/policy/artificial-intelligence/ai-governance-assurance-and-frameworks/nsw-ai-assessment-framework
url_2: https://www.digital.nsw.gov.au/sites/default/files/2026-07/nsw-ai-operational-policy-2026-v1_2.pdf
brief: ai
threads: [Ad Hoc Regulatory Regime, AI Sovereignty, Supply Chain]
beat: AI / Policy / Australia / NSW
status: developing
used_in:
---

# NSW mandates AI registration, assessment and attestation across government

**What happened.** NSW published its **AI Operational Policy** (approved 11 Jun 2026, published Jul 2026),
issued under **Circular DCS-2026-02** and binding on all NSW Government sector agencies, statutory
authorities and their employees — State Owned Corporations and Advisory Entities are *recommended*, not
mandated. Four hard obligations: nominate an **Accountable Official within three months** of issue; **register
every AI use case before use** (existing use "as soon as practicable"); run the **AI Assessment Framework**
where registration says to, referring critical and high-risk cases to the **AI Review Committee within five
business days of completing the AIAF**; and file an **annual attestation by 31 October**, endorsed by the
Accountable Official and approved by the Agency Head, first one due **31 Oct 2027**. Plus AI incident
reporting to the Office for AI and AI literacy training "made available to employees." The AIAF is the
instrument — **16 mandatory questions** in Section 2 that produce a risk level and trigger a Privacy Impact
Assessment, a Human Rights Impact Assessment and a cybersecurity review. It currently ships as a **2.33 MB
Excel workbook**; the platform version is under development.

**Why it matters.** This is the state jurisdiction doing what the Commonwealth said it would not. Howell's
read of the federal plan (see [[Australia mandatory AI standards and Office of AI]]) was that Australia
centralises *coordination* but leaves supervision to existing regulators "using their general powers rather
than introducing any special ex ante AI regulatory powers." NSW built the ex ante machinery anyway: a new
gate, a new committee, a new register, a new attestation. Federal enforcement is staged 2027–28; NSW's first
attestation lands 31 Oct 2027. **The state is ahead of the Commonwealth and has more teeth** — which is still
the shape of an ad hoc regime, except the uncoordinated bodies are now federal and state rather than industry
and statute. Anyone operating across state lines reconciles two.

## Observations

- **2026-08-06** — First seen. Both primary documents fetched and the specifics below verified against them.

- **2026-08-06 — The hole is the supply chain, and it is explicit.** Third-party suppliers who use AI to
  deliver services to an agency are **excluded from the registration requirement**; those arrangements are
  "managed through procurement, contracting, and supplier assurance processes." So the register — the thing
  that makes the whole regime legible, and the thing the Office for AI reports on — covers AI the agency runs
  and not AI the agency buys the output of. Meanwhile the only contractual lever named is that arrangements
  must support "transparency, including mechanisms for suppliers to disclose AI use and notify the agency of
  material changes over time." An agency can be fully compliant and still not know what its vendors run. That
  is the piece.

- **2026-08-06 — The obligation that will actually bite is continuity, not ethics.** Agencies must ensure AI
  systems "maintain continuity of government services, including the ability to operate or transition services
  if an AI solution, model or service becomes unavailable or materially changes," and that "AI dependencies
  supporting critical services have tested business continuity plans." Records of AI-generated decisions must
  be "captured and retained as State records" under the **State Records Act 1998**, where they inform decisions
  affecting "people's rights, interests, or access to services" — and loss or destruction gets reported to
  State Records NSW. A policy explicitly refusing to let an agency become dependent on a vendor it cannot
  replace, and refusing to let the audit trail live only in the vendor's system. Public-sector version of
  [[You cannot rent an audit trail]]. Also the most expensive lines in the document, and the ones least likely
  to survive a procurement cycle intact.

- **2026-08-06 — "Treat all inputs to and outputs of AI systems as potentially shared with the provider."**
  Stated flat, as policy, by a state government. Paired with: "Do not enter personal and/or health information
  (OFFICIAL: Sensitive or above) or security classified information into AI systems unless this use is
  explicitly approved by your agency." This is the sovereignty argument arriving as an acceptable-use clause
  rather than as infrastructure policy — cheaper, faster, and it bites the week it is written. Contrast the
  federal approach of underwriting data centres.

- **2026-08-06 — Where AI faces the public, a human alternative is mandatory.** "Where AI interacts with the
  public, ensure a human or non-AI service option is available as part of the overall service." One sentence,
  and it quietly caps how much of the savings case an agency can ever book. Worth pricing.

- **2026-08-06 — The law-enforcement carve-out is unusually well-drafted.** Exempt "to the extent that
  compliance would prejudice, or would be reasonably likely to prejudice, the agency's lawful performance of
  its operational, investigative, intelligence, protective or emergency response functions" — but "not a
  blanket exemption," not available "to administrative or non-operational uses of AI," "strictly limited to
  what is necessary," documented, "justified on a use-case basis, with periodic review," and law enforcement
  still carries internal governance and accountability duties. Hold it up next to jurisdictions that wrote the
  same carve-out as a single sentence. If it holds, it is a model; if it quietly widens, it is the story. (No
  separate national-security exemption appears in the document.)

- **2026-08-06 — Indigenous representation is a governance control, not a values statement.** Decision-makers
  must consider lifecycle impacts "including appropriate Aboriginal and Torres Strait Islander representation
  in design, implementation and oversight," and agencies must ensure outputs are "appropriate for diverse
  communities, including Aboriginal and Torres Strait Islander people." The policy also credits Aboriginal and
  Torres Strait Islander contributors to its own drafting. Rare to see this land as a board-level control.
  Relevant to the tribal data sovereignty framing for the NIGC/US audience.

- **2026-08-06 — This runs opposite to CPS 230, and that is the piece.** Lars flagged the register
  exclusion as cutting against the [[APRA CPS 230 voice AI vendors]] argument. It does, and harder than
  "federal and state disagree." Both regimes turn on a **register**, and they point in opposite directions:

  - **CPS 230 catches vendor AI without ever naming it.** Materiality is functional — "those on which the
    entity relies to undertake a critical operation or that expose it to material operational risk." Offshore
    provision is captured as a **material offshoring arrangement** with a duty to notify APRA *before*
    entering it. The standard contains no mention of AI, inference or data residency, and catches AI anyway.
  - **The NSW policy names AI everywhere and misses it.** Because the register is scoped to the agency's
    *own* AI use cases, AI arriving inside a supplier's service is explicitly out — "managed through
    procurement, contracting, and supplier assurance processes."

  So the **technology-agnostic instrument has the coverage the AI-specific one lacks.** That inverts the
  default assumption of the whole policy debate — that AI needs bespoke rules — and it is a much better
  argument than "the states and the Commonwealth are out of step." The out-of-step version is the setup;
  this is the payload.

  **The asymmetry a skeptic will swing at, and the honest answer.** These are not the same instrument:
  CPS 230 is a prudential standard binding regulated financial entities, its register is a *material
  service provider* register rather than an AI register, and NSW is a public-sector policy with an
  AI-specific one. Do not write it as a like-for-like comparison — it is not. Write it as the mechanism
  point: a register keyed to **function and reliance** catches AI wherever it enters, a register keyed to
  **the technology the entity itself operates** only catches what the entity operates. The scoping choice
  decides the coverage, and NSW made the newer choice and got the smaller net. Concede the asymmetry in
  the piece rather than waiting to be handed it.

  **Draft target:** Ad Hoc Regulatory Regime slot, week of 17–23 Aug (per `References/week-plan_2026-08-17.md`,
  which already reserves one) — or the 10–16 week if it lands sooner.

- **2026-08-06 — Research pass corrects the framing: it is a visibility gap, not a coverage gap.** Full dig in
  `References/research_nsw-ai-operational-policy_2026-08-06.md`. NSW's *AI procurement essentials* (updated
  **6 May 2026**) explicitly names *"Platform, service or outcome-based procurement involving AI: Contracting a
  supplier to deliver a specific outcome or deliverable, where the supplier utilises generative AI technologies
  as part of service provision"* and expects an AIAF triage at planning and an AIAF self-assessment at sourcing —
  under a Procurement Policy Framework with statutory force under the *Public Works and Procurement Act 1912*.

  So supplier AI is **not unregulated. It is unregistered.** Do not write "nobody covers vendor AI" — a
  procurement officer will take the piece apart in the comments. The defensible claim is about the register and
  the reporting line built on it: vendor AI is checked once at purchase and then never appears in the central
  inventory the Office for AI reports on or the attestation certifies.

  Better still, the two tracks are not reconciled with each other — the procurement guidance predates the July
  policy by two months and still describes the AIAF self-assessment world rather than the register world. That
  is the ad hoc regime in miniature, inside a single government, and it is a stronger fact than the one this note
  started with.

- **2026-08-06 — The assurance picture is now complete, and it is soft all the way down.** Mandatory gate,
  voluntary everything behind it: attestation is self-signed with internal audit only *"strongly recommend[ed]"*;
  **no penalties or enforcement provisions appear in the document at all**; the AI Review Committee's advice on
  critical-risk systems is *"advisory, with agencies retaining full decision-making authority and
  accountability"* (12 members, chaired by **Prof. Ed Santow**); and the Auditor-General's AI governance audit is
  **scheduled for 2026–27 and has not yet reported**. Nothing published on registered use-case counts or
  high/critical outcomes. The absence of a number is the evidence.

## Feeds

- [[Ad Hoc Regulatory Regime]] — a state regime running ahead of, and independently of, the federal one; new ex ante powers where the Commonwealth declined to create them
- [[APRA CPS 230 voice AI vendors]] — the counter-example: a technology-agnostic register that catches vendor AI, against an AI-specific register that exempts it
- [[AI Sovereignty]] — sovereignty asserted through acceptable-use and continuity clauses rather than infrastructure spend
- [[Supply Chain]] — supplier-delivered AI is exempt from the register; contracts are the only lever

## Open

- **Version hygiene.** The file is served as `nsw-ai-operational-policy-2026-v1_2.pdf`, the document body reads
  **"Final version 1,"** approved 11 Jun 2026, published Jul 2026. No effective/commencement date is stated —
  only a transitional period. Do not cite a version number or a commencement date without re-checking the
  document itself.
- ~~**Does the Operational Policy supersede the AI Ethics Policy / DCS-2024-04?**~~ **RESOLVED 2026-08-06 —
  yes, both.** DCS-2024-04 (issued 1 Jul 2024) is marked **Archived, superseded by DCS-2026-02** on the NSW
  circulars register, and the policy states it *"replaces the NSW AI Ethics Policy."* So the staleness claim is
  live and citable: the **AIAF landing page** still cites DCS-2024-04 and the Ethics Policy as its authority, and
  the **Ethics Policy page itself carries no supersession banner** and reads as current guidance (both checked
  6 Aug 2026). Bonus fact for the thread: DCS-2020-04 → DCS-2022-01 → DCS-2024-04 → DCS-2026-02, four circulars in
  six years, no statute.
- ~~**Attestation assurance unverified.**~~ **RESOLVED 2026-08-06, and I was wrong to retract two provisions —
  both are in the document.** The extension pathway is real: written request to the Office for AI *"prior to
  30 September of every reporting year,"* with a *"time-bound remediation plan, including milestones, interim
  controls."* The internal-audit line is real and is a recommendation, not a requirement. An attestation template
  exists and *"includes the evidence requirements"* — but is not published anywhere reachable, so the evidence
  standard exists and is not public. Minor ambiguity left: the extension text reads first-cycle in one place and
  *"every reporting year"* in another; don't assert "one-off grace period."
- **Nobody has read the sixteen questions.** They live inside the XLSX, not on the page, and the page does not
  name the risk-level categories. The Medium/High boundary is where the cost lands — a PIA, an HRIA, a cyber
  review and an AIRC referral per High case, plus central oversight above **$5M** under the Digital Assurance
  Framework. Pull the workbook and read the scoring logic before writing the economics.
- **How many use cases are registered, and how many came back High or Critical?** Searched 2026-08-06 — **nothing
  published.** No case counts from the AIRC, no figures in the Jan 2026 media release, no Auditor-General report
  yet. Treat the absence as the finding rather than chasing a number that isn't there.
- **The forward hook.** The Auditor-General's *Governance of NSW Government agencies' use of artificial
  intelligence and automation* is an upcoming **2026–27** audit (announced 10 Sep 2024, page updated 20 Feb 2026).
  That is when the "mandatory gate, invisible behind it" claim gets tested — so writing the gap now gives the
  piece a scheduled sequel.
- **No independent legal commentary exists on this policy.** Searched 2026-08-06 and found none — AU firms have
  covered NSW WHS/AI and the federal 2026 landscape, nobody the Operational Policy itself. For a
  whole-of-government mandatory instrument a month old, that silence is notable, and it means being first carries
  the matching obligation to be right.
