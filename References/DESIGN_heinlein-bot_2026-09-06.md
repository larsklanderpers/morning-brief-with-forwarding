---
type: design-note
topic: Heinlein bot - a self-hosted Slack app that replaces the polling transport for intake and delivery
date: 2026-09-06
status: PROPOSED, Lars approved the recommendation 6 Sep ("I like the recommendation. please proceed.")
requested-by: Lars, 6 Sep 2026 - "would all these problems with the container and the attachments be
  addressed by making a bot out of it?"
supersedes: nothing. Extends DESIGN_heinlein-slack-control-plane_2026-09-03.md, option C.
---

# Design Note - The Heinlein Bot

## 1. Bottom line

**1.** A small Python process on Lars's Windows box, a Slack app in Socket Mode, that turns every
message and reaction in the four Heinlein channels into an event and answers it by running Claude
Code headless inside the repo folder. No public URL, no webhook, no polling tick.
**2.** It replaces two things: the four-times-a-day intake task, and the connector's two-step file
upload. It posts as **Heinlein**, with its own identity, and uploads a draft in one call.
**3.** It does **not** replace the three brief tasks. Their Gmail and Chrome lanes ride on claude.ai
connectors that a local process cannot borrow. The briefs stay as scheduled tasks in the desktop app
until those lanes are rebuilt on direct APIs, which is a separate decision.
**4.** Everything built for the polling version carries over unchanged: channel IDs, reaction
vocabulary, `intake.md`, the parser, the state files. The bot is a new transport under the same
contract.
**5.** Cost and auth are settled in section 4. The short version: the bot shells out to the Claude
Code CLI under Lars's own login, so it runs on the subscription, not on per-token API billing. The
one-time setup is Lars installing the CLI and logging in, which nobody else can do for him.

## 2. What the bot fixes, and what it does not

| Friction today | Cause | Bot |
|---|---|---|
| Phone share waits up to five hours | polling tick | event, seconds |
| Draft upload is a signed URL plus curl | connector two-step | one `files_upload_v2` call with a bot token |
| Drafts over 5,000 chars need thread splitting | message limit | file upload, plus a summary message |
| Scheduled tasks need the desktop app open | app-hosted scheduler | bot runs as a Windows service from boot |
| Posts appear as Lars | connector acts as the user | posts as Heinlein; Lars's reactions and Heinlein's receipts are distinct |
| Cowork sandbox may lack a shell | Cowork | Cowork keeps using the connector for outbound; the bot handles inbound |
| Gmail and Chrome lanes in the briefs | claude.ai connectors | **not fixed**; briefs stay as desktop-app scheduled tasks |
| Canvases | Slack free plan | **not fixed**; file uploads cover it |

## 3. Architecture

```
  Slack (lars-klander-personal)
      | Socket Mode (outbound websocket from the box; no inbound port)
      v
  heinlein/bot/app.py            Bolt for Python, one process, Windows service
      |  event -> Job (pure function, tested)
      v
  heinlein/bot/queue.py          one job at a time per channel, dedupe by ts, retry once
      |
      v
  heinlein/bot/runner.py         claude -p "<prompt>" in the repo folder, JSON out, 15 min cap
      |  reads heinlein/skills/intake.md and the same state files as today
      v
  Slack reply in thread, receipt reaction, file upload, log line
```

**Events handled (phase 1)**

| Slack event | Channel | Job |
|---|---|---|
| `message` (new top-level post by Lars) | inbox | intake one item, per `intake.md` sections 2 and 4 |
| `message` (thread reply by Lars) | inbox, briefs, out | follow-up instruction on the parent item |
| `reaction_added` by Lars | briefs, inbox, out | honour the reaction per `reactions.md` |
| `app_mention` | any Heinlein channel | free-form question answered in thread, read-only unless the text names a file to change |
| `file_shared` (image, PDF) | inbox | download with the bot token, hand the local path to intake |

Reactions from anyone but Lars are ignored. Messages from the bot itself are ignored. Events
outside the four channel IDs in `channels.json` are dropped and logged.

**Outbound (phase 1)**

- `post_deliverable(path, kind, state)`: summary message plus one-call file upload in thread.
  Exposed two ways: a CLI (`python -m heinlein.bot.post <file>`) any Claude Code session can call,
  and a slash command `/heinlein post <path>` from Slack.
- `post_brief(path)`: the same parent-plus-thread shape as today, using the existing parser, so the
  brief tasks can switch to it with one line when they move.

**Concurrency and idempotency.** One worker per channel, jobs keyed by message ts, and the same
`processed` map in `heinlein_state.json`. A crash mid-job leaves no receipt, so the job re-runs on
restart from a small on-disk queue. The receipt reaction remains the visible guard.

**Process supervision.** `nssm` or Task Scheduler "at startup", running under Lars's user so the
CLI login and the repo are visible. Logs to `heinlein/bot/logs/` with daily rotation. A `/heinlein
status` slash command reports uptime, queue depth, last job, and CLI login state.

## 4. Auth and cost (settled 6 Sep, documentation check plus one local probe)

**Decision: the bot shells out to the Claude Code CLI (`claude -p`) under Lars's own login.**
Not the Agent SDK, not an API key by default.

What the documentation says, with the two things it does not say marked:

