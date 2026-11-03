# Research Note -- Sun 4 Oct capstone: the recall math, craft upstream vs attention downstream
For: Sun 4 capstone (untitled) · Depth: deep (local-first + 4 web primaries) · Date: 2026-10-03

## Bottom line
Every leg of his spine is footed, mostly from the week's own notes, so the capstone can call back rather than re-report. The one new primary worth adding is **Knight Capital, 1 Aug 2012 (SEC order 34-70694)**: one deployment step skipped on one of eight servers, 45 minutes, over 4 million executions, $460M lost, 97 warning emails "not acted upon", and no written deployment procedure or second-person review. It is the recall math and the craft-vs-attention split in one documented case, and it is unspent in the corpus. Mollick's "The Dot and the Swarm" (1 Oct) is the strongest counter and says nothing about checking output. @_isomerism is now footed at source.

## What's solid
- **Knight Capital** -- SEC Admin. Proceeding 34-70694 (16 Oct 2013), primary: https://www.sec.gov/litigation/admin/2013/34-70694.pdf
  - para 1: "SMARS routed millions of orders into the market over a 45-minute period, and obtained over 4 million executions in 154 stocks for more than 397 million shares."
  - para 15: "one of Knight's technicians did not copy the new code to one of the eight SMARS computer servers."
  - para 16: orders with "the repurposed flag" sent to the eighth server "triggered the defective Power Peg code still present on that server."
  - para 17: ~$3.5B net long, ~$3.15B net short; "Ultimately, Knight realized a $460 million loss on these positions."
  - para 19: "Knight's system sent 97 of these e-mail messages ... before the 9:30 a.m. market open ... these notifications were not acted upon before the market opened."
  - para 26: "Knight did not have written code development and deployment procedures for SMARS ... Knight did not require a second technician to review code deployment in SMARS."
- **Warp cost per PR ~$80 -> ~$30**; "human interactions per PR", goal to drive it down -- research_mon28 note; ALREADY PRINTED Mon 28 (callback only).
- **Faros 2026**: incidents per PR +242.7%, time in review +441.5%, merged "without any review, human or agentic" +31.3% -- research_mon28; ALREADY PRINTED Mon 28 with caveats (vendor; correlational). Callback only, keep the caveat in a clause.
- **Brevo, 14 Sep 2026**: one long-lived Cloudflare key in source; forms script, chat widget, SDK loader served ClickFix on customer sites about four and a half hours -- research_wed30; PRINTED Wed 30. Callback only.
- **Isenberg, "$5T opportunity: AI Roll Ups", YouTube 28 Sep 2026 [04:52]**: "The people who used to do the work are becoming the people who check it." -- research_isenberg note, transcript in primary-sources. NOT yet printed (Fri 2 used his roll-up thesis, not this line).
- **Oliver Ye @_isomerism, X, 25 Sep 2026 02:18 UTC** (24 Sep US time): "the moat is literally just caring about your work and being proud of your output and holy shit it does not seem to apply to 99% of people" -- read at source via firecrawl 3 Oct. 7,519 likes. @poteto replied "true".
- **Mollick, "The Dot and the Swarm", One Useful Thing, 1 Oct 2026**: "The agents sent about 2.7 million messages, reaching their result after 88 hours." He concedes he assumed companies "would need to rebuild management for machines ... but much of management exists to solve problems agents don't have."
- **pcloadletter, "Software Craftsmanship Is Dead", 3 Jan 2026** (the piece Fri 2 cites without author): incentives reward shipping fast "without regard for the maintenance burden".

## What's contested / watch out
- **Mollick as counter:** his swarm worked with thin direction, which reads against "craft is scarce and must be led". But the piece "contains no explicit discussion of error-checking, failure rates, or output quality verification" (fetch summary; re-read before asserting the absence in print -- absence from a fetch is not evidence). Use him as the strongest opposing view, attributed, and answer it: a swarm that reaches a result in 88 hours is a run count, and the run count is what multiplies whatever is wrong in the setup.
- **Knight is a 2012 trading system, not AI.** That is the point (the arithmetic is not new), but say so, or the skeptic will. Do not call it "an AI failure".
- **Knight could be read as a HITL-wins story** (97 emails, someone should have looked). His spine reads it the other way: the emails were attention arriving after the defect was live; the missing written procedure and second reviewer were the craft. Both are in the SEC text; print both.

