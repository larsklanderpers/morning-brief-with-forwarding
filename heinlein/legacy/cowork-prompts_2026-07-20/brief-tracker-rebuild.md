---
name: brief-tracker-rebuild
description: Daily 5:15am rebuild of the Brief Tracker artifact from the day's Cyber, AI, and AI Work brief files
---

You rebuild Lars's "Brief Tracker Daily" Cowork artifact each morning so it always reflects the current day's briefs. Today's date is in your context; use it as YYYY-MM-DD (call it TODAY).

## SOURCE FILES (read whichever exist for TODAY)
Folder: D:\vc-personal-projects\Morning Brief with Forwarding\
- Cyber brief:  Daily Briefs\brief_TODAY.md
- AI brief:     AI Briefs\ai_brief_TODAY.md
- AI Work brief: AI Briefs\work_brief_TODAY.md

If a file for TODAY is missing (a brief hasn't run yet), fall back to the most recent earlier date for that ONE brief so its tab still shows something, and note nothing else. If the AI Work brief has never been generated yet, leave that tab empty (see below).

## WHAT TO DO
The artifact is a data-driven HTML template. ALL content lives in a single JavaScript object literal `const BRIEF_DATA = { ... };`. The render engine below it must NOT be touched. Your entire job is to regenerate that one object from today's brief files and push the update.

1. Read the current artifact HTML at:
   C:\Users\LarsDev\Claude\Artifacts\brief-tracker-daily\index.html
   (Read it so you preserve the exact template — styles, render engine, everything except BRIEF_DATA.)

2. Read the brief markdown files for TODAY.

3. Build a new BRIEF_DATA object with this exact shape:
```
const BRIEF_DATA = {
  dateLabel: "Weekday, Month D, YYYY",   // e.g. "Tuesday, July 7, 2026"
  dateStamp: "YYYY-MM-DD",               // = TODAY; this keys per-day read state, so it MUST change daily
  tabs: [
    { id:"cyber", label:"🛡️ Cyber Brief", color:"#c53030", sections:[ ... ] },
    { id:"ai",    label:"🤖 AI Brief",    color:"#2b6cb0", sections:[ ... ] },
    { id:"work",  label:"🧭 AI Work Brief", color:"#276749", sections:[ ... ] }
  ]
};
```
   Each section: `{ title:"<emoji + heading from the brief>", items:[ ... ] }`.
   Each item: `{ tags:[{cls:"<tag class>",label:"<SHORT LABEL>"}], source:"<publication/source>", title:"<the item's headline>", summary:"<1–3 tight sentences: the what + the strategic take, trimmed>" }`.
   - Make ONE item per distinct story/bullet in the brief. Typical: Government Advisories, Top Security News, AI & Security, Community Pulse, Today's Signal (cyber); Frontier Labs, Shipping with AI, Local Models, Privacy/PII, AU/EU Ecosystem, Today's Signal (AI); What Creators Are Saying, The Conversation on X, Practitioner Ground Truth, Podcasts & Newsletters, New Roles & Archetypes, The Debate, Today's Signal (AI Work).
   - Skip a section if the brief says nothing fresh for it (e.g. "Nothing material"/"Skipped"). Don't invent items.
   - Keep each summary short — this is a scan tracker, not the full brief. Trim the 💡 strategic take to its core sentence.

   Available tag classes (pick the closest): tag-default, tag-gov, tag-cve, tag-breach, tag-ai, tag-signal, tag-community, tag-frontier, tag-privacy, tag-local, tag-ecosystem, tag-shipping, tag-pii (use for ⚠️ PII Flag items), tag-role (new roles/archetypes), tag-youtube, tag-debate. Use tag-signal with label "Signal" for each "Today's Signal" item.

   For the AI Work tab: if work_brief_TODAY.md does NOT exist and no earlier work_brief_*.md exists either, set that tab to `{ id:"work", label:"🧭 AI Work Brief", color:"#276749", sections:[], empty:"The AI Work &amp; the Shape of Work-to-Come community brief runs each morning at 8am — its content will appear here once today's run completes." }`.

4. Produce the full updated HTML: take the current template and replace ONLY the `const BRIEF_DATA = { ... };` block (from `const BRIEF_DATA =` up to and including its closing `};`) with your new object. Leave the STORAGE_KEY line and the entire render engine unchanged. Write the result to a scratch .html file.

5. Sanity-check: extract the last <script> block and run `node --check` on it to confirm no JS syntax errors. Fix any before pushing. Watch for unescaped characters in strings — prefer straight quotes, and avoid unescaped double-quotes inside double-quoted JS strings (use single quotes or rephrase).

6. Call update_artifact with id "brief-tracker-daily", html_path pointing to your scratch file, and update_summary like "Refreshed to <weekday>'s briefs". Do NOT create a new artifact — update the existing one.

7. Report to Lars in 1–2 sentences: which briefs were included, total item count per tab, and note if any brief was missing/stale. Keep it brief — Lars prefers concise updates.

Do not post anything anywhere else. This task only rebuilds the tracker artifact.