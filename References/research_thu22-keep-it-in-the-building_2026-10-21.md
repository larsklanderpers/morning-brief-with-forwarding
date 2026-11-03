# Research note -- Thu 22 Oct 2026, Keep It in the Building (working)

Written 21 Oct 2026 evening PT (Thu 22 day chat). Research then draft, on his word.

## SOLID (primary reached)

1. **Muse Spark Open -- Meta's own post, 15 Oct 2026.** research.meta.ai/blog/muse-spark-open
   - "816B total parameters (42B active)", "1M-token context window", natively multimodal.
   - "run on your desktop using two Apple M5 Ultra Mac Studios"; "up to 512 GB per Mac Studio, so two machines can hold an entire model"; "two Mac Studios behave like one supercomputer with a terabyte of unified memory." Runs via MLX.
   - Licence named: "Muse Model License", "limited commercial terms, which allow many developers to use the model for free."
   - Also hosted by Baseten, Fireworks, Groq, Modal, Nebius, OpenRouter, Together; weights via SageMaker, Google Model Garden, Hugging Face, Microsoft Foundry.
   - **The page does NOT say data stays local.** It says "at home" and agentic tests ran "entirely on-device". Do not put a privacy promise in Meta's mouth.
2. **Muse Model License -- Hugging Face model card** (huggingface.co/meta-models/Muse-Spark-Open-816B-A42B).
   - Model-as-a-service above **US$20M gross revenue in any 12 months: must notify Meta and sign a separate agreement.**
   - Usage Policy (Exhibit A) incorporated; "not intended for individuals under the age of 18".
   - **Must display "Built with Muse Spark Open"** in UI, docs, site or settings.
   - "Meta claims no ownership of outputs."
   - No termination clause in the text as fetched (fetch may be partial: do not print "cannot be revoked").
   - Weights in BF16 and NVFP4; GPU route "at least 700GB of VRAM for NVFP4 and 2TB for BF16"; "optimized to run on two Mac Studios with M5 Ultra using MLX."
3. **DeepMind + GovTech Singapore, 14 Oct 2026.** deepmind.google/blog/on-device-ai-scam-detection-mddi/
   - Fine-tuned lightweight Gemma on local scam conversations. Two stages: a lightweight classifier screens inbound messages; only suspicious ones go to Gemma with "a larger snapshot of the conversation".
   - Reason stated: privacy. Runs "entirely on-device", so neither the Singapore Government nor Google "will be able to access users' conversations through its deployment."
   - **Not live.** Rollout "carefully phased", inside applications, with user consent. No app named (ScamShield NOT named). No accuracy figures.
   - Context figures (Google's): scams over half of Singapore's reported crimes; more than S$4 billion lost since 2019.
4. **DHS FASCSA order on DeepSeek** -- Federal Register public inspection 2026-21447, filed 19 Oct, published 20 Oct 2026. Authority: Federal Acquisition Supply Chain Security Act of 2018 (41 U.S.C. 1321-1328). Excludes DeepSeek from civilian procurement; removes DeepSeek products AND "third-party products and services developed using DeepSeek implementations." **The excerpt does not say whether self-hosted open weights are covered.** Do not claim either way.
5. **MOFCOM + MOST Announcement No. 48 of 2026, 16 Oct.** Proposed revision of the Catalogue of Technologies Prohibited and Restricted from Export; 23 AI items (large models, agents, compute clusters). Already-open-sourced technology excluded ("已通过开源...进入公共领域的技术，不纳入管理范围"). Registration before export applies from 16 Oct. Comments close 15 Nov 2026.
   - Thresholds (2T params, "globally leading", 1e26 FLOPs) are from secondaries (letsdatascience, China AI Dispatch translation), not on the MOFCOM page as fetched: attribute or omit.

## CONTESTED / SECONDARY ONLY

- **Mac Studio price.** Apple's store page (fetched 21 Oct) shows no M5 Ultra memory upgrade pricing and no 512GB option. iClarified: M5 Ultra "starts at $5,499"; "The 512GB configuration will become available in late October." Guru3D: a 256GB / 4TB M5 Ultra config "priced at $12,299". MacRumors (15 Oct): 512GB "supposed to be coming later this month"; 256GB already over $10,000.
  -> **His $40,000 to $50,000 for two is his estimate; attribute it to him and say the 512GB machine was not yet on Apple's store when this was written.** NVIDIA $150K-$250K: his figure, attributed (no primary sought; NVIDIA's own GB300 blog exists for Muse but gives no price).
- **DeepSeek V4.1 Flash 1017** (20 Oct): open weights, MIT licence per secondaries (pasqualepillitteri, mind-verse); hosted API reportedly lets DeepSeek train on inputs (brief, secondary). Benchmarks are DeepSeek's own; independent index lower. Not footed at DeepSeek's HF page.
- **Pragmatic Engineer "halved API bills"** (21 Oct brief): not read at the page. Do not use without it.

## DO NOT PRINT

- That Meta promises your data stays local.
- That the Singapore tool is live, or that it is ScamShield.
- That the DHS order covers (or exempts) self-hosted DeepSeek weights.
- MOFCOM thresholds as if from the MOFCOM text.
- Any Apple price for the 512GB configuration.
- "the Muse licence cannot be revoked".

## Commercial interests to name

- Meta is giving away weights while selling Meta AI; Apple is selling the $5,499-and-up machines the release was built around (Ternus congratulated Zuckerberg publicly). The "two desktops" demo is a joint marketing moment for both.
- Google wrote the Singapore post and supplies the Gemma model.

## Corpus

- "Mac Studio": 0 hits in Published (plan, 17 Oct). On-device: Thu 1, Sat 26 Sep. Local model on the desk: Thu 1 (Copilot+). Agent's own computer: Thu 8.
