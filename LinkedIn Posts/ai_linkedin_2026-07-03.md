# AI LinkedIn Post — 3 July 2026
**Status:** Draft (review before posting)

---

Your vendor says your data lives in Australia.

Ask them where the model *thinks*.

That single question is exposing a compliance gap that's going to catch a lot of organisations flat-footed before December.

Here's the problem: "Australian hosting" has become a marketing claim, not a technical guarantee. Multiple cloud AI providers store data in Sydney or Melbourne data centres while routing inference — the actual model computation — through Singapore or US regions during peak load. Storage residency and processing residency are different things. Most enterprise contracts only guarantee the first one.

This matters right now for a specific reason.

APRA issued a letter on April 30 calling out four AI governance failures across its regulated entities — banks, insurers, and super funds. One of the failures it named explicitly: treating AI as "just another technology" risk. APRA's point is precise. AI's probabilistic outputs, adaptive behaviour, and heightened data exposure aren't covered by the standard IT risk frameworks most financial services firms have been trying to bolt it onto. And if you don't have a formal inventory of your AI use cases and where data flows through them, APRA has now signalled that's a supervisory target.

Meanwhile, the Privacy Act clock is ticking. From December 10 this year, APP entities must disclose in their privacy policies what types of personal information feed substantially automated decisions, the nature of those decisions, and where they could significantly affect individual rights. The penalty structure — up to AUD 50 million, or three times the benefit from the contravention — means a profitable AI use case can generate a fine that dwarfs the revenue it ever produced.

Here's what makes this moment genuinely interesting.

The open-weight model ecosystem crossed a significant threshold this month. GLM-5.2, a self-hostable open-source model, now outperforms GPT-5.5 on SWE-Bench Pro coding benchmarks. MiniMax M3 combines a 1M-token context window with native image and video processing — in a model you can run on your own infrastructure. Ollama v0.30.8 runs 27B-parameter models on Apple Silicon with serious MLX acceleration.

What this means practically: the capability gap between "cloud AI" and "local AI" is closing. The privacy compliance gap between them is not.

Running inference on your own infrastructure — or in a verifiably sovereign cloud with contractual processing-residency guarantees — is no longer a performance tradeoff. The models are good enough. The regulatory pressure is real enough. And the processing-residency question — not just where data is stored, but where it is computed — is now the right question to be asking every AI vendor in your supply chain.

For decision-makers in financial services, health, and government: if you haven't started your AI use-case inventory, you are already behind the APRA timeline. If you haven't verified processing residency with your cloud AI vendors, you are already assuming a compliance position you haven't confirmed.

The December deadline is five months away. The supervisory program is active now.

The question isn't whether to use AI. It's whether you know where it thinks.

---

#AI #DataSovereignty #PrivacyByDesign #LocalAI #GDPR #AustralianPrivacyAct #APRA #AIGovernance
