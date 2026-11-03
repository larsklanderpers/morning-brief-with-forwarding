---
name: heinlein-brief-ai
description: Daily 04:45 AI Morning Brief (frontier labs, shipping, local models, privacy/PII, AU/EU, Substack inbox, social, AIDB), LinkedIn draft, posted to #heinlein-briefs
schedule: 45 4 * * *
replaces: Cowork task ai-morning-brief (legacy/cowork-prompts_2026-07-20/ai-morning-brief.md) plus the AI Chat Daily and Firecrawl-AIDB lanes from the root ai-morning-brief-skill.md of 2026-07-21
---

You are running the daily AI Morning Brief for Lars Klander. Today's date is in your context.
Gather today's AI intelligence across the lanes below, write the brief, draft the LinkedIn post,
post the brief to Slack.

## STEP 0: READ THE SHARED RULES

Read `heinlein/common/brief-rules.md` and
apply it.

Workspace root: `./` (the repository root, which is the working directory)
- `AI Briefs\` : the brief markdown, `ai_brief_YYYY-MM-DD.md`
- `LinkedIn Posts\` : the LinkedIn draft, `ai_linkedin_YYYY-MM-DD.md`
- `Substack Drafts\` : only written when Lars flags items

## STEP 0b: BACKFILL ANY PREVIOUS SOCIAL-LANE MISS

Look for `AI Briefs\.social_pending_*.md`. If any exist:
1. Run the Lane 6 preflight below. If no browser is connected, leave the markers alone and go to
   STEP 1.
2. If a browser is connected, for each marker (oldest first, at most 3): read which date is
   missing its social lane, run that date's Lane 6 searches now (results will be current, that is
   expected), open that `ai_brief_YYYY-MM-DD.md` and replace the placeholder
   "## 📡 Social Intelligence" section with the recovered content, prefixed with one line:
   *Backfilled [today]: Chrome was unavailable at the original run; signals are current as of
   backfill.* Delete the marker only after the brief is updated.
3. Say which dates you backfilled in STEP 5.

## STEP 1: GATHER INTELLIGENCE

Run ALL of the following. Last 24 to 48 hours where possible. To add a source, add a line to the
lane it belongs to.

**Lane 1: Frontier Labs**
1. WebSearch: "OpenAI news today" OR "Anthropic news today" OR "Google DeepMind news today"
2. WebSearch: "Meta AI" OR "Mistral AI" OR "xAI Grok" news this week
3. WebSearch: "new AI model release 2026" OR "frontier model benchmark"

**Lane 2: Shipping with AI**
4. WebSearch: "AI product launch 2026" OR "built with AI" OR "AI integration shipped"
5. WebSearch: site:reddit.com/r/LocalLLaMA OR site:reddit.com/r/MachineLearning "released" OR "launched"
6. Fetch: https://www.reddit.com/r/MachineLearning/hot.json?limit=8
7. Fetch: https://www.reddit.com/r/LocalLLaMA/hot.json?limit=8
(If Reddit JSON is blocked, cover it via WebSearch; do not try other fetch methods.)

**Lane 3: Local Models**
8. WebSearch: "local LLM news 2026" OR "open weights model release" OR "Ollama" OR "llama.cpp" OR "LM Studio"
9. WebSearch: "open source AI model 2026" OR "self-hosted AI" OR "on-premise LLM"

**Lane 4: Privacy, PII and Data Sovereignty (AU/GDPR)**
10. WebSearch: "AI privacy Australia 2026" OR "Australian Privacy Act AI" OR "OAIC AI"
11. WebSearch: "GDPR AI compliance 2026" OR "EU AI Act enforcement" OR "data sovereignty AI"
12. WebSearch: "local AI model privacy GDPR" OR "on-premise AI compliance" OR "AI PII protection"
13. WebSearch: "AI data residency Australia" OR "sovereign AI Australia" OR "APRA AI data"

**Lane 5: AU/EU AI Ecosystem**
14. WebSearch: "AI regulation Australia 2026" OR "Australia AI policy" OR "Australian AI startup"
15. WebSearch: "European AI model" OR "EU sovereign AI" OR "Mistral Europe" OR "AI made in Europe"
16. WebSearch: "local AI model GDPR countries" OR "AI without cloud" OR "edge AI privacy"

**Lane 5b: AI Chat Daily sweep (aichatdaily.com)**
Beat pages are plain HTML indexes (headline, summary, relative time). Pull items from the last 48h
and fold each into the lane it belongs to, tagged Source: AI Chat Daily. No separate section.
Dedupe against WebSearch results and cite the primary source when both cover a story. Skip the
careers beat (it belongs to the work brief) and the faith beat.
17. WebFetch: https://aichatdaily.com/ai-news
18. WebFetch: https://aichatdaily.com/ai-models (Lanes 1 and 3)
19. WebFetch: https://aichatdaily.com/ai-tools (Lane 2)
20. WebFetch: https://aichatdaily.com/ai-business (Lanes 1 and 5)
21. WebFetch: https://aichatdaily.com/ai-security (Lane 4)
22. WebFetch: https://aichatdaily.com/ai-analysis (informs Today's Signal)

**Lane 6: Social Intelligence (LinkedIn and X)**

Needs the Claude in Chrome tools. Lars's machine runs all the time, so no browser means Chrome is
closed or the extension dropped, not that the lane should be quietly abandoned.

Preflight:
1. One ToolSearch call:
   `select:mcp__claude-in-chrome__list_connected_browsers,mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__read_page`
2. Call `list_connected_browsers`. If at least one browser: `tabs_context_mcp` with createIfEmpty
   true, then run the searches. If empty or error: wait about 60 seconds and retry, 3 attempts.
3. If all 3 fail, degrade loudly:
   - Write the section as:
     `## 📡 Social Intelligence`
     `⚠️ **Lane skipped: no Chrome browser connected at [HH:MM] after 3 attempts.** LinkedIn and X signals are missing today. A backfill marker has been written; the next run recovers this lane once Chrome is connected.`
   - Write `AI Briefs\.social_pending_YYYY-MM-DD.md` with the target brief filename, the failed
     attempt timestamps and the Lane 6 URLs still to run.
   - Say so in STEP 5. Do not fetch LinkedIn or X any other way. Chrome or nothing.

