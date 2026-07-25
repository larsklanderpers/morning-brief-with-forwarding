---
date_first_seen: 2026-07-20
date_updated: 2026-07-20
source: RyderAI / Brightlume AI
url: https://brightlume.ai/blog/data-residency-ai-workloads-australian-compliance-sovereign-deployment
brief: ai
threads: [Ad Hoc Regulatory Regime, AI Sovereignty, Clubs - AML]
beat: AI / Policy / APRA / Data Residency
status: developing
used_in:
---

# APRA CPS 230 — voice AI vendors are material service providers

**What happened.** In effect from 1 July. Australian banks, insurers and super funds must
bring voice AI vendors into full third-party risk management: service provider registers,
continuity planning, resilience testing, concentration risk.

**Why it matters.** The sharp edge is that data residency under CPS 230 now explicitly
covers **model inference**, not just database storage. That quietly invalidates the
common architecture where data is stored onshore but reasoned over offshore — which is
most cloud AI deployments. Any institution running customer-facing voice AI without the
vendor on the register is already non-compliant, not approaching non-compliance.

## Observations

- **2026-07-20** — Second appearance (also in the 19 July brief). The framing has hardened from "watch this space" to "you are already exposed."

## Feeds

- [[Ad Hoc Regulatory Regime]] — obligation arriving through a prudential standard rather than AI-specific law
- [[AI Sovereignty]] — the inference-vs-storage distinction is the whole Model Sovereignty argument, now with a regulator behind it
- [[Clubs - AML]] — same third-party risk muscle the sector already has

## Verified 2026-07-20 — the framing was wrong, the argument is stronger

Primary text checked ([APRA CPS 230](https://www.apra.gov.au/standards/cps-230)). The standard
contains **no mention of AI, inference, or data residency**. It does not classify voice AI
vendors as anything — materiality is functional: "those on which the entity relies to undertake
a critical operation or that expose it to material operational risk."

What it *does* say, verbatim: *"Material offshoring arrangement means a material arrangement
where the service provided is undertaken outside Australia. Offshoring includes arrangements
where the service provider is incorporated in Australia, but the physical location of the
service being provided is undertaken outside Australia."* Plus a duty to notify APRA **before**
entering such an arrangement.

So offshore inference is captured — not as a residency rule but as an **offshoring
notification obligation**, which is a harder duty, not a softer one. Also: CPS 230 applied from
**1 July 2025**; the amended standard commences 1 July 2026. The briefs' "takes effect 1 July
2026" is wrong.

**Provenance problem:** every brief entry since 25 June traces to four commercial sources —
Trillet (voice AI vendor), Brightlume (sovereign deployment consultancy), RyderAI, Lorikeet.
All sell the remedy. No APRA guidance, no law-firm alert, no regulator statement anywhere in
the chain.

## Open

- This is now a piece in its own right — see `References/research_verify-four-claims_2026-07-20.md`, angle 1 — and it is now running as a correction section in *Bring the Model Home* (Fri 24 Jul).
- CPG 230 guidance not separately checked; if APRA has addressed AI it would be there.
