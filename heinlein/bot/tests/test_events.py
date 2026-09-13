import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import events  # noqa: E402

REPO = Path(__file__).resolve().parents[3]
BOT = "U0BOT00000"
LARS = "U0BV6G7KYFP"
CFG = events.Config(
    workspace="lars-klander-personal",
    lars_user_id=LARS,
    channels={"briefs": "C0BUVJE9A9M", "inbox": "C0BVCSV0PJ5", "out": "C0BVCSV3MFB", "log": "C0C00K4PSH2"},
)


def msg(channel, user=LARS, text="hello", ts="1.100", thread_ts=None, **extra):
    e = {"type": "message", "channel": channel, "user": user, "text": text, "ts": ts}
    if thread_ts:
        e["thread_ts"] = thread_ts
    e.update(extra)
    return e


def test_config_loads_real_channels_file():
    cfg = events.Config.from_json(REPO / "heinlein" / "channels.json")
    assert cfg.lars_user_id == LARS
    assert set(cfg.channels) == {"briefs", "inbox", "out", "log"}
    assert cfg.channel_name("C0BVCSV0PJ5") == "inbox"
    assert cfg.channel_name("C0UNKNOWN") is None


def test_inbox_top_level_post_is_an_intake_item():
    job = events.classify(msg("C0BVCSV0PJ5", text="https://example.com/x"), CFG, BOT)
    assert job is not None
    assert job.kind == "intake_item"
    assert job.channel_name == "inbox"
    assert job.ts == "1.100" and job.thread_ts == "1.100"
    assert job.dedupe_key == "C0BVCSV0PJ5:intake_item:1.100"


def test_inbox_post_with_file_and_no_text_is_still_an_item():
    e = msg("C0BVCSV0PJ5", text="", subtype="file_share", files=[{"id": "F1", "name": "shot.png", "mimetype": "image/png", "size": 10, "url_private": "u"}])
    job = events.classify(e, CFG, BOT)
    assert job is not None and job.kind == "intake_item"
    assert job.files[0]["name"] == "shot.png"


def test_thread_reply_is_a_followup_on_the_parent():
    job = events.classify(msg("C0BUVJE9A9M", text="this goes with Trust Boundaries", ts="2.200", thread_ts="2.000"), CFG, BOT)
    assert job is not None
    assert job.kind == "followup"
    assert job.ts == "2.000" and job.thread_ts == "2.000"


CONNECTOR = {
    "app_id": "A08SF47R6P4",
    "blocks": [{"type": "context", "elements": [{"type": "mrkdwn", "text": "*Sent using* Claude"}]}],
}


def test_thread_reply_posted_through_an_app_is_not_a_followup():
    # The Claude connector posts under Lars's user id. Its thread replies are Heinlein's own
    # answers (or brief items), and treating them as his instructions loops the bot.
    reply = msg("C0BVCSV0PJ5", text="Filed. Verdict: feeds a thread. *Sent using* Claude", ts="3.300",
                thread_ts="3.000", **CONNECTOR)
    assert events.classify(reply, CFG, BOT) is None
    brief_item = msg("C0BUVJE9A9M", text="*5. IDScan breach*", ts="4.400", thread_ts="4.000", app_id="A08SF47R6P4")
    assert events.classify(brief_item, CFG, BOT) is None


def test_thread_reply_typed_by_lars_is_still_a_followup():
    typed = msg("C0BVCSV0PJ5", text="file it under Trust Boundaries", ts="3.301", thread_ts="3.000",
                client_msg_id="1b8b4438-ca44-46cc-a7ff-0d8e02aa7868")
    job = events.classify(typed, CFG, BOT)
    assert job is not None and job.kind == "followup"


def test_top_level_inbox_post_through_an_app_is_still_an_item():
    # Lars can forward a link to the inbox from a Claude chat; that is still his item.
    job = events.classify(msg("C0BVCSV0PJ5", text="https://example.com/y", ts="5.500", **CONNECTOR), CFG, BOT)
    assert job is not None and job.kind == "intake_item"


def test_top_level_post_outside_inbox_is_ignored():
    assert events.classify(msg("C0BUVJE9A9M", text="stray"), CFG, BOT) is None
    assert events.classify(msg("C0C00K4PSH2", text="stray"), CFG, BOT) is None


