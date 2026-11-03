---
type: intake
date: 2026-09-13
source_url: https://p.superdesign.dev/draft/73d501d5-ee18-4ccb-bf78-2d26b6da1f60 ; https://p.superdesign.dev/draft/996218be-abb6-4bee-9370-9916f999aa3d
slack_permalink: https://lars-klander-personal.slack.com/archives/C0BVCSV0PJ5/p1789256629452949 ; https://lars-klander-personal.slack.com/archives/C0BVCSV0PJ5/p1789256644329819
slack_ts: ["1789256629.452949", "1789256644.329819"]
slack_ts_related: ["1789256671.365289", "1789256742.853899", "1789256768.944209"]
lars_note: "(two bare links, no note; instructions came in the next messages, quoted below)"
reactions: []
verdict: backgrounder - two Superdesign drafts of Daniel's Scout (RunScout) marketing pages; private third-party work, nothing planned to attach it to; Lars asked for the batch to live in its own container
filed_to: Research Notes/intake (this file); container index at Research Notes/runscout/README.md; review request queued in References/heinlein_queue.md; no vault Signal
---

# Scout marketing page drafts on Superdesign (homepage and "What it does")

Two of five messages Lars sent to #heinlein-inbox on Sat 12 Sep 2026, 16:43:49 to 16:46:08 PDT. The
bot's run at the time failed on all four of these ("Claude returned non-JSON output") and the earlier
intake note (`intake_2026-09-12_runscout-evaluation.md`) recorded that the text of these two was
unrecovered. It is recovered here from Slack directly. Both pages fetched with Firecrawl on 13 Sep
(status 200, Superdesign preview timestamps 2026-09-13 01:52 UTC). No text on either page was
addressed to Heinlein. Images on the pages (projection board, session log, Now board, Needs
Attention, Morning Digest) were not read; only their captions.

Private: these are Daniel's product drafts. Not a Substack source without Lars's say.

## Extracted

### Draft 1: homepage. Page title "Scout - There can be only one record for your team's AI"

- Hero: "THERE CAN BE ONLY ONE." Sub: "ONE RECORD. EVERY AGENT READS IT. EVERY AGENT WRITES IT."
  Descriptor: "Scout is the one durable record of what the team intended, changed, and decided. Kept
  current so every agent and the person running the team sees what is true now. No re-briefing. No
  drift." CTAs: Start the trial, Get a demo (both "#" placeholders).
- Stamp: "NO SCRUM. / NO BULLSHIT."
- Ticker: nothing important is lost / only what's current reaches the model / Claude, Cursor,
  Copilot, whatever's next / 15 days, every seat, no card.
- Side A, the problem: agent amnesia (agents rewrite each other's work); context bloat ("The model
  ignores 90% of it and hallucinates a file that doesn't exist"); the manual re-brief ("20 minutes").
- Side B, what Scout does: one append-only log ("Full parity"); current-state projection ("Only what
  changed and why is fed to the model"); zero re-explaining.
- Quote: "A folder grows until the model is guessing from last year." Attributed "Design partner,
  CTO", unnamed.
- "Session start" section: "When the quickening happens, your agents connect to the source."
- For the person who runs the team: "You see the record exactly as the agents do." "No
  surveillance, just the durable intent of the team." Three outputs: Now board (active intent,
  blockers, decisions), Needs attention (stale facts, agent handoff contracts), Morning digest (in
  Slack).
- Stats row: "$14.99 Per seat / monthly billed"; "4x Velocity gain (internal measurement)"; "One
  link: connection to all agents via MCP". Footnote: "Honesty is the flex: 4x gain measured from 4.0
  to 17.1 commits per developer per week in our own team, Jan-Jun 2026. N=2. Your results depend on
  your rules."
- Not this: not a coding agent, not a shared wiki, not a chatbot for your repo, not a commit
  dashboard, not vendor memory.
- Close: "Stop re-briefing the room. Start the trial. 15 days. Every seat. No credit card required."

### Draft 2: "Scout - What it does" (architecture / MCP spine)

- Hero: "One durable record every agent reads/writes." "A durable spine for your AI fleet."
- [01] During work: agents update the record as they execute, noting abandoned paths, new
  dependencies, technical debt.
- Eight kinds of entry: architecture, dependency, deviation (tech debt, workarounds), intent,
  abandoned, convention, blocker, milestone.
- [02] Current state: "A living, single-source projection of the codebase's intent. Not a wiki, not
  a commit log. The actual current state that governs every future action taken by the team."
- [03] Session start: agents read the record first. "The re-briefing tax is eliminated."
- [04] Between sessions: watchers beside GitHub, Linear and Slack evaluate state and surface
  attention needs to human managers.
- CTAs: Start the trial, Read the docs (Superdesign placeholder paths).

## Lars's note

The two link messages carry no text. The instructions for the batch, verbatim, in order:

- 16:44:31 (1789256671.365289): "Let's look at design feedback, business corpus, etc, and then also anything that jumps out at you"
- 16:45:42 (1789256742.853899): "There is also a document in my Google Drive called run scout something or other which is my initial feedback"
- 16:46:08 (1789256768.944209): "Put all of this into its own container and probably go ahead and make a cowork project on it and we'll track it there"
