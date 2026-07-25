# AI LinkedIn Post — 19 July 2026
**Status:** Draft (review before posting)

---

Three regulatory deadlines. Five months. The same architectural answer.

APRA CPS 230 went live on July 1. The EU AI Act applies in full on August 2 — two weeks from today. Australia's Privacy Act automated-decision disclosure requirements hit December 10.

Three separate regimes. Three enforcement bodies. One common thread: if your AI processes customer PII and the inference happens offshore, you have a problem you cannot policy-document your way out of.

Here's what most organisations are still getting wrong.

They treat data residency as a storage question. They ensure the database is onshore. They get the cloud hosting right. Then they route the actual AI inference — the step where the model reads customer data, reasons about it, and generates a response — through a US-based API endpoint, and call it compliant.

It isn't. CPS 230 is explicit: the model inference layer is in scope for material service provider obligations. The OAIC's December deadline covers decisions made "by computer programs" using personal information. The EU AI Act's human oversight requirements apply at the point of AI-generated output, not just data storage.

This week, the open-weight model world made that architectural fix considerably easier.

Kimi K3 — a 2.8 trillion parameter model from Moonshot AI, currently #1 on frontend coding benchmarks, with a 1 million token context window — releases its full open-source weights on July 27. Self-hostable. Completely under your infrastructure control. GLM-5.2 (MIT licence, also #1 on SWE-Bench Pro) is available now. Mistral Large and Small just moved to Apache 2.0 — backed by French and German government framework agreements through 2030 and a €11.7 billion valuation.

The capability gap between cloud AI and local AI has closed. What hasn't closed is the compliance gap — and it's getting wider, not narrower.

That's the decision facing every CIO, CISO, and Chief Privacy Officer in a regulated Australian or European business right now. Not "is AI ready?" It is. Not "can we afford it?" You can't afford not to. The question is: which local, under whose governance norms, auditable by whom?

Australia's PM announced national AI standards last week and an Office of AI within his own department. China launched WAICO — a 29-nation AI governance bloc positioned explicitly as a rival to the US framework — the same week Kimi K3 went live. The geopolitics of AI infrastructure and the compliance obligations of regulated businesses are no longer separate conversations.

The organisations that will navigate this well are the ones that answer the sovereignty question before the regulator does.

#DataSovereignty #AIGovernance #PrivacyByDesign #LocalAI #AustralianPrivacyAct #GDPR #APRA #RegulatedIndustries #AICompliance
