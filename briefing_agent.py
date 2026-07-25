#!/usr/bin/env python3
"""
Cybersecurity Morning Briefing Agent
Pulls from RSS feeds, Reddit, CISA, ACSC, and formats a daily digest
with strategic commentary via Claude API.

Usage:
  python briefing_agent.py              # Run full briefing
  python briefing_agent.py --flag <n>  # Flag item #n for Substack drafts
  python briefing_agent.py --post <n>  # Publish item #n to LinkedIn
  python briefing_agent.py --dry-run   # Show what would be collected, no AI calls
"""

import json
import os
import sys
import re
import gzip
import argparse
import urllib.request
import urllib.error
import urllib.parse
import imaplib
import email
from email.header import decode_header

from datetime import datetime, timezone, timedelta
from pathlib import Path
from xml.etree import ElementTree as ET

# ── Config ──────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
CONFIG_PATH = SCRIPT_DIR / "config.json"


def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)


# ── HTTP helpers ─────────────────────────────────────────────────────────────
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; CyberBriefBot/1.0; +personal-use)"
}


def fetch_url(url, timeout=15, accept_gz=False):
    req = urllib.request.Request(url, headers=HEADERS)
    if accept_gz:
        req.add_header("Accept-Encoding", "gzip")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
            if accept_gz and (resp.info().get("Content-Encoding") == "gzip" or url.endswith(".gz")):
                data = gzip.decompress(data)
            return data.decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  [WARN] Could not fetch {url}: {e}")
        return None


# ── RSS Parser ────────────────────────────────────────────────────────────────
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "dc": "http://purl.org/dc/elements/1.1/",
    "content": "http://purl.org/rss/1.0/modules/content/",
}


def parse_rss(xml_text, source_name, max_items=5):
    items = []
    try:
        root = ET.fromstring(xml_text)
        # RSS 2.0
        entries = root.findall(".//item")
        if not entries:
            # Atom
            entries = root.findall(".//atom:entry", NS)
        for entry in entries[:max_items]:
            title = (
                _text(entry, "title")
                or _text(entry, "atom:title", NS)
                or "Untitled"
            )
            link = (
                _text(entry, "link")
                or (entry.find("atom:link", NS).get("href") if entry.find("atom:link", NS) is not None else "")
                or ""
            )
            desc = (
                _text(entry, "description")
                or _text(entry, "atom:summary", NS)
                or _text(entry, "content:encoded", NS)
                or ""
            )
            pub_date = _text(entry, "pubDate") or _text(entry, "atom:published", NS) or ""
            # Strip HTML tags from description
            desc = re.sub(r"<[^>]+>", " ", desc).strip()
            desc = re.sub(r"\s+", " ", desc)[:500]
            items.append({
                "source": source_name,
                "title": title.strip(),
                "url": link.strip(),
                "summary": desc,
                "published": pub_date,
                "type": "news",
            })
    except Exception as e:
        print(f"  [WARN] RSS parse error for {source_name}: {e}")
    return items


def _text(elem, tag, ns=None):
    found = elem.find(tag, ns) if ns else elem.find(tag)
    if found is not None and found.text:
        return found.text.strip()
    return None


# ── Reddit ────────────────────────────────────────────────────────────────────
def fetch_reddit(subreddit, limit=10, sort="hot", filter_keywords=None):
    url = f"https://www.reddit.com/r/{subreddit}/{sort}.json?limit={limit}"
    text = fetch_url(url)
    if not text:
        return []
    try:
        data = json.loads(text)
        posts = data["data"]["children"]
        items = []
        for post in posts:
            p = post["data"]
            if p.get("stickied") or p.get("is_self") is False and p.get("score", 0) < 10:
                pass  # include anyway
            title = p.get("title", "")
            if filter_keywords:
                if not any(kw.lower() in title.lower() for kw in filter_keywords):
                    continue
            items.append({
                "source": f"r/{subreddit}",
                "title": title,
                "url": "https://reddit.com" + p.get("permalink", ""),
                "summary": (p.get("selftext", "") or p.get("url", ""))[:400],
                "score": p.get("score", 0),
                "comments": p.get("num_comments", 0),
                "published": datetime.fromtimestamp(p.get("created_utc", 0), tz=timezone.utc).strftime("%Y-%m-%d"),
                "type": "reddit",
            })
        return items
    except Exception as e:
        print(f"  [WARN] Reddit parse error for r/{subreddit}: {e}")
        return []


