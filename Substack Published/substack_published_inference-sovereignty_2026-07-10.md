# Not Where It Lives. Where It Thinks.

**Status: Scheduled -- Friday, 10 July 2026**

---

This week, the United States switched two frontier AI models back on for the rest of the world. Australia should be paying very close attention to what that actually means.

Anthropic's Fable 5 and Mythos 5 -- models that had been fenced off under national-security export restrictions -- were cleared for global redeployment after the White House lifted the controls. No product launch. No price change. A policy decision, reversed by a later policy decision. And it is worth remembering that the restrictions those models were just released from were themselves imposed the same way: by decree, without warning, without a vote.

Sit with that sequence. The same frontier capability was fenced off, then released, on nothing more than a memo -- and the memo could just as easily run the other direction tomorrow. For Australian businesses that have quietly built their AI strategy around "we'll access whatever the best model is via API," that is the wake-up call. Your access to the infrastructure powering your AI capability is not a commercial arrangement. It is a foreign policy decision. It can be granted, and it can be revoked, and you will not get a vote either time.

---

## The Concept Nobody Is Talking About: Inference Sovereignty

Here in Australia, we've spent two years (at least) debating data sovereignty and the implications in the modern connected world. Where does our data live? Which cloud provider? Which Australian region? Is it in Sydney or Singapore? These are legitimate questions -- particularly as it relates to the individual's PII and the protection of that data from worldwide scraping regimes -- and we've built entire compliance programmes around answering them.

But there's a more fundamental question that barely got a mention until APRA dropped its letter on 30 April 2026.

Where does the thinking happen?

APRA -- after a targeted engagement across large Australian banks, insurers, and superannuation trustees -- documented four AI governance failure categories and drew a bright line: AI inference on customer or member data must occur onshore, or within jurisdictions with equivalent regulatory oversight.

Read that again. Not storage. *Inference.* The computational act of your AI model *reasoning* about your customer's data -- that is a regulated activity, and for the first time an Australian prudential regulator has said it must happen in a controlled jurisdiction.

This is inference sovereignty. It is not a concept from a think tank paper. It is now APRA guidance, and every regulated entity in Australia -- banks, insurers, superannuation funds -- is in scope.

Here is the hard architectural reality for most organisations running cloud AI in 2026: your data might sit in an Australian AWS or Azure region. Your inference almost certainly doesn't. When you call a GPT or Claude API, the model weights, the GPU cluster running the computation, and the process of "thinking" about your customer's data are all happening on infrastructure located in the United States, under US legal jurisdiction, accessible to US law enforcement under the CLOUD Act. (Note: Anthropic and AWS announced last week that Bedrock will have locally hosted Claude inference, if not already then very soon, which does provide some improvement to the access to frontier models. From AWS: For frontier models (like Claude Sonnet 4.6 and Opus 4.6), you can ensure strict data residency by using Geographic Cross-Region Inference (Geo-CRIS) to protect against transport. For clarity by me: CRIS is not available for newer models like Opus 4.8, Fable 5, or Sonnet 5, at this time.)

Data residency and inference residency are two different things. We've been solving for the first one. The second one just became urgent.

---

## This Is Not a New Problem. We Just Never Named the AI Version.

Every regulated business already understands one principle in its bones: the infrastructure that makes decisions about your customers has to be documented, auditable, and within reach of the regulator. *Where* a decision gets made matters as much as what the decision is. We apply that instinct to identity verification, to credit decisioning, to transaction monitoring. We have simply never applied it to our AI stack.

So apply it. When a model flags a customer's risk, generates a service decision, or processes anything that touches a person's identity or transaction history, that model -- and the inference it runs -- is part of your regulated decision-making infrastructure. The OAIC's Privacy Act amendments, effective 10 December 2026, will require you to disclose in your privacy policy *which AI systems make substantially automated decisions* that significantly affect customer rights, and *what personal information* feeds those systems.

Most organisations cannot answer those questions right now. Not because the answers are complicated -- because nobody asked them at deployment time.

The window is short. The OAIC's formal guidance doesn't drop until September; the disclosures are due 10 December. We are being asked to build disclosure frameworks for systems we deployed without them, using a rulebook we don't have yet, under a penalty regime that caps at the greater of AUD 50 million, three times the benefit obtained, or 30% of adjusted annual turnover.

---

## The World Is Building Walls -- And We're Still Assuming Open Borders

Australia is not the only jurisdiction that arrived at this conclusion this week. The world is building sovereign AI infrastructure at a pace that should reframe how any Australian business thinks about its technology supply chain.

France activated Mistral's Bruyères-le-Châtel data centre -- thousands of NVIDIA H100 GPUs, €2.1 billion in state investment, 50 kilometres south of Paris. This is not a startup's colocation facility. This is a national AI infrastructure project, backed by the French state, designed to ensure that European AI inference happens on European soil, under European legal jurisdiction, beyond the reach of American subpoenas and Chinese IP law.

The EU AI Act becomes fully applicable on 2 August 2026 -- just over three weeks from now. The OpenEuroLLM consortium, funded by the EU and spanning research institutions across multiple countries, expects to release its first open-source multilingual models this month. Europe has decided it wants frontier AI capability that it controls end to end: the model weights, the training data, the compute, and the inference.

