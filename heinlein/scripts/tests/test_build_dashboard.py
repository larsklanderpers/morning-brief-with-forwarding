import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import build_dashboard as bd  # noqa: E402

WORK = """# 🧭 AI Work & the Shape of Work-to-Come
**Saturday, 26 September 2026** · *Community brief - constructive lens*

---

## 🎥 What Creators Are Saying (YouTube)

**"How People Are Actually Using Jev"** - The AI Daily Brief / NLW (25 Sep) · https://www.youtube.com/watch?v=uV6h3Uo4Nh8
NLW sorts real usage into six categories.
💡 Constructive read: A referee is only as good as the rulebook.

## 🧑‍💻 Practitioner Ground Truth (Reddit)

⚠️ Lane failed: Chrome refuses reddit.com.

## 📌 Today's Signal

Pick one recurring decision.

---
*To flag an item for Substack: react ⚠️ never appears here but guard anyway.*
"""


def test_slack_link_parent_and_reply():
    assert bd.slack_link("C1", "1790.000100") == "https://lars-klander-personal.slack.com/archives/C1/p1790000100"
    assert bd.slack_link("C1", "1790.2", "1790.1").endswith("/p17902?thread_ts=1790.1&cid=C1")
    assert bd.slack_link("", "1790.2") == ""
    assert bd.slack_link("C1", "") == ""


def test_lane_warnings_skips_footer():
    assert bd.lane_warnings(WORK) == ["⚠️ Lane failed: Chrome refuses reddit.com."]


def test_latest_revisions_keeps_highest_rv():
    names = ["a_2026-09-24.md", "a_2026-09-24-rv2.md", "a_2026-09-24-rv10.md", "b_2026-09-20.md"]
    assert bd.latest_revisions(names) == ["a_2026-09-24-rv10.md", "b_2026-09-20.md"]


def test_missing_brief_entry():
    e = bd.build_brief_entry("cyber", "2026-09-26", None, None)
    assert e["status"] == "missing" and e["items"] == []


def test_entry_joins_posted_state():
    posted = {"channel": "C1", "parent_ts": "10.1", "items": [{"index": 1, "ts": "10.2"}]}
    e = bd.build_brief_entry("work", "2026-09-26", WORK, posted)
    assert e["status"] == "posted"
    assert e["signal"] == "Pick one recurring decision."
    assert len(e["items"]) == 1
    item = e["items"][0]
    assert item["id"] == "2026-09-26-work-1"
    assert item["url"] == "https://www.youtube.com/watch?v=uV6h3Uo4Nh8"
    assert item["slack"].endswith("/p102?thread_ts=10.1&cid=C1")


def test_entry_on_disk_when_not_posted():
    e = bd.build_brief_entry("work", "2026-09-26", WORK, None)
    assert e["status"] == "on_disk" and e["items"][0]["slack"] == ""


def test_public_data_strips_internal_fields():
    posted = {"channel": "C1", "parent_ts": "10.1", "items": [{"index": 1, "ts": "10.2"}]}
    entry = bd.build_brief_entry("work", "2026-09-26", WORK, posted)
    data = {"built": "x", "today": "2026-09-26", "days": [{"date": "2026-09-26", "briefs": [entry]}],
            "drafts": [{"file": "d.md", "title": "D", "modified": "2026-09-26"}]}
    out = bd.public_data(data, "me/brief-desk")
    b = out["days"][0]["briefs"][0]
    assert out["mode"] == "public" and out["issues_repo"] == "me/brief-desk"
    assert out["drafts"] == [] and b["warnings"] == [] and b["slack"] == ""
    assert b["items"][0]["slack"] == "" and b["items"][0]["title"]
    assert entry["slack"] and entry["items"][0]["slack"], "trim must not mutate the private build"


def test_public_needs_valid_repo():
    assert bd.main(["x", "--public"]) == 2
    assert bd.main(["x", "--public", "--repo", "not a repo"]) == 2
