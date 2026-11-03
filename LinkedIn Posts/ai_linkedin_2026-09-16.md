# AI LinkedIn Post — 16 September 2026
**Status:** Draft (review before posting)

---

Your AI vendor says they host your data in Australia.

That stopped being enough eight months ago.

On 31 January 2026, the Australia-US CLOUD Act Agreement entered into force. What that means in practice: if your AI vendor is a US-incorporated company — AWS, Azure, GCP, OpenAI, Anthropic — a US law enforcement agency can now compel production of your customers' data through a treaty-backed channel, without going through an Australian court, even if that data never leaves an Australian data centre.

"Australian hosting" and "data sovereignty" are not the same thing. They never were, but now the legal mechanism making them different has a name and a signature on it.

This week, three things converged that I think regulated-industry leaders need to sit with together.

First: 55% of enterprise AI inference is now running on-premise. Up from 12% three years ago. The companies driving that shift aren't doing it because on-premise AI became easier — it didn't. They're doing it because their legal teams and risk committees finally read the actual data residency provisions in their cloud contracts.

Second: The Australian Privacy Act December 2026 deadline is 85 days away. From 10 December, APP entities must disclose in their privacy policies the types of personal information used in substantially automated decisions. "We use AI in our operations" is not the disclosure the OAIC is looking for. The disclosure has to name the information types, the decision categories, and the potential impact on individual rights. If this isn't already in your compliance pipeline, you are behind.

Third: Open-weight models capable of running on your own infrastructure have just crossed a credibility threshold that makes avoiding cloud inference a real choice rather than a research project. Moonshot's Kimi K3 — 2.8 trillion parameters, open weights, 1 million token context — is the most downloaded model on Hugging Face right now. The capability gap that previously forced sensitive workloads onto frontier cloud APIs has materially narrowed.

I'm not arguing that every organisation should rip out its cloud AI stack today. The economics don't support that for most use cases, and the operational complexity of self-hosted inference is real.

What I am arguing is that the "we'll sort sovereignty later" posture has run out of road. The December deadline is regulatory. The CLOUD Act is treaty law. APRA's CPS 230, which extends information security obligations to material AI service providers, is already in force.

The questions your board should be asking your technology leads right now:

Which of our AI workloads process personal information that's material to our regulatory obligations? Where does inference actually run for those workloads — and is that provider US-incorporated? What's the disclosure in our current privacy policy about automated decision-making? And what's our plan if the OAIC's new proactive enforcement posture finds us without a satisfactory answer to any of the above?

The good news is that the market has built the infrastructure to answer these questions. The timeline to comply with December's obligations is tight but achievable. The harder work is the honest audit of which AI workloads are processing what data where — because most organisations don't have that map yet.

Build the map. Then decide the architecture.

#DataSovereignty #AustralianPrivacyAct #LocalAI #PrivacyByDesign #GDPR #AIGovernance #RegulatedIndustries
