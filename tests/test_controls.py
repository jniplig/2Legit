"""Self-tests: 2Legit applies its own rules to itself."""
from pathlib import Path

from scripts.generate_trust import TRUST_FILE, render
from scripts.validate_controls import ROOT, load, validate


def _control(**overrides):
    base = {
        "id": "X-01",
        "title": "t",
        "layer": "governance",
        "min_tier": "T1",
        "standards": [{"source": "ssdf", "ref": "PW.8 Test Executable Code"}],
        "applied_in": [6],
        "enforced_by": "automated",
        "evidence": [],
        "status": "planned",
    }
    base.update(overrides)
    return {"controls": [base]}


def test_repo_matrix_is_valid():
    assert validate(load()) == []


def test_trust_md_is_up_to_date():
    assert TRUST_FILE.read_text(encoding="utf-8") == render(load())


def test_planned_control_needs_no_evidence():
    assert validate(_control(), root=ROOT) == []


def test_implemented_without_evidence_is_rejected():
    errors = validate(_control(status="implemented"), root=ROOT)
    assert any("needs at least one evidence path" in e for e in errors)


def test_implemented_with_missing_file_is_rejected(tmp_path: Path):
    errors = validate(_control(status="implemented", evidence=["nope.md"]), root=tmp_path)
    assert any("evidence file not found" in e for e in errors)


def test_implemented_with_existing_file_is_accepted(tmp_path: Path):
    (tmp_path / "ok.md").write_text("x", encoding="utf-8")
    assert validate(_control(status="implemented", evidence=["ok.md"]), root=tmp_path) == []


def test_duplicate_ids_are_rejected():
    data = _control()
    data["controls"].append(dict(data["controls"][0]))
    assert any("duplicate id" in e for e in validate(data, root=ROOT))


def test_bad_tier_layer_and_status_are_rejected():
    errors = validate(_control(min_tier="T9", layer="nope", status="done"), root=ROOT)
    assert len(errors) == 3


def test_malformed_input_is_rejected():
    assert validate(None) != []
    assert validate({"controls": []}) != []


def test_generated_text_never_claims_compliance():
    text = render(load()).lower()
    assert "certified" not in text.replace("not a certification", "")
    assert "compliant" not in text.replace("claim of compliance", "")
