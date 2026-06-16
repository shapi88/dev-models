# dev-models

**Developer Manual + Multi-Language / Multi-Framework Templates**

Reference modules:
- Java 25 + Spring Boot 4 (templates/java/spring-boot-4/)
- Python 3 + FastAPI (templates/python/fastapi/)

Includes cross-cutting architectures, onboarding, and full agent scaffolding (.github/ + .grok/).

A practical, versioned **Developer Manual** focused on **Java 25 + Spring Boot 4**, architectural models, best practices, and API design.

Goal: Help junior developers get a fast, reliable upside on the learning curve on high-demand enterprise platforms (especially those using modern Java + Spring Boot).

## What "models" means here

In this repository, **models** = reference models and guides:

- Architectural models (Monolith, Microservices, and their evolution over time)
- Implementation patterns and best practices for specific platforms
- Versioned framework handbooks (especially Spring Boot 4 and its new APIs)

Everything is structured so you can quickly find "the current recommended way" and see how it changed from previous versions.

## Focus Areas

- **Architectures**: Monolith vs Microservices (trade-offs, structure, when to use, migration)
- **Spring Boot 4** (and other major versions): new APIs, migration guides, recommended patterns
- **Best practices**: Coding, testing, security, API design, configuration, observability, etc.
- **API design & documentation**: REST guidelines, versioning strategies, error handling, OpenAPI usage
- Per-language companions for high-demand stacks (Java, JavaScript/TypeScript, Python, Kotlin, ...)

## Quick Navigation

```bash
# Architectural models
architectures/monolith/v1/
architectures/microservices/v1/

# Spring Boot 4 (current focus)
spring-boot/4/
spring-boot/4/api/
spring-boot/4/best-practices/

# Cross-cutting
api-design/rest/versioning.md
onboarding/junior-developer-guide.md
```

See the detailed structure and versioning rules in the plan:

- [plan.md](plan.md)
- (Future) docs/naming-and-versioning.md

## Current Content (Early Bootstrap)

- **Architectures**
  - Monolith model v1
  - Microservices model v1
- **Spring Boot 4**
  - Getting started for juniors
  - REST controller best practices
  - API versioning strategies
  - Basic security best practices
  - Error handling (stub)
- **Onboarding**
  - Junior developer guide with recommended reading order
- **Naming & Versioning rules** documented in `docs/naming-and-versioning.md`

This is intended to be a living handbook.

## Contributing

See [plan.md](plan.md) for the current rollout phases and content guidelines.

Core rule: Every major section that can evolve (architectures, framework versions, important best practices) should be versioned in the directory structure.

---

**Repo:** `/Users/andreleitao/MyProjects/dev-models`  
**Full plan & decisions:** [plan.md](plan.md)