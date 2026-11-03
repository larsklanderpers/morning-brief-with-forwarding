---
name: morning-brief-project
description: "Daily cybersecurity brief pipeline — folder structure, tools, and where research notes live"
metadata:
  node_type: memory
  type: project
sources: [cowork-import]
imported_at: 2026-09-15T13:26:34Z
---

Lars's daily brief pipeline lives at `D:\vc-personal-projects\Morning Brief with Forwarding\`.

## Folder structure
- `Daily Briefs\` — `brief_YYYY-MM-DD.md`, the cyber morning brief
- `AI Briefs\` — `ai_brief_*` and `work_brief_*` (the 8am ai-work-community-brief feeds Shape-of-Work-to-Come)
- `References\` — **research notes and week plans. This is the one directory to check first.**
- `Substack Drafts\` · `Substack Scheduled\` · `Substack Published\` — the writing pipeline, see [[substack-pipeline]]
- `Writing Flow\` — flow charter + skill snapshots, see [[writing-flow]]
- `Vault\Writing\` — Obsidian vault, thread hubs + signal notes, see [[writing-vault]]
- `reference_mds\` — the voice canon, see [[voice-canon]]
- `briefing_agent.py`, `config.json` — the generator

## Research notes (confirmed by Lars, 10 Aug 2026)
**All research notes go in `References\`, and Lars files them there himself.** He said so directly:
he stores research notes in that same named directory under the project. So:
- **Look in `References\` before searching anywhere else** for backing on a claim, and before
  commissioning fresh research — a note may already exist.
- Naming runs `research_<slug>_<date>.md`; **he does not always use the ISO date format** (his own
  `research_eo14409recheck_20260809.md` sits next to `research_us-ai-eo-status_2026-08-02.md`).
  Do not "correct" his filenames; match what is there and move on.
- Week plans live in the same folder as `week-plan_YYYY-MM-DD.md` (Monday date).
- **A newer note supersedes an older one on the same subject and says so in its own header.** Check for
  a supersession line before trusting any note, and read the newest first. This is not theoretical —
  see the EO 14409 case below.

## The supersession case worth remembering (9–10 Aug 2026)
`research_eo14409recheck_20260809.md` **supersedes** `research_us-ai-eo-status_2026-08-02.md` and
**refutes its central finding.** The 2 Aug note said the White House missed the 1 Aug deadline for the
EO 14409 framework; in fact the framework was completed on time and is being withheld from publication,
confirmed by a White House official on the record to Axios on 3 Aug plus five other outlets. The 2 Aug
claim traced back to an opinion column with no named sources. A week-plan slot had been built on the
refuted version.

**How to apply:** when a plan cites a research note, check the note's date against anything newer in
`References\` covering the same subject before drafting a word. A stale note that reads as thorough is
more dangerous than no note, because the draft inherits its confidence.

## Security hygiene note (flagged 8 Aug 2026, unresolved)
`config.json` holds a live Substack session cookie and a Gmail app password in plaintext. Flagged to
Lars; he has not said whether he rotated them. Avoid dumping that file's contents into a transcript.
