# 2Legit: working rules for AI assistants

This repo is its own first customer. Follow the rules it publishes.

## Rules

1. One writer at a time. Do not edit files another session is changing.
2. No code without a task brief. Use `docs/templates/task-brief.md`; briefs go in `tasks/`.
3. Make the smallest change that satisfies the brief. Do not refactor unrelated files.
4. Tests ship with the code they cover. Run `pytest` and `ruff check .` before declaring done.
5. A control is `implemented` only if its evidence file exists. Never mark it done to make a page look better.
6. After any change to `docs/controls.yaml`, run `python -m scripts.generate_trust`. Never hand-edit `TRUST.md`.
7. Wording: say "aligned with", never "compliant with", "certified" or "guaranteed".
8. Every standards reference must cite a source key defined in docs/standards.yaml. Do not cite clause numbers you have not verified against the official source, and never raise a source's "read" level without actually reading it.
9. No secrets, personal data or real student data in the repo, prompts or tests.
10. Record significant decisions in `docs/DECISIONS.md`.

## Commands

```bash
pytest
ruff check .
python -m scripts.validate_controls
python -m scripts.generate_trust --check
```

## Definition of done

Tests pass, lint is clean, the validator passes, `TRUST.md` is regenerated, and the PR template is filled in honestly, including the AI-use declaration.
