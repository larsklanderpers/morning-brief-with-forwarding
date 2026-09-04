---
name: ai-morning-brief
description: Daily 4:45am AI intelligence briefing — frontier labs, local models, privacy/PII, Australia & GDPR, LinkedIn + X social scan (self-healing if Chrome is down), Substack inbox scan, AIDB episode check
---

You are running the daily AI Morning Brief for Lars Klander. Today's date is available in your context. Your job is to gather today's top AI intelligence across seven lanes, write a formatted brief, and produce a LinkedIn post draft.

Lars runs a business where protecting customer PII is a top priority. Content about data sovereignty, local/on-premise models, GDPR/Australian Privacy Act compliance, and AI privacy risks is always material. His Substack and LinkedIn audience skews toward regulated industries (financial services, government, health) and Australian/UK/EU markets.

## WORKSPACE
Save all output files to: D:\vc-personal-projects\Morning Brief with Forwarding\

Subfolders:
- AI Briefs\  — the morning brief markdown
- LinkedIn Posts\ — the LinkedIn post draft (same folder as cyber brief, prefix with ai_)
- Substack Drafts\ — (only written when user flags items manually)

## STEP 0: BACKFILL ANY PREVIOUS SOCIAL-LANE MISS

Before gathering today's news, check for leftover work from a previous run:

Look for files matching D:\vc-personal-projects\Morning Brief with Forwarding\AI Briefs\.social_pending_*.md