# ── CISA Advisories ───────────────────────────────────────────────────────────
def fetch_cisa(max_items=5):
    url = "https://www.cisa.gov/cybersecurity-advisories/all.xml"
    text = fetch_url(url)
    if not text:
        return []
    return parse_rss(text, "CISA Advisory", max_items)


# ── ACSC (Australian Cyber Security Centre) ───────────────────────────────────
def fetch_acsc(max_items=5):
    """Fetch ACSC advisories. Falls back to web scrape if RSS unavailable."""
    # Try their alert RSS if it exists
    rss_url = "https://www.cyber.gov.au/api/v1/rss/advisories"
    text = fetch_url(rss_url)
    if text and "<item>" in text:
        return parse_rss(text, "ACSC Advisory", max_items)

    # Fallback: scrape the advisories page for links
    page = fetch_url("https://www.cyber.gov.au/about-us/advisories")
    if not page:
        return []
    items = []
    # Extract advisory titles and links with simple regex
    pattern = r'href="(/about-us/advisories/[^"]+)"[^>]*>([^<]{10,200})<'
    matches = re.findall(pattern, page)
    seen = set()
    for path, title in matches[:max_items * 2]:
        title = title.strip()
        if title in seen or len(title) < 10:
            continue
        seen.add(title)
        items.append({
            "source": "ACSC Advisory",
            "title": title,
            "url": "https://www.cyber.gov.au" + path,
            "summary": "",
            "published": datetime.now().strftime("%Y-%m-%d"),
            "type": "government",
        })
        if len(items) >= max_items:
            break
    return items


# ── Australian Feeds (keyword-filtered) ──────────────────────────────────────
def fetch_australian_feeds(config, max_per_source=5):
    """Fetch Australian news/regulatory RSS feeds, filtering by relevance keywords."""
    au_feeds = config["sources"].get("australian_feeds", [])
    all_items = []
    for feed in au_feeds:
        text = fetch_url(feed["url"])
        if not text:
            continue
        items = parse_rss(text, feed["name"], max_items=50)  # fetch more, then filter
        keywords = [kw.lower() for kw in feed.get("keywords", [])]
        if keywords:
            items = [
                i for i in items
                if any(kw in (i["title"] + " " + i.get("summary", "")).lower() for kw in keywords)
            ]
        items = items[:max_per_source]
        for item in items:
            item["type"] = "australian"
        print(f"  {feed['name']}: {len(items)} relevant items")
        all_items.extend(items)
    return all_items


