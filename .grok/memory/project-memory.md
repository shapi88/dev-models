# Project Memory for dev-models (local .grok)

Key context for agents working in this repo:

- Primary goal: Developer Manual + real templates per language/framework.
- Reference module: templates/java/spring-boot-4/docs/ (very complete with Java 25 focus, migration, optimizations, persistence).
- New modules must match depth (see templates/python/fastapi/ for example).
- Current modules: Java Spring Boot 4, Python FastAPI.
- Architectures (monolith v1, microservices v1) are shared in manual/architectures/.
- **Rule Set:** All agents and skills MUST follow the exact same structure and strategy as defined in .github/ (frontmatter, Core Directives, schemas, guardrails). .grok/ is the local execution view; .github/ is the CI view. Always enforce consistency across modules.
- Use the .grok/skills/ and agents/ (and cross-reference .github/) for task execution.
- Always check plan.md for the current roadmap and the "Phase: Adapt .grok..." section for alignment details.

When acting locally, load rules from .grok/guardrails.md and .grok/grok-instructions.md.