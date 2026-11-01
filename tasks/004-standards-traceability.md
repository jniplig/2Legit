# Task 004: Standards traceability (source register, verifiable references, lifecycle mapping)

## Goal
Every claim of alignment with a standard must be traceable. A reader must be able to see, for each control: which standard and which part it derives from (with a link to the official source), at which lifecycle phase it applies, whether it is enforced by a tool or only by process, and what its honest limits are. The generated `TRUST.md` must show all of this, and CI must reject references that cannot be traced.

## Prerequisites (STOP if false)
- Task 003 is merged to `main`, or the human has said to skip it.
- `git status` is clean and you are on an up-to-date `main`.
- The folder `tasks/004-assets/` contains `controls.yaml` and `standards.yaml`.

## Scope
Work on a new branch `task-004-traceability`.

In:
1. Move `tasks/004-assets/standards.yaml` to `docs/standards.yaml` using `git mv`. Do not edit its content.
2. Replace `docs/controls.yaml` with `tasks/004-assets/controls.yaml` (use `git mv` to overwrite). One exception: if the existing `ENG-01` entry on `main` has `status: implemented`, keep that status and its `evidence` list in the new file, and leave its other fields as given in the asset. Do not edit any other field of any control.
3. Update `scripts/validate_controls.py` to enforce the new schema. Keep `validate(data, root)` as the function signature and add an optional parameter `register` (a dict loaded from `docs/standards.yaml`; load it by default). The validator must report an error when:
   - a control is missing `applied_in`, `enforced_by` or `standards`
   - `applied_in` is empty or contains a value outside 1 to 10
   - `enforced_by` is not `automated` or `process`
   - `standards` is empty and the control does not have `basis: project-specific`
   - a standards entry is not a mapping with non-empty `source` and `ref`
   - a `source` is not a key in the register
   - the cited source has `read: none` in the register and `ref` is not exactly `General alignment only (clauses not reviewed)`
   - a register entry lacks any of: `name`, `id`, `publisher`, `version`, `published`, `url`, `access`, `read`, `verified_on`, `note`
   - a register `access` is not `free` or `paid`, or `read` is not one of `full`, `partial`, `toc`, `names`, `none`
   - `url` in the register does not start with `https://`
   Keep all existing checks (layers, tiers, statuses, duplicate ids, evidence files for implemented controls).
4. Update `scripts/generate_trust.py` so that `TRUST.md` contains, in this order:
   a. the existing introduction, plus one added sentence: `Every reference below links to the official source and states how much of that source was read.`
   b. the existing Summary section (unchanged logic)
   c. one table per layer with these columns: `ID | Control | From tier | Applied at phase | Enforced by | Aligned with | Limits | Status | Evidence`. In `Aligned with`, show each reference as a Markdown link: `[<source id> <ref>](<source url>)`, one per line separated by `<br>`. For a control with `basis: project-specific`, show `Project-specific (no external standard)`. In `Applied at phase`, show the phase numbers separated by commas. `Limits` shows the `note` field, or `none recorded`.
   d. a new section `## Where controls apply in the lifecycle` with one row per phase 1 to 10, columns `Phase | Name | Controls`. Use these phase names exactly: 1 Idea and scope, 2 Design decisions, 3 Repo foundation, 4 Walking skeleton, 5 Iterate in slices, 6 Test, 7 Review and merge, 8 Release, 9 Pilot, 10 Maintain. List control ids applying at that phase, with planned ones followed by ` (planned)`. Phases with no controls show `none yet`.
   e. a new section `## Sources` with one row per register source that is cited by at least one control, columns `Source | Version | Published | Access | How much was read | Checked on | Notes`. The first column is a Markdown link to the source url. Add a sentence below the table: `Paid standards are linked to the official purchase page. 2Legit does not reproduce them.`
   Output must stay deterministic (no timestamps). Keep the `--check` mode.
5. Add tests in `tests/test_standards.py` covering at least: the repo's register is valid; an unknown source is rejected; a `read: none` source with a clause-level ref is rejected; a `read: none` source with the exact general-alignment ref is accepted; empty `standards` without `basis: project-specific` is rejected; empty `standards` with it is accepted; `applied_in` out of range is rejected; invalid `enforced_by` is rejected; a register entry missing a field is rejected; generated TRUST text contains every control id in the lifecycle section; generated TRUST text contains a link to the source url for every cited source. Update `tests/test_controls.py` only where the new schema requires it.
6. In `CLAUDE.md`, replace rule 8 with exactly: `8. Every standards reference must cite a source key defined in docs/standards.yaml. Do not cite clause numbers you have not verified against the official source, and never raise a source's "read" level without actually reading it.`
7. In `README.md`, add one sentence under "How it works": `Every standards reference is traceable through [docs/standards.yaml](docs/standards.yaml), which records the official source, version, date checked and how much of each source was read.`
8. Under `[Unreleased]` in `CHANGELOG.md`, add: `- Standards source register, per-control lifecycle phase, enforcement type and limits, with CI checks (control GOV-04)`
9. Regenerate `TRUST.md` with `python -m scripts.generate_trust`.

Out:
- Do not change the wording of any control title, reference, note or register entry.
- Do not edit `TRUST.md` by hand.
- Do not merge. Open a pull request with `gh pr create` and fill in every section of the PR template honestly.

## Acceptance criteria
- [ ] `pytest`, `ruff check .`, `python -m scripts.validate_controls` and `python -m scripts.generate_trust --check` all pass
- [ ] `TRUST.md` has the new columns, the lifecycle section and the Sources section
- [ ] Every reference in `TRUST.md` is a link to an `https://` URL
- [ ] Control `GOV-04` shows as Implemented
- [ ] The controls `ENG-01` and `SEC-05` show their status exactly as in the asset (ENG-01 is the only permitted deviation, per step 2)
- [ ] Temporarily setting a control's source to `nonexistent` makes `validate_controls` fail; revert afterwards and confirm `git diff` is empty for that file
- [ ] The pull request is open and CI is passing

## Report back
Output of the four standard checks, the failing output from the `nonexistent` source test, the PR URL, the CI result, and every file changed.

## AI use
Tool and model: Claude Code CLI
Executor session: this session
Reviewer (must differ from executor): the Claude chat session that wrote this brief. The standards mapping content was written by that chat session and checked against official sources; the human must spot-check the register links before relying on them externally.