# ── Gmail Google Alerts Reader ────────────────────────────────────────────────
def fetch_gmail_alerts(config, max_items=5):
    """
    Read Google Alert emails from Gmail via IMAP and extract article URLs.
    Requires an App Password: https://myaccount.google.com/apppasswords
    Enable in config.json: sources.gmail_alerts.enabled = true
    """
    gcfg = config["sources"].get("gmail_alerts", {})
    if not gcfg.get("enabled"):
        return []

    app_pw = gcfg.get("app_password", "")
    if not app_pw or app_pw == "YOUR_GMAIL_APP_PASSWORD":
        print("  [SKIP] Gmail alerts: set app_password in config.json and enabled=true")
        return []

    email_addr = gcfg.get("email", "")
    imap_server = gcfg.get("imap_server", "imap.gmail.com")
    imap_port = gcfg.get("imap_port", 993)
    lookback_hours = gcfg.get("lookback_hours", 25)
    target_subjects = gcfg.get("alert_subjects", [])

    items = []
    try:
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)
        mail.login(email_addr, app_pw)
        mail.select("INBOX")

        # Search for recent Google Alert emails
        since_date = (datetime.now() - timedelta(hours=lookback_hours)).strftime("%d-%b-%Y")
        _, msg_ids = mail.search(None, f'(FROM "googlealerts-noreply@google.com" SINCE {since_date})')

        seen_urls = set()
        for mid in msg_ids[0].split():
            _, msg_data = mail.fetch(mid, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])

            # Check subject matches our target alerts
            subject_raw = msg.get("Subject", "")
            subject = decode_header(subject_raw)[0][0]
            if isinstance(subject, bytes):
                subject = subject.decode(errors="replace")

            if target_subjects and not any(ts in subject for ts in target_subjects):
                continue

            # Extract plaintext body
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode("utf-8", errors="replace")
                        break
            else:
                body = msg.get_payload(decode=True).decode("utf-8", errors="replace")

            # Extract article URLs (Google Alert wraps them in google.com/url?...url=<actual>)
            raw_urls = re.findall(r'url=(https?://(?!www\.google\.com)[^\s<>&\)]+)', body)
            # Also catch direct URLs in plaintext alerts
            plain_urls = re.findall(r'<(https?://(?!www\.google\.com)[^>]+)>', body)

            for raw in raw_urls + plain_urls:
                url = urllib.parse.unquote(raw).split("&ct=")[0].split("&cd=")[0]
                if url in seen_urls or "google.com" in url:
                    continue
                seen_urls.add(url)

                # Extract title from the line above the URL in the plaintext
                title_match = re.search(
                    r'([A-Z][^\n]{15,120})\n[^\n]*\n\s*<' + re.escape(raw[:40]), body
                )
                title = title_match.group(1).strip() if title_match else url

                # Infer source from alert subject
                source_tag = re.sub(r"^Google Alert - ", "", subject).strip('\"')

                items.append({
                    "source": f"Google Alert: {source_tag}",
                    "title": title[:120],
                    "url": url,
                    "summary": "",
                    "published": datetime.now().strftime("%Y-%m-%d"),
                    "type": "google_alert",
                })
                if len(items) >= max_items * len(target_subjects):
                    break

        mail.logout()
        print(f"  Gmail alerts: {len(items)} article URLs extracted")
    except Exception as e:
        print(f"  [WARN] Gmail alerts error: {e}")

    return items[:max_items * 3]


