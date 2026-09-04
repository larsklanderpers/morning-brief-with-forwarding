---
name: heinlein-brief-cyber
description: Daily 04:30 Cybersecurity Morning Brief with LinkedIn draft, posted to #heinlein-briefs
schedule: 30 4 * * *
replaces: Cowork task cyber-morning-brief (legacy/cowork-prompts_2026-07-20/cyber-morning-brief.md)
---

You are running the daily Cybersecurity Morning Brief for Lars Klander. Today's date is in your
context. Gather the top cybersecurity intelligence of the last 24 hours, write the brief, draft the
LinkedIn post, post the brief to Slack.

## STEP 0: READ THE SHARED RULES

Read `D:\vc-personal-projects\Morning Brief with Forwarding\heinlein\common\brief-rules.md` and
apply it. It carries the item shape, the accuracy rules, the killed-claims check and the voice.

Workspace root: `D:\vc-personal-projects\Morning Brief with Forwarding\`
- `Daily Briefs\` : the brief markdown
- `LinkedIn Posts\` : the LinkedIn draft
- `Substack Drafts\` : only written when Lars flags items

## STEP 1: GATHER INTELLIGENCE

Search for cybersecurity news published in the last 24 hours. Run ALL of these. To add a source,
add a line here.

1. WebSearch: "cybersecurity news today" (top 5 results)
2. WebSearch: "CISA advisory today" OR "CISA alert cybersecurity" (latest government advisories)
3. WebSearch: "Australian Cyber Security Centre advisory" site:cyber.gov.au (ACSC alerts)
4. WebSearch: "AI cybersecurity threat 2026" (the AI angle on security)
5. WebSearch: "data breach today" OR "ransomware attack today" (active incidents)
6. WebSearch: site:reddit.com/r/netsec OR site:reddit.com/r/cybersecurity (top community posts)
7. Fetch: https://www.reddit.com/r/netsec/hot.json?limit=8 (parse JSON for top posts)
8. Fetch: https://www.reddit.com/r/cybersecurity/hot.json?limit=8 (parse JSON for top posts)
9. WebSearch: "CVE critical vulnerability today" (top new CVEs)

If a Reddit JSON fetch is blocked, cover that signal via WebSearch and move on; do not try other
fetch methods. If a story needs the primary page and WebFetch returns navigation chrome, use
Firecrawl scrape (`firecrawl_scrape`, formats markdown, onlyMainContent true).

For each result capture: title, source, URL, one-sentence summary of what happened.

## STEP 2: WRITE THE BRIEF

Create `Daily Briefs\brief_YYYY-MM-DD.md`:

```
# 🛡️ Cybersecurity Morning Brief
**[Day of week], [Date]**

---

## 🚨 Government Advisories
[CISA and ACSC items]

## 📰 Top Security News
[News items]

## 🤖 AI & Security
[AI-related cybersecurity stories]

## 🗣️ Community Pulse
[Top Reddit posts from r/netsec and r/cybersecurity: title, Source: r/<sub> | [Link](url), score if available, and a "Why it matters:" line]

## 📌 Today's Signal
[ONE paragraph: the overarching theme connecting today's stories. What should a strategic decision-maker be thinking about?]

---

## 📝 Outstanding Substack Drafts
[per brief-rules.md; omit if none]

---
*To flag an item for Substack: react 📌 on it in Slack, or save the URL and notes to Substack Drafts\.*
*To post to LinkedIn, open the LinkedIn Posts\ folder and copy-paste the draft.*
```

Every item follows the item shape in brief-rules.md, with a "💡 Strategic take:" of 2 to 3
sentences: thought leader, strategic, business and policy implications, what decision-makers should
know. Specific, not generic.

## STEP 3: WRITE THE LINKEDIN POST DRAFT

Create `LinkedIn Posts\linkedin_YYYY-MM-DD.md`. A LinkedIn article of 500 to 700 words as Lars
Klander, cybersecurity thought leader:
- Hook: provocative, specific opening. No "In today's fast-paced world".
- Weave 3 or 4 of today's stories into one strategic narrative.
- Draw out the bigger-picture implication: what trend or risk does this reveal?
- End with a clear, opinionated takeaway for decision-makers.
- Short paragraphs. 4 to 6 hashtags at the end (#CyberSecurity #InfoSec etc.).

```
# LinkedIn Post - [Date]
**Status:** Draft (review before posting)

---

[Post content]
```

## STEP 4: POST TO SLACK

Follow `D:\vc-personal-projects\Morning Brief with Forwarding\heinlein\common\post-brief-to-slack.md`
for the file you wrote in STEP 2.

## STEP 5: PRESENT TO LARS

Four lines: items found per section, one sentence on today's dominant theme, any lane that failed,
the Slack parent link (or "Slack not configured"). Present the two files. Keep it brief.
