---
name: project_brief_tracker_star_feature
description: Brief Tracker artifact has a star/flag story-candidate feature in its render engine that rebuilds MUST preserve; regressed once on Aug 18 2026
metadata: 
  node_type: memory
  type: project
  originSessionId: 165fb16e-c6f4-49c7-a08d-59383637614c
  modified: 2026-08-19T23:48:22.319Z
sources: [cowork-import]
imported_at: 2026-09-15T13:26:34Z
---

The "brief-tracker-daily" Cowork artifact (rebuilt each weekday by the brief-tracker-rebuild scheduled task) has a **star/flag "story candidate" feature** built into its render engine and template — NOT just the read-toggle. It includes: a `.flag-zone` ★ on each item's right edge, `toggleFlag`/`flaggedIds`/`flaggedMarkdown`/`copyFlagged` functions, a `#export-overlay` copy panel, a header `#flag-btn` ("☆ N flagged"), and `resetAll()` that clears read marks but KEEPS flags. Flags persist per day in localStorage under key `candId(id) = id + '#c'`.

The rebuild task says to swap ONLY the `const BRIEF_DATA = {...}` block and leave the render engine untouched. On **2026-08-18** a rebuild replaced the whole render engine with a starless one, silently dropping the feature; every rebuild after copied the broken engine forward (incl. the morning of Aug 19) because the task preserves whatever engine is currently live.

**Why:** Lars uses starring to collect signal for deeper analysis — losing it breaks his workflow, and the loss is invisible unless he notices the stars are gone.

**How to apply:** When rebuilding, after swapping BRIEF_DATA, verify the star machinery survived — grep the output for `toggleFlag`, `flag-zone`, `copyFlagged`, `flaggedMarkdown`. If the live index.html ever lacks them, restore the render engine from the newest `versions\*.html` that still has it (last-good was `versions\1786969901990.html`, Aug 17). Version history lives at `C:\Users\LarsDev\Claude\Artifacts\brief-tracker-daily\versions\` (reachable via Read/Grep, not the bash mount). See [[project_morning_brief]].