# ── Claude AI Summary ─────────────────────────────────────────────────────────
def call_claude(prompt, api_key, model="claude-haiku-4-5-20251001", max_tokens=2000):
    url = "https://api.anthropic.com/v1/messages"
    payload = json.dumps({
        "model": model,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}]
    }).encode("utf-8")
    req = urllib.request.Request(url, data=payload, method="POST")
    req.add_header("x-api-key", api_key)
    req.add_header("anthropic-version", "2023-06-01")
    req.add_header("content-type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read())
            return result["content"][0]["text"]
    except Exception as e:
        print(f"  [WARN] Claude API error: {e}")
        return None


def generate_commentary(item, config):
    """Generate strategic commentary for a single news item."""
    api_key = config.get("claude_api_key", "")
    if not api_key or api_key == "YOUR_ANTHROPIC_API_KEY":
        return "[Commentary requires Claude API key in config.json]"
    style = config["brief"]["commentary_style"]
    prompt = f"""You are writing for {config['brief']['author_name']}'s cybersecurity morning brief.
Tone: {style}

Article: {item['title']}
Source: {item['source']}
Summary: {item.get('summary', '')}

Write 2-3 sentences of sharp strategic commentary. Focus on business implications,
policy impact, or what decision-makers should do. Be specific, not generic.
Do NOT start with "This article" or "This news". Start with the insight."""
    return call_claude(prompt, api_key, max_tokens=200) or "[Commentary unavailable]"


def generate_linkedin_post(items, config):
    """Generate a LinkedIn article from the day's top items."""
    api_key = config.get("claude_api_key", "")
    if not api_key or api_key == "YOUR_ANTHROPIC_API_KEY":
        return "[LinkedIn post generation requires Claude API key in config.json]"
    headlines = "\n".join([f"- {i['title']} ({i['source']})" for i in items[:6]])
    style = config["brief"]["commentary_style"]
    author = config["brief"]["author_name"]
    prompt = f"""You are writing a LinkedIn article for {author}, a cybersecurity thought leader.
Voice/tone: {style}

Today's top cybersecurity stories:
{headlines}

Write a LinkedIn article (500-700 words) that:
1. Opens with a provocative, specific hook (no "In today's fast-paced world")
2. Weaves 3-4 of these stories into a coherent strategic narrative
3. Draws out the bigger-picture implication or trend
4. Ends with a clear, opinionated call-to-action or takeaway
5. Uses short paragraphs suitable for LinkedIn
6. Includes 4-6 relevant hashtags at the end

Write only the article text, no meta-commentary."""
    return call_claude(prompt, api_key, model="claude-sonnet-4-6", max_tokens=1000) or "[LinkedIn post generation failed]"


# ── Format Brief ──────────────────────────────────────────────────────────────
def format_brief(all_items, commentaries, config):
    date_str = datetime.now().strftime("%A, %B %d, %Y")
    lines = [
        f"# 🛡️ Cybersecurity Morning Brief",
        f"**{date_str}**",
        f"",
        f"---",
        f"",
    ]

    # Group by type
    sections = {
        "🚨 Government Advisories": [i for i in all_items if i["type"] == "government"],
        "🇦🇺 Australian News & Regulation": [i for i in all_items if i["type"] == "australian"],
        "📧 Google Alert Articles": [i for i in all_items if i["type"] == "google_alert"],
        "📰 Security News": [i for i in all_items if i["type"] == "news"],
        "🗣️ Community (Reddit)": [i for i in all_items if i["type"] == "reddit"],
    }

    item_index = 1
    index_map = {}  # item_index -> item

    for section_title, items in sections.items():
        if not items:
            continue
        lines.append(f"## {section_title}")
        lines.append("")
        for item in items:
            index_map[item_index] = item
            commentary = commentaries.get(id(item), "")
            lines.append(f"### [{item_index}] {item['title']}")
            lines.append(f"**Source:** {item['source']}  |  **Published:** {item.get('published', 'Unknown')}")
            lines.append(f"**Link:** {item['url']}")
            if item.get("summary"):
                lines.append(f"")
                lines.append(f"> {item['summary'][:300]}...")
            if commentary:
                lines.append(f"")
                lines.append(f"💡 **Strategic take:** {commentary}")
            if item["type"] == "reddit" and item.get("score"):
                lines.append(f"")
                lines.append(f"👍 {item['score']} upvotes  |  💬 {item.get('comments', 0)} comments")
            lines.append("")
            lines.append(f"*Flag for Substack: `python briefing_agent.py --flag {item_index}`*")
            lines.append(f"*Post to LinkedIn: `python briefing_agent.py --post {item_index}`*")
            lines.append("")
            lines.append("---")
            lines.append("")
            item_index += 1

    return "\n".join(lines), index_map


# ── Save / Flag / Post ────────────────────────────────────────────────────────
def save_brief(content, config):
    folder = SCRIPT_DIR / config["output"]["daily_briefs_folder"]
    folder.mkdir(exist_ok=True)
    filename = folder / f"brief_{datetime.now().strftime('%Y-%m-%d')}.md"
    filename.write_text(content, encoding="utf-8")
    print(f"✅ Brief saved: {filename}")
    return filename


def save_linkedin_post(post_text, config, item_title=""):
    folder = SCRIPT_DIR / config["output"]["linkedin_posts_folder"]
    folder.mkdir(exist_ok=True)
    slug = re.sub(r"[^a-z0-9]+", "-", item_title.lower())[:40] if item_title else "digest"
    filename = folder / f"linkedin_{datetime.now().strftime('%Y-%m-%d')}_{slug}.md"
    content = f"# LinkedIn Post Draft\n\n**Date:** {datetime.now().strftime('%Y-%m-%d')}\n**Status:** Draft\n\n---\n\n{post_text}"
    filename.write_text(content, encoding="utf-8")
    print(f"✅ LinkedIn post saved: {filename}")
    return filename


def flag_for_substack(item, commentary, config):
    folder = SCRIPT_DIR / config["output"]["substack_drafts_folder"]
    folder.mkdir(exist_ok=True)
    slug = re.sub(r"[^a-z0-9]+", "-", item["title"].lower())[:50]
    filename = folder / f"{datetime.now().strftime('%Y-%m-%d')}_{slug}.md"
    content = f"""# Substack Draft Seed

**Flagged:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Source:** {item['source']}
**Original title:** {item['title']}
**URL:** {item['url']}

---

## What caught my eye

{item.get('summary', '')}

## Initial take

{commentary or '(Add commentary here)'}

---

## Expand into article

*(Draft your full Substack piece here)*

"""
    filename.write_text(content, encoding="utf-8")
    print(f"✅ Flagged for Substack: {filename}")
    return filename


def markdown_to_html(md_text):
    """Convert basic markdown to HTML suitable for Substack email import."""
    lines = md_text.split("\n")
    html_lines = []
    in_para = False

    for line in lines:
        # Skip metadata lines at top (Status:, Story source:, URL:)
        if re.match(r"\*\*(Status|Story source|URL):\*\*", line):
            continue
        # Skip HTML comment blocks
        if line.strip().startswith("<!--") or line.strip().startswith("-->") or line.strip() == "-->":
            continue
        # Headings
        if line.startswith("# "):
            if in_para: html_lines.append("</p>"); in_para = False
            html_lines.append(f"<h1>{line[2:].strip()}</h1>")
        elif line.startswith("## "):
            if in_para: html_lines.append("</p>"); in_para = False
            html_lines.append(f"<h2>{line[3:].strip()}</h2>")
        elif line.startswith("### "):
            if in_para: html_lines.append("</p>"); in_para = False
            html_lines.append(f"<h3>{line[4:].strip()}</h3>")
        elif line.strip() == "---":
            if in_para: html_lines.append("</p>"); in_para = False
            html_lines.append("<hr>")
        elif line.strip() == "":
            if in_para: html_lines.append("</p>"); in_para = False
        else:
            # Inline formatting
            formatted = line
            formatted = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", formatted)
            formatted = re.sub(r"\*(.+?)\*", r"<em>\1</em>", formatted)
            formatted = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', formatted)
            if not in_para:
                html_lines.append("<p>"); in_para = True
            html_lines.append(formatted)

    if in_para:
        html_lines.append("</p>")

    return "\n".join(html_lines)


def send_to_substack(md_file_path, config):
    """Send a markdown draft to Substack as a draft post via the unofficial API."""
    sub_cfg = config.get("substack", {})
    pub_url = sub_cfg.get("publication_url", "").rstrip("/")
    session_cookie = sub_cfg.get("session_cookie", "")

    if not pub_url or "YOUR_HANDLE" in pub_url:
        print("❌ publication_url not set in config.json → substack.publication_url")
        print("   Example: https://larsk.substack.com")
        return False

    md_path = Path(md_file_path)
    if not md_path.exists():
        print(f"❌ File not found: {md_file_path}")
        return False

    md_text = md_path.read_text(encoding="utf-8")
    title_match = re.search(r"^# (.+)$", md_text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else md_path.stem
    html_body = markdown_to_html(md_text)

    # Use full cookie string if available (preferred — includes substack.lli JWT + cf_clearance)
    # Fall back to session_cookie only for backwards compat
    cookie_string = sub_cfg.get("cookie_string", "")
    if not cookie_string:
        if not session_cookie:
            print("❌ No Substack auth configured.")
            print("   Run: python substack_auth.py")
            return False
        cookie_value = urllib.parse.unquote(session_cookie)
        cookie_string = f"substack.sid={cookie_value}"
        print("  ⚠️  Using session_cookie only — if this 403s, run: python substack_auth.py --full-cookies")

    base_headers = {
        "Cookie": cookie_string,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
        "Referer": f"{pub_url}/publish/post",
        "Origin": pub_url,
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
    }

    # Fetch author ID for draft_bylines (required by Substack API)
    author_id = None
    try:
        me_req = urllib.request.Request(
            "https://substack.com/api/v1/me",
            headers={**base_headers, "Origin": "https://substack.com", "Referer": "https://substack.com/"}
        )
        with urllib.request.urlopen(me_req, timeout=10) as resp:
            me = json.loads(resp.read())
            author_id = me.get("id")
            print(f"  Author ID: {author_id}")
    except Exception as e:
        print(f"  ⚠️  Could not fetch author ID: {e}")

    # POST the draft (no CSRF header needed — Substack uses cookie-based auth only)
    api_url = f"{pub_url}/api/v1/drafts"
    draft_bylines = [{"id": author_id, "is_guest": False}] if author_id else []
    payload = json.dumps({
        "draft_title": title,
        "draft_body": html_body,
        "draft_subtitle": "",
        "draft_bylines": draft_bylines,
        "section_chosen": False,
        "type": "newsletter",
        "audience": "everyone",
    }).encode("utf-8")

    post_headers = {**base_headers, "Content-Type": "application/json"}

    req = urllib.request.Request(api_url, data=payload, method="POST", headers=post_headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read())
            post_id = result.get("id", "")
            draft_url = f"{pub_url}/publish/post/{post_id}" if post_id else f"{pub_url}/publish/drafts"
            print(f"✅ Draft created on Substack: '{title}'")
            print(f"   Edit & publish at: {draft_url}")
            return True
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"❌ Substack API error ({e.code}) on {api_url}")
        print(f"   Response: {body[:500]}")
        if e.code == 401:
            print("   → Cookie expired or wrong. Run: python substack_auth.py")
        elif e.code == 404:
            print("   → Endpoint not found. Check publication_url in config.json is correct.")
            print(f"     Tried: {api_url}")
        elif e.code == 403:
            print("   → Forbidden — CSRF token issue or cookie doesn't match this publication.")
        return False
    except Exception as e:
        print(f"❌ Failed to reach Substack: {e}")
        return False


def post_to_linkedin(post_text, config):
    """Post content to LinkedIn via API. Requires valid access_token in config."""
    access_token = config["linkedin"].get("access_token", "")
    if not access_token:
        print("❌ No LinkedIn access token. Run: python linkedin_auth.py")
        return False

    # Get author URN first
    me_url = "https://api.linkedin.com/v2/me"
    req = urllib.request.Request(me_url)
    req.add_header("Authorization", f"Bearer {access_token}")
    req.add_header("X-Restli-Protocol-Version", "2.0.0")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            me = json.loads(resp.read())
            author_urn = f"urn:li:person:{me['id']}"
    except Exception as e:
        print(f"❌ Could not get LinkedIn profile: {e}")
        return False

    # Create post
    post_url = "https://api.linkedin.com/v2/ugcPosts"
    payload = {
        "author": author_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": post_text},
                "shareMediaCategory": "NONE",
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(post_url, data=data, method="POST")
    req.add_header("Authorization", f"Bearer {access_token}")
    req.add_header("Content-Type", "application/json")
    req.add_header("X-Restli-Protocol-Version", "2.0.0")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read())
            print(f"✅ Posted to LinkedIn: {result.get('id', '')}")
            return True
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"❌ LinkedIn post failed ({e.code}): {body}")
        return False