If one or more exist:
1. Run the Lane 6 preflight (see below). If no browser is connected, leave the marker files alone and move on to STEP 1 — do not delete them.
2. If a browser IS connected, then for each marker file (oldest first, maximum 3):
   - Read the marker to see which date's brief is missing its social lane.
   - Run that date's Lane 6 searches now (results will be current, not historical — that is expected and fine).
   - Open the corresponding ai_brief_YYYY-MM-DD.md and REPLACE the placeholder "## 📡 Social Intelligence" section with the recovered content, prefixed with a one-line note: *Backfilled [today's date] — Chrome was unavailable at the original run time; signals below are current as of backfill.*
   - Delete the marker file only after the brief has been successfully updated.
3. Note in your STEP 5 summary which dates you backfilled.

## STEP 1: GATHER INTELLIGENCE

Run ALL of the following searches. Pull results from the last 24–48 hours where possible.

**Lane 1 — Frontier Labs**
1. WebSearch: "OpenAI news today" OR "Anthropic news today" OR "Google DeepMind news today"
2. WebSearch: "Meta AI" OR "Mistral AI" OR "xAI Grok" news this week
3. WebSearch: "new AI model release 2026" OR "frontier model benchmark"

**Lane 2 — Shipping with AI**
4. WebSearch: "AI product launch 2026" OR "built with AI" OR "AI integration shipped"
5. WebSearch: site:reddit.com/r/LocalLLaMA OR site:reddit.com/r/MachineLearning "released" OR "launched"
6. Fetch: https://www.reddit.com/r/MachineLearning/hot.json?limit=8 — parse JSON for top posts
7. Fetch: https://www.reddit.com/r/LocalLLaMA/hot.json?limit=8 — parse JSON for top posts
(Note: if the Reddit JSON fetches are blocked, cover the Reddit signal via WebSearch instead — do not try alternative fetch methods.)

**Lane 3 — Local Models**
8. WebSearch: "local LLM news 2026" OR "open weights model release" OR "Ollama" OR "llama.cpp" OR "LM Studio"
9. WebSearch: "open source AI model 2026" OR "self-hosted AI" OR "on-premise LLM"

**Lane 4 — Privacy, PII & Data Sovereignty (AU/GDPR)**
10. WebSearch: "AI privacy Australia 2026" OR "Australian Privacy Act AI" OR "OAIC AI"
11. WebSearch: "GDPR AI compliance 2026" OR "EU AI Act enforcement" OR "data sovereignty AI"
12. WebSearch: "local AI model privacy GDPR" OR "on-premise AI compliance" OR "AI PII protection"
13. WebSearch: "AI data residency Australia" OR "sovereign AI Australia" OR "APRA AI data"

**Lane 5 — Thought Leadership: AU/EU AI Ecosystem**
14. WebSearch: "AI regulation Australia 2026" OR "Australia AI policy" OR "Australian AI startup"
15. WebSearch: "European AI model" OR "EU sovereign AI" OR "Mistral Europe" OR "AI made in Europe"
16. WebSearch: "local AI model GDPR countries" OR "AI without cloud" OR "edge AI privacy"

**Lane 6 — Social Intelligence (LinkedIn + X)**

This lane needs the Claude in Chrome MCP tools. Lars's machine runs 24/7, so an unavailable browser means Chrome itself is closed or the extension has dropped its connection — NOT that the lane should be quietly abandoned.

**Preflight — do this before any social searches:**
1. Load the Chrome tools in one ToolSearch call:
   `select:mcp__claude-in-chrome__list_connected_browsers,mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__read_page`
2. Call `list_connected_browsers`.
   - If it returns at least one browser, call `tabs_context_mcp` with createIfEmpty: true and proceed with the searches below.
   - If it returns an empty list or errors, wait ~60 seconds and retry. Try up to 3 times total (roughly 2 minutes of patience) — the extension sometimes reconnects on its own.
3. If all 3 attempts fail, DEGRADE LOUDLY rather than silently:
   - Write the brief's Social Intelligence section as:
     `## 📡 Social Intelligence`
     `⚠️ **Lane skipped — no Chrome browser connected at [HH:MM] after 3 attempts.** LinkedIn and X signals are missing from today's brief. A backfill marker has been written; the next run will recover this lane automatically once Chrome is connected.`
   - Write a marker file at: D:\vc-personal-projects\Morning Brief with Forwarding\AI Briefs\.social_pending_YYYY-MM-DD.md containing the target brief filename, the timestamp of each failed attempt, and the list of Lane 6 URLs that still need running.
   - Call this out explicitly in your STEP 5 summary to Lars — do not bury it.
   - Do NOT attempt to fetch LinkedIn or X through web_fetch, curl, Python, or any other method. Chrome MCP or nothing.

**LinkedIn searches** — navigate to each URL and extract the top 3–5 posts (author, post snippet, engagement if visible):
- https://www.linkedin.com/search/results/content/?keywords=%23AIGovernance&datePosted=past-24h&sortBy=date_posted
- https://www.linkedin.com/search/results/content/?keywords=%23AIPolicy+Australia&datePosted=past-24h&sortBy=date_posted
- https://www.linkedin.com/search/results/content/?keywords=%23AISovereignty&datePosted=past-24h&sortBy=date_posted
- https://www.linkedin.com/search/results/content/?keywords=%23ResponsibleAI+Australia&datePosted=past-24h&sortBy=date_posted

**X (Twitter) searches** — navigate to each URL and extract the top 3–5 tweets (handle, text snippet, engagement):
- https://x.com/search?q=AI+licensing+regime+frontier+models&src=typed_query&f=live
- https://x.com/search?q=sovereign+AI+Australia+local+models&src=typed_query&f=live
- https://x.com/search?q=AI+data+sovereignty+GDPR+2026&src=typed_query&f=live
- https://x.com/search?q=%23AIGovernance+Australia&src=typed_query&f=live

If the browser drops mid-lane (a tool starts erroring after some searches succeeded), keep whatever you gathered, note which searches were incomplete in the section, and write the marker file listing only the URLs that did not complete.

**AI Daily Brief episode check** — fetch today's episode page. Try in order:
- https://aidailybrief.ai/e/[TODAY'S DATE as YYYY-MM-DD] (e.g. for June 30: https://aidailybrief.ai/e/2026-06-30)
- If 404, try yesterday's date (navigate via the Chrome MCP if web_fetch declines the URL)
- If found, read the episode title and top 3 key points from the transcript (available at same URL + /transcript.md)
- Note: AIDB episodes are public and free — no login required
- The AIDB site is client-rendered; if web_fetch returns a page shell with no episode content, use the Chrome MCP tools rather than retrying the fetch. If Chrome is unavailable, note "AIDB check skipped — Chrome unavailable" and include it in the marker file.

For each social result, note: platform, handle/author, key point, why it's relevant to Lars's audience.

**Lane 7 — Substack Inbox (Lars's subscriptions)**

Use the Gmail MCP tools to pull the last 24 hours of Substack newsletter email:
- search_threads with query: `from:substack.com newer_than:1d` (page through if needed; there are typically 15–25/day)
- FILTER to newsletters relevant to the brief's beats: AI, frontier labs, local/open models, AI security, privacy/data sovereignty, AI policy/governance, future of work, AI product/engineering practice. SKIP: politics/news/art/lifestyle newsletters, live-video notifications, Substack administrative mail (no-reply@substack.com), and anything from larsklander@substack.com (his own publication — stats/share notifications, not a source).
- For each relevant newsletter, call get_thread (FULL_CONTENT) and read the actual body — don't rely on the snippet.
- If an email is truncated, teases a longer post, or the piece merits deeper reading (strong relevance to PII/sovereignty/regulated-industry angles), open the post itself on substack.com using the Claude in Chrome MCP tools — Lars is logged into his Substack account in Chrome, so subscriber-only content is readable there. Read it with get_page_text. If Chrome is unavailable, work from the email body alone and note the item was not read in full.
- Extract per item: newsletter name, post title, URL (from the email), 1–2 sentence summary, and why it matters to Lars's audience. Pick the 3–6 strongest items. If a Substack item is itself a major story for Lanes 1–5, use it there (cite the newsletter as source) instead of duplicating.
- Reading only — do not archive, label, delete, or reply to any email, and do not like/comment/subscribe on Substack.
- If Gmail tools are unavailable, skip this lane gracefully and note it in the summary.

For each result, extract: title/handle, source, URL, brief summary.

## STEP 2: CHECK OUTSTANDING SUBSTACK DRAFTS

Scan: D:\vc-personal-projects\Morning Brief with Forwarding\Substack Drafts\

List all .md files whose last-modified date is less than 7 days ago and whose content contains "Status: Draft" (i.e., not yet submitted/published). For each, extract the filename, title (first H1 heading), and age in days.

These will be surfaced in the brief under a dedicated section.

## STEP 3: WRITE THE BRIEF

Create a markdown file at: D:\vc-personal-projects\Morning Brief with Forwarding\AI Briefs\ai_brief_YYYY-MM-DD.md

Format:

```
# 🤖 AI Morning Brief
**[Day of week], [Date]**

---

## 🔬 Frontier Labs
[Top stories from OpenAI, Anthropic, Google DeepMind, Meta AI, Mistral, xAI — title, source, URL, 1-2 sentence summary, strategic take]

## 🚀 Shipping with AI
[Notable AI product launches, integrations, or developer tools shipped — title, source, URL, summary, strategic take]

## 🏠 Local Models
[Open-weights releases, self-hosted LLM news, Ollama/llama.cpp/LM Studio updates — title, source, URL, summary, strategic take]

## 🔒 Privacy, PII & Data Sovereignty
[AI privacy regulation, GDPR/Australian Privacy Act enforcement, data residency news, PII protection approaches — title, source, URL, summary, strategic take]
⚠️ Flag any story where cloud AI vendors are expanding data collection or where a breach involved AI-processed PII.

## 🌏 AU/EU AI Ecosystem
[Australian and European AI policy, sovereign AI initiatives, local model development, thought leadership on running AI without sending data offshore — title, source, URL, summary, strategic take]

## 📬 From the Substacks
[3–6 strongest items from Lars's Substack subscriptions (Lane 7). Format each as:
**[Newsletter Name] — "Post Title"** — [1-2 sentence summary] — URL
💡 Strategic take: [why it matters / what Lars might do with it — including "possible Substack response piece" or "cite in [thread]" where apt]]

## 📡 Social Intelligence
[Top signals from LinkedIn and X. Format each as:
**[Platform] @handle or Author Name** — [key point or quote snippet]
*Why it matters: [1 sentence relevance to Lars's regulated-industry audience]*
If the Chrome preflight failed, use the ⚠️ skipped-lane block from Lane 6 instead.]

### 🎙️ AI Daily Brief — [Episode Title if found]
[Top 3 key points from today's (or yesterday's) AIDB episode. If no episode found, omit this subsection.]

## 📌 Today's Signal
[ONE paragraph: the overarching theme or trend connecting today's stories. Particular weight on anything that affects how businesses with sensitive customer data (like Lars's) should be thinking about AI adoption. What's the strategic read for a decision-maker who must balance AI capability with PII obligations?]

---

## 📝 Outstanding Substack Drafts
[Table of any .md files in Substack Drafts\ that are less than 7 days old and still marked "Status: Draft". Columns: filename, title, age. If none, omit this section entirely.]

---
*To flag an item for Substack, save the article URL and notes to: D:\vc-personal-projects\Morning Brief with Forwarding\Substack Drafts\*
*To post to LinkedIn, open the LinkedIn Posts\ folder and review the ai_linkedin_YYYY-MM-DD.md draft.*
```

For each item, add a "💡 Strategic take:" — 2-3 sentences in Lars's voice: thought leader, strategic, big-picture, business and policy implications. Be specific. Don't start with "This article" or "This is important because." Give particular weight to implications for businesses that must protect customer PII.

If a lane has no fresh news, write "Nothing material in the last 24h." — don't pad with stale items. Distinguish this from a lane that could not run: "nothing material" means you looked and found nothing; a tooling failure gets the ⚠️ treatment and a marker file.

## STEP 4: WRITE THE LINKEDIN POST DRAFT

Create a file at: D:\vc-personal-projects\Morning Brief with Forwarding\LinkedIn Posts\ai_linkedin_YYYY-MM-DD.md

Write a LinkedIn article (500-700 words) as Lars Klander, AI and privacy thought leader:
- Hook: provocative, specific opening — no clichés
- Weave 2-3 of today's stories into a coherent strategic narrative
- Angle: lean toward the tension between AI capability and data privacy/sovereignty — this is Lars's distinctive perspective
- Draw out the bigger-picture implication for businesses with PII obligations
- End with a clear, opinionated call-to-action for decision-makers
- Short paragraphs, LinkedIn-optimised
- 4-6 relevant hashtags (#AI #PrivacyByDesign #DataSovereignty #LocalAI #GDPR #AustralianPrivacyAct etc.)

Format:
```
# AI LinkedIn Post — [Date]
**Status:** Draft (review before posting)

---

[Post content here]
```

## STEP 5: PRESENT TO LARS

After saving both files:
- State how many items found across which lanes (including how many Substack newsletters were scanned vs. surfaced)
- One sentence on today's dominant theme
- Flag any PII/privacy stories that are particularly material to his business
- Note the AIDB episode title if one was found today
- Call out how many outstanding Substack drafts were found (if any)
- **Explicitly report the Chrome/social lane status**: ran clean, backfilled an earlier date, or failed with a marker written. Never let a skipped lane pass without mention.
- Present the two files so he can open them

Keep the summary brief — Lars prefers concise updates.