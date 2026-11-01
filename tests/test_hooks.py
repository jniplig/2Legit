"""The Claude Code hook (AI-06) runs lint and tests after every AI edit."""
import json

from scripts.validate_controls import ROOT

SETTINGS = ROOT / ".claude" / "settings.json"


def _post_tool_use():
    return json.loads(SETTINGS.read_text(encoding="utf-8"))["hooks"]["PostToolUse"]


def test_settings_is_valid_json():
    json.loads(SETTINGS.read_text(encoding="utf-8"))


def test_post_tool_use_hook_exists():
    assert _post_tool_use()


def test_matcher_covers_edit_and_write():
    matcher = _post_tool_use()[0]["matcher"]
    assert "Edit" in matcher and "Write" in matcher


def test_command_runs_ruff_and_pytest():
    command = _post_tool_use()[0]["hooks"][0]["command"]
    assert "ruff" in command and "pytest" in command
