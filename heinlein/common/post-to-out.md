# Post a deliverable to #heinlein-out

For any session, Cowork or Claude Code, that finishes a draft, a revision, a research note, a
panel verdict or a week-plan change. The Slack connector is the same claude.ai connector in both,
so this works from either. Nothing here needs a shell.

Channel ID: read `out` from `heinlein/channels.json` (currently `C0BVCSV3MFB`). Never post a
deliverable anywhere else.

## 1. The parent message (always)

One `slack_send_message` to `out`, under 5,000 characters:

```
*<Kind>: <Title>*
<repo-relative file path>
<one line of state: "v1, not panelled" / "rv3, panel 9.1, clears bar, pending sign-off" / "research note, 4 primaries">
<the first paragraph of the piece, or the bottom line of the note>
React: ✏️ another pass · 🔍 re-verify a claim (say which in a reply) · ❌ park it · ✅ receipt
```

Kinds: Draft, Revision, Research, Panel, Plan.

## 2. The full text (drafts and revisions)

Post the body as thread replies under the parent, each under 5,000 characters, split at
paragraph boundaries, in order. A 3,000-word piece is four or five replies. Do not truncate and
do not summarise; Lars reads the whole thing on his phone.

If the session has a shell (Claude Code does, Cowork may not), a file upload is cleaner:
`slack_get_file_upload_url` with the exact byte length, POST the bytes with curl to the returned
URL, then `slack_complete_file_upload` with `channel_id` = `out`, `thread_ts` = the parent, and a
`title`. Confirm the destination is `out` before completing; the share is irreversible.

## 3. Record

Append to `heinlein/state/posted/out_<YYYY-MM-DD>.json` (create if absent):

```json
{"ts": "<parent message_ts>", "kind": "Draft", "file": "Substack Drafts/...", "title": "..."}
```

One object per line is fine; intake reads the file as a list of parents to watch for reactions.
A Cowork session that cannot write JSON reliably may instead reply in the Slack thread with the
line `heinlein: recorded <file path>`; intake treats that reply as the record.

## 4. What comes back

Intake honours reactions on the parent: ✏️ runs another revision pass with the editor panel,
🔍 re-verifies the claim named in a thread reply, ❌ parks the draft and notes it in the index.
Replies in words beat the emoji. Intake answers in the same thread.
