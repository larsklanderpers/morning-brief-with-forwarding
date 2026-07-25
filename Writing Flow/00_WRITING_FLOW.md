---
name: writing-flow
description: Run Lars's end-to-end Substack writing flow — interviewer (mine his take + stress-test the argument) → research-assistant (dig on any gaps) → draft → six-seat editor-panel (loop to the 9.0 bar) → his sign-off → final-review (Pangram, post-sign-off measurement only). Use whenever Lars wants to take a piece from idea to publish-ready, says "run the writing flow" / "let's write the [topic] piece properly" / "take this all the way", or wants the full interview-research-edit chain rather than a single stage. Start here for a new piece; the interviewer, research-assistant, editor-panel, and final-review skills each run one stage on their own.
---

# Lars's Writing Flow

Three packages sit on top of the existing Substack pipeline. They don't replace how drafts get written and published — they add the muscle Lars asked for: getting to the meat, digging deeper when a topic is thin, and looping a draft until it reads like him with no seams.

Invoke a package by name in chat ("interview me on X", "research this", "run the editor panel on <draft>"), or run the whole chain for a new piece.

## The chain

```
        ┌─────────────────────────────────────────────────────────────┐
        │  PREP (existing): read SUBSTACK_INDEX + all drafts, pick     │
        │  thread, mine the daily briefs  (substack-drafting-process)  │
        └───────────────────────────┬─────────────────────────────────┘
                                     │
                 ┌───────────────────▼───────────────────┐
                 │  1. INTERVIEWER   (interviewer skill)  │
                 │  Pass 1: mine Lars — stakes, insider   │
                 │  take, analogy, economics              │
                 │  Pass 2: interrogate the argument      │
                 │  → capture_<slug>.md  +  [VERIFY] tags │
                 └───────────────────┬───────────────────┘
                                     │ (if gaps / "I don't know enough")
                 ┌───────────────────▼───────────────────┐
                 │  2. RESEARCH ASSISTANT (research skill)│
                 │  local corpus first → fan-out → fetch  │
                 │  primaries → verify → cited note       │
                 │  → References\research_<slug>.md       │
                 └───────────────────┬───────────────────┘
                                     │
                 ┌───────────────────▼───────────────────┐
                 │  DRAFT (existing): write the piece in  │
                 │  Lars's voice + taste from capture +   │
                 │  research                              │
                 └───────────────────┬───────────────────┘
                                     │
                 ┌───────────────────▼───────────────────┐
                 │  3. EDITOR PANEL  (editor-panel skill) │
                 │  6 seats score vs voice + taste → loop │
                 │  revise/re-score until bar 9.0 + slop  │
                 │  clean + no open [VERIFY]              │
                 │  → substack_draft_<slug>-rvN.md        │
                 └───────────────────┬───────────────────┘
                                     │
                 ┌───────────────────▼───────────────────┐
                 │  LARS'S SIGN-OFF (final gate — always) │
                 │  his edits = fresh voice calibration   │
                 └───────────────────┬───────────────────┘
                                     │
                 ┌───────────────────▼───────────────────┐
                 │  4. FINAL-REVIEW (final-review skill)   │
                 │  POST-sign-off. Pangram on the         │
                 │  APPROVED text — measurement only.     │
                 │  No edits, no gate, no slop feed.       │
                 │  Stamp header + log; >75% = post-hoc    │
                 │  heads-up, his call. → References\      │
                 │  final-review_<slug>.md                 │
                 └───────────────────┬───────────────────┘
                                     │
        ┌────────────────────────────▼────────────────────────────────┐
        │  PUBLISH (existing): update SUBSTACK_INDEX, dual-write to    │
        │  Drive, stage-move/rename  (project-substack-pipeline)       │
        └──────────────────────────────────────────────────────────────┘
```

## The three packages, in one line each

1. **Interviewer** — makes sure the piece has meat before it's written: Lars's first-person stakes and insider view first, then a stress-test of the argument. Output: an interview capture that seeds the draft.
2. **Research Assistant** — when Lars feels thin on something, goes and gets the depth: searches his own briefs first, fans out on the web, fetches primaries, verifies adversarially, and hands back a cited note that says what's solid vs. what isn't.
3. **Editor Panel** — six editors (voice-fidelity, line, structure, skeptic/fact-check, AI-slop allergist, editorial-taste) score the draft against how Lars actually writes *and* against independent editorial quality, then loop until it clears the bar and hand it to him. Editorial-taste ranks below voice-fidelity — it catches "on-voice but weak" without ever overriding his voice. He's always the final gate.

