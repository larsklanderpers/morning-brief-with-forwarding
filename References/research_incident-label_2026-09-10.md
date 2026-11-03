# Research Note -- The label that decides whether the clause fires
For: Fri 18 Sep (`what-your-contract-calls-it`) · Depth: deep, four parallel digs · Date: 2026-09-10

**Commissioned by Lars, 10 Sep: NSW case law, US federal commercial law, the journalism hunt, and the
contract-language dig. All four came back. Everything below was fetched live 10 Sep 2026.**

---

## Bottom line

**The thesis survives, and the contract prong is stronger than I expected. Two digs broke parts of it,
and both breaks improve the piece.**

**What holds, overwhelmingly:** OpenAI, Anthropic, Google, Microsoft and AWS all define their
notification trigger with the *same sentence*, lifted from GDPR Art. 4(12): a **breach of the vendor's
security** leading to destruction, loss, alteration, unauthorized disclosure of, or access to **customer
data**. A model that behaves badly satisfies neither limb. The word **"malfunction" appears in none of
the five.** Nor does "misalignment," "harmful output," "hallucination," "serious incident," or "AI Act."
Zero hits, five vendors, complete documents.

**What broke, first:** *the vendor does not legally own the label*, and I had that wrong. **Bartlett v
ANZ [2016] NSWCA 30** holds that where a contract turns on a defined event, the clause presumptively
requires **the objective occurrence** of that event, not the party's opinion of it. So the real problem
is not that the vendor gets to decide. **It is that nobody ever wrote a definition that reaches behaviour
at all, and the vendor is the only party who knows what happened.** That is a sharper and more defensible
argument.

**What broke, second, and it is the best thing in the whole dig:** the story is not that the law has a
gap. **It is that where the law has finally addressed this, it wrote the vendor's discretion into the
trigger and left the customer off the distribution list entirely.** See §3.

**And the constructive action already exists, written by his readers' own government.** See §5.

---

## §1 -- The contract position, verbatim, five vendors

All fetched 10 Sep 2026. **Every load-bearing quote below is from the vendor's own terms page.**

