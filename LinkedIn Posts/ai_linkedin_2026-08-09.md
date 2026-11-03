# AI LinkedIn Post — 9 August 2026
**Status:** Draft (review before posting)

---

There is a sentence I keep hearing in risk committees right now: "We have data sovereignty covered — our AI vendor has an Australian data centre."

They do not have it covered.

Here is what that sentence is missing.

An Australian data centre run by a US-owned cloud provider is reachable under the Australia-US CLOUD Act Agreement, which came into force on January 31, 2026. The agreement creates a legal pathway for US law enforcement to compel access to data held by US companies — regardless of which country the server is physically sitting in.

That is one problem.

The second is inference routing. Multiple Australian-focused AI platforms have been documented routing inference through Singapore and US regions during peak load. The application database is onshore. The model compute is not. Every prompt your contact centre agent sends — including any account numbers, health history, or authentication details spoken into it — is processed offshore in that gap.

The third is the CLOUD Act overlay on that offshore compute. You have now stacked two vulnerabilities.

The EU worked this out years ago, which is why Mistral's enterprise product is built around a single provable commitment: EU data residency, no data transfer to third countries, inference included. A major German financial institution deploying it locally reduced compliance approval timelines by 72% in Q1 2026. The savings came from being able to answer the regulator's question cleanly rather than negotiating exceptions to a patchwork of partial commitments.

Australia's December 10 deadline for automated decision-making transparency is four months away. The OAIC has not yet released its final guidance, which means any privacy policy drafted right now is targeting a moving mark. And APRA's CPS 230 (operational risk, effective July 2025) already extends material service provider obligations to AI vendors — which means the inference routing question is not a future problem. It is an audit question today.

The practical answer for most organisations is not to abandon cloud AI entirely. It is to build a tiered architecture: public-facing, low-sensitivity workflows on well-governed cloud deployments; PII-heavy, regulated, or strategically sensitive processing on infrastructure where you can contractually prove where every inference ran.

Open-weight models make that second tier increasingly viable. The best open-weight models are now roughly three months behind frontier proprietary capability. Self-hosted inference reaches cost parity with cloud APIs in three to six months above moderate query volumes. The gap between "capable" and "controllable" is closing fast.

The question for every APRA-regulated entity, every health organisation, every government department evaluating AI right now is not "which model is best." It is "which architecture gives us both capability and an auditable answer to where our data went."

A data centre location is not that answer. An architecture decision is.

#DataSovereignty #AIGovernance #AustralianPrivacyAct #LocalAI #PrivacyByDesign #APRA #GDPR #ResponsibleAI
