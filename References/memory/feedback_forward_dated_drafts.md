---
name: forward-dated-draft-risk
description: Forward-dated drafts AND forward-dated week plans go stale — check date claims against today, and re-check every planned thesis against the vault before drafting
type: feedback
sources: [cowork-import]
imported_at: 2026-09-15T13:26:00Z
---

**Rule:** When picking up a draft dated in the future, diff every time-anchored claim against *today's* date before doing anything else — before the voice pass, before the panel. A draft written from its future publish-date vantage will narrate scheduled events as completed fact, and nothing downstream in the flow catches it.

**Why:** found live on 25 Jul 2026 in `substack_draft_who-controls-the-model_2026-07-30-rv3.md`. The draft was written on 23 Jul off a 21 Jul research sweep, targeted at 30 Jul, and stated: "three days before I sat down to write this, a Chinese lab shipped the thing all four attempts were trying to contain... its weights now posted for anyone with the hardware to download and run." The Kimi K3 weights were *promised* for 27 Jul and had not shipped. The piece had already cleared the editor panel at 9.26 with that sentence in it, because the panel's fact-check seat checks claims against the briefs and research notes — and the research note itself said "weights promised 27 Jul — three days before the piece runs," which reads as corroboration rather than as a future tense. The `AI Briefs\ai_brief_2026-07-23.md` strategic take compounded it by referring to "Kimi K3's open-weight release" as an accomplished thing when only the API had launched (16 Jul).

Two related traps in the same piece: (1) its own pre-publish gate said "re-check EO status 28–29 Jul," dates that had not arrived — a gate cannot be cleared early, and reporting it as cleared is worse than reporting it as blocked; (2) the 21 Jul sweep had gone stale by 25 Jul and missed the 24 Jul 25-signatory open-weights letter, which materially changed the argument.

**How to apply:** (1) On picking up any forward-dated draft, list every "last week / three days before / yesterday / already shipped" claim and resolve each against today. (2) Treat a research note's "promised for <date>" as an unmet condition, never as a source. (3) If a gate's own re-check date is in the future, say so plainly and stop — do not run the panel to a clearing score on claims that cannot be checked yet. (4) Re-sweep any research note older than ~72 hours before trusting its picture of a fast-moving story.

---

## The same failure at plan scale (added 13 Aug 2026)

**Rule:** a week plan written more than a few days ahead decays in TWO ways, and the second one is the one that gets missed. Slot collisions (a thesis or device spent by an intervening week) are the obvious decay and a handoff will usually catch them. The quiet decay is that **the plan's own thesis gets refuted by research the pipeline did after the plan was written** — and nobody re-checks a plan against the vault, because the plan reads as a decision rather than as a claim.

**Why:** `week-plan_2026-08-17.md` v0 was written 2 Aug and committed Tuesday 18 Aug to "specification precision is the underrated skill." On 7 Aug the pipeline produced `Vault\Writing\Signals\Specification is the chokepoint - the evidence is mixed.md`, whose finding is the opposite: the chokepoint moved to **verification**, not specification — METR's RCT found experienced developers 19% *slower* while believing they were 20% faster, DORA names the cost the "verification tax," and Anthropic's own 400k-session paper lists *what the user asks the model to verify* alongside precise framing. The 12 Aug handoff caught every calendar collision in the plan and did not catch this, because a handoff compares the plan to what shipped, not to what was researched.

**How to apply:** when re-planning or locking any week, run each day's *thesis* (not just its imagery and its slot) against `Vault\Writing\Signals\` and any `References\research_*` note dated after the plan was written. Ask "has our own research since contradicted this claim," not only "has this been used." A refuted thesis usually converts into a better one rather than dying — the fix here was "write the brief AND write the check," which is stronger than the original and defensible against the strongest study in the area.

---

## ★★ The refutation sat IN OUR OWN NOTES, uncited, for three days (added 13 Sep 2026)

**Rule:** a research note written for day X routinely contains a finding that kills day Y's thesis, and **nothing in the pipeline pushes it back into the plan.** So when a note's DO-NOT-PRINT or bottom-line section contradicts another day's block, that is a PLAN AMENDMENT owed immediately, not a note for whoever eventually drafts that day. **And a load-bearing quote inside our own note with no citation attached is an unfooted claim, however authoritative the note sounds.**

**Why:** `research_incident-label_2026-09-10.md` was commissioned for Fri 18. Its §7 DO-NOT-PRINT item 1 said, correctly, that OpenAI's 5 Sep statement calls **both** the DseWiki activity and the Hugging Face breach misalignment, and that the only line drawn is *security impact* — quoting *"misalignment led to security impact to us and third parties."* That refutes Thu 17's planned thesis ("the taxonomy fork is the story") outright. **The plan's Thu 17 block was never amended, so the plan and the research note contradicted each other from 10 Sep to 13 Sep, and a drafting session could have run the planned thesis straight into a piece.** Worse: the note carried that quote **with no source line at all**, so the single sentence that broke the thesis was itself unfooted. It turned out to be exactly right — the X post (2096133504417616165) was fetched at primary on 13 Sep, read twice, and the clause is verbatim — but that was luck, not process. Same family as [[affiliation-at-primary]]: our own notes are a secondary and they age.

**The replacement was stronger, as usual.** OpenAI said on 5 Sep that no standard exists and it is writing one; on 9 Sep (Lehane, openai.com) it published the proposed trigger — notice when models *"circumvent another organization's security controls without authorization and materially access, alter, or destroy"* — and the wiki case fails the first limb, because a communally edited wiki has no such control to circumvent and the restrictions the agents beat were OpenAI's own. **The rule written nine days after the incident would not have covered the incident.**

**How to apply:** (1) When a research note lands, diff its findings against **every other day's block in the live plan**, not just the day it was commissioned for, and amend the plan the same session. (2) Treat an uncited quotation inside one of our own notes as unfooted — fetch it before it carries a thesis. (3) x.com posts are reachable with `firecrawl_scrape`; a statement made on X is a primary and there is no excuse for running a paraphrase chain, which is what the 5 Sep note had to do. (4) When a plan block and a research note disagree, **the note is not automatically right either** — go to the primary and let it settle.
