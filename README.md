# Cybersecurity Morning Brief — Setup Guide

## What this does
Every morning at 9am, Claude automatically:
1. Searches cybersecurity news, Reddit, CISA, ACSC, AI/security stories
2. Writes a formatted intelligence brief → `Daily Briefs/`
3. Drafts a LinkedIn post → `LinkedIn Posts/`

You then review and can publish, or flag items for longer Substack articles.

---

## Folder Structure
```
Morning Brief with Forwarding/
├── Daily Briefs/          ← Morning briefs (auto-generated)
├── LinkedIn Posts/        ← LinkedIn drafts (auto-generated)
├── Substack Drafts/       ← Articles you flag for deeper writing
├── briefing_agent.py      ← Run manually anytime
├── linkedin_auth.py       ← One-time LinkedIn setup
├── config.json            ← Your credentials and settings
└── README.md              ← This file
```

---

## One-Time Setup

### 1. Add your Anthropic API key
Open `config.json` and replace `YOUR_ANTHROPIC_API_KEY`:
- Get one at: https://console.anthropic.com/

### 2. Set up LinkedIn posting
You need a free LinkedIn Developer App:

1. Go to https://developer.linkedin.com/ → **Create App**
2. App Name: anything (e.g. "Morning Brief")
3. Under **Products**, request access to:
   - "Share on LinkedIn"
   - "Sign In with LinkedIn using OpenID Connect"
4. Go to **Auth** tab:
   - Copy **Client ID** and **Client Secret** into `config.json`
   - Add redirect URL: `http://localhost:8888/callback`
5. Run once to authenticate:
   ```
   python linkedin_auth.py
   ```
   A browser will open → log into LinkedIn → token saved automatically.

> LinkedIn tokens last 60 days. Re-run `linkedin_auth.py` when they expire.

---

## Daily Workflow

The brief arrives automatically at 9am in your `Daily Briefs/` folder.

### To post to LinkedIn
After your morning review:
```bash
# Post the full digest (pre-drafted)
# Open LinkedIn Posts/linkedin_YYYY-MM-DD.md, review, then:
python briefing_agent.py --post <item_number>

# Or just open the LinkedIn Posts/ folder and copy-paste manually
```

### To flag an item for Substack
```bash
python briefing_agent.py --flag <item_number>
```
This creates a seed file in `Substack Drafts/` with the article, summary, and space for your notes.

### To run the brief manually (any time)
```bash
python briefing_agent.py
```

### Dry run (no AI calls, just see what's collected)
```bash
python briefing_agent.py --dry-run
```

---

## Sources Monitored
- **News**: Krebs on Security, Bleeping Computer, The Hacker News, Dark Reading, Threatpost, Schneier on Security, SANS ISC
- **Government**: CISA (US), ACSC (Australia)
- **Community**: r/netsec, r/cybersecurity, r/hacking
- **AI angle**: AI + security stories via search

---

## Troubleshooting

**Brief not appearing at 9am?**
Cowork must be open for scheduled tasks to run. If it was closed, the brief runs on next launch.

**LinkedIn token expired?**
Re-run `python linkedin_auth.py` — it detects expiry and re-authenticates.

**Want to change sources or tone?**
Edit `config.json` — the `sources` and `brief` sections control everything.
