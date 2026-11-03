# Research Note -- Sun 11 capstone (DELEGATED AUTHORITY merge)
For: Sun 11 Oct capstone (untitled) · Depth: deep · Date: 2026-10-09 · Plan: week-plan_2026-10-05.md

## Bottom line
The human side is solid. Scope, provisioning and incentive are each written down for people, at primaries: Restatement (Third) of Agency, COSO P3, ASX Rec 1.1, the UK Code, NIST AC-2/AC-6/PS-3, and FINRA 2111 / Reg BI.
**The plan's thesis "agents are handed all three with none written down" does NOT survive as worded.**
- Scope and provisioning terms for agents now exist in standards and government text: NIST AC-6 ("processes acting on behalf of users"), Five Eyes May 2026, Singapore IMDA Jan 2026, OWASP Dec 2025.
- What survives is narrower and better. Those terms are written as ACCESS CONTROLS by the security team, not as a DELEGATION by the manager whose work the agent does. The accountable-human field is optional (Entra "can have a sponsor"). NIST's NCCoE was still listing "delegation of authority for 'on behalf of' scenarios" as an open question in Feb 2026.
- The incentive term turns up nowhere on the agent side. Reg BI's incentive rule is written about a "natural person". This is an absence from a search, not proof.
- Proposed thesis for his ruling: **for a person, the three terms sit on one page signed by the manager. For an agent, scope sits in a security control, onboarding sits in an optional field, and the pay term sits on the seller's price sheet. Nobody holds all three, and the manager holds none of them.**

## What's solid
**Human precedents**
- Restatement (Third) of Agency §1.01, §2.01 (actual authority), §2.03 (apparent authority) and §8.01 (loyalty), verbatim via the opencasebook Pollard excerpts (a secondary reproduction; the ALI text is paywalled).
  - §2.01: "An agent acts with actual authority when ... the agent reasonably believes, in accordance with the principal's manifestations to the agent, that the principal wishes the agent so to act."
  - §2.03: apparent authority arises when "a third party reasonably believes the actor has authority ... and that belief is traceable to the principal's manifestations."
  - https://opencasebook.org/casebooks/16481-selected-excerpts-of-restatement-of-agency-third-professor-randle-pollard/as-printable-html/
- Restatement §1.04 cmt e, as quoted in Kolt, *Governing AI Agents* (arXiv 2501.07913, n.26): "a computer program is not capable of acting as a principal or an agent as defined by the common law. At present, computer programs are instrumentalities of the persons who use them." Attribute it as "as quoted by"; the ALI original was not reached.
- COSO 2013 Principle 3: "Management establishes, with board oversight, structures, reporting lines, and appropriate authorities and responsibilities in the pursuit of objectives."
- ASX CGC Principles, 4th ed., Rec 1.1: a board charter setting out "those matters expressly reserved to the board and those delegated to management."
- UK Corporate Governance Code 2024: responsibilities "should be clear, set out in writing, agreed by the board and made publicly available." Provision number unconfirmed; say "the Code requires".
- NIST SP 800-53 Rev 5:
  - AC-6: least privilege for "users (or processes acting on behalf of users)".
  - AC-2: approvals to create accounts; "Align account management processes with personnel termination and transfer processes."
  - PS-3: "Screen individuals prior to authorizing access."
- FINRA 2111.05(c), quantitative suitability (turnover rate, cost-equity ratio, in-and-out trading). It no longer applies to retail recommendations since Reg BI (June 2020).
- Reg BI, 17 CFR 240.15l-1(a)(2)(iii):
  - (B) mitigate conflicts that "create an incentive for a natural person ... to place the interest of the broker ... ahead of the interest of the retail customer";
  - (D) "identify and eliminate any sales contests, sales quotas, bonuses, and non-cash compensation" tied to specific securities in a limited period.
  - https://www.ecfr.gov/current/title-17/section-240.15l-1

**Agent side**
- OWASP LLM06:2025 Excessive Agency: root causes are "excessive functionality; excessive permissions; excessive autonomy". Its example: "a generic high-privileged identity". https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
- OWASP Top 10 for Agentic Applications 2026 (10 Dec 2025) names Tool Misuse and Identity and Privilege Abuse. Do not print the ASI item numbers.
- Five Eyes, *Careful Adoption of Agentic AI Services* (1 May 2026): CISA, NSA, ASD ACSC, NCSC-UK, the Canadian Cyber Centre and NCSC-NZ.
  - "construct each agent as a distinct principal, a cryptographically anchored identity"
  - "Limit privileges of AI agents to the minimum required for its task."
  - https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services
