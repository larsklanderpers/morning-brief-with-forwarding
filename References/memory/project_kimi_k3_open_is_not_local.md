---
name: kimi-k3-open-is-not-local
description: "Kimi K3 weights date RESOLVED; Lars RULED the bring-it-home draft stands; NEW 23 Aug — the licence gate is NARROWER than the corpus recorded and internal use is exempt"
type: project
sources: [cowork-import]
imported_at: 2026-09-15T13:26:34Z
---

Verified 26 Jul 2026. Full note + sources: `References\research_kimi-k3-weights_2026-07-26.md`.
Licence section below re-verified from primary text 23 Aug 2026 —
`References\research_story-candidates_2026-08-23.md` §7.3.

## ⚠️ CORRECTION 23 Aug 2026 — the $20M gate binds Model-as-a-Service operators ONLY

The corpus (and the MEMORY index line) recorded the Kimi K3 licence as *"Commercial Use Restricted
above $20M revenue."* **That is over-broad and would be caught by any lawyer in the room.** The
operative clause, from the licence text at
`huggingface.co/moonshotai/Kimi-K3/raw/main/LICENSE`:

> "If the Licensee or any of its affiliates operates a **Model as a Service** business, and the
> aggregate revenue of the Licensee and its affiliates exceeds **20 million US dollars** … over any
> consecutive 12 months, the Licensee must enter into a separate agreement with Moonshot AI before
> using the Software or its derivative works for any commercial purpose."

**Model as a Service** is defined as giving a third party access to inference or fine-tuning (e.g.
via API) such that they control inputs, parameters or training data. And **Section 4 expressly carves
out internal use** — *"any use that does not make the Software, its outputs, or its underlying
capabilities available to third parties."*

**Consequence for Lars's audience: a bank, a club or an insurer self-hosting K3 internally is NOT
caught by the $20M gate.** The SaaS reselling it is. Never write the gate as a general commercial-use
restriction.

**Section 3 is separate and does bite a consumer product:** prominent "Kimi K3" branding on the UI
above **100M MAU or $20M monthly revenue**.

⚠️ **Also stale: "~50B active parameters."** The model card says **2.8T total / 104B activated**,
MXFP4 native, 1M context.

★ **The teachable counter-example:** Qwen and Muse Glimmer ship **Apache 2.0 with no such gate.** So
the honest frame is not "open weights come with strings" but *"open" now has three separate
conditions — downloadable, runnable, and legally usable **for your specific business model** — and the
third is the one nobody checks.*

★ **The companion proof, same month:** **GLM-5.3** shipped via API on **15 Aug 2026**, promised
weights **~28 Aug**, and Z.ai **held them back** — *"As we scaled post-training, cyber capability
developed faster than we expected."* Open is now a release *process* with a vendor's hand on the tap.
⚠️ Do not print "GLM-5.3 beat closed models on CyberGym" unqualified: 84.5% is Z.ai's own
unreproducible number (the weights needed to check it are the withheld weights), the margin over
Fable 5 / GPT-5.6 Sol is **0.7–0.9pp**, and on ExploitBench it **loses 54.4 to 78.0**.

## The date is settled -- stop re-checking it
Kimi K3 open weights release = **27 July 2026, 00:00 UTC** = 26 July 8:00 PM ET = 27 July 10:00 AM AEST. US coverage dated 25 Jul ran "arrive Sunday"; the 27 July date in the drafts is the same moment on a different clock.

**Consequence:** no date correction needed anywhere. `bring-it-home` (24 Jul) "27 July" is accurate. The `who-controls-the-model` (30 Jul) pre-authored upgrade line "-- and on 27 July, they were" is accurate as written and safe to apply at the 28-29 Jul gate once the drop is confirmed. If a future session sees a brief say "tonight," this is why -- do not open a correction.

## The 1.4TB objection -- RAISED AND RULED ON, 26 Jul. Do not re-raise.
The raw serving numbers are real: ~1.4 TB fast GPU memory for K3, ~18 x 80GB accelerators minimum, Nvidia Blackwell or AMD MI400 only (MXFP4), Moonshot recommending 64+ accelerator supernodes; local inference caps ~131K context day one; licence unpublished as of 25 Jul.

I flagged this as an exposure in `substack_draft_bring-it-home_2026-07-24.md` -- line 35 claims "you can run inside your own walls" / "the kitchen is now something you can actually own" with no hardware qualifier.

**LARS'S RULING (26 Jul): the draft stands. His reasoning, which is better than my flag:**
> "they can get there with quants of other models for the vast majority of what they need, and I have no doubt a quant of kimi k3 is not far away."

**Why this settles it:** the flag implicitly measured "can you run it" against serving the full-precision flagship at cloud scale. That is the wrong yardstick for his audience. The real question is whether a regulated business can run *enough* capability on hardware it owns, and quantised open-weight models already clear that bar for the vast majority of workloads. Quantisation is the missing term -- the objection only bites if you assume full weights.

**How to apply:**
- Do NOT propose hardware caveats on open-weight claims unless the piece is specifically about serving the flagship at full precision. Assume quants.
- When a "you can't actually run that" objection surfaces, check the quantised tier before raising it.
- Note for the [[content-architecture]] "Open Is Not Local" idea parked in SUBSTACK_IDEAS.md: if that piece is ever written, quantisation is its resolution, not its problem -- the honest version is "the flagship is not local, but you do not need the flagship," not "open weights are a mirage."