# ── Main ──────────────────────────────────────────────────────────────────────
def collect_all(config, dry_run=False):
    cfg = config["sources"]
    max_per = config["brief"]["max_items_per_source"]
    all_items = []

    print("\n🔍 Fetching government advisories...")
    cisa = fetch_cisa(max_per)
    print(f"  CISA: {len(cisa)} items")
    acsc = fetch_acsc(max_per)
    print(f"  ACSC: {len(acsc)} items")
    for item in cisa + acsc:
        item["type"] = "government"
    all_items.extend(cisa + acsc)

    print("\n🇦🇺 Fetching Australian feeds...")
    au_items = fetch_australian_feeds(config, max_per)
    all_items.extend(au_items)

    print("\n📧 Reading Gmail Google Alerts...")
    alert_items = fetch_gmail_alerts(config, max_per)
    all_items.extend(alert_items)

    print("\n📰 Fetching RSS news feeds...")
    for feed in cfg["rss_feeds"]:
        text = fetch_url(feed["url"])
        if text:
            items = parse_rss(text, feed["name"], max_per)
            print(f"  {feed['name']}: {len(items)} items")
            all_items.extend(items)

    print("\n🗣️  Fetching Reddit...")
    for sub in cfg["reddit"]:
        items = fetch_reddit(
            sub["subreddit"],
            sub.get("limit", 10),
            sub.get("sort", "hot"),
            sub.get("filter_keywords"),
        )
        print(f"  r/{sub['subreddit']}: {len(items)} items")
        all_items.extend(items)

    return all_items


