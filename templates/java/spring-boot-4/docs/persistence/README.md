# Persistence & Data Access (Java 25 + Spring Boot 4)

This section covers how to work with relational and NoSQL databases in our Java 25 + Spring Boot 4 applications.

## General Principles

- Prefer Spring Data repositories over raw JDBC/Hibernate when possible.
- Always use constructor injection for repositories and services.
- Keep persistence concerns isolated (use the ports & adapters style from the monolith architecture).
- Transactions: Use `@Transactional` at the service/use-case layer, not in repositories or controllers.
- Prefer immutable records for DTOs and projection results.

## Available Guides

- [PostgreSQL with Spring Data JPA](./postgresql.md)
- [MongoDB with Spring Data MongoDB](./mongodb.md)
- [General SQL / JDBC Best Practices](./sql-jdbc.md)

## Common Recommendations Across Databases

- Use connection pooling (HikariCP is the default and recommended).
- Enable statement caching where supported.
- Use read replicas for reporting queries when available.
- Implement proper timeout and retry policies (especially important in microservices).
- For multi-module monoliths or microservices: each bounded context owns its data.

See the monolith-to-microservices migration guide for data splitting strategies.