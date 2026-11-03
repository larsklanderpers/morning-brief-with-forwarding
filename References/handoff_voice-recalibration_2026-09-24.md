# HANDOFF: Voice recalibration, from the 24 Sep 2026 Fri 25 session

**Open the new session with:** "Read References\handoff_voice-recalibration_2026-09-24.md and run it."
**Do NOT run day-start first.** This session is not a per-piece chat.

## Why this exists
His question of 24 Sep: *"why was the voice so erratic? you have a crap ton of voice references for me, why were they not in play? ... do we need to run an update on it now that we have 3 months of essays in?"*

The diagnosis had two causes:
1. **The references were never loaded at drafting time.** day-start's `draft it` loaded no voice files; they were loaded only at the panel. The drafter paragraphs were written blind and read like a report, so the panel scored "two writers". This is fixed going forward in a day-start skill card; check that he saved it.
2. **The references are stale.**
   - `Writing Flow\feedback_lars_writing_voice.md` is dated 12 Aug.
   - `reference_mds\lars-about-me.md` is dated 12 Aug.
   - The project-memory rubric is a 15 Sep import of the same era.
   - `feedback_lars_contractions.md` exists ONLY in project memory, not on disk.
   - **38 pieces have been published since 12 Aug**, and none of them have been folded in.

## The job
**1. Build the pairs.** For each piece in `Substack Published\` dated from 12 Aug onward (38 files), find:
   - the last DRAFTER-ONLY revision in `Substack Drafts\` (the version before his first edit pass; the STATUS headers say which rvN was his);
   - the published final.

   Skip a pair where provenance is unclear, and list the skips.

**2. Diff each pair.** Fan out with subagents, about 8 pieces each, and pass them file paths only. For each piece, extract what HE changed:
   - what he adds (first-person stakes, asides, analogies, glosses);
   - what he cuts;
   - what he rephrases, and into what;
   - sentence shape, openers, closes, and headers he writes or renames;
   - contractions by location (direct address vs. exposition);
   - dashes and emphasis habits;
   - words and phrases he reaches for, and ones he removes.

   Quote examples verbatim, with file and line.

**3. Aggregate.** Only a pattern seen in **3 or more pieces** becomes a candidate rule. Tag each candidate NEW, CONFIRMS or CONTRADICTS against the current rubric.
   - A CONTRADICTS finding is the most valuable kind. Flag it prominently.
   - Watch the 23-24 Sep examples: his register rewrite of drafter sections in `substack_draft_adoption-speed-control-speed_2026-09-25-rv17.md` (compare with rv16). This is the cleanest before/after pair available, because it is his rewrite of drafter text on purpose.

**4. Propose, do not apply.** Give him a short list: each rule in one line, with two or three quoted examples. **He approves or vetoes each one.** Nothing is written until he rules.

**5. On his approval, write to ALL copies** (they drift, five times so far):
   - project memory: `feedback_lars_writing_voice.md` (the live one), `feedback_lars_contractions.md`, `feedback_lars_absolutes.md`;
   - disk: `Writing Flow\feedback_lars_writing_voice.md`, plus a new `Writing Flow\feedback_lars_contractions.md`;
   - `reference_mds\lars-about-me.md`: phrase bank, golden examples (swap in recent pieces), writing laws;
   - dated entries in `reference_mds\taste-interview-transcript.md` under "## POST-INTERVIEW ACCRETIONS (living log)" (line ~896). Append only, and flag them for his veto.

## House rules that bind this job
- The rubric describes HIS voice. Never "improve" it toward generic good writing. Rough-but-his is the target.
- **Report in plain English, labelling each item as confirmed, new or contradicted.** He found the panel's jargon hard to follow (24 Sep).
- An observed edit is not a rule until it recurs. A single edit may be housekeeping; if in doubt, ask.
- Report what the machinery found. Do not narrate his edits as having "rescued" drafts. His text carrying the piece is the premise.
- No em-dashes; `--` only.

## Also open from the 24 Sep session (not part of this job)
- He needs to save the two skill cards (editor-panel with the 5K length rule and the plain-English reports; day-start with the automatic brief read and the voice files loaded before writing), if he has not already.
- The AI brief header for 23 Sep says "Tuesday"; the 23rd was a Wednesday. There is a weekday bug in the brief generator.
- Sat 26 needs its extraction session. Sun 27 has not been started. The supply-chain cluster is held for next Wednesday.

---

## STATUS: DONE 25 Sep 2026
Steps 1-5 complete. Proposal: `voice-recal_proposal_2026-09-24.md`; evidence: `voice-recal_findings\`. Lars ruled every item 25 Sep (C1 = option c). Written to: project memory voice / contractions / absolutes; `Writing Flow\feedback_lars_writing_voice.md` (now merged with memory, drift closed); new `Writing Flow\feedback_lars_contractions.md`; `reference_mds\lars-about-me.md` (laws, phrase bank, 3 new golden examples); transcript accretions entry (flagged for veto). Panel charter + day-start conflicting contraction/hedge lines patched: disk snapshot `03_editor-panel.SKILL.md` updated; installed skills offered as skill cards (need his save).
