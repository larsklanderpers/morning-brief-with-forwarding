---
name: file-verification-staging-cache
description: "Device-bridge staging can serve STALE content for a repeatedly re-staged same-path file; verify on-disk state with device_bash, not stage+Read. When device_bash is down, bust the cache with device_list_dir on a SIBLING directory first. ALSO: the panel's window sweep must stage fresh from the device, never read the uploads snapshot. ALSO: Lars saves his hand-edits as new -rvN.md siblings — read the latest before revising, and before writing any published file."
metadata:
  type: feedback
sources: [cowork-import]
imported_at: 2026-09-15T13:26:00Z
---

**Rule:** To verify the current on-disk state of a file I read more than once at the SAME path in a session (e.g. `SUBSTACK_INDEX.md`, a week plan), use `device_bash` (`sha256sum` / `sed -n` / `cat`) as ground truth. Do NOT rely on `device_stage_files` + Read for re-verification of a path I already staged earlier.

**Why:** On 2026-07-19, `SUBSTACK_INDEX.md` appeared to keep "reverting" to an older ascending version after every commit. Instrumented test proved the disk was correct and stable the whole time: `device_bash sha256sum` on the mount returned the new/correct hash and held steady across 25s untouched, while a FRESH `device_stage_files` of the same path returned the OLD content (different hash) — yet reported CURRENT metadata (matching mtime + byte size). So the staging layer / uploads dir-cache served a stale snapshot with fresh-looking metadata. It only affected the index because that's the one file re-staged repeatedly at one path; one-off draft files (fresh `-rvN` filenames) staged once and read correctly. There is NO on-device automation, sync, or pipeline rewriting the file (`briefing_agent.py` never references it; no git; no sync markers — all checked).

## ★★ 12 Sep 2026 — it fired again, WITH `device_bash` UNAVAILABLE, and `device_list_dir` was cached too

The Sat 12 session updated the week-plan status board while the `device_bash` mount was down all session (`no Plan9 drive shares mounted`), so rule 1's ground-truth check was not available. What happened:

