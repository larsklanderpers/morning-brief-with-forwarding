# Research Note — Claude Code auto mode as default: the numbers and the mechanics

For: Fri 14 Aug 2026 piece (Trust Boundaries × Ad Hoc Regulatory Regime — *whose job is the guardrail*) · Depth: deep · Date: 2026-08-10
Companion to: `Vault\Writing\Signals\Auto mode becomes the default - the approver is now a model.md` (this note CLOSES its open `[VERIFY]`)

## Bottom line

**The headline number verifies exactly, and the methodology behind it matters more than the number does.**
The primary reads: *"The testers caught the dangerous command just 13.6% of the time (143 of 1,053), while
auto mode blocked 89% of the same commands (937 of 1,053)."* Same denominator, same commands — **but not the
same test.** The humans met a single injected prompt mid-task, in a study environment that was not their own
codebase, knowing they were being evaluated, with nothing at stake if they got it wrong. Auto mode was
evaluated separately against the same command set. Anthropic never claims the arms are equivalent; it also
never flags that they are not.

**This makes the argument stronger, not weaker, provided Lars says it himself.** 13.6% is a floor on human
vigilance, not a measurement of it. Even granting real practitioners three times the study's attentiveness in
their own repos with real consequences, you land near 40% and the seat is still mostly empty. Making that
concession in the piece is what stops a sharp reader making it for him.

**One complication he has to own:** the planned landing is *the deny rule is the governor*. On **7 August**,
the day of the auto-mode announcement, Anthropic patched a bug where **sandbox filesystem deny entries written
with a trailing slash were silently bypassable on Linux and macOS**. The governor had a leak too. Handled
honestly this is fine — deny rules are the only thing in the stack that is not a suggestion, and they still
need auditing — but it cannot be omitted.

---

## What's solid

**The study, verbatim and in full.**
> "In a controlled experiment with 1,053 paid professional testers, human review caught just 13.6% of dangerous commands, while auto mode caught 89%."

> "The testers caught the dangerous command just 13.6% of the time (143 of 1,053), while auto mode blocked 89% of the same commands (937 of 1,053)."

**The methodology, verbatim — this is the part to read twice.**
> "We hired 1,053 paid testers through a research vendor for a coding study. These participants worked in a test environment set up specifically for the study, not in their own codebases or on real projects. Participants knew they were being evaluated, but—following standard blind-study design—weren't told which behavior was being measured. Partway through each session, a single permission prompt was swapped for a clearly dangerous command, and the vendor recorded whether the tester approved it."

Note what this does and does not establish. It is a **single-trial, per-tester** measure of whether somebody
mid-task notices one injected prompt. "Clearly dangerous" is **never defined** in the post. And the auto-mode
arm was run against the same commands **separately**, not inside the live sessions.

**Anthropic's own limitation line.**
> "while we believe auto mode reduces risk for most users, it relies on classification systems and therefore does not eliminate risk."

**The red-team tradeoff, and it is unusually honest for a vendor.** After hardening against Apollo's attack set:
> "Auto mode caught about half of the attacks it previously missed, at a cost of missing about 2% of attacks it previously caught."

That is a stated precision/recall trade, disclosed voluntarily. Worth crediting explicitly — it is the kind of
disclosure the piece is asking regulators to demand elsewhere this week.

**The rollout, verbatim.**
> "Starting on August 14, new sessions on Pro, Max, and Team plans will run in auto mode."

> "Auto mode remains opt-in for now on Claude Enterprise, the Claude API, Claude Platform on AWS, Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry."

Announced **7 Aug 2026**; effective **14 Aug 2026**, which is the publication date.

**The mechanics (docs, confirmed).** `permissions.deny` is evaluated **before** the classifier and neither the
classifier nor user intent can override it. `permissions.ask` forces a prompt the classifier cannot
auto-approve. `disableAutoMode` in managed settings removes it org-wide. **~40 categories** are blocked with
zero configuration. Circuit breaker: **3 blocks in a row or 20 total** and auto mode pauses, with Claude Code
resuming prompting. The classifier sees user messages and tool calls with assistant messages and tool results
**stripped**, so hostile file or web content cannot argue with the reviewer. Auto-mode config is **not**
readable from `.claude/settings.json` or `.claude/settings.local.json`.

**The changelog — every claim in the vault note verifies, with dates and versions.**

| Bypass | Version | Date | Wording |
|---|---|---|---|
| Commands over 10,000 chars auto-running | 2.1.214 | 18 Jul | "commands over 10,000 characters now always prompt instead of running automatically" |
| PowerShell 5.1 session bypass | 2.1.214 | 18 Jul | "a permission-check bypass affecting commands run in Windows PowerShell 5.1 sessions" |
| zsh variable subscripts in `[[ ]]` treated as inert text | 2.1.214 | 18 Jul | "these commands now prompt for approval" |
| zsh hidden commands in `[[ ]]` regex conditionals | **2.1.221** | 4 Aug | "zsh could execute hidden commands in `[[ ]]` regex conditionals" |
| Worktree isolation bypass for destructive git | 2.1.222 | 4 Aug | isolation "now applies to file edits and Bash in every session type" |
| PreToolUse auto-allow hooks bypassing tool restrictions | 2.1.222 | 4 Aug | in background agent tasks |
| Tabs / invisible Unicode hiding part of a command | 2.1.223 | 6 Aug | "can no longer hide part of the command from the approval dialog" |
| `bypassPermissions` in an agent definition ignoring org policy | 2.1.223 | 6 Aug | "ignored the org bypass-permissions disable policy" |
| Dynamic `import()` escaping the workflow sandbox | 2.1.223 | 6 Aug | "run code outside the workflow sandbox" |
| **Sandbox deny entries with a trailing slash silently bypassable** | **2.1.224** | **7 Aug** | e.g. `denyRead: "~/.aws/"` — "silently bypassable on Linux and macOS" |

