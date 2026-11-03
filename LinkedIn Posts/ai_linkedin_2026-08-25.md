# AI LinkedIn Post — 25 August 2026
**Status:** Draft (review before posting)

---

The world's best AI model just lost an enterprise deal.

Not because it failed a benchmark. Not because it had a security incident. Because it couldn't promise a bank that the data it processed wouldn't be retained somewhere it couldn't audit.

The Ramp AI Index shows Claude Fable 5 enterprise spending has been flat since June. The reason being cited: no zero data retention offering for regulated customers. The highest-performing general model available, losing deals to a checkbox.

That's the actual state of enterprise AI adoption in 2026.

---

Two other things happened this week that complete the picture.

Meta released Muse Glimmer — a 30-billion-parameter model under Apache 2.0 licence, running on a single 24GB GPU card. No API contract. No data sharing agreement. No US legal process exposure. You pull it down, you run it on your own hardware, your PII never leaves the building.

And Ollama 0.32.6 shipped with full OpenAI API wire-format compatibility — meaning any application already built against OpenAI's SDK can route to a local model with a single environment variable change. The switching cost for "we need to stop sending sensitive data to a cloud API" just became one line of config.

---

For Australian businesses, this isn't abstract.

10 December 2026: Privacy Act amendments take effect requiring transparency for AI systems making automated decisions — in hiring, lending, insurance, customer analytics. The OAIC started compliance sweeps in January. Penalties reach AUD 50 million.

2 August 2026: The EU AI Act's full enforcement provisions went live. Organisations with European customers now face dual enforcement — GDPR (data processing) plus EU AI Act (system transparency) — from the same AI deployment.

APRA's CPS 230 has been in force since July 2025, extending operational risk obligations to material AI service providers. That includes where inference happens, not just where data is stored.

Here's the gap regulators are about to probe: of the major AI platforms operating in Australia, all of them can store data at rest onshore. Most of them process it elsewhere. Storage residency and processing residency are not the same thing — and the difference is exactly where the CLOUD Act exposure lives.

---

The organisations getting this right aren't waiting for enforcement to clarify the rules.

They're building a routing layer now: frontier cloud AI for non-sensitive workloads, local or sovereign-deployment AI for anything that touches customer PII. The capability gap that once justified sending everything to a cloud API — "local models aren't good enough" — closed in 2026. A 30B model on a single GPU card is good enough for most of what regulated businesses actually need AI to do.

The question for every CISO, CRO, and CDO in Australian financial services, health, or government is the same one the AI model market is already answering with its feet:

**If an AI system processed your customers' data today, can you tell me exactly where the inference happened and whose law governed it?**

The organisations that can answer that question won't be scrambling in January.

---

#AI #DataSovereignty #PrivacyByDesign #AustralianPrivacyAct #LocalAI #APRA #AIGovernance #GDPR
