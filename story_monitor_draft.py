#!/usr/bin/env python3
"""
story_monitor_draft.py  —  Gmail draft helper for the AI Product Story Monitor

Creates a Gmail draft via IMAP APPEND using the app_password in config.json.
This replaces the Cowork Gmail MCP — no OAuth or GWS CLI install required,
just the existing App Password.

Usage (called by the Claude Code slash command after building the briefing):
    python story_monitor_draft.py --subject "AI Product Story Monitor — 2026-08-12" \
                                  --file /path/to/briefing.html

    python story_monitor_draft.py --subject "..." --stdin   # reads HTML from stdin

If you'd rather use gam (GAM / GAMADV-XTD3), swap the send_draft() body for:
    subprocess.run(["gam", "user", EMAIL, "draft", "message",
                    "to", EMAIL, "subject", SUBJECT, "htmlmessage", html], check=True)
"""

import argparse
import email.mime.multipart
import email.mime.text
import imaplib
import json
import sys
import time
from datetime import datetime
from pathlib import Path

# ── Config ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
CONFIG_PATH = SCRIPT_DIR / "config.json"

IMAP_HOST = "imap.gmail.com"
IMAP_PORT = 993
DRAFTS_FOLDER = "[Gmail]/Drafts"


def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)


# ── Draft creation via IMAP APPEND ────────────────────────────────────────────
def send_draft(subject: str, html_body: str, email_addr: str, app_password: str) -> None:
    msg = email.mime.multipart.MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = email_addr
    msg["To"] = email_addr
    msg["Date"] = email.utils.formatdate(localtime=True)
    msg.attach(email.mime.text.MIMEText(html_body, "html", "utf-8"))

    raw = msg.as_bytes()
    timestamp = imaplib.Time2Internaldate(time.time())

    mail = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)
    try:
        mail.login(email_addr, app_password)
        # APPEND places the message directly into Drafts with the \Draft flag
        status, data = mail.append(DRAFTS_FOLDER, r"\Draft", timestamp, raw)
        if status != "OK":
            raise RuntimeError(f"IMAP APPEND failed: {status} {data}")
        print(f"  Draft created in Gmail Drafts folder")
    finally:
        mail.logout()


# ── CLI ────────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Create a Gmail draft from an HTML file or stdin")
    parser.add_argument("--subject", required=True, help="Email subject line")
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument("--file", metavar="PATH", help="Path to HTML file to use as body")
    src.add_argument("--stdin", action="store_true", help="Read HTML body from stdin")
    args = parser.parse_args()

    config = load_config()
    gcfg = config["sources"]["gmail_alerts"]
    email_addr = gcfg["email"]
    app_password = gcfg["app_password"]

    if not app_password or app_password == "YOUR_GMAIL_APP_PASSWORD":
        print("ERROR: set sources.gmail_alerts.app_password in config.json", file=sys.stderr)
        sys.exit(1)

    if args.file:
        html_body = Path(args.file).read_text(encoding="utf-8")
    else:
        html_body = sys.stdin.read()

    print(f"Creating draft: {args.subject!r} → {email_addr}")
    send_draft(args.subject, html_body, email_addr, app_password)
    print("Done.")


if __name__ == "__main__":
    import email.utils  # noqa: needed for formatdate inside send_draft
    main()
