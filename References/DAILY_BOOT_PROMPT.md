# Daily boot — one chat per piece

**Superseded by the `day-start` skill (proposed 4 Sep 2026).** Once that skill is saved, start a day's
chat by typing `/day-start` — or just say "start the day" — and it does everything below, plus it works
out the live week plan from the date instead of being told, and opens by showing you the week and asking
which day you are on.

This file stays as the fallback for a session where the skill is not available.

---

## The fallback prompt

```
Substack pipeline, new chat for one piece. Work out which week plan is live before you read anything:
week plans are References\week-plan_YYYY-MM-DD.md, dated to the MONDAY of the week they cover, so the
live one is the plan for the Monday of the week containing the piece's publication date -- which is
often tomorrow, not today, because I draft the night before. Do not use a plan whose week has passed.
If no plan exists for that week, say so and offer to write one.

Then read, in this order:

1. CLAUDE.md (the working agreement -- GREEN/AMBER/RED, accuracy rules, voice)
2. That week plan -- the STATUS BOARD at the end first, then the day block. Amendment blocks inside a
   day block supersede the reasoning above them.
3. Substack Drafts\SUBSTACK_INDEX.md, newest few rows.
4. References\MEMORY.md, then whichever memory files it indexes look relevant.

Then show me the week as a table -- day, title, state, panel score, folder -- and ask me which day I am
working. With it, about ten lines on: what the plan says that piece is, what has changed under the plan
since it was written, what is spent in the seven-day window that today cannot reuse (images, action
moves, closes), and what you need from me before you start.
```

---

## The tasks it dispatches into

- `draft it` — write v1, email it, stop. No panel unless asked.
- `read my rvN` — report what my pass added, flag what needs my ruling, apply mechanics silently as the
  next rv, propose word and tone rather than making the change.
- `panel it` — six-seat panel against the window, **run as a subagent with file paths**, not by pasting
  the window into the chat. That is what keeps a per-piece chat viable.
- `research pass` — foot every claim at a primary first; write the note; mark unreached as unreached.
- `schedule it` — only on my explicit word.

## What it must not assume

- That the plan is right. Landed text beats it.
- That a piece is ready to move. Scheduled needs my word, every time.
- That anything may be published. I push to Substack myself.
- That my text needs improving. Mechanics silent, word and tone proposed.

## Before the session ends

Update the live plan's status board. It is the next chat's memory.
