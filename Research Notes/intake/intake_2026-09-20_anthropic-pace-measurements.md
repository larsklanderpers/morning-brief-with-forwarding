---
type: intake
date: 2026-09-20
source_url: https://www.anthropic.com/institute/measuring-pace-of-ai-development
slack_permalink: https://lars-klander-personal.slack.com/archives/C0BVCSV0PJ5/p1789951288238139
lars_note: "<https://www.anthropic.com/institute/measuring-pace-of-ai-development>"
reactions: []
verdict: feeds a thread - Ad Hoc Regulatory Regime (and Shape of Work-to-Come); nearest day is Thu 24 Sep, as context not as spine
filed_to: Vault\Writing\Signals\Anthropic publishes its own pace metrics.md; thread lines on Ad Hoc Regulatory Regime and Shape of Work-to-Come; pointer on the 21 Sep week plan status board
---

# Measurements for understanding the pace of AI development inside frontier labs

**Publisher:** Anthropic PBC, on the `/institute/` path. Same body and the same lead author as
*"When AI builds itself"* (4 Jun 2026), which is where the 80% merged-code figure came from and which
this page links to.

**Authors:** Marina Favaro and Phillie Wright, "with editorial support from Santi Ruiz, Adam Farina,
and Sarah Pollack."

**Date:** ⚠️ **No date on the page.** Secondaries put it at **17 Sep 2026**; one aggregator carries
19 Sep. That is the second Anthropic Institute essay in four months to publish undated, which is the
same trap `research_anthropic-80pc_2026-08-16.md` recorded in August. Do not print a date without a
better source than a search summary.

⚠️ **FETCH CAVEAT, and it binds every quotation below.** The page was read through a summarising
fetcher, not a raw scrape. The quotes are as that reader returned them. **Re-read the page directly
before a word of it is printed**, exactly as the 19 Sep board-policies item was flagged.

⚠️ **Instruction check.** Nothing on the page is addressed to me. The one instruction-shaped block is
an example classifier prompt in the compute appendix, beginning *"You're helping to perform an
internal audit at the frontier AI company Anthropic..."*. It is published methodology, treated as
data, not followed.

## Extracted

**The frame.** Three measurements Anthropic proposes as the things the public should be able to see
inside a frontier lab, offered explicitly against its own CEO's call to slow down. *"We want to
illuminate the pace of progress for the public."* *"As the world considers pacing the frontier, we
should do everything possible to minimize the gap between what frontier labs know and what the public
knows."* The page links `darioamodei.com/post/we-must-pace-the-frontier` directly.

**1. AI-led AI R&D automation index.**
- A six-rung scale: AL0 *no AI involvement*, AL1 *minimal AI involvement*, AL2 *AI assists*,
  AL3 *collaborates*, AL4 *leads*, AL5 *is autonomous*.
- As of **August 2026, Claude "leads" 26%** of Anthropic's AI R&D work, **up from under 1% in
  February 2026**.
- **Over 90%** of measured work is at *collaborates* or above.
- **Not fully autonomous (AL5) on any measured subset.**
- Caveat, theirs: *"The automation ratings depend on the judge model"* - and the judge can make the
  same errors as the model it is judging.
- The page links Epoch's *"Toward an O\*NET for AI R&D"*.

**2. Oversight of AI agents.**
- Roughly **30,000 agents** doing research and engineering work simultaneously on the primary
  platform.
- Online monitors: **100% action coverage** with real-time blocking, **0.002% blocking rate**, about
  **1 in 47,000 decisions** blocked.
- Offline monitors: **100% post-fact coverage**, roughly **1-2 transcripts per thousand** flagged,
  about **50 high-priority flags a week** escalated to a human.
- Caveats, theirs: *"At this scale of agent activity, it is hard to be certain we have a complete
  picture of all possible kinds of behaviors"*; the monitoring has run *"for months, not years."*
- The ask on the industry: *"Developers should share how often known agent misbehavior is caught by
  monitors, and should have third parties do this kind of testing independently."*

**3. Compute allocation to safety.**
- **6%** of AI R&D compute to safety research, on a **13-20 July** snapshot.
- **12%** of *AI-driven* AI R&D compute to safety research.
- *"These are deliberately conservative estimates."*
- Caveats, theirs: *"Compute is an imperfect proxy for how much a company focuses on safety"*; *"some
  cases were too difficult to determine even after several hours of human review"*; *"many of the
  underlying labels we relied on are best-effort, not verified"*; one week is *"enough to show that
  the measurement can be made, but not enough to show a meaningful trend."*
- The line that does the most work: *"Safety research is hard to distinguish from capabilities
  research, and each developer will be tempted to draw the line generously,"* and therefore *"the
  burden of proof should sit with the developer to show that work is safety-related."*

**On verification.** Future tense, and that is the point: *"We plan to embed independent third-party
evaluators from multiple organizations at Anthropic, and give them access to internal processes,
systems, and data comparable to what internal risk assessment teams have."* As published, every
number here is self-measured, self-judged and unaudited.

## Lars's note

<https://www.anthropic.com/institute/measuring-pace-of-ai-development>