Every major jurisdiction is building the same thing. India's sovereign AI initiative. The Gulf states' Arabic-language model programmes. Japan's AI sovereignty framework. South Korea. Canada. The emerging consensus in global AI policy is that inference -- the *act of AI reasoning* -- is a strategic capability that cannot be wholly delegated to two American companies and a Chinese lab.

Australia has a AUD 29.9 million AI Safety Institute. It is doing important work. It is not a sovereign compute infrastructure.

The question for Australian business leaders is: what happens when every major AI-producing jurisdiction decides to manage access to its frontier models the way the US now openly does -- gating or releasing by decree, on its own timetable? What does your AI strategy look like if the API calls stop working?

---

## The Chinese Model Question

This is the part that makes compliance teams nervous and capability teams interested.

The open-weight Chinese models are genuinely good, and their licences change the game. GLM-5.2 shipped this month -- 744 billion parameters, MIT licence. MiniMax M3 pairs a million-token context window with native vision. An MIT licence means you download the weights and run them on your own infrastructure, in your own jurisdiction, with no API key, no terms-of-service review, and no data sent anywhere. Once downloaded, the model is yours. On this axis the inference sovereignty argument actively *favours* them: the thinking happens exactly where you decide it happens, beyond the reach of any foreign government's access controls.

But.

These models were trained under Chinese legal frameworks, by organisations subject to a national security law that compels cooperation with state intelligence on request -- with no obligation to disclose that cooperation to users. You cannot audit the provenance of a 744-billion-parameter model the way you can audit a financial statement. The upside is real: they cannot be gated by a foreign government. The downside is equally real: their creation sat under a legal regime structurally incompatible with Australian privacy law and APRA's data governance expectations.

And here is the scenario nobody has modelled publicly. What if China does what the US just demonstrated -- but in reverse, and selectively? Washington showed this month that frontier access can be restricted or released by decree. Beijing could pull the same lever on its open-weight models: export controls, licence changes, or simply altering the terms under which weights can be downloaded. Apply that not globally but to specific jurisdictions, for specific geopolitical purposes. If Australia's relationship with China deteriorated the way it did in 2020, and Beijing treated AI model access the way it once treated barley, every Australian business that had quietly made open-weight Chinese models its sovereignty play would be left with exactly what it had already downloaded, and nothing newer. Whether that is a feature or a bug depends entirely on how recently you downloaded.

Or worse -- as discussed in my recent piece 'The Agent Obeyed. It Just Wasn't Obeying You,' the potential exposure to foreign national security directives, an exposure by no means unique to the Chinese models, is very real, particularly for a regime (or regimes, depending on how cynical you are feeling as you read this) that has made clear that traditional Australian expectations of privacy and "a fair go" don't hold.

---

## What Inference Sovereignty Actually Requires

We have learned this lesson before in other domains: compliance is never satisfied by a policy document alone. It requires operating infrastructure, documented processes, and audit trails a regulator can actually inspect. Those things were never glamorous, but they became the competitive baseline.

Inference sovereignty requires the same treatment. It is not a vendor selection question. It is an architecture question.

**Know where every inference call lands.** Build a model inventory -- not just "which AI tools do we use" but specifically: which AI systems touch customer PII, which decisions do they inform, and where does the inference computation happen? This is the question the OAIC will ask in September when guidance drops. It is the question APRA is already asking. Have the answer before the regulator asks it.

**Treat inference location as a data governance decision.** The same rigour you apply to deciding which cloud region holds your transaction data should apply to deciding where AI reasoning about that data occurs. "The vendor has an Australian data region" is not a sufficient answer if inference is routed through US infrastructure. Confirm inference location contractually, not just in marketing materials.

**Evaluate open-weight models seriously, with clear eyes.** Local deployment of open-weight models -- whether Mistral, MiniMax M3, or permissively-licensed open models -- is a legitimate sovereignty strategy, but it is not risk-free. Understand the training data provenance, the licence terms, and the upstream legal obligations of any model you deploy. MIT licence does not mean no risk. It means no ongoing API relationship -- which solves one problem and potentially creates others.

**Build for supplier diversity.** The organisations most exposed to this week's US gating decision are those with a single frontier model dependency. The organisations least exposed have a stack that mixes cloud frontier models for appropriate workloads, local open-weight models for sensitive inference, and clear policies about which PII flows where.

**Get your December disclosures ready now.** The OAIC's formal guidance arrives in September. Your privacy policy amendments are due December 10. That is ten weeks between guidance and deadline. For any organisation that needs board approval, legal review, and a communications process, ten weeks is not enough if you're starting from scratch. Start from the model inventory now.

---

## The Bottom Line

Two governments made the same point this week in different languages. The US said: frontier AI capability is a geopolitical asset we control. APRA said: AI inference on Australian customer data is a regulated activity that must happen in a jurisdiction we can reach.

Both of them are right. And both of them are telling you the same thing: your AI stack is part of your regulated infrastructure, the same way your transaction processing and identity verification systems are. The difference is that this piece of infrastructure does its work on someone else's soil, under someone else's law, at someone else's discretion -- and can be switched off between a Friday memo and a Monday morning.

We've built compliant, auditable, sovereign infrastructure for all of those things. The question isn't whether we can do it for AI. The question is whether we'll do it proactively, before the regulator's sweep, or reactively, after the letter arrives.

In this industry, we know which of those two outcomes is preferable.

The thinking needs to stay where we can see it.

---

*Lars Klander writes about cybersecurity, AI, and technology risk for regulated industries. This article reflects his personal analysis.*
