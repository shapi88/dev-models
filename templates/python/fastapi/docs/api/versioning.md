# API Versioning in FastAPI

## Recommended Strategy

Use URL path versioning for consistency with the Spring Boot 4 module:

```python
from fastapi import APIRouter

v1_router = APIRouter(prefix="/api/v1")
v2_router = APIRouter(prefix="/api/v2")

app.include_router(v1_router)
app.include_router(v2_router)
```

## Alternatives
- Header-based (Accept: application/vnd.company.v1+json) — for advanced cases.
- Query param — simple but less RESTful.

## Best Practices
- Keep old versions stable or explicitly deprecated with sunset headers.
- Share models where possible, but version DTOs when behavior changes.
- Document versions in OpenAPI tags or separate docs.

See the Java module's api/versioning.md for the full rationale and migration notes.