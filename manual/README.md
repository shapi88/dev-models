# Developer Manual

**Java 25 + Spring Boot 4 Edition**

This is the official **Developer Manual** for working on our high-demand platforms.

It is designed especially for junior developers to quickly get up to speed with the architectures, patterns, and APIs we use in production.

## Table of Contents

1. [Getting Started](./getting-started/)
2. [Architectures](./architectures/)
   - [Monolith Model v1](./architectures/monolith/v1/overview.md)
   - [Microservices Model v1](./architectures/microservices/v1/overview.md)
3. **Java 25 + Spring Boot 4** (Primary Platform)
   - [Overview](./java-25-spring-boot-4/README.md)
   - [Getting Started with Java 25 + Spring Boot 4](./java-25-spring-boot-4/getting-started.md)
   - [Migration from Spring Boot 3](./java-25-spring-boot-4/migration-from-spring-boot-3.md)
   - **Migration Strategies**
     - [Multi-Module Monolith to Microservices Strategy Guide](./java-25-spring-boot-4/migration/monolith-to-microservices.md)
   - [API Development](./java-25-spring-boot-4/api/)
     - [REST Controller Best Practices](./java-25-spring-boot-4/api/rest-controller-best-practices.md)
     - [API Versioning Strategies](./java-25-spring-boot-4/api/versioning.md)
     - [Error Handling](./java-25-spring-boot-4/api/error-handling.md)
   - [Best Practices](./java-25-spring-boot-4/best-practices/)
     - Memory Usage Reduction Strategies *(new)*
     - Application Spin-up Time Reduction Strategies *(new)*
   - [Persistence & Data Access](./java-25-spring-boot-4/persistence/)
     - PostgreSQL (JPA)
     - MongoDB
     - SQL / JDBC
   - [Java 25 Specific Features](./java-25-spring-boot-4/java-25-features/) *(coming soon)*
4. [API Design (Cross-cutting)](./api-design/)
5. [Onboarding for Junior Developers](./onboarding/junior-developer-guide.md)

## How to Use This Manual

- Start with the **Architectures** section to understand the big picture (monolith vs microservices).
- The **Java 25 + Spring Boot 4** chapter is the most detailed — this is our current primary high-demand stack.
- Use the versioned directories (`v1/`, `4/`) to see how recommendations evolve.
- Always check the "Last updated" dates and migration notes when moving between versions.

This manual uses a clear, version-aware directory structure so you always know which recommendations apply to the exact Java 25 + Spring Boot 4 platform you are targeting.

---

For repo organization and contribution rules, see the root [plan.md](../plan.md) and [docs/naming-and-versioning.md](../docs/naming-and-versioning.md).