"""Post a deliverable (draft, revision, research note, panel verdict) to #heinlein-out as Heinlein.

CLI:  python heinlein/bot/post.py "Substack Drafts/substack_draft_x_2026-09-08.md" --kind Draft --state "v1, not panelled"
Also used by the /heinlein post slash command.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

LEGEND = "React: ✏️ another pass · 🔍 re-verify a claim (say which in a reply) · ❌ park it · ✅ receipt"
KINDS = ("Draft", "Revision", "Research", "Panel", "Plan")


def guess_kind(path: Path) -> str:
    n = path.name.lower()
    if "research" in n or path.parent.name.lower().startswith("research"):
        return "Research"
    if re.search(r"-rv\d+", n):
        return "Revision"
    if "panel" in n:
        return "Panel"
    if "week-plan" in n:
        return "Plan"
    return "Draft"


def title_of(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def first_paragraph(text: str) -> str:
    body = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)
    for block in re.split(r"\n\s*\n", body):
        b = block.strip()
        if b and not b.startswith("#") and not b.startswith("|") and not b.startswith("**Status"):
            return b[:900]
    return ""


def render_parent(kind: str, title: str, rel_path: str, state_line: str, lead: str) -> str:
    lines = [f"*{kind}: {title}*", rel_path]
    if state_line:
        lines.append(state_line)
    if lead:
        lines.append(lead)
    lines.append(LEGEND)
    return "\n".join(lines)[:3900]


def record(root: Path, ts: str, kind: str, rel_path: str, title: str) -> None:
    out_dir = root / "heinlein" / "state" / "posted"
    out_dir.mkdir(parents=True, exist_ok=True)
    f = out_dir / f"out_{time.strftime('%Y-%m-%d')}.json"
    with f.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({"ts": ts, "kind": kind, "file": rel_path, "title": title}, ensure_ascii=False) + "\n")


def post_deliverable(slack, cfg, root: Path, path: str, kind: str | None = None, state_line: str = "") -> str:
    p = Path(path)
    if not p.is_absolute():
        p = root / p
    if not p.exists():
        raise FileNotFoundError(p)
    rel = str(p.resolve().relative_to(root.resolve())).replace("\\", "/")
    text = p.read_text(encoding="utf-8", errors="replace")
    kind = kind or guess_kind(p)
    title = title_of(text, p.stem)
    parent = render_parent(kind, title, rel, state_line, first_paragraph(text))
    channel = cfg.channels["out"]
    ts = slack.post(channel, parent)
    slack.upload(channel, p, thread_ts=ts, title=p.name, comment="Full text as a file.")
    record(root, ts, kind, rel, title)
    return slack.permalink(channel, ts) or ts


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--kind", choices=KINDS)
    ap.add_argument("--state", default="", help='state line, e.g. "rv3, panel 9.1, pending sign-off"')
    a = ap.parse_args()

    from dotenv import load_dotenv  # noqa: PLC0415
    load_dotenv(HERE / ".env")
    import events  # noqa: PLC0415
    from slack_io import Slack  # noqa: PLC0415

    root = Path(os.environ.get("HEINLEIN_ROOT") or HERE.parents[1]).resolve()
    cfg = events.Config.from_json(root / "heinlein" / "channels.json")
    slack = Slack(os.environ["SLACK_BOT_TOKEN"])
    print(post_deliverable(slack, cfg, root, a.path, a.kind, a.state))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
