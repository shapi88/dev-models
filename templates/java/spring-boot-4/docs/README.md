# Java 25 + Spring Boot 4 — Handbook

**Status:** Current recommended platform (Java 25 + Spring Boot 4 as of 2026)

This is the **main chapter** of the Developer Manual. It documents how we build applications using **Java 25 + Spring Boot 4** on our high-demand platforms.

## Why Java 25 + Spring Boot 4?

- **Java 25** is the current baseline (Virtual Threads are fully mature, enhanced Records, powerful Pattern Matching, Scoped Values, etc.).
- **Spring Boot 4** + Spring Framework 6.x provides excellent integration with Java 25 features (especially virtual threads for web workloads, records as DTOs, and improved observability).
- This combination is one of the highest-demand enterprise stacks in 2026.

### Key Java 25 Features We Leverage with Spring Boot 4
- Virtual Threads (great for I/O-bound services — reduces thread-per-request overhead)
- Records (clean, immutable DTOs and domain objects)
- Pattern Matching (switch expressions, record patterns)
- Scoped Values (better alternative to ThreadLocal for request context)
- Improvements in the HTTP client and concurrency APIs

Spring Boot 4 works excellently on Java 25 (official support starts from Java 21, with Java 25 providing the best experience).

See the new sections on:
- Monolith → Microservices migration strategy
- Memory and startup time optimization
- Persistence APIs for PostgreSQL, MongoDB, and SQL/JDBC

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