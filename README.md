# 2Legit

A standards-aligned assurance layer for AI-assisted software projects.

2Legit gives every project the same small set of enforceable controls, scaled by
risk tier, and turns them into a public, evidence-linked trust page. The aim is
to show active measures against low-quality ("slop") AI-generated work, so that
users, customers and investors can check the claims instead of taking them on
trust.

## How it works

1. **Declare a tier** for the project (T0 spike, T1 personal tool, T2 external). See [docs/TIERS.md](docs/TIERS.md).
2. **Controls** live in [docs/controls.yaml](docs/controls.yaml). Each control maps to standards and to an evidence file.
3. **CI enforces them.** A control marked `implemented` fails the build if its evidence file is missing.
4. **[TRUST.md](TRUST.md) is generated** from the matrix. It is never hand-edited, and it never claims planned controls.

Every standards reference is traceable through [docs/standards.yaml](docs/standards.yaml), which records the official source, version, date checked and how much of each source was read.

## Layers and the standards they align with

| Layer | Aligned with |
|---|---|
| Governance | ISO/IEC/IEEE 12207 (software life cycle processes) |
| Engineering controls | DevOps CI/CD practice, NIST SSDF |
| AI controls | NIST AI RMF, ISO/IEC 42001, OWASP Top 10 for LLM Applications |
| Security | NIST SSDF (SP 800-218), OpenSSF Scorecard |
| Operations | ITIL 4 |
| Measurement | DORA four key metrics |

"Aligned with" is not "certified" or "compliant with". See the wording rule in [docs/DECISIONS.md](docs/DECISIONS.md).

## Use it

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -e ".[dev]"
pre-commit install
pytest
python -m scripts.validate_controls
python -m scripts.generate_trust
```

To adopt 2Legit in another project, copy `docs/`, `scripts/`, `tests/`, `.github/` and
`.pre-commit-config.yaml`, then edit `docs/controls.yaml` and `docs/CHARTER.md`.

## Status

v0.1: tiers, control matrix, validator, TRUST.md generator, PR template with AI-use
declaration, and CI. See [CHANGELOG.md](CHANGELOG.md) and the `planned` rows in [TRUST.md](TRUST.md).

## Licence

MIT. See [LICENSE](LICENSE).
