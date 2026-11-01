#!/usr/bin/env python3
"""Generate TRUST.md from docs/controls.yaml and docs/standards.yaml.

Run:   python -m scripts.generate_trust          (write TRUST.md)
Check: python -m scripts.generate_trust --check  (fail if TRUST.md is stale)

Output is deterministic (no timestamps) so the freshness check is stable.
"""
from __future__ import annotations

import sys

from scripts.validate_controls import (
    LAYERS,
    PHASES,
    PROJECT_SPECIFIC,
    ROOT,
    TIERS,
    load,
    load_register,
    validate,
)

TRUST_FILE = ROOT / "TRUST.md"

PHASE_NAMES = {
    1: "Idea and scope",
    2: "Design decisions",
    3: "Repo foundation",
    4: "Walking skeleton",
    5: "Iterate in slices",
    6: "Test",
    7: "Review and merge",
    8: "Release",
    9: "Pilot",
    10: "Maintain",
}

INTRO = """\
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
"""


def _evidence_cell(evidence: list[str]) -> str:
    return "<br>".join(f"[{p}]({p})" for p in evidence) if evidence else "none yet"


def _standards_cell(control: dict, sources: dict) -> str:
    if control.get("basis") == PROJECT_SPECIFIC:
        return "Project-specific (no external standard)"
    return "<br>".join(
        f"[{sources[s['source']]['id']} {s['ref']}]({sources[s['source']]['url']})"
        for s in control["standards"]
    )


def render(data: dict, register: dict | None = None) -> str:
    sources = (register if register is not None else load_register())["sources"]
    controls = sorted(data["controls"], key=lambda c: c["id"])
    done = sum(1 for c in controls if c["status"] == "implemented")
    total = len(controls)
    lines = [INTRO, "## Summary", ""]
    lines.append(f"**{done} of {total} controls implemented ({round(100 * done / total)}%).**")
    lines.append("")
    lines.append("| Tier | Controls expected | Implemented |")
    lines.append("|---|---|---|")
    for index, tier in enumerate(TIERS):
        expected = [c for c in controls if TIERS.index(c["min_tier"]) <= index]
        impl = sum(1 for c in expected if c["status"] == "implemented")
        lines.append(f"| {tier} | {len(expected)} | {impl} |")
    lines.append("")
    for layer, name in LAYERS.items():
        group = [c for c in controls if c["layer"] == layer]
        if not group:
            continue
        header = (
            "| ID | Control | From tier | Applied at phase | Enforced by | Aligned with "
            "| Limits | Status | Evidence |"
        )
        lines += [f"## {name}", "", header, "|---|---|---|---|---|---|---|---|---|"]
        for c in group:
            phases = ", ".join(str(p) for p in c["applied_in"])
            lines.append(
                f"| {c['id']} | {c['title']} | {c['min_tier']} | {phases} "
                f"| {c['enforced_by'].capitalize()} | {_standards_cell(c, sources)} "
                f"| {c.get('note') or 'none recorded'} "
                f"| {c['status'].capitalize()} | {_evidence_cell(c['evidence'])} |"
            )
        lines.append("")

    lines += ["## Where controls apply in the lifecycle", ""]
    lines += ["| Phase | Name | Controls |", "|---|---|---|"]
    for phase in PHASES:
        ids = [
            c["id"] + (" (planned)" if c["status"] == "planned" else "")
            for c in controls
            if phase in c["applied_in"]
        ]
        lines.append(f"| {phase} | {PHASE_NAMES[phase]} | {', '.join(ids) or 'none yet'} |")
    lines.append("")

    cited = {s["source"] for c in controls for s in c["standards"]}
    lines += ["## Sources", ""]
    lines.append(
        "| Source | Version | Published | Access | How much was read | Checked on | Notes |"
    )
    lines.append("|---|---|---|---|---|---|---|")
    for key, src in sources.items():
        if key not in cited:
            continue
        lines.append(
            f"| [{src['id']}]({src['url']}) | {src['version']} | {src['published']} "
            f"| {src['access'].capitalize()} | {src['read']} | {src['verified_on']} "
            f"| {src['note']} |"
        )
    lines += [
        "",
        "Paid standards are linked to the official purchase page. 2Legit does not reproduce them.",
    ]
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str]) -> int:
    data = load()
    register = load_register()
    errors = validate(data, register=register)
    if errors:
        print("Refusing to generate: controls.yaml is invalid.")
        for error in errors:
            print(f"  - {error}")
        return 1
    text = render(data, register)
    if "--check" in argv:
        current = TRUST_FILE.read_text(encoding="utf-8") if TRUST_FILE.exists() else ""
        if current != text:
            print("TRUST.md is out of date. Run: python -m scripts.generate_trust")
            return 1
        print("TRUST.md is up to date.")
        return 0
    TRUST_FILE.write_text(text, encoding="utf-8", newline="\n")
    print(f"Wrote {TRUST_FILE.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