def run_briefing(config, dry_run=False):
    all_items = collect_all(config, dry_run)
    print(f"\n📊 Total items collected: {len(all_items)}")

    commentaries = {}
    if not dry_run:
        print("\n🤖 Generating strategic commentary...")
        # Limit AI calls: top items only
        priority_items = (
            [i for i in all_items if i["type"] == "government"][:3]
            + [i for i in all_items if i["type"] == "news"][:4]
            + [i for i in all_items if i["type"] == "reddit"][:2]
        )
        for i, item in enumerate(priority_items):
            print(f"  ({i+1}/{len(priority_items)}) {item['title'][:60]}...")
            commentaries[id(item)] = generate_commentary(item, config)

    brief_md, index_map = format_brief(all_items, commentaries, config)
    save_brief(brief_md, config)

    if not dry_run:
        print("\n✍️  Generating LinkedIn post draft...")
        top_news = [i for i in all_items if i["type"] in ("news", "government")][:6]
        linkedin_text = generate_linkedin_post(top_news, config)
        save_linkedin_post(linkedin_text, config)

    # Save index map for --flag / --post commands
    index_file = SCRIPT_DIR / ".last_brief_index.json"
    serializable = {str(k): v for k, v in index_map.items()}
    index_file.write_text(json.dumps(serializable, indent=2))

    print(f"\n✅ Morning brief complete! {len(all_items)} items across {len(set(i['source'] for i in all_items))} sources.")
    return brief_md, index_map


