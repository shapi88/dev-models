# Guardrails for dev-models (local .grok)

This file defines rules that all local agents, Grok sessions, and contributors must follow when working in this repo via the local Grok environment.

## Hard Rules
- Do not modify .github/ or .grok/ without a human-approved plan (these define the agent behavior itself).
- Maintain strict separation: templates/<language>/<framework>/ must be self-contained and mirror the reference module (e.g. the Java Spring Boot 4 structure for new ones like Python FastAPI).
- All new content must be suitable for junior developers.
- When adding persistence docs, cover at least Postgres, Mongo, and general SQL for parity.
- Update plan.md and relevant READMEs for any structural change.
- Respect versioning (v1 for architectures, major versions for frameworks like spring-boot-4 or fastapi equivalents).

## Soft Guidelines
- Prefer async patterns in Python/FastAPI modules.
- Link cross-cutting architectures from every module.
- Keep examples minimal but runnable in the template/ dirs.
- When using local agents, always follow the Core Directives from the .agent.md files.

Violations should be caught via review (use skills like review-pr).

This mirrors the .github/guardrails.md for consistency between local and CI.