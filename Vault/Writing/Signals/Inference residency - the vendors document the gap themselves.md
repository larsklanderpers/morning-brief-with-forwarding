---
date_first_seen: 2026-08-07
date_updated: 2026-08-07
source: AWS Bedrock docs / Microsoft Learn / Google Vertex docs / OpenAI Help Center
url: https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html
brief: ai
threads: [AI Sovereignty, Ad Hoc Regulatory Regime, Clubs - AML]
beat: AI / Data Residency / Inference
status: developing
used_in:
---

# Inference residency — the gap is documented by the vendors themselves

**What happened.** The brief's claim: *"Many platforms claiming 'Australian hosting' still route inference
through Singapore or US regions at peak load."* Checked properly, the framing needs one adjustment and
becomes far stronger for it. **There is no documented incident of an unannounced failover.** There does not
need to be — **the routing is the default, it is documented, and the vendors market it as burst capacity.**
Write it as *"by design and by default"*, not *"caught doing it."*

## The four quotes that carry the argument

**AWS Bedrock.** *"Cross-Region inference routes your requests by using compute across different AWS
Regions."* Global profiles: *"Amazon Bedrock automatically selects a commercial AWS Region to process the
request"* — worldwide, no geographic restriction. AWS's own warning: *"If you have strict data residency …
requirements, you should carefully evaluate whether cross-Region inference aligns with your policies and
regulations, as your inference data can be processed across multiple pre-configured Regions."* And the
residency-vs-processing split in AWS's own words: *"None of the customer data is stored in any destination
Region when using cross-Region inference."* Global CRIS is explicitly sold as burst — handling
*"unplanned traffic bursts"*, AWS's India post frames it around *"3-5x the normal traffic."*
Prefixes: `au.*` = ap-southeast-2 + ap-southeast-4 only; `apac.*` from Sydney can land in Tokyo, Seoul,
Osaka, Mumbai, Hyderabad, **Singapore**, Sydney, Melbourne — six of eight destinations outside Australia;
`global.*` is worldwide. **The existence of an `au.*` prefix is the tell: AWS built an Australia-only
geography because the default paths are not Australia-only.**

**Microsoft.** *"Data stored at rest remains in the designated Azure geography."* … *"For **Global**
deployment types, the service can process prompts and responses in any geography where the model is
deployed."* And Global Standard is the recommended default: *"For most workloads, start with Global
Standard. It launches first when a new model releases, has the lowest price, and offers the broadest region
coverage."* Data Zone Standard confines to US, EU or **APAC** — and *"Microsoft can add regions to either
data zone without prior notice."*

**The single best data point in the whole file.** An Australian healthcare customer asked Microsoft for
Regional Standard GPT-5.x in Australia East. Microsoft staff answer, on the record:
*"GPT-5.1 and GPT-5.4-mini are not currently listed as available for Standard (Regional) deployment in
Australia East."* … *"Global Standard … does not guarantee processing exclusively within Australia East."*
… *"Data Zone Standard … is not equivalent to processing exclusively within a single Azure region."*
… *"Microsoft has not published a roadmap or ETA."*
**For frontier models on Azure in Australia, in-Australia inference is not currently purchasable.**

**Google Vertex.** *"Don't use the global endpoint if you have ML processing requirements, because you
can't control or know which region your ML processing requests are sent to."* And flatly:
*"Endpoints don't guarantee data residency or in-region ML processing."*

**OpenAI** splits the two concepts by name: data residency governs *"where in-scope customer content is
stored"*; inference residency governs *"where model inference on in-scope customer content runs on GPUs."*
**Inference residency is offered only in Europe (EEA + Switzerland), the United States and the UAE.**
Australia is a **data-residency option only.** Even with inference residency on, *"CPU-based processing,
including but not limited to external integrations"* may occur elsewhere.
**Google Workspace/Gemini:** admin-selectable data regions are **US or Europe only** — no Australia option
at all, and coverage does extend to processing.

## Why this is the load-bearing note in the sovereignty thread

*Not Where It Lives. Where It Thinks.* (10 Jul) argued the distinction. This note is the **proof, in the
vendors' own documentation, with an Australian regulator hook attached**: CPS 230 para 59(b) requires
notifying APRA **before** entering a material offshoring arrangement, footnoted as one where *"the service
provided is undertaken outside Australia."* **Cross-region inference to Singapore or the US is service
provision undertaken outside Australia.** The obligation exists today; the routing is on by default; and
Microsoft has said in writing that the compliant alternative is unavailable for frontier models.
That is a complete argument with no speculation in it.

## Observations

- **2026-08-07** — First seen as a vendor-sourced sovereignty claim; verified into something much better. The "at peak load" phrasing is the only part to drop.

## Feeds

- [[AI Sovereignty]] — promote into State of play; this is the thread's strongest verified artifact
- [[APRA CPS 230 voice AI vendors]] — para 59(b) is the mechanism that bites
- [[CLOUD Act Australia - the exposure predates the agreement]] — the legal half of the same argument
- [[Self-hosted AI as the GDPR-compliant path]] — the remedy, and its real cost
- [[Clubs - AML]] — member data, offshore inference, a regulator that already asks about offshoring

## Open

- Does an entity actually *know* which inference profile its vendor or SaaS supplier uses? For a bank buying a voice-AI product built on Bedrock, the routing decision is made two layers up the stack. That is the fourth-party problem with a technical fingerprint — and it is checkable: ask for the model ID prefix.
