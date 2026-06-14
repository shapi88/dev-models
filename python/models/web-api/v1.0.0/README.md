# Python Web API — Model v1.0.0

**A clean, modern, production-oriented reference structure for a Python web API/service.**

## When to use this model
- Building a new HTTP API / microservice in Python.
- You want the current (2026) recommended packaging and layout without framework lock-in in the folder names.
- You value clear src/ layout, type safety, fast iteration (uv + ruff), and easy Dockerization.

This is **not** a full framework tutorial. It gives you the skeleton + the "why".

## Layout (what you get when you copy this dir)

```
v1.0.0/
├── README.md                 # you are here
├── pyproject.toml
├── .python-version           # optional pin (uv / pyenv style)
├── src/
│   └── myapp/
│       ├── __init__.py
│       ├── main.py           # entrypoint / app factory example
│       └── config.py
├── tests/
│   └── test_health.py
├── Dockerfile
└── .gitignore
```

## Key Decisions & Rationale

- **src/ layout** — avoids import surprises and is the modern recommendation (see PEP 420 / packaging guides).
- **pyproject.toml only** — no legacy setup.py / requirements.txt sprawl.
- **Single "myapp" namespace** inside src — rename this to your real project name immediately.
- Minimal but real **Dockerfile** using the same Python version.
- Basic health endpoint pattern so you have something that runs immediately.
- Ruff + (commented) mypy in pyproject for fast linting + types from day one.

## How to turn this into a real project

```bash
# 1. Copy the model
cp -r path/to/dev-models/python/models/web-api/v1.0.0/* ./my-api/
cd my-api

# 2. Rename the package (example)
mv src/myapp src/my_real_api
# Then update imports and pyproject.toml [project] name + packages

# 3. Initialize
uv sync          # or pip install -e ".[dev]"
uv run ruff check
uv run pytest

# 4. Run
uv run python -m my_real_api.main

# 5. Docker
docker build -t my-api .
```

## Compatibility
- Python 3.11+
- Designed around uv (strongly recommended) but works with pip + venv
- ruff, pytest, (optional mypy)

Tested with Python 3.12.

## Next versions ideas (for v1.1+)
- Add observability (structlog + prometheus)
- SQLAlchemy / async DB example
- Auth patterns (JWT)
- Better config management (pydantic-settings)

## References
- https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
- https://docs.astral.sh/uv/
- https://github.com/astral-sh/ruff

---

**Model version:** v1.0.0  
**Last reviewed:** 2026-06-14

Copy this version, evolve it for your needs, and consider contributing improvements back as a new minor or major version.