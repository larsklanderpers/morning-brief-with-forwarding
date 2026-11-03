---
name: final-review-pangram
description: "Stage 4 of the writing flow — Pangram AI-detection pass; POST-sign-off measurement only, threshold, Chrome-vs-API, and the check-back"
type: project
sources: [cowork-import]
imported_at: 2026-09-15T13:26:34Z
---

Lars added a **final-review** stage (stage 4) to the writing flow on 20 Jul 2026 and, on 21 Jul 2026, **moved it to run AFTER his sign-off** as a measurement only. Skill file: `Writing Flow\04_final-review.SKILL.md`. Feasibility write-up: `Writing Flow\final-review_pangram_research_2026-07-20.md`.

## The decisions (his calibration)
- **Runs POST-sign-off, on the exact text Lars approved.** Never on a pre-sign-off draft.
- **Measurement only — it never edits, never gates, never loops, and does NOT feed the AI-Slop Allergist.** The detector is fully decoupled from the writing. Reason: if a Pangram score could drive edits before sign-off, it would push the prose toward beating a detector instead of toward his voice. He'd rather ship a rough edge that's his than an overpolished piece that isn't. Running it after the gate gives a clean measurement of what he actually approved AND an uncontaminated dataset (no editing-to-the-test) for the threshold review.
- **It measures provenance, not voice.** "Was a machine involved" ≠ "sounds like Lars." His drafts are Claude-assisted by design, so **AI-Assisted / AI labels are expected and fine — never a voice judgment.**
- **75% is an annotation, not a gate.** Log every score. ≤75% = record and move on. >75% = record AND drop Lars a **post-hoc, his-call** heads-up ("came in at NN%, want to look?") — still no block, no auto-revise. Provisional line; revisit ~**3 Aug 2026**.
- **Output = two writes, no body edits:** (a) stamp a compact Pangram line into the scheduled file's **header, alongside the references**, at the draft→scheduled stage move; (b) append the run to `References\final-review_<slug>_<date>.md`.

## The AI-Slop Allergist is separate (21 Jul 2026)
Editor-panel Seat 5 stays in the pre-sign-off loop but runs on **its own tells only — no Pangram input.** De-slopping (killing "not-just-X", tricolons, "delve/leverage", em-dashes, symmetry sheen) is voice-positive: it removes machine residue, making the piece *more* like Lars. That's independent of the detector by design.

## Overpolish guard on the 9.0 bar (same conversation)
The raised 9.0 editor-panel bar is a bar on **voice-truth and substance, not polish.** Intentional rough edges that serve his voice score a 10 on voice-fidelity and are never "corrected"; the loop stops once voice-fidelity + slop are maxed, even if a tightening seat could smooth further. Logged in [[writing-flow]] and `03_editor-panel.SKILL.md`. This is Lars's explicit priority: rough-but-his > smooth-but-generic.

## Chrome-first, API as upgrade
- **Runs via Claude-in-Chrome against pangram.com today.** The Pangram API is egress-blocked in the cloud session (tested 20 Jul: all `pangram.com` domains reset at Anthropic's egress gateway; GitHub/PyPI pass). `device_bash` has no network either. Needs `pangram.com` allowed once in the Chrome extension's site permissions. Free tier = 4 checks/day (1 credit per ~1,000 words).
- **Escalate to the Pangram API only if Chrome proves insufficient.** `pip install pangram-sdk`; `predict_sliding_window` gives per-window scores + offsets; ~$0.05/1,000 words (~$0.10/piece). Requires `text.external-api.pangram.com` allowlisted for egress (org Owner setting, Admin → Capabilities — may not exist on his plan) + a `PANGRAM_API_KEY` (env var / git-ignored, **never committed, never in memory**). Same rules regardless of transport.

## The check-back (scheduled)
A scheduled task (trig_01AEVyiEUtQUufU4mKY2oV4z) fires **3 Aug 2026** to review: how many pieces came in over 75% over the two weeks, is the Chrome path reliable enough or do we need the API, and should the 75% line move. Sources: `References\final-review_*.md` logs + the header stamps + this note.
