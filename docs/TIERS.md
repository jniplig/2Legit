# Assurance tiers

Rigor scales with risk. Declare a tier in the project charter. Promote the tier
before the first external user, customer or investor sees the project.

| Tier | Name | Use when | Expected controls |
|---|---|---|---|
| T0 | Spike | Throwaway experiment. No real data, no users. | Controls with `min_tier: T0` |
| T1 | Personal tool | Used by the owner or family. Low-risk data. | T0 and T1 controls |
| T2 | External | Real users, customers, investors, or other people's personal data. | All controls |

## Lifecycle gates

| Phase | Gate | Applies from |
|---|---|---|
| 1. Idea and scope | One-page charter | T1 |
| 2. Design decisions | Decisions recorded | T1 |
| 3. Repo foundation | CI green, main protected, secret scanning on | T0 (CI and main protection from T1) |
| 4. Walking skeleton | Runs on a clean checkout | T0 |
| 5. Iterate in slices | One task brief, one PR | T1 |
| 6. Test | Tests written with the code | T1 |
| 7. Review and merge | Independent review recorded in the PR | T1 |
| 8. Release | Changelog; evidence bundle at T2 | T1 |
| 9. Pilot | Findings triaged into the backlog | T2 |
| 10. Maintain | Incident log, dependency updates, metrics | T1 (metrics at T2) |

Phases 4 to 7 repeat for every slice of work.

## Promotion checklist (T1 to T2)

- [ ] Every control with `min_tier: T2` is implemented or has a dated exception in `docs/DECISIONS.md`
- [ ] `TRUST.md` regenerated and reviewed
- [ ] Data classification in the charter re-confirmed
