# Simple Dockerfile for the Python web-api model
# Uses the same Python version the model targets
FROM python:3.12-slim

WORKDIR /app

# Install uv (fast) or fall back to pip
RUN pip install --no-cache-dir uv

COPY pyproject.toml ./
# Copy source
COPY src ./src
COPY tests ./tests

# Install the project (dev deps optional at runtime)
RUN uv pip install --system -e .

EXPOSE 8000

# In real life: use uvicorn/gunicorn with proper workers
CMD ["python", "-m", "myapp.main"]