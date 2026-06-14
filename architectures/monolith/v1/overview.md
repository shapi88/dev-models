# Monolith Architecture — Model v1

**Last updated:** 2026-06-14  
**Applies to:** Most new projects and many existing high-demand platforms

## What is a Monolith?

A **monolith** is a single, cohesive application that contains all the business logic, UI (if any), and data access in one deployable unit.

All modules, services, and features are developed, built, tested, and deployed together.

## Typical Structure (Recommended Model)

```
my-app/
├── src/main/java/com/example/myapp/
│   ├── config/           # Spring configuration, security, etc.
│   ├── controller/       # REST controllers (thin)
│   ├── service/          # Business logic
│   ├── repository/       # Data access
│   ├── domain/           # Entities, value objects, domain events
│   ├── dto/              # Data transfer objects (input/output)
│   └── MyAppApplication.java
├── src/main/resources/
│   ├── application.yml
│   └── db/migration/     # Flyway / Liquibase scripts
├── src/test/
└── pom.xml (or build.gradle)
```

### Key Characteristics of This Model
- Single codebase and single database (usually)
- One deployment artifact (JAR/WAR)
- Shared database schema (with clear module boundaries inside the code)
- Simple local development and debugging
- Easier to reason about transactions and consistency

## When to Choose the Monolith Model (v1)

**Strongly recommended for:**
- New projects / startups / small-to-medium teams
- When you don't yet know the right service boundaries
- High-demand platforms where speed of delivery and simplicity matter more than independent scaling
- Teams with junior developers (lower cognitive load)

**Consider microservices instead when you have:**
- Very clear, stable domain boundaries
- Independent scaling or deployment requirements
- Multiple teams that need to move at different cadences
- Strong organizational reasons (different tech stacks, compliance boundaries, etc.)

## Trade-offs

**Advantages**
- Fast development velocity
- Simple deployment pipeline (one artifact)
- Easy to refactor across modules early on
- Lower operational complexity (one app to monitor, one database)
- Easier debugging and end-to-end testing

**Disadvantages**
- Can become a "big ball of mud" if boundaries are not enforced
- Scaling is all-or-nothing (you scale the whole thing)
- Technology lock-in (harder to introduce a new language for one part)
- Longer build/test times as the application grows
- Risk of deployment bottlenecks (one bad change can take everything down)

## Best Practices for Monoliths (v1)

1. **Enforce module boundaries** inside the monolith (packages + architecture tests — ArchUnit or similar).
2. Use a **clean/hexagonal/ports-and-adapters** style even inside a monolith.
3. Keep controllers thin — move logic to services or dedicated use-case classes.
4. Use a single database but organize schema by bounded context (schema prefixes or separate schemas).
5. Invest in good integration tests + contract tests early.
6. Make the monolith "modular monolith" ready — it should be easy to extract a service later if needed.

## Migration Path to Microservices

See `architectures/microservices/v1/migration-from-monolith.md` (to be written) for a pragmatic, incremental approach.

Common first extractions:
- Reporting / analytics
- Notification service
- File processing / heavy background jobs

## Version History of This Model

- **v1** (2026-06): Initial reference model focused on simplicity and junior developer onboarding.

---

**This is the current recommended monolith model for most new work on our high-demand platforms.** 

Always read the "when to use" section before starting a new project.