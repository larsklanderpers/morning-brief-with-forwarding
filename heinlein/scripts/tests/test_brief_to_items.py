import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import brief_to_items as b2i  # noqa: E402

REPO = Path(__file__).resolve().parents[3]

CYBER = """# 🛡️ Cybersecurity Morning Brief
**Thursday, 3 September 2026**

---

## 🚨 Government Advisories

**CISA Adds Seven Exploited Flaws to KEV**
Source: The Hacker News | [Link](https://thehackernews.com/2026/09/cisa-adds-seven.html)
CISA has added seven newly confirmed exploited vulnerabilities to its catalog.
💡 Strategic take: Seven KEV additions in one advisory signals a busy week.

**ACSC: Active Exploitation of N-able**
Source: Australian Cyber Security Centre | [Link](https://www.cyber.gov.au/alerts)
ACSC has confirmed active exploitation in Australia.
💡 Strategic take: RMM tools are a force multiplier for attackers.

---

## 🗣️ Community Pulse

**Citizen Lab: "Bad Connection"**
Source: r/netsec | [Link](https://www.securityvue.net/news/reddit-r-netsec/)
Citizen Lab research documenting systematic exploitation of telecoms.
Why it matters: Telco infrastructure exploitation has direct implications.

---

## 📌 Today's Signal

Three threads converge today. The common denominator is trust.

---
*To flag an item for Substack, save the article URL and notes to: D:\\x\\Substack Drafts\\*
*To post to LinkedIn, open the LinkedIn Posts\\ folder and copy-paste the draft.*
"""

AI = """# 🤖 AI Morning Brief
**Thursday, 3 September 2026**

---

## 🔬 Frontier Labs

**Claude Fable 5.1 & Mythos 5.1 ship**
Source: Anthropic | https://anthropic.com
Anthropic launched Fable 5.1 and Mythos 5.1 on September 1.
💡 **Strategic take:** The anti-distillation move is the significant story.

## 📬 From the Substacks

43 newsletters scanned. 6 surfaced.

**Product with Attitude (Karo Zieminski) \u2014 "Claude Fable 5.1: What Chinese Coverage Says"**
\u2014 English coverage led with cost; Chinese coverage led with anti-distillation. \u2014 https://karozieminski.substack.com/p/claude-fable
💡 **Strategic take:** The relay economy is a data provenance risk.

## 📡 Social Intelligence

**LinkedIn @Shrikanth Sampath** \u2014 *"AI governance isn't just a compliance exercise."*
*Why it matters: The accountability framing is the question boards are asking.*

### 🎙️ AI Daily Brief \u2014 The Agent Economy
Point one. Point two. Point three.

## 📌 Today's Signal

The week's defining tension is capability versus accountability.

---

## 📝 Outstanding Substack Drafts

| Filename | Title | Age |
|---|---|---|
| `substack_draft_x.md` | X | 0 days |
"""

WORK = """# 🧭 AI Work & the Shape of Work-to-Come
**Thursday, 3 September 2026** · *Community brief \u2014 constructive lens*

---

## 🎥 What Creators Are Saying (YouTube)

**"The Job Positions of the AI Future"** \u2014 The AI Daily Brief / NLW (recent, on Spotify) · https://open.spotify.com/episode/5vgmT6
NLW walks through the full archetype set.
💡 Constructive read: The job title is the wrong level of analysis.

## 🧑‍💻 Practitioner Ground Truth (Reddit)

**r/cscareerquestions** \u2014 "Uber to lay off 10% of workforce" (863 upvotes) · https://techcrunch.com/2026/09/02/uber
Announced Sep 2. Uber combining divisions.
💡 The constructive read is in the org design: Uber is flattening layers.

## 📌 Today's Signal

The dominant story is compression of human layers.
"""


def test_kind_from_filename():
    assert b2i.brief_kind_from_filename("brief_2026-09-03.md") == "cyber"
    assert b2i.brief_kind_from_filename("ai_brief_2026-09-03.md") == "ai"
    assert b2i.brief_kind_from_filename("work_brief_2026-09-03.md") == "work"
    assert b2i.brief_kind_from_filename("random.md") == "unknown"
    assert b2i.date_stamp_from_filename("work_brief_2026-09-03.md") == "2026-09-03"


def test_cyber_parse():
    brief = b2i.parse_brief(CYBER, "brief_2026-09-03.md")
    assert brief.kind == "cyber"
    assert brief.title == "🛡️ Cybersecurity Morning Brief"
    assert brief.date_label == "Thursday, 3 September 2026"
    assert [s.heading for s in brief.sections] == ["🚨 Government Advisories", "🗣️ Community Pulse"]
    assert brief.item_count == 3

    kev = brief.sections[0].items[0]
    assert kev.title == "CISA Adds Seven Exploited Flaws to KEV"
    assert kev.source == "The Hacker News"
    assert kev.url == "https://thehackernews.com/2026/09/cisa-adds-seven.html"
    assert kev.summary == "CISA has added seven newly confirmed exploited vulnerabilities to its catalog."
    assert kev.take == "Seven KEV additions in one advisory signals a busy week."

    pulse = brief.sections[1].items[0]
    assert pulse.source == "r/netsec"
    assert pulse.take == "Telco infrastructure exploitation has direct implications."

    assert brief.signal == "Three threads converge today. The common denominator is trust."
    assert brief.drafts_note == ""


