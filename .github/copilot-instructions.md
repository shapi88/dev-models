# Copilot Instructions for dev-models

This repository contains the Developer Manual and templates separated by framework and language.

## Agent Behavior Rules
- Always respect the templates/ structure: each language/framework (e.g. java/spring-boot-4, python/fastapi) should have parallel docs (getting-started, api/, best-practices/, persistence/, migration/) + a template/ code skeleton.
- When editing or generating, maintain consistency with the Spring Boot 4 reference module.
- Cross-cutting content (architectures, onboarding) lives in manual/.
- Prefer updating plan.md and READMEs when structure changes.
- For new modules, mirror the full depth: include memory/startup optimization, persistence for multiple DBs (Postgres, Mongo, SQL), and migration strategies.
- Use Python 3 + FastAPI specifics: async/await, Pydantic v2, SQLAlchemy 2.0 or Motor, uvicorn.

Read the root plan.md and templates/*/docs/README.md before proposing large changes.