LinkedIn searches (top 3 to 5 posts each: author, snippet, engagement):
- https://www.linkedin.com/search/results/content/?keywords=%23AIGovernance&datePosted=past-24h&sortBy=date_posted
- https://www.linkedin.com/search/results/content/?keywords=%23AIPolicy+Australia&datePosted=past-24h&sortBy=date_posted
- https://www.linkedin.com/search/results/content/?keywords=%23AISovereignty&datePosted=past-24h&sortBy=date_posted
- https://www.linkedin.com/search/results/content/?keywords=%23ResponsibleAI+Australia&datePosted=past-24h&sortBy=date_posted

X searches (top 3 to 5 posts each: handle, snippet, engagement):
- https://x.com/search?q=AI+licensing+regime+frontier+models&src=typed_query&f=live
- https://x.com/search?q=sovereign+AI+Australia+local+models&src=typed_query&f=live
- https://x.com/search?q=AI+data+sovereignty+GDPR+2026&src=typed_query&f=live
- https://x.com/search?q=%23AIGovernance+Australia&src=typed_query&f=live

If the browser drops mid-lane, keep what you have, note which searches were incomplete, and write
the marker listing only the URLs that did not complete.

**Lane 6b: The AI Daily Brief episode (aidailybrief.ai)**
The page is client-rendered. Ladder, in order:
- Firecrawl scrape `https://aidailybrief.ai/e/<today YYYY-MM-DD>` with formats ["markdown"],
  onlyMainContent true, waitFor 5000.
- If Firecrawl is absent or errors, read the same URL with the Chrome tools.
- If today 404s, try yesterday once. Otherwise note "no fresh AIDB episode" and move on.
- Transcript at `/e/YYYY-MM-DD/transcript.md`, only when an item needs direct quotes.
Fold AIDB items into the lanes, tagged Source: The AI Daily Brief, and keep the episode subsection
in the Social section (format below).

