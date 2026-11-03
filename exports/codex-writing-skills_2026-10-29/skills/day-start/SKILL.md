---
name: "day-start"
description: "Boot a fresh per-piece Substack chat: work out which week plan is live from today's date, check the slot gates, show Lars the week as currently planned, ask which day he is working, and load only what that day needs. Use at the start of any new Substack chat, or on \"start the day\", \"which day are we on\", \"new piece\", \"boot me up\"."
---

# Day Start

One chat per piece per day (adopted 4 Sep 2026). No session carries the whole week in its head, so no panel ever runs through a compacted summary. This skill is how a cold session gets oriented in one pass.

**Everything that matters is on disk, not in the conversation.** Derive, never assume. In particular: **never hardcode a week-plan filename** -- work it out from the date of the piece being written.

Project root on his machine: `D:\vc-personal-projects\Morning Brief with Forwarding\`. Prefer `device_bash` (ground truth; staging can serve stale copies). If the local workspace fails to start, fall back to `device_stage_files` and read in the container.

---

## Step 1 -- Work out which plan is live

```bash
cd "$HOME/mnt/Morning Brief with Forwarding"
date +"%F %A"                    # today
ls -1 References/week-plan_*.md   # every plan on disk
ls -lt "Substack Drafts" | head -12   # what has actually been written, newest first
ls -1 "Substack Scheduled" "Substack Published"
```

**Never truncate a folder listing by position.** `tail -30` and `head -12` on an alphabetical listing hide whole pages, and on 6 Sep that made two already-written drafts invisible and produced a wrong week picture that reached him in a table. `ls -lt | head` is fine for "what changed recently" because it sorts by time; anything you are using to decide whether a day is drafted must be filtered by DATE, not position:

```bash
ls -1 "Substack Drafts" | grep -E "2026-09-(0[7-9]|1[0-4])"   # every file for this window
```

Week plans live in `References\` as `week-plan_YYYY-MM-DD.md`, **dated to the Monday of the week they cover**. The live plan is the one whose Monday is the Monday of the week containing **the piece's publication date** -- which is often tomorrow, not today, because he frequently drafts the night before.

```bash
# Monday of the week containing any date
D=2026-09-05; date -d "$D -$(( $(date -d "$D" +%u) - 1 )) days" +%F
```

Before asking anything, pick the plan covering **today**; adjust if he names a day in another week.

**If no plan file exists for that week** (common on a Sunday or Monday), say so in one line and offer to write one. Do not draft to a stale plan from a previous week -- a plan whose Monday has passed is expired, not "close enough".

## Step 2 -- Read, in this order, and stop

1. `CLAUDE.md` -- the working agreement. GREEN / AMBER / RED, the standing accuracy rules, voice and process.
2. **`References\SLOT_CHARTER.md`** -- what each day of the week is FOR. Short, and it governs the week plan rather than the other way round.
3. The live week plan -- **its status board first**, then the day block for the day in question. Amendment blocks inside a day block supersede the reasoning above them; superseded text is kept deliberately, so read down to the last amendment.
4. `Substack Drafts\SUBSTACK_INDEX.md` -- the newest three or four rows. (The index lives in the Drafts folder, not the root.)
5. `References\MEMORY.md`, then whichever memory files it indexes bear on today. Project memory (`project_memory_read`) is the live index; `References\MEMORY.md` may not exist on disk at all, and its absence is not a finding.
6. **The newest daily brief -- AUTOMATICALLY, every boot (his ruling, 24 Sep 2026).** Read the most recent `AI Briefs\ai_brief_<date>.md`: its **Lane 7 -- Substack Signal** section in full, and the headline items of the other lanes. Skim the newest `work_brief_<date>.md` headlines too. **Why:** on 23 Sep the Fri 25 angle was sitting in the 22 Sep brief while the session ran two research hunts for pitches he could not stand behind. The plan is written before the week runs; the brief is what landed since. When a day's planned angle is weak or dead, the brief is the first place to look for its replacement, and any pitch should say which brief item it came from.

7. **#heinlein-inbox -- AUTOMATICALLY, every boot (his ruling, 27 Sep 2026).** Read the channel (Slack, `C0BVCSV0PJ5`) back to the last session's date and list anything he dropped that bears on the day: links, "footing for" notes, rulings. Also list `Research Notes\intake\` for intake notes dated since the plan was written, and read the research note's ADDENDA, not just its body. **Why:** on 26 Sep he dropped the @poteto X link as footing for Mon 28 at 14:51; the day chat booted without reading the inbox, told him the source was still his to find, and he had to ask "did you not receive it?" An inbox chat had also already written an intake note and a research-note addendum the day chat never opened.

Do **not** read the whole window yet, and do not read every research note. Load a piece's full text only when the task actually needs it (see Step 4).

### ⚠️ 2a -- Count the status boards before you trust one

**A plan can carry more than one board, and on 5 Sep 2026 one did.** Two sessions the same day each appended their own; each was right about its own day and stale about the other's, and one asserted "Mon 7 has no draft session yet" while that draft was already in the folder. Never assume there is exactly one board, and never conclude there is none without grepping:

```bash
grep -n "STATUS BOARD" References/week-plan_<Monday>.md
```

- **Zero hits** -- the plan genuinely has no board. Open one, once, at the end of the file.
- **One hit** -- that is the board. Use it.
- **More than one hit** -- **stop and reconcile before doing anything else.** Check every day's row against the files actually on disk (`ls -lt "Substack Drafts"`, `Substack Scheduled\`, `Substack Published\`), merge into the newest board, mark the others `SUPERSEDED -- merged into <the live one>. DO NOT UPDATE.`, and keep any research detail they carry that exists nowhere else. Tell him you found it.

**Re-grep before you write at the end of the session, not only at the start.** Another chat can open or take over the board while you are working, and a board that had zero hits at boot can have one -- someone else's -- by the time you go to update it.

**Never trust a board's row for a day that board's session did not write.** A board is one chat's snapshot, not the plan's state. The files on disk beat it, exactly as landed text beats the plan.

### ⛔ 2b -- Check the slot gates, and report their absence as a finding

Added 10 Sep 2026, after he called the drift himself: *"we've drifted from what we said was going to be the rule."* **Tuesday and Saturday are VARIATIONS, not spine days**, and both had collapsed into the weekday spine before anyone noticed -- because a per-piece chat only ever sees one day, so nothing in the pipeline was looking across slots.

```bash
grep -n "TUESDAY GATE\|SATURDAY GATE" References/week-plan_<Monday>.md
```

Every plan must carry both lines, PASS or FAIL with a one-line reason. **A missing line is itself a FAIL** -- it means nobody ran the check. Report it in the boot table, in one line, as a finding about the plan rather than about the day.

**And when the day being worked is a Tuesday or a Saturday, run the gate yourself against the block as written, even if the plan says PASS.** `SLOT_CHARTER.md` carries the full tests. In short:

- **Tuesday is the breath.** It must read as a **different KIND of thing** from Mon/Wed/Thu/Fri: lighter, a different vein, organized around what it does for you and what the implications are. Automatic fail -- a thread string matching an adjacent weekday; a regulator, vendor policy, breach or filing as the subject; "here's the news and here's what it means"; a third consecutive Tuesday on one sub-thread; or no one-line answer to what a reader would DO differently.
- **Saturday is what it does for you.** It must name **one solid human feature or shared human feature** in a single line -- a family bot, a control plane, a tool at a price, a thing he built, a thing a reader can have. Automatic fail -- a body of studies or statistics; a company's incident, filing or policy as the subject; an action that is an audit, inventory or self-assessment rather than something to build, install or try; or a piece heavier than the weekdays around it. **Saturday does not have to tie to the week's arc.** Draw a line if one is there; if not, that is fine and is not a defect.

**A gate FAIL never blocks him.** It is a call-out you owe him before he spends a session drafting: say it, propose the re-pitch, and pull from **the charter's Saturday bench** rather than from the week's research leftovers. Leftovers are all weekday-shaped, and reaching for them is the entire mechanism of the drift.

## Step 3 -- Show him the week, then ask

Render the week as a compact table from the status board and the folder listings -- day, title, state, panel score, folder -- then ask which day he is working. Offer, via `AskUserQuestion`: the next day with no piece yet (recommended), the day after, an existing draft that is waiting on him, and let "Other" carry anything else. **If he already named the day in his opening message, do not ask which day** -- dispatch straight to Step 4 and ask what he wants DONE with that day instead.

With the table, give him about ten lines covering:

- what the plan says that day's piece is;
- **the gate result, when the day is a Tuesday or a Saturday**, and whether you agree with the plan's own call;
- **what has changed under the plan since it was written** -- landed text beats the plan, always -- **including what the newest brief (Step 2, item 6) and the inbox (item 7) offer for this day**;
- what is already spent in the seven-day window and cannot be reused today: controlling images, analogy setup frames, action moves, section headers, registers, closes, and any categorical bans the plan's metaphor-debt section carries;
- what you need from him before you can start.

**`Substack Scheduled\` beats the plan.** Where they disagree, what is scheduled is fact and the plan is stale -- say so rather than drafting to the plan. Past-due Scheduled pieces get reconciled into `Substack Published\`, so a window piece may sit in either folder -- check both before telling him where anything is.

**⚠️ The window moves under you mid-session.** Other chats draft, panel and schedule while you work. On 9 Sep a boot table showed two days as unpanelled drafts and one as undrafted; by the time the piece was written, one was published, one was scheduled at rv8, and the undrafted one had been drafted and delivered -- and that last one produced the session's only real collision. **Re-run the window against the FILES, not against your boot table, before you write and again before you finish.**

**The plan's assigned REGISTER is a hypothesis, not a given.** It was written before the week ran, and every day that lands slightly off-plan moves the registers still available. If the days since have spent it, say so and propose the amendment. That is a finding to bring him, not a deviation to hide.

**If another chat already owns a day**, say so and do not start a second draft of it. A day marked as being drafted elsewhere is that session's, and its progress is not tracked from here.

## Step 4 -- Dispatch

**⛔ VOICE FILES LOAD BEFORE ANY WRITING (his question of 24 Sep 2026: "why was the voice so erratic? you have a crap ton of voice references for me, why were they not in play?").** The answer: nothing in this skill loaded them. The rubric loaded only at the panel, so every drafter paragraph was written blind, and the panel then marked the piece down for reading like two writers. Before `draft it`, before `read my rvN` whenever you will write any bridging or replacement text, and before proposing any wording to him, load:

- project memory `feedback_lars_writing_voice.md` (the live rubric; the `Writing Flow\` copy lags it);
- project memory `feedback_lars_contractions.md` and `feedback_lars_absolutes.md`;
- `reference_mds\lars-about-me.md` (taste profile: voice fingerprint, phrase bank, golden examples), applied silently;
- the **last two published pieces he edited heavily**, from `Substack Published\`, read as live voice samples. The rubric is retrospective, and his newest published text is the most current calibration there is.

Draft in his register from the first line: conversational, first person where he has a stake, analogy before argument, jargon glossed inline, no contractions in your own expository prose (direct address may carry them), no self-narrating signposts ("I would rather X than Y", "that is the whole piece"). A drafter paragraph that reads like a report is a defect you created, not one the panel should have to find.

Then one of these, loading only what it needs:

- **`draft it`** -- write v1 from the plan and the research notes, **ending with the standing footer written out in full (see House rules; never the `[STANDING FOOTER]` placeholder)**, save as `substack_draft_<slug>_<date>.md`, stop. **Delivery is RED and needs his word** -- do not email or Slack it unasked. Do not panel unasked. (When he does ask for a Slack drop, the standing destination is `#heinlein-out`, never his self-DM, and it is not a question to re-ask.)
- **`read my rvN`** -- his edit is on disk. Report what his pass added; flag what needs his ruling (unfooted claims, absolutes, named attributions, window collisions); apply mechanics silently as the next `-rvN`; propose word and tone changes rather than making them. Panel only if he says so.
- **`panel it`** -- run the six-seat panel (the `editor-panel` skill) against the window. **Run it as a subagent with file paths, not by pasting texts into the main context** -- that is what keeps a per-piece chat viable. Report scores, stop short of Scheduled. **Relay the report to him in plain English, every item labelled praise or criticism**; he should never have to ask which an item was.
- **`research pass`** -- the `research-assistant` skill. Foot every claim at a primary before drafting; write `References\research_<slug>_<date>.md`; mark anything unreached as unreached rather than guessing.
- **`schedule it`** -- only on his explicit word. **Footer gate first:** `grep -c "Thanks for reading" <file>` must be 1 and `grep -c "STANDING FOOTER" <file>` must be 0. If the footer is missing or still a placeholder, write it in (the "Today's argument" line is drafter text: show it to him) before the copy, and say so. Then copy to `Substack Scheduled\substack_scheduled_<slug>_<date>.md` with a status header recording the panel result, his rulings and the accuracy catches; add the index row; update the status board.

