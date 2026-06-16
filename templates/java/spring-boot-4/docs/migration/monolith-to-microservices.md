# Multi-Module Monolith to Microservices Migration Strategy (Java 25 + Spring Boot 4)

**Last updated:** 2026-06-14

This guide provides a practical, incremental strategy for extracting services from a well-structured multi-module monolith into independent microservices using **Java 25 + Spring Boot 4**.

## Prerequisites (Do These First)

Before attempting extraction:

1. Your monolith must be a **modular monolith** (see `architectures/monolith/v1/`).
   - Clear package/module boundaries using Maven/Gradle modules or strong package structure.
   - Use of ArchUnit or similar to enforce boundaries.
   - Bounded contexts identified via Domain-Driven Design (DDD).

2. Each module should already be independently testable and have its own data access layer (no direct cross-module entity sharing).

3. Observability (tracing, metrics, logging) and CI/CD must support multiple services.

4. You have identified a clear **first candidate service** based on:
   - High change frequency / team ownership
   - Independent scaling needs
   - Clear data ownership
   - Pain points in the monolith (deployment coupling, etc.)

**Rule:** Never start microservices extraction on a big-ball-of-mud monolith. Refactor to modular monolith first.

## Recommended Migration Approach: Strangler Fig Pattern + Incremental Extraction

### Phase 1: Prepare the Monolith for Extraction

- Introduce **anti-corruption layers** (facades) around the module you plan to extract.
- Use **ports and adapters** inside the module so the interface is stable.
- Add **feature flags** or routing logic at the edge (API Gateway or in the monolith controller) to decide whether to call local module or the future remote service.
- Extract the data model for the service into its own database schema (or prepare for separate DB).

### Phase 2: Create the New Microservice (Java 25 + Spring Boot 4)

1. Generate a new Spring Boot 4 project targeting **Java 25**.
2. Use the same package naming conventions as the monolith module for easy future moves.
3. Implement the service using the anti-corruption layer contracts.
4. Choose communication style:
   - **Synchronous** (REST/OpenFeign or gRPC) for simple queries.
   - **Asynchronous** (Spring Cloud Stream + Kafka/RabbitMQ or virtual threads + WebClient) for commands and eventual consistency.
5. Set up its own PostgreSQL / MongoDB database (see persistence docs).

### Phase 3: Data Migration Strategy

Common patterns (choose per bounded context):

- **Shared Database → Database per Service** (most common)
  - Initially keep shared DB but route writes through the new service.
  - Use change data capture (Debezium) or dual-write with outbox pattern.
  - Eventually split the schema/tables into a dedicated DB for the service.

- **Saga / Choreography** for distributed transactions.
- **CQRS** if read and write models diverge significantly.

**Important in Java 25 + SB4:**
- Use `@Transactional` carefully across services (you can't).
- Prefer event-driven with Spring's `@EventListener` or Spring Cloud Stream for loose coupling.
- Virtual threads can help with high-concurrency data sync jobs.

### Phase 4: Incremental Cutover (Strangler Fig)

- Route a small percentage of traffic to the new service (canary).
- Keep the monolith module as fallback for a period.
- Gradually increase traffic while monitoring.
- Once stable, remove the monolith implementation of that bounded context.
- Repeat for next service.

### Phase 5: Post-Extraction Cleanup

- Remove the old module from the monolith.
- Introduce service discovery / API Gateway if not already present.
- Add centralized configuration (Spring Cloud Config or Kubernetes ConfigMaps).
- Implement circuit breakers, retries, bulkheads (Resilience4j is excellent with SB4).
- Strengthen contract testing (Spring Cloud Contract or Pact).

## Communication Patterns in Extracted Services (SB4)

- Prefer **asynchronous events** for most business flows (reduces coupling).
- Use **Spring Boot 4's improved WebClient** + virtual threads for non-blocking calls when sync is required.
- For inter-service security: JWT or OAuth2 with Spring Security 6.

## Testing Strategy

- Contract tests between services (critical).
- The monolith's integration tests should continue to pass during transition.
- Use Testcontainers for each service's database in CI.

## Common Pitfalls to Avoid

- Distributed monolith (services that must deploy together).
- Shared database as the default.
- Synchronous calls creating a web of dependencies (death star).
- Ignoring eventual consistency from day one.
- Not having proper observability (distributed tracing with Micrometer + Zipkin/Jaeger is mandatory).

## Recommended Tooling with Java 25 + Spring Boot 4

- Spring Cloud 2023/2024 release train (compatible with SB4 + Java 25)
- Resilience4j
- Spring Cloud Stream (Kafka recommended)
- Debezium for CDC
- Kubernetes + Spring Cloud Kubernetes or plain K8s manifests
- GraalVM native images for some services (dramatically improves startup and memory)

## Timeline Expectation

For a typical medium-sized multi-module monolith:

- First service extraction: 4–8 weeks (including learning curve)
- Subsequent services: 2–4 weeks each once patterns are established

Start small. One service successfully extracted and running in production is worth more than a half-finished grand plan.

---

**Related sections:**
- `architectures/monolith/v1/`
- `architectures/microservices/v1/`
- `persistence/` (for data splitting strategies)
- Best practices for memory and startup time (these become even more important once you have many services)

Update this guide as your team gains real extraction experience.