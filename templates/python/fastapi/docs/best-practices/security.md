# Security Best Practices - FastAPI (Python 3)

## Core Recommendations (mirrors Java 25 + Spring Boot 4)

- Use FastAPI's built-in dependency injection for auth (OAuth2PasswordBearer, HTTPBearer, etc.).
- Prefer JWT or OAuth2 with libraries like python-jose or authlib.
- Validate all input with Pydantic (strict mode where possible).
- Use HTTPS only in production (enforce via middleware or reverse proxy).
- Rate limiting with slowapi or starlette middleware.
- CORS configuration (restrict origins).
- Never log sensitive data (passwords, tokens).

## Example Dependency

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # validate token...
    if not valid:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user
```

## Additional
- Use secrets management (e.g. via pydantic-settings + env or vault).
- SQL injection prevention via SQLAlchemy parameterized queries (see persistence docs).
- Regular dependency updates (use dependabot or renovate, configured in .github).

Cross-reference the Java security.md and the overall guardrails in .github/guardrails.md.