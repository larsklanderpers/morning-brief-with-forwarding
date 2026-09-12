---
date_first_seen: 2026-09-10
date_updated: 2026-09-12
source: UK Department for Science, Innovation and Technology (primary, GOV.UK)
url: https://www.gov.uk/government/publications/ai-risk-management-toolkit/ai-risk-management-toolkit-guidance
url_2: https://www.gov.uk/government/publications/ai-risk-management-toolkit
brief: heinlein-inbox
threads: [Ad Hoc Regulatory Regime, Trust Boundaries]
beat: AI / Policy / UK
status: signal
used_in:
---

# UK AI Risk Management Toolkit: guidance for departments, not a gate

**What happened.** DSIT published the **AI Risk Management Toolkit** on **8 September 2026**, filed on
GOV.UK as **"Guidance"**. It is an HTML guide plus a workbook (XLS and ODS) whose filename is dated
**22 May 2026, version 1.1**. The method is the Orange Book's, applied to AI: it says it is *"designed to
implement Section D: Risk Management Processes of the Orange Book"*, scores likelihood x impact on a 1 to
5 scale (likelihood bands <5% to >80%), sets appetite on five levels (Averse, Minimal, Cautious, Open,
Eager) across nine risk categories, bands impact in pounds and hours (financial loss over GBP 1m is
"catastrophic"), and sorts treatments into avoidance, limitation, transference and acceptance. Security
questions cross-walk to the NCSC **Cyber Assessment Framework** section by section. It points to the
**AI Playbook for the UK Government**, NCSC's ML security principles, the Algorithmic Transparency
Recording Standard, and ICO and EHRC guidance.

**Status, exactly.** Written for UK government departments and the public sector (*"created to assist
departments"*; appetite *"signed off at the departmental board level"*), although the landing page says
"anyone involved in AI projects." **No statement that anyone must use it**, no mandate cited for it, and it
calls itself *"a starting point."* The one ask of departments is that GDS *"encourages"* them to keep a
central log of AI risks and share it with GDS and DSIT's central team. Nothing addresses the private
sector. It is not "voluntary" in its own words either: it simply states no requirement. Write it as
guidance with no stated requirement, and nothing stronger.

**Why it matters.** The UK has joined this thread's pattern from the soft end. See the observations.

## Observations

- **2026-09-10** - Lars sent it to #heinlein-inbox: *"this probably needs to be added to our information
  corpus."* Filed 2026-09-12 from the primary, both pages read in full (intake note:
  `Research Notes/intake/intake_2026-09-12_uk-ai-risk-toolkit.md`).

- **2026-09-12 - Same instrument as NSW, opposite status.**
  [[NSW mandates AI registration and assessment across government]] also ships its assessment as an
  **Excel workbook**, but behind a binding circular, a
  register, a review committee and a dated attestation. The UK ships a workbook behind the word
  "encourages." Two governments reached for the same spreadsheet: one made it a gate, the other a
  suggestion. Add [[APRA CPS 230 voice AI vendors]] and there are three registers with three scoping
  choices and three levels of bite. Do not write it as like-for-like: NSW is a state policy, the UK is
  central-government guidance, APRA is a prudential standard. Argue the status gap, not the content.

- **2026-09-12 - The human checker is booked as a transfer, not a control.** Two treatment rows,
  verbatim. Poor accuracy: *"Make end users clearly aware of the limitations of the system, that they use
  the outputs at their own risk, and are responsible for verifying the outputs."* Hallucinations:
  *"AI generated content should be checked for accuracy by end users."* **Both are categorised
  Transference.** In the government's own method, end-user verification is where risk is *sent*, not where
  it is stopped. The toolkit defines end users to include external people *"who use AI products to access
  goods or services"*, though neither row says which end users it means. This is the same move vendors
  make in contract (see `References/research_incident-label_2026-09-10.md` §1: output accuracy is the
  customer's problem). So risk goes down the chain twice, vendor to department by contract and department
  to user by treatment, and in this vocabulary each step counts as managing it. That is this thread's
  argument in a regulator-adjacent document, and it is the strongest line in the toolkit.

- **2026-09-12 - It defines trouble by behaviour internally, and asks nothing specific of suppliers.**
  Internally: incident procedures for when the system *"performs beyond acceptable limits"*, alerts when
  production metrics drift from pre-deployment tests, bypass or deactivate procedures. For suppliers:
  only *"processes for third party suppliers to report known or potential issues"* and *"robust warranty
  and indemnity provisions."* No incident definition, no clock, no clause text, and "malfunction" and
  "notify" do not appear anywhere. The Australian DTA AI Model Clauses wrote the supplier sentence (clause
  2.4.1(g), per the research note, primary copy still to be confirmed at buyict.gov.au). **The UK
  recommends having the process; Australia wrote the clause.** Optional contrast for Fri 18 "What Your
  Contract Calls It". It corroborates that piece and does not break it.

- **2026-09-12 - What it does NOT map to.** **ISO/IEC 42001 and NIST AI RMF are not named anywhere in
  the text** (complete fetch, through Appendix 4 to the page footer). Standards appear only generically
  (ISO, IEC, IEEE SA, via the AI Standards Hub). The **EU AI Act** appears only as an example of
  "applicable AI Laws" and as an export concern (*"continue to export to our trading partners"*).
  Anyone writing that the UK toolkit "aligns with ISO 42001" or "operationalises NIST" is supplying it
  from somewhere else.

- **2026-09-12 - Two quotable oddities.** The "Eager" appetite for technical robustness reads *"Agile
  delivery is embraced over secure by design principles"*: a government appetite scale that names
  trading off secure by design as a legitimate setting. And staff impacts list *"Job displacement... by
  percentage"* as quantifiable, then give it no band in the scoring table. Named as measurable, never
  scored.

- **2026-09-12 - Quote hygiene.** The document looks like "framework" was globally replaced with
  "toolkit" (VERIFIED strings; the cause is INFERRED): *"Cyber Assessment toolkit (CAF)"*, *"Central AI
  Risk Toolkit Team (CAIRF)"*, *"Risk Management toolkit (RMF) found in the Orange book"*, *"legal
  toolkits"*, while the workbook is still titled *"AI Risk Management Framework"*. Cite it by its
  published name, and do not repeat the CAF or Orange Book misnaming. Appendix 1's category headings are
  offset one step from their questions, so quote a question by its content, not its heading.

## Feeds

- [[Ad Hoc Regulatory Regime]] - UK central government's AI risk machinery is guidance with no stated
  requirement; the soft pole against NSW's binding register
- [[Trust Boundaries]] - end-user verification classified as Transference: the checker is where risk is
  sent
- Related: [[NSW mandates AI registration and assessment across government]],
  [[APRA CPS 230 voice AI vendors]], [[You cannot rent an audit trail]] (the toolkit's auditability row
  asks for logging of the system's processes, outcomes and impacts, but does not say who holds the log)

## Open

- **The workbook is unread.** It is where the scoring logic, weighting and the "AI Risk Monitoring
  Dashboard" presumably live (the dashboard is not a separate file). Download needs Lars's OK.
- **Is it required by something else?** These two pages state no requirement. Whether a Cabinet Office,
  GDS or spend-control instrument makes departments use it was **not searched**. Until it is, write
  "guidance, no stated requirement", never "voluntary by policy" and never "mandatory."
- **Watch the CAIRF team.** DSIT says it is preparing *"common scenarios and risks"* and causal mapping.
  Any published output would be the first sign of the central log being used.
- **The page's `updated-at` moved on 10 Sep with no public change note.** Re-check the page history
  before quoting anything that might have been edited.
