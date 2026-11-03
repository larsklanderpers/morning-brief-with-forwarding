---
name: business-skills-export
description: Generalized business/corporate versions of the writing skills exported for Lars's corporate account (24 Jul 2026); plus the pending project-folder rename
type: project
sources: [cowork-import]
imported_at: 2026-09-15T13:26:34Z
---

Lars asked (24 Jul 2026) to export the personal writing skills into portable, generalized skills for a **separate corporate account** where he does a lot of executive writing. The personal set here stays UNTOUCHED — "everything on the business account is business voice; I don't need the personal voice except as appropriate for a senior executive."

## What was built and delivered (as .skill files, via SendUserFile)
Five skills, generalized (no Lars/Substack/thread/vault-path specifics), source in cloud workspace `/home/claude/business-writing-skills/`:
- **interviewer** — neutral author, executive-stakes framing, `[VERIFY]` handoff kept. Output `./drafts/capture_*`.
- **research-assistant** — searches configured corpus/vaults + project memory FIRST, then web; solid/contested/unverified; records durable findings back.
- **editor-panel** — House-Voice seat now scores a **pluggable [STYLE PROFILE]** (memory-first), with a built-in default executive-business charter until a profile exists; Prime Directive generalized to "don't flatten the author"; six core seats + optional technical/business seats.
- **technical-editor** (NEW, standalone + optional panel seat) — owns technical correctness/precision; **learns the org's systems**: reads `systems_reference.md`, asks one specific question on a gap, records the answer, flags `[CONFIRM]` rather than guessing.
- **business-editor** (NEW, standalone + optional panel seat) — decision-maker lens (value prop, so-what, numbers, risk, unmissable ask); learns `business_context.md`.
Plus `writing_config.md` (drop into the corporate account's project memory; all five read it) and a `README.md`.

## Design decisions (his direction)
- Editors packaged **standalone + optional seats** (his pick) — pull the right reviewer per doc type; technical on specs, business on proposals.
- Skills are **memory- and vault-aware and learn as they go** — his explicit requirement. Knowledge stores (`systems_reference.md`, `business_context.md`) grow over runs.
- The **taste interview compilation Lars is finishing (owed ~Sat 25/26 Jul)** plugs into the editor-panel's **[TASTE PROFILE]** slot (and likely the [STYLE PROFILE]). Business voice = senior-executive register, to be calibrated by that file. Also still owed: fold the taste file into the PERSONAL editor-panel taste seat (see [[writing-flow]] reserved `feedback_lars_taste.md` hook).

## Project rename — PENDING Lars's Windows-side action
Lars wants the local project renamed **"Morning Brief with Forwarding" → "personal-writing-support"** (more indicative). Cannot be done from a cloud session: the folder is a **mountpoint** (mount root can't be renamed in-session) and the Windows parent isn't reachable + Obsidian/desktop locks. Lars must rename it in Windows Explorer with Obsidian + the desktop connection closed, then reconnect the folder (and its Vault) in the desktop app.
Good news: the morning-brief pipeline is **path-portable** — `config.json` uses `workspace_path: "."` and `briefing_agent.py`/auth scripts don't hardcode the folder name, so the rename won't break the daily brief. Only ABSOLUTE-path references need updating AFTER the rename:
- Memory notes with the old path: this note's siblings — `project_writing_flow.md`, `project_final_review_pangram.md`, `project_writing_vault.md` (path hints only; don't touch calibration).
- The 1 CCR scheduled task **"Pangram final-review check-back"** (next run 2026-08-03) — its prompt names the folder + `References\`/`Writing Flow\` paths; update via update_trigger.
- Device docs (cosmetic snapshots): `ai-morning-brief-skill.md`, `README.md`, `Writing Flow\01_interviewer.SKILL.md`, `Writing Flow\03_editor-panel.SKILL.md`.
- The INSTALLED personal **editor-panel** skill has an absolute fallback path to the old folder — can't be edited from a session; needs a re-exported .skill re-import (memory-first still works, so low urgency).
NEXT SESSION AFTER RENAME: apply those reference updates.
