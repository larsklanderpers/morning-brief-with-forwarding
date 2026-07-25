# AI LinkedIn Post — 25 June 2026
**Status:** Draft (review before posting)

---

Yesterday, Anthropic accused Alibaba of running 25,000 fake accounts to extract 28.8 million Claude conversations over six weeks. Not to use Claude — to *steal* it.

The technique is called adversarial distillation. Train a cheaper model on the outputs of a more capable one until it behaves like the original. No R&D costs. No safety research. No alignment work. Just scale.

This should unsettle every business that relies on cloud AI.

If a sophisticated lab couldn't detect this campaign until it had already run for six weeks and generated nearly 30 million exchanges, what confidence can enterprise customers have that their usage — their prompts, their data, their IP — isn't being similarly harvested, analysed, or exfiltrated by other actors running through the same shared APIs?

The Anthropic/Alibaba story is a data integrity story dressed up as a geopolitics story. The question it raises isn't just "who's stealing AI capabilities?" It's "what happens to everything that flows through a public inference endpoint?"

Simultaneously, APRA published a formal letter to every bank, insurer, and superannuation trustee in Australia identifying four AI governance failures that are now live supervisory concerns. One of them was dangerous single-vendor AI dependency. Another was boards that lack the technical literacy to challenge management on AI risks.

These two stories are connected.

The organisations most exposed to both threats — capability theft and regulatory non-compliance — are the ones that handed AI adoption to their engineering teams, said yes to cloud AI productivity tools without governance frameworks, and assumed the vendor's terms of service were sufficient data protection.

They're not.

There is an architecture that addresses both problems simultaneously: local and on-premise model deployment for anything that involves PII, customer data, or confidential business information — with cloud AI reserved for genuinely non-sensitive workloads. This isn't a performance compromise in 2026. This month alone saw MIT-licensed open-weight models at 744 billion parameters (GLM-5.2), frontier-level coding in a fully local model (MiniMax M3), and Ollama expanding hardware support so local inference runs on the infrastructure you already own.

The capability argument for cloud-only AI is gone. The compliance argument never existed.

What remains is inertia, procurement convenience, and the assumption that "our cloud vendor has good security." Meanwhile APRA has formally told Australian financial services boards that AI risk is different from ordinary IT risk — probabilistic, adaptive, harder to audit, and requiring human oversight for high-stakes decisions.

France understood this and committed €2.1 billion to sovereign AI infrastructure. Europe's regulators understood this and built data residency requirements into the AI Act. Australian regulators are now saying the same thing through APRA and the Privacy Act's December 2026 automated decision-making obligations.

The window to get ahead of this is closing. If your business makes decisions using AI — about customers, credit, hiring, pricing, or risk — and you cannot answer these five questions, you have a governance problem:

1. What AI systems do we run, and what data do they touch?
2. Where does inference happen — whose data centre, under whose law?
3. Which decisions are substantially automated, and are they disclosed in our privacy policy?
4. What's our exit strategy if our primary AI vendor becomes unavailable or compromised?
5. Has our board reviewed and challenged our AI risk posture in the last 90 days?

Capability is no longer the differentiator. Governance is.

#AI #DataSovereignty #PrivacyByDesign #LocalAI #GDPR #AustralianPrivacyAct #APRA #AIGovernance
