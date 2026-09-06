"""Parse a morning-brief markdown file into items, and render those items as Slack messages.

Deterministic on purpose: the scheduled skills call this instead of eyeballing the markdown,
so what lands in Slack is the same shape every day regardless of how the brief was worded.

Usage:
    python brief_to_items.py <brief.md>            JSON to stdout
    python brief_to_items.py <brief.md> --slack    parent message + one line per item message, JSON
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

SLACK_TEXT_LIMIT = 5000
SUMMARY_LIMIT = 700
TAKE_LIMIT = 500

SKIP_SECTIONS = ("outstanding substack drafts",)
SIGNAL_SECTION = "today's signal"

BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
MD_LINK_RE = re.compile(r"\[([^\]]*)\]\((https?://[^)\s]+)\)")
BARE_URL_RE = re.compile(r"https?://[^\s<>()\[\]]+")
SOURCE_LINE_RE = re.compile(r"^\**Source:\**\s*(.+?)\s*(?:\|.*)?$")
BULLET_ITEM_RE = re.compile(r"^\s*[-*]\s+\*\*")
TAKE_PREFIX_RE = re.compile(
    r"^\s*(?:💡\s*)?\*{0,2}\s*(?:Strategic take|Constructive read|The constructive read is|Why it matters)\s*:?\s*\*{0,2}\s*:?\s*",
    re.IGNORECASE,
)
DATE_STAMP_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")

BRIEF_KIND_BY_PREFIX = {
    "work_brief": "work",
    "ai_brief": "ai",
    "brief": "cyber",
}

BRIEF_LABELS = {
    "cyber": "Cyber Brief",
    "ai": "AI Brief",
    "work": "AI Work Brief",
}


@dataclass
class Item:
    title: str
    source: str = ""
    url: str = ""
    summary: str = ""
    take: str = ""
    section: str = ""


@dataclass
class Section:
    heading: str
    note: str = ""
    items: list[Item] = field(default_factory=list)


@dataclass
class Brief:
    kind: str
    title: str
    date_label: str
    date_stamp: str
    sections: list[Section] = field(default_factory=list)
    signal: str = ""
    drafts_note: str = ""

    @property
    def item_count(self) -> int:
        return sum(len(s.items) for s in self.sections)


def brief_kind_from_filename(name: str) -> str:
    stem = Path(name).stem
    for prefix, kind in BRIEF_KIND_BY_PREFIX.items():
        if stem.startswith(prefix + "_"):
            return kind
    return "unknown"


def date_stamp_from_filename(name: str) -> str:
    m = DATE_STAMP_RE.search(Path(name).stem)
    return m.group(1) if m else ""


def _clean(text: str) -> str:
    text = text.replace("**", "")
    text = re.sub(r"(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def _strip_urls(text: str) -> str:
    text = MD_LINK_RE.sub("", text)
    text = BARE_URL_RE.sub("", text)
    text = re.sub(r"\s*[·|\u2014-]\s*$", "", text.strip())
    return text.strip()


def _first_url(text: str) -> str:
    m = MD_LINK_RE.search(text)
    if m:
        return m.group(2)
    m = BARE_URL_RE.search(text)
    if not m:
        return ""
    return m.group(0).rstrip(".,;:")


def _source_from_meta(meta: str) -> str:
    meta = _strip_urls(meta)
    meta = meta.strip(" \u2014-·:")
    if not meta:
        return ""
    head = re.split(r"\s+[·|]\s+", meta, maxsplit=1)[0]
    return _clean(head)[:120]


def parse_item(block: list[str], section_heading: str) -> Item:
    first = block[0]
    bold = BOLD_RE.search(first)
    title = _clean(bold.group(1)) if bold else _clean(_strip_urls(first))
    remainder = first[bold.end():] if bold else ""

    source = ""
    url = _first_url(first)
    summary_lines: list[str] = []
    take_lines: list[str] = []

    meta_text = remainder.strip()
    if meta_text and not url:
        url = _first_url(meta_text)
    if meta_text:
        stripped_meta = _clean(_strip_urls(meta_text)).strip(" \u2014-·")
        looks_like_meta = bool(url) or "·" in stripped_meta or len(block) > 1
        if stripped_meta and looks_like_meta and not stripped_meta.startswith('"') and len(stripped_meta) <= 80:
            source = _source_from_meta(stripped_meta)
        elif stripped_meta:
            summary_lines.append(stripped_meta.strip(" \u2014-·"))

    for line in block[1:]:
        stripped = line.strip()
        if not stripped:
            continue
        src = SOURCE_LINE_RE.match(stripped)
        if src:
            link = MD_LINK_RE.search(src.group(1))
            source = _clean(link.group(1)) if link else _clean(_strip_urls(src.group(1)))
            if not url:
                url = _first_url(stripped)
            continue
        if TAKE_PREFIX_RE.match(stripped) and (
            stripped.startswith("💡") or stripped.lower().lstrip("*").startswith("why it matters")
        ):
            take_lines.append(_clean(TAKE_PREFIX_RE.sub("", stripped, count=1)).strip("* "))
            continue
        if not url:
            url = _first_url(stripped)
        summary_lines.append(_clean(_strip_urls(stripped)).strip(" \u2014-·"))

    summary = " ".join(s for s in summary_lines if s)
    take = " ".join(t for t in take_lines if t)
    return Item(
        title=title,
        source=source,
        url=url,
        summary=summary[:SUMMARY_LIMIT].rstrip(),
        take=take[:TAKE_LIMIT].rstrip(),
        section=_clean(section_heading),
    )


def _blocks(lines: list[str]) -> list[list[str]]:
    blocks: list[list[str]] = []
    current: list[str] = []
    for line in lines:
        if line.strip() == "" or line.strip() == "---":
            if current:
                blocks.append(current)
                current = []
            continue
        current.append(line.rstrip())
    if current:
        blocks.append(current)
    return blocks


def _group_item_blocks(blocks: list[list[str]]) -> list[list[str]]:
    """Normalise the three item shapes the briefs have used into bold-title blocks.

    - `**Title**` block: as is.
    - `### Title` heading: absorbs every following plain block until the next item starts,
      because that style puts blank lines between source, body and take.
    - Bullet list of `- **Title** ...` lines: one item per line.
    """
    out: list[list[str]] = []
    open_heading: list[str] | None = None
    for b in blocks:
        first = b[0]
        if first.startswith("### "):
            if open_heading:
                out.append(open_heading)
            open_heading = ["**" + _clean(first[4:]) + "**"] + b[1:]
            continue
        if all(BULLET_ITEM_RE.match(l) for l in b):
            if open_heading:
                out.append(open_heading)
                open_heading = None
            for l in b:
                out.append([re.sub(r"^\s*[-*]\s+", "", l)])
            continue
        if first.lstrip().startswith("**") and not SOURCE_LINE_RE.match(first.strip()):
            if open_heading:
                out.append(open_heading)
                open_heading = None
            out.append(b)
            continue
        if open_heading is not None:
            open_heading.extend(b)
        else:
            out.append(b)
    if open_heading:
        out.append(open_heading)
    return out


def _is_footer(block: list[str]) -> bool:
    return all(l.strip().startswith("*") and not l.strip().startswith("**") for l in block)


def parse_brief(text: str, filename: str = "") -> Brief:
    lines = text.splitlines()
    title = ""
    date_label = ""
    for line in lines[:6]:
        if line.startswith("# ") and not title:
            title = _clean(line[2:])
        elif line.startswith("**") and not date_label:
            date_label = _clean(BOLD_RE.search(line).group(1)) if BOLD_RE.search(line) else _clean(line)

    brief = Brief(
        kind=brief_kind_from_filename(filename),
        title=title,
        date_label=date_label,
        date_stamp=date_stamp_from_filename(filename),
    )

    section: Section | None = None
    body: list[str] = []

    def flush() -> None:
        nonlocal section, body
        if section is None:
            body = []
            return
        heading_l = _clean(section.heading).lower()
        blocks = [b for b in _blocks(body) if not _is_footer(b)]
        if SIGNAL_SECTION in heading_l:
            brief.signal = " ".join(_clean(" ".join(b)) for b in blocks)
        elif any(s in heading_l for s in SKIP_SECTIONS):
            brief.drafts_note = "\n".join(l for b in blocks for l in b)
        else:
            for b in _group_item_blocks(blocks):
                if b[0].lstrip().startswith("**"):
                    section.items.append(parse_item(b, section.heading))
                elif section.items:
                    section.items[-1].summary = (section.items[-1].summary + " " + _clean(" ".join(b)))[:SUMMARY_LIMIT]
                else:
                    section.note = (section.note + " " + _clean(" ".join(b))).strip()
            brief.sections.append(section)
        section = None
        body = []

    for line in lines:
        if line.startswith("## "):
            flush()
            section = Section(heading=_clean(line[3:]))
            continue
        if section is not None:
            body.append(line)
    flush()
    return brief


def _truncate(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def render_parent(brief: Brief, legend: str = "") -> str:
    label = BRIEF_LABELS.get(brief.kind, brief.title or "Brief")
    lines = [f"*{label}: {brief.date_label or brief.date_stamp}*"]
    counts = ", ".join(f"{s.heading} {len(s.items)}" for s in brief.sections if s.items)
    lines.append(f"{brief.item_count} items. {counts}")
    if brief.signal:
        lines.append("")
        lines.append("*Today's Signal.* " + brief.signal)
    if legend:
        lines.append("")
        lines.append(legend)
    return _truncate("\n".join(lines), SLACK_TEXT_LIMIT)


def render_item(item: Item, index: int) -> str:
    head = f"*{index}. {item.title}*"
    meta_parts = [p for p in (item.section, item.source) if p]
    meta = " · ".join(meta_parts)
    if item.url:
        meta = f"{meta} · <{item.url}|link>" if meta else f"<{item.url}|link>"
    lines = [head]
    if meta:
        lines.append(meta)
    if item.summary:
        lines.append(item.summary)
    if item.take:
        lines.append("💡 " + item.take)
    return _truncate("\n".join(lines), SLACK_TEXT_LIMIT)


def render_slack(brief: Brief, legend: str = "") -> dict:
    items = []
    n = 0
    for s in brief.sections:
        for it in s.items:
            n += 1
            items.append({"index": n, "title": it.title, "section": s.heading, "url": it.url, "text": render_item(it, n)})
    return {"kind": brief.kind, "date_stamp": brief.date_stamp, "parent": render_parent(brief, legend), "items": items}


def load_legend(path: str | Path) -> str:
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.strip():
            return line.strip()
    return ""


def load_brief(path: str | Path) -> Brief:
    p = Path(path)
    return parse_brief(p.read_text(encoding="utf-8"), p.name)


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    brief = load_brief(argv[1])
    legend = ""
    if "--legend" in argv:
        legend = load_legend(argv[argv.index("--legend") + 1])
    if "--slack" in argv:
        out = render_slack(brief, legend)
    else:
        out = asdict(brief)
        out["item_count"] = brief.item_count
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
