# Python FastAPI Template (dev-models reference)

This is the starter template for Python 3 + FastAPI, matching the documentation in `docs/`.

## Quick Start
1. cd template
2. uv sync (or pip install -e .)
3. uv run uvicorn app.main:app --reload

## Structure
- app/ : Main application code (routers, models, dependencies).
- pyproject.toml : Dependencies and tool config.
- Dockerfile : Container image.

Expand this skeleton when using as the base for a new project. See the sibling `docs/` for full guidance (getting-started, best-practices, persistence, etc.).

Parity with Java Spring Boot 4 template.