---
date_first_seen: 2026-08-07
date_updated: 2026-08-07
source: Attorney-General's Department / DOJ / 18 USC 2713 / agreement text
url: https://www.ag.gov.au/international-relations/international-crime-cooperation-arrangements/international-production-order-framework
brief: ai
threads: [AI Sovereignty, Ad Hoc Regulatory Regime, Clubs - AML]
beat: AI / Data Sovereignty / Law Enforcement Access
status: developing
used_in:
---

# Australia–US CLOUD Act — the date is wrong and the causation is backwards

**What the brief said.** *"Australia–US CLOUD Act Agreement (in force Jan 31, 2026) — US law enforcement
can now reach data held in Australia by US-headquartered cloud providers."*

**Both halves fail.** Keep this note as the standing correction — the claim will recur, because the vendors
pushing it sell the remedy.

## The date: 2024, not 2026

Signed **15 December 2021**. AG certification 15 Dec 2021, Congress notified 22 Dec 2021, 180-day review.
**Entered into force 30 January 2024** (AGD wording: *"On 30 January 2024, Australia and the United States
brought into force the Agreement…"*), reported as 31 January 2024 in US reckoning — same event, timezone.
**Nothing happened on 31 January 2026.** The 2026 date traces only to AI-consulting vendor content
(aivy.com.au and similar), which sells sovereignty scoping. **UNVERIFIED-OR-VENDOR-SOURCED-ONLY.**

## The causation: reach came in 2018, and the Agreement partly *narrows* it

US extraterritorial reach over provider-held data has existed since **23 March 2018** under
**18 U.S.C. § 2713**: a provider *"shall comply with the obligations of this chapter to preserve, backup,
or disclose … **regardless of whether such communication, record, or other information is located within or
outside of the United States**."* No Australian data-centre location has ever changed that.

The 2024 Agreement does something narrower and largely the reverse:

- It resolves **conflicts of law** so providers can answer the other party's process — primarily so
  **Australian** agencies can send International Production Orders directly to US providers instead of
  waiting on MLAT.
- Art. 4.3: orders *"shall not intentionally target a Receiving-Party Person."* Home Affairs gloss:
  *"The US will be prohibited from targeting Australian persons under the Agreement, including citizens,
  permanent residents, corporations, non-incorporated associations like charities, government entities and
  persons physically located in Australia."*
- Art. 4.5: specific accounts only. "Covered Offense" = **maximum penalty ≥ 3 years**. Art. 5: independent
  judicial or equivalent review. Art. 7: minimisation. Art. 11: annual compliance review and public
  aggregate reporting.
- It makes Australia a **qualifying foreign government** under § 2523, which **activates the § 2703(h)
  comity motion**: a provider may move to quash within 14 days where it reasonably believes *"that the
  customer or subscriber is not a United States person and does not reside in the United States"* and that
  disclosure *"would create a material risk that the provider would violate the laws of a qualifying foreign
  government."* **That motion exists only where a qualifying agreement is in place.**
- Australian side: IPOs issued by judges and ART members, every outbound order reviewed by the **Australian
  Designated Authority**, Ombudsman and IGIS oversight, framework in Schedule 1 of the TIA Act 1979.

## The sentence to use instead

> US agencies could already compel a US-headquartered provider to produce Australian-stored data — that has
> been true since the CLOUD Act in 2018, and no Australian data-centre location changes it. The 2024
> bilateral agreement did something narrower and in one respect the opposite: it created a reciprocal
> direct-order channel, barred orders under it from intentionally targeting Australian persons, and gave
> providers a comity route to resist US process over non-US persons.

**Why this is better material, not worse.** The vendor version is a scare with a wrong date. The true
version is more useful to a regulated audience: **the exposure is eight years old, structural, and
unaffected by where the data sits — which is exactly why the argument has to move from storage to
inference.** See [[Inference residency - the vendors document the gap themselves]].

## Observations

- **2026-08-07** — First seen in the AI brief's sovereignty section, sourced to Brightlume/Amaze. Same provenance problem already logged against [[APRA CPS 230 voice AI vendors]]: every appearance of this claim traces to a company selling sovereign deployment. That is now a pattern worth naming in a piece — **the sovereignty market is generating its own legal facts.**

## Feeds

- [[AI Sovereignty]] — kills the residency comfort blanket properly, with primary law
- [[Ad Hoc Regulatory Regime]] — obligations and exposures arriving through instruments nobody legislated for AI
- [[Clubs - AML]] — same audience, same question about where member data can be compelled from

## Open

- The genuinely open question the vendors never ask: does § 2713 reach **inference** — a prompt processed offshore and never stored — as "information within the provider's possession, custody, or control"? Transient processing sits awkwardly in a statute written for stored communications. **[VERIFY] — worth a lawyer's read before a piece asserts either way.**
