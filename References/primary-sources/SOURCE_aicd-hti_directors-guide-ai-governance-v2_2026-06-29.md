---
type: primary-source-capture
captured: 2026-08-30
document: AICD & Human Technology Institute (UTS), "A Director's Guide to AI Governance", Version 2
published: 29 June 2026 (per the AICD landing page)
landing: https://www.aicd.com.au/news-media/research-and-reports/a-directors-guide-to-ai-governance.html
pdf_v2: https://www.aicd.com.au/content/dam/aicd/pdf/news-media/research/2026/director-guide-to-ai-governance.pdf
also: SME/NFP checklist -- .../a-directors-guide-to-ai-governance-check-list-26.pdf
  · snapshot -- .../a-directors-guide-to-ai-governance-snapshot-26.pdf
---

# ⚠️ READ THIS FIRST -- THERE ARE TWO EDITIONS AND THE PUBLIC ONE IS THE WRONG ONE

The PDF that surfaces first on a search, at
`content/dam/aicd/pdf/tools-resources/director-resources/a-directors-guide-to-ai-governance-web.pdf`,
is the **2024 FIRST EDITION** (© AICD and HTI 2024, ref CCT1403_24). It is NOT the v2 the corpus
cites. Anyone re-checking these quotes against that file will find some of them and conclude the
others were invented.

**v2 is at the `news-media/research/2026/` path above.** Its landing page is member-gated
("You have reached your limit for guest contents... exclusive for AICD members"), **but the PDF on
the content CDN is not** -- it fetches directly. Note that a plain command-line fetch from a browser-less
client gets a 403 from the CDN; it has to come through a real browser or a fetcher that presents like
one. Same shape as the CISA 403 problem: browser, not proxy.

# VERIFICATION RESULT -- all three corpus quotes CONFIRMED, one of them is longer than we had it

| Corpus claim | Status | Exact text and location |
|---|---|---|
| Boards ultimately accountable | ✅ VERBATIM | "Boards are ultimately accountable for the adoption, implementation and outcomes of AI technologies in their organisations." (**Ministerial Foreword**) |
| Directors need not be experts | ✅ VERBATIM, **and we had it truncated** | "Directors do not need to be AI experts. But they do need a minimum viable understanding of AI to ask the right questions, **make informed strategic decisions, and ensure appropriate governance structures and processes are in place.**" (The role of the board, Part 1) |
| Vendors / accountability | ✅ VERBATIM | "While these risks may originate with vendors, accountability remains with the organisation." (AI governance practices, Part 2) |

⚠️ **The accountability sentence is in the MINISTERIAL FOREWORD, not the body.** That matters for how
it is attributed. It is the strongest sentence in the document and it is the one written by a
politician rather than by the AICD or HTI. Cite it as the guide's foreword, not as "the AICD's
position" or "HTI research."

# ★ THE ASIC ITEM -- CORRECTED, AND THE CORPUS HAD THIS SLIGHTLY WRONG

`research_story-candidates_2026-08-16.md` §1.4 says: *"The guide characterises ASIC's position as
extending director duties to AI adoption. That is AICD reporting ASIC -- not verified against an ASIC
primary."*

**The guide does not characterise. It quotes.** Verbatim, in The role of the board, Part 1:

> "Company directors and officers must discharge their duties with a reasonable degree of care and
> diligence. These duties extend to the adoption, deployment and use of AI. Directors and officers
> should be aware of the use of AI within their companies, the extent to which they rely on
> AI-generated information to discharge their duties and the reasonably foreseeable associated risks."

**The distinction is real and it changes the safe sentence.** It is not "the AICD reads ASIC as
saying X." It is "the guide reproduces what it presents as ASIC's own words." That is one hop closer
to the primary.

⚠️ **BUT THE STANDING RULE IS UNCHANGED AND STILL BINDS.** A targeted search on 30 Aug for this
wording returned **only law-firm commentary** (Hall & Wilcox, Holding Redlich, Norton Rose Fulbright,
Bedell Cristin) and **no ASIC primary**. So:
> **SAFE:** "ASIC's position, as quoted in the AICD and HTI guide, is that..." with the guide named.
> **DO NOT PRINT:** the passage sourced directly to ASIC · any Corporations Act section number on
> this authority (the guide still cites none) · "ASIC has ruled/found/determined."
> **STILL OPEN:** find the ASIC primary. It is the single highest-value unfooted claim on the
> management beat, and it would upgrade a hedge into a regulator quote.

# Structure (for anyone mining it later)

Ministerial Foreword · Executive summary with eight governance elements · Part 1: AI and the
governance imperative (contains "the role of the board" and the ASIC passage) · Part 2: practical
steps for directors (contains the vendor/accountability sentence) · four case studies · appendix.

⚠️ The 2024 first edition's case studies were Telstra, KPMG Australia, UTS and Microsoft. Do not
assume v2 carries the same four without checking.
