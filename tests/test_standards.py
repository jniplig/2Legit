"""Traceability: every standards reference cites a registered, honestly described source."""
from scripts.generate_trust import render
from scripts.validate_controls import (
    GENERAL_ALIGNMENT,
    ROOT,
    load,
    load_register,
    validate,
    validate_register,
)


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


def _register(**source_overrides):
    """A register with one unread source ('closed') plus one read source ('ssdf')."""
    closed = {
        "name": "n",
        "id": "CLOSED-1",
        "publisher": "p",
        "version": "1",
        "published": "2020",
        "url": "https://example.org/closed",
        "access": "paid",
        "read": "none",
        "verified_on": "2026-11-01",
        "note": "not read",
    }
    closed.update(source_overrides)
    ssdf = dict(closed, id="SSDF", url="https://example.org/ssdf", access="free", read="partial")
    return {"sources": {"closed": closed, "ssdf": ssdf}}


def test_repo_register_is_valid():
    assert validate_register(load_register()) == []


def test_unknown_source_is_rejected():
    data = _control(standards=[{"source": "nonexistent", "ref": "x"}])
    assert any("unknown source" in e for e in validate(data, root=ROOT))


def test_unread_source_with_clause_ref_is_rejected():
    data = _control(standards=[{"source": "closed", "ref": "4.1 Context"}])
    errors = validate(data, root=ROOT, register=_register())
    assert any("was not read" in e for e in errors)


def test_unread_source_with_general_alignment_ref_is_accepted():
    data = _control(standards=[{"source": "closed", "ref": GENERAL_ALIGNMENT}])
    assert validate(data, root=ROOT, register=_register()) == []


def test_empty_standards_without_basis_is_rejected():
    errors = validate(_control(standards=[]), root=ROOT)
    assert any("must not be empty" in e for e in errors)


def test_empty_standards_with_project_specific_basis_is_accepted():
    assert validate(_control(standards=[], basis="project-specific"), root=ROOT) == []


def test_standards_entry_must_be_mapping_with_source_and_ref():
    errors = validate(_control(standards=["NIST SSDF PW.8"]), root=ROOT)
    assert any("non-empty 'source' and 'ref'" in e for e in errors)
    errors = validate(_control(standards=[{"source": "ssdf", "ref": ""}]), root=ROOT)
    assert any("non-empty 'source' and 'ref'" in e for e in errors)


def test_applied_in_out_of_range_is_rejected():
    for phases in ([0], [11], [], [True], "5"):
        errors = validate(_control(applied_in=phases), root=ROOT)
        assert any("applied_in" in e for e in errors), phases


def test_invalid_enforced_by_is_rejected():
    errors = validate(_control(enforced_by="hope"), root=ROOT)
    assert any("enforced_by" in e for e in errors)


def test_missing_new_fields_are_rejected():
    data = _control()
    for field in ("applied_in", "enforced_by", "standards"):
        del data["controls"][0][field]
    errors = validate(data, root=ROOT)
    for field in ("applied_in", "enforced_by", "standards"):
        assert f"missing field '{field}'" in " ".join(errors)


def test_register_entry_missing_field_is_rejected():
    register = _register()
    del register["sources"]["closed"]["verified_on"]
    assert any("missing field 'verified_on'" in e for e in validate_register(register))


def test_register_bad_access_read_and_url_are_rejected():
    errors = validate_register(_register(access="free?", read="skimmed", url="http://x"))
    assert len(errors) == 3


def test_lifecycle_section_lists_every_control():
    data = load()
    text = render(data)
    lifecycle = text.split("## Where controls apply in the lifecycle")[1].split("## Sources")[0]
    for control in data["controls"]:
        assert control["id"] in lifecycle


def test_sources_section_links_every_cited_source():
    data = load()
    register = load_register()
    text = render(data, register)
    sources = text.split("## Sources")[1]
    cited = {s["source"] for c in data["controls"] for s in c["standards"]}
    for key in cited:
        assert f"]({register['sources'][key]['url']})" in sources
