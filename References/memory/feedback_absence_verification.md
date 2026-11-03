---
name: absence-verification
description: A negative from a fetch of a long page is not evidence of absence — the 5 Sep 2026 near-miss where a truncated Hansard fetch nearly produced a "fabrication" verdict against a real ministerial quote, plus the 9 Sep variant where a 403/429/paywall was recorded as an unclosable gap
type: feedback
sources: [cowork-import]
imported_at: 2026-09-15T13:26:00Z
---

**5 Sep 2026. The verification layer produced a confident FALSE NEGATIVE and it was three sentences
from print.** This is the mirror of [[Killed-Claim FALSE POSITIVE]], one stage earlier — a kill that
would have been *born* wrong.

## What happened

A dig reported that the phrase **"proportionate containment powers"** appeared nowhere in the 1 Sep 2026
Lords Grand Committee Hansard on the Cyber Security and Resilience (Network and Information Systems)
Bill, that "containment" did not appear in that debate at all, and that the phrase existed in no UK
government document. It was written up as a **FABRICATION** — the strongest verdict available, an
accusation that a government had been quoted saying something it never said.

**It is a direct quote from the responding minister.** Baroness Lloyd of Effra (Lab), Grand Committee,
1 Sep 2026, replying to Amendment 84: *"This includes examining whether proportionate containment powers
could provide a more effective and targeted response, including powers to restrict access to specific AI
systems where necessary to prevent or mitigate serious harm."*

## How the false negative was manufactured — the mechanism is the lesson

Three negatives stacked, each reading as independent confirmation of the others:

1. A general web search for the quoted phrase returned only Cold War containment-doctrine noise.
2. The Lords Business page for 1 Sep did not show it.
3. ⚠️ **A direct fetch of the Hansard debate page returned "I found no instances of the words
   'containment,' 'contain,' 'contained'" — because the fetch had silently retrieved a truncated
   excerpt of a very long debate.**

Only the structured Hansard API surfaced the truth, on the first query.

## The rule

**A negative from a fetch of a long page is not evidence of absence.** Long Hansard, court, legislative
and regulatory documents are silently truncated in transit, and the truncation is invisible — the tool
reports a clean "not found," not "I only read the first part."

**How to apply.** Before any absence claim about a long document goes into a note, a kill, or a draft,
re-run it against a **structured API or a search index**, not a page fetch:
- Hansard: `hansard-api.parliament.uk/search/contributions/Spoken.json?queryParameters.searchTerm="..."`
- Prefer any site's own search endpoint or JSON API over fetching the rendering page.
- If no structured surface exists, the honest verdict is **UNREACHED**, never "does not exist."

**And never let three weak negatives stack into a strong one.** They were not independent — all three
were the same failure to see the whole document.

## ★★ THE 9 SEP VARIANT — A BLOCKED FETCH IS A TOOL LIMIT, NOT AN ABSENCE

**Same day, second demonstration, and this one cost a whole research pass.** The 9 Sep story-candidate
note closed with **twelve unclosed items**, three of which were recorded as genuine gaps and honestly
flagged as "could not verify." All three were **tool refusals, not absences**, and all three fell to
**Firecrawl** (`mcp__remote-devices__firecrawl__*`) on the first attempt:

| Recorded as unclosed | Actual cause | What it turned out to hold |
|---|---|---|
| BOD 26-04's text — *"every cisa.gov URL returned 403"* | fetcher blocked | **The directive drives its remediation clock off CISA's own Vulnrichment enrichment** — the finding that turned a bench item into a piece. Also: **BOD 22-01 is revoked** |
| The FT Preparedness piece — *"ft.com is blocked, an absence I could not close"* | paywall | **The FT printed OpenAI's denial in the original article**, Scandinaro **moved rather than left**, and **Wired broke the title change** — three corrections to a standing kill |
| The Gamers Nexus video — *"YouTube returned 429 on two attempts"* | rate limit | **The full auto-transcript**, which resolved the ambient-vs-wake-word crux the entire story turned on |

**The rule: 403, 429, `SITE_BLOCKED`, robots-disallowed and paywall are transport failures. They say
nothing whatever about the content.** Recording one as "an absence I could not close" is better than
recording it as proven silence — but it is still a stop one tool too early, and the honest label
misleads the next reader into thinking the ground was searched.

**How to apply — escalate before you record a gap:**
1. **Firecrawl** (`firecrawl_scrape`, `maxAge: 0`; add `proxy: "stealth"` for a paywall). It reached
   cisa.gov, ft.com and YouTube where WebFetch could not.
2. **A syndication or alternate URL.** The FT's own `?syn-...=1` link returns the full article body.
3. **The structured API**, per the Hansard rule above.
4. **Chrome**, per the house rule for robots-blocked pages.
5. **Only then** record it, and record it as **BLOCKED (tool)**, never as absence.
★ **Label the two states differently in the note.** "I searched and it is not there" and "I could not
open the page" must never share a bullet — the first is evidence and the second is a to-do.

⚠️ **Two things Firecrawl did not solve, so they are the real remaining shape:** a **member-gated**
article body (Tom's Hardware) still returns only the shell, and a document published **as an image**
(BOD 26-04's Table 1 is a PNG) is unreadable by any text fetch. **Those are genuine UNREACHED.**

⚠️ **And a new hazard the transcript introduced: YouTube auto-captions are ASR.** The retrieved
transcript rendered *Alphonso* as "Alfonso", *Wendell* as "Wendle", *MrBruh* as "Mr. Bra", *Wireshark*
as "wire sharkark", and a named SEC respondent as "Serge Mada". **ASR text is reliable for substance and
unusable for quotation.** Take the finding, note the chapter timestamp, and re-hear the line before it
goes inside quotation marks — and never take a proper noun or a spelling from it.

## Why it matters more than a false positive

**A false positive gets caught by a reader and costs a correction. A false negative gets caught by
nobody**, because the output is silence: the claim does not run, and no one writes in to say the thing
you did not print was true. Worse in this pipeline specifically — **a kill born wrong enters the
deny-list and every later run cites it as settled.**

Same morning as the Hansard case, the other direction: the deny-list's generic `five days` match string
fired on the vCenter item, where the five days is a genuine observed calendar interval (QUIRSO, 3 Aug vs
Broadcom's 29 Jul advisory) and not the previously-killed Mandiant average. **Two independent
demonstrations in one intake that the verification layer needs the same skepticism as the thing it
verifies — and the case for [[brief-radar]]'s annotate-never-suppress rule.**

## What actually caught it

An adversarial verification pass whose brief was **to refute, not to confirm**, run as a separate agent
on the note's three highest-stakes claims. It found the phrase on its first structured query. **Budget
that pass for any note carrying a REFUTED or FABRICATION verdict.** ★ **And 9 Sep adds the cheaper
companion: before a note ships, re-run every item on its own unclosed list through the escalation ladder
above. Three of twelve fell in one round.**
