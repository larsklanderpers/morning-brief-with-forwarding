# AI LinkedIn Post — 4 July 2026
**Status:** Draft (review before posting)

---

The most important AI compliance deadline you're probably not tracking lands in four weeks.

On 2 August 2026, the EU AI Act reaches full enforcement. On 10 December, Australia's automated decision-making obligations under the Privacy Act kick in. APRA published a letter in April naming four specific AI governance failures it's observed across regulated entities — and declared formal supervisory intent.

Three separate regulators. Three separate deadlines. One common thread: they're all arriving at exactly the moment when running frontier AI on-premise — without sending a single byte of customer data offshore — has become genuinely practical for the first time.

This week, OpenAI released two open-weight reasoning models under Apache 2.0: gpt-oss-20b (runs on 16 GB RAM) and gpt-oss-120b (80 GB). In the same breath, GLM-5.2 dropped under MIT licence with 1M-token context and benchmarks that beat GPT-5.5 on SWE-Bench Pro. Qwen3 runs from 1.7B to 235B with no commercial restrictions.

These are not "good enough for experiments" models. These are frontier-quality, production-ready, locally deployable models with permissive licences.

For years, the conversation about AI and data privacy has been shaped by a false choice: use a capable model and accept the data egress, or run local AI and accept a capability penalty. That trade-off is gone. A single GPU workstation now runs a model that, eighteen months ago, required cloud infrastructure and an API key — and a privacy policy that said "your data may be used to improve our services."

The compliance case isn't hypothetical anymore either. OAIC's guidance on automated decision-making transparency closes for consultation last month and formal guidance arrives in September — giving organisations one final chance to adjust before December enforcement. APRA's letter is already on file. The EU AI Act's penalties — 7% of global turnover, higher than GDPR — are live in four weeks.

Here's what I think the next 90 days look like for any business that processes customer PII with AI:

The ones that have already mapped their automated decision-making processes and documented their model selection rationale will move quickly. They'll evaluate gpt-oss-20b or GLM-5.2 against their use case, run a proof-of-concept on local infrastructure, and either adopt or document why cloud remains appropriate. Either way, they'll have a defensible position when the regulator asks.

The ones that haven't started will spend those same 90 days in a very expensive scramble.

The technology has closed the gap. The regulation has set the deadline. The only remaining variable is whether your organisation treats this as a strategic opportunity — to build AI capability with privacy by design — or as a compliance fire drill.

The infrastructure to do this right now exists. The regulatory window to do it in time is closing.

---

What's your organisation's plan for local AI deployment? I'd genuinely like to hear what's working and what's blocking progress.

#DataSovereignty #PrivacyByDesign #LocalAI #AustralianPrivacyAct #EUAIAct #GDPR #AIGovernance #APRA
