---
name: affiliation-at-primary
description: Never take a person's job title or employer — or a standard's, classification's or agency's NAME — from secondary coverage or from an older note of our own. Fetch the primary. A stale label is a fabricated attribution.
type: feedback
sources: [cowork-import]
imported_at: 2026-09-15T13:26:00Z
---

**Rule: a named person's employer, title and current status get footed at a primary — their own profile, their own post, the company's own page — before they go in a draft. Secondary coverage is not a source for affiliation, no matter how many outlets agree.**

**Why:** On 9 Sep 2026 the Fri 11 Astra draft built a whole section around *"Joshua Achiam, who works there"* — a current OpenAI voice supplying the strongest counter-argument. He had left OpenAI in July 2026. His own X bio says so in three words: *"Prev: @openai."* The error came from three independent secondary sources that all said the same wrong thing: LessWrong/Zvi tagged the quote "(OpenAI)", the Daily AI Digest wrote "OpenAI's Joshua Achiam", and the aggregator framing carried it too. Consensus among secondaries is not corroboration when they are all copying the same stale label. The catch came from project memory ([[story-candidates-2026-09-09]]), not from the research pass — **the research pass had quoted him twice and never checked who he was.**

Two further errors were hiding behind the first and only surfaced because the affiliation check forced a look at the primary:
- **The post was dated 2 Sep, the day BEFORE the model shipped.** The draft framed it as a response to the system card. It was a response to The Information's reporting.
- **The quote was truncated.** The full post carried a genuine concession and a second paragraph criticizing press disclosure of frontier methods — context that changes how the speaker reads, and which a reply under the post called out as a retroactive defense of his former employer.

## ★★ EXTENSION, 12 Sep 2026: institutions and standards go stale the same way, and OUR OWN NOTES are a secondary

**The Mon 14 research pass caught "no ANZSCO code" heading for print. ANZSCO does not exist any more.** The Australian Bureau of Statistics replaced it with **OSCA (Occupation Standard Classification for Australia) on 6 December 2024** — the first full rebuild in about twenty years. The stale name was sitting in **two of our own artifacts**: the `research_story-candidates_2026-09-09.md` §12 kill, and the Mon 14 block of the week plan written off it. Nobody introduced it from the outside. **We propagated it ourselves, from note to plan to the edge of a draft.**

**The engine is identical to Achiam.** A real thing, correctly described, under a name that expired. Same failure, non-human subject.

**Same pass, same shape, a second catch:** the plan's implied mechanism was that the orchestrator role has no US occupational code *because 739 postings is too small*. The SOC Policy Committee says in writing it **"does not use a specific employment size cut-off."** An assumption about how an institution works, never checked at the institution's own published rules.

**How to apply:**
- Any sentence of the form "X, who works at Y" needs the bio fetched. `firecrawl_scrape` on the profile URL returns it in one call — see [[x-com-via-firecrawl]].
- **Check every named voice in a piece, not just the suspicious one.** The same sweep confirmed Marcus Williams ("Monitoring at OpenAI") and Micah Carroll ("RSI Preparedness lead @openai") as current, and produced better primary quotes for both than the secondary fragments in the research note.
- ★ **Treat the NAME of any standard, classification, framework, register or agency as an affiliation claim and foot it the same way.** ANZSCO, SOC, O*NET, ESCO, NIST frameworks, ISO numbers, CVSS versions, statutory instruments — all of these get renamed, superseded and reissued, and secondary coverage keeps using the old name for years.
- ★★ **Our own research notes and week plans are SECONDARY SOURCES about the outside world.** A label that entered a note weeks ago and has been copied forward since has had zero verification events, not several. **Age in our corpus is not corroboration; it is decay.**
- ★ **Do not infer an institution's decision rule. Read its published rules.** "It is too small to qualify" / "they would never approve that" / "there is no process for this" are all checkable at a primary, and were all wrong or unprovable here.
- **A departure changes the argument, not just the label.** A current employee criticizing their employer's product and a former employee defending it are different exhibits. Fix the framing, not only the noun. **Same for institutions: a rebuilt classification with a live public consultation is a completely different exhibit from a dormant one.** The OSCA catch did not just fix a word — it produced the piece's action move and its entire second half.
- **When the mislabeling is itself widespread, it may be a beat rather than an embarrassment.** In the Astra piece the fix was printed: the universal miscrediting of Achiam became an exhibit for the piece's own thesis about accepting documents at face value. **The Mon 14 draft does the same with ANZSCO, in his own voice: *"If you work in this area and you have been saying ANZSCO recently, and I have, the label has been superseded for the better part of two years."***
- Read project memory's blockers for the day BEFORE drafting. This one was sitting in the MEMORY.md index line the whole time.

Related: [[brief-claim-provenance]] (this is a distinct engine — a REAL person or REAL institution with a STALE predicate, sibling to the real-proper-noun-manufactured-predicate engine), [[absence-verification]], [[x-com-via-firecrawl]].
