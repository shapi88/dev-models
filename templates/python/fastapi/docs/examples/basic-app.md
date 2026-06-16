# Example: Basic FastAPI App

See the `template/` directory for the runnable skeleton.

Key files:
- app/main.py : FastAPI app with lifespan and health endpoint.
- app/routers/items.py : Example router with Pydantic models.
- app/dependencies.py : DB/auth dependencies (expand as needed).
- pyproject.toml : Modern Python packaging with uv.

Run with:
uv run uvicorn app.main:app --reload

This mirrors the "examples/" style in the Java Spring Boot 4 module.