import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import post  # noqa: E402
import runner  # noqa: E402


def test_build_args_shape():
    args = runner.build_args("claude", "do the thing", max_turns=7, mcp_config="x.json", resume="abc")
    assert args[:3] == ["claude", "-p", "do the thing"]
    assert "--output-format" in args and args[args.index("--output-format") + 1] == "json"
    assert args[args.index("--max-turns") + 1] == "7"
    assert args[args.index("--allowedTools") + 1] == runner.ALLOWED_TOOLS
    assert args[args.index("--permission-mode") + 1] == "acceptEdits"
    assert args[args.index("--mcp-config") + 1] == "x.json"
    assert args[args.index("--resume") + 1] == "abc"
    assert "--cwd" not in args


def test_parse_result_success_and_error_shapes():
    ok = runner.parse_result(json.dumps({"result": "Filed.", "is_error": False, "session_id": "s1", "total_cost_usd": 0.12, "num_turns": 9}))
    assert ok.ok and ok.text == "Filed." and ok.session_id == "s1" and ok.cost_usd == 0.12 and ok.turns == 9

    err = runner.parse_result(json.dumps({"result": "Not logged in · Please run /login", "is_error": True}))
    assert not err.ok and "Not logged in" in err.text

    empty = runner.parse_result("")
    assert not empty.ok

    trailing = runner.parse_result("warning line\n" + json.dumps({"result": "ok", "is_error": False}))
    assert trailing.ok and trailing.text == "ok"

    garbage = runner.parse_result("not json at all")
    assert not garbage.ok and garbage.raw["stdout"] == "not json at all"


def test_resolve_cli_raises_when_missing():
    try:
        runner.resolve_cli("definitely-not-a-real-binary-xyz")
    except FileNotFoundError as e:
        assert "claude login" in str(e)
    else:
        raise AssertionError("expected FileNotFoundError")


def test_post_helpers():
    assert post.guess_kind(Path("Substack Drafts/substack_draft_x_2026-09-08.md")) == "Draft"
    assert post.guess_kind(Path("Substack Drafts/substack_draft_x_2026-09-08-rv3.md")) == "Revision"
    assert post.guess_kind(Path("References/research_x_2026-09-05.md")) == "Research"
    assert post.guess_kind(Path("References/week-plan_2026-09-07.md")) == "Plan"

    text = "---\ntype: draft\n---\n# The Title\n\n**Status:** Draft\n\nFirst real paragraph here.\n\nSecond.\n"
    assert post.title_of(text, "fallback") == "The Title"
    assert post.first_paragraph(text) == "First real paragraph here."

    parent = post.render_parent("Draft", "The Title", "Substack Drafts/x.md", "v1, not panelled", "First real paragraph here.")
    lines = parent.splitlines()
    assert lines[0] == "*Draft: The Title*"
    assert lines[1] == "Substack Drafts/x.md"
    assert lines[2] == "v1, not panelled"
    assert lines[-1].startswith("React:")
    assert len(parent) <= 3900


def test_parse_result_finds_json_among_noise_lines():
    noisy = "Some warning line\n" + json.dumps({"type": "system", "x": 1}) + "\n" + json.dumps({"type": "result", "result": "Filed it.", "is_error": False, "num_turns": 3}) + "\nTrailing noise"
    r = runner.parse_result(noisy)
    assert r.ok and r.text == "Filed it." and r.turns == 3
