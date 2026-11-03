---
name: project-substack-pipeline
description: "Substack draft pipeline — audience, beats, index file location, week-plan-on-disk rule, workflow conventions, and the stage-move reconciliation gap"
metadata: 
  node_type: memory
  type: project
  originSessionId: 00c78578-c086-444c-8f0d-fd432050a46a
sources: [cowork-import]
imported_at: 2026-09-15T13:26:50Z
---

Lars writes two Substack publications drawing from the daily briefs:
- **Cyber morning brief context** — cybersecurity strategy, threats, policy (Gaslight piece is the voice reference)
- **AI strategy / privacy / data sovereignty** — AI adoption, Privacy Act, GDPR, local models (Privacy Act piece is the voice reference)

**Primary audience for clubs-focused pieces:** Australian registered clubs (RSLs, leagues clubs, gaming venues). Key regulatory parallel is AUSTRAC (anti-money laundering) — clubs already have AML/CTF obligations, so OAIC/Privacy Act compliance often maps to the same documentation layer. Lars writes as an industry insider ("we", "our") for this audience, not as an outside consultant. **Cross-Pacific parallel (18 Jul 2026):** the same structure maps onto Native-American gaming corporations (NIGC-regulated tribal gaming + Indigenous data sovereignty under CARE/OCAP principles) — the two regulated regimes Lars works in are Australian inference/ADM rules AND Native-American corporation data sovereignty. Gaming + AML + data sovereignty is the shared spine; "bring inference in-jurisdiction" is the shared architectural answer.

## WEEK PLAN GOES ON DISK — STANDING RULE (Lars, 7 Aug 2026)

**As soon as Lars and I agree a week's schedule, it gets written to `References\week-plan_<YYYY-MM-DD>.md`, dated to the MONDAY of that week.** Not to memory alone, not to chat alone. Other sessions cannot read this session's conversation, and a plan that lives only in a chat log is invisible to the scheduled tasks, to a fresh session, and to Lars on another machine.

**Why the rule exists:** on 7 Aug we found `week-plan_2026-08-03.md` and `week-plan_2026-08-17.md` on disk but **nothing for the week we were actually in**. The 10–16 Aug shape had been agreed on 1–2 Aug and existed only in conversation plus a partial memory note that covered Monday and Tuesday. Wednesday onward had no artefact at all. Lars asked mid-week what Wednesday was and the honest answer was "nothing on disk."

**What the file must carry** (see `week-plan_2026-08-10.md` as the model):
- YAML front matter: `type: week-plan`, `week:` range, `status:`, `capstone:` date, and `mirror_week:` if the week pairs with another
- The capstone spine in one paragraph, and what the week's argument actually is
- One block per day: slug, thread, status (SCHEDULED / drafted rvN / undrafted), the spine, the load-bearing evidence, and the path to any research note
- **Standing constraints:** which pieces own which metaphors and data, which signature devices are spent, thread-rotation warnings
- Open questions and unresolved provenance, named as such

**Keep it current as the week runs.** When a piece is scheduled, when a spine changes, when a device gets spent — update the file. It is the week's source of truth for any session that is not this one. The memory note for a week (e.g. `project_week_2026_08_10.md`) is a pointer and a summary; the disk file is the artefact.

## Index and naming

**Substack index file:** `D:\vc-personal-projects\Morning Brief with Forwarding\Substack Drafts\SUBSTACK_INDEX.md`
Every time a new Substack draft is created, add a row to this index.

