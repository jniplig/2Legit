# Trust and assurance

> Generated from [`docs/controls.yaml`](docs/controls.yaml). Do not edit by hand.

This page states which engineering controls this project has actually put in
place, and links to the evidence for each one.

How to read it:

- **Implemented** means the evidence file exists in this repository and is
  checked by CI.
- **Planned** means the control is not yet in place and is not claimed.
- **Aligned with** means the control was designed with reference to the named
  standard or framework. It is not a certification, an audit result or a claim
  of compliance.

## Summary

**16 of 22 controls implemented (73%).**

| Tier | Controls expected | Implemented |
|---|---|---|
| T0 | 2 | 2 |
| T1 | 17 | 16 |
| T2 | 22 | 16 |

## Governance

| ID | Control | From tier | Aligned with | Status | Evidence |
|---|---|---|---|---|---|
| GOV-01 | Project charter states purpose, owner, tier and data classification | T1 | ISO/IEC/IEEE 12207 (planning and project assessment processes) | Implemented | [docs/CHARTER.md](docs/CHARTER.md) |
| GOV-02 | Significant decisions are recorded with context and consequences | T1 | ISO/IEC/IEEE 12207 (decision management process) | Implemented | [docs/DECISIONS.md](docs/DECISIONS.md) |
| GOV-03 | Assurance tier is declared and lifecycle gates are defined per tier | T0 | ISO/IEC/IEEE 12207 (life cycle model management) | Implemented | [docs/TIERS.md](docs/TIERS.md) |

## Engineering controls

| ID | Control | From tier | Aligned with | Status | Evidence |
|---|---|---|---|---|---|
| ENG-01 | Default branch is protected; changes merge by pull request only | T1 | NIST SSDF PS.1<br>OpenSSF Scorecard: Branch-Protection | Planned | none yet |
| ENG-02 | CI runs lint, tests, matrix validation and TRUST.md freshness on every PR | T1 | NIST SSDF PO.3<br>DevOps continuous integration practice | Implemented | [.github/workflows/assurance.yml](.github/workflows/assurance.yml) |
| ENG-03 | Pre-commit hooks block common defects before commit | T1 | NIST SSDF PW.7 | Implemented | [.pre-commit-config.yaml](.pre-commit-config.yaml) |
| ENG-04 | Automated tests exist and run in CI | T1 | NIST SSDF PW.8<br>ISO/IEC/IEEE 12207 (verification process) | Implemented | [tests/test_controls.py](tests/test_controls.py) |

## AI controls

| ID | Control | From tier | Aligned with | Status | Evidence |
|---|---|---|---|---|---|
| AI-01 | A written task brief precedes AI-generated code | T1 | NIST AI RMF: GOVERN<br>NIST SSDF PW.1 | Implemented | [docs/templates/task-brief.md](docs/templates/task-brief.md) |
| AI-02 | Every pull request declares whether and how AI was used | T1 | NIST AI RMF: GOVERN<br>ISO/IEC 42001 (AI management system) | Implemented | [.github/pull_request_template.md](.github/pull_request_template.md) |
| AI-03 | AI-generated changes are reviewed by someone other than the generator | T1 | NIST SSDF PW.7<br>NIST AI RMF: MEASURE | Implemented | [.github/pull_request_template.md](.github/pull_request_template.md)<br>[docs/AI_USE_POLICY.md](docs/AI_USE_POLICY.md) |
| AI-04 | A written AI-use policy defines allowed use, review rules and data limits | T1 | ISO/IEC 42001 (AI management system)<br>NIST AI RMF: GOVERN | Implemented | [docs/AI_USE_POLICY.md](docs/AI_USE_POLICY.md) |
| AI-05 | Apps that call LLMs version prompts and keep an eval set with expected outputs | T2 | NIST AI RMF: MEASURE<br>OWASP Top 10 for LLM Applications | Planned | none yet |

## Security

| ID | Control | From tier | Aligned with | Status | Evidence |
|---|---|---|---|---|---|
| SEC-01 | Secret scanning runs before every commit | T0 | NIST SSDF PS.1<br>OpenSSF Scorecard: Vulnerabilities | Implemented | [.pre-commit-config.yaml](.pre-commit-config.yaml) |
| SEC-02 | Dependency updates are automated | T1 | NIST SSDF RV.1<br>OpenSSF Scorecard: Dependency-Update-Tool | Implemented | [.github/dependabot.yml](.github/dependabot.yml) |
| SEC-03 | A security policy tells people how to report vulnerabilities | T1 | NIST SSDF RV.1<br>OpenSSF Scorecard: Security-Policy | Implemented | [SECURITY.md](SECURITY.md) |
| SEC-04 | A software bill of materials is published with each release | T2 | NIST SSDF PS.3 | Planned | none yet |

## Operations

| ID | Control | From tier | Aligned with | Status | Evidence |
|---|---|---|---|---|---|
| OPS-01 | Changes are recorded in a changelog with each release | T1 | ITIL 4: Change enablement<br>ITIL 4: Release management | Implemented | [CHANGELOG.md](CHANGELOG.md) |
| OPS-02 | Incidents and their root causes are logged | T1 | ITIL 4: Incident management<br>ITIL 4: Problem management | Implemented | [docs/INCIDENTS.md](docs/INCIDENTS.md) |
| OPS-03 | A runbook documents deploy, rollback and recovery | T2 | ITIL 4: Service continuity management | Planned | none yet |

## Measurement

| ID | Control | From tier | Aligned with | Status | Evidence |
|---|---|---|---|---|---|
| MEA-01 | Delivery metrics (deploy frequency, lead time, change failure rate, recovery time) are reported | T2 | DORA four key metrics | Planned | none yet |

## Trust

| ID | Control | From tier | Aligned with | Status | Evidence |
|---|---|---|---|---|---|
| TRU-01 | TRUST.md is generated from this matrix and never hand-edited | T1 | Evidence-based assurance practice | Implemented | [TRUST.md](TRUST.md)<br>[scripts/generate_trust.py](scripts/generate_trust.py) |
| TRU-02 | Each release ships an evidence bundle (test results, SBOM, review record, AI-use summary) | T2 | NIST SSDF PS.3 | Planned | none yet |
