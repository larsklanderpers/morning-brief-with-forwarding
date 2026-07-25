---
name: ai-morning-brief
description: Daily 9:15am AI intelligence briefing — frontier labs, shipping with AI, local models, privacy/PII, Australia & GDPR
---

You are running the daily AI Morning Brief for Lars Klander. Today's date is available in your context. Your job is to gather today's top AI intelligence across five lanes, write a formatted brief, and produce a LinkedIn post draft.

Lars runs a business where protecting customer PII is a top priority. Content about data sovereignty, local/on-premise models, GDPR/Australian Privacy Act compliance, and AI privacy risks is always material.

## WORKSPACE
Save all output files to: D:\vc-personal-projects\Morning Brief with Forwarding\

Subfolders:
- AI Briefs\  — the morning brief markdown
- LinkedIn Posts\ — the LinkedIn post draft (same folder as cyber brief, prefix with ai_)
- Substack Drafts\ — (only written when user flags items manually)

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

**Lane 6 — AI Chat Daily Sweep (aichatdaily.com)**
AI Chat Daily is an original daily AI-news publication ("news for operators, founders, and engineers") organised into topic beats. Its beat pages render as plain, reliably-fetchable HTML (unlike JS-heavy social feeds), so use it as a broad daily signal source that back-stops the WebSearch lanes above — it routinely surfaces shipping/model/business items the searches miss. Pull items published in roughly the last 48h.

17. WebFetch: https://aichatdaily.com/ai-news — top general stories → route each to the most relevant lane below
18. WebFetch: https://aichatdaily.com/ai-models — frontier + open-weights releases → Lane 1 (Frontier Labs) / Lane 3 (Local Models)
19. WebFetch: https://aichatdaily.com/ai-tools — product & developer-tool launches → Lane 2 (Shipping with AI)
20. WebFetch: https://aichatdaily.com/ai-business — funding, company moves, policy → Lane 1 / Lane 5 (AU/EU Ecosystem)
21. WebFetch: https://aichatdaily.com/ai-security — AI security, breaches, PII exposure → Lane 4 (Privacy, PII & Data Sovereignty)
22. WebFetch: https://aichatdaily.com/ai-analysis — commentary → informs 📌 Today's Signal and any lane

Beat pages are indexes (headline + 1–2 sentence summary + relative timestamp). That summary is usually enough for the brief; open the individual article (URL pattern `https://aichatdaily.com/[beat]/[slug]`) only when an item is strong enough to warrant a full strategic take and the index summary is too thin.

**Fold, don't silo:** do NOT create a separate "AI Chat Daily" section. Map each item into the existing lane it belongs to (per the mappings above), tag its **Source:** as "AI Chat Daily," and let it compete with the WebSearch items on merit. Deduplicate — if AI Chat Daily and a WebSearch result cover the same story, keep one entry and cite the primary/original source.

**Careers beat → hand off to the Work Community Brief (do NOT include here):** the `https://aichatdaily.com/ai-careers` beat (AI jobs, roles, workforce, hiring, layoffs, archetypes) belongs to the separate 8am *AI Work & the Shape of Work-to-Come* brief, not this one — skip it in the AI Morning Brief. The Faith beat (`/ai-faith`) is out of scope for both — skip. Exception: if a genuinely material privacy/security or frontier-lab story happens to sit in the careers beat, you may still pull that specific item into the relevant lane here — but ordinary jobs/roles/workforce content stays out of the morning brief.

**Lane — The AI Daily Brief podcast (AIDB, aidailybrief.ai)**
AIDB publishes a full written brief per episode at `https://aidailybrief.ai/e/YYYY-MM-DD` (segments with timestamps, quotes, a numbers block). The page is client-rendered: plain WebFetch sees only a shell, and the on-page "Download .md" link (`/e/YYYY-MM-DD.md`) returns 404 to a direct fetch — do not use those paths. Use this ladder (confirmed working 2026-07-21):

23. **Firecrawl scrape** — the local Firecrawl MCP server, bridge-proxied into cloud sessions (tool `firecrawl_scrape`; load via tool search): scrape `https://aidailybrief.ai/e/<today>` with formats `["markdown"]`, `onlyMainContent: true`, `waitFor: 5000`. Costs ~1 credit.
24. **Chrome fallback** — if the Firecrawl tools are absent (desktop app closed) or the scrape errors, read the same URL with the Chrome tools.
25. If today's episode 404s, try yesterday's date once (episodes skip some days); otherwise note "no fresh AIDB episode" and move on. A per-episode transcript exists at `/e/YYYY-MM-DD/transcript.md` — scrape it only when an item needs direct quotes.

Fold, don't silo — same rule as AI Chat Daily: map AIDB items into the lanes above, tag **Source:** as "The AI Daily Brief," and dedupe against WebSearch/AI Chat Daily coverage of the same story.

For each result, extract: title, source, URL, brief summary.

## STEP 2: CHECK OUTSTANDING SUBSTACK DRAFTS

Before writing the brief, scan: D:\vc-personal-projects\Morning Brief with Forwarding\Substack Drafts\

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

If a lane has no fresh news, write "Nothing material in the last 24h." — don't pad with stale items.

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
- State how many items found across which lanes
- One sentence on today's dominant theme
- Flag any PII/privacy stories that are particularly material to his business
- Call out how many outstanding Substack drafts were found (if any)
- Present the two files so he can open them

Keep the summary brief — Lars prefers concise updates.
