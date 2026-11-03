---
type: thread
status: active
last_reviewed: 2026-08-10
---

# AI Sovereignty

Model and inference sovereignty — where the model runs, where it thinks, and whose jurisdiction that puts your customer data under. The thread closest to Lars's own operating problem.

## State of play

The thread's core argument is now **dated rather than directional**: four compliance
deadlines stack up (CPS 230 in effect, EU AI Act 2 Aug, AU mandatory standards, OAIC ADM
10 Dec) in the same window open weights reach rough parity — see
[[Compliance deadlines converge with open-weight parity]]. The capability excuse for cloud
AI expired as the compliance cost of cloud AI spiked.

Thread A closes Friday 24 Jul with *Bring the Model Home*. Its successor — the **provenance
question** — now has its sharpest, verified artifact: [[You cannot rent an audit trail]]
(Seale, confirmed 2026-07-21). The 26 Jul capstone *The Model Was Never the Hard Part* takes
it one step further, off the back of Lars's own interview: for inference specifically the
audit trail you can't rent is a **boundary you can prove**, not a **path you can trace** —
management by exception, "prove it could not have gone anywhere you didn't sanction." That
boundary framing is the live successor argument, and may deserve its own signal. Second live
angle: [[Two visions for agentic routing]] — frontier-first routing means the planning layer,
which sees everything, is the part that leaves the building. Nobody is framing that as a
sovereignty decision.

**Promoted 2026-08-07 — the sovereignty argument is now provable from vendor documentation, and the legal
scare it was resting on was wrong.**

[[Inference residency - the vendors document the gap themselves]] is the thread's strongest verified
artifact. AWS: *"your inference data can be processed across multiple pre-configured Regions"*, and global
cross-region inference is **marketed as burst capacity**. Microsoft: *"Data stored at rest remains in the
designated Azure geography… For Global deployment types, the service can process prompts and responses in
any geography"* — with Global Standard the **recommended default**, and a Microsoft staff answer on the
record that **Regional Standard GPT-5.x is not available in Australia East with no published ETA**. Google:
*"Endpoints don't guarantee data residency or in-region ML processing."* OpenAI offers **inference residency
only in the EEA/Switzerland, the US and the UAE** — Australia is data-residency only. The regulator hook is
**CPS 230 para 59(b)**: notify APRA *before* a material offshoring arrangement, where the service is
"undertaken outside Australia."

Against that, [[CLOUD Act Australia - the exposure predates the agreement]] retires a claim the briefs have
carried twice: the Australia–US agreement came into force **30 January 2024, not 31 January 2026**, and US
reach over provider-held offshore data has existed since **18 U.S.C. § 2713 in 2018**. The agreement is in
part *protective* — it bars orders under it from intentionally targeting Australian persons and unlocks the
§ 2703(h) comity motion. **Same provenance problem as the APRA claim: every appearance traces to a company
selling sovereign deployment.** That pattern — *the sovereignty market generating its own legal facts* — is
itself a piece.

Net effect on the thread: the **legal** argument gets weaker and older; the **technical** argument gets much
stronger and is now sourced entirely from the vendors' own manuals. Lead with routing, not with subpoenas.

**Updated 2026-08-10 — the physical layer arrives, and the cost argument does not.**

[[Anthropic Australian capacity tender and the copyright ask]] — AFR, off confidential tender documents:
**1.4 GW of Australian data-centre capacity, up to US$15 billion** (the A$21.6bn in circulation is a derived
conversion — use "US$15 billion, roughly A$21.6 billion" or no number), minimum **1 GW live by end-2027**,
procured from operators rather than built. And from **Treasury's own FOI'd briefing notes**, not from
Anthropic: investment in model-development capability and associated infrastructure is recorded as
**contingent on clarity of copyright settings**, with the **"long tail"** of small rights holders as the
stated obstacle. Officials rejected it. Australia has refused a TDM exception repeatedly — Rowland Oct 2025,
the Productivity Commission's **final** report Dec 2025, the Government's response since. Anthropic declined
to comment; **cut the "same play in the EU and UK" line**, which has no documented basis.

[[Token gray market - the operator can read every prompt]] — Okta and Unit 42, same week: resellers at
**5–15% of official per-token price**, stocked by fraudulent signups, abused startup credits and stolen
developer keys, routed through reverse-proxy "transfer stations". Okta: *"the service provider has full
visibility into prompts, as those prompts must be forwarded to a model."* Nobody has shown prompts **are**
harvested — and the sharpest fact is that `oai-reverse-proxy` **defaults to not using a key if invocation
logging is enabled**. The market has engineered around the only instrumentation that would produce evidence.
Sovereignty arriving via expense claim rather than procurement.

**And the correction that protects the thread:** [[Private AI cost parity - the break-even does not survive arithmetic]]. The "$8–12K box, cost parity in 3–6 months above 50K queries/month" claim comes from two pieces
of vendor content, shows no working, and is off by roughly an order of magnitude against real August 2026
API pricing — ~33 months before power, 50–100 after. The hardware band survives; the break-even does not.
**Do not print the cost excuse as expired.** The defensible economic leg is **per-seat licensing** (crossover
at 100–150 users, from the vendor's own honest paragraph) plus vendor dependency — not per-token inference.

## Pieces

- 2026-07-26 — The Model Was Never the Hard Part *(draft rv1; Sunday capstone; provenance → the boundary you can prove)*
- 2026-07-24 — Bring the Model Home: The Same Answer in Two Jurisdictions *(scheduled; closes Thread A)*
- 2026-07-21 — Accept, Refuse, or Delegate *(· Co-Existence / Judgment)*
- 2026-07-20 — The Compliance Tool Nobody Ordered Just Shipped as a Model
- 2026-07-10 — Not Where It Lives. Where It Thinks.
- 2026-06-30 — You Are the Product
- 2026-06-27 — When Five Spy Agencies Agree, You Should Listen *(· Geopolitics)*

## Open questions

- Now that open weights have closed the capability gap, what is left of the cloud argument for sensitive workloads?
- Which local, under whose governance norms, auditable by whom?
- For inference, can the "boundary you can prove" actually be enforced — or does the attack surface (prompt injection, subverted approval, the agent that talks itself onto another path) make the fence leaky? The capstone names this; it is not resolved.

## Signals

Linked signal notes appear in **Backlinks** below. Promote the load-bearing ones into *State of play* on the Sunday pass.
