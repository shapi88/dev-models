# API Versioning Strategies — Spring Boot 4

## Our Current Recommended Approach (v1)

We version our public APIs using **URL path versioning** as the primary mechanism:

```
/api/v1/orders
/api/v2/orders
```

### Why URL Path Versioning?

- Extremely explicit and visible in logs, proxies, API gateways, and client code.
- Easy to route and cache at the infrastructure level.
- Simple for juniors to understand and implement.
- Works well with OpenAPI (you generate separate specs per version or use one spec with versioned paths).

### When We Use Other Approaches

- **Header versioning** (`Accept: application/vnd.company.v1+json`): Only for very advanced cases or internal APIs where clients are under our control.
- **No versioning**: Only for truly internal, non-breaking utility endpoints (rare).

## How to Introduce a New Version

1. Create a new package or controller suffix: `v2.OrderController`
2. Copy the previous version and evolve it.
3. Deprecate the old version using `@Deprecated` + OpenAPI deprecation flag + clear timeline in docs.
4. Keep the old version running for the agreed deprecation period (usually 3–6 months for major platforms).

## Versioning Inside the Monolith or Microservice

Even inside a single service, we try to keep versioned controllers separate so the old version can be removed cleanly later.

## Best Practices

- Never change the behavior of an existing version (create a new one instead).
- Use semantic versioning for the API (`v1`, `v2`), not the internal implementation version.
- Document breaking changes prominently.
- Provide migration guides in this handbook (under `spring-boot/4/api/migration-guides/` when needed).

## Example Controller

```java
@RestController
@RequestMapping("/api/v1/orders")
public class OrderV1Controller { ... }

@RestController
@RequestMapping("/api/v2/orders")
public class OrderV2Controller { ... }
```

See `rest-controller-best-practices.md` for the full controller guidelines that apply to every version.

---

This page will be versioned alongside major changes to our API design philosophy.