## How it respects the existing setup

- **Voice is the target, not a suggestion.** Every package reads `feedback_lars_writing_voice.md` — the live project-memory note first, with an on-disk fallback copy in the `Writing Flow\` folder for runs without memory access (memory wins if both differ). The em-dash ban, analogy-first openers, problem-before-fix, and the protected long rolling sentences are load-bearing, not stylistic garnish. Signature devices (the reader's-calculus close, "Read that again.", the escalating-tool metaphor, Hollywood-vs-grind) are CONDITIONAL callbacks — rationed to once or twice a week each, deployed only when the story calls for them, never a required slot (Lars, 2026-07-24).
- **Taste rides alongside voice (LIVE as of 2026-07-24).** Lars's dedicated taste reference landed: the compiled profile `reference_mds\lars-about-me.md` (identity, voice fingerprint, writing laws, taste loves/disgusts, hard refusals, phrase bank, golden examples — apply silently), with its deep source `reference_mds\taste-interview-transcript.md` (the 100-question taste interview + living POST-INTERVIEW ACCRETIONS log; new beats append there, flagged to Lars for veto). It plugs into TWO stages: the **draft** step writes toward it, and the editor panel's **editorial-taste seat** scores against it. Taste ranks below voice everywhere: it sharpens, it never overrides.
- **The corpus matters.** Interviewer and structure seat both check `SUBSTACK_INDEX.md` and `project_content_architecture.md` for thread continuity — callbacks, forward refs, thread rotation, Saturday-Diversion vs. weekday register, Sunday capstone logic.
- **Lars holds the final gate.** Nothing here publishes or overwrites. Revisions save as new `-rvN` files beside the original; his edits at sign-off feed back into the voice rubric.
- **Publish conventions are untouched.** Index update, Google Drive dual-write, and stage-move/rename all run exactly as they do today, after sign-off.

## Running just one package

You don't have to run the whole chain. Common single moves:
- "Interview me on <topic>" → just the interviewer, before you draft.
- "I don't know enough about <X> — dig into it" → just the research assistant.
- "Run the editor panel on <draft>" → just the panel loop on an existing draft (this is the quickest way to see the flow work).

## The stage skills
Each stage is its own installed skill you can invoke directly:
- **interviewer** — "interview me on <topic>"
- **research-assistant** — "dig into <X>" / "I don't know enough about <X>"
- **editor-panel** — "run the editor panel on <draft>" / "does this sound like me?"
- **final-review** — "run the final review" / "check this for AI" / "run pangram on <draft>"

## Stage 4 — final-review (Pangram), added 20 Jul 2026 · moved POST-sign-off 21 Jul 2026
**This runs after Lars signs off, not before** — on the exact text he approved. It's a measurement, not an editor: it never changes a word, never gates publication, never loops, and does NOT feed the AI-Slop Allergist. Lars's reason (21 Jul): if a detector score could drive edits before sign-off, it would push the prose toward beating a detector instead of toward his voice, and he'd rather ship a rough edge that's his than an overpolished piece that isn't. So the detector is fully decoupled — it only *measures* what he already approved.

It measures **provenance, not voice** (Claude-assisted drafts will read as AI-Assisted or AI — expected, fine, never a voice judgment). It logs the overall AI-likelihood % into the scheduled file's header alongside the references, and into a run log (`References\final-review_<slug>.md`). The **≤75% comfort line** is just an annotation; a score **over 75%** gets a post-hoc, his-call heads-up ("came in at NN%, want to look?") — it still doesn't block or auto-revise. Runs via Claude-in-Chrome against pangram.com today (API egress-blocked); escalates to the Pangram API if Chrome proves insufficient. 75% line provisional — under review ~3 Aug 2026 (see `project_final_review_pangram.md`). Feasibility: `Writing Flow\final-review_pangram_research_2026-07-20.md`.

## Overpolish guard on the 9.0 bar (Lars's priority, 21 Jul 2026)
The raised bar is a bar on **voice-truth and substance, not polish.** Intentional rough edges that serve his voice score a 10 on voice-fidelity and are never "corrected"; the panel stops the moment voice-fidelity and slop are maxed, even if a tightening seat could smooth further. "Top flight" = unmistakably Lars and genuinely good — never buffed into competent mush.