Correction to the vault note: the `[[ ]]` regex conditional fix is **2.1.221**, not 2.1.221/222.

---

## What's contested / watch out

**The comparison itself.** Not contested by any source, because nobody has interrogated it publicly yet — but
it will not survive a careful reader. Human arm: real people, one injected prompt, sandbox codebase, known
study, zero consequence. Classifier arm: offline evaluation against the same commands. **The right way to write
it is as the vendor's own reported figure with the design stated in the same breath**, which is both honest and
more interesting than the bare number.

**"Clearly dangerous" is undefined.** The post never says what the swapped command was. Do not characterise it.

**The 17% false-negative figure is from March.** It comes from the 25 Mar 2026 engineering post
("The 17% false-negative rate on real overeager actions is the honest number"), not from the August
announcement, and no updated figure has been published. **Do not present it as current.**

---

## Couldn't verify

- **Any independent replication or third-party evaluation** of the 13.6% / 89% comparison. Searched; none
  exists as of 10 Aug. Every number in this story is the vendor's.
- **Whether the classifier has a published eval beyond the 1,053-tester study and the Apollo red-team pass.**
  Nothing found.
- **What the swapped "clearly dangerous command" actually was.**

---

## The economics

The cost story is the cleanest of the week, and it is the one that rescues the capstone from being four days
of the same complaint.

A classifier call costs a fraction of a cent and runs on every tool call, all day, without fatigue. A human
approver costs a salary, and — on the vendor's own numbers, in the vendor's own study design — was catching
**143 of 1,053**. So **a classifier is cheaper than a colleague, and on this evidence it is also better than
the colleague was.** Every other instrument this week was narrow *because* it was cheap. This one is cheap and
wider. That is the honest exception, and printing it is what keeps the argument from being a complaint.

What the money does not buy is the seat. The classifier is a control the vendor operates and ships defaults
for. `permissions.deny` in **managed settings** is the one control the customer holds and neither the
classifier nor the user can override — and it is free, and almost nobody has written one. The cheapest
control in the entire stack is the one still sitting unclaimed.

---

## Drop-in facts

- "The testers caught the dangerous command just 13.6% of the time (143 of 1,053), while auto mode blocked 89% of the same commands (937 of 1,053)." — Anthropic, 7 Aug 2026
- "These participants worked in a test environment set up specifically for the study, not in their own codebases or on real projects." — same
- "Starting on August 14, new sessions on Pro, Max, and Team plans will run in auto mode." — same
- "Auto mode remains opt-in for now on Claude Enterprise, the Claude API, Claude Platform on AWS, Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry." — same
- "while we believe auto mode reduces risk for most users, it relies on classification systems and therefore does not eliminate risk." — same
- "Auto mode caught about half of the attacks it previously missed, at a cost of missing about 2% of attacks it previously caught." — same, Apollo red-team section
- "A separate classifier model reviews actions before they run, blocking anything that escalates beyond your request, targets unrecognized infrastructure, or appears driven by hostile content Claude read." — Claude Code docs
- Circuit breaker: 3 consecutive or 20 total blocks and auto mode pauses; prompting resumes. — docs
- Six distinct permission-bypass fixes shipped between 18 Jul and 7 Aug 2026 across v2.1.214, .221, .222, .223 and .224 — changelog
- "Fixed sandbox filesystem deny entries written with a trailing slash (e.g. `denyRead: \"~/.aws/\"`) being silently bypassable on Linux and macOS" — v2.1.224, 7 Aug 2026

---

## The two standing do-not-writes (unchanged, now re-confirmed)

1. **Never "Claude Code stops asking."** It stops asking *routinely*. Deny rules, ask rules, ~40 zero-config
   blocks and the circuit breaker all still interrupt. **The un-configured state is the tight one**;
   configuration mostly loosens it. The Substack framing "a live gun with the safety off" inverts this.
2. **Never "for everyone."** Pro, Max and Team only. Enterprise, API, Bedrock, Vertex and Foundry stay opt-in,
   so most regulated shops are untouched on the 14th.

## Angles this opens

- **31 Jul, sign / camera / governor** — the cleanest callback available all week. The prompt was the sign. The
  classifier is the camera. `permissions.deny` in managed settings is the governor. And the 7 Aug trailing-slash
  bug is the reminder that even the governor needs someone checking it.
- **The Fri 14 Aug national-scale half** (`research_eo14409recheck_20260809.md`) — one rule was written in a room
  and shown to nobody; the other was published in full and will be read by almost no one. Two ways for a rule to
  go unread.
- **[[Anthropic inference hooks - a deny switch you hold]]** — same vendor, same question: which control do *you*
  hold, and have you written it down.
