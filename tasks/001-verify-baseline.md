# Task 001: Verify the baseline on Windows and create the first commit

## Goal
Confirm that 2Legit v0.1 installs and passes all of its own checks on this Windows machine (Python 3.14), then record a clean first commit. Do not add features.

## Scope
In:
- Install the project into the existing `.venv`.
- Run the checks listed under Verification.
- Fix only problems that are specific to this machine (Windows paths, line endings, Python 3.14 differences). Make the smallest possible change.
- Add a `.gitattributes` file containing exactly the single line `* text=auto eol=lf` to stop CRLF noise.
- Create the first git commit.

Out:
- Do not change `docs/controls.yaml` or any control's status.
- Do not rewrite or refactor any file that works.
- Do not add dependencies.
- Do not push. Do not add a git remote.

## Steps (run in this order, in the project root)
1. Confirm these four files exist: `.pre-commit-config.yaml`, `.github/dependabot.yml`, `.github/workflows/assurance.yml`, `.github/pull_request_template.md`. If any is missing, STOP and report which one. Do not create it.
2. Run: `.venv\Scripts\python.exe -m pip install -e ".[dev]"`
3. Run the four checks under Verification. Record the exact output.
4. If a check fails, diagnose the cause, apply the smallest fix, and re-run. If the cause is not machine-specific (for example a logic bug in `scripts/`), STOP and report instead of fixing.
5. Create `.gitattributes` as described above.
6. Run: `.venv\Scripts\pre-commit.exe run --all-files`. If hooks modify files, re-run until it passes. If the gitleaks hook cannot download because of network limits, report that and continue.
7. Run `git status` and confirm `.venv/` is not listed as untracked. If it is, STOP and report.
8. Stage everything with `git add -A` and commit with the message: `chore: 2Legit v0.1 baseline`

## Acceptance criteria
- [ ] `pytest` reports 10 passed
- [ ] `ruff check .` reports no problems
- [ ] `python -m scripts.validate_controls` prints "controls.yaml is valid."
- [ ] `python -m scripts.generate_trust --check` prints "TRUST.md is up to date."
- [ ] `git log --oneline` shows exactly one commit
- [ ] `git status` is clean

## Verification
```
.venv\Scripts\python.exe -m pytest -q
.venv\Scripts\python.exe -m ruff check .
.venv\Scripts\python.exe -m scripts.validate_controls
.venv\Scripts\python.exe -m scripts.generate_trust --check
```

## Report back
Paste the output of the four commands, the output of `git log --oneline`, and a list of every file you changed and why.

## AI use
Tool and model: Claude Code CLI
Executor session: this session
Reviewer (must differ from executor): the Claude chat session that wrote this brief
