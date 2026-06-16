# Guardrails for dev-models

This file defines rules that all agents, Copilot, and contributors must follow.

## Hard Rules
- Do not modify .github/ or .grok/ without a human-approved plan (these define the agent behavior itself).
- Maintain strict separation: templates/<language>/<framework>/ must be self-contained and mirror the reference module.
- All new content must be suitable for junior developers.
- When adding persistence docs, cover at least Postgres, Mongo, and general SQL for parity.
- Update plan.md and relevant READMEs for any structural change.
- Respect versioning (v1 for architectures, major versions for frameworks like spring-boot-4 or fastapi equivalents).

## Soft Guidelines
- Prefer async patterns in Python/FastAPI modules.
- Link cross-cutting architectures from every module.
- Keep examples minimal but runnable in the template/ dirs.

Violations should be caught in PR reviews (see skills/review-pr.yml).