"""Thin Slack wrapper. Every call the bot makes to Slack goes through here."""
from __future__ import annotations

from pathlib import Path

import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

MESSAGE_LIMIT = 4000


class Slack:
    def __init__(self, bot_token: str):
        self.client = WebClient(token=bot_token)
        self._bot_token = bot_token
        self.bot_user_id = self.client.auth_test()["user_id"]

    def post(self, channel: str, text: str, thread_ts: str | None = None) -> str:
        resp = self.client.chat_postMessage(channel=channel, text=text[:MESSAGE_LIMIT], thread_ts=thread_ts)
        return resp["ts"]

    def post_chunks(self, channel: str, chunks: list[str], thread_ts: str) -> list[str]:
        return [self.post(channel, c, thread_ts) for c in chunks]

    def react(self, channel: str, ts: str, name: str) -> None:
        try:
            self.client.reactions_add(channel=channel, timestamp=ts, name=name)
        except SlackApiError as e:
            if e.response.get("error") != "already_reacted":
                raise

    def unreact(self, channel: str, ts: str, name: str) -> None:
        try:
            self.client.reactions_remove(channel=channel, timestamp=ts, name=name)
        except SlackApiError as e:
            if e.response.get("error") != "no_reaction":
                raise

    def permalink(self, channel: str, ts: str) -> str:
        try:
            return self.client.chat_getPermalink(channel=channel, message_ts=ts)["permalink"]
        except SlackApiError:
            return ""

    def upload(self, channel: str, path: str | Path, thread_ts: str | None = None,
               title: str | None = None, comment: str | None = None) -> str:
        p = Path(path)
        resp = self.client.files_upload_v2(
            channel=channel, file=str(p), filename=p.name, title=title or p.name,
            initial_comment=comment, thread_ts=thread_ts,
        )
        f = resp.get("file") or {}
        return f.get("permalink") or f.get("id", "")

    def download(self, url_private: str, dest: str | Path) -> Path:
        dest = Path(dest)
        dest.parent.mkdir(parents=True, exist_ok=True)
        r = requests.get(url_private, headers={"Authorization": f"Bearer {self._bot_token}"}, timeout=120)
        r.raise_for_status()
        dest.write_bytes(r.content)
        return dest

    def thread_text(self, channel: str, ts: str, limit: int = 50) -> list[dict]:
        resp = self.client.conversations_replies(channel=channel, ts=ts, limit=limit)
        return [{"user": m.get("user", ""), "ts": m.get("ts", ""), "text": m.get("text", "")}
                for m in resp.get("messages", [])]
