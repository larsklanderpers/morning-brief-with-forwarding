---
name: writing-flow
description: "The interviewer -> research-assistant -> editor-panel -> sign-off -> final-review package layered on the Substack pipeline; installed skills + where files live and how they run"
type: project
sources: [cowork-import]
imported_at: 2026-09-15T13:26:50Z
---

Lars added a writing flow on top of the existing Substack pipeline (20 Jul 2026); a Pangram final-review stage was added 21 Jul 2026 (and that same day repositioned to run POST-sign-off).

## Installed as first-class skills
Packaged and delivered as `.skill` files for one-click install into his profile. Once installed they auto-trigger and can be invoked by name:
- **interviewer** — "interview me on <topic>"
- **research-assistant** — "dig into <X>" / "I don't know enough about <X>"
- **editor-panel** — "run the editor panel on <draft>" / "does this sound like me?" / "is this ready?"
- **final-review** — "run the final review" / "check this for AI" / "run pangram on <draft>" (stage 4, post-sign-off; see [[final-review-pangram]])
- **writing-flow** — orchestrator; "run the writing flow on <piece>" (runs the whole chain)

Source skill folders also on disk at `D:\vc-personal-projects\Morning Brief with Forwarding\Writing Flow\` (00_WRITING_FLOW.md + 01/02/03/04 SKILL files) as the human-readable copy. Built to match his `ai-morning-brief-skill.md` format and voice memory ([[lars-writing-voice]]).

## Memory-source fallback (added 20 Jul 2026)
Every skill loads voice/taste memory notes **memory-first, with an on-disk fallback**: prefer the live project-memory note; if memory isn't available (headless/scheduled run), read the snapshot copy in the `Writing Flow\` folder; memory wins if both differ. A snapshot of `feedback_lars_writing_voice.md` lives in that folder.

## The packages
1. **Interviewer** — author-first, always: Pass 1 mines Lars (skin-in-the-game story, insider "we", the analogy/spine, economics/cost-collapse, reader's-calculus close), Pass 2 interrogates the argument (counterexample, skeptic rebuttal, hidden assumption, so-what). Output: `Substack Drafts\capture_<slug>_<date>.md`, with `[VERIFY]` tags handed to research. Ask in small rounds; capture verbatim; never invent a personal stake; flag his X-sourced stats rather than assuming right/wrong.
2. **Research Assistant** — triggered by "I don't know enough about X" or a `[VERIFY]`. **Search local corpus FIRST** (AI Briefs / Daily Briefs / References / Substack folders — his briefs usually already source the claim), then fan-out web + fetch primaries + adversarial verify. Output: `References\research_<slug>_<date>.md` with solid / contested / couldn't-verify buckets, economics framing, and sourced drop-in facts. Never let unverified pass as verified.
3. **Editor Panel** — **6 seats** (added Editorial Taste 20 Jul 2026): Voice-Fidelity (×3), AI-Slop Allergist (×2, Lars's own addition), **Editorial Taste (×2)**, Line, Structure, Skeptic/Fact-Check. Scores 0–10 → weighted **Voice Score, bar 9.0** (raised 21 Jul 2026 from 8.5 — genuinely excellent after the panel, not merely clearing); any open `[VERIFY]` caps the piece at 7.0 until Lars rules. **Loops until it clears 9.0** (revise → save `-rvN` → re-score); exit is the bar, not a round count. Stop early only on a **plateau** / **judgment call only he can make** / open `[VERIFY]`; **hard backstop 6 rounds**. **Overpolish guard (21 Jul 2026):** the bar measures **voice-truth + substance, not polish** — intentional rough edges that serve his voice score a 10 on voice-fidelity and are never "corrected"; the loop stops the instant voice-fidelity + slop are maxed, even if a tightening seat could smooth further. Rough-but-his > smooth-but-generic. The **AI-Slop Allergist runs on its own tells — NOT on any Pangram score** (decoupled 21 Jul; de-slopping is voice-positive and stays independent of the detector). **Prime directive: don't flatten him** — protect em-dash ban, long rolling core sentences, light section openings, problem-before-fix. **Lars is always the final gate**; his sign-off edits feed back into [[lars-writing-voice]].
4. **Final Review (Pangram)** — stage 4, **POST-sign-off measurement only** (repositioned 21 Jul 2026). Runs on the text Lars already approved; never edits, never gates, never loops, does NOT feed the slop allergist. Logs the AI-likelihood % into the scheduled file's header + a run log; >75% = post-hoc, his-call heads-up, not a block. Provenance not voice; AI-Assisted expected. Full detail in [[final-review-pangram]].

## Editorial-taste seat + pending taste file (20 Jul 2026)
Lars's point: the voice rubric is retrospective (only logged taste). Added a 6th **Editorial Taste** seat = independent quality judgment (real idea? one thing per section? specific-over-abstract? earned emotion? momentum? surprise? does the "so what" land?). **Ranks BELOW Voice-Fidelity and the Prime Directive** — can lower the score and flag "on-voice but weak," but must NEVER propose a fix that fights his voice; on conflict, voice wins and the tension is surfaced to Lars.
**Lars is building a dedicated taste file.** It plugs into TWO stages: (a) the DRAFT step writes toward it, and (b) the editor's taste seat scores against it. Reserved hook: `feedback_lars_taste.md` (memory-first, folder fallback `Writing Flow\feedback_lars_taste.md`). WHEN LARS PROVIDES THE FILE: read it, decide final placement (may belong in drafting guidance, the taste seat, and possibly voice) — he explicitly wants me to look and decide one-or-multiple homes. Until then both stages run on the seat's built-in taste charter.

## Why / how to apply
He asked for this explicitly. Run a package by name or the whole chain for a new piece. Publish conventions ([[project-substack-pipeline]] index + Drive dual-write + stage moves) are unchanged and run after sign-off; the Pangram stamp happens at the draft→scheduled stage move.

## Pilot (20 Jul 2026) — completed end to end
Ran the editor panel on bring-it-home (24 Jul): scored ~8.6 prose (under the old 8.5 bar it cleared; under today's 9.0 it would loop further) but capped at 7.0 by three unverified stats. Research assistant confirmed all three vs his briefs + web (Kimi K3 27 Jul open weights + frontend-coding win, #4 overall; WAICO 29-nation bloc vs 35-nation Pax Silica; near-frontier price $25–50→$4–6). Applied fixes (price made concrete, Kimi K3 scoped to "real coding work", CPS 230/APRA glosses, news-cycle-fatigue close, slop dedupe). Pushed corrected version to `Substack Scheduled\substack_scheduled_bring-it-home_2026-07-24.md` (old one parked in `Substack Scheduled\_to_delete\` for Lars to trash), updated SUBSTACK_INDEX, and created the current Google Doc in Drive Scheduled (doc id 1cU5mI5lyRPWDW6BoTDdxXIQ1WdscCwS_h-WWfQE3CkE). Research note at `References\research_bring-it-home_2026-07-24.md`.
