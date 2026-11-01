#!/usr/bin/env python3
"""Validate docs/controls.yaml and docs/standards.yaml: schema, uniqueness, evidence
integrity and traceability of every standards reference.

Run: python -m scripts.validate_controls
Exit code 0 = valid, 1 = errors found.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MATRIX = ROOT / "docs" / "controls.yaml"
REGISTER = ROOT / "docs" / "standards.yaml"

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
REQUIRED_FIELDS = (
    "id", "title", "layer", "min_tier", "standards", "applied_in", "enforced_by", "evidence",
    "status",
)
PHASES = range(1, 11)
ENFORCERS = ("automated", "process")
PROJECT_SPECIFIC = "project-specific"
GENERAL_ALIGNMENT = "General alignment only (clauses not reviewed)"
SOURCE_FIELDS = (
    "name", "id", "publisher", "version", "published", "url", "access", "read", "verified_on",
    "note",
)
ACCESS = ("free", "paid")
READ_LEVELS = ("full", "partial", "toc", "names", "none")


def load(path: Path = MATRIX) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_register(path: Path = REGISTER) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def validate_register(register: object) -> list[str]:
    """Return a list of error strings for the standards register."""
    if not isinstance(register, dict) or not isinstance(register.get("sources"), dict):
        return ["register: top level must be a mapping with a 'sources' mapping"]
    errors: list[str] = []
    for key, source in register["sources"].items():
        if not isinstance(source, dict):
            errors.append(f"register {key}: must be a mapping")
            continue
        for field in SOURCE_FIELDS:
            if field not in source:
                errors.append(f"register {key}: missing field '{field}'")
        if source.get("access") not in ACCESS:
            errors.append(f"register {key}: access must be one of {ACCESS}")
        if source.get("read") not in READ_LEVELS:
            errors.append(f"register {key}: read must be one of {READ_LEVELS}")
        if not str(source.get("url", "")).startswith("https://"):
            errors.append(f"register {key}: url must start with https://")
    return errors


def _validate_standards(cid: str, control: dict, sources: dict) -> list[str]:
    standards = control.get("standards")
    if not isinstance(standards, list):
        return [f"{cid}: standards must be a list"]
    if not standards:
        if control.get("basis") == PROJECT_SPECIFIC:
            return []
        return [f"{cid}: standards must not be empty unless basis is '{PROJECT_SPECIFIC}'"]
    errors: list[str] = []
    for entry in standards:
        if not (
            isinstance(entry, dict)
            and isinstance(entry.get("source"), str) and entry["source"]
            and isinstance(entry.get("ref"), str) and entry["ref"]
        ):
            errors.append(f"{cid}: each standards entry needs a non-empty 'source' and 'ref'")
            continue
        source = sources.get(entry["source"])
        if not isinstance(source, dict):
            errors.append(f"{cid}: unknown source '{entry['source']}' (not in docs/standards.yaml)")
        elif source.get("read") == "none" and entry["ref"] != GENERAL_ALIGNMENT:
            errors.append(
                f"{cid}: source '{entry['source']}' was not read; ref must be "
                f"'{GENERAL_ALIGNMENT}'"
            )
    return errors


def validate(data: object, root: Path = ROOT, register: dict | None = None) -> list[str]:
    """Return a list of error strings. An empty list means the matrix is valid."""
    if register is None:
        register = load_register()
    errors: list[str] = validate_register(register)
    sources = register["sources"] if isinstance(register, dict) else {}
    if not isinstance(sources, dict):
        sources = {}
    if not isinstance(data, dict) or not isinstance(data.get("controls"), list):
        return errors + ["top level must be a mapping with a 'controls' list"]
    controls = data["controls"]
    if not controls:
        return errors + ["'controls' must not be empty"]

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
        if "standards" in control:
            errors += _validate_standards(cid, control, sources)
        if "applied_in" in control:
            phases = control["applied_in"]
            if (
                not isinstance(phases, list)
                or not phases
                or any(isinstance(p, bool) or p not in PHASES for p in phases)
            ):
                errors.append(f"{cid}: applied_in must be a non-empty list of phases 1 to 10")
        if "enforced_by" in control and control["enforced_by"] not in ENFORCERS:
            errors.append(f"{cid}: enforced_by must be one of {ENFORCERS}")
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
