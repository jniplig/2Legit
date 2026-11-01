# Trust and assurance

> Generated from [`docs/controls.yaml`](docs/controls.yaml). Do not edit by hand.

This page states which engineering controls this project has actually put in
place, and links to the evidence for each one. Every reference below links to
the official source and states how much of that source was read.

How to read it:

- **Implemented** means the evidence file exists in this repository and is
  checked by CI.
- **Planned** means the control is not yet in place and is not claimed.
- **Aligned with** means the control was designed with reference to the named
  standard or framework. It is not a certification, an audit result or a claim
  of compliance.

## Summary

**19 of 25 controls implemented (76%).**

| Tier | Controls expected | Implemented |
|---|---|---|
| T0 | 2 | 2 |
| T1 | 20 | 19 |
| T2 | 25 | 19 |

## Governance

| ID | Control | From tier | Applied at phase | Enforced by | Aligned with | Limits | Status | Evidence |
|---|---|---|---|---|---|---|---|---|
| GOV-01 | Project charter states purpose, owner, tier and data classification | T1 | 1 | Process | [ISO/IEC/IEEE 12207:2017 6.3.1 Project Planning process](https://www.iso.org/standard/63712.html)<br>[NIST AI 100-1 MAP 1.1 (intended purposes and context documented)](https://www.nist.gov/itl/ai-risk-management-framework) | none recorded | Implemented | [docs/CHARTER.md](docs/CHARTER.md) |
| GOV-02 | Significant decisions are recorded with context and consequences | T1 | 2, 5 | Process | [ISO/IEC/IEEE 12207:2017 6.3.3 Decision Management process](https://www.iso.org/standard/63712.html) | none recorded | Implemented | [docs/DECISIONS.md](docs/DECISIONS.md) |
| GOV-03 | Assurance tier is declared and lifecycle gates are defined per tier | T0 | 1, 2, 3 | Process | [ISO/IEC/IEEE 12207:2017 6.2.1 Life cycle model management process](https://www.iso.org/standard/63712.html) | none recorded | Implemented | [docs/TIERS.md](docs/TIERS.md) |
| GOV-04 | Every cited standard is listed in a register with source, version, date checked and how much was read | T1 | 2, 10 | Automated | Project-specific (no external standard) | CI rejects references to sources missing from the register. It cannot check that the reference itself is apt; that is a human judgement. | Implemented | [docs/standards.yaml](docs/standards.yaml) |

## Engineering controls

| ID | Control | From tier | Applied at phase | Enforced by | Aligned with | Limits | Status | Evidence |
|---|---|---|---|---|---|---|---|---|
| ENG-01 | Default branch is protected; changes merge by pull request only | T1 | 3, 7 | Automated | [NIST SP 800-218 PS.1 Protect All Forms of Code from Unauthorized Access and Tampering](https://csrc.nist.gov/pubs/sp/800/218/final)<br>[OpenSSF Scorecard Branch-Protection](https://github.com/ossf/scorecard/blob/main/docs/checks.md) | none recorded | Implemented | [docs/evidence/branch-protection.json](docs/evidence/branch-protection.json) |
| ENG-02 | CI runs lint, tests, matrix validation and TRUST.md freshness on every PR | T1 | 3, 6, 7 | Automated | [NIST SP 800-218 PO.3 Implement Supporting Toolchains](https://csrc.nist.gov/pubs/sp/800/218/final)<br>[OpenSSF Scorecard CI-Tests](https://github.com/ossf/scorecard/blob/main/docs/checks.md) | none recorded | Implemented | [.github/workflows/assurance.yml](.github/workflows/assurance.yml) |
| ENG-03 | Pre-commit hooks block common defects before commit | T1 | 5 | Automated | [NIST SP 800-218 PW.7 Review and/or Analyze Human-Readable Code](https://csrc.nist.gov/pubs/sp/800/218/final) | Runs on the developer's machine and can be bypassed with --no-verify. CI re-runs lint only. | Implemented | [.pre-commit-config.yaml](.pre-commit-config.yaml) |
| ENG-04 | Automated tests exist and run in CI | T1 | 6 | Automated | [NIST SP 800-218 PW.8 Test Executable Code](https://csrc.nist.gov/pubs/sp/800/218/final)<br>[ISO/IEC/IEEE 12207:2017 6.4.9 Verification process](https://www.iso.org/standard/63712.html)<br>[OpenSSF Scorecard CI-Tests](https://github.com/ossf/scorecard/blob/main/docs/checks.md) | none recorded | Implemented | [tests/test_controls.py](tests/test_controls.py) |

## AI controls

| ID | Control | From tier | Applied at phase | Enforced by | Aligned with | Limits | Status | Evidence |
|---|---|---|---|---|---|---|---|---|
| AI-01 | A written task brief precedes AI-generated code | T1 | 5 | Process | [ISO/IEC/IEEE 12207:2017 6.4.3 System/Software requirements definition process](https://www.iso.org/standard/63712.html) | Nothing technical stops code being written without a brief. | Implemented | [docs/templates/task-brief.md](docs/templates/task-brief.md) |
| AI-02 | Every pull request declares whether and how AI was used | T1 | 7 | Process | [NIST AI 100-1 GOVERN 2.1 (roles and responsibilities documented)](https://www.nist.gov/itl/ai-risk-management-framework)<br>[ISO/IEC 42001:2023 General alignment only (clauses not reviewed)](https://www.iso.org/standard/81230.html) | The template prompts for a declaration; GitHub cannot verify that it is complete or true. | Implemented | [.github/pull_request_template.md](.github/pull_request_template.md) |
| AI-03 | AI-generated changes are reviewed by someone other than the generator | T1 | 7 | Process | [NIST AI 100-1 MAP 3.5: Processes for human oversight are defined, assessed, and documented](https://www.nist.gov/itl/ai-risk-management-framework)<br>[NIST SP 800-218 PW.7 Review and/or Analyze Human-Readable Code](https://csrc.nist.gov/pubs/sp/800/218/final)<br>[OpenSSF Scorecard Code-Review](https://github.com/ossf/scorecard/blob/main/docs/checks.md) | Solo project: GitHub requires zero approvals, so reviewer independence rests on the documented process. Expect a low Scorecard Code-Review result. | Implemented | [.github/pull_request_template.md](.github/pull_request_template.md)<br>[docs/AI_USE_POLICY.md](docs/AI_USE_POLICY.md) |
| AI-04 | A written AI-use policy defines allowed use, review rules and data limits | T1 | 2, 5 | Process | [NIST AI 100-1 GOVERN 1.4 (risk management through transparent policies)](https://www.nist.gov/itl/ai-risk-management-framework)<br>[ISO/IEC 42001:2023 General alignment only (clauses not reviewed)](https://www.iso.org/standard/81230.html) | none recorded | Implemented | [docs/AI_USE_POLICY.md](docs/AI_USE_POLICY.md) |
| AI-05 | Apps that call LLMs version prompts and keep an eval set with expected outputs | T2 | 5, 6 | Automated | [NIST AI 100-1 MEASURE 2.1 (test sets, metrics and tools documented)](https://www.nist.gov/itl/ai-risk-management-framework)<br>[OWASP LLM Top 10 (2025) LLM05:2025 Improper Output Handling](https://genai.owasp.org/llm-top-10/) | none recorded | Planned | none yet |
| AI-06 | Lint and tests run automatically after every AI edit | T1 | 5, 6 | Automated | [NIST SP 800-218 PO.3 Implement Supporting Toolchains](https://csrc.nist.gov/pubs/sp/800/218/final)<br>[NIST SP 800-218 PW.7 Review and/or Analyze Human-Readable Code](https://csrc.nist.gov/pubs/sp/800/218/final)<br>[NIST SP 800-218 PW.8 Test Executable Code](https://csrc.nist.gov/pubs/sp/800/218/final) | Fires only in Claude Code sessions opened in this project (proved by a live test on 2026-11-01). Hand edits rely on pre-commit and CI. Uses a Windows-only interpreter path. | Implemented | [.claude/settings.json](.claude/settings.json) |

## Security

| ID | Control | From tier | Applied at phase | Enforced by | Aligned with | Limits | Status | Evidence |
|---|---|---|---|---|---|---|---|---|
| SEC-01 | Secret scanning runs before every commit | T0 | 5 | Automated | [NIST SP 800-218 PW.7 Review and/or Analyze Human-Readable Code](https://csrc.nist.gov/pubs/sp/800/218/final) | Local only today and bypassable. No OpenSSF Scorecard check covers committed secrets. See SEC-05. | Implemented | [.pre-commit-config.yaml](.pre-commit-config.yaml) |
| SEC-02 | Dependency updates are automated | T1 | 10 | Automated | [NIST SP 800-218 RV.1 Identify and Confirm Vulnerabilities on an Ongoing Basis](https://csrc.nist.gov/pubs/sp/800/218/final)<br>[NIST SP 800-218 PW.4 Reuse Existing, Well-Secured Software When Feasible](https://csrc.nist.gov/pubs/sp/800/218/final)<br>[OpenSSF Scorecard Dependency-Update-Tool](https://github.com/ossf/scorecard/blob/main/docs/checks.md) | none recorded | Implemented | [.github/dependabot.yml](.github/dependabot.yml) |
| SEC-03 | A security policy tells people how to report vulnerabilities | T1 | 10 | Process | [NIST SP 800-218 RV.1 Identify and Confirm Vulnerabilities on an Ongoing Basis](https://csrc.nist.gov/pubs/sp/800/218/final)<br>[OpenSSF Scorecard Security-Policy](https://github.com/ossf/scorecard/blob/main/docs/checks.md) | none recorded | Implemented | [SECURITY.md](SECURITY.md) |
| SEC-04 | A software bill of materials is published with each release | T2 | 8 | Automated | [NIST SP 800-218 PS.3 Archive and Protect Each Software Release](https://csrc.nist.gov/pubs/sp/800/218/final)<br>[OpenSSF Scorecard SBOM](https://github.com/ossf/scorecard/blob/main/docs/checks.md) | none recorded | Planned | none yet |
| SEC-05 | Secret scanning also runs in CI and GitHub push protection is enabled | T1 | 3, 5 | Automated | [NIST SP 800-218 PS.1 Protect All Forms of Code from Unauthorized Access and Tampering](https://csrc.nist.gov/pubs/sp/800/218/final)<br>[NIST SP 800-218 PW.7 Review and/or Analyze Human-Readable Code](https://csrc.nist.gov/pubs/sp/800/218/final) | none recorded | Planned | none yet |

## Operations

| ID | Control | From tier | Applied at phase | Enforced by | Aligned with | Limits | Status | Evidence |
|---|---|---|---|---|---|---|---|---|
| OPS-01 | Changes are recorded in a changelog with each release | T1 | 8 | Process | [ITIL 4 Change enablement](https://www.peoplecert.org/news-and-announcements/itil-4-management-practices-2023)<br>[ITIL 4 Release management](https://www.peoplecert.org/news-and-announcements/itil-4-management-practices-2023) | none recorded | Implemented | [CHANGELOG.md](CHANGELOG.md) |
| OPS-02 | Incidents and their root causes are logged | T1 | 10 | Process | [ITIL 4 Incident management](https://www.peoplecert.org/news-and-announcements/itil-4-management-practices-2023)<br>[ITIL 4 Problem management](https://www.peoplecert.org/news-and-announcements/itil-4-management-practices-2023)<br>[NIST SP 800-218 RV.3 Analyze Vulnerabilities to Identify Their Root Causes](https://csrc.nist.gov/pubs/sp/800/218/final) | none recorded | Implemented | [docs/INCIDENTS.md](docs/INCIDENTS.md) |
| OPS-03 | A runbook documents deploy, rollback and recovery | T2 | 8, 10 | Process | [ITIL 4 Service continuity management](https://www.peoplecert.org/news-and-announcements/itil-4-management-practices-2023)<br>[ISO/IEC/IEEE 12207:2017 6.4.12 Operation process](https://www.iso.org/standard/63712.html) | none recorded | Planned | none yet |

## Measurement

| ID | Control | From tier | Applied at phase | Enforced by | Aligned with | Limits | Status | Evidence |
|---|---|---|---|---|---|---|---|---|
| MEA-01 | Delivery metrics (change lead time, deployment frequency, failed deployment recovery time, change fail rate, deployment rework rate) are reported | T2 | 10 | Automated | [DORA Software delivery metrics (five, per the current guide)](https://dora.dev/guides/dora-metrics-four-keys)<br>[ISO/IEC/IEEE 12207:2017 6.3.7 Measurement process](https://www.iso.org/standard/63712.html) | none recorded | Planned | none yet |

## Trust

| ID | Control | From tier | Applied at phase | Enforced by | Aligned with | Limits | Status | Evidence |
|---|---|---|---|---|---|---|---|---|
| TRU-01 | TRUST.md is generated from this matrix and never hand-edited | T1 | 8 | Automated | Project-specific (no external standard) | none recorded | Implemented | [TRUST.md](TRUST.md)<br>[scripts/generate_trust.py](scripts/generate_trust.py) |
| TRU-02 | Each release ships an evidence bundle (test results, SBOM, review record, AI-use summary) | T2 | 8 | Automated | [NIST SP 800-218 PS.3 Archive and Protect Each Software Release](https://csrc.nist.gov/pubs/sp/800/218/final)<br>[NIST SP 800-218 PS.2 Provide a Mechanism for Verifying Software Release Integrity](https://csrc.nist.gov/pubs/sp/800/218/final) | none recorded | Planned | none yet |

## Where controls apply in the lifecycle

| Phase | Name | Controls |
|---|---|---|
| 1 | Idea and scope | GOV-01, GOV-03 |
| 2 | Design decisions | AI-04, GOV-02, GOV-03, GOV-04 |
| 3 | Repo foundation | ENG-01, ENG-02, GOV-03, SEC-05 (planned) |
| 4 | Walking skeleton | none yet |
| 5 | Iterate in slices | AI-01, AI-04, AI-05 (planned), AI-06, ENG-03, GOV-02, SEC-01, SEC-05 (planned) |
| 6 | Test | AI-05 (planned), AI-06, ENG-02, ENG-04 |
| 7 | Review and merge | AI-02, AI-03, ENG-01, ENG-02 |
| 8 | Release | OPS-01, OPS-03 (planned), SEC-04 (planned), TRU-01, TRU-02 (planned) |
| 9 | Pilot | none yet |
| 10 | Maintain | GOV-04, MEA-01 (planned), OPS-02, OPS-03 (planned), SEC-02, SEC-03 |

## Sources

| Source | Version | Published | Access | How much was read | Checked on | Notes |
|---|---|---|---|---|---|---|
| [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) | 1.1 | 2022-02 | Free | partial | 2026-11-01 | Practice IDs and names (PO, PS, PW, RV) verified against the PDF. Individual tasks such as PO.3.1 are not mapped. A draft Rev. 1 (SSDF 1.2) was published for comment on 2025-12-17 and is not adopted here. |
| [NIST AI 100-1](https://www.nist.gov/itl/ai-risk-management-framework) | 1.0 | 2023-01-26 | Free | partial | 2026-11-01 | Sixteen Core subcategory statements verified (GOVERN 1.1, 1.4, 2.1, 4.1, 4.2, 6.1; MAP 1.1, 3.5; MEASURE 1.1, 2.1, 2.3, 2.5, 2.7; MANAGE 1.1, 2.2, 4.1). NIST states the framework is being revised. |
| [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html) | Edition 1 | 2023-12 | Paid | none | 2026-11-01 | Purchase required; not read. It specifies requirements for an organisation's AI management system and is certifiable at organisation level. 2Legit cites it for general alignment only and makes no certification claim. |
| [ISO/IEC/IEEE 12207:2017](https://www.iso.org/standard/63712.html) | Edition 1 | 2017-11 | Paid | toc | 2026-11-01 | Clause numbers and process names verified from the publisher's public table-of-contents preview. Normative text not read. ISO lists the standard as due for revision. |
| [OWASP LLM Top 10 (2025)](https://genai.owasp.org/llm-top-10/) | 2025 | 2024-11 | Free | partial | 2026-11-01 | Entry IDs LLM01:2025 to LLM10:2025 and their names verified on the official page. |
| [OpenSSF Scorecard](https://github.com/ossf/scorecard/blob/main/docs/checks.md) | documentation on main branch | continuously updated | Free | partial | 2026-11-01 | Check names and descriptions verified. No Scorecard check detects committed secrets. Re-verify before external use because the documentation changes. |
| [DORA](https://dora.dev/guides/dora-metrics-four-keys) | current guide | continuously updated | Free | partial | 2026-11-01 | The current official guide lists five metrics: change lead time, deployment frequency, failed deployment recovery time, change fail rate and deployment rework rate. Older material refers to four key metrics. |
| [ITIL 4](https://www.peoplecert.org/news-and-announcements/itil-4-management-practices-2023) | ITIL 4 | 2019, practice guidance revised 2023 | Paid | names | 2026-11-01 | Practice names confirmed from official AXELOS and PeopleCert pages and a published practice list; the practice guides are paywalled and were not read. The name Service continuity management comes from a secondary source. |

Paid standards are linked to the official purchase page. 2Legit does not reproduce them.
