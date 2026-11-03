# Research note: Kimi K3 open weights -- the date, and the "open is not local" problem
**Date:** 26 July 2026 (Sunday)
**Trigger:** today's story-candidate brief said the weights land "tonight," which read as a conflict with the 27 July date used in three pieces.
**Bottom line:** the 27 July date is CORRECT and needs no correction. The self-hosting numbers below are real but do NOT constrain his argument -- see the ruling under EXPOSURE: quantised models are the answer, and `bring-it-home` stands as written.

---

## SOLID -- the date is not a conflict

Release is **27 July 2026, 00:00 UTC**. That converts to **26 July, 8:00 PM ET** -- which is why US coverage dated 25 Jul ran the headline "arrive Sunday" while the model's own published date is the 27th. Same moment, two clocks.

For the AU audience it is unambiguously **Monday 27 July, 10:00 AM AEST**.

**Consequence:** no date correction is needed in any piece.
- `substack_draft_bring-it-home_2026-07-24.md` -- "27 July" is accurate.
- `substack_scheduled_who-controls-the-model_2026-07-30.md` -- the pre-authored optional upgrade line ("-- and on 27 July, they were") is accurate as written. Safe to apply at the 28-29 Jul gate once the drop is confirmed.
- The week plan's "re-check weights 28-29 Jul" gate stands unchanged.

## SOLID -- the specs, and why they matter more than the date

| Fact | Detail |
|---|---|
| Parameters | 2.8T total, ~50B active (sparse MoE) |
| Weights size | ~594 GB at MXFP4 four-bit |
| **Memory to actually serve it** | **~1.4 TB of fast GPU memory** (~5.6 TB at 16-bit) |
| Accelerators | ~18 x 80GB just to load weights; a single newest-gen node (8 x 192GB, ~1.5TB) barely fits with no headroom for context or concurrency |
| Silicon lock-in | MXFP4 runs natively only on **Nvidia Blackwell or AMD MI400**. Other hardware effectively excluded. |
| Vendor guidance | Moonshot recommends a supernode of **64+ accelerators** in one high-bandwidth interconnect domain |
| Context asymmetry | The 1M-token window is initially a **cloud serving feature**; local inference on day one caps at ~131,072 tokens |
| Licence | **Not published as of 25 Jul.** K2 used a Modified MIT requiring brand attribution above revenue thresholds. Read the actual repo licence file before any commercial deployment. |

TECHi's phrasing is the useful handle: **"open is not local."** The realistic operators are inference providers, the clouds, and a handful of very large enterprises -- not a registered club, not a mid-size regulated business, not the open-source developer community. The binding constraint is keeping 1.4 TB warm, i.e. tokens per megawatt, not raw throughput.

## CONTESTED / UNVERIFIED
- The 93.4% SWE-bench Verified figure in today's brief is Moonshot's own claim. UK AISI/CAISI published a *preliminary* cyber assessment 23 Jul; independent benchmark verification is exactly what the brief itself says to wait for. Do not print the number bare.
- Licence terms are unknown until the repo lands. Any "you can deploy this commercially" implication is unsupported until then.

---

## EXPOSURE -- RAISED AND RULED ON, 26 Jul. `bring-it-home` STANDS AS WRITTEN.

I flagged line 35 of `substack_draft_bring-it-home_2026-07-24.md` -- "near-frontier capability is now something you can run inside your own walls" / "the kitchen is now something you can actually own" -- as unqualified against the 1.4 TB serving numbers.

**Lars ruled the draft stands, 26 Jul:** "they can get there with quants of other models for the vast majority of what they need, and I have no doubt a quant of kimi k3 is not far away."

He is right and the flag was measured against the wrong yardstick. It implicitly asked whether you can serve the full-precision flagship at cloud scale. The question that actually matters to a regulated business is whether it can run *enough* capability on hardware it owns -- and quantised open-weight models already clear that bar for the vast majority of workloads. Quantisation is the missing term above: every number in the table is full-weight MXFP4 for the 2.8T flagship, and none of it constrains the 30-70B quants a club or a mid-size firm would actually deploy. A K3 quant is a near-certainty besides.

**Standing rule from this:** do not raise hardware caveats on open-weight claims unless the piece is specifically about serving a flagship at full precision. Assume quants; check the quantised tier before flagging.

## OPPORTUNITY -- "open is not local" is a piece

Strongest new angle from this brief. The gap between "the weights are free" and "you can run it" is the same shape as every other governance gap he writes about: the right exists on paper, the capability to exercise it is distributed unevenly. Pairs naturally with Ng's OpenWorker and Cisco Antares (both genuinely local-scale), and with the hedge framing from the "$5/month research server" item -- the real local-first story is small models you can actually host, not the 2.8T headline. Constructive, operational, how-to. Diversion-shaped.

---

**Sources:**
- [TechTimes -- Kimi K3 Open Weights Arrive Sunday (25 Jul 2026)](https://www.techtimes.com/articles/321551/20260725/kimi-k3-open-weights-arrive-sunday-self-hosting-cuts-china-data-risk-api-never-can.htm)
- [TECHi -- Kimi K3's open weights arrive July 27. The catch is 1.4TB](https://www.techi.com/kimi-k3-open-weights-inference-economics/)
- [VentureBeat -- Moonshot releases Kimi K3, largest open-source model ever](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems)
- [Nathan Lambert / Interconnects -- Kimi K3: The open-weights escalation](https://www.interconnects.ai/p/kimi-k3-the-open-weights-escalation)
- [Simon Willison -- Kimi K3](https://simonwillison.net/2026/Jul/16/kimi-k3/)