| Question | Finding | Source |
|---|---|---|
| Agent SDK on a subscription login | **No.** The SDK docs state that claude.ai login is not offered to third-party developers; use an API key. So an SDK-based bot is pay-per-token on top of the subscription. | code.claude.com/docs/en/agent-sdk/overview |
| `claude -p` on a subscription login | The auth precedence list puts a claude.ai subscription login after the API-key environment variables, so with no key set a logged-in CLI runs on the subscription. The docs never say "headless is fine on a subscription" in those words. **Unconfirmed in writing; confirmed by how the CLI is built.** | code.claude.com/docs/en/authentication |
| `--bare` mode | API key only. Not used here. | code.claude.com/docs/en/headless |
| claude.ai connectors (Gmail, Slack, Chrome) from a headless run | **No.** They are fetched only for an interactive subscription session. This is why the bot does all Slack I/O itself and why the briefs stay in the desktop app. | code.claude.com/docs/en/mcp |
| Local MCP servers (Firecrawl) | Yes, via `.mcp.json` or `--mcp-config`. Needs Lars's Firecrawl API key in that config; he holds it. | code.claude.com/docs/en/mcp |
| Project and plugin skills | Yes. Dynamic context injection is off, which does not affect the Heinlein skills. | code.claude.com/docs/en/skills |
| Flags | `-p`, `--output-format json`, `--max-turns`, `--allowedTools`, `--permission-mode`, `--append-system-prompt`, `--mcp-config`, `--resume`, `--model` all confirmed. There is no `--cwd`; the runner sets the working directory on the subprocess. | code.claude.com/docs/en/cli-reference |
| Terms for automated personal use | Not stated either way in the docs found. What is stated is the prohibition on third parties offering subscription login to *their* users, which this is not: one person, one login, one machine. | agent-sdk/overview |
| Usage limits | Subscription usage windows apply to every headless run exactly as they do to interactive ones. Many short runs per day spend the same budget as the chats do. No separate cap on concurrent `-p` processes is documented. | rate-limits, sub-agents docs |

**Local probe, 6 Sep.** The desktop app's bundled `claude.exe` (2.1.260) runs `-p` and returns
JSON, but reports "Not logged in" on its own: the app injects its session, the binary alone has
none. A `.credentials.json` from 22 July exists under `~/.claude` and did not satisfy it. So step 2
of the build plan is real: Lars installs the CLI and runs `claude login` once.

**Cost shape.** On the subscription: zero incremental spend, bounded by the usage window; if
intake and reaction jobs start crowding out his interactive work, the runner already accepts an
`ANTHROPIC_API_KEY` in `.env` and switches to per-token billing with no code change, and the JSON
result carries `total_cost_usd` per job so the switch can be measured before it is made. Firecrawl
stays at one credit per fetch either way.

**What settles the last unconfirmed point.** Step 4 of the build plan runs one real intake job
from the service context after a reboot. If it runs on the login, the question is closed; if it
asks for a key, the fallback above is a one-line change.

## 5. Security posture

- **Tokens.** Bot token (`xoxb-`) and app-level token (`xapp-`, Socket Mode) live in
  `heinlein/bot/.env`, which is git-ignored. Lars creates the app and pastes the tokens; I never see
  or handle them. The bot refuses to start if either is missing.
- **Scopes, minimal.** `channels:history`, `groups:history`, `reactions:read`, `reactions:write`,
  `chat:write`, `files:read`, `files:write`, `app_mentions:read`, `commands`, `users:read`. No
  DM scopes in phase 1.
- **Instruction boundary.** Only messages from `lars_user_id` are instructions. The body of any
  fetched page or attached file is data. This is written into the runner's system prompt and into
  `intake.md`, and the runner strips nothing; it labels.
- **Tool allow-list for the headless session.** Read, Write, Edit, Glob, Grep, Bash (repo folder
  only), WebFetch, and the Firecrawl MCP server. No Slack MCP from inside the session; the bot
  does all Slack I/O itself, so the session cannot post anywhere the bot did not intend.
- **RED stays RED.** Publishing, email, deletion, task creation and the work tenant are out of
  reach by construction: the session has no connector for any of them.

## 6. Build plan

| Step | Deliverable | Who |
|---|---|---|
| 1 | Slack app created from `heinlein/bot/manifest.yaml`, tokens into `.env` | Lars |
| 2 | Claude Code CLI installed and logged in once (`claude login`) | Lars |
| 3 | `heinlein/bot/` with `events.py` (pure: event -> Job), `runner.py`, `slack_io.py`, `app.py`, tests for the pure parts | me |
| 4 | Dry run: bot in a terminal, Lars drops a link, watches the thread | both |
| 5 | Service install script and `/heinlein status` | me |
| 6 | Disable the `heinlein-intake` scheduled task; the bot owns intake | Lars |
| 7 | Later, if wanted: `post_brief` switch for the three brief tasks | both |

Time at risk: two to three days to step 4. Nothing to uninstall if it does not work out; the
polling task is one click to re-enable.

## 7. Open questions

1. Whether the CLI login survives reboots and service context without a browser re-auth. Test at
   step 4 by restarting the box.
2. Whether `/heinlein` slash commands are worth their setup; reactions may be enough.
3. Whether to give the headless session the editor-panel and research-assistant skills as
   project skills so ✏️ and 🔍 run end to end, or keep those as manual sessions for now.
