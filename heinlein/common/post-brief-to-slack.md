# Post a brief to Slack

Runs at the end of each brief skill. Deterministic where it can be: the parser decides what the
messages say, you only send them and record where they landed.

## 0. Preconditions

- Read `heinlein/channels.json`. If `briefs` is an empty string, stop here and say in the summary
  "Slack not configured, brief on disk only". Do not improvise a channel.
- Load the Slack tools if they are not already loaded (one ToolSearch call):
  `select:slack_send_message,slack_add_reaction`
  (the tool names carry a connector prefix; search on the short names).

## 1. Render

```bash
python "D:\vc-personal-projects\Morning Brief with Forwarding\heinlein\scripts\brief_to_items.py" "<path to today's brief file>" --slack --legend "D:\vc-personal-projects\Morning Brief with Forwarding\heinlein\reactions.md"
```

The JSON has `parent` (one string) and `items` (index, title, section, url, text). If the parser
fails or returns zero items, post nothing, and report the error with the traceback in the summary.
Do not hand-write messages as a fallback; a broken parser is a bug to fix, not to route around.

## 2. Post

1. Send `parent` to the `briefs` channel with `slack_send_message`. The result carries
   `message_context.message_ts`; that is the parent timestamp. Keep it.
2. For each item in order, send `text` as a thread reply: same channel, `thread_ts` set to the
   parent timestamp. Do not set `reply_broadcast`. Keep each reply's `message_ts`.
   Send the replies as parallel tool calls in batches; Slack accepted 22 in one burst on the
   4 Sep dry run without a rate-limit error.
3. Slack rate-limits bursts. If a send errors, wait a few seconds and retry that one item once.
   If it fails again, continue with the rest and list the failed indexes in the summary.

## 3. Record

Write `heinlein/state/posted/<date_stamp>_<kind>.json`:

```json
{
  "kind": "cyber",
  "date_stamp": "2026-09-04",
  "file": "Daily Briefs/brief_2026-09-04.md",
  "channel": "C0XXXXXXX",
  "parent_ts": "1725400000.123456",
  "items": [
    {"index": 1, "ts": "1725400001.000100", "title": "...", "section": "...", "url": "..."}
  ]
}
```

Intake uses this map to turn a reaction on a thread reply back into the item it belongs to. If a
ts was lost, record `"ts": ""` for that item; intake falls back to matching on title text.

## 4. Report

In the summary to Lars: the parent message link, the item count posted, and any failures. One line.