## Couldn't verify
- Nothing load-bearing. The 100,000 executions and "under $100 a unit" are HIS illustration and must be printed as his.

## The economics
- His recall math: defect cost = unit cost x run count, not a line item. Knight is the worked case: whatever each order was worth, 4 million executions in 45 minutes turned one skipped copy step into $460M.
- Warp's $80 -> $30 lowers the unit; Thu 1's on-device zero removes the meter on run count; together they push run count up, which is the multiplier on any defect (Faros incidents per PR is the direction of that, correlational).
- Who keeps margin (Base44 ~0% -> ~60% on its own model; Stripe top decile 61x median, median down 23%) is Fri 2's ground and is SPENT for Sunday; at most a one-clause callback.

## Corpus sweep (spent devices) -- Published + Scheduled
- "human in the loop" / "human-in-the-loop": 24 files across Jul to Sep. Use the phrase only as HIS term inside his distinction, once or twice, never as a header. HITL-as-theater ran (theater in 5 files incl. Tue 29); do not use "theater".
- "recall": only as a verb ("recall yesterday") and the Aug 23 recall list; **product/vehicle recall as an image is UNSPENT.** Wed 30's Tylenol did not use the word "recall"; keep Tylenol, bottles and seals out.
- "craft/craftsmanship": printed only in Fri 2 ("Software Craftsmanship Is Dead", utilities vs full solutions). Sunday is the answer Fri 2 promised.
- "messy middle": NOT printed (HTML comment in Mon 28 only). Held line available.
- Knight Capital, Ariane, Therac, Takata, measure-twice, carpenter-as-image: 0 hits. CrowdStrike: 9 files (spent). Toyota/andon/jidoka: 5 files (spent). Deming: 3 files (avoid).
- "blast radius" (12 files) and "multiply" forms (14): avoid as stock phrasing.
- Mon 28 sentence shape "the making got cheap, and something after the making did not": do not reprint.

## Drop-in facts
- On 1 August 2012, a technician at Knight Capital did not copy new code to one of eight servers; in 45 minutes the system obtained "over 4 million executions in 154 stocks for more than 397 million shares", and Knight lost $460 million. [SEC 34-70694, paras 1, 15, 17]
- Before the market opened, Knight's system sent 97 warning emails; "these notifications were not acted upon." [SEC, para 19]
- "Knight did not have written code development and deployment procedures for SMARS ... Knight did not require a second technician to review code deployment." [SEC, para 26]
- "The people who used to do the work are becoming the people who check it." -- Greg Isenberg, YouTube, 28 Sep 2026 [04:52]
- "the moat is literally just caring about your work and being proud of your output" -- Oliver Ye (@_isomerism), X, 24 Sep 2026
- "much of management exists to solve problems agents don't have." -- Ethan Mollick, One Useful Thing, 1 Oct 2026

## DO-NOT-PRINT
- Knight as an AI incident. Knight per-order values (not in the order). Any SEC fine figure unless re-read at primary.
- "Mollick says swarms never check their work" (absence from a fetch).
- Faros causation ("AI caused the incidents").
- All DO-NOT lists from the Mon 28, Wed 30, Thu 1, Fri 2 notes; "Warp ships 2,000 agent-written PRs".
- Isenberg "3x EBITDA"; the 7,000 returns at Larson Gross.
- Re-run: OpenAI DNS sandbox escape belongs to Wed 7 (next plan).

## Angles this opens
- Picks up Thu 1's promise: when the invoice stops being the signpost, run count is invisible, and run count is the multiplier.
- Picks up Fri 2's promise: utilities can live without craft because the platform replaces them; full solutions cannot, because they run 100,000 times inside someone's business.
