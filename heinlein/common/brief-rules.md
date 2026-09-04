# Shared rules for the three morning briefs

Every brief skill reads this first. It holds what is common so the three skills only carry what
differs: their lanes, their sections, their stance.

## Who this is for

Lars Klander. CTO of Player Elite (club and casino gaming tech, US and Australia). Writes a
Substack on AI and cybersecurity for CISOs and decision-makers, and content for Australian
registered clubs. Protecting customer PII is a top priority for his business, so data sovereignty,
local and on-premise models, GDPR and Australian Privacy Act compliance, and AI privacy risk are
always material. His audience skews to regulated industries (financial services, government,
health) and Australian, UK and EU markets.

## Item shape (the parser depends on this)

Each item is one paragraph block, separated from the next by a blank line:

```
**Title of the item**
Source: Publication name | [Link](https://...)
One or two sentences on what happened. Facts, numbers, who said it.
💡 Strategic take: Two or three sentences in Lars's voice.
```

- Title in bold on its own line. Nothing else bold in the block.
- Source line exactly as shown when the source is a publication. Community items may put the
  source on the title line instead: `**r/netsec** - "Thread title" (score) · URL`.
- The take line starts with 💡 followed by "Strategic take:" (cyber, AI) or "Constructive read:"
  (work). Social items may use `*Why it matters: ...*` instead.
- One URL per item, the primary or original source. No trackers, no search-result URLs.
- Sections are `## ` headings. Do not add `###` subsections except the AIDB episode block.
- Use a hyphen or a colon, never an em-dash or en-dash, anywhere in the file.

## Accuracy rules (from CLAUDE.md, and they bite)

1. A regulatory claim needs a primary source: the regulator's own text, standard or guidance.
   A vendor blog or consultancy explainer is not a source for "regulation X requires Y". If only
   secondary sources exist, say so in the sentence.
2. Name the commercial interest. If the only sources for a claim are companies selling the fix,
   that is the story.
3. Numbers get a source and a date. "48% of layoffs attributed to AI" without both is a fresh
   error waiting to be caught later.
4. Do not launder confidence. "Reportedly", "appears to", "one outlet reports" stay in.
5. Before writing, read `References/derived_killed-claims_2026-08-25.json` if it exists and the
   most recent `References/research_*.md` from the last 14 days. A claim that has been killed does
   not come back as a finding. If a story touches a killed claim, say "previously killed on
   <date>: <reason>" instead of restating it.
6. Read the last three days of the same brief before writing. Do not re-run a story that was
   covered unless it moved, and if it moved say what changed.

## Voice for the take lines

Thought leader, strategic, big picture, business and policy implications. Concrete before
abstract. Reach for the analogy, then the claim. Pair capability with its economics when you can.
Do not start with "This article", "This is important because", or "In today's fast-paced world".
Do not use the same closing device twice in one brief.

## Lane failure vs nothing found

"Nothing material in the last 24h" means you looked and found nothing. A tool failure (Chrome down,
Gmail unavailable, Firecrawl error) is not that. Mark it with ⚠️ in the section, name the tool and
the time, and report it in the summary. Never let a skipped lane pass silently.

## Outstanding drafts section

Scan `Substack Drafts/` for .md files modified in the last 7 days containing "Status: Draft".
Table: filename, title (first H1), age in days. Omit the section entirely if none. This section is
excluded from the Slack post by the parser; it is for the file.

## When done

Run the Slack post procedure in `heinlein/common/post-brief-to-slack.md`, then give Lars a
four-line summary: items per lane, today's theme in one sentence, any lane that failed, and the
Slack thread link. Concise. He prefers brief updates.
