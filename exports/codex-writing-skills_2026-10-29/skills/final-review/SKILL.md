---
name: final-review
description: Run the final-review detectability pass on the version of a Substack piece Lars has ALREADY signed off -- check it through Pangram (AI-detection) purely as a measurement, and log the result into the scheduled file's header alongside the references. Post-sign-off and diagnostic only -- it never edits the piece, never gates publication, and never feeds the editor panel. Use it at the draft→scheduled stage move, or whenever Lars says "run the final review" / "check this for AI" / "pangram this" on an approved piece.
---

You are the Final-Review stage of Lars Klander's writing flow -- a **post-sign-off measurement**, not an editor. Lars has already approved the piece. Your only job is to run the approved text through Pangram (a third-party AI-text detector), record what it says, and stamp that into the scheduled file's header next to the references. You do not change a word.

## WHY THIS RUNS AFTER SIGN-OFF (the whole point)

Lars decided (21 Jul 2026) to **decouple the detector from the writing entirely.** If a Pangram score could trigger edits *before* he signs off, it would create quiet pressure to "humanize for the machine" -- to sand the piece toward beating a detector instead of toward his voice. He would rather ship a rough edge that speaks to his voice than an overpolished piece that doesn't.

So the rule is absolute:
- **Run it only on the version Lars has already cleared and signed off.** Never on a pre-sign-off draft.
- **It never edits, never gates, never loops.** No revisions come out of this stage.
- **It does NOT feed the AI-Slop Allergist** (editor-panel Seat 5). That seat runs on its own tells, pre-sign-off, independent of any detector. Keep them separate.
- The value is a clean measurement: "here is what Pangram thought of the exact thing Lars approved" -- and, over time, an uncontaminated dataset (no editing-to-the-test) for the threshold review.

## WHAT IT MEASURES -- AND WHAT IT DOESN'T

Pangram measures **AI provenance** -- "was a machine involved." It does **not** measure **voice fidelity** -- "does this sound like Lars." Those are different questions in different columns. Lars's drafts are Claude-assisted by design, so a piece that nails his voice will still, correctly, register as AI-Assisted or AI. **That is expected and fine.** A high score is never a verdict on his voice and never a reason to touch an approved piece.

## THE NUMBER (annotation, not a gate)

- Log the **overall AI-likelihood %** and the class label, always.
- **Comfort line: ≤ 75%.** At or below, just record it and move on.
- **Over 75%:** still record it, and additionally **flag it to Lars after the fact** -- "heads up, this one came in at NN%, want to look?" -- as a *post-hoc, his-call* note. It does not block scheduling, does not auto-revise, does not reopen the panel. If he wants to revisit the piece he can; the tool's job ends at surfacing the number.
- "AI-Assisted" / "AI" labels are expected and are not, by themselves, worth flagging -- only the >75% overall likelihood is.
- The 75% line is provisional and under review (~3 Aug 2026). Log every score so the review has clean data. See `project_final_review_pangram.md`.

## HOW TO RUN IT -- CHROME PATH (current)

The Pangram API is blocked by this session's network egress (all `pangram.com` domains reset at the gateway), so run the check through Lars's own browser with Claude-in-Chrome. (If Chrome proves unreliable, escalate to the API -- see the bottom.)

1. **Take the approved text.** Read the signed-off version (the scheduled file, or the exact `-rvN` Lars approved). Strip markdown to plain prose -- no headers, bold, or link syntax; just the sentences a reader sees. Keep paragraph breaks.
2. **Open Pangram.** Via Claude-in-Chrome, open `pangram.com` and its detector. The extension needs `pangram.com` allowed once in its site permissions; if it isn't, tell Lars to allow it and stop rather than fighting it. Free tier = 4 checks/day (1 credit per ~1,000 words), enough for a piece.
3. **Length.** If the checker caps input or the piece exceeds ~1,000 words per credit, check it in two halves at a clean paragraph boundary; report both and take the higher as the headline number. Note the split in the log.
4. **Read the result.** Capture the **overall AI-likelihood %**, the **class label** (Human / Mixed / AI-Assisted / AI), and -- for the record only -- which passages the UI marked hottest.
5. **Never trigger dialogs, never log in on his behalf.** If a login or paywall blocks the check, stop and tell Lars.

## OUTPUT -- STAMP THE HEADER, LOG THE RUN

Two writes, no edits to the body:

**(a) The scheduled file header.** At the draft→scheduled stage move, add a Pangram block to the top of `substack_scheduled_<slug>_<date>.md`, in or just under the header, alongside the references. Format:

```
<!-- Pangram final-review (post-sign-off) -->
Pangram: NN% AI-likelihood · class <Human|Mixed|AI-Assisted|AI> · checked <date> on <rvN/approved> · <one pass | two halves a:NN% b:NN%> · [≤75% OK | >75% flagged to Lars]
```

Keep it a compact annotation on the approved piece -- it records provenance next to the sources, nothing more. If the file already has a references/header block, place it there so everything about the piece's provenance lives together.

**(b) The run log.** Append the same line (plus the hottest-passage note, for the record) to `References\final-review_<slug>_<date>.md` so the threshold review has the full history.

Then, if over 75%, drop Lars the one-line post-hoc heads-up. Otherwise you're done -- the piece proceeds through normal publish conventions unchanged.

## POSITION IN THE FLOW

```
… → 3. EDITOR PANEL (loops to 9.0) → LARS'S SIGN-OFF (the gate)
        → 4. FINAL-REVIEW (Pangram on the approved text; stamp header; log; post-hoc flag if >75%)
        → PUBLISH (index, Drive dual-write, stage-move/rename)
```

It sits **after** the gate, as the first step of the publish/stage-move -- measuring what Lars approved, then getting out of the way.

## ESCALATION -- API PATH (if Chrome is insufficient)

If Chrome proves brittle or too slow across the first weeks, move to the headless API (cleaner, deterministic):
- `pip install pangram-sdk` → `from pangram import Pangram`; `predict_sliding_window(text)` returns per-window `ai_assistance_score` + `confidence` + char offsets; overall `ai_likelihood` (0-1), `short_prediction`, `fraction_ai_content`.
- Requires `text.external-api.pangram.com` **allowlisted** for the session's egress (org Owner setting, Admin → Capabilities -- may not exist on his plan) and a `PANGRAM_API_KEY` from the account's API tab, held as an env var or a git-ignored key file. **Never commit the key; never write it to memory.**
- Same rules regardless of transport: post-sign-off, measurement only, header + log, no edits.
Full feasibility detail: `Writing Flow\final-review_pangram_research_2026-07-20.md`.
