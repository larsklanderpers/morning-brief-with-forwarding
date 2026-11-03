---
date_first_seen: 2026-07-20
date_updated: 2026-08-07
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

- **2026-08-06 — The counter-example arrived, and it makes this note load-bearing again.** See
  [[NSW mandates AI registration and assessment across government]]. NSW's AI Operational Policy explicitly
  **exempts supplier-delivered AI from its register** — AI arriving inside a vendor's service is out of
  scope, "managed through procurement, contracting, and supplier assurance processes." CPS 230 does the
  reverse without ever using the word AI: materiality is functional, so vendor AI is caught wherever it
  sits on a critical operation, and offshore provision carries a pre-notification duty.

  The pair is the argument: **the technology-agnostic register catches AI; the AI-specific register does
  not.** Scoping to *function and reliance* nets everything the entity depends on. Scoping to *the
  technology the entity itself operates* nets only what it runs in-house. This is the strongest use yet
  for the verified reading below — the correction that killed the residency framing is exactly what makes
  the comparison work, because "no mention of AI" turns from the embarrassment into the point.

  Caveat to carry into any draft: not like-for-like. Prudential standard vs public-sector policy;
  material-service-provider register vs AI register. Concede it up front and argue the mechanism.

- **2026-08-07 — the "expected APRA cloud guidance on AI inference" does not exist, and the position is thinner than 2024.**
  Verified against primaries. (a) APRA **rescinded** its 2018 information paper *Outsourcing Involving Cloud
  Computing Services* on **19 February 2025**, to "reduce regulatory burden and improve clarity", pointing
  entities to CPS 230 instead — so cloud-specific guidance went **backwards**, not forwards. (b) The
  **1 July 2026 amended CPS 230** (determination made 23 Apr 2026) is narrow: limited exemptions from
  *specified contractual requirements* for non-traditional providers — government agencies, regulators,
  central banks, exchanges, clearing/settlement, payment operators, financial messaging. **Industry asked for
  "information technology and cloud infrastructure" to be added and APRA refused** — "The exemptions are
  reserved for types of provider where there is a universal contract gap and inability to negotiate bespoke
  terms." Take-it-or-leave-it hyperscaler AI terms get **no relief**. (c) APRA **has** spoken on AI: a
  **Letter to industry on Artificial Intelligence, 30 April 2026** (with a parallel ASIC letter) — boards to
  "maintain sufficient understanding and literacy"; map "the full AI supply chain, including material,
  third-party and fourth-party dependencies"; contractual "audit rights, model updates and deviations,
  incident notification"; concentration risk with "plausible and systemic failure scenarios" and credible
  "substitution, portability or exit arrangements". **But the letter never mentions CPS 230, CPS 234, data
  location, offshoring, sovereignty or inference services**, and commits only to "finalising its forward
  plan". So: the AI expectations are live *today* through CPS 230's existing machinery — including
  **para 59(b)**, notify APRA **before** entering a material offshoring arrangement, footnoted as one where
  "the service provided is undertaken outside Australia". **[VERIFY] closed: "updated cloud guidance expected"
  is vendor expectation, not an APRA commitment — cut it or attribute it.**

- **2026-08-07 — para 59(b) now has its technical counterpart.** See
  [[Inference residency - the vendors document the gap themselves]]. AWS, Microsoft, Google and OpenAI all
  document in their own materials that inference routes outside the nominated geography by default.
  Cross-region inference to Singapore or the US **is** service provision undertaken outside Australia.
  The obligation and the default behaviour are now both established from primaries, with no speculation in
  between — that is the sovereignty piece assembled.

- **2026-08-10 — third recurrence, same commercial chain, and the retired framing is back.** Flagged again in
  the AI brief as *"APRA CPS 230: AI vendors now material service providers"*, sourced to **Aona AI /
  Brightlume** — the same sovereign-deployment consultancy line as the 20 Jul appearance — with the added
  claims that *"pre-existing contracts require compliance by July 2026"* and that *"no-train clauses are a
  floor, not a ceiling."* The second is a fair point. The first is the framing **retired on 2026-07-20**:
  CPS 230 applied from **1 July 2025**; the 1 July 2026 amendment is the narrow non-traditional-provider
  exemption. And the standard still does not classify AI vendors as anything — materiality is functional.
  **Nothing new has happened. The claim simply recirculated.** That is now the most useful thing about it:
  three appearances, one provenance chain, zero regulator sources, and the corrected version each time is
  stronger than the vendor version. See [[Capability restated as certainty]] — this note is that pattern's
  longest-running case, and the reason it can be written with receipts.

## Feeds

- [[Ad Hoc Regulatory Regime]] — obligation arriving through a prudential standard rather than AI-specific law
- [[NSW mandates AI registration and assessment across government]] — the state counter-example; opposite scoping choice, opposite coverage
- [[AI Sovereignty]] — the inference-vs-storage distinction is the whole Model Sovereignty argument, now with a regulator behind it
- [[Clubs - AML]] — same third-party risk muscle the sector already has
- [[Supply Chain]] — functional materiality is the mechanism that reaches vendor AI at all

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
