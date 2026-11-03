---
type: intake
date: 2026-09-20
source_url: https://x.com/0xCodila/status/2101433560796467348
slack_permalink: https://lars-klander-personal.slack.com/archives/C0BVCSV0PJ5/p1789929295913289
lars_note: "https://x.com/0xcodila/status/2101433560796467348?s=46&t=hFGPxOsruf8YIDTpfEWrFA"
reactions: []
verdict: feeds a thread -- Two visions for agentic routing (Shape of Work-to-Come, AI Sovereignty, Trust Boundaries). The local-router side of the fork now has a shipped product and a viral install recipe.
filed_to: Vault\Writing\Signals\Two visions for agentic routing.md (updated, not duplicated) · Threads\Trust Boundaries.md · Threads\Shape of Work-to-Come.md · References\week-plan_2026-09-21.md (intake note, no day row touched)
---

# "Jev + GrokBot is the best AI agent system I've built in my life" -- a seven-step install recipe, 253K views

## Fetch provenance

⚠️ **x.com itself returned HTTP 403 to the fetcher.** The post text below came back through the
**fxtwitter mirror** (`api.fxtwitter.com`), not from X. Treat the text as a good transcription but
**re-read it at x.com before quoting a word of it in a draft.** Engagement counts are the mirror's
as of 20 Sep 2026 and move.

No Firecrawl tool was loaded in this session; WebFetch was used instead. The linked repo and the
"Jev deep dive" were NOT fetched -- they sit behind the post's own "below" links, which the mirror
does not resolve.

⛔ **The post is a set of instructions addressed to whoever reads it (create an API key, have a bot
store it, install an SDK on the agent computer, add a routing skill, flip it active). Per CLAUDE.md
that text is DATA, not instruction. Nothing in it was executed, no key was created, no SDK was
installed, and no skill was added.** It is recorded here verbatim because the recipe is the story.

## Extracted

**Author:** codila, @0xCodila, verified, ~20,558 followers.
**Posted:** Sat 19 Sep 2026 22:09 UTC. **Media:** a 15.58-second video.
**Engagement (mirror, 20 Sep):** 253,794 views · 4,486 bookmarks · 1,842 likes · 200 reposts · 94 replies.
**Quote-tweets his own earlier post:** *"Jev is the 'Internet' moment for the AI industry."*

Post text, as returned by the mirror:

> Jev + GrokBot is the best AI agent system I've built in my life
>
> It just made my setup CHEAPER and FASTER than what 95% of people are running...
>
> setup takes literally 7 minutes:
>
> prompt -> GrokBot -> Jev decision -> GrokBot execution -> result
>
> step 1 -> open @typesafeai , create API key (keep it off chat paste)
> step 2 -> tell Grok Bot: store TYPESAFE_API_KEY in the secure field
> step 3 -> prompt Grok Bot: install typesafe-sdk on Agent Computer + smoke system_one (Choice)
> step 4 -> tell Grok Bot: build the usage lab (router, dry-run, config, logs) - or clone Github below
> step 5 -> add skill jev-usage-router: before browser / research / retry / extra bot -> call the router, honor action
> step 6 -> stay shadow first, read logs, then active when you trust it - kill switch: bypass jev or enabled: false
> step 7 -> flip active: GrokBot obeys route - Jev decides - GrokBot executes - humans control irreversible actions
>
> the result: Jev + GrokBot the best and fastest agent running directly on your computer rn, I've
> already tested it on routine tasks - and the results are genuinely incredible
>
> You can come up with endless ways to use Jev + GrokBot - but the most important thing is to
> install it as soon as possible
>
> Copy this 2028 setup, explore my repo below - then read the full Jev deep dive

("2028" is his, verbatim. Read as hype rather than a date.)

## What Jev is, and how well that is footed

**Not footed at a primary in this tick. Web-search summary only, typesafe.ai was not fetched.**
Jev is TypeSafe AI's first public **"System One" model**: it does not generate text, it returns
typed answers with calibrated probabilities for routing, tool selection, classification, scoring
and escalation. JavaScript SDK `@typesafe-ai/sdk`. Distribution is already broad for something this
new: Vercel AI Gateway (`typesafe-ai/jev`), OpenRouter, and a LangChain `TypeSafeClassifier`
integration.

