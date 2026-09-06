"""Run one headless Claude Code job in the repo folder and return its result.

The only place the bot talks to Claude. Everything else is Slack plumbing.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
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


def parse_result(stdout: str) -> RunResult:
    stdout = stdout.strip()
    if not stdout:
        return RunResult(False, "Claude returned no output.")
    try:
        data = json.loads(stdout)
    except json.JSONDecodeError:
        last = stdout.splitlines()[-1]
        try:
            data = json.loads(last)
        except json.JSONDecodeError:
            return RunResult(False, "Claude returned non-JSON output.", raw={"stdout": stdout[-2000:]})
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
            args, cwd=str(root), capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=timeout_min * 60, env=env,
        )
    except subprocess.TimeoutExpired:
        return RunResult(False, f"Job exceeded {timeout_min} minutes and was stopped.")
    result = parse_result(proc.stdout)
    result.stderr = (proc.stderr or "")[-2000:]
    if proc.returncode != 0 and result.ok:
        result.ok = False
    return result
