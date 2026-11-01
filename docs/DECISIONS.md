# Decision log

## D-001: Project name is 2Legit
Status: accepted. A play on "to legit(imate)". The tagline stays factual.

## D-002: MIT licence
Status: accepted. Simple and permissive so other projects can adopt the kit freely.
Consequence: no patent grant. Revisit if commercial use grows.

## D-003: Wording rule for claims
Status: accepted. Public text says "aligned with", never "compliant with", "certified" or "guaranteed".
Reason: only an accredited auditor can certify. Overclaiming is itself a form of slop.
Consequence: a test fails if generated text contains those words outside the disclaimer.

## D-004: Evidence rule
Status: accepted. A control is `implemented` only if its evidence file exists; CI enforces it. Planned controls are listed but never claimed.

## D-005: Python for the tooling
Status: accepted. Matches the owner's main stack. The kit's rules are language-neutral; stack add-ons come later.

## D-006: Standard references use names, not clause numbers
Status: accepted. Only references that are well established are cited (for example NIST SSDF practice IDs). Verify against the current edition before external use.
