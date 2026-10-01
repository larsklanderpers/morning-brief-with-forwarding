"""Build the Brief Desk dashboard: one HTML page over the last N days of all three briefs.

Reads the brief files with the same parser the Slack post uses, joins the posted-state maps so
each item links to its Slack thread reply, lists lane failures and open drafts, and injects the
lot as JSON into heinlein/dashboard/template.html.

With --public it writes the trimmed GitHub Pages copy instead: no Slack links, no lane failures,
no open drafts, and "Send to Claude" becomes a pre-filled issue on the --repo given.

Usage:
    python build_dashboard.py [--days 7] [--today YYYY-MM-DD] [--out path]
    python build_dashboard.py --public --repo OWNER/NAME [--out path]
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import asdict
from datetime import date, datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brief_to_items import BRIEF_LABELS, parse_brief  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SLACK_WORKSPACE = "lars-klander-personal"
KINDS = ("cyber", "ai", "work")
DATA_MARKER = "/*__DATA__*/null"
REVISION_RE = re.compile(r"^(?P<base>.+?)(?:-rv(?P<rev>\d+))?\.md$")
WARNING_RE = re.compile("⚠")
# The reactions legend carries no ⚠️, but footers and drafts notes can; those are not lane failures.
WARNING_IGNORE = ("to flag an item", "outstanding substack drafts")


def brief_path(root: Path, kind: str, stamp: str) -> Path:
    if kind == "cyber":
        return root / "Daily Briefs" / f"brief_{stamp}.md"
    prefix = "ai_brief" if kind == "ai" else "work_brief"
    return root / "AI Briefs" / f"{prefix}_{stamp}.md"


def slack_link(channel: str, ts: str, parent_ts: str = "") -> str:
    if not channel or not ts:
        return ""
    link = f"https://{SLACK_WORKSPACE}.slack.com/archives/{channel}/p{ts.replace('.', '')}"
    if parent_ts and parent_ts != ts:
        link += f"?thread_ts={parent_ts}&cid={channel}"
    return link


def lane_warnings(text: str) -> list[str]:
    out = []
    for line in text.splitlines():
        if not WARNING_RE.search(line):
            continue
        clean = re.sub(r"[*_`]", "", line).strip()
        if any(k in clean.lower() for k in WARNING_IGNORE):
            continue
        out.append(clean[:280])
    return out


def latest_revisions(names: list[str]) -> list[str]:
    """Keep the highest -rvN of each draft; a bare name counts as revision 0."""
    best: dict[str, tuple[int, str]] = {}
    for name in names:
        m = REVISION_RE.match(name)
        if not m:
            continue
        rev = int(m.group("rev") or 0)
        base = m.group("base")
        if base not in best or rev > best[base][0]:
            best[base] = (rev, name)
    return sorted(n for _, n in best.values())


def build_brief_entry(kind: str, stamp: str, text: str | None, posted: dict | None) -> dict:
    entry = {"kind": kind, "label": BRIEF_LABELS[kind], "date": stamp, "status": "missing",
             "signal": "", "warnings": [], "items": [], "slack": ""}
    if text is None:
        return entry
    brief = parse_brief(text, f"x_{stamp}.md")
    posted = posted or {}
    channel = posted.get("channel", "")
    parent_ts = posted.get("parent_ts", "")
    ts_by_index = {p.get("index"): p.get("ts", "") for p in posted.get("items", [])}
    entry.update(status="posted" if parent_ts else "on_disk", signal=brief.signal,
                 warnings=lane_warnings(text), slack=slack_link(channel, parent_ts))
    n = 0
    for section in brief.sections:
        for item in section.items:
            n += 1
            d = asdict(item)
            d.update(id=f"{stamp}-{kind}-{n}", index=n, kind=kind, date=stamp,
                     slack=slack_link(channel, ts_by_index.get(n, ""), parent_ts))
            entry["items"].append(d)
    return entry


def read_drafts(root: Path, today: date, days: int = 7) -> list[dict]:
    folder = root / "Substack Drafts"
    cutoff = datetime.combine(today - timedelta(days=days), datetime.min.time()).timestamp()
    candidates = {}
    for p in folder.glob("*.md"):
        if p.stat().st_mtime < cutoff:
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        if "Status: Draft" not in text:
            continue
        h1 = next((ln[2:].strip() for ln in text.splitlines() if ln.startswith("# ")), p.stem)
        candidates[p.name] = {"file": p.name, "title": h1,
                              "modified": datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d")}
    return [candidates[n] for n in latest_revisions(list(candidates))]


def build_data(root: Path, today: date, days: int) -> dict:
    stamps = [(today - timedelta(days=i)).isoformat() for i in range(days)]
    out_days = []
    for stamp in stamps:
        briefs = []
        for kind in KINDS:
            path = brief_path(root, kind, stamp)
            text = path.read_text(encoding="utf-8") if path.exists() else None
            posted_path = root / "heinlein" / "state" / "posted" / f"{stamp}_{kind}.json"
            posted = json.loads(posted_path.read_text(encoding="utf-8")) if posted_path.exists() else None
            briefs.append(build_brief_entry(kind, stamp, text, posted))
        out_days.append({"date": stamp, "briefs": briefs})
    return {"built": datetime.now().strftime("%Y-%m-%d %H:%M"), "today": today.isoformat(),
            "days": out_days, "drafts": read_drafts(root, today)}


def public_data(data: dict, repo: str) -> dict:
    """Trim a build for a public page: anyone with the URL can read it, so nothing internal stays."""
    days = []
    for day in data["days"]:
        briefs = []
        for b in day["briefs"]:
            items = [{**i, "slack": ""} for i in b["items"]]
            briefs.append({**b, "slack": "", "warnings": [], "items": items})
        days.append({**day, "briefs": briefs})
    return {**data, "days": days, "drafts": [], "mode": "public", "issues_repo": repo}


def arg(argv: list[str], flag: str, default: str | None = None) -> str | None:
    return argv[argv.index(flag) + 1] if flag in argv else default


def main(argv: list[str]) -> int:
    days = int(arg(argv, "--days", "7"))
    today = date.fromisoformat(arg(argv, "--today", date.today().isoformat()))
    public = "--public" in argv
    repo = arg(argv, "--repo")
    if public and not (repo and re.fullmatch(r"[\w.-]+/[\w.-]+", repo)):
        print("--public needs --repo OWNER/NAME", file=sys.stderr)
        return 2
    default_out = ROOT / "heinlein" / "dashboard" / ("public/index.html" if public else "brief-desk.html")
    out = Path(arg(argv, "--out", str(default_out)))
    out.parent.mkdir(parents=True, exist_ok=True)
    template = (ROOT / "heinlein" / "dashboard" / "template.html").read_text(encoding="utf-8")
    built = build_data(ROOT, today, days)
    if public:
        built = public_data(built, repo)
    data = json.dumps(built, ensure_ascii=False).replace("</", "<\\/")
    out.write_text(template.replace(DATA_MARKER, data), encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