- `device_stage_files` reported **138,807 bytes** (the Sun 13 chat's v2.9) and, on a later re-stage of the same path, served **130,159 bytes** of v2.8 content while still reporting 138,807 in its metadata.
- After a correct commit, **`device_list_dir` ALSO returned the stale 130,159 size** — so the directory listing is cached on the same layer, not just the file body. Two independent-looking checks agreed with each other and were both wrong.
- This produced a convincing false alarm that the board had been clobbered and that the Sun 13 chat's update had been lost. It had not.

**★ THE CACHE-BUSTER, when `device_bash` is down:** call `device_list_dir` on a **SIBLING directory** (e.g. `References\primary-sources`), then re-list the directory you actually care about. The intervening call invalidates the cached listing and the second call returns true sizes. This resolved it in one round trip after ten minutes of chasing a phantom lost update.

**Corollary — do not "fix" a phantom revert by force-committing blind.** Re-derive the merged content from the newest copy you actually hold, confirm your own markers are in it, commit, then bust the cache and verify the byte size matches what you wrote. On 12 Sep the final state was correct (143,416 bytes, both chats' work present) and the intermediate panic was entirely cache artifact.

**★ And use `expectedMtimeMs` on every shared-file commit, taken from the stage result and nothing else.** On 12 Sep a board commit was correctly REJECTED because the expected mtime had been guessed from a pattern rather than read from the stage response. The guard working is the good outcome: re-stage, reapply the change to the fresh copy, commit with the real value. Never reach for `force` to get past a guard you tripped yourself.

## ★★ 12 Sep 2026 — THE PANEL'S WINDOW SWEEP READ A STALE SNAPSHOT AND CALLED A FILE NON-EXISTENT

Seat 5 ran the cross-piece window sweep against `/mnt/user-data/uploads/...`, listed all four Substack folders "by hand plus a filesystem-wide search," and reported — with high confidence, twice — that **no forward draft existed for Sun 13 → Sat 19.** It then flagged a project-memory line claiming a Sun 13 capstone had been drafted as a probable memory error.

**The memory was right and the sweep was wrong.** `substack_draft_four-numbers-no-instrument_2026-09-13.md` existed on the device, drafted by the Sun 13 chat the same day. The uploads directory is a **snapshot of what this session staged**, not a live view of the folder — so a file another chat wrote after the last stage is invisible to it, and a filesystem search of the container will confirm its absence with total confidence.

**RULE: the window sweep stages fresh from the device.** Before the sweep, `device_list_dir` the three Substack folders on the device and stage anything dated inside the window that is not already in uploads. A backward-only or snapshot-only sweep is blind in exactly the direction the charter says matters most — the forward drafts. And per [[absence-verification]], "not in the uploads folder" is a TOOL LIMIT, never evidence that a piece was not written.

(In this instance the late check came back CLEAR — Sunday's own second paragraph already summarises Saturday — but that was luck, not process.)

**How to apply:**
1. Trust `device_commit_files` — commits DO land on disk correctly. Do not re-commit because a staged re-read looks reverted.
2. To confirm a file's real state, `device_bash sha256sum`/`sed`/`cat` the mount path — that is ground truth. **If the mount is down, bust the cache with a sibling `device_list_dir` call, then re-list.**
3. If a staged Read looks stale or "reverted" for a path staged earlier this session, suspect the cache FIRST; verify before "fixing" anything.
4. Never diagnose an on-device automation/sync problem from a stale staged read alone — instrument it (hash disk before/after commit; compare disk-hash vs staged-copy hash; compare byte size against what you wrote).
5. **Stage the cross-piece window fresh from the device at the start of every panel run.** Never let a seat conclude a forward draft does not exist from a container-side listing.

---

**Rule 2 (Lars's hand-edits live in NEW -rvN.md siblings — read the latest before you revise).** When Lars edits a draft himself, he saves it as a NEW sibling file with a bumped suffix (e.g. he took `substack_draft_<slug>_<date>.md` and saved his edits as `substack_draft_<slug>_<date>-rv1.md`). Before producing ANY next revision (rvN+1, panel pass, or fold-in), `device_bash ls` the draft's siblings, find the highest/most-recent hand-edited version, and `cat` it as ground truth — build the new revision on THAT, never on the base file, an earlier rv, or my own in-context copy.

**Why:** On 2026-07-31 I built rv2 of "Nothing Held" off the base `...2026-08-03.md` (my own copy) while Lars's substantial hand-edits lived in `...2026-08-03-rv1.md`. rv2 silently reverted all of his work (the medieval-siege parenthetical, the "cage built for a different actor" turn, the JFrog-chaining point, the "big door" beat, the Emperor-has-no-clothes close). He caught it — "you have reverted a bunch of stuff i already edited." Had to rebuild rv3 on his `-rv1.md`. His edits are the source of truth (per [[substack-review-workflow]]); losing them reads as not respecting his work.

**★ THIRD CASE, 12 Sep 2026 — AND IT FIRES AT *PUBLISH* TIME, NOT ONLY AT REVISE TIME.** After he published the Sat 12 Grok Bot piece, he asked for the week to be marked published. The published archive was built from **rv10 — the panel's last revision**. But a routine `device_list_dir` of `Substack Drafts\` showed **`-rv11.md`, timestamped five hours after rv10**: his own final polish pass, which is what actually went live. rv11 added the OpenClaw/Hermes beat that answers the panel's one unresolved objection, rewrote the close, and put the end-of-day evaluation into question form. Building the permanent record off rv10 would have silently reverted all three — the same failure as 2026-07-31, but landing in `Substack Published\` where it becomes the archive of record rather than a draft he can catch.

**RULE 2 EXTENDS: before writing ANY `substack_published_*` file, list the draft's `-rv*` siblings and build from the newest, which is almost always HIS, not the panel's.** The panel's last rv is the last *panelled* version; it is not the published text. And once the file is in `Substack Published\`, it must match the live post **verbatim** — mechanical typos in his final pass stay (three shipped on 12 Sep: `its` x2, `elses`), because editing a published piece is his call alone and an archive that silently differs from the post is worse than one carrying his typos. Flag them for a correct-forward; never fix them in place.

**How to apply:**
1. Before revising any named draft, list its `-rv*` siblings on disk and identify the newest one whose mtime/content shows a Lars edit (his versions won't have my status-header changelog; they'll have prose changes).
2. `cat` that file via `device_bash` and diff it mentally against my last version to catalog HIS changes; preserve every one of them verbatim (fix only mechanical typos silently — and NOT at all once the file is the published archive).
3. Weave new material as ADDITIVE beats around his prose; never wholesale-replace a paragraph he hand-wrote.
4. If unsure which file is "his," ask which rv to build on rather than guessing off the base.
5. **At publish/reconcile time, re-run step 1 before creating the `substack_published_*` file.** His final pass usually lands after the panel has stopped looking.