**Index format (updated 18 Jul 2026, per Lars):** Reverse-chronological — NEWEST ROW AT TOP. Columns: `Date | Title | Thread | Beat | Status | Folder`. **Thread** = the interlaced narrative-thread tag (e.g. AI Sovereignty, AI Attack Surface, Trust Boundaries, Machine Identity, Shape of Work, Practitioner/Coding, Co-Existence/Judgment, Ad Hoc Regulatory Regime, Diversions, Sunday Capstone; full list in the index's "Thread legend"). **Beat** = the finer topic tag (Cyber / AI Security / Privacy / …). Keep BOTH columns — Lars uses Thread to see the interlaced-thread flow and Beat for the fine topic. Add the Thread tag for every new row.

**Draft naming convention:** actual files use a stage prefix: `substack_{draft,scheduled,published}_<slug>_<YYYY-MM-DD>.md`. On stage transition, rename the prefix and move folders.

**Stage moves on disk (18 Jul 2026):** when a piece publishes, move its local .md from `Substack Scheduled\` → `Substack Published\` and rename the prefix `substack_scheduled_` → `substack_published_`; keep v1+v2 pairs together (Published/ already holds version pairs). Use `device_bash` `mv` for the move — the desktop bridge allows `mv`/rename; only `rm` is blocked. Update the index Folder column to match. (Did this for the whole 13–18 Jul run on 18 Jul.)

**Status options in index:** Draft · In editing · Ready to publish · Published · Shelved

**Why:** Lars asked for a project-level index so he doesn't have to search through daily brief runs to find drafts, and wants to keep his eyes on the publishing flow.

**How to apply:** When writing any Substack draft, immediately add a row to SUBSTACK_INDEX.md (newest at top, Thread + Beat both filled). When Lars asks "what Substack drafts do we have" or "where's that piece on X", read the index first. When he asks what a given DAY is, read the week-plan file for that week first.

## ⚠️ THE STAGE-MOVE RECONCILIATION GAP (diagnosed and cleared 20 Aug 2026)

**On 20 Aug 2026, `Substack Scheduled\` held 20 past-due pieces spanning 27 Jul – 16 Aug** — three
full weeks of published work still sitting in the queue folder, with `SUBSTACK_INDEX.md` still
calling every one of them Scheduled. Cleared that day: all 20 moved to `Substack Published\`,
prefixes renamed, index Status and Folder columns updated. **Diagnosis, because the same shape will
recur elsewhere:**

1. **The rule has no trigger.** "Reconcile a past-due Scheduled piece to Published" lives *only* in
   `CLAUDE.md`'s AMBER list, and it is phrased **reactively and in the singular** — *"if a piece's
   scheduled date is in the past…"*. Nothing runs it. `briefing_agent.py` never touches the Substack
   folders. `.claude/commands/` holds only `story-monitor.md`. It fires only if a session happens to
   compare folder dates against today, which nothing asks it to do.
2. **The writing flow has no stage 5.** `Writing Flow\00_WRITING_FLOW.md` runs interviewer →
   research-assistant → editor-panel → sign-off → final-review and **terminates at Scheduled.** The
   chain never revisits a piece after it is queued.
3. **Every session works forward.** Sessions read `Substack Scheduled\` constantly — the
   "Scheduled beats the plan" rule makes them — but only to see *what has run*. Reading the folder
   is not the same as reconciling it.
4. **It has always been manual.** Every file in `Substack Published\` still carries
   `**Status: Scheduled …**` in its own in-file header, including ones moved the same morning. The
   stage move has only ever been a filename rename done by hand; the in-file header is not part of
   the convention and is inconsistent throughout.
5. **On 20 Aug it half-fired.** A concurrent session reconciled 17–20 Aug correctly (including that
   day's piece) but swept only the current week — consistent with a rule written for one piece
   rather than for a backlog.

**How to apply.** Treat the reconcile as a **folder sweep, not a per-piece reaction**: at the start
of any session that touches the pipeline, list `Substack Scheduled\`, compare every filename date to
today, and move everything dated **on or before today**. Anything dated after today stays.

**The generalisable finding, and it is the same failure as the killed-claims problem:** this project
has several rules written in prose that no process executes — the reconcile rule, and the do-not-print
lists that `briefing_agent.py` cannot read (see [[Brief Claim Provenance]] §5). **A rule with no
runner is a rule that fires only by luck.** When proposing a durable fix, propose the runner.

⚠️ **Two pre-existing orphan index rows** (2026-07-09, 2026-07-06) are marked Published with no file
in the folder. Predate the 20 Aug sweep; unresolved.

**Google Drive mirror (added 2026-07-06):** Lars travels and wants to edit pieces from his laptop, so the whole Substack cycle is mirrored to Google Drive as **Google Docs** (converted from the local markdown for easy in-browser/mobile editing). Local markdown stays the source of truth; Drive is the travel-edit copy.
- Drive structure: **My Drive > writings > substacks > {Substack Drafts, Substack Scheduled, Substack Published}**
- Folder IDs: writings `137akzLAHwcwLfyB_IpYf70o1laBUHueq` · substacks `1QrsFPY6xcbgTsGLwRTp0L6bHd818tXX6` · Drafts `1XBA-yFxY9Mf_7fXAQg7MJsnN8rkVLtXM` · Scheduled `1f8bVeNe23WqDXWYZrIBNqFZSqIGPuZOM` · Published `1J9nfscjfVE-jwVsorqM1ArlV-geCcvBU`
- **DUAL-WRITE RULE:** every Substack action applies to BOTH locations. New draft → write local .md AND create a Google Doc in the matching Drive folder. Stage move (draft→scheduled→published) → rename/move the local file AND create the Doc in the matching Drive folder. Drive Doc title = local filename without .md. **Exception for v1 drafts under review (18 Jul 2026): hold the Drive Doc until Lars has done his first review pass, so we don't create a Doc then immediately supersede it — avoids stale-Doc churn given the connector can't delete. Create the single current Doc once the draft stabilizes.**
  ⚠️ **The 20 Aug backlog sweep did NOT mirror to Drive** — 20 pieces moved locally with no Drive
  counterpart created, because doing so would spawn 20 new Docs and leave 20 stale Docs in Drive
  Scheduled for Lars to trash by hand. **Open item; ask before running it.**
- **Drive = ONLY the current version (Lars's rule, 6 Jul 2026).** No version-suffixed Docs (`_v2`, `_v3`) in Drive — one Doc per piece. Do NOT mirror intermediate revisions as new Docs.
- **Connector limitation:** the Google Drive connector only exposes create/copy/read/search — NO update-in-place, delete, or move/rename tools. This is unexposed functionality, not an OAuth-scope/permissions issue; broader rights won't add the tools. Consequence: I cannot overwrite, delete, or move a Doc from my side. On any revision or stage move, I create the new current Doc and MUST tell Lars exactly which superseded Doc(s) to delete manually in Drive (a quick trash). Keep Drive tidy by always flagging stale Docs for deletion.
- Upload as Google Doc via Drive create_file with contentMimeType `text/markdown` (conversion on). Drive write API rate-limits on rapid bulk uploads — space out or retry on "Resource exhausted".
- If Lars edits a Doc in Drive while traveling, reconcile changes back into the local .md on return (local is source of truth).
