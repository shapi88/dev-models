# Python 3 + FastAPI — Getting Started

**Target:** Python 3.12+ / 3.13 + FastAPI + Uvicorn (or Hypercorn).

## Recommended Setup (2026 model)

Use `uv` (fast) or `poetry`:

```bash
uv init my-fastapi-app
cd my-fastapi-app
uv add fastapi uvicorn[standard] pydantic-settings
uv add --dev pytest httpx ruff
```

## Project Structure (Recommended for this module)

```
my-fastapi-app/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   ├── routers/
│   │   └── items.py
│   └── models/
├── pyproject.toml
├── Dockerfile
└── README.md
```

## Run

```bash
uv run uvicorn app.main:app --reload
```

## Java 25 / Spring Boot 4 Equivalence Notes

- FastAPI + Pydantic v2 ≈ Spring MVC + records + validation
- Dependencies (Depends) ≈ @Autowired + custom resolvers
- Uvicorn workers ≈ Spring Boot embedded Tomcat with virtual threads
- SQLAlchemy 2.0 (async) ≈ Spring Data JPA

See the other docs in this module for direct parallels.