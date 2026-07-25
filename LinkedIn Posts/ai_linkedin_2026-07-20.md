# AI LinkedIn Post — 20 July 2026
**Status:** Draft (review before posting)

---

Your cloud AI vendor has a data centre in Virginia.

Your database is in Sydney.

Congratulations — you've solved the wrong problem.

Here's what actually happened in Australian AI compliance this month, and why the "where is the data?" question has been replaced by a harder one: where does the model *think*?

---

APRA CPS 230 took effect July 1. Voice AI vendors are now classified as material service providers for banks, insurers, and super funds. That means full third-party risk management — vendor assessments, concentration risk analysis, contractual data controls.

But read the guidance carefully. What CPS 230 actually requires isn't just data residency. It's *inference* residency. The moment your AI vendor runs a query on customer data — even if the data itself sits onshore — that inference is happening somewhere. And in most cloud AI architectures, that somewhere is an American data centre under American jurisdiction.

That distinction is now regulatory, not theoretical.

---

Thirteen days from now, the EU AI Act becomes fully applicable. High-risk AI in financial services — credit assessment, insurance underwriting, customer-facing decisions — must maintain activity logs, demonstrate human oversight, and pass conformity assessments. Penalties reach €35 million or 7% of global turnover. That's higher than GDPR.

And on December 10, Australia's own automated decision-making disclosure obligations come into force under the amended Privacy Act. APP entities will need to disclose what personal information feeds their AI decisions and give individuals the ability to contest outcomes.

Three frameworks. Three deadlines. Stacking up over the next five months.

---

The good news is that the capability gap that used to justify cloud AI despite these risks has closed faster than anyone predicted.

Kimi K3 — an open-weight model whose weights release publicly on July 27 — benchmarks at Claude Opus 4.8 level intelligence. It runs on your own infrastructure. The data doesn't leave your building. The inference doesn't cross a border.

GLM-5.2, the current open-weight leader, runs similarly. Microsoft Presidio handles PII detection and anonymisation at the ingestion layer. The tooling is there.

The question is no longer whether local models are good enough. It's whether your compliance team has communicated that to your procurement team — and whether your procurement team has moved yet.

---

There is a window here. Open-weight frontier models are available now, ahead of the December 10 compliance deadline, ahead of the OAIC's formal guidance expected in September, and ahead of whatever mandatory Australian AI Standards look like once the new Office of AI codifies them.

Organisations that act before September — mapping their AI-assisted decisions, identifying where inference is happening, and deploying local models for sensitive workloads — will be ready to implement guidance the day it arrives.

Organisations that wait for guidance to act will be behind before the starting gun fires.

---

The frame I'd offer to any decision-maker in a regulated business:

The cloud AI vendors are not your partners in this compliance exercise. They're your counterparties. Their business model depends on keeping your inference offshore. Your compliance obligation runs the other way.

Understanding that tension — and building AI architecture that resolves it on your terms, not theirs — is the governance decision of 2026.

---

#DataSovereignty #AICompliance #AustralianPrivacyAct #LocalAI #GDPR #APRA #PrivacyByDesign #ResponsibleAI
