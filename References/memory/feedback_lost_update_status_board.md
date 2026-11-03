---
name: lost-update-status-board
description: "One board per plan does NOT prevent silent clobbering. ★★ AMENDED 13 Sep after a SECOND occurrence in which the documented mitigation was followed correctly and failed anyway: re-staging and expectedMtimeMs do NOT protect a row, because the hazard is the OTHER session's stage time, which you cannot see. Verify your row after committing."
type: feedback
sources: [cowork-import]
imported_at: 2026-09-15T13:26:00Z
---

**Rule: edit the week plan IN PLACE with `device_bash`. If the mount is down and you must stage → edit → commit, re-stage immediately before the commit, pass `expectedMtimeMs`, AND THEN RE-READ THE FILE TO CONFIRM YOUR ROW IS STILL THERE. The last step is the only one that actually catches this.**

## ★★ SECOND OCCURRENCE, 13 Sep 2026 — the mitigation was followed and the row was lost anyway

The Sun 13 chat wrote its panel result into the Sun 13 row of `week-plan_2026-09-07.md` (rv5 = 9.24,
three rounds, the categorical fail, his rulings). It followed this note exactly: re-staged the plan
immediately before writing, applied its row to that fresh copy, passed `expectedMtimeMs`, did not use
`force`. **The commit succeeded. The row was gone within the hour**, reverted to "DRAFTED v1, NOT
PANELLED" by another chat's whole-file write.

★ **Why the documented mitigation could not have worked, and this is the part the first entry got
wrong:** `expectedMtimeMs` guards the interval between YOUR stage and YOUR commit. It does nothing
about the interval that actually matters, which is between **the other session's stage** and **its
commit** — and that session had staged before your write and committed after it. **You cannot see the
other session's stage time, and no parameter available to you covers it.** A whole-file commit is a
read-modify-write with no compare-and-swap on a file with multiple concurrent writers; the guard only
ever protected the wrong end of the race.

**So the practical rule changes shape:**
- `expectedMtimeMs` is still correct and still worth passing. It is **not** protection, it is a
  narrowing. Do not treat a clean commit as proof.
- **The only reliable check is to re-read the file afterwards and grep for your own text.** Do it at
  the end of the session, and again if the session runs long. The 13 Sep loss was found only because
  Lars asked an unrelated question about the plan being stale, which sent the session back to look.
- **When two chats are known to be live on the same plan** (a Saturday piece being panelled while a
  Sunday piece is drafted, a Monday piece being researched), assume your row will be lost at least
  once and budget a re-check rather than a hope.
- ⚠️ **A lost `device_bash` mount that persists for a WHOLE session, as on 12-13 Sep, turns this from
  a hazard into a near-certainty.** Every write that session is a whole-file commit.

## The first occurrence, 9 Sep 2026

The Fri 11 chat wrote a full status-board row at 16:54 — the Achiam correction, the re-check findings,
the firecrawl discovery. **It was silently reverted within the hour.** The Sat 12 chat had staged its
own copy of the plan *before* that write, edited only its own Sat 12 row, and committed the **whole
file** back as v2.2, restoring its stale copy of every other row. Nothing errored. Neither session
broke a rule. The Fri 11 chat only noticed because it went back to add a later edit and found its own
text missing.

★ **The "one board per plan" rule does not cover this.** That rule was written for the 5 Sep collision,
where two chats each *appended* a rival board. This is the opposite shape: **one board, edited
correctly by both chats, and one of them lost anyway.** The rule says "edit the board in place" — but a
stage/commit cycle *looks* like an in-place edit and is not one.

**The trigger was a tool failure, not carelessness:** `device_bash` lost its Plan9 mount
("no Plan9 drive shares mounted"), which forces the stage → edit → commit path. **Treat a lost mount as
a concurrency hazard, not just an inconvenience.**

## How to apply

- Prefer `device_bash` with a python read-modify-write **on the user's machine**, which reads and
  writes the live file in one step and is immune to this.
- When the mount is down: stage, edit, **re-stage, re-apply to the fresh copy, commit with
  `expectedMtimeMs`** — then **verify**.
- Never `force: true` on a shared file. That is how a row disappears with no trace at all.
- **Rebuild your own row from your own knowledge, never from a stale copy**, and leave every other row
  exactly as the fresh copy has it. This is what makes recovery cheap when it does happen.
- ★ **Consider not fighting the race at all for long content.** A per-day handoff file that only one
  chat writes (`References\handoff_<day>_<date>.md`) cannot be clobbered by another chat's whole-file
  commit, and the board row can then be a one-line pointer to it. Raised 13 Sep, not adopted, his call.

Related: [[week-2026-09-07]] (the 5 Sep two-boards collision and both of these) ·
[[file-verification]] (staging can also serve *stale reads*, the same hazard from the other direction) ·
[[slot-drift-gates]] (the 13 Sep session also found the PLAN stale against research that had already
run — plans go stale in both directions, not just against landed text).
