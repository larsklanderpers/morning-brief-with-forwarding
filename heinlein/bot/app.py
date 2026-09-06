"""Heinlein bot: Slack Socket Mode app that turns Heinlein channel events into headless Claude jobs.

Run:  python heinlein/bot/app.py
Env:  heinlein/bot/.env (see .env.example)
"""
from __future__ import annotations

import logging
import os
import queue
import sys
import threading
import time
from dataclasses import asdict
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import events  # noqa: E402
import runner  # noqa: E402
from slack_io import Slack  # noqa: E402
from state import JobQueue, State  # noqa: E402

load_dotenv(HERE / ".env")

ROOT = Path(os.environ.get("HEINLEIN_ROOT") or HERE.parents[1]).resolve()
TIMEOUT_MIN = int(os.environ.get("HEINLEIN_JOB_TIMEOUT_MIN") or 15)
WORKING_REACTION = "hourglass_flowing_sand"
STARTED_AT = time.time()

LOG_DIR = HERE / "logs"
LOG_DIR.mkdir(exist_ok=True)
handler = TimedRotatingFileHandler(LOG_DIR / "heinlein-bot.log", when="midnight", backupCount=14, encoding="utf-8")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                    handlers=[handler, logging.StreamHandler(sys.stdout)])
log = logging.getLogger("heinlein")

for var in ("SLACK_BOT_TOKEN", "SLACK_APP_TOKEN"):
    if not os.environ.get(var):
        log.error("%s missing from heinlein/bot/.env; refusing to start", var)
        sys.exit(2)

cfg = events.Config.from_json(ROOT / "heinlein" / "channels.json")
slack = Slack(os.environ["SLACK_BOT_TOKEN"])
state = State(ROOT / "heinlein" / "state" / "heinlein_state.json")
jobs = JobQueue(HERE / "queue")
mcp_config = str(ROOT / ".mcp.json") if (ROOT / ".mcp.json").exists() else None

app = App(token=os.environ["SLACK_BOT_TOKEN"])
work: "queue.Queue[events.Job]" = queue.Queue()
last_job: dict = {}


def log_line(text: str) -> None:
    if "log" in cfg.channels:
        try:
            slack.post(cfg.channels["log"], text[:3900])
        except Exception as e:  # noqa: BLE001
            log.warning("log post failed: %s", e)


def download_files(job: events.Job) -> events.Job:
    if not job.files:
        return job
    dest_dir = HERE / "downloads" / job.ts.replace(".", "_")
    enriched = []
    for f in job.files:
        d = dict(f)
        if f.get("url_private"):
            try:
                d["local_path"] = str(slack.download(f["url_private"], dest_dir / (f.get("name") or f.get("id"))))
            except Exception as e:  # noqa: BLE001
                d["local_path"] = f"(download failed: {e})"
        enriched.append(d)
    return events.Job(**{**asdict(job), "files": tuple(enriched)})


def handle(job: events.Job) -> None:
    key = job.dedupe_key
    if state.is_done(key):
        log.info("skip %s (already processed)", key)
        jobs.complete(key)
        return
    global last_job
    last_job = {"key": key, "kind": job.kind, "started": time.strftime("%H:%M:%S")}
    slack.react(job.channel_id, job.ts, WORKING_REACTION)
    try:
        job = download_files(job)
        prompt = events.build_prompt(job, str(ROOT), permalink=slack.permalink(job.channel_id, job.ts))
        if job.kind in ("followup", "mention"):
            thread = slack.thread_text(job.channel_id, job.thread_ts)
            prompt += "\n\nTHREAD SO FAR (oldest first):\n" + "\n".join(
                f"[{m['user']}] {m['text']}" for m in thread if m["ts"] != job.ts)
        result = runner.run(prompt, ROOT, timeout_min=TIMEOUT_MIN, mcp_config=mcp_config)
        reply = result.text if result.ok else f"Heinlein could not finish this one: {result.text}"
        for chunk in events.chunk_text(reply):
            slack.post(job.channel_id, chunk, thread_ts=job.thread_ts)
        if result.ok:
            slack.react(job.channel_id, job.ts, events.RECEIPT_REACTION)
        state.mark(key, {"channel": job.channel_name, "kind": job.kind, "reaction": job.reaction,
                         "ok": result.ok, "session_id": result.session_id, "cost_usd": result.cost_usd,
                         "turns": result.turns})
        log_line(f"bot {time.strftime('%H:%M')}: {job.kind} in #heinlein-{job.channel_name}"
                 f"{' :' + job.reaction + ':' if job.reaction else ''} -> {'ok' if result.ok else 'FAILED'}"
                 f" ({result.turns} turns, ${result.cost_usd:.2f}). {reply[:300]}")
        last_job["ok"] = result.ok
    except Exception as e:  # noqa: BLE001
        log.exception("job %s failed", key)
        slack.post(job.channel_id, f"Heinlein hit an error on this item: {e}", thread_ts=job.thread_ts)
        last_job["ok"] = False
    finally:
        slack.unreact(job.channel_id, job.ts, WORKING_REACTION)
        jobs.complete(key)


def worker() -> None:
    while True:
        job = work.get()
        try:
            handle(job)
        finally:
            work.task_done()


def enqueue(job: events.Job) -> None:
    if state.is_done(job.dedupe_key):
        return
    jobs.enqueue(job.dedupe_key, asdict(job))
    work.put(job)
    log.info("queued %s", job.dedupe_key)


@app.event("message")
def on_message(event, ack=None):
    job = events.classify(event, cfg, slack.bot_user_id)
    if job:
        enqueue(job)


@app.event("reaction_added")
def on_reaction(event):
    job = events.classify(event, cfg, slack.bot_user_id)
    if job:
        enqueue(job)


@app.event("app_mention")
def on_mention(event):
    job = events.classify(event, cfg, slack.bot_user_id)
    if job:
        enqueue(job)


@app.event("reaction_removed")
def on_reaction_removed(event):
    return


@app.command("/heinlein")
def on_command(ack, command, respond):
    ack()
    if command.get("user_id") != cfg.lars_user_id:
        respond("Heinlein answers only to Lars.")
        return
    text = (command.get("text") or "").strip()
    if text.startswith("post "):
        path = text[5:].strip().strip('"')
        try:
            import post as post_mod  # noqa: PLC0415
            link = post_mod.post_deliverable(slack, cfg, ROOT, path)
            respond(f"Posted: {link}")
        except Exception as e:  # noqa: BLE001
            respond(f"Post failed: {e}")
        return
    if text == "tick":
        respond("Ticks are events now; drop something in #heinlein-inbox or react on an item.")
        return
    uptime = int(time.time() - STARTED_AT)
    try:
        cli = runner.resolve_cli()
    except FileNotFoundError as e:
        cli = f"MISSING ({e})"
    respond(f"Heinlein up {uptime // 3600}h{(uptime % 3600) // 60}m. Queue depth {work.qsize()}. "
            f"Last job: {last_job or 'none'}. CLI: {cli}. Root: {ROOT}")


def replay_pending() -> None:
    for payload in jobs.pending():
        try:
            payload["files"] = tuple(payload.get("files") or ())
            work.put(events.Job(**payload))
            log.info("replayed pending job %s", payload.get("ts"))
        except TypeError:
            log.warning("could not replay %s", payload)


if __name__ == "__main__":
    threading.Thread(target=worker, daemon=True, name="heinlein-worker").start()
    replay_pending()
    log.info("Heinlein bot starting; root=%s channels=%s", ROOT, cfg.channels)
    log_line(f"bot online {time.strftime('%Y-%m-%d %H:%M')}; root {ROOT}")
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
