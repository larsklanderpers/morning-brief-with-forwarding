---
date_first_seen: 2026-08-07
date_updated: 2026-08-07
source: Scale AI / Center for AI Safety — Remote Labor Index
url: https://labs.scale.com/leaderboard/rli
brief: work
threads: [Shape of Work-to-Come, Co-Existence - Judgment, Practitioner - Coding Ground Truth]
beat: Future of Work / Benchmarks
status: developing
used_in:
---

# Remote Labor Index — the 2.5% is nine months stale, and the real number is the story

**What happened.** The 7 Aug work brief cited *"AI completes only 2.5% of tasks at human gold-standard
quality (March 2026)"* as evidence that 97.5% of the human edge is intact. **The figure is from the launch
paper submitted 30 October 2025.** There is no March 2026 version — that date appears to be invented
somewhere in the aggregation chain.

**The current leaderboard (CAIS update dated 1 Jul 2026):**

| Model | Automation rate |
|---|---|
| **Fable-5** | **15.80%** |
| Opus 4.8 | 8.33% |
| Codex GPT-5.5 | 6.25% |
| Opus 4.6 (Cowork) | 4.17% |
| gpt-5.2 / Manus 1.5 / Manus 1.0 | 2.50% |
| gemini-2.5-pro-preview | 0.83% |

**2.5% (Oct 2025) → 4.17% → 15.8% (Jul 2026). Roughly 6x in eight months.**

**Why it matters.** Two reasons, and the second is the important one.

1. **Do not publish 2.5%.** It is exactly the catchable error a hostile reader lands on, and it would sit
   in a piece arguing the human edge is durable — the worst possible place to be nine months behind.
   (Use **15.8%** and cite the leaderboard; CAIS's dashboard says 15.83% and one secondary says 16.1%.)
2. **The constructive argument survives the correction and gets sharper.** At 15.8%, **~84% of real,
   paid, end-to-end remote projects still fail.** The honest line is not "97.5% of your edge is yours" —
   it is *"the edge is still yours, and it shrank by two-thirds in eight months while everyone was arguing
   about whether it would."* Direction of travel beats a snapshot.

## What it actually measures, and its limits

**240 real freelance projects, 6,000+ hours, $140,000+ of work already completed and paid for by human
professionals** — game development, product design, architecture, data analysis, video animation. Some
projects >$10,000 and >100 hours. Scored on whether the deliverable met a level a paying client would accept.

Limits, stated by the researchers themselves:

- **AI judges are unreliable here.** A judge calibrated on earlier models **overestimated newer models by
  2.3–2.9x**, though it ranked them correctly. Human evaluation is still required — so automated re-scoring
  inflates the number.
- **Time-horizon models don't fit**: the relationship between task duration and AI success is *"flat to
  slightly rising, not the downward slope a time-horizon model would assume."*
- **It measures full end-to-end automation of a whole project — the hardest possible bar.** It says nothing
  about AI doing 70% of a project with a human finishing it, which is the actual working pattern. A low RLI
  score is fully compatible with large real-world productivity effects.

That last limitation is the bridge to the archetypes: **RLI measures the Prototyper-to-shipped gap, and the
Sweeper, Editor and Risk Steward archetypes live inside it.** "Good enough for a draft" and "good enough to
ship" are different bars, and RLI is a direct measurement of the distance between them.

## Observations

- **2026-08-07** — First seen as a YouTube-sourced item in the work brief. Verified into a correction plus a better argument. This is the second time this week a work-brief number has arrived stale from a video summary; treat creator-sourced statistics as unverified by default.

## Feeds

- [[Shape of Work-to-Come]] — the empirical spine of the "97.5% is yours" claim, now dated
- [[Co-Existence - Judgment]] — the draft/ship gap is where judgment is priced
- [[Practitioner - Coding Ground Truth]] — pairs with the METR result in [[Specification is the chokepoint - the evidence is mixed]]
- [[The archetypes converge on one shape]]

## Open

- A piece that *leads with the correction* — "I was going to tell you 97.5% of the work is still yours; the number moved while I was writing" — is more honest and more interesting than one that quietly uses the current figure. That is a Diversions-slot shape.
