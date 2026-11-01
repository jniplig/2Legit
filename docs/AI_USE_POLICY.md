# AI use policy

Applies to every project that adopts 2Legit.

## Allowed

- AI assistants may draft code, tests, documentation and analysis.
- AI output is a draft. A human owns every change that is merged.

## Required

1. **Brief first.** A written task brief (`docs/templates/task-brief.md`) exists before AI generates code.
2. **Declare.** Every pull request states whether AI was used, which tool, and for what.
3. **Review by someone else.** AI-generated changes are reviewed by a person or session other than the one that generated them. The reviewer checks against the brief, not just whether it runs.
4. **Explainability.** The author can explain every line in the pull request.
5. **Tests ship with code.** Behaviour added by AI is covered by tests that fail without it.
6. **Verify claims.** Facts, citations, standards references and version numbers produced by AI are checked against a primary source before they are published.

## Prohibited

- Putting secrets, credentials or personal data into prompts, repos or test fixtures.
- Marking a control as implemented, or a test as passing, without evidence.
- Merging AI output that the author does not understand.

## For apps that call LLMs (T2)

Pin model versions, keep prompts as versioned files, keep an eval set of fixed inputs with expected outputs, validate model output against a schema, and track cost and rate limits. (Planned: control AI-05.)
