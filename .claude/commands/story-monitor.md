# AI Product Story Monitor

You are running a story monitor for Lars Klander (lars.klander@gmail.com). The story is "You Are the Product: How AI Followed the Playbook Everyone Swore It Wouldn't," covering ChatGPT advertising, GPT-Bidi-1, Microsoft Copilot data leaks, Google Gemini data/advertising pipeline, and the @tag corporate-secrets risk.

Run all five searches, compile the briefing, write it to a temp file, then create the Gmail draft via `story_monitor_draft.py`. Do this non-interactively — make reasonable editorial calls without stopping to ask.

---

## Step 1 — Search all five threads

Run these in parallel if possible:

1. `GPT-Bidi-1 launch` OR `ChatGPT bidirectional audio 2026` — official announcements, new privacy disclosures
2. `ChatGPT ads` OR `OpenAI advertising 2026` — policy changes, new ad formats, data practices
3. `Microsoft Copilot vulnerability` OR `Copilot data leak 2026` — new CVEs, incidents, patches
4. `Gemini privacy` OR `Google AI advertising data 2026` — policy updates, new disclosures
5. `enterprise AI data leak` OR `shadow AI 2026` — significant new incidents or statistics

Skip minor blog rehashes. Only report new incidents, official announcements, policy changes, or statistics that materially update the story.

---

## Step 2 — Compile the briefing

Format the findings as a short HTML briefing with three sections:
- **What's new** (one `<li>` per item with source link and one sentence of story-impact context)
- **Story impact** (prose: does it strengthen, complicate, or require updating any section?)
- **Urgency** (one line: can wait / update before next publish / time-sensitive)

Use this HTML skeleton:

```html
<html><body style="font-family:Georgia,serif;max-width:680px;margin:0 auto;color:#222;">
<h2 style="border-bottom:1px solid #ccc;padding-bottom:6px;">AI Product Story Monitor — DATE</h2>
<p style="font-size:.85em;color:#666;">Monitoring: "You Are the Product" — all five story threads.</p>
<h3>What's new</h3>
<ul style="line-height:1.8;">
  <!-- one <li> per material development -->
</ul>
<h3>Story impact</h3>
<p>...</p>
<h3>Urgency</h3>
<p>...</p>
<hr style="margin-top:2em;border:none;border-top:1px solid #eee;">
<p style="font-size:.75em;color:#999;">Automated monitor run · DATE · "You Are the Product" story thread</p>
</body></html>
```

Replace DATE with today's date in `DD Mon YYYY` format.

---

## Step 3 — Write to temp file and send draft

```bash
# Write the HTML to a temp file
python -c "
import sys, pathlib, datetime
html = sys.stdin.read()
p = pathlib.Path('D:/vc-personal-projects/Morning Brief with Forwarding/.claude/story_monitor_tmp.html')
p.write_text(html, encoding='utf-8')
print(p)
" << 'HTMLEOF'
[paste your HTML here]
HTMLEOF

# Create the Gmail draft
python "D:/vc-personal-projects/Morning Brief with Forwarding/story_monitor_draft.py" \
  --subject "AI Product Story Monitor — $(date +%Y-%m-%d)" \
  --file "D:/vc-personal-projects/Morning Brief with Forwarding/.claude/story_monitor_tmp.html"
```

Or more simply, write the HTML content directly to the temp file using the Write tool, then run:

```bash
cd "D:/vc-personal-projects/Morning Brief with Forwarding"
python story_monitor_draft.py --subject "AI Product Story Monitor — YYYY-MM-DD" --file ".claude/story_monitor_tmp.html"
```

---

## Done

Report: how many material developments found, which threads had activity, whether the draft was created successfully. One or two sentences max.
