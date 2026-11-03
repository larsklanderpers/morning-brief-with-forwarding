---
date_first_seen: 2026-08-10
date_updated: 2026-08-10
source: Anthropic blog 7 Aug 2026 + Claude Code docs (primaries) / flagged via The Anthropic Stack, 10 Aug 2026
url: https://claude.com/blog/auto-mode-default-in-claude-code
brief: ai
threads: [Trust Boundaries, AI Attack Surface, Practitioner - Coding Ground Truth]
beat: AI / Agentic tooling / Human-in-the-loop
status: developing
used_in:
---

# Auto mode becomes the default — the approver is now a model

**What happened.** On **7 August 2026** Anthropic announced that from **14 August 2026**, new Claude Code
sessions on **Pro, Max and Team plans** default to **auto mode**: the per-tool-call permission prompt is
replaced by a **separate classifier model** that reviews each action before it runs. It remains **opt-in on
Claude Enterprise, the API, Bedrock, Vertex/Agent Platform and Microsoft Foundry**. Auto mode itself is not
new — the engineering write-up is dated 25 Mar 2026. What changed is *which mode a session starts in*.

**Why it matters.** This is the human-in-the-loop approval boundary being **reassigned to software, on a
date, by the vendor, as a default**. Not weakened, not removed — *reassigned*. Every argument on the Trust
Boundaries thread since GhostApproval has been about who is standing on the boundary. As of Friday the
answer, for the most-used agentic coding tool in the world, is a classifier.

## The primary, verbatim

Docs (repeated at `permission-modes` and `auto-mode-config`):

> "Starting August 14, 2026, auto mode becomes the default permission mode for new sessions on Pro, Max, and
> Team plans. You can switch modes at any time. A default you set yourself stays in place unless you accept
> the one-time switch prompt, and a default your organization manages is unchanged."

> "Auto mode lets Claude execute without routine permission prompts. A separate classifier model reviews
> actions before they run, blocking anything that escalates beyond your request, targets unrecognized
> infrastructure, or appears driven by hostile content Claude read. Explicit ask rules still force a prompt."

> "Auto mode reduces permission prompts but does not guarantee safety. Use it for tasks where you trust the
> general direction, not as a replacement for review on sensitive operations."

Engineering post, 25 Mar 2026 — the honest line, and it is Anthropic's own:

> "The 17% false-negative rate on real overeager actions is the honest number."

## The mechanism, accurately

- The classifier sees **user messages and the agent's tool calls**, with assistant messages and tool
  results stripped out — so hostile file or web content cannot argue with the reviewer. That is a genuinely
  good design and should be said out loud.
- **~40 categories are blocked with zero configuration**: `curl | bash`, production deploys and migrations,
  IAM/repo permission grants, force push, `terraform destroy`, `git reset --hard`, writing to secret
  managers/DNS/TLS, merging an unapproved PR, disabling CI checks, printing live credentials, opening
  tunnels or reverse shells, writing to Claude Code's own session transcripts.
- **Newly unprompted**: local file ops in the working directory, dependency installs from lockfiles,
  read-only HTTP, reading `.env` and sending credentials to their matching API, and **pushing to any branch
  of the repo you are working in, including the default branch**, plus PR creation.
- **Circuit breaker**: "If the classifier blocks an action 3 times in a row or 20 times total, auto mode
  pauses and Claude Code resumes prompting."
- **`permissions.deny` is evaluated before the classifier** — "Neither the classifier nor user intent can
  override it." `permissions.ask` forces a prompt the classifier cannot auto-approve. `disableAutoMode` in
  managed settings removes it org-wide.
- Auto-mode config is **not readable from `.claude/settings.json` or `.claude/settings.local.json`**, "so a
  checked-in repo or a build step could otherwise inject its own allow rules." Someone thought about that.

## The two things a draft must not get wrong

1. **"Stops asking" is wrong.** It stops asking *routinely*. Deny rules, ask rules, ~40 default blocks and
   the circuit breaker all still interrupt. The un-configured state is the **tight** one; configuration
   mostly *loosens* it to cut false positives. The Substack framing — *"a live gun with the safety off"* —
   inverts this, and a reader who has read the docs will bin the piece.
2. **Plan scope.** Pro/Max/Team only. **Enterprise, API, Bedrock, Vertex and Foundry remain opt-in**, which
   means most regulated shops are untouched on the 14th. Omitting this inverts the risk picture for exactly
   the audience that reads him.

## The better story underneath

The July–August changelog is dense with **permission-bypass fixes**: hidden commands in zsh `[[]]` regex
conditionals (v2.1.221/222), commands "padded with tabs or invisible Unicode" hiding from the approval
dialog (v2.1.223), commands over 10,000 characters (v2.1.214), a PowerShell 5.1 bypass (v2.1.214),
`bypassPermissions` in agent definitions ignoring org policy (v2.1.223), dynamic `import()` escaping the
workflow sandbox (v2.1.223).

That is a string-parsing gate leaking for months. Which is simultaneously **the best argument for moving
adjudication to a model** and the reminder that **the prompt being replaced was never the control anyone
thought it was.** The prompt was the sign. The deny rule is the governor. Straight into the 31 Jul ladder.

Anthropic's reported safety case: an experiment with **1,053 users** found humans caught **13.6%** of
dangerous commands versus **89%** caught by auto mode. Worth carrying — it is the strongest version of
"the human was never doing the job we credited them with," and it comes from the vendor, which is both its
power and its weakness. Attribute it as Anthropic's own reported figure.

## Observations

- **2026-08-10** — First seen via *The Anthropic Stack*, "Claude Code Stops Asking First" (published today).
  The Substack's directional read is defensible; its tense and its "safety off" characterisation are not.
  Verified against Anthropic primaries the same morning.

## Feeds

- [[Trust Boundaries]] — the approval boundary, reassigned to software on a published date
- [[AI Attack Surface]] — the newly-unprompted list includes reading `.env` and pushing to the default branch
- [[Practitioner - Coding Ground Truth]] — this is the tool his readers actually use
- [[Anthropic inference hooks - a deny switch you hold]] — same vendor, same question: which control do *you* hold
- [[MCP servers as supply chain - the numbers are in]] — "human-as-the-rubber-stamp" now has a vendor conceding the rubber stamp was 13.6% effective

## Open

- **The date is inside the publishing week.** 14 Aug is Friday. Anything written for that slot is either
  same-day or stale.
- Did the classifier ship with an published eval beyond the 1,053-user experiment? The 17% false-negative
  figure is from March; is there an August number?
- **[VERIFY] before use:** the 13.6% / 89% / 1,053-user figures are reported in Anthropic's blog prose,
  read here through a verification pass rather than quoted from the post verbatim. Pull the exact sentences
  before printing them.