def main():
    parser = argparse.ArgumentParser(description="Cybersecurity Morning Briefing Agent")
    parser.add_argument("--dry-run", action="store_true", help="Collect items but skip AI calls")
    parser.add_argument("--flag", type=int, metavar="N", help="Flag item N for Substack drafts")
    parser.add_argument("--post", type=int, metavar="N", help="Post item N to LinkedIn")
    parser.add_argument("--linkedin-digest", action="store_true", help="Post today's full digest to LinkedIn")
    parser.add_argument("--substack-file", metavar="FILE", help="Send a Substack draft file to your Substack drafts inbox")
    args = parser.parse_args()

    config = load_config()

    if args.substack_file:
        send_to_substack(args.substack_file, config)
        return

    if args.flag or args.post:
        index_file = SCRIPT_DIR / ".last_brief_index.json"
        if not index_file.exists():
            print("❌ No brief index found. Run the briefing first.")
            sys.exit(1)
        index = json.loads(index_file.read_text())
        item = index.get(str(args.flag or args.post))
        if not item:
            print(f"❌ Item #{args.flag or args.post} not found in last brief.")
            sys.exit(1)

        if args.flag:
            commentary = generate_commentary(item, config) if config.get("claude_api_key") != "YOUR_ANTHROPIC_API_KEY" else ""
            flag_for_substack(item, commentary, config)

        if args.post:
            commentary = generate_commentary(item, config) if config.get("claude_api_key") != "YOUR_ANTHROPIC_API_KEY" else item.get("summary", "")
            linkedin_text = f"{item['title']}\n\n{commentary}\n\n🔗 {item['url']}\n\n#CyberSecurity #InfoSec #StrategicRisk"
            save_linkedin_post(linkedin_text, config, item["title"])
            print("\nPost saved. To publish, run: python linkedin_auth.py (if not done) then confirm posting.")

        return

    # Full briefing run
    run_briefing(config, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
