---
name: brief-radar
description: "The fix for killed-claim regeneration in the morning briefs — a post-generation annotator over derived stores; includes the CORRECTION that briefing_agent.py is not the generator"
type: project
sources: [cowork-import]
imported_at: 2026-09-15T13:26:34Z
---

**Design note on disk: `References\DESIGN_brief-radar_2026-08-25.md`. Status PROPOSED, nothing built
into the tree.** Deny-list already generated: `References\derived_killed-claims_2026-08-25.json`.

## ⚠️ FIRST — the correction, because it has been steering the fix wrong

[[Brief Claim Provenance]] §5 says the do-not-print lists live in `References\` and
**"`briefing_agent.py` does not read any of them."** The *mechanism* is right; **the file is wrong.**

**`briefing_agent.py` does not generate the briefs and has not for some time.** Its
`format_brief()` emits numbered items (`### [n]`), per-item `*Flag for Substack: python
briefing_agent.py --flag n*` lines, and a section list (*Australian News & Regulation*, *Google Alert
Articles*) that appears in **no** recent brief. Its commentary calls Haiku at `max_tokens=200`.
**It is legacy. Do not patch it.**

**What actually runs:** three agentic skill prompts on a schedule (~11:41 UTC daily) writing
`Daily Briefs\brief_*.md`, `AI Briefs\ai_brief_*.md`, `AI Briefs\work_brief_*.md`. And the root-level
`ai-morning-brief-skill.md` is **itself a stale snapshot** — its section list no longer matches what
the AI brief emits. That is [[Charter Drift (3 copies)]] again, in the brief pipeline.

**Consequence for any future fix: work on the OUTPUT, not the generator.** One format, three files,
no prompt-drift surface.

## The three failures, which are not one problem

Do not let "restatement" stay a single word. It is three defects needing three mechanisms:

- **A — Regeneration.** A killed claim returns. **Deny-list catches it. 96% of kills carry a
  distinctive literal (a number, a CVE, a proper noun), so this is a string problem, not a model
  problem.**
- **B — Repetition.** The topic is already written. Needs a **spent-index** from SUBSTACK_INDEX +
  Published + Scheduled.
- **C — Fresh error.** A new wrong number, never killed because never seen. ⚠️ **A deny-list cannot
  catch this, ever.** Needs a watched-numbers table. (25 Aug example: a brief printed *"Challenger
  shows 48% of 2026 layoffs attributed to AI"* — the real figure is 112,713/477,033 = **24%**.)

## The design in one line

**A post-generation annotator (`radar.py`) over two DERIVED stores, which annotates and never
suppresses.**

- **Post-generation**, because one implementation beats three prompts and it survives skill drift.
- **Derived stores**, because a hand-authored kill file violates the standing "no second store, no
  fourth copy" rule and drifts in a fortnight. The research notes stay the source of truth; the JSON
  is a build artifact like a compiled index.
- **Annotate, never delete** — [[Killed-Claim FALSE POSITIVE]] means a kill can be wrong, and silent
  suppression would make a bad kill permanent and invisible.
- **⚪ STALE KILL badge:** **58 of 243 kills (24%) rest on ABSENCE of evidence** (`expiry_risk: high`).
  Those expire and get surfaced for re-test rather than fired as kills. This is the part that keeps a
  deny-list from becoming a ratchet, and nobody builds it.

## Demonstration result, 25 Aug 2026 — this ran, it is not a proposal

243 claims extracted, 674 match strings, **31 hits across today's three briefs** after a precision
pass (raw 54; the difference is generic match strings like "malware"/"sandbox" that need tightening).
**`CVE-2026-68820` fired THREE separate kills in one brief**, at regeneration counts ×3, ×2 and ×1.
Runtime under a second, no model call.

**Free regression test:** the corpus records which claims were killed on which date and when they came
back, so `radar.py` can be run over 14–25 Aug and scored against known answers before it is trusted.
No other component in this pipeline has one.

## The separable cheap win — do it first

**Date every item on the board.** His idea, 25 Aug, and it stands alone. The brief skills emit
`**Published:** YYYY-MM-DD` per item (`unknown` when it cannot be found — *unknown* is information,
and never default to today), and `outputs_build/build.py` renders an age badge (≤2d plain · 3–7d
amber · >7d ⏳ with days · unknown = distinct grey). **It kills the date-trap engine on its own** —
that engine has four recorded instances, including a 2023 study run as August 2026 news.

## Build order

**0)** dates on the board · **1)** commit the deny-list + precision pass on noisy match strings ·
**2)** `radar.py` deny-list only, sidecar output · **3)** regression-run over 14–25 Aug ·
**4)** spent-index · **5)** watched-numbers + superlative/engagement/date-trap regex ·
**6)** stale-kill expiry · **7)** tracker renders badges · **8)** research-assistant emits a fenced
do-not-print block so extraction becomes `grep` forever.

**Steps 0–2 are the 80%.** ⚠️ **Scheduling radar.py is RED** — new standing automation is his call.

## Also found, not fixed

- **`CLAUDE.md`'s "Current week plan" pointer is stale** — still names `week-plan_2026-08-17.md`,
  whose window closed 23 Aug. Not fixed because `CLAUDE.md` is outside its own GREEN list.
- **`ai-morning-brief-skill.md` at project root is a stale snapshot** — reconcile or delete it so
  nobody edits it believing it is live.
