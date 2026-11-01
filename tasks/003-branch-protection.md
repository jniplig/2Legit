# Task 003: Protect main and record the evidence (control ENG-01)

## Goal
Make `main` on GitHub accept changes only through pull requests with passing CI, and store proof of that setting in the repo so control ENG-01 can be marked implemented.

## Prerequisites (the human does these first; STOP if any is false)
- The repository `jniplig/2Legit` exists on GitHub and is public.
- The human has pushed `main` to it.
- Task 002 has been reviewed and merged, or the human has said to skip it.
- The CI workflow `assurance` has run at least once on `main`.
- `gh auth status` shows the human is logged in.

## Scope
In:
1. Apply branch protection to `main` by running exactly this command:

```
gh api --method PUT repos/jniplig/2Legit/branches/main/protection --input - <<'EOF'
{
  "required_status_checks": { "strict": true, "contexts": ["checks"] },
  "enforce_admins": true,
  "required_pull_request_reviews": { "required_approving_review_count": 0 },
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false
}
EOF
```

2. On a new branch `task-003-protection`, export the setting to evidence: `gh api repos/jniplig/2Legit/branches/main/protection > docs/evidence/branch-protection.json`
3. In `docs/controls.yaml`, change control ENG-01: set `evidence: [docs/evidence/branch-protection.json]` and `status: implemented`. Change nothing else.
4. Regenerate `TRUST.md` with `python -m scripts.generate_trust`.
5. Add one line under `### Added` in `[Unreleased]` in `CHANGELOG.md`: `- Branch protection on main, with exported evidence (control ENG-01)`
6. Open a pull request into `main` with `gh pr create`, filling in every section of the PR template honestly, including the AI-use declaration.

Out:
- Do not merge the pull request.
- Do not change any other control or file.

## Acceptance criteria
- [ ] `gh api repos/jniplig/2Legit/branches/main/protection` shows required status check `checks` and `allow_force_pushes.enabled` false
- [ ] `docs/evidence/branch-protection.json` exists and is valid JSON
- [ ] `pytest`, `ruff check .`, `validate_controls` and `generate_trust --check` all pass
- [ ] The pull request is open and CI is running on it

## Report back
The protection API response, the PR URL, and the CI result.

## AI use
Tool and model: Claude Code CLI
Executor session: this session
Reviewer (must differ from executor): the Claude chat session that wrote this brief, plus the human as merger
