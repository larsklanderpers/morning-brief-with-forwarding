---
name: slot-drift-gates
description: "★★ 10 Sep 2026: Tuesday and Saturday are VARIATIONS, not spine days, and both had drifted into the weekday spine. Two hard gates now run at PLAN time. ⛔ ENFORCEMENT BEGINS WITH THE WEEK OF MON 14 SEP 2026, his ruling 12 Sep -- earlier plans are out of scope. Read before writing or amending any week plan."
type: feedback
sources: [cowork-import]
imported_at: 2026-09-15T13:26:17Z
---

**The rule: Tuesday and Saturday are VARIATIONS. They are a different KIND of thing from the spine, and
the plan must prove it in writing before anything is drafted.**

Source of truth is `References\SLOT_CHARTER.md` (v1.2, 10 Sep 2026, on his word; effective date added
12 Sep). `CLAUDE.md` points at it. The `day-start` skill checks it at boot (step 2b). This note is the why.

## ⛔ EFFECTIVE DATE -- HIS RULING, 12 Sep 2026. Read this before reporting any gate finding.

Verbatim: *"we only adopted the gate rule a couple of days ago because we kept missing the tuesday and
saturday. enforcement needs to being Monday 14th."*

**The gates bind from `week-plan_2026-09-14.md` onward.** Plans dated **7 September or earlier are OUT OF
SCOPE**: a missing `TUESDAY GATE:` or `SATURDAY GATE:` line in one of them is **not a finding, not a FAIL,
and is not reported as either.** Charter §7.5 is the only copy of this.

**Why, so it is not re-opened on merit:** the charter was adopted 10 Sep, three days into a week planned
on 4 Sep. Scoring a plan against a rule that postdates it measures nothing about the plan, and the only
available remedy is retro-fitting a PASS after the days have shipped -- which is precisely the paper
compliance the charter exists to catch. **A planning control binds at plan time or not at all.**

⚠️ **Two things this does NOT change.** It changes WHEN the gates apply, never WHAT they say. And it
covers the PLAN's missing lines, never the DAY's work: a Tuesday or Saturday piece drafted against an
older plan is still checked against the charter's tests by its own chat under 2b.
⚠️ **It is an effective date, not a grace period.** Nothing re-opens for the older plans on 14 Sep.

**How this came up (12 Sep, the Sun 13 chat):** the boot reported the 7 Sep plan's missing Tuesday line as
a FAIL, correctly under the rule as written, and he withdrew it. **The lesson is narrower than "do not
report gate findings": check the plan's DATE against the effective date before reporting one at all.**

## Why the gates exist

He raised it himself, 10 Sep 2026, unprompted, after catching a bad Saturday at boot the day before:
*"I have seen, for the last 23 weeks... that we've drifted from what we said was going to be the rule."*
And: *"We can't sort of sink back into just kicking out shit off the typewriter and it's no big deal."*

**He was right and the record is worse than his impression.** Measured across every published and
scheduled piece:

- **Saturday.** The last genuinely hands-on Saturday was **8 Aug ("Own the Kitchen", indexed as
  `Saturday Diversion (hands-on)`)**. The five since have been argument or evidence pieces, and 5 Sep
  ("The Second Number Nobody Measures") ran four studies, a Lancet RCT and an EEG preprint at ~3,600
  words -- **longer than every weekday piece that week except one.** Saturday had become one of the
  heaviest days, not the lightest.
- **Tuesday drifted twice.** First into a three-week coding-practice sub-arc (18 Aug / 25 Aug / 1 Sep,
  near-identical thread strings), then on **8 Sep into a straight weekday cyber-governance piece**
  ("Your Opt-Out Has an Owner", `AI Attack Surface x Trust Boundaries`).
- **The planning artifact inflated while the slots blurred.** Week plans went 11 KB → 125 KB in six
  weeks and not one of those bytes was a slot check.

## The mechanism, because it is not laziness

**A per-piece chat only ever sees one day.** Nothing in the pipeline looked across slots -- the editor
panel checks form, accuracy and cross-piece collisions, never whether a piece belongs in its slot. So
the drift was structurally invisible and would have kept going.

**And Saturday drift has one specific cause: at plan time the only candidates on the table are the
week's research leftovers, and those are all weekday-shaped.** Saturday defaults to leftovers because
nothing else is in front of the planner. ⚠️ Two Saturday-shaped builds
(`DESIGN_heinlein-slack-control-plane_2026-09-03.md`, `DESIGN_brief-radar_2026-08-25.md`) sat unused in
`References\` through the entire drift.

## How to apply

**Write both gate lines into every week plan from 14 Sep onward, at PLAN time, PASS or FAIL with a
one-line reason. A missing line is itself a FAIL -- it means nobody ran the check.**

```
TUESDAY GATE: PASS|FAIL -- <why it reads as a different KIND of thing from Mon/Wed/Thu/Fri>
SATURDAY GATE: PASS|FAIL -- human feature: <name it in one line, or say there is none>
```

- **Check the plan's date first.** Dated before 14 Sep 2026: no gate finding, ever. See the effective
  date above.
- **Tuesday is the breath.** Lighter, different vein, organized around what it does for you and what the
  implications are. Can be a political beat, or something fun done with a tool. **Never "here's the news
  and here's what it means"** -- Wed/Thu/Fri own that.
- **Saturday is what it does for you.** One named human or shared-human feature: a family bot, a control
  plane, a tool at a price, a thing he built. Sample prompts in the body, fuller set as an addendum.
  **Saturday does not have to tie to the week** -- his call: draw a line if one is there, fine if not.
- **Pull Saturday from the charter's bench FIRST**, never from research leftovers.
- **A FAIL is a call-out, never a veto.** Say it, propose the re-pitch, let him decide. He can overrule
  in one word; the plan records the overrule and the reason so it is not re-argued later.

## Open, and his

**Thursday as a third variation.** He floated it 10 Sep (*"the most popular pieces... a bit less dry"*)
against his own six-beat spine (Mon shape-of-work, Wed cyber, Thu AI growth, Fri turning-a-business-into-
something, Sun capstone). **Not adopted:** three variations leaves only Mon/Wed/Fri feeding a ~4,000-word
capstone, and he wants Friday to arrive with four or five arc pieces behind it. **Adopted instead:**
Thursday is written as the least dry of the spine days, and dryness there is worth flagging even though
it is not a gate. His call if he wants the full version.

## Related

[[content-architecture]] · [[week-shaping-skills]] · [[lars-length-aside]] (lightness is a state of
being, not a length metric -- the Saturday gate measures feel and reader gain, never word count) ·
[[decide-dont-reconfirm]] (a gate FAIL is proposed-and-proceeded, not re-asked every week)