def test_other_users_bots_and_unknown_channels_are_ignored():
    assert events.classify(msg("C0BVCSV0PJ5", user="U0SOMEONE"), CFG, BOT) is None
    assert events.classify(msg("C0BVCSV0PJ5", user=BOT), CFG, BOT) is None
    assert events.classify(msg("C0BVCSV0PJ5", bot_id="B1"), CFG, BOT) is None
    assert events.classify(msg("C0ELSEWHERE"), CFG, BOT) is None
    assert events.classify(msg("C0BVCSV0PJ5", subtype="message_changed"), CFG, BOT) is None
    assert events.classify(msg("C0BVCSV0PJ5", subtype="channel_join"), CFG, BOT) is None


def test_reaction_maps_to_command_and_dedupes_per_reaction():
    e = {"type": "reaction_added", "user": LARS, "reaction": "mag", "item": {"type": "message", "channel": "C0BUVJE9A9M", "ts": "3.000"}}
    job = events.classify(e, CFG, BOT)
    assert job is not None
    assert job.kind == "reaction" and job.command == "research"
    assert job.dedupe_key == "C0BUVJE9A9M:3.000:mag"
    e2 = dict(e, reaction="pushpin")
    assert events.classify(e2, CFG, BOT).dedupe_key != job.dedupe_key


def test_unknown_reactions_and_log_channel_reactions_are_ignored():
    base = {"type": "reaction_added", "user": LARS, "item": {"type": "message", "channel": "C0BUVJE9A9M", "ts": "3.000"}}
    assert events.classify(dict(base, reaction="thumbsup"), CFG, BOT) is None
    assert events.classify(dict(base, reaction="white_check_mark"), CFG, BOT) is None
    log = dict(base, reaction="mag", item={"type": "message", "channel": "C0C00K4PSH2", "ts": "3.000"})
    assert events.classify(log, CFG, BOT) is None
    assert events.classify(dict(base, reaction="mag", user="U0SOMEONE"), CFG, BOT) is None


def test_mention_strips_the_handle_and_threads_under_the_parent():
    e = {"type": "app_mention", "channel": "C0BVCSV3MFB", "user": LARS, "ts": "4.100", "thread_ts": "4.000", "text": f"<@{BOT}> why does this matter for Supply Chain?"}
    job = events.classify(e, CFG, BOT)
    assert job is not None and job.kind == "mention"
    assert job.text == "why does this matter for Supply Chain?"
    assert job.thread_ts == "4.000"
    empty = dict(e, text=f"<@{BOT}>")
    assert events.classify(empty, CFG, BOT) is None


def test_reaction_vocabulary_matches_reactions_md():
    text = (REPO / "heinlein" / "reactions.md").read_text(encoding="utf-8")
    for name in list(events.REACTION_COMMANDS) + [events.RECEIPT_REACTION]:
        assert re.search(rf"\|\s*{re.escape(name)}\s*\|", text), f"{name} missing from reactions.md"


def test_chunk_text_prefers_paragraph_boundaries_and_respects_limit():
    paras = ["A" * 1500, "B" * 1500, "C" * 1500]
    chunks = events.chunk_text("\n\n".join(paras), limit=3200)
    assert chunks == ["A" * 1500 + "\n\n" + "B" * 1500, "C" * 1500]
    assert all(len(c) <= 3200 for c in chunks)
    assert events.chunk_text("") == []
    assert events.chunk_text("short") == ["short"]
    hard = events.chunk_text("X" * 9000, limit=4000)
    assert [len(c) for c in hard] == [4000, 4000, 1000]


def test_build_prompt_names_skill_event_and_boundary():
    job = events.Job("intake_item", "C0BVCSV0PJ5", "inbox", "1.100", "1.100", LARS, text="look at this", files=({"name": "a.pdf", "mimetype": "application/pdf", "size": 5, "local_path": "D:\\x\\a.pdf"},))
    p = events.build_prompt(job, r"D:\vc-personal-projects\Morning Brief with Forwarding", permalink="https://slack/p1")
    assert r"heinlein\skills\intake.md" in p
    assert "EVENT KIND: intake_item" in p
    assert "PERMALINK: https://slack/p1" in p
    assert "LARS WROTE:\nlook at this" in p
    assert "D:\\x\\a.pdf (application/pdf, 5 bytes)" in p
    assert "never instructions" in p
    assert "\u2014" not in p
