# Microservices Architecture — Model v1

**Last updated:** 2026-06-14

## What is a Microservice?

A microservice is a small, independently deployable service that focuses on a single business capability. Each service owns its own data, can be developed and deployed independently, and communicates with other services over the network (usually via HTTP or messaging).

## Core Principles of This Model (v1)

1. **Single Responsibility** — One service = one bounded context.
2. **Independent Deployability** — You can release one service without touching others.
3. **Data Ownership** — Each service owns its database (no shared database).
4. **Autonomous Teams** — Small teams can own services end-to-end.
5. **Resilience & Observability** — Services must handle failures of other services gracefully.

## Typical High-Level Structure

```
order-service/
payment-service/
inventory-service/
notification-service/
api-gateway/
```

Each service usually follows its own internal monolith-like structure (see `architectures/monolith/v1/`), but is much smaller in scope.

## When to Choose Microservices (v1)

Only after you have **proven** the domain boundaries in a modular monolith first.

Good signals:
- Clear, stable bounded contexts
- Need for independent scaling (e.g. payment service has different load profile)
- Multiple teams that are blocked on each other's release cycles
- Regulatory or compliance reasons that require isolation

**Anti-patterns (avoid in v1):**
- Starting a greenfield project with 8 microservices
- "Distributed monolith" (services that must be deployed together)
- Premature optimization for scale that never materializes

## Communication Patterns

- **Synchronous**: REST / gRPC (use for simple request/response)
- **Asynchronous**: Events / messaging (Kafka, RabbitMQ, etc.) — preferred for most inter-service communication
- **API Gateway** (or BFF — Backend for Frontend) for external clients

## Major Challenges for Juniors

- Distributed transactions → use saga pattern or eventual consistency
- Service discovery & configuration
- Observability (distributed tracing is mandatory)
- Data consistency across services
- Versioning of contracts between services
- Increased operational complexity (more things to deploy, monitor, and debug)

## Recommended Starting Point (Even When Going Micro)

1. Start with a well-structured **modular monolith** (see monolith model).
2. Identify the first candidate for extraction using real usage data and team pain.
3. Extract one service at a time using strangler fig pattern.
4. Only then adopt full microservices tooling (service mesh, centralized logging, etc.).

## Version History

- **v1** (2026-06): Conservative, pragmatic model. Strong recommendation to prove boundaries in a monolith first.

---

See also:
- `architectures/monolith/v1/`
- Future: `architectures/microservices/v2/` (when we have more experience with event-driven patterns, new frameworks, etc.)

**Rule of thumb for juniors:** If you're not sure, start with the monolith model. Microservices are a scaling strategy for organizations and complexity, not a default.