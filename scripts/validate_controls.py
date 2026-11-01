#!/usr/bin/env python3
"""Validate docs/controls.yaml: schema, uniqueness and evidence integrity.

Run: python -m scripts.validate_controls
Exit code 0 = valid, 1 = errors found.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MATRIX = ROOT / "docs" / "controls.yaml"

LAYERS = {
    "governance": "Governance",
    "engineering": "Engineering controls",
    "ai": "AI controls",
    "security": "Security",
    "operations": "Operations",
    "measurement": "Measurement",
    "trust": "Trust",
}
TIERS = ("T0", "T1", "T2")
STATUSES = ("implemented", "planned")
REQUIRED_FIELDS = ("id", "title", "layer", "min_tier", "standards", "evidence", "status")


def load(path: Path = MATRIX) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def validate(data: object, root: Path = ROOT) -> list[str]:
    """Return a list of error strings. An empty list means the matrix is valid."""
    if not isinstance(data, dict) or not isinstance(data.get("controls"), list):
        return ["top level must be a mapping with a 'controls' list"]
    controls = data["controls"]
    if not controls:
        return ["'controls' must not be empty"]

    errors: list[str] = []
    seen: set[str] = set()
    for index, control in enumerate(controls):
        if not isinstance(control, dict):
            errors.append(f"control #{index}: must be a mapping")
            continue
        cid = str(control.get("id", f"#{index}"))
        for field in REQUIRED_FIELDS:
            if field not in control:
                errors.append(f"{cid}: missing field '{field}'")
        if cid in seen:
            errors.append(f"{cid}: duplicate id")
        seen.add(cid)
        if control.get("layer") not in LAYERS:
            errors.append(f"{cid}: layer must be one of {sorted(LAYERS)}")
        if control.get("min_tier") not in TIERS:
            errors.append(f"{cid}: min_tier must be one of {TIERS}")
        if control.get("status") not in STATUSES:
            errors.append(f"{cid}: status must be one of {STATUSES}")
        standards = control.get("standards")
        if not isinstance(standards, list) or not standards:
            errors.append(f"{cid}: standards must be a non-empty list")
        evidence = control.get("evidence")
        if not isinstance(evidence, list):
            errors.append(f"{cid}: evidence must be a list")
            continue
        if control.get("status") == "implemented":
            if not evidence:
                errors.append(f"{cid}: implemented control needs at least one evidence path")
            for path in evidence:
                if not (root / path).exists():
                    errors.append(f"{cid}: evidence file not found: {path}")
    return errors


def main() -> int:
    errors = validate(load())
    if errors:
        print("controls.yaml is INVALID:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("controls.yaml is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