def test_ai_parse_covers_substack_social_and_subheading():
    brief = b2i.parse_brief(AI, "ai_brief_2026-09-03.md")
    headings = [s.heading for s in brief.sections]
    assert headings == ["🔬 Frontier Labs", "📬 From the Substacks", "📡 Social Intelligence"]

    frontier = brief.sections[0].items[0]
    assert frontier.url == "https://anthropic.com"
    assert frontier.take.startswith("The anti-distillation move")

    subs = brief.sections[1]
    assert subs.note == "43 newsletters scanned. 6 surfaced."
    item = subs.items[0]
    assert item.title.startswith("Product with Attitude")
    assert item.url == "https://karozieminski.substack.com/p/claude-fable"
    assert "English coverage led with cost" in item.summary
    assert item.take == "The relay economy is a data provenance risk."

    social = brief.sections[2]
    assert len(social.items) == 2
    assert social.items[0].title == "LinkedIn @Shrikanth Sampath"
    assert social.items[0].summary == '"AI governance isn\'t just a compliance exercise."'
    assert social.items[0].take == "The accountability framing is the question boards are asking."
    assert social.items[1].title == "🎙️ AI Daily Brief \u2014 The Agent Economy"
    assert social.items[1].summary == "Point one. Point two. Point three."

    assert "Outstanding" not in " ".join(headings)
    assert "substack_draft_x.md" in brief.drafts_note


def test_work_parse_meta_line_shapes():
    brief = b2i.parse_brief(WORK, "work_brief_2026-09-03.md")
    yt = brief.sections[0].items[0]
    assert yt.title == '"The Job Positions of the AI Future"'
    assert yt.source == "The AI Daily Brief / NLW (recent, on Spotify)"
    assert yt.url == "https://open.spotify.com/episode/5vgmT6"
    assert yt.take == "The job title is the wrong level of analysis."

    reddit = brief.sections[1].items[0]
    assert reddit.title == "r/cscareerquestions"
    assert reddit.url == "https://techcrunch.com/2026/09/02/uber"
    assert '"Uber to lay off 10% of workforce" (863 upvotes)' in reddit.summary
    assert reddit.take.startswith("in the org design")


def test_render_slack_shapes_and_limits():
    brief = b2i.parse_brief(CYBER, "brief_2026-09-03.md")
    out = b2i.render_slack(brief, legend="📌 file · 🔍 research")
    assert out["kind"] == "cyber"
    assert out["parent"].startswith("*Cyber Brief: Thursday, 3 September 2026*")
    assert "3 items." in out["parent"]
    assert "Today's Signal" in out["parent"]
    assert out["parent"].rstrip().endswith("📌 file · 🔍 research")
    assert [i["index"] for i in out["items"]] == [1, 2, 3]
    first = out["items"][0]["text"]
    assert first.splitlines()[0] == "*1. CISA Adds Seven Exploited Flaws to KEV*"
    assert "<https://thehackernews.com/2026/09/cisa-adds-seven.html|link>" in first
    assert first.splitlines()[-1].startswith("💡 ")
    for i in out["items"]:
        assert len(i["text"]) <= b2i.SLACK_TEXT_LIMIT
    assert len(out["parent"]) <= b2i.SLACK_TEXT_LIMIT


def test_truncation_respects_limit():
    long_item = b2i.Item(title="t", summary="x" * 6000)
    text = b2i.render_item(long_item, 1)
    assert len(text) <= b2i.SLACK_TEXT_LIMIT
    assert text.endswith("…")


def test_json_roundtrip_cli(tmp_path, capsys):
    p = tmp_path / "brief_2026-09-03.md"
    p.write_text(CYBER, encoding="utf-8")
    assert b2i.main(["x", str(p)]) == 0
    data = json.loads(capsys.readouterr().out)
    assert data["item_count"] == 3
    assert data["sections"][0]["items"][0]["source"] == "The Hacker News"


@pytest.mark.parametrize(
    "relpath, min_items",
    [
        ("Daily Briefs/brief_2026-09-03.md", 12),
        ("AI Briefs/ai_brief_2026-09-03.md", 20),
        ("AI Briefs/work_brief_2026-09-03.md", 8),
    ],
)
def test_real_briefs_parse_if_present(relpath, min_items):
    path = REPO / relpath
    if not path.exists():
        pytest.skip(f"{relpath} not on disk")
    brief = b2i.load_brief(path)
    assert brief.item_count >= min_items
    assert brief.signal
    assert all(it.title for s in brief.sections for it in s.items)
    urls = sum(1 for s in brief.sections for it in s.items if it.url)
    assert urls >= min_items // 2
