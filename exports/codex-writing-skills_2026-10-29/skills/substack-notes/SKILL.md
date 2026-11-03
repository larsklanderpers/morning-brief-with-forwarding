---
name: "substack-notes"
description: "Write the day's Substack Note from that day's piece: 3 candidates, 1 recommended, afternoon slot. Batch mode on demand for flagship pieces. Use on \"today's note\", \"write a note\", \"notes from X\", and every time a piece moves to Scheduled."
---

# Substack Notes

One strong note a day, mined from that day's piece and posted in the afternoon. Lars publishes a piece every day, so the unit is the day, not the week.

**Run it without being asked (his correction, 30 Sep 2026: "you skipped the note suggestions again").** Every time a piece moves to `Substack Scheduled\`, produce that piece's three candidates in the same turn.

## Modes
- **Daily (default).** Take today's piece and produce 3 candidates. Recommend 1.
- **Batch (only when Lars asks: "batch this one", "this one has legs").** Take a flagship piece and produce 3-4 extra notes. They go to the reserve (below), not the schedule.
- **Reserve pull.** On days when the day's piece won't yield a strong note (capstone, diversion, thin piece), recommend one from the reserve instead. Say that it came from the reserve.

## Inputs
- The day's piece in its FINAL, signed-off form. Read the whole file, including its status header: rulings, redactions, printed promises.
- The notes log: `Substack Notes\notes_log.md`. It covers the last 14 days of posted notes in full plus the reserve, and drives the repetition check.
- The permanent ledger: `Substack Notes\notes_ledger.md`. Every posted note, full text, newest first, never trimmed. This is the corpus to go back to.
- Voice: the live `feedback_lars_writing_voice.md` + `feedback_lars_contractions.md`. If they aren't reachable, use the `editor-panel` Prime Directive. Apply the taste file `reference_mds\lars-about-me.md` silently.

## Step 1: Mine
Pull 6-10 raw candidates, in this order of value:
1. His own quotable lines. Lifting his sentence beats writing one.
2. Numbers and specifics already in the piece: costs, counts, thresholds, timelines.
3. A rule or principle he states.
4. A first-person moment: a mistake, a wry aside, a story beat.
5. A prompt or artifact a reader can use today.
6. The contrarian turn the piece argues.

## Step 2: Draft 3 candidates
- **Different angles.** Each candidate uses a different type AND different source material from the piece.
- **Types (only these):** Single-Punch, Contrarian, Pattern Observation, Problem -> Fix, Direct Advice, Build-in-Public, Prompt Drop. Never use income-proof, vulnerability-bait or permission-giving formulas.
- **Standalone by default.** A candidate must land for someone who never reads the piece.
  - At most one of the three may be a link-back version.
  - Across the week, aim for about 2 in 3 posted notes standalone.
  - Check the log before recommending a link-back.
- **Length.** Default 2-6 lines. Use white space and single-line paragraphs.

## Step 3: Rules (tighter at daily cadence)
- **Provenance.**
  - His sentences stay intact: contractions, `-`/`--` dashes, stance markers, asides.
  - Drafter lines follow the rubric: no contractions in exposition, never an em-dash.
  - Tag every candidate as his / drafter / mixed.
- **No new claims.** Every fact, number and name must already be in the piece. Carry its redactions (employer, customers, repos, tickets). Keep its hedges.
- **7-day repetition check against the log**, applied to drafter text. His lifted lines are reported, not failed. A fail is any of:
  - the same type posted yesterday
  - the same opener shape or closer shape within 7 days
  - the same controlling image or device within 7 days
  - the same lifted-line pattern within 7 days (e.g. negate-then-correct twice)
- **Never pre-empt a printed promise.** A note must not spend material a later piece has promised to deliver, and must not front-run tomorrow's topic.
- **Slop gate.** Run Seat 5 of `editor-panel` on drafter lines. Kill on sight:
  - negate-then-correct (drafter writes none)
  - hollow tricolons, throat-clearing glue, LLM diction
  - engagement bait ("Would you stop scrolling", "Here's the thing", "This changed everything")
- **Fit the day's register.** The Saturday personal build and the Tuesday management piece each keep their own voice in the note.

## Step 4: Recommend
Pick the one that is most specific, most his, and most likely to be screenshotted. State the reason in one line.

## Output
```
### Today's note -- <piece slug>, <date>, afternoon
**Recommended: <A|B|C>** -- <one-line why>

**A. <Type>** (standalone | link-back) -- provenance: <his | drafter | mixed>
<text>

**B. ...**
**C. ...**

Log check: <clean | what collided and which candidate it knocked out>
Rulings needed: <plain English, real calls only, or "none">
```

## After Lars picks
- **Write it down in the same turn he names the pick, in BOTH files.** On 1 Oct 2026 he had to paste the Tue 29 and Wed 30 notes back because those chats never logged them. A note that is not on disk did not happen, as far as the next chat knows.
  - `notes_log.md`: date, type, opener shape, closer shape, controlling image, standalone/link-back, provenance, source piece, text.
  - `notes_ledger.md`: the same entry with full text, newest first.
- **Date it to the day it is POSTED.** He often picks after midnight or names several days at once ("the 30th was C, the 29th was A, today will be B"). If the date is ambiguous, ask in one line before logging.
- **Record his posted wording if it differs from the candidate**, marked "as posted". If he edited it and did not paste it, say the final wording is not captured and invite him to paste it.
- Unpicked candidates that pass the rules may go to the reserve, but only if Lars says so.
- Trim `notes_log.md` entries older than 14 days into a one-line-per-week summary. **Never trim `notes_ledger.md`.**
- Lars posts to Substack himself. This skill never posts.