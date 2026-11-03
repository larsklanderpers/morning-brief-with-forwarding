---
name: substack-review-workflow
description: How Lars flags drafts for review, how editing fits in, how to merge his edits when they collide with yours, and how to report back without misattributing the piece
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 85cb2e63-b9a6-479f-a63a-d5c356a270db
sources: [cowork-import]
imported_at: 2026-09-15T13:26:17Z
---

**Rule:** When Lars asks to review a Substack piece, read the file directly from the Substack Drafts folder — no copy-paste needed. His edits to the file are always the source of truth; never compare to a prior draft version or try to restore anything.

**How Lars flags a piece:** By name or description in chat ("look at the prompt injection draft", "review my latest"). Read the current file state from disk.

**Two review modes — always clarify which if not stated:**
- **Draft-pass** — mid-edit, Lars wants eyes before continuing. Flag issues without rewriting sections unless asked.
- **Final-pass** — pre-publish proofread. Catching what slipped through; lighter touch, faster turnaround.

**When Lars has made substantial changes** (rewrote the lede, added a section, changed the angle): he'll flag it briefly. Use those changes to update voice calibration — his rewrites are the training data, not corrections to log and move past.

**Why:** Lars edits/adds to every piece. Treating his edits as expected (not as divergence from a "correct" draft) keeps the workflow smooth and accelerates voice alignment over time.

**How to apply:** Read → assess scope → flag issues with brief inline notes or a clean revised version depending on what's asked. Always confirm draft-pass vs. final-pass if unclear. Reference [[lars-writing-voice]] and [[substack-drafting-process]].

**Third mode — structural revision pass (confirmed Jul 4 2026, "Nobody Gave You a Week" v2):** When Lars asks to "challenge the form and structure" and lengthen a piece, he wants a full rewrite saved as a new `_v2` file alongside the untouched original, plus a critique in chat of what changed and why. Techniques that landed: bookend the opening analogy at the close; enforce section symmetry with a repeated refrain beat; add the week's missing thread/story rather than padding existing ones; mine the daily briefs for material additions; plant forward references to scheduled pieces. Flag any stat that can't be verified against the briefs.

**MERGE, DON'T ADOPT — his higher rvN can be based on an OLDER state than yours (2026-07-25, "Who Controls the Model").** In a fast back-and-forth he edits a copy he took at some earlier point in the exchange, then saves it as the next rv number. His rv10 arrived *after* my rv9 but was cut from a pre-second-turn copy: adopting it wholesale would have silently dropped a whole section he had just asked for, plus the header. **A higher rv number does not mean a later base.**

How to apply, every time a new rvN from him appears:
1. Diff his file against your latest, both directions — look for what his version is *missing*, not just what it adds.
2. Merge his additions into your complete version; never replace yours with his.
3. Say plainly in chat that you merged rather than adopted, and why — he cannot see which base he cut from.

His content edits still win on every line where both versions have text. This rule is only about not losing work that isn't in his copy at all.

**★★ HOW TO REPORT BACK — his text carrying the piece is the PREMISE, not a finding (his correction, 10 Sep 2026).** His words: *"my stuff should always carry the piece. that's why we still have me."* A wrap-up that credits his edit pass with "doing the real work", or singles out his contribution as the thing that lifted a score, quietly inverts the arrangement — it treats the drafted version as the default and his voice as an improvement on it. It is the wrong way round and he will say so.

**How to apply:**
- Report **what the machinery caught** — errors, collisions, unfooted claims, window bleed, what needs his ruling. That is what the pipeline is for and that is the useful half of any summary.
- Do **not** narrate who contributed what, do not score his authorship, and do not frame his edits as the rescue of a draft.
- Where his text has to be named — a merge note, a status header, a board row — name it factually and for provenance (*"his close, his triple, his [YOUR TAKE]"*), so a later session knows what is protected. That is record-keeping, not praise.
- Praise an outcome if it is genuinely earned and say it once, plainly (*"good piece, the seatbelt is the line people will quote"*). Then stop.
- Corollary for the panel: seat scores measure the piece, never the split of labor. A section improving because he wrote it is the system working as designed, not a result.

**Also 10 Sep: a delivery-copy handed to him becomes a live fork.** Once he has a reading copy (Word or otherwise), any later rewrite of the same passage creates two live versions and his pass will be built on the older one. Either re-issue the copy after the rewrite or expect to splice paragraph by paragraph. Splice, never stack — and say which you did.

Related: [[length-aside-two-beat]] (a single observed edit is not a preference — ask before writing housekeeping into the canon as a rule), [[lars-writing-voice]].

**24 Sep 2026 (Fri 25 "Adoption Speed, Control Speed" session) -- three lessons:**
- **[stated] Panel reports lost him:** "I am struggling to really understand their objections." Every panel report to him now carries a plain-English "why the scores are where they are" (5 bullets max), each item labelled PRAISE or CRITICISM, quoting the line in question. He also asked "was that approval or criticism" about a line the panel praised. When relaying a report, never pass through charter jargon ("competing landings", "register seam") without translating it.
- **"All suggestions acceptable" does NOT cover a fill-or-cut choice on HIS slot.** The drafter cut his Gemini [YOUR TAKE] under a blanket accept; he immediately said "then i will write the gimini paragraph." When an option is "you fill it, or cut it", default to keeping his slot open.
- **Pasted AI-search summaries are leads, not sources.** His pasted overview claimed Sottiaux says "reset your agents.md"; the cited LinkedIn post reads as Tibo's habit of resetting Codex usage limits, and the LinearB page supports only "harness as temporary infrastructure" / "some adaptation always necessary". Verify each attribution at the page before printing it, and say plainly which parts held up.
- **Before correcting his number, check the lab's own claim.** The drafter told him "Opus 5.5 is 20% cheaper, not 40%"; Anthropic's own page says 40% less to run "on typical workloads" (list price is 20%, cache reads 60%). He was right; the caveat was the useful addition.

**30 Sep 2026 (Thu 1 "The Model Moves Onto the Desk") -- panel pedantry calibration:**
- [stated] He took all seven panel rulings but called them "a bit pedantic", and specifically: "four days against five years ... feels like a false one to me." Rounded figures in his own conversational text (ages, durations, "more than five years") are not Skeptic findings unless the rounding changes the argument. Raise a precision fix only when a reader could fairly call the claim wrong, not when it is a few days off a round number.
- [stated] He wants fewer, heavier rulings when he is tired; batch the trivial ones as silent mechanics or drop them.
- [stated] **"You skipped the note suggestions again."** Every time a piece moves to Scheduled, run the `substack-notes` skill in the same turn and give him the three candidates without being asked. Neither day-start's `schedule it` step nor the panel triggers it, so it keeps getting dropped. Also: log the posted note when he names it. The Tue 29 (A) and Wed 30 (C) chats produced notes but never wrote them to `notes_log.md`, so their text is not on disk.