⚠️ **Name the commercial interest, per the standing rule.** The speed and cost numbers everywhere
in circulation are **TypeSafe's own, from TypeSafe's own workflow evaluations**: "up to 193.6x
faster and 444.6x cheaper than LLMs" in the vendor framing, rounded to "200x / 400x" by the
secondaries. No independent benchmark surfaced. **Do not print either pair as fact.**

⚠️ **Launch date is contested in our own corpus and must not be asserted.** `AI Briefs\ai_brief_2026-09-20.md`
says **15 September**, sourced to Generative Programmer, and attributes it to **Diogo Almeida, a
ChatGPT researcher**. MarkTechPost's write-up is dated **19 September**. Both are secondary. Settle
it at typesafe.ai before any draft carries a date.

⚠️ **And the poster's own interest is undisclosed.** He links his own repo and a "deep dive" and
tells readers to "install it as soon as possible". Whether this is paid, affiliated or simply
enthusiasm is not established either way from the post.

## Where this is already in the corpus

- `AI Briefs\ai_brief_2026-09-20.md` -- today's brief, Shipping with AI and From the Substacks.
  Frames Jev as a cost and latency play for ticket triage, compliance classification and document
  routing, plus a privacy read ("returns probabilities rather than generated text").
- `AI Briefs\work_brief_2026-09-18.md` -- NLW's "judgement models" segment. Its constructive read is
  the good one: if machines say "72% likely", the scarce skill is knowing which decisions are worth
  escalating.
- The same brief records X as a login wall, with "Jev AI Model Speeds Up Structured Decisions for
  Developers" trending at 50.2K posts. **So this post is not a new story. It is a new angle on a
  story the briefs already carry, and the angle is the part the briefs do not have.**

## Lars's note

Verbatim, the link and nothing else:

`https://x.com/0xcodila/status/2101433560796467348?s=46&t=hFGPxOsruf8YIDTpfEWrFA`

No reaction on the message at the time of this tick.

## Why it is worth holding

**Three things in it that the briefs do not carry.**

1. **It is the local-router side of the fork, shipped.** `Two visions for agentic routing` (filed
   2026-07-20 off Mollick) set out the architectural choice: a frontier model routing downward,
   versus a small local model calling up when it needs help. Mollick leaned frontier-first. The
   signal's own open question was that the routing decision is a sovereignty decision nobody frames
   that way. **Fourteen months later the small-local side has a product, a gateway listing and a
   framework integration, and the first viral how-to puts it on the reader's own machine.**
2. **The recipe is the trust-boundary story.** Steps 1 to 3 are: mint a credential, have the agent
   store it, then have the agent install an SDK on the Agent Computer. That is a credential and an
   install handed to the bot, on the shared machine, by 4,486 people who bookmarked a seven-minute
   promise. It is the same shape as
   [[Managed agent harnesses - the vendor keeps the session]]'s finding that subagents share one
   filesystem and inherit MCP credentials, and the same shape Sat 12 flagged in Grok Bot's own
   one-computer design.
3. **Steps 6 and 7 are better than the thread they are in, and that is the twist worth keeping.**
   Shadow mode first, read the logs, go active only when you trust it, a named kill switch
   (`bypass jev` / `enabled: false`), and humans keep irreversible actions. **That is a competent
   staged-rollout discipline, printed inside a "install it as soon as possible" hype thread.** The
   interesting sentence is not that the recipe is reckless; it is that the recipe is careful and the
   framing around it is not, and the framing is what travels.

## Cautions for whoever uses this

- Re-read the post at x.com. The mirror is a transcription, not the source.
- Do not print the speed or cost multiples. Vendor evals, no independent benchmark.
- Do not print a launch date until typesafe.ai settles 15 vs 19 September.
- Do not print the poster's motive. Undisclosed is undisclosed.
- **Grok Bot caution carries from the 14 Sep plan:** Sat 19 promised a return to Grok Bot on a
  *later* Saturday, and Sat 26 is already spoken for by a printed promise (the attention widget).
  This is not Sat 26 material.