**Lane 7: Substack Inbox (Lars's subscriptions)**

Gmail tools, read only:
- `search_threads` with `from:substack.com newer_than:1d` (page through; typically 15 to 25 a day).
- Keep newsletters on the brief's beats: AI, frontier labs, local and open models, AI security,
  privacy and data sovereignty, AI policy and governance, future of work, AI product and
  engineering practice. Skip politics, news, art and lifestyle newsletters, live-video
  notifications, Substack administrative mail (no-reply@substack.com), and anything from
  larsklander@substack.com (his own publication).
- For each relevant newsletter, `get_thread` with full content and read the body, not the snippet.
- If an email is truncated or the piece merits it (strong PII, sovereignty or regulated-industry
  angle), open the post on substack.com with the Chrome tools (Lars is logged in there) and read
  it with `get_page_text`. If Chrome is unavailable, work from the email body and say the item
  was not read in full.
- Per item: newsletter name, post title, URL from the email, 1 to 2 sentence summary, why it
  matters to Lars's audience. Pick the 3 to 6 strongest. If a Substack item is a major story for
  Lanes 1 to 5, put it there and cite the newsletter instead of duplicating.
- Never archive, label, delete or reply to any email; never like, comment or subscribe on Substack.
- If Gmail tools are unavailable, skip the lane and say so.

## STEP 2: WRITE THE BRIEF

Create `AI Briefs\ai_brief_YYYY-MM-DD.md`:

```
# 🤖 AI Morning Brief
**[Day of week], [Date]**

---

## 🔬 Frontier Labs
[OpenAI, Anthropic, Google DeepMind, Meta AI, Mistral, xAI]

## 🚀 Shipping with AI
[Product launches, integrations, developer tools shipped]

## 🏠 Local Models
[Open-weights releases, self-hosted LLM news, Ollama, llama.cpp, LM Studio]

## 🔒 Privacy, PII & Data Sovereignty
[AI privacy regulation, GDPR and Australian Privacy Act enforcement, data residency, PII protection]
⚠️ Flag any story where cloud AI vendors expand data collection or a breach involved AI-processed PII.

## 🌏 AU/EU AI Ecosystem
[Australian and European AI policy, sovereign AI, local model development, running AI without sending data offshore]

## 📬 From the Substacks
[First line: "N newsletters scanned. M surfaced." Then 3 to 6 items:]
**[Newsletter Name] - "Post Title"**
- [1 to 2 sentence summary] - URL
💡 Strategic take: [why it matters, what Lars might do with it: "possible response piece", "cite in [thread]"]

## 📡 Social Intelligence
[Top LinkedIn and X signals:]
**[Platform] @handle or Author Name** - *[key point or quote]*
*Why it matters: [one sentence for Lars's regulated-industry audience]*
[If the Chrome preflight failed, the ⚠️ block from Lane 6 goes here instead.]

### 🎙️ AI Daily Brief - [Episode Title]
[Top 3 key points. Omit the subsection if no episode was found.]

## 📌 Today's Signal
[ONE paragraph: the theme connecting today's stories, weighted to how businesses with sensitive customer data should think about AI adoption. What is the strategic read for a decision-maker balancing AI capability against PII obligations?]

---

## 📝 Outstanding Substack Drafts
[per brief-rules.md; omit if none]

---
*To flag an item for Substack: react 📌 on it in Slack, or save the URL and notes to Substack Drafts\.*
*To post to LinkedIn, open the LinkedIn Posts\ folder and review the ai_linkedin_YYYY-MM-DD.md draft.*
```

Every item follows the item shape in brief-rules.md, with a "💡 Strategic take:" of 2 to 3
sentences in Lars's voice, weighted to implications for businesses that must protect customer PII.

## STEP 3: WRITE THE LINKEDIN POST DRAFT

Create `LinkedIn Posts\ai_linkedin_YYYY-MM-DD.md`. A LinkedIn article of 500 to 700 words as Lars
Klander, AI and privacy thought leader:
- Hook: provocative, specific opening, no clichés.
- Weave 2 or 3 of today's stories into one strategic narrative.
- Angle: the tension between AI capability and data privacy or sovereignty. That is his edge.
- Draw out the implication for businesses with PII obligations.
- End with a clear, opinionated call to action for decision-makers.
- Short paragraphs. 4 to 6 hashtags (#AI #PrivacyByDesign #DataSovereignty #LocalAI #GDPR #AustralianPrivacyAct and similar).

```
# AI LinkedIn Post - [Date]
**Status:** Draft (review before posting)

---

[Post content]
```

## STEP 4: POST TO SLACK

Follow `heinlein/common/post-brief-to-slack.md`
for the file you wrote in STEP 2.

## STEP 5: PRESENT TO LARS

Keep it short:
- Items per lane, including newsletters scanned vs surfaced.
- One sentence on today's dominant theme.
- Any PII or privacy story that is particularly material to his business.
- AIDB episode title if found.
- Outstanding drafts count, if any.
- Chrome and social lane status, explicitly: ran clean, backfilled a date, or failed with a marker.
- The Slack parent link, or "Slack not configured".
