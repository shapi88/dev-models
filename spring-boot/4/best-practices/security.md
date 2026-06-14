# Security Best Practices — Spring Boot 4

## Core Principles

- Security is **not optional** and is not only the security team's job.
- Fail closed by default.
- Validate everything on the server (never trust the client).
- Least privilege.

## Spring Boot 4 / Spring Security 6+ Recommendations

- Use the new **Lambda DSL** for security configuration (much more readable).
- Prefer **method security** (`@PreAuthorize`) for business rules.
- Use `SecurityFilterChain` beans (multiple if needed).
- Enable CSRF where appropriate (most modern SPAs use token-based auth and can disable it for the API).

## Common Patterns We Enforce

1. All production endpoints require authentication unless explicitly marked public.
2. Use JWT or OAuth2 (we standardize on one primary mechanism per platform).
3. Never log sensitive data (passwords, tokens, PII).
4. Input validation + output encoding.
5. Rate limiting on public endpoints.

## For Juniors

When you add a new endpoint:
- Think "Who is allowed to call this?"
- Think "What data does this expose?"
- Add the authorization check in the service layer (not only in the controller).

See the main security configuration in your team's application for the current concrete setup.

---

More sections (input validation, secrets management, vulnerability scanning) will be added.