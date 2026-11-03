# AI LinkedIn Post — 29 August 2026
**Status:** Draft (review before posting)

---

Your organisation probably has an "Australian data centre" AI contract.

What it likely doesn't have is an audit log showing where your customer data was processed during peak load last Tuesday.

Those are different things. And starting 10 December 2026, the difference carries penalties up to AUD 50 million.

---

Three things landed this week that belong in the same conversation.

**First.** The EU AI Act's high-risk obligations became enforceable on 2 August. Maximum fines: 7% of global annual turnover — exceeding GDPR. 78% of organisations haven't started meaningful compliance work. 50% can't tell you what AI systems they're running. The enforcement clock is now ticking.

**Second.** Australia's Privacy Act reform kicks in on 10 December. From that date, if your AI or automated process makes a decision that significantly affects an individual, you need to say so in your privacy policy. OAIC formal guidance is expected in September — which gives you about three months between receiving the guidance and being required to comply with it.

**Third.** A Dutch specialist posted something on LinkedIn this week that I think is the clearest articulation of the problem I've seen: "Copilot is not the first step. It is the final test." His point: most organisations are enabling AI before they've classified the data underneath it, configured sensitivity labels, locked down DLP policies, or established governance over what the AI is actually *allowed* to use.

They're failing the test before they've sat the exam.

---

Here's the part that regulators are starting to understand and most AI vendors still won't say clearly:

**Data residency is not data sovereignty.**

If your AI vendor is headquartered in the US, your data is subject to US legal jurisdiction regardless of which data centre it sits in. The CLOUD Act doesn't care that your servers are in Sydney.

And if your vendor claims "Australian processing" but routes inference through Singapore during peak hours — which is common, because it's cheaper and faster — then your data is leaving the country on a schedule your contract doesn't reflect and your CISO probably doesn't know about.

This is the unresolved gap for every APRA-regulated entity. APRA is expected to publish updated CPS 230 guidance on cloud risk that will address it. When that guidance arrives, it will not be kind to organisations that contracted for storage residency and assumed they'd covered processing sovereignty.

---

The argument for acting now rather than waiting:

Open-weight models that match frontier performance on most enterprise tasks now run on your own infrastructure. OpenAI released open-weight models this month. Ollama's latest update aligned its API with OpenAI's wire format — which means local deployment now has the same integration overhead as cloud deployment.

The capability parity argument is gone. The compliance argument for local or sovereign AI is getting stronger by the quarter. The window to shape your architecture before regulators finalize what they're measuring is Q4 2026.

An Australian specialist recently described the decision well: start with the information architecture, then enable the AI. Classification, sensitivity labels, governance, audit trail — and only then the model.

The alternative is doing it backwards and spending 2027 unwinding it.

---

If you run a bank, insurer, or government agency in Australia and you haven't mapped which AI systems are making or substantially assisting decisions affecting your customers, that's the starting point. Not a vendor demo. Not a pilot. A system inventory.

December is four months away.

#AI #DataSovereignty #PrivacyByDesign #AustralianPrivacyAct #GDPR #LocalAI #APRA #EUAIAct #AIGovernance #RegulatedIndustries
