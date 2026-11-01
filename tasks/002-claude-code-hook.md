# Task 002: Enforce lint and tests automatically after every AI edit

## Goal
Add a Claude Code hook so that every file edit made by Claude Code in this project automatically runs lint and tests. Failures must be fed back to Claude so it fixes them. Record this as a new control with evidence.

## Prerequisite
Task 001 is committed. Do not start if `git log --oneline` does not show `chore: 2Legit v0.1 baseline`.

## Scope
In:
1. Create `.claude/settings.json` with a `PostToolUse` hook:
   - matcher: `Edit|Write|MultiEdit`
   - hook type: `command`
   - command (exactly): `"$CLAUDE_PROJECT_DIR/.venv/Scripts/python.exe" -m ruff check . >&2 && "$CLAUDE_PROJECT_DIR/.venv/Scripts/python.exe" -m pytest -q >&2 || exit 2`
   - Exit code 2 is required so the failure output is returned to Claude.
2. Create `tests/test_hooks.py` with tests that load `.claude/settings.json` and assert: the file is valid JSON; a `PostToolUse` hook exists; its matcher contains `Edit` and `Write`; its command contains both `ruff` and `pytest`.
3. Add this control to `docs/controls.yaml` in the `ai` section, directly after AI-04:
   - id: AI-06
   - title: Lint and tests run automatically after every AI edit
   - layer: ai
   - min_tier: T1
   - standards: ["NIST SSDF PW.7", "NIST SSDF PW.8"]
   - evidence: [.claude/settings.json]
   - status: implemented
4. Regenerate `TRUST.md` with `python -m scripts.generate_trust`.
5. Under `## [Unreleased]` in `CHANGELOG.md`, add `### Added` and one bullet: `- Claude Code hook that runs lint and tests after every AI edit (control AI-06)`

Out:
- Do not change any other control.
- Do not edit `TRUST.md` by hand.
- Do not add subagents or other hooks.
- Do not push.

## Acceptance criteria
- [ ] `.claude/settings.json` exists and is valid JSON
- [ ] `pytest` passes, including the new tests in `tests/test_hooks.py`
- [ ] `ruff check .` passes
- [ ] `python -m scripts.validate_controls` passes
- [ ] `python -m scripts.generate_trust --check` passes and TRUST.md now lists AI-06 as Implemented
- [ ] The hook command exits 0 when everything is clean
- [ ] The hook command exits 2 when a lint error is present

## Verification
1. Run the hook command from the project root in Git Bash. Confirm exit code 0 (`echo $?`).
2. Temporarily add the line `import os` to the top of `scripts/__init__.py`. Run the hook command again. Confirm exit code 2. Then remove that line and confirm `git diff scripts/__init__.py` is empty.
3. Run the four standard checks from task 001.

## Commit
Work on a branch named `task-002-hook`, not on `main`. Commit with the message: `feat: run lint and tests after every AI edit (AI-06)`. Do not merge. Do not push.

## Report back
Exit codes from verification steps 1 and 2, output of the four standard checks, and every file changed.

## AI use
Tool and model: Claude Code CLI
Executor session: this session
Reviewer (must differ from executor): the Claude chat session that wrote this brief
