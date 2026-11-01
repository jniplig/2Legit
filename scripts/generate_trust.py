#!/usr/bin/env python3
"""Generate TRUST.md from docs/controls.yaml.

Run:   python -m scripts.generate_trust          (write TRUST.md)
Check: python -m scripts.generate_trust --check  (fail if TRUST.md is stale)

Output is deterministic (no timestamps) so the freshness check is stable.
"""
from __future__ import annotations

import sys

from scripts.validate_controls import LAYERS, ROOT, TIERS, load, validate

TRUST_FILE = ROOT / "TRUST.md"

INTRO = """\
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
"""


def _evidence_cell(evidence: list[str]) -> str:
    return "<br>".join(f"[{p}]({p})" for p in evidence) if evidence else "none yet"


def render(data: dict) -> str:
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
        header = "| ID | Control | From tier | Aligned with | Status | Evidence |"
        lines += [f"## {name}", "", header, "|---|---|---|---|---|---|"]
        for c in group:
            standards = "<br>".join(c["standards"])
            lines.append(
                f"| {c['id']} | {c['title']} | {c['min_tier']} | {standards} "
                f"| {c['status'].capitalize()} | {_evidence_cell(c['evidence'])} |"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str]) -> int:
    data = load()
    errors = validate(data)
    if errors:
        print("Refusing to generate: controls.yaml is invalid.")
        for error in errors:
            print(f"  - {error}")
        return 1
    text = render(data)
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
