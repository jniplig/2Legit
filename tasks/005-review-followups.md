# Task 005: Follow-ups from the review of task 004

## Goal
Close three gaps found in review: an outdated DORA description in the README, an AI-06 note that does not mention shell-command edits bypassing the hook, and a hook that only works on Windows.

## Prerequisites (STOP if false)
- PR #5 (task 004) is merged to `main`.
- You are on an up-to-date `main` with a clean `git status`.

## Scope
Work on a new branch `task-005-followups`.

In:
1. `README.md`: in the layer table, change the Measurement row from `DORA four key metrics` to `DORA software delivery metrics`. Run `git grep -n -i "four key"` and report any other hits. Do not change hits inside `docs/standards.yaml`.
2. Create `scripts/hook_check.py`, a cross-platform hook launcher:
   - Find the project root as the parent of the `scripts` folder.
   - Choose the interpreter: `.venv/Scripts/python.exe` under the root if it exists, otherwise `.venv/bin/python` if it exists, otherwise `sys.executable`. Put this choice in a function `find_python(root)` that returns a string path.
   - Run `<python> -m ruff check .` and then `<python> -m pytest -q`, both with the working directory set to the root, with output sent to stderr.
   - Exit 0 if both pass. Exit 2 if either fails (stop after the first failure). Exit code 2 is required so Claude Code returns the failure to Claude.
   - Use only the standard library.
3. Update `.claude/settings.json`: keep the same `PostToolUse` entry and matcher `Edit|Write|MultiEdit`, and change the command to exactly: `python "$CLAUDE_PROJECT_DIR/scripts/hook_check.py"`
4. Update `tests/test_hooks.py`: the command test must now assert the command contains `hook_check.py`. Add tests for `find_python`: it prefers the Windows venv path, then the POSIX venv path, then `sys.executable` (use `tmp_path` and create the files).
5. `docs/controls.yaml`, control `AI-06`: add `scripts/hook_check.py` to `evidence` (keep `.claude/settings.json`), and replace the `note` with exactly: `Fires for Claude Code file-edit tools in sessions opened in this project (proved by a live test on 2026-11-01). Edits made through shell commands bypass it, as happened once during task 004 (disclosed in that report). Hand edits rely on pre-commit and CI.`
6. `CLAUDE.md`: add a new rule 11 with exactly: `11. Do not edit project files through shell commands (heredocs, sed, echo redirection) to avoid the post-edit hook. If a change spans several files and the hook fails on intermediate states, stop and ask the human.`
7. `CHANGELOG.md`, under `[Unreleased]`: add `- Cross-platform hook launcher; README DORA wording; AI-06 limits and a rule against shell edits that bypass the hook`
8. Regenerate `TRUST.md` with `python -m scripts.generate_trust`.

Out:
- No other changes. Do not merge. Open a pull request with `gh pr create` and fill in every section of the PR template honestly.

Method note: use the Edit and Write tools for step 2 onward so the hook runs. If the hook fails on an intermediate state, STOP and report instead of switching to shell edits.

## Acceptance criteria
- [ ] `pytest`, `ruff check .`, `python -m scripts.validate_controls` and `python -m scripts.generate_trust --check` pass
- [ ] `python scripts/hook_check.py` exits 0 on a clean tree
- [ ] After temporarily adding the line `import os` to the top of `scripts/__init__.py`, `python scripts/hook_check.py` exits 2 and prints the ruff error; after removing the line, `git diff scripts/__init__.py` is empty
- [ ] The PR is open and CI passes

## Human step (required before merge)
The human opens a NEW Claude Code session in the project folder, runs `/hooks` to confirm the hook is listed, and asks Claude to add `import os` to `scripts/__init__.py` with the Edit or Write tool. The failure must come back to Claude. The human then restores the file with `git restore scripts/__init__.py` and tells the reviewer the result. Do not merge before this.

## Report back
Output of the four standard checks, the exit codes from the two `hook_check.py` runs, `git grep` hits for step 1, the PR URL and CI result, and every file changed.

## AI use
Tool and model: Claude Code CLI
Executor session: this session
Reviewer (must differ from executor): the Claude chat session that wrote this brief
