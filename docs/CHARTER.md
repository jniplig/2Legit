# Project charter

| Field | Value |
|---|---|
| Project | 2Legit |
| Owner | Jeremy Gilpin |
| Purpose | A reusable assurance layer that shows, with evidence, how AI-assisted projects avoid low-quality output |
| Tier | T1 (personal tool, public repo) |
| Data classification | No personal data. Public repository. |
| Stack | Python 3.10+, PyYAML, pytest, ruff, GitHub Actions |
| Users | The owner first, then other small teams who adopt the kit |

## Scope (v0.1)

In: tier definitions, control matrix, validator, TRUST.md generator, PR template with AI-use declaration, CI.

Out (planned): release evidence bundle, SBOM, DORA metrics, runbook template, LLM prompt and eval tooling, Claude Code hooks.

## Success criteria

- Every `implemented` control has a checked evidence file.
- A new project can adopt the kit by copying files and editing two documents.
- No page produced by the kit claims certification or compliance.
