---
name: "writing-flow"
description: "Run Lars's end-to-end Substack writing flow -- interviewer (mine his take + stress-test the argument) → research-assistant (dig on any gaps) → draft → six-seat editor-panel (score to the bar) → his sign-off → the day's note. Use whenever Lars wants to take a piece from idea to publish-ready, says \"run the writing flow\" / \"let's write the [topic] piece properly\" / \"take this all the way\", or wants the full interview-research-edit chain rather than a single stage. Start here for a new piece; the interviewer, research-assistant, editor-panel and substack-notes skills each run one stage on their own."
---

# Lars's Writing Flow

Four packages sit on top of the existing Substack pipeline. They don't replace how drafts get written and published. They add the muscle Lars asked for: getting to the meat, digging deeper when a topic is thin, looping a draft until it reads like him with no seams, and turning each day's piece into one strong Substack Note.

Invoke a package by name in chat ("interview me on X", "research this", "run the editor panel on <draft>", "today's note"), or run the whole chain for a new piece.

## The chain

```
        ┌─────────────────────────────────────────────────────────────┐
        │  PREP (existing): read SUBSTACK_INDEX + all drafts, pick     │
        │  thread, mine the daily briefs  (substack-drafting-process)  │
        └───────────────────────────┬─────────────────────────────────┘
                                     │
                 ┌───────────────────▼───────────────────┐
                 │  1. INTERVIEWER   (interviewer skill)  │
                 │  Pass 1: mine Lars -- stakes, insider   │
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
                 │  research; END WITH THE FOOTER IN FULL │
                 └───────────────────┬───────────────────┘
                                     │
                 ┌───────────────────▼───────────────────┐
                 │  3. EDITOR PANEL  (editor-panel skill) │
                 │  6 seats score vs voice + taste → loop │
                 │  revise/re-score until bar 9.0 + slop  │
                 │  ≥ 9.5 + no categorical fail + no open │
                 │  [VERIFY] + footer                     │
                 │  → substack_draft_<slug>-rvN.md        │
                 └───────────────────┬───────────────────┘
                                     │
                 ┌───────────────────▼───────────────────┐
                 │  LARS'S SIGN-OFF (final gate -- always) │
                 │  his edits = fresh voice calibration   │
                 └───────────────────┬───────────────────┘
                                     │
        ┌────────────────────────────▼────────────────────────────────┐
        │  PUBLISH (existing): update SUBSTACK_INDEX, dual-write to    │
        │  Drive, stage-move/rename  (project-substack-pipeline)       │
        └────────────────────────────┬────────────────────────────────┘
                                     │
                 ┌───────────────────▼───────────────────┐
                 │  4. DAILY NOTE  (substack-notes skill) │
                 │  mine the signed-off piece → 3         │
                 │  candidates, recommend 1, afternoon    │
                 │  slot; 7-day log check; mostly         │
                 │  standalone                            │
                 │  → Substack Notes\notes_log.md         │
                 └───────────────────────────────────────┘
```

## The four packages, in one line each

1. **Interviewer** -- makes sure the piece has meat before it's written: Lars's first-person stakes and insider view first, then a stress-test of the argument. Output: an interview capture that seeds the draft.
2. **Research Assistant** -- when Lars feels thin on something, goes and gets the depth: searches his own briefs first, fans out on the web, fetches primaries, verifies adversarially, and hands back a cited note that says what's solid vs. what isn't.
3. **Editor Panel** -- six editors (voice-fidelity, line, structure, skeptic/fact-check, AI-slop allergist, editorial-taste) score the draft against how Lars actually writes *and* against independent editorial quality, then loop until it clears the bar and hand it to him. Editorial-taste ranks below voice-fidelity -- it catches "on-voice but weak" without ever overriding his voice. He's always the final gate.
4. **Daily Note** -- runs after sign-off, never before, because it lifts his final text. Three candidate Substack Notes from the day's piece, one recommended for the afternoon, checked against the last 7 days of notes, mostly standalone rather than promotional. On request ("batch this one"), fills a reserve from a flagship piece for thin days. Lars posts it himself.

## How it respects the existing setup

- **Voice is the target, not a suggestion.** Every package reads `feedback_lars_writing_voice.md` -- the live project-memory note first, with an on-disk fallback copy in the `Writing Flow\` folder for runs without memory access (memory wins if both differ). The em-dash ban, analogy-first openers, rationed signature devices, and the protected long rolling sentences are load-bearing, not stylistic garnish.
- **Taste rides alongside voice.** Lars's taste profile is live at `reference_mds\lars-about-me.md`, with the deep source in `reference_mds\taste-interview-transcript.md`. It plugs into the **draft** step, the editor panel's **editorial-taste seat**, and the **daily note** pick. Taste ranks below voice everywhere: it sharpens, it never overrides.
- **The corpus matters.** Interviewer and structure seat both check `SUBSTACK_INDEX.md` and `project_content_architecture.md` for thread continuity -- callbacks, forward refs, thread rotation, Saturday-Diversion vs. weekday register, Sunday capstone logic. The daily note respects printed promises and never front-runs tomorrow's piece.
- **Every piece ends with the standing footer, written out in full (27 Sep 2026, his word: "please make sure the writing skill always puts the footer in there").** After the closing `---`:

```
*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about AI governance (often), AI methodologies (also often), cybersecurity strategy (sometimes), and technology risk (always). Today's argument is that <one sentence, specific to THIS piece>.*
```

  The first line is fixed, verbatim. The "Today's argument is that..." sentence is written fresh for each piece and updated if the thesis moves in revision. **Never write the literal placeholder `[STANDING FOOTER]`.** The drafters did, and Fri 25 *Adoption Speed, Control Speed* published with only the placeholder. The editor panel blocks on a missing or placeholder footer, and `day-start`'s `schedule it` step refuses to move a file to Scheduled without it. Saturday Diversions carry the same footer until he settles a lighter variant. The daily note never lifts the footer as note material.
- **Lars holds the final gate.** Nothing here publishes or overwrites. Revisions save as new `-rvN` files beside the original; his edits at sign-off feed back into the voice rubric.
- **Publish conventions are untouched.** Index update, Google Drive dual-write, and stage-move/rename all run exactly as they do today, after sign-off.

## Running just one package

You don't have to run the whole chain. Common single moves:
- "Interview me on <topic>" → just the interviewer, before you draft.
- "I don't know enough about <X> -- dig into it" → just the research assistant.
- "Run the editor panel on <draft>" → just the panel loop on an existing draft (this is the quickest way to see the flow work).
- "Today's note" / "note from <piece>" → just the daily note on a signed-off piece.
- "Batch this one" → reserve notes from a flagship piece.

## The stage skills
Each stage is its own installed skill you can invoke directly:
- **interviewer** -- "interview me on <topic>"
- **research-assistant** -- "dig into <X>" / "I don't know enough about <X>"
- **editor-panel** -- "run the editor panel on <draft>" / "does this sound like me?"
- **substack-notes** -- "today's note" / "batch this one"