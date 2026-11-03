# AI LinkedIn Post — 17 August 2026
**Status:** Draft (review before posting)

---

Your AI vendor says the data stays in Australia.

Here's what that claim is actually worth.

The Australia-US CLOUD Act Agreement came into force on January 31, 2026. Under it, US law enforcement can compel any US-headquartered cloud provider to produce data stored in Australian data centres — without going through Australian courts, and without necessarily notifying you.

If your AI vendor is headquartered in the US, your data is subject to US jurisdiction. Where the server sits is a different question from who can reach the data.

And there's a second problem most organisations haven't discovered yet.

Many AI vendors claim "Australian hosting" but route inference — the step where your data is actually processed by the model — through Singapore or US regions during peak loads. Your data might be stored in Sydney and processed in Virginia. The privacy policy covers storage, not inference.

For APRA-regulated entities, CPS 230 (effective since July 2025) now extends operational risk obligations to material AI service providers. That means the inference routing question isn't just a privacy hygiene issue — it's a regulatory compliance question with a named obligation behind it.

So what does the compliance-safe path actually look like?

Three options have real answers. Everything else is wishful thinking.

**Option 1: Local/on-premise deployment.** Models like Meta's Muse Glimmer (Apache 2.0, runs on a single 24GB GPU, released this week) or OpenAI's newly released open-weight models (gpt-oss-20b, gpt-oss-120b) change the economics of on-premise AI meaningfully. Inference never leaves your infrastructure. Ollama 0.32.6 now speaks the OpenAI API wire format natively — existing integrations point to a local endpoint with a one-line config change.

**Option 2: EU-style regional control with contractual SLA.** Mistral announced this week that its regional endpoints — where you contractually lock inference to a specific geography — are now generally available, with an uptime SLA and opening to third-party open models. This is structural, not just a default setting. Mistral is EU-headquartered, which means the CLOUD Act doesn't reach it the same way it reaches US providers. (Read the DPA carefully — "limited sub-processor transfers" still apply.)

**Option 3: Verify the inference routing claim explicitly.** Ask your current vendor: does inference ever leave the declared region under load? What's the contractual commitment, not just the default? Get the answer in writing before the December 10 Privacy Act deadline.

That deadline matters because from December 10, 2026, Australian Privacy Act amendments require organisations to disclose in their privacy policies what AI they're using for automated decisions and how it works. Penalties up to AUD $50 million. The OAIC has said it expects good-faith progress before the deadline — not a completed project, but evidence you're taking it seriously.

Four months.

The question isn't whether your organisation will use AI. You already are. The question is whether the infrastructure underneath it survives a regulator asking "who can access this data and under what law."

Data residency is where the data sits.
Data sovereignty is who controls the stack.

Only one of those protects your customers.

---

#DataSovereignty #AICompliance #AustralianPrivacyAct #LocalAI #PrivacyByDesign #GDPR #AIGovernance #RegulatedIndustries
