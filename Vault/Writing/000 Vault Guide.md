# Writing Vault — how this works

A working memory for the Substack. Not an archive — the daily briefs in
`Morning Brief with Forwarding\Daily Briefs\`, `AI Briefs\` are the archive.
This vault holds only what got **promoted**: signals worth building on.

## The three note types

**Signals** (`Signals/`) — one note per story or observation you flagged.
Atomic. Links out to the thread hub(s) it feeds. Gets *updated* when the story
recurs, never duplicated.

**Threads** (`Threads/`) — one hub per narrative line, matching the thread legend
in `SUBSTACK_INDEX.md`. This is where evidence accumulates. When you sit down to
write, you open the hub, not eleven brief files.

**Templates** (`Templates/`) — the signal note skeleton.

## The rules that keep it useful

1. **Flagged items only.** Everything you star in the Brief Tracker; nothing else.
   If the whole brief flows in, the hubs stop being readable inside a fortnight.
2. **Update, don't duplicate.** Kimi K3 has appeared in four briefs. That is one
   signal note with four dated observations, not four notes. Check `Signals/`
   before creating.
3. **Every signal links to at least one thread.** An unlinked signal is a
   bookmark, and bookmarks rot. If it fits no thread, that is worth noticing —
   either it is a new thread or it does not belong here.
4. **Prune on Sundays.** The capstone is the forcing function. Promote what is
   load-bearing, merge duplicates, mark spent signals `status: used`.

## Frontmatter fields

- `date_first_seen` / `date_updated` — the second is what makes recurrence visible
- `source` / `url` — provenance, so the research assistant can re-verify
- `brief` — which brief it came from: `cyber`, `ai`, `work`
- `threads` — one or more, matching `Threads/` note names exactly
- `status` — `signal` (raw) → `developing` (building toward a piece) → `used` (published)
- `used_in` — the piece that consumed it, once published

## For future automation

Brief tasks and the research-assistant skill should search `Signals/` and
`Threads/` before fanning out to the web. Local signal first — that is the point.

## Added 2026-08-16 — a fourth note type

**Reference** (`Reference/`) — a body of source material too large to be a signal and too
foundational to be a piece. One note per corpus, not per source. Created for the AI-adoption
reading list, which was 35 sources at once: promoting each one to `Signals/` would have broken
rule 1 inside a single afternoon, and leaving them out would have lost the work.

Rules that keep it from becoming a dumping ground:

1. **A Reference note is graded, not listed.** Every source carries a provenance grade and the
   caveat that has to travel with it. A bare bibliography is a bookmark folder.
2. **It still links to a thread.** Same as rule 3 above.
3. **When one source inside it becomes load-bearing, promote it to `Signals/`** and leave the
   Reference note as the place the corpus lives. That is what happened with the six adoption
   signals filed 2026-08-16.

Current contents: `Foundational research — AI adoption and change management`,
`ADKAR and Kotter — a provenance file`. Both feed `Threads/Adoption and Change`.
