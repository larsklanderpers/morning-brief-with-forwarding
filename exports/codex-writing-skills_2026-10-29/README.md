# Writing skills: Codex export (29 Oct 2026)

Eight skills from the Substack writing pipeline, plus the voice and charter files they load.

## What is in here

| Skill | Source copied from | Notes |
|---|---|---|
| `day-start` | installed Claude skill | boots a per-piece chat |
| `week-plan` | installed Claude skill | drafts the Monday plan and slot gates |
| `writing-flow` | installed Claude skill (20 Oct) | end-to-end orchestrator |
| `interviewer` | installed Claude skill (25 Sep) | see "Known drift" below |
| `research-assistant` | installed Claude skill (1 Oct) | |
| `editor-panel` | installed Claude skill | identical to `Writing Flow\03_editor-panel.SKILL.md` |
| `substack-notes` | installed Claude skill | |
| `final-review` | repo `Writing Flow\04_final-review.SKILL.md` | never installed in Claude; Pangram measurement only |

`references/` holds the files the skills tell the agent to load before writing:

- `feedback_lars_writing_voice.md`, `feedback_lars_contractions.md`, `feedback_lars_absolutes.md`: the LIVE copies from Claude project memory (newer than the `Writing Flow\` snapshots)
- `lars-about-me.md` (taste profile) and `SLOT_CHARTER.md`

The only change from the originals: every em-dash became `--` and every en-dash became `-` (house rule).

## Install in Codex

Codex reads skills as `<name>/SKILL.md` folders with `name` and `description` frontmatter, which these already are.

```powershell
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\skills\*" "$HOME\.codex\skills\"
```

Put the `references/` files where the skills expect them, or tell Codex where they are (see the AGENTS.md block below). The skills address project files by path relative to `D:\vc-personal-projects\Morning Brief with Forwarding\`, so run Codex from that folder.

## Claude-only tools the skills mention, and what to do in Codex

| Skill text says | In Codex |
|---|---|
| `device_bash` / `device_stage_files` (day-start) | plain shell in the repo folder |
| `project_memory_read` / "project memory" | read `references\` (or `References\memory\` in the repo) |
| `AskUserQuestion` | ask in chat |
| `WebFetch`, `mcp__Firecrawl__firecrawl_scrape` | Codex web search / fetch, or a Firecrawl MCP if you add one |
| "run the panel as a subagent with file paths" | run it inline, or in a separate Codex task, pointing at the files |
| Slack `#heinlein-inbox` / `#heinlein-out` | needs a Slack MCP in Codex; otherwise skip and say so |
| Pangram (final-review) | needs the Pangram API key in Codex's environment |

## Known drift

- `interviewer`: the repo copy (`Writing Flow\01_interviewer.SKILL.md`) has two passages the installed one lacks: loading `lars-about-me.md` and the taste-interview transcript, and the rule that the "reader's calculus" close is rationed rather than the default. The installed copy is exported because it is what actually runs; merge those two passages in if you want them.
- `writing-flow`: the installed copy ends at `substack-notes`; the older repo copy ends at `final-review`. Both stages are exported.

## AGENTS.md block (optional)

Paste into the repo's `AGENTS.md` so Codex loads voice before any writing:

```
Before drafting or proposing wording for any Substack piece, read:
references/feedback_lars_writing_voice.md, references/feedback_lars_contractions.md,
references/feedback_lars_absolutes.md, references/lars-about-me.md.
Before writing a week plan, read references/SLOT_CHARTER.md.
Never use em-dashes or en-dashes. Never publish or send anything; Lars does that.
```