**A perishability re-check comes before any of these when the day already has a draft written more than a few days ago.** A draft can be killed by what landed after it was written -- a payload since published, an argument shape spent by a later piece -- and none of that is visible from the draft itself. Run it before touching a word.

The window for cross-piece checks is **seven days in both directions** -- the pieces in `Substack Scheduled\` and `Substack Published\` dated within seven days of the piece being written, plus any drafts already written for the days after it. Those files are ground truth for metaphor bleed, machinery bleed, register bleed, header repetition and the closes check.

**Before renewing a bench item, read it against `Substack Published\`, not just against the current week.** A bench thesis that "survives on merit" at every review may only be surviving because nobody re-read what already ran. One survived five reviews and turned out to have been printed four times, and refuted once, in his own published text.

## What a fresh session must never assume

- **That the plan is right.** It is a starting position. Pieces that have landed beat it, and a research pass that breaks the plan's thesis is a finding, not a problem to route around.
- **That the SLOT is right.** A plan can assign a weekday-shaped piece to Tuesday or Saturday and nothing downstream will catch it -- the panel checks form and accuracy, never whether the piece belongs in its slot. See 2b. On 9 Sep he caught one himself at boot, which is one chat too late.
- **That the status board is complete or current.** It is whatever the last chat knew. Check it against the folders. See 2a.
- **That a day is undrafted because you did not see a file.** List the folder properly, filtered by date, and check. See Step 1.
- **That the week is as it was at boot.** Other chats move it under you. Re-run the window against the files before you write.
- **That a handoff's file inventory is current.** He often carries files across by hand between sessions. List the folders before acting on a handoff that says something did not reach disk.
- **That a piece is ready to move.** Moving to `Substack Scheduled\` needs his word, every time.
- **That anything may be published.** He pushes to Substack himself. Always. (RED.)
- **That his text needs improving.** His edits are the voice ground truth. Mechanics are fixed silently; word and tone changes are proposed, not made. Do not sand down his rough edges -- the rolling comma-spliced sentences are his register, not errors.
- **That an absence is a fact.** A negative from a fetch of a long page (Hansard, legislation, court records) is not evidence of absence -- those are silently truncated in transit. Re-run against a structured API or search index, or record it as unreached. Never write "nobody has said this" from a failed search.
- **That he has not already sent you the source.** Check #heinlein-inbox and the intake notes (Step 2, item 7) before telling him anything is still his to find.

## House rules that must survive a cold start

- **No em-dashes, ever.** `--` only. **Contractions (ruled 25 Sep 2026):** the drafter writes none in expository prose; **nobody ever expands a contraction he wrote, in any register** (see `feedback_lars_contractions.md`). His stance markers, emphasis, lead-ins, appended clauses, nicknames and extended closes are his and are never stripped -- the 25 Sep section of `feedback_lars_writing_voice.md` has the full list. US spelling. Two-declarative opener, analogy-first, problem-before-fix, bold lead-in action sections, two-paragraph close, standing footer.
- **⛔ STANDING FOOTER, written out in full on every piece (rule since 12 Aug 2026; enforced 27 Sep 2026 on his word: "please make sure the writing skill always puts the footer in there").** After the closing `---`, every draft from v1 onward ends with:

```
*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about AI governance (often), AI methodologies (also often), cybersecurity strategy (sometimes), and technology risk (always). Today's argument is that <one sentence, specific to THIS piece>.*
```

  The first line is fixed, verbatim. The second line's opening is fixed; the "Today's argument is that..." clause is written fresh for each piece in one sentence (drafter text, his to change). **Never write the literal placeholder `[STANDING FOOTER]`** -- the headless drafters did, Fri 25 *Adoption Speed, Control Speed* was published with only the placeholder, and Mon 28 reached Scheduled with it. Saturday Diversions carry the same footer until he settles a lighter variant; do not invent one. When revising, keep the footer in every rvN, and update the argument line if the thesis moved.
- **Length is a guidepost, never a gate (his rulings, 10 and 24 Sep 2026).** The weekday target is about 2,750 words, and he does not want length pressed below 5,000 on anything but a Saturday Diversion. Capstones may run to 7,000.
- **Saturday is measured by whether it feels lighter and whether the reader gains something, never by word count.** Lightness is a state of being, not a length metric.
- **Saturday format:** sample prompts in the body, the fuller set as an addendum at the end.
- `[VERIFY]` never ships. `[YOUR TAKE]` is never fabricated -- it is his to fill. **A "fill it or cut it" choice on his slot defaults to keeping the slot open**, even under a blanket "accept all suggestions".
- Regulatory claims need a primary. Name the commercial interest in the text.
- Absolutes are a voice defect, and the fix is SPECIFICITY, not hedging.
- A research note's DO-NOT-PRINT list binds every later revision of that piece, not just the first draft -- **unless he rules otherwise; record the ruling in the note.**
- **A killed claim can have been wrongly killed.** Absence-kills are provisional and nobody re-tests them, because skepticism reads as rigour. Re-test before treating one as settled, and narrow an over-broad kill rather than defending it whole.
- **Pasted AI-search summaries are leads, not sources.** Verify each attribution at the cited page before it is printed.
- Correct forward in public; never edit a published piece in place.
- Filenames: `substack_draft_<slug>_<date>-rvN.md` (hyphen before `rv`), `substack_scheduled_<slug>_<date>.md`.
- Do not route around a robots block with curl. Use a browser, or record the source as unreached. After a browser navigation, re-read once before trusting the extraction -- the first read can return the previous page's text under the new URL. **x.com IS reachable via `firecrawl_scrape`**, despite older research notes recording it as blocked.

## Before the session ends

**Update the live plan's status board -- the existing one, in place.** It is the next chat's memory, and the only thing standing between one-chat-per-piece and amnesia.

> **One board per plan. Edit it; never append a second.** If you think the plan has no board, grep first (2a) -- and grep AGAIN before writing, because another chat may have opened one while you worked. "The plan had no board, this is it" is how the 5 Sep collision happened.

The board should say: every day's state and panel score, where each file sits, what his rulings were, what was caught and closed, what is carried on purpose, what another chat owns, and what is blocked on him. **Only edit rows for days this session actually touched** -- leave another chat's rows alone rather than overwriting them from stale knowledge, and if you must correct one, check the folder first and say what you corrected.

When he closes a call, write the decision AND the reasoning into the plan, so it is not re-opened on merit by a session that only sees the entry. A retired piece gets a why. **A gate overrule gets a why too.**

Before moving anything to Scheduled, run the footer gate (Step 4, `schedule it`). If the day's piece moved to Scheduled, also add its `SUBSTACK_INDEX.md` row (newest first) and flip the board's row for that day.