"""On-disk state shared with the polling skill: the same heinlein_state.json, plus a tiny job queue."""
from __future__ import annotations

import json
import threading
import time
from pathlib import Path

_lock = threading.Lock()


class State:
    def __init__(self, path: str | Path):
        self.path = Path(path)

    def _load(self) -> dict:
        if not self.path.exists():
            return {"watermarks": {"inbox": "0", "out": "0"}, "processed": {}, "last_run": ""}
        return json.loads(self.path.read_text(encoding="utf-8"))

    def _save(self, data: dict) -> None:
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        tmp.replace(self.path)

    def is_done(self, key: str) -> bool:
        with _lock:
            return key in self._load().get("processed", {})

    def mark(self, key: str, info: dict) -> None:
        with _lock:
            data = self._load()
            data.setdefault("processed", {})[key] = dict(info, processed_at=time.strftime("%Y-%m-%dT%H:%M:%S%z"))
            data["last_run"] = time.strftime("%Y-%m-%dT%H:%M:%S%z") + " (bot)"
            self._save(data)


class JobQueue:
    """One pending-job file per job so a crash mid-run leaves the job to be retried on restart."""

    def __init__(self, folder: str | Path):
        self.folder = Path(folder)
        self.folder.mkdir(parents=True, exist_ok=True)

    def _file(self, key: str) -> Path:
        safe = "".join(c if c.isalnum() or c in "._-" else "_" for c in key)
        return self.folder / f"{safe}.json"

    def enqueue(self, key: str, payload: dict) -> None:
        self._file(key).write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

    def complete(self, key: str) -> None:
        f = self._file(key)
        if f.exists():
            f.unlink()

    def pending(self) -> list[dict]:
        out = []
        for f in sorted(self.folder.glob("*.json")):
            try:
                out.append(json.loads(f.read_text(encoding="utf-8")))
            except json.JSONDecodeError:
                f.rename(f.with_suffix(".bad"))
        return out
