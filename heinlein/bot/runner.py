"""Run one headless Claude Code job in the repo folder and return its result.

The only place the bot talks to Claude. Everything else is Slack plumbing.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

ALLOWED_TOOLS = "Read,Write,Edit,Glob,Grep,Bash,WebFetch,WebSearch,mcp__firecrawl__firecrawl_scrape"
DEFAULT_MAX_TURNS = 60


@dataclass
class RunResult:
    ok: bool
    text: str
    session_id: str = ""
    cost_usd: float = 0.0
    turns: int = 0
    raw: dict | None = None
    stderr: str = ""


def resolve_cli(explicit: str | None = None) -> str:
    candidate = explicit or os.environ.get("CLAUDE_CLI") or "claude"
    found = shutil.which(candidate)
    if found:
        return found
    if Path(candidate).exists():
        return str(Path(candidate))
    raise FileNotFoundError(f"Claude Code CLI not found: {candidate}. Install it and run `claude login` once.")


def build_args(cli: str, prompt: str, max_turns: int = DEFAULT_MAX_TURNS, mcp_config: str | None = None,
               resume: str | None = None) -> list[str]:
    args = [cli, "-p", prompt, "--output-format", "json", "--max-turns", str(max_turns),
            "--allowedTools", ALLOWED_TOOLS, "--permission-mode", "acceptEdits"]
    if mcp_config:
        args += ["--mcp-config", mcp_config]
    if resume:
        args += ["--resume", resume]
    return args


def _find_result_object(stdout: str) -> dict | None:
    """The CLI prints one JSON object, but other lines can surround it (warnings, tool chatter).
    Take the whole thing if it parses; otherwise the last line that parses as a result object;
    otherwise any parsable line."""
    try:
        data = json.loads(stdout)
        if isinstance(data, dict):
            return data
    except json.JSONDecodeError:
        pass
    candidates: list[dict] = []
    for line in stdout.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict):
            candidates.append(obj)
    for obj in reversed(candidates):
        if obj.get("type") == "result" or "result" in obj:
            return obj
    return candidates[-1] if candidates else None


def parse_result(stdout: str) -> RunResult:
    stdout = stdout.strip()
    if not stdout:
        return RunResult(False, "Claude returned no output.")
    data = _find_result_object(stdout)
    if data is None:
        return RunResult(False, "Claude returned non-JSON output.", raw={"stdout": stdout[-4000:]})
    text = str(data.get("result") or "").strip()
    ok = not data.get("is_error", False) and bool(text)
    return RunResult(
        ok=ok,
        text=text or "Claude returned an empty result.",
        session_id=str(data.get("session_id") or ""),
        cost_usd=float(data.get("total_cost_usd") or 0.0),
        turns=int(data.get("num_turns") or 0),
        raw=data,
    )


def run(prompt: str, root: str | Path, timeout_min: int = 15, cli: str | None = None,
        max_turns: int = DEFAULT_MAX_TURNS, mcp_config: str | None = None, resume: str | None = None) -> RunResult:
    exe = resolve_cli(cli)
    args = build_args(exe, prompt, max_turns=max_turns, mcp_config=mcp_config, resume=resume)
    env = dict(os.environ)
    env.setdefault("PYTHONIOENCODING", "utf-8")
    try:
        proc = subprocess.run(
            args, cwd=str(root), capture_output=True, stdin=subprocess.DEVNULL, text=True,
            encoding="utf-8", errors="replace", timeout=timeout_min * 60, env=env,
        )
    except subprocess.TimeoutExpired:
        return RunResult(False, f"Job exceeded {timeout_min} minutes and was stopped.")
    result = parse_result(proc.stdout)
    result.stderr = (proc.stderr or "")[-2000:]
    if not result.ok:
        dump_dir = Path(__file__).resolve().parent / "logs"
        dump_dir.mkdir(exist_ok=True)
        stamp = time.strftime("%Y%m%d-%H%M%S")
        (dump_dir / f"job-{stamp}.stdout.txt").write_text(proc.stdout or "", encoding="utf-8")
        (dump_dir / f"job-{stamp}.stderr.txt").write_text(proc.stderr or "", encoding="utf-8")
    if proc.returncode != 0 and result.ok:
        result.ok = False
    return result
