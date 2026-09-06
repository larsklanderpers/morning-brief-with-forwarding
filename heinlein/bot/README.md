# Heinlein bot

The self-hosted Slack app that replaces the polling intake task. Design and reasoning:
`References/DESIGN_heinlein-bot_2026-09-06.md`. Contract it implements: `../skills/intake.md`,
`../reactions.md`, `../channels.json`.

## Files

| File | Role |
|---|---|
| `manifest.yaml` | paste into Slack's "create app from manifest" |
| `events.py` | pure: Slack event in, Job out. All the "what counts as an instruction" rules. Tested |
| `runner.py` | runs `claude -p` in the repo folder, parses the JSON result. Tested |
| `slack_io.py` | every Slack call: post, react, upload, download, permalink |
| `state.py` | the shared `heinlein_state.json` processed map, plus a crash-safe job queue |
| `app.py` | the Bolt Socket Mode app, one worker thread, `/heinlein` command |
| `post.py` | post a draft or note to `#heinlein-out` as Heinlein, file attached. CLI and slash command |
| `Start-Heinlein.ps1` | foreground start, used by the scheduled task |
| `Install-HeinleinTask.ps1` | registers a logon task that keeps the bot running |
| `.env.example` | the two tokens and three settings; copy to `.env` |

## Setup, in order (Lars does 1 to 3)

1. **Create the Slack app.** api.slack.com/apps, "Create New App", "From a manifest", workspace
   `lars-klander-personal`, paste `manifest.yaml`. Install to workspace. On the app page:
   Basic Information, App-Level Tokens, generate one with scope `connections:write` (that is the
   `xapp-` token). OAuth and Permissions holds the Bot User OAuth Token (`xoxb-`). Copy
   `.env.example` to `.env` and paste both. Never paste them anywhere else.
2. **Invite the bot** to the four channels: in each of `#heinlein-briefs`, `#heinlein-inbox`,
   `#heinlein-out`, `#heinlein-log`, type `/invite @Heinlein`. They are private, so this is
   required.
3. **Install and log in to the Claude Code CLI** once, as your normal user:
   `npm install -g @anthropic-ai/claude-code` (or the native installer from the docs), then run
   `claude login` in a terminal and finish the browser step. Check with `claude -p "say OK"`. If
   the CLI is not on PATH, put its full path in `CLAUDE_CLI` in `.env`.
4. **Dry run.** `pip install -r heinlein/bot/requirements.txt`, then `.\Start-Heinlein.ps1` from
   this folder. The log channel gets "bot online". Drop a link in `#heinlein-inbox` and watch:
   an hourglass appears, the reply lands in the thread, the hourglass becomes a tick.
5. **Install as a task.** Elevated PowerShell: `.\Install-HeinleinTask.ps1`. Reboot once and post
   `/heinlein status` in Slack to confirm it came back and the CLI is still logged in.
6. **Retire the poller.** In the desktop app's Scheduled sidebar, disable `heinlein-intake`.

## What it does with each event

- New top-level post in `#heinlein-inbox`: one intake job per `intake.md`. Reply in thread, ✅.
- Reply by Lars in any Heinlein thread: a follow-up job with the thread text attached.
- One of 📌 🔍 ✏️ ❌ 👀 from Lars on a message in briefs, inbox or out: the command in
  `reactions.md`. Each reaction is its own job and its own receipt.
- `@Heinlein <question>` in a thread: answered in the thread.
- Anything from anyone else, any other channel, or the bot itself: dropped.

While a job runs the message carries ⏳. On success it carries ✅. On failure the thread gets one
plain sentence saying so and the ⏳ is removed, no ✅, so it is easy to find and retry (react again,
or reply "again").

## Posting a deliverable

From any Claude Code session or a terminal:

```bash
python heinlein/bot/post.py "Substack Drafts/substack_draft_opt-out-proxy_2026-09-08.md" --kind Draft --state "v1, not panelled"
```

Or in Slack: `/heinlein post Substack Drafts/substack_draft_opt-out-proxy_2026-09-08.md`.
Cowork sessions without a shell keep using the connector per `../common/post-to-out.md`; the bot
watches both shapes.

## Cost and auth in one paragraph

The runner shells out to the CLI under your login, so jobs spend your subscription's usage window
and nothing else. If that ever crowds out your interactive work, set `ANTHROPIC_API_KEY` in `.env`
and the same runner bills per token instead; each job's `cost_usd` is already logged so you can
compare before switching. Headless runs cannot use claude.ai connectors, which is why the bot does
its own Slack I/O and why the three morning briefs stay as desktop-app scheduled tasks.

## Operating

- Logs: `heinlein/bot/logs/heinlein-bot.log`, rotated daily, 14 days kept.
- Queue: `heinlein/bot/queue/`, one file per in-flight job; replayed on start.
- Downloads: `heinlein/bot/downloads/<ts>/`, the attachments intake read. Safe to clear.
- Tests: `python -m pytest -q heinlein/bot/tests`.
