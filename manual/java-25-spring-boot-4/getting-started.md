# Java 25 + Spring Boot 4 — Getting Started

**For junior developers**

## Recommended Project Setup (2026 model)

Use **Spring Initializr** (https://start.spring.io) with these settings:

- **Spring Boot**: 4.x (latest patch)
- **Java**: 25 (our current baseline)
- **Language**: Java
- **Packaging**: Jar

**Important**: Always select Java 25 when generating new projects for our platforms. Spring Boot 4 has excellent support for Java 25 features.
- **Language**: Java
- **Packaging**: Jar
- **Dependencies** (start minimal):
  - Spring Web
  - Spring Boot DevTools (dev)
  - Spring Data JPA + your DB driver
  - Validation
  - Spring Boot Actuator (always)
  - Micrometer Observation (observability)
  - Testcontainers (testing)

**Build tool**: Maven or Gradle (we currently standardize on Maven for most teams).

## Project Structure We Recommend

Follow the monolith model in `architectures/monolith/v1/`, adapted for Spring Boot 4:

```
src/main/java/com/company/platform/order/
├── OrderApplication.java
├── config/               # @Configuration classes, SecurityConfig, etc.
├── web/                  # Controllers + DTOs (input/output)
│   ├── OrderController.java
│   └── dto/
├── application/          # Use cases / services (orchestration)
│   └── OrderService.java
├── domain/               # Aggregates, entities, value objects, domain events
│   └── Order.java
├── infrastructure/       # Repositories, external clients, persistence adapters
│   └── persistence/
└── shared/               # Cross-cutting utilities
```

### Important Spring Boot 4 / Spring 6 Conventions

- Prefer **constructor injection** (no `@Autowired` on fields).
- Use **records** for DTOs and value objects where possible.
- Use **@RestControllerAdvice** + `ProblemDetail` (RFC 9457) for error responses.
- Virtual threads are enabled by default in many places — understand when they help.
- Configuration properties use `@ConfigurationProperties` + records (very clean in SB4).

## Running Locally

```bash
./mvnw spring-boot:run
# or
java -jar target/*.jar
```

Use `application-local.yml` + Spring profile `local`.

## First Things to Add After Initializr

1. Actuator endpoints (health, info, metrics)
2. Structured logging (JSON in production)
3. Correlation ID / trace propagation
4. Input validation on all DTOs
5. Basic security configuration (even if just "permit all" initially)

See the `best-practices/` and `api/` sections for details.

## Next Steps for Juniors

1. Read the monolith architecture model.
2. Implement a simple CRUD endpoint following the patterns in `api/rest-controller-best-practices.md`.
3. Add a test using `@SpringBootTest` + Testcontainers.
4. Read the error handling and API versioning pages.

---

Questions? Update this page or ask in the team channel. This handbook is meant to be improved by the people using it.