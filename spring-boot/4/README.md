# Spring Boot 4 — Handbook

**Status:** Current recommended platform version (as of 2026)

This section documents how we use **Spring Boot 4** on our high-demand platforms, including new APIs, changes from Spring Boot 3, best practices, and concrete examples.

## Why Spring Boot 4?

Spring Boot 4 brings several important improvements relevant to junior developers and production systems:

- Java 21 baseline (virtual threads, improved records, pattern matching)
- Spring Framework 6.2 improvements
- Better AOT / GraalVM support
- Improved observability (Micrometer Observation)
- Modern configuration and testing defaults
- Stronger security posture out of the box

## Structure of This Handbook

- [Getting Started](getting-started.md)
- [Migration from Spring Boot 3](migration-from-3.md)
- [API Layer](api/)
  - REST controller best practices
  - API versioning strategies
  - Error handling & problem details
- [Best Practices](best-practices/)
  - Security
  - Testing
  - Configuration & profiles
  - Performance & virtual threads
- [Examples](examples/)

## Versioning Note

This entire `spring-boot/4/` directory represents the **current model** for Spring Boot 4.

When Spring Boot 5 (or significant 4.x changes) arrives, we will create `spring-boot/5/` and keep `4/` for reference and migration guidance.

---

**New to Spring Boot?** Start with [Getting Started](getting-started.md) and the junior onboarding guide in `onboarding/`.