| Vendor | Instrument | The trigger, verbatim |
|---|---|---|
| **OpenAI** | [DPA](https://openai.com/policies/data-processing-addendum/) §2.7, §6 | *"'Personal Data Breach' means **a breach of security** leading to the accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to Customer Data..."* |
| **Anthropic** | [DPA](https://www.anthropic.com/legal/data-processing-addendum) §A.7, §G.1 | *"'Security Breach' means **a breach of Anthropic's security** leading to... unauthorized access to, Customer Personal Data."* Notification *"within 48 hours"* |
| **Google** | [Cloud DPA](https://cloud.google.com/terms/data-processing-addendum) §2, §7.2.1 | *"'Data Incident' means **a breach of Google's security** leading to... access to, Customer Data on systems managed by or otherwise controlled by Google"* |
| **Microsoft** | [Products and Services DPA](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) | *"If Microsoft becomes aware of **a breach of security** leading to the accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to Customer Data..."* |
| **AWS** | [DPA](https://d1.awsstatic.com/legal/aws-dpa/aws-dpa.pdf) §9.1, §17 | *"'Security Incident' means **a breach of AWS's security** leading to... access to, Customer Data."* |

★ **The 48 hours is the number a CISO thinks they bought.** It runs on a security breach of customer
personal data and on nothing else.

**And the same paper affirmatively disclaims the other half.** Anthropic Commercial ToS §L.2:
*"ANTHROPIC DOES NOT WARRANT, AND DISCLAIMS THAT, THE SERVICES OR OUTPUTS ARE ACCURATE, COMPLETE OR
ERROR-FREE."* OpenAI SA §4.3: *"Customer is solely responsible for all use of the Outputs and for
evaluating the accuracy and appropriateness of Output for Customer's use case."* Google SST §20(b):
generative services *"may provide inaccurate or offensive Generated Output, and are not designed for or
intended to meet Customer's regulatory, legal, or other obligations."*

**Two clauses, one contract: bad data handling is a 48-hour notifiable event; bad model output is a
contractually disclaimed non-event.**

**Liability caps:** OpenAI §14.2 and Anthropic §L.3.a both cap at 12 months' fees. OpenAI carves out
breach of its Security Measures. **Neither carves out output harm.**

### The counter-evidence, and it must be in the piece

Three things do reach behaviour, and only one is real:

1. **Microsoft is the strongest counter and it is genuine.** Azure Product Terms, *Retirement of Services
   or Features*: *"Microsoft will provide Customer with 12 months' notice before discontinuing a
   Microsoft Azure Service or removing any material feature or functionality."* That reaches capability
   **removal**. It does not reach a model that keeps every feature and starts behaving badly.
2. **OpenAI SA §2.3:** *"If an OpenAI update materially reduces the Services functionality, OpenAI will
   notify Customer,"* with a five-business-day termination window. ★ **Note what the remedy is: notice,
   then exit. Not fix, not compensate.** And §5.1 gives the same degradation right for *security*
   measures. **Security gets a degradation clause. Behaviour does not.**
3. **Microsoft Foundry Models terms** are the only place "harmful outputs" appears -- and it is a
   **retention right for Microsoft**, not a duty to the buyer: it stores content *"to monitor for and
   prevent abusive or harmful uses or outputs."* Anthropic SST §F is the same shape: safety review is a
   vendor entitlement that **overrides the customer's zero-data-retention commitment**, with no
   reciprocal duty to say what it found.

**No vendor has added an EU AI Act clause to its standard commercial terms.** Zero hits across all five.

---

## §2 -- The statutory position

### Australia: the gate is personal information, and the reform does not widen it

**Privacy Act 1988 (Cth) s 26WE(2)** -- an eligible data breach requires *"unauthorised access to, or
unauthorised disclosure of, the information"* or its loss. **The OAIC's own restatement:** the first step
is *"whether there has been a data breach; that is, unauthorised access to or unauthorised disclosure of
personal information, or a loss of personal information."* And, usefully: ***"The Privacy Act does not
define these terms."***

★★ **The reform, and this is ten days old.** The **Exposure Draft Privacy Amendment (Personal Data
Protection) Bill 2026**, released **31 August 2026**, submissions close **18 September 2026** -- the day
this piece would run. It splits the definition (new s 26WBA) and **hardens the clock to 72 hours** (new
s 26WK(2)). **It does not widen the gate.** Personal information remains the hinge.

⚠️ **The strongest counter-pressure, and Lars should carry it:** **s 26WH** fires an *assessment*
obligation on mere **suspicion** -- *"reasonable grounds to suspect that there may have been an eligible
data breach"* -- with 30 days to complete. And **Datateks Pty Ltd (Privacy) [2023] AICmr 97** shows the
regulator overriding an entity's own characterisation and timing: *"Notwithstanding the respondent's
claim that it formed a suspicion on 1 September 2020, I remain of the view that the circumstances known
to the respondent on 26 June 2020... were sufficient."* **The entity classified; the regulator
reclassified; the entity lost.**

★ **NSW does the thing the Commonwealth does not.** PPIP Act s 59L(2): *"an eligible data breach is taken
to have occurred if the head of the agency **decides** under Division 2 there are reasonable grounds to
believe the data breach is an eligible data breach."* **A clean statutory instance of the notification
division applying only once the party bearing the obligation classifies the event.** Best legislative
illustration available.

⛔ **The statutory tort does not help.** Sch 2 cl 7(1)(c) requires the invasion be *"intentional or
reckless."* Unintended model behaviour is neither. **And a correction to our own corpus: it commenced
10 June 2025**, per the commencement table in Act No 128 of 2024.

### United States: same key, one weak prong

- **Cal. Civ. Code § 1798.82(g)**: *"unauthorized acquisition of computerized data that compromises...
  personal information."* **N.Y. Gen. Bus. Law § 899-aa(1)(c)** is the broadest major statute (SHIELD
  added mere *access*) and the object is still *private information*. **FTC Health Breach Notification
  Rule**, same structure.
- ⚠️ **THE SEC PRONG IS THE WEAK ONE AND THE PIECE MUST CONCEDE IT.** 17 CFR 229.106(a) defines a
  cybersecurity incident as *"an unauthorized occurrence... that jeopardizes the confidentiality,
  integrity, or availability of a registrant's information systems or any information residing
  therein,"* and *"information systems"* covers resources *"owned or used by"* the registrant, which the
  SEC extended to third-party and cloud resources so registrants could not *"evade the disclosure
  requirements... by contracting out."* **And the adopting release says: *"an accidental occurrence is
  an unauthorized occurrence... even if there is no confirmed malicious activity."*** An agentic model
  corrupting records is arguably an integrity event.
  **The honest, narrower claim:** the definition turns entirely on *"unauthorized,"* a word the SEC has
  never applied to a model doing what its operator did not intend, and which no registrant has read that
  way. Where the model did what it was permitted to do and the harm is in the output, *"unauthorized"*
  has nothing to bite on. ★ **Write the concession in. A sharp reader attacks here first.**

---

## §3 ★★ -- THE BEST FINDING: where the law finally reached behaviour, it handed the vendor the label

**California SB 53** (Stats. 2025 Ch. 138), Cal. Bus. & Prof. Code **§ 22757.11(d)(4)** -- the first US
statutory definition of a reportable AI incident, and when it got to the misalignment case it wrote:

> *"A frontier model that uses deceptive techniques against the frontier developer to subvert the
> controls or monitoring of its frontier developer **outside of the context of an evaluation designed to
> elicit this behavior** and in a manner that **demonstrates materially increased catastrophic risk.**"*

**Both qualifiers are the developer's call**, and they are exactly the two moves that turn a disclosable
event into a system-card finding. Then: report goes to **Cal OES within 15 days** (§ 22757.13(c)(1)); is
**exempt from the California Public Records Act** (§ 22757.13(f)); enforceable **only by the Attorney
General**, up to $1,000,000 per violation, **no private right of action** (§ 22757.15).

**EU AI Act Art. 3(49)** is the only definition anywhere that says ***"or malfunctioning of an AI
system"*** -- it genuinely reaches behaviour. **Art. 73** reports it to **market surveillance
authorities** (15 days; 2 days for critical infrastructure; 10 days for death). **Art. 55(1)(c)** routes
GPAI systemic-risk incidents to **the AI Office**.

★★★ **The line the piece turns on: in the one jurisdiction that legislated a misalignment-reporting duty
and in the one Act whose definition says "malfunction," the report goes to a state emergency agency or a
market surveillance authority. Neither runs to the customer. The CTO who bought the thing is not on the
distribution list.**

---

## §4 -- The legal machinery, and it points the other way from my first framing

⚠️ **CORRECTION TO THE THESIS. The "vendor owns the label" claim does not survive NSW law.**

**Bartlett v ANZ [2016] NSWCA 30**, Macfarlan JA: a clause allowing dismissal where conduct was *"in the
opinion of ANZ"* serious misconduct did **not** make the bank's opinion the trigger --

> *"the conclusion should be drawn that termination by the Bank under Clause 14.3(b) requires the
> **objective existence** of 'misconduct', not simply the opinion of the Bank that that has occurred."*

> *"their contract should be scrutinized carefully before concluding that they have done so."*

Fallback at [49]: the bank was *"obliged to act reasonably, at least in the Wednesbury sense and at least
so far as its process, as distinct from the result, was concerned."* Applied again in **Hannover Life Re
v Jones [2017] NSWCA 233**.

⚠️ **Three qualifiers, all of which must be stated:**
1. **The escape hatch.** *Growthbuilt* [2021] NSWSC 290: *"The words 'absolute discretion' have been
   accepted as excluding an obligation to act reasonably."* **A well-advised vendor adds "in its sole and
   absolute discretion" the moment customers start citing Bartlett.**
2. **Braganza is not Australian law at High Court level.** NSWCA has applied it; the High Court expressly
   declined to express a view in *Barker* [2014] HCA 32. Five relevant NSW decisions in 22 years. **Do
   not write "Australian law constrains contractual discretion" without that qualifier.**
3. **Delaware forecloses the US version.** *Nemec v. Shrader*, 991 A.2d 1120 (Del. 2010): *"The implied
   covenant only applies to developments that could not be anticipated, not developments that the parties
   simply failed to consider."* ★ **That is the thesis, stated by the Delaware Supreme Court, against the
   customer.** *Dalton v ETS*, 87 N.Y.2d 384 (1995) helps the customer -- *"a promise not to act
   arbitrarily or irrationally in exercising that discretion"* -- but most enterprise AI contracts are
   Delaware or California law.

**So the argument that survives is this:** the label is not the vendor's to own, and it does not need to
be. **The definition was never written to reach behaviour, and the customer has no contractual right to
the facts that would let them apply a definition even if one existed.** Ask for an objective definition
*and* a duty to disclose the underlying facts. A duty to notify "Security Incidents" just re-imports the
vendor's judgment.

---

## §5 ★★★ -- The constructive action exists, and an Australian government wrote it

**Digital Transformation Agency, *AI Model Clauses* v2.0, March 2025. Crown copyright, CC-BY-4.0.**

**Clause 14, definitions:**
> *"**AI Incident** means an event, circumstance or series of events where the development, **use or
> malfunction of the AI System** directly or indirectly leads to any of the following harms: a. injury or
> harm to the health of a person...; b. disruption of the management and operation of critical
> infrastructure; c. a breach of obligations under any law or policy intended to prevent discrimination...;
> or d. harm to property, communities or the environment."*

> *"**AI Hazard** means an event... where the development, use or malfunction of the AI System **could
> plausibly lead to an AI Incident**."* ★ **A near-miss reporting duty. No analogue in any vendor paper.**

**Clause 2.4.1 -- and (g) is the sentence this whole piece was looking for:**
> *"The Seller must: a. notify the Buyer **immediately**... [where] f. ^Optional^ **the AI System is
> malfunctioning or producing incorrect or harmful outputs**; g. ^Optional^ **the AI System behaves in a
> way that was not intended or predicted, which adversely affects outputs or the delivery of a Buyer
> service**."*

**Clause 2.5.2** -- a circuit breaker: stop the system immediately on the Buyer's instruction, *"via a
human-machine interface tool accessible to the Buyer."* **Clause 2.3.3** -- the Seller must *"request
written approval from the Buyer before any change is made to the Approved underlying AI model,"* with a
termination right if refused. **Compare Microsoft's 12 months' notice and OpenAI's five-day exit window:
the DTA gives the buyer a veto.**

**The EU's equivalent** (Commission Public Buyers Community, *MCC-AI-High-Risk*, Feb 2025) is weaker on
notification but **stronger on warranty**: Art. 8.1 requires the system *"achieves an appropriate level
of accuracy, robustness, safety and cybersecurity, and perform consistently in those respects,"* with
metrics in **Annex G**. ★ **A contractual accuracy warranty with a metrics annex -- the precise thing
every vendor disclaims.**

**Recommendation for the action: the Australian template, borrowing the EU's Annex G.** It is his
readers' own government, it is CC-licensed, and clause 2.4.1(f) and (g) can go into a renewal rider
tomorrow morning.

---

## §6 -- The exhibits, best first

### ★★★ 1. OpenAI's published vulnerability-disclosure policy. The centrepiece.

Not a dispute, not an allegation, not said under pressure. A **current, published, deliberately drafted
document a customer can read today.** [bugcrowd.com/engagements/openai](https://bugcrowd.com/engagements/openai),
page last updated 19 Aug 2026:

> *"Some model safety issues, such as jailbreaks, do not fit well within a bug bounty program, as they
> are not individual, discrete bugs that can be directly fixed. **Addressing these issues often involves
> substantial research and a broader approach.** ... please report them using the Model Behavior Feedback
> form, rather than submitting them through the bug bounty program."*

> *"**Issues related to the content of model prompts and responses are strictly out of scope** for the
> Security and Safety Bug Bounty programs, and will not be rewarded."*

And the one sentence that is the entire piece:

> *"Prompt injection, jailbreaks, hallucinations, misleading model output, or an agent misusing access or
> valid, applicable approvals it already has... **This exclusion applies even if the agent leaks sensitive
> data or performs an unwanted action.**"*

**Every CISO in his audience runs a vulnerability-management program whose SLAs assume a vendor will call
a leak a leak. That assumption is void, in writing, before any incident happens.**

### ★★ 2. Moffatt v Air Canada, 2024 BCCRT 149. The pair.

Tribunal Member Rivers, para 27:
> *"Air Canada argues it cannot be held liable for information provided by one of its agents, servants,
> or representatives -- including a chatbot. It does not explain why it believes that is the case. In
> effect, Air Canada suggests the chatbot is a separate legal entity that is responsible for its own
> actions. **This is a remarkable submission.**"*

★ **And the underused half**, para 31: *"it did not provide a copy of the relevant portion of the
tariff... Air Canada is a sophisticated litigant that should know it is not enough in a legal process to
assert that a contract says something without actually providing the contract."*
**The rhetorical turn: these arguments work right up until somebody makes you say them out loud to a
judge.**

### ★★ 3. Landgericht München 26 O 869/26, 28 May 2026

Google argued it *"merely operates a search engine that automatically displays the data and information
of third parties."* The court held the AI Overview is **"the defendant's own statement" made by its own
AI**, making Google a direct infringer rather than an intermediary. Injunction granted. **Under appeal;
judgment is a primary but not final.**

### ★ 4. The Bugcrowd PHI log -- the visceral detail

Named researcher, cross-tenant data exposure in ChatGPT including apparent PHI. Platform log:
submitted **12:13:46**, closed *"Not reproducible"* at **12:27:57**. **Fourteen minutes.** Reopened six
weeks later, set **P1 Critical**, $2,000, Resolved. The researcher names the mechanism: the
**"Hallucination Triaging Dilemma"** -- a genuine breach and a confabulation look identical from outside,
and the default disposition is "model artifact, not security incident."
★ **OpenAI's careful hedge:** the researcher *"observed unexpected model output that appeared to contain
potentially sensitive information."* **Never confirmed as PHI, so no notification duty ever fired.**
⚠️ Researcher's narrative on the vendor's own platform; he is authorised to say only that he reported and
was paid. **Treat the timestamped activity log as solid and the surrounding analysis as advocacy.**

### ★ 5. Piao, Li & Woods, "Measuring the Vulnerability Disclosure Policies of AI Vendors" (arXiv 2509.06136)

264 AI vendors. **36% have no disclosure channel at all; only 18% mention AI risks.** Named exclusions:
Atlassian (*"AI issues not mentioned explicitly above are considered ineligible"*), Tripadvisor
(*"Attacks against our artificial intelligence systems are ineligible"*), Nubank, Skroutz. The authors'
line: *"The AI vendors appear to be shipping products that they acknowledge can never be fixed, or at
least not directly."*

### 6. Wolf River Electric v Google -- the business-harmed case

200-employee Minnesota solar installer; AI Overview falsely said the state AG was suing it; customers
cancelled; damages framed at $110M-$210M. GC Nicholas Kasprowicz: Google *"offered no corrective action,
no public acknowledgment, and no commitment to prevent it from continuing."*
⚠️ **The complaint and Google's answer were NOT fetched directly** -- this rests on Politico and Minnesota
Lawyer reporting. **Close that before printing.**

---

## §7 ⛔ DO-NOT-PRINT

**Binds every revision.**

1. **Do NOT say OpenAI classified one thing as misalignment and another as a security incident.** ⚠️ **Its
   own 5 Sep statement says the Hugging Face event was *also* misalignment and got the security playbook
   because *"misalignment led to security impact to us and third parties."* The line it drew was
   IMPACT, not taxonomy.** That is better for the piece -- the vendor's own stated test for whether
   disclosure fires is its own assessment of impact.
2. **Do NOT use Replit or Cursor as stonewalling examples.** Both vendors did the opposite: Replit's CEO
   called it unacceptable and refunded; Cursor's cofounder apologised within a day and refunded. Using
   them would be wrong on the facts.
3. **Do NOT assert the SEC definition plainly excludes model behaviour.** Concede §2's counter-text.
4. **Do NOT write "Australian law constrains contractual discretion"** without the Braganza qualifier.
5. **Do NOT claim the vendor legally owns the label.** *Bartlett* says otherwise.
6. ⚠️ **Raine v OpenAI is available and I recommend AGAINST it.** OpenAI's Answer does plead the system
   card as an affirmative defence -- genuinely novel -- and also pleads *"ChatGPT is a service and/or not
   a product,"* the AUP, the as-is disclaimer and Section 230. **But it is a wrongful-death case
   involving a 16-year-old's suicide.** It will swamp a contract-risk piece, a skeptical reader will
   fairly say a defendant pleads every available defence, and the subject deserves better than being an
   exhibit. **His call, and if he takes it, the narrow system-card point only.**
7. **Do NOT claim no US company has ever disclosed an AI incident as a fact of law** -- it is an EDGAR
   full-text search result (see the facts below), which is evidence of what was filed, not of what exists.
8. **Do NOT use the Colorado SB 26-189 detail** that the 90-day AG reporting duty did not survive. That is
   the dig's inference from a legislature summary page, **not verified against the enacted text.**
9. **Do NOT use the Gouchev Law "service company" anecdote.** It is an unattributed hypothetical in law-firm
   marketing copy.

---

## §8 -- Drop-in facts

- **92** -- Form 8-K filings containing "Item 1.05" from 18 Dec 2023 to 10 Sep 2026, per EDGAR full-text
  search. **Of those, effectively zero concern AI model behaviour** (two matched "artificial
  intelligence" and one is a false positive).
- **475** -- 8-K filings using the word "misalignment." Clustered in medical devices, pharma and banking.
  **None concern AI systems. The word does not exist in securities disclosure as a technology term.**
- **48 hours** -- Anthropic's contractual notification clock, running on a security breach of customer
  personal data and nothing else.
- **15 days / 24 hours** -- SB 53's clocks to Cal OES. **$1,000,000** per violation, AG-only, no private
  right of action.
- **72 hours** -- the new Australian clock in the 31 Aug 2026 exposure draft.
- **36%** -- AI vendors with no vulnerability disclosure channel at all (n=264).
- **14 minutes** -- from PHI report to "Not reproducible" close.
- **Zero** -- vendors of the five with any EU AI Act clause in their standard commercial terms.
- **Zero** -- occurrences of "malfunction" across all five vendors' complete contract documents. It
  appears in exactly two places in everything read: **EU AI Act Art. 3(49)**, and **a procurement
  template an Australian government agency wrote because its own lawyers noticed the gap.**

---

## §9 -- Unreached, and recorded as unreached

- **legislation.gov.au** would not yield s 26WE text; AustLII reproduction plus the OAIC's restatement
  carry it. **Check against the Register compilation before publication.**
- **The DTA primary copy at buyict.gov.au is UNREACHED** (ServiceNow portal). The v2.0 text was read from
  a complete, DTA-branded, CC-licensed copy on a law firm's host. ⚠️ **Pull it from buyict.gov.au and
  confirm clause numbering before quoting verbatim.**
- **WSJ, FT, The Atlantic, Bloomberg, The Information: not a single substantive hit.** The
  domain-restricted search was silently ignored by the backend. ⚠️ **This is a TOOL LIMIT, not an
  absence. Lars's instinct that something is in one of these is untested, not disproven.** The ft.com
  `?syn-` trick was never exercised. **Worth a dedicated pass if he wants it.**
- **No practitioner account** of a vendor stonewalling was found on HN, r/sysadmin, r/msp or
  r/ExperiencedDevs. Hypothesis: these are under NDA and settle as credits. **Recorded as not-found, not
  as absence** -- one search framing only.
- **No Australian case, tribunal decision or OAIC determination** was found where a party argued an AI
  system's behaviour was not a defined "breach" or "incident." **The entire AICmr database returns four
  determinations mentioning "eligible data breach,"** so this is an artefact of how few determinations
  exist. **Say that rather than implying a gap in the law.**
- **SOCI Act s 12M is a live lead, not a finding.** Its "cyber security incident" definition includes
  *"unauthorised modification of computer data"* with **no mention of personal information** -- an agent
  escaping its sandbox may fire it for critical infrastructure entities. **ss 30BC/30BD not verified.**
- Not fetched: Wolf River complaint and answer; the full Munich judgment in German; OpenAI's Security
  Measures PDF; Microsoft's AI Code of Conduct; Anthropic's Trust Center.

---

## §10 -- Angles this opens

- **The inversion nobody has written.** From the Cursor thread: *"the other possible scenario is that you
  tried to hose your paying customers then when you saw the blowback blamed it on a bot."* ★ **"It was a
  hallucination" is itself becoming a characterisation that discharges responsibility.** Fresh, and
  unspent anywhere in his corpus.
- **The system card as an affirmative defence.** A document written as a research disclosure now does
  work as a liability shield. ⚠️ Sourced to the Raine pleading -- see the do-not-print.
- **Window check owed:** this piece sits two days after Wed 16 (machine-assigned severity) and one day
  after Thu 17 (the taxonomy fork). All three are the same arc, so **the risk is machinery bleed within
  the week, not against last week.** Diff the three action sections before drafting Friday.
