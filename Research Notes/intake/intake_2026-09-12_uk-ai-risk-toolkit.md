---
type: intake
date: 2026-09-12
source_url: https://www.gov.uk/government/publications/ai-risk-management-toolkit/ai-risk-management-toolkit-guidance
primary_url: https://www.gov.uk/government/publications/ai-risk-management-toolkit
slack_permalink: https://lars-klander-personal.slack.com/archives/C0BVCSV0PJ5/p1789092636186849
slack_ts: "1789092636.186849"
lars_note: "this probably needs to be added to our information corpus, if you can get it into the vault?"
reactions: [pushpin]  # his words ("get it into the vault"), not an emoji; no reaction was on the message
verdict: feeds a thread (Ad Hoc Regulatory Regime; secondary Trust Boundaries). Optional exhibit for Fri 18 "What Your Contract Calls It", not proposed as the verdict.
filed_to: Vault/Writing/Signals/UK AI Risk Management Toolkit - guidance, not a gate.md
---

# AI Risk Management Toolkit (UK Department for Science, Innovation and Technology, 8 Sep 2026)

Posted to #heinlein-inbox by Lars 10 Sep 2026 19:10 PDT; intake was down, processed 12 Sep. Both pages
fetched live 12 Sep 2026 via Firecrawl (served from Firecrawl's cache, cached 12 Sep 07:00 UTC). The
guidance page came back complete: the fetched text runs through Appendix 4 and the GOV.UK page footer,
so absence claims below are from a whole-document read, not a truncated one.

**Who is speaking and what interest they have.** A UK government department describing its own
publication. No commercial interest. It is the primary for claims about its own status, structure and
content. It is not a source for what any other UK instrument requires.

## Extracted

### Status and provenance (parent page and page metadata)

- **Publisher:** Department for Science, Innovation and Technology (DSIT). GOV.UK format label:
  **"Guidance"**. Crown copyright 2026, Open Government Licence v3.0.
- **Published:** 8 September 2026 (metadata: first published 2026-09-08 11:53:29 BST). The page's
  "Updates to this page" history lists only *"Published 8 September 2026"*. Page metadata carries a
  technical `updated-at` of 2026-09-10 09:33 BST with no public change note. Treat it as unchanged since
  8 Sep.
- **Parent page summary:** *"Guidance to help anyone involved in AI projects understand, assess and
  manage risks when designing, procuring or delivering AI products."* It *"supports anyone involved in
  designing, operating, procuring or delivering products that use artificial intelligence (AI)."*
- **Documents on the parent page:** the HTML guidance, plus *"AI Risk Management Framework: workbook"*
  as XLS (280 KB) and ODS (18.5 KB). Filename:
  `20260522_AI_Risk_Management_Framework_workbook_V1.1_OFF.xlsx`, so the workbook is dated 22 May 2026,
  version 1.1, and carries an "OFF" suffix (probably the OFFICIAL marking; not confirmed). **The workbook
  was not opened** (downloading a file needs Lars's OK).

### Is it mandatory? What the text actually says

- The guidance body is written for **UK government departments and the public sector**: *"This Toolkit
  has been created to assist departments with identifying and managing risks associated with the
  development, deployment, procurement and use of AI solutions."* Also: *"for the UK public sector to
  succeed in its ambition to realise significant benefits from AI."* Risk appetite should be *"signed
  off at the departmental board level."* Security appetite rows refer to *"HMG property, assets,
  information or people."*
- The parent page says "anyone involved in AI projects." **Nothing in either page addresses the private
  sector specifically.**
- **No statement that anyone is required to use it.** It calls itself *"a starting point for teams
  looking to implement good risk management practices."* It cites no statutory or policy mandate for
  itself. The one ask of departments is soft: *"The Government Digital Service (GDS) encourages
  departments to keep a central log of AI risks, and to share these with GDS and the Department of
  Science, Innovation and Technology's (DSIT) Central AI Risk Toolkit Team (CAIRF) team."*
- The word "must" appears only inside the method (scores *"must be scored between 1 and 5"*; senior
  leaders *"must own responsibility for the organisational risk appetite"*) and once on the parent page
  (*"You must understand and justify AI risks and treatment strategies to use AI responsibly and
  ethically"*). None of these is a mandate to use the toolkit. The word "voluntary" does not appear
  either. **Exact status: guidance, no requirement stated.**

### What it maps to

- **Orange Book.** *"The Toolkit is designed to implement Section D: Risk Management Processes of the
  Orange Book"*: risk identification and assessment, treatment, monitoring, reporting. Its appetite scale
  is *"designed to align with the Orange Book."* The toolkit describes the Orange Book as establishing
  *"risk management principles and processes for government departments and other UK public sector
  organisations."*
- **Cyber Assessment Framework (CAF).** Security questions let a team reuse CAF evidence section by
  section: A1 Board Direction, A2 Risk Management, A4 Supply Chain, B1 Service Protection Policies and
  Processes, B3 Data Security, B6 Staff Awareness and Training, Objective C Detecting Cyber Security
  Events, Objective D Minimising the Impact of Cyber Security Incidents, each *"assuming your response
  has been expanded to include use of AI."*
- **AI Playbook for the UK Government:** the risk questions are a starting point to extend *"using the
  principles set out in the AI Playbook for government."*
- **Also named:** NCSC *principles for the security of machine learning*; *"the GDS and RTA's
  Algorithmic Transparency Recording Standard"* (asked as *"Have you complied with...?"*); ICO guidance on
  AI and data protection; EHRC guidance on the Public Sector Equality Duty; UK GDPR (including the right
  to rectification); Human Rights Law; Equality Law; Intellectual Property; Social Value Act; DPIAs.
- **EU AI Act:** named only as an example of *"applicable AI Laws (E.g. EU AI Act)"* and in two
  questions about keeping a regime *"that allows us to continue to export to our trading partners."*
- **Standards:** only generically. ISO, IEC and IEEE SA are named as standards bodies, pointing to the
  AI Standards Hub database. **ISO/IEC 42001 and NIST AI RMF are not named anywhere in the text.**

### Structure

- Components listed: a guide to AI risk assessment; *"a set of critical questions"*; *"a workbook to
  record identified risks"* (an existing risk register may be used instead); *"an AI Risk Monitoring
  Dashboard."* **The dashboard is not a separately published file**; presumably inside the workbook,
  unverified.
- **Roles:** a multi-disciplinary "AI risk management team", ideally led by an **AI governance officer**,
  plus senior leaders, data teams, AI practitioners, security, legal and compliance, business domain
  experts, and end users. End users are defined to include *"colleagues who use AI solutions to support
  their role"* and *"external stakeholders who use AI products to access goods or services."*
- **Nine risk categories:** financial; legal and regulatory compliance; appropriate transparency and
  explainability; fairness; accountability and governance; contestability and redress; technical
  robustness; security; people and the environment.
- **Scoring:** likelihood x impact, each 1 to 5, product is the risk score, optional weighting.
  Likelihood bands: 1 Rare <5%, 2 Unlikely 5-20%, 3 Possible 20-50%, 4 Likely 50-80%, 5 Almost Certain
  >80%. Likelihood methods: historical data, model analysis (accuracy, precision, recall, BERTscore),
  expert judgement, Alpha/Beta experimentation.
- **Appetite (Appendix 2):** five levels, Averse, Minimal, Cautious, Open, Eager, across nine rows.
  Security rows name *"data poisoning and leakage, perturbation attacks, prompt injection threats."*
  Technical robustness at "Eager": *"Agile delivery is embraced over secure by design principles."*
- **Impact (Appendix 3):** quantifiable vs non-quantifiable across Business, Staff, Service
  User/Citizen, Reputation. Scoring bands, e.g. financial loss <GBP 10,000 negligible, GBP 10k-50k minor,
  50k-200k moderate, 200k-1m major, >GBP 1m catastrophic; downtime <1h to >24h. Staff "quantifiable"
  impacts include *"Job displacement, with the reduction in workforce in departments where AI is
  implemented, by percentage"* and *"Job transformation, with the number of tasks automated within a
  specific job role"*, but the scoring table's staff column bands only turnover, absenteeism, training
  cost, morale, job satisfaction and culture. **Displacement is named as measurable and given no band.**
- **Treatment (Appendix 4):** four categories, avoidance, limitation (the text's "limiting"),
  transference, acceptance. Rows that matter for this pipeline, verbatim:
  - Poor accuracy or performance: *"Make end users clearly aware of the limitations of the system, that
    they use the outputs at their own risk, and are responsible for verifying the outputs."*
    Category: **Transference**.
  - Hallucinations and misinformation: *"Establish policies and procedures that AI generated content
    should be checked for accuracy by end users."* Category: **Transference**.
  - Poor accuracy or performance: *"Establish incident response procedures for when the AI solution
    performs beyond acceptable limits. Put alerts in place for when performance indicators observed in
    production differ from pre-deployment test outcomes"*. Category: Avoidance.
  - *"Establish and regularly review procedures to bypass or deactivate the AI solution"*. Avoidance.
  - Red-teaming *"by external experts independent from the AI project team"*. Limitation.
  - Explainability: *"Establish mechanisms that facilitate the auditability of the AI solution,
    including development process traceability, sources of training data, logging of the AI solution's
    processes, outcomes, and impacts"*. Limitation.
  - Failure of third party elements: *"Establish processes for third party suppliers to report known or
    potential issues and vulnerabilities in supplied resources"* (Limitation) and *"Ensure contracts and
    licences have robust warranty and indemnity provisions"* (Avoidance, Transference).
- **No definition of an AI incident anywhere.** The word "malfunction" does not appear. The word
  "notify" does not appear. The accountability questions ask only *"Is there an incident response
  plan?"*

### Document hygiene, for anyone quoting it

- **Framework-to-toolkit rename residue (VERIFIED that the strings are there; the cause is INFERRED).**
  *"Cyber Assessment toolkit (CAF)"*, linked to a URL reading `introduction-to-the-cyber-assessment-framework-caf`;
  *"Central AI Risk Toolkit Team (CAIRF)"*; *"the Risk Management toolkit (RMF) found in the Orange
  book"*; *"legal toolkits"* for legal frameworks; and the workbook is still titled *"AI Risk Management
  Framework: workbook"*. Reads as a global find-and-replace of "framework" with "toolkit." Cite it by its
  published name, "AI Risk Management Toolkit", and do not repeat the CAF or Orange Book misnaming.
- **Appendix 1 headings are offset from their questions.** Legal questions sit under "Financial",
  transparency questions under "Legal and regulatory compliance", fairness under "Transparency", and so
  on down the list. Quote a question by its content, not by its heading.

## Lars's note

"this probably needs to be added to our information corpus, if you can get it into the vault?"

## Match (step 2c)

- **Week plans.** `week-plan_2026-09-07.md`: nothing on UK AI governance or this toolkit.
  `week-plan_2026-09-14.md`: the nearest is **Fri 18 "What Your Contract Calls It"** and
  `research_incident-label_2026-09-10.md`. The toolkit **corroborates, does not contradict**: it gives
  departments a behaviour-based internal trigger ("performs beyond acceptable limits") but asks of
  suppliers only "processes... to report known or potential issues" and "robust warranty and indemnity
  provisions", with no definition, no clock and no use of "malfunction". The note's line that
  "malfunction" appears in exactly two places in everything read still holds. The toolkit's
  transference rows are the buyer-side mirror of the vendor output disclaimers in §1 of that note (OpenAI
  SA §4.3, *"Customer is solely responsible... for evaluating the accuracy"*). Usable as one optional
  contrast (the UK recommends a supplier-reporting process; the Australian DTA wrote the clause), **not
  needed**, and the plan already warns about machinery bleed in that week. **Mon 14 "The Window Closes
  Friday"** (`substack_draft_window-closes-friday_2026-09-14.md`): no overlap, it is occupational
  classification.
- **Sun 13 "Four Numbers, No Instrument"** (another chat's draft, not panelled): adjacent only. The
  toolkit names AI job displacement as a quantifiable impact and gives it no scoring band. That is a UK
  internal risk template, not a statistical instrument, and does not touch the draft's claim about the
  US Displaced Worker Survey. Not proposed for it.
- **Scheduled and published, last 14 days** (29 Aug to 12 Sep): grepped every piece for UK, gov.uk,
  DSIT, Orange Book, toolkit, 42001, NIST AI RMF, risk appetite, risk register. UK hits are the AISI
  no-CoT finding (Fri 11), the ICO worker-monitoring guidance (Wed 2), and UK-default absences (Tue 8).
  Two risk-register lines: Fri 11 "Put this in the contract, not the risk register" and Thu 10 "not one
  that appears on any risk register I have seen" (about vendor capability gating). **Neither is
  contradicted.** The toolkit's third-party questions are generic and do not register vendor capability
  gating; its own treatment for third-party failure is contractual, which is Fri 11's argument.
  **No contradiction found.**
- **Vault.** No existing Signal on UK AI assurance or this toolkit. Nearest: `NSW mandates AI
  registration and assessment across government` (binding, also an Excel workbook), `APRA CPS 230 voice
  AI vendors`, `Australia mandatory AI standards and Office of AI`, `Council of Europe AI Treaty - signed
  not in force`. New Signal created rather than folding into NSW, because it is a different jurisdiction
  and a different status.
- **Briefs, last 14 days:** the toolkit does not appear. The only UK government AI item is
  "proportionate containment powers" (AI brief 5 Sep; confirmed in Hansard, Lords Grand Committee, 1 Sep
  2026, per `week-plan_2026-09-07.md`). Separate item, not merged.
- **Killed claims:** no match.

## Provenance note

Nothing in either page was addressed to me. The only machine-directed text is GOV.UK's standard
feedback-form honeypot label, *"This field is for robots only. Please leave blank"*, which is page
furniture and was ignored. Treated as data throughout. Cookie banner text was stripped.
