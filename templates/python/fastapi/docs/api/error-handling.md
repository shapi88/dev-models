# Error Handling in FastAPI (Python 3 + FastAPI)

## Recommended Pattern

Use HTTPException with consistent error models, or a custom exception handler for RFC 7807 / Problem Details style (similar to Spring Boot's ProblemDetail).

```python
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class ErrorResponse(BaseModel):
    detail: str
    code: str | None = None

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(detail=exc.detail, code=getattr(exc, "code", None)).model_dump(),
    )
```

## Best Practices
- Always return structured errors, never raw exceptions in production.
- Use status codes correctly (400 for validation, 404 for not found, 409 for conflicts).
- Log full errors server-side, return minimal safe details to client.
- For async DB errors, catch and translate (e.g. IntegrityError -> 409).

Mirror the approach in the Java Spring Boot 4 error-handling docs for cross-stack consistency.