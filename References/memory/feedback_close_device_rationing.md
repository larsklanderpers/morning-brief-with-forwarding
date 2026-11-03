---
name: charter-drift-across-three-copies
description: The panel charter exists in 3 places and drifts BOTH ways; Seat 5 spec current as of 15 Aug 2026 (adds the section-header sweep). Newest wins, memory beats both files.
type: feedback
sources: [cowork-import]
imported_at: 2026-09-15T13:26:00Z
---

**Rule:** The editor-panel charter lives in **three** places that drift apart — the project-memory voice note, the `Writing Flow\03_editor-panel.SKILL.md` snapshot, and the **installed** skill the Skill tool actually loads. **The newest wins; the memory note beats both files.** Before trusting any rule the panel enforces, check whether the installed copy agrees with the `Writing Flow\` snapshot. When they differ, that IS the finding — report it and fix the stale copy, don't just fix the piece. **Drift runs in both directions** — 25 Jul the installed copy was stale; 15 Aug the snapshot was.

**Why:** found 25 Jul 2026. Four consecutive weekday closes (27, 28, 29, 30 Jul) carried the reader's-calculus / "news cycle that never even seems to pause" device, three near-verbatim. The initial diagnosis — that the `Writing Flow\` snapshot was stale — was **wrong**. That snapshot had been correctly updated on 24 Jul with the rationing rule, the cross-piece repetition check in Seat 5, and the 9.0 bar. The **installed** skill was the stale one: it still listed the calculus close as a standing requirement, had no cross-piece check, and carried the old 8.5 bar. It was scoring the device's *absence* as a voice miss on every piece, pushing each close back toward the formula.

Two knock-on facts worth keeping:
- **The bar is 9.0, not 8.5** (raised 21 Jul 2026). Lars's own handoff prompt cited 8.5 — the stale number propagates through prompts too, not just files. Confirm rather than quietly scoring to the lower bar.
- Lars's call on the four pieces: fix Thursday only, flag the rest, touch nothing already Scheduled or signed off.

---

## SEAT 5 SPEC — CURRENT AS OF 2026-08-15

### The 7 Aug changes (window + categorical rule)

**1. Window widened: last two pieces -> the full seven-day publication arc.** Three days either side at minimum. Rationale he gave: "that's the pattern I am writing in."

**2. Anchor to PUBLICATION order, not draft order, and check BOTH directions.** He drafts three to four days ahead, so the files nearest in the folder are not the ones his reader just read. Check `Substack Published` / `Substack Scheduled` for what has run AND `Substack Drafts` for what is already written for later in the same week.

**3. Cross-piece repetition is a CATEGORICAL FAIL, independent of numeric score.** Numeric slop floor 9.5. Lars proposed 9.3; the counter he accepted is that this seat scores in effective half-point steps, and a numeric floor can be averaged away by a generous read on minor in-piece tells while a structural bleed slips through.

**Driver case (6 Aug):** the Mon 10 Aug draft carried "the bot gave away the house keys... a stranger walking around in your kitchen" two days after Sat 8 Aug's entire piece was the kitchen. Scored 8 with a clean line-level read; would have shipped under a purely numeric rule.

### NEW 15 Aug 2026 — the SECTION-HEADER SWEEP (Lars asked for this by name)

**The categorical rule now also covers section headers — verbatim OR by function — at three or more inside the window.**

**Driver:** on 15 Aug the Mon 17 draft was about to carry `## Where I would push back on myself`, a header that had already run **verbatim** on Thu 13, Fri 14 and Sun 16 — and had **cleared all three panels**. In the same window `## What I would actually do this week` ran in five of six consecutive pieces ("...do today", "...do with a Saturday", "...do this week to start tuning my own instruments" — one header wearing four coats). Lars: *"I caught the repetition but didn't realize it was that much that fast."*

**Why it needed its own check rather than falling out of the existing one:** Seat 5 hunts controlling images, devices and closes — all of which live in prose. **Headers are read as furniture, not as prose**, so a careful human reading each piece in isolation reliably misses them, and so did the panel, three times running. This is the one repetition class that must be caught **mechanically**: extract the `## ` lines across the window and diff them. Do not try to notice it by feel.

**The fix is a rename, and it is voice-neutral** — it touches none of his sentences, so it counts as a safe fix under the loop rules rather than a proposal. **Do NOT delete the section.** His concession beat and his action beat are structural parts of the form, not devices. Rename so the header states what *this* piece's version is actually about.

**Second finding in the same pass:** the `Writing Flow\` snapshot's round-report template was stale against the installed copy — missing the `Cross-piece window checked` and `Categorical cross-piece fail` lines added 7 Aug, so a panel run from the snapshot would never have reported the window it read. Restored 15 Aug along with the `Charter copy loaded` line.

---

## STATUS OF THE THREE COPIES — 2026-08-15

- **Memory note (this file):** current.
- **`Writing Flow\03_editor-panel.SKILL.md`:** patched 15 Aug, current.
- **Installed skill:** **Lars pasted the patched copy over it on 15 Aug and confirmed in chat.** Treat as current.

⚠️ **Not independently verified, and here is why it cannot be.** The installed skill is exposed to a session as a **read-only cache snapshotted at session start**. When I checked after he confirmed, the container copy still showed the pre-patch file dated 13 Aug — that is expected sync lag, not evidence he missed a step, and it is *not* a signal to make him re-do it. **Do not re-ask him whether he installed it** (see [[decide-dont-reconfirm]]).

**The observable tell, next panel run:** a round report that includes a `Section headers swept:` line means the patched copy loaded. If that line is absent, the run is on a stale copy — say so in the report, fall back to the `Writing Flow\` snapshot, and do the header sweep manually regardless.

**How to apply:** (1) When a repeated flaw shows up across several pieces, suspect the generator before the judgment — check all three charter copies against each other. (2) After correcting one copy, correct the others in the same pass or the drift just reverses direction. (3) State in the panel report which copy you loaded and whether it agreed with memory. (4) A skill file written from a session is a read-only cache — patch the `Writing Flow\` snapshot, hand Lars the file for the installed copy, and never report a skill as installed when all you did was deliver it. (5) Related: [[forward-dated-draft-risk]] — the same "trust the artifact, don't re-derive it" failure mode, applied to dates instead of rules.
