---
name: "week-plan"
description: "Draft the coming week's Substack plan: derive the live Monday, read the charter and last week's board, run the Tuesday and Saturday gates, sweep the spent window, and write an unsigned plan with one status board. Use on \"draft the week plan\", \"plan next week\", or when day-start finds no plan for the week."
---

# Week Plan

This writes the plan. `day-start` boots a per-piece chat against a plan that already exists; when it
reports that no plan covers the week, this is what runs next.

**The plan is a proposal, always.** It is written to disk as v0.1 PROPOSED, unsigned, with nothing
drafted. This skill never drafts a piece, never panels, never schedules, never moves a file between
stages, and never marks a day done. Those need his word, every time.

Project root on his machine: `D:\vc-personal-projects\Morning Brief with Forwarding\`. Prefer
`device_bash` (ground truth). If the mount fails, fall back to `device_list_dir` / `device_stage_files`.

---

## THE MAP -- every plan is written to it and checked against it (his ruling, 28 Sep 2026)

**Source of truth: `References\SLOT_CHARTER.md` §1.1.** It is copied here so the skill cannot be run
without it. **If the charter and this table ever differ, the charter wins; say so in the report and flag
this skill as stale.** Effective the week of Monday 5 October 2026, until the 26 October review.

| Day | Slot | Formula |
|---|---|---|
| **Mon** | **Quiet: one Substack Note, standalone.** No piece. | One Note that stands on its own. May draw a line from Sunday's capstone; it is not a newsletter drop. |
| **Tue** | **Management** | Challenge named fully, then a proposal (what a manager would do differently), then something usable today: sample prompt(s) in the body, fuller toolkit as an addendum. |
| **Wed** | **Cyber -- OPENS THE ARC** | Two-declarative opener, analogy first, problem before fix, **2-3 points**. States the week's arc. |
| **Thu** | **AI growth** | The least dry weekday; allowed to land up. **2-3 points.** Feeds Sunday. |
| **Fri** | **Commercial** | What it costs and who pays. **2-3 points.** Sets up Sunday. |
| **Sat** | **Personal** | Something I did that you can do: one named human feature, prompts in the body, fuller set as an addendum. Need not tie to the arc. |
| **Sun** | **Capstone** | Merges Wed-Fri into one argument, not a summary of three. The long one. |

"2-3 points" is the spine's formula, not a word count. Length is always his call.

---

## Step 1 -- Derive the week, and never hardcode a filename

```bash
cd "$HOME/mnt/Morning Brief with Forwarding"
date +"%F %A"
ls -1 References/week-plan_*.md
D=<the target date>; date -d "$D -$(( $(date -d "$D" +%u) - 1 )) days" +%F   # its Monday
```

Plans are `References\week-plan_YYYY-MM-DD.md`, dated to the **Monday** of the week they cover. If a
plan for that Monday already exists, stop and read it -- amend it, do not write a second.

**List folders by DATE, never by position.** `head`/`tail` on an alphabetical listing hides whole pages
and has produced a wrong week picture that reached him in a table.

```bash
ls -1 "Substack Drafts" | grep -E "<date regex for the window>"
ls -1 "Substack Scheduled" "Substack Published"
```

## Step 2 -- Read, in this order

1. `CLAUDE.md` -- the working agreement, GREEN/AMBER/RED, standing accuracy rules.
2. **`References\SLOT_CHARTER.md`** -- what each day is FOR, **§1.1 the map first**. It governs the plan,
   never the reverse.
3. **The previous plan's status board, its rulings, and its carried-forward sections.** The rulings and
   their reasoning migrate forward; a decision closed on merit must not be re-opened by a later chat
   that only sees the entry.
4. **`References\IDEA_BANK.md`** -- the one bench for Tuesday and Saturday. Pull from it FIRST for both
   slots, before the week's research leftovers (leftovers are weekday-shaped; reaching for them is the
   drift mechanism). Mark any entry the plan takes as `TAKEN -> <date>`.
5. `Substack Drafts\SUBSTACK_INDEX.md`, newest few rows.
6. Project memory (`project_memory_read`), for the feedback files bearing on planning: the slot gates,
   metaphor and machinery and register bleed, the spent-payload sweep, affiliation at primary.

## Step 3 -- Establish what is actually true, because the plan you are reading is stale

In order of authority: **files on disk beat the status board; the board beats the plan.**

- Reconcile every day of the closing week against `Substack Drafts\`, `Substack Scheduled\` and
  `Substack Published\`. Rows saying "untouched" for days that have drafts are normal and are a finding.
- A **past-due file still in `Substack Scheduled\`** is published in fact; CLAUDE.md calls for
  reconciling it into `Substack Published\`. Offer it; do not do it silently.
- A piece may sit in Scheduled **or** Published. Check both before saying where anything is.
- Note any day another chat owns, and leave it alone.

## Step 4 -- Read what the published week PROMISED

**This is the step nothing else in the pipeline performs, and it has already claimed a slot.**

```bash
grep -n -i "next week\|next tuesday\|next saturday\|next sunday\|I will\|we will come back\|come back to\|coming week\|from next week" \
  "Substack Published"/*.md "Substack Scheduled"/*.md
```

A promise printed in a published piece is binding on the slot it names and outranks any pitch. Record it
in the day block in the piece's own words, marked as a printed promise. An undated promise ("I will
come back to it") binds no date; list it under open calls so it is not lost.

## Step 5 -- Derive the arc from the capstone's CURRENT revision

Read the newest revision of the closing Sunday capstone, not the plan's description of it and not the
board's summary. His own edit pass is the voice and argument ground truth, and a capstone routinely
supersedes its planned merge.

Then name the new arc as a **different axis**, not the next paragraph of the old one, and write the
continuation risk into the plan as a THESIS RISK with the specific moves that are now spent -- the
closing piece's frame, its controlling image, and any sentence it printed that the new arc would restate.

**The arc now opens on WEDNESDAY and runs on three spine days.** Write it as: the one-line arc; the 2-3
points Wednesday opens with; what Thursday adds; what Friday adds; and the single argument Sunday merges
them into. If the three spine days cannot each name their own points, the arc is too thin -- say so.

**If a day's research cannot foot the arc's central claim, the arc is wrong.** Say so; do not pad it.

## Step 6 -- Write each day block, to the map

One block per map row. Every piece block carries, and no block is finished without them:

- **Map row:** the slot and formula, copied from the map, so the block is written against it.
- **Thesis**, in one or two lines.
- **Points (spine days): the 2-3 points, named.** Not a list of everything the research found.
- **Storyline role:** opens the arc / feeds Sunday with point X / merges / independent (Tue, Sat).
- **Footing status** -- footed at primaries, footed at secondaries only, or none. Name the research note.
- **THESIS RISK: LOW / MEDIUM / HIGH**, with the sentence that has to survive contact.
- **DO NOT** -- what an adjacent day owns, and what the closing week spent.
- **[YOUR TAKE]** where the piece needs what only he has. Never fabricated.

**Monday's block is a Note, not a piece:** one line on what the Note is about (it may draw from Sunday's
capstone), no thesis, no research, no gate. It is drafted with the `substack-notes` skill on the day.

## Step 6a -- The slot guidelines each block must carry

The gates in Step 7 are tests. These are the intent behind them, and a block written without them
passes its gate and still comes out wrong. **Three spine days (Wed-Fri) feed Sunday; Tuesday and
Saturday are VARIATIONS and are not required to.**

**Tuesday is management** (charter §2.1, extended through December 2026). His register: *"Here's how
I've changed the way I manage. Here's how you could use that in your business."* Three parts, every
time: the challenge, named fully; a proposal, what a manager would do differently; something usable
today (prompts, a template or a worked example; sample in the body, fuller set as an addendum). A
Tuesday with no part 3 fails. It must name, in one line, what a manager would DO differently on
Tuesday afternoon. His first-person practice is his: leave `[YOUR TAKE]`. Model-agnostic by default.

**Thursday is the least dry of the spine days, by construction, and the block says so.** AI growth is
the beat; the instruction is that it is written that way rather than as the week's driest filing.
A Thursday block that reads like Wednesday with different nouns has lost the point of the slot.

**Saturday is what it does for you** -- concrete, hands-on, warm, something he is actually doing written
up so a reader can do it too, at a named price, with the prompts. His register: *"Here's something I
did that you can do."* Three things belong in every Saturday block:

- **Format:** sample prompts **in the body**, the fuller set as an **addendum at the end**.
- **Lightness is the test, never length.** Lightness is a state of being, not a length metric, and
  length is always his call. Do not flag it.
- **Saturday does not have to tie to the week's arc.** His explicit ruling: draw a line if one is there,
  and if not, that is fine and is not a defect. A Saturday bent to serve the arc has usually stopped
  being a Saturday.

**Repetition rule (his ruling, 27 Sep 2026):** on Tuesday, Thursday and Sunday a repeated TOPIC is fine
as long as the CONTENT is unique. Same-sub-thread and consecutive-topic signals are advisories on those
days, not fails. Repeated content (the same exhibit, statistic, argument, analogy, action or close) still
fails everywhere.

**Tier 0 bookending, adopted 23 Aug 2026, applies to Tuesday and Saturday pieces that hand the
reader a skill.** One clause, early in the piece, naming the previous entry and the skill it handed
over. Nothing else. **Explicitly not adopted:** a series name, a marker line, numbering, or an index
post. Do not creep past Tier 0. Devices are seasoning, never a slot to fill.

**When a Saturday is part of a running build**, say which part and what the previous part covered, so
the piece is written as the next instalment rather than as a standalone that repeats the setup.

## Step 7 -- Run both gates, at plan time, in these words

```
TUESDAY GATE: PASS|FAIL -- <one line: the manager's act, and the part-3 toolkit>
SATURDAY GATE: PASS|FAIL -- human feature: <name it in one line, or say there is none>
```

**A missing line is a FAIL**, because it means nobody ran the check. The full tests are in the charter;
in short: Tuesday fails on no manager's act, no part 3, org-theory with no act, or "here is the news and
here is what it means". Saturday must name one solid human feature (automatic fail: a body of studies; a
company's incident or filing; an action that is an audit or self-assessment rather than something to
build, install or try; or a piece heavier than the weekdays around it).

**A FAIL never blocks him.** It is a call-out plus a re-pitch, drawn from **`References\IDEA_BANK.md`**,
never from the week's research leftovers.

**When he overrules a gate, record the overrule, his words, and the reasoning**, so no later seat
re-litigates it on merit. Then write the boundary: if two days now share a subject, each block states
what belongs to it and what belongs to the other.

## Step 7a -- MAP CHECK: line the week up against the map, row by row

**His instruction, 28 Sep: "make sure that when we get the week plan back, that we look exactly at these
items and that the story lines up against them."** Write this table into the plan, directly under the
arc, and put it FIRST in the report to him:

```
MAP CHECK
| Day | Map slot | This week's piece | Formula met? | Storyline role | Verdict |
```

For each row, test the block against the map's formula, not against the idea:

- **Mon:** a Note only. Any piece scheduled on a Monday is a FAIL.
- **Tue:** all three parts present, a one-line manager's act, not a Monday/Wednesday exhibit.
- **Wed:** it OPENS the arc -- the arc is stated here -- and names its 2-3 points.
- **Thu / Fri:** each names its own 2-3 points, none borrowed from another spine day, and says what it
  hands Sunday. Thursday is marked least dry.
- **Sat:** one named human feature; prompts in body plus addendum.
- **Sun:** names the single argument that merges Wed-Fri, and which point from each day it uses.

**Then the storyline test, in one paragraph under the table:** read Wed -> Thu -> Fri -> Sun as one
argument. Does each spine day advance it, does any two days make the same point, and does Sunday
merge rather than recap? A spine day that could be deleted without Sunday noticing is a FAIL.

Verdict per row is PASS or FAIL with one line. **A FAIL is a call-out with a proposed fix, never a
block.** Record his overrules with his words.

## Step 8 -- Sweep what is spent, seven days back

Read the headers of everything scheduled and published in the window, and list in the plan:

- **controlling images** (and which day owns each)
- **closes**, including any close form at three uses and therefore banned
- **action machinery** -- the verbs of the do-this sections
- **header forms at saturation**
- **saturated phrases**
- **standing DO-NOT-PRINT items** inherited from the window's research notes and scheduled headers

A collision can be pure syntax -- the same sentence shape with different nouns is still a collision.

## Step 9 -- Commission research, in priority order

Rank by what blocks a draft soonest, not by day order. **Tuesday ranks first** (it is now the first
piece of the week and is usually drafted Monday), then Wednesday, since Wednesday opens the arc. Name,
per item, the primaries to reach. A subject with **zero corpus** is flagged as such -- check it with a
corpus grep rather than assuming.

## Step 10 -- Open calls, then write the file

List what is blocked on him, each as a decision rather than a status. Then write
`References\week-plan_<Monday>.md`:

- version line (`v0.1 PROPOSED, <date>. Not locked, not signed off. Nothing here is drafted.`)
- the arc and its thesis risk · **the MAP CHECK table and storyline paragraph** · the day blocks (Monday
  as a Note line) with both gate lines · research order · open calls · the spent-window list
- **one status board at the end**, every row `Planned` / `Untouched`, plus a short carried-forward section
  for rulings from the closing plan that must not be lost

**Length discipline:** map check, day blocks, gates, risks, spent window, open calls, nothing else.
Session findings go on the board. Keep the plan near 15 KB.

**House mechanics:** no em-dashes, `--` only. US spelling. No contractions in the plan's own expository
prose, since the plan is drafter text -- but **never expand a contraction inside a quotation of his
words**, in any register. Quote him exactly as he wrote it.

## Step 11 -- Verify before reporting

```bash
grep -n "TUESDAY GATE\|SATURDAY GATE" References/week-plan_<Monday>.md
grep -c "MAP CHECK" References/week-plan_<Monday>.md          # must be at least 1
grep -c "STATUS BOARD" References/week-plan_<Monday>.md       # must be exactly 1
```

Re-list the folders and confirm every spent-window and stage claim against the files, re-grep for a
second board (another chat may have opened one while you worked), and check that no em-dash reached the
body and no quotation of his was silently altered. **Never edit another chat's rows in the closing
plan**; if the closing plan is being actively edited, leave it alone and say so.

**Report to him in this order:** the MAP CHECK table; the storyline paragraph; the two gate lines; the
open calls. Plain English, each finding labelled as a pass or a problem.

## What this skill must never assume

- **That the previous plan is right.** It is a starting position; landed text beats it.
- **That the board is current.** It is whatever the last chat knew.
- **That a day is undrafted because no file was seen.** Filter the listing by date and check.
- **That a slot is free.** A published piece may have promised it.
- **That an absence is a fact.** A robots block or a failed fetch is unreached, not absent.
- **That a variation must serve the arc.** Saturday is independent by his ruling, and Tuesday runs on
  its own axis.
- **That the map in this file is current.** The charter's §1.1 is; check it every run.
- **That the plan may commit anything.** Drafting, panelling, scheduling, publishing and deleting all
  need his word.