- Singapore IMDA Model AI Governance Framework for Agentic AI (22 Jan 2026):
  - "humans are ultimately accountable"
  - "placing limits on agents' powers such as agents' autonomy and access to tools and data"
  - "defining significant checkpoints at which human approval is required"
  - https://www.mddi.gov.sg/newsroom/singapore-launches-new-model-ai-governance-framework-for-agentic-ai--/
- NIST NCCoE concept paper, *Accelerating the Adoption of Software and AI Agent Identity and Authorization* (5 Feb 2026). Its open questions include:
  - "How do we handle delegation of authority for 'on behalf of' scenarios?"
  - "How do we establish 'least privilege' for an agent, especially when its required actions might not be fully predictable when deployed?"
- Microsoft Entra Agent ID: "Agent identities can have a sponsor, which records the human user or group that's accountable for an agent." "Can", not "must". This is vendor documentation; Microsoft sells it. https://learn.microsoft.com/en-us/entra/agent-id/agent-identities
- Packt *Agent Safety Playbook, Part 1*, Thomas De Vos (HCLTech), modified 8 Oct 2026:
  - "If the default is 'no, unless explicitly allowed', capability is bounded by the explicit grants."
  - Three tool tiers (read-only / internal write / external write). He calls them "a working classification, not an industry standard".
  - "Reads can disclose sensitive information even though they change nothing."
  - Interest: the post promotes his Packt book; HCLTech sells consulting.

## Contested / watch out
- **Moffatt v. Air Canada, 2024 BCCRT 149**, para 27: "Air Canada suggests the chatbot is a separate legal entity that is responsible for its own actions. This is a remarkable submission." Award $812.02 CAD.
  - It is a small-claims tribunal ruling in NEGLIGENT MISREPRESENTATION, not an agency holding.
  - Primary UNREACHED (CanLII robots; CRT 403). Quoted via McCarthy Tetrault.
- **Bengio**, *Transformer* open letter, 8 Oct 2026: "If you truly prioritize safety, it is time for you to leave frontier AI companies."
  - Interest: he recruits to LawZero.
  - The UNSC briefing is SOLID: 10228th meeting, 23 Sep 2026, with Altman and Amodei; press.un.org/en/sc/16462.doc.htm.
  - His "first time the Council convened" line is CONTESTED: the Council held AI meetings in Jul 2023 and Dec 2024.
- **Restatement §8.09(1)** (act only within actual authority): the wording comes from search snippets only.
- **IETF draft-oauth-ai-agents-on-behalf-of-user-02** (WSO2): an individual draft, expired 27 Feb 2026. It is not a standard, and WSO2 sells identity software.

## Couldn't verify
- **@bruno_apps "44 AI employees"** (X, ~4 Oct): profile reachable (42 followers, sells a product); the post itself UNREACHED. Do not use.
- **Agent-side incentive rules:** none found anywhere (regulator, standard or vendor). Print it as "I could not find", never "none exist".

## The economics
- Fri 9 already carried the money: per-action meters, Robinhood's $776M of $1.31B, Agentforce, Intercom, CodeRabbit, OpenAI tiers. Sunday should not re-reveal any of it. Cite in a clause at most.
- The cost angle Sunday can own: the person delegating pays for terms nobody signed.
  - The Five Eyes, IMDA and NIST controls cost the SECURITY budget.
  - The incentive term costs the BUSINESS budget, set by the seller's meter.
  - The manager who wanted the work done holds neither line. That split is the economic shape of the gap.

## Drop-in facts
1. NIST's least-privilege control already reaches "processes acting on behalf of users." (SP 800-53 Rev 5, AC-6)
2. Six agencies from the US, UK, Australia, Canada and New Zealand said in May 2026 to "construct each agent as a distinct principal" and limit its privileges "to the minimum required for its task."
3. In Feb 2026 NIST's NCCoE was still asking "How do we handle delegation of authority for 'on behalf of' scenarios?"
4. Microsoft's agent identity "can have a sponsor" -- the accountable human is optional.
5. The ASX asks listed companies to write down "those matters expressly reserved to the board and those delegated to management."
6. Reg BI's incentive rule is written about a "natural person".
7. As quoted by Kolt, the Restatement's own commentary: "At present, computer programs are instrumentalities of the persons who use them."
8. Air Canada argued its chatbot was "a separate legal entity"; the tribunal called that "a remarkable submission."

## Corpus collision read (Published + this week's Scheduled)
- **The three-terms synthesis is UNSPENT.** The risks are images, form and two printed lines.
- **MED, 21 Jul *Accept, Refuse, Delegate*:**
  - delegation as "pre-decided the damage is small"
  - "Write the bucket down, and name who owns the no"
  - "they were always the same document"
  - the globe/atlas close
- **MED, 22 Jul *29 Minutes*:** "An AI agent gets provisioned like a piece of software -- quietly, by a team lead, with a checkbox -- but it behaves like an employee ... minus every accountability structure we wrap around an actual hire." That is Sunday's onboarding term in one sentence. Quote it as a declared callback, or go past it.
- **MED, 1 Sep *Score the Catch*:** the DeepMind triad "authority, responsibility, accountability" is already printed. Sunday's triad (scope / provisioning / pay) must not echo that phrasing.
- **LOW-MED, 14 Aug *The Seat Got Filled*:** the locum, standing orders, the bookkeeper wire limit, "write four lines".
- **Sun 27 *Sold As Is*, HIGH on FORM:**
  - the "Four pieces this week ended with..." opener
  - the bold per-day roll-call
  - the film-quote header
- **Sun 4:** Knight Capital, recall math, Mollick "Dot and the Swarm". If Mollick's line is used, it is a live counter and must be declared as a callback.
- **Spine handoffs, verbatim. Sunday must pay off both promises:**
  - Wed 7: "That is the first term of any delegation, and on Sunday I will argue it is one of three."
  - Thu 8: "It is what you would do for anyone who was about to get a building pass and a login to everything, and on Sunday I will come back to why that is exactly the point."
  - Fri 9 recapped the arc in its opener, and its close is near Sunday's thesis: "Agents are being handed authority faster than that has been written down." Reuse only as a declared callback.
- **Earlier uses of "new hire":** 25 Aug (production database on the first morning), 4 Aug, 18 Aug.
- **"Temp agency" analogy** spent: 18 Sep.

## DO NOT PRINT (binds every revision unless he rules otherwise; record rulings here)
- "None written down" or "nobody is writing these" as an absolute. It is contradicted by AC-6, Five Eyes, IMDA and OWASP.
- "No rules exist for agent incentives". Say "I could not find".
- Moffatt at all: ALREADY PRINTED 18 Sep (what-your-contract-calls-it, incl. "remarkable submission") -- found by the v1 drafter, missed by the collision read. Callback clause only, if ever.
- Moffatt as an agency-law holding.
- §1.04 cmt e or §8.09(1) as quoted "from the ALI". Attribute them as "as quoted by Kolt", or cut.
- Bengio's "first time the Council convened".
- Anything from @bruno_apps.
- The IETF OBO draft as a "standard".
- De Vos's tiers as an industry standard.
- OWASP ASI item numbers.
- A UK Code provision number, or "ASX 5th edition".
- Re-revealing any Wed 7 / Thu 8 / Fri 9 exhibit beyond a clause.

## Spent for Sunday (images, phrases, form)
- **Images:** bread maker; purchasing card; contractor's badge; building pass (callback only, Thu 8's promise); hostel/hotel; taxi meter; chicken wings; locum and standing orders; sprinkler; four eyes; rubber stamp; used car / As Is; Knight's eighth server; new hire and the prod database; temp agency; globe/atlas; pharmacist; dog training.
- **Phrases:** "write it down" as the close (used 21 Jul, 14 Aug, Wed 7, Fri 9); "costs exactly one name"; "name who owns the no"; "a seat nobody is sitting in"; "authority, responsibility, accountability"; "task vs job"; "limited allowed list"; "whoever counts the action owns the margin".
- **Form:** the capstone roll-call; "What to do tonight" headers; film-quote headers; a numbered question set; an open-question close; the historical-analogy bookend; a forward "on Sunday/next week I will" close.

## Angles this opens (unspent)
- **The written instruments themselves:** power of attorney, the signing-authority / delegation-of-authority matrix, the offer letter. Never printed, and a non-household opener candidate.
- **Apparent authority as Wed 7 seen backwards.** The purchasing card LOOKED authorized, and the law binds the principal to what it let others believe. This is a callback, not a retell.
- **The terms compound.** Pay pulls against scope (a metered, diligent agent goes looking for exits), and onboarding decides whether anyone notices. The weekdays treated each term alone.
- **One page vs three places.** A person's terms sit on one page signed by one manager. An agent's sit in a security control, an optional sponsor field and a vendor price sheet. This is the proposed thesis.
- **[YOUR TAKE]:** a delegation he has written for a person (a DoA matrix, a signing limit, a comp plan) at Tech Results or as a CTO. It is his; never invented.
