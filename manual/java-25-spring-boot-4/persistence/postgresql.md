# PostgreSQL with Spring Data JPA (Java 25 + Spring Boot 4)

## Configuration Example

```yaml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: appuser
    password: ${DB_PASSWORD}
    hikari:
      maximum-pool-size: 10
      connection-timeout: 30000
  jpa:
    hibernate:
      ddl-auto: validate          # Never use 'create' or 'update' in production
    properties:
      hibernate:
        dialect: org.hibernate.dialect.PostgreSQLDialect
        format_sql: true
    open-in-view: false
  flyway:
    enabled: true
    locations: classpath:db/migration
```

## Recommended Repository Pattern

```java
public interface OrderRepository extends JpaRepository<Order, UUID> {
    List<Order> findByCustomerId(String customerId);
    
    @Query("SELECT o FROM Order o WHERE o.status = :status")
    List<Order> findByStatus(@Param("status") OrderStatus status);
}
```

Use **projections** or **records** for read-only queries to reduce memory:

```java
public record OrderSummary(UUID id, BigDecimal total) {}
```

## Transactions & Best Practices

- `@Transactional` on service methods.
- Read-only transactions for queries: `@Transactional(readOnly = true)`.
- Use `EntityManager` directly only when necessary (performance or complex queries).

## Schema Management

We use **Flyway** (preferred) or Liquibase for all schema changes. Migrations live in `src/main/resources/db/migration`.

## Performance Tips (Java 25 + SB4)

- Use batch inserts/updates with `hibernate.jdbc.batch_size`.
- Enable second-level cache only after measuring (usually not needed).
- Use `fetch = FetchType.LAZY` and explicit joins.
- Consider Spring Data JPA + QueryDSL or jOOQ for complex queries.

See `best-practices/memory-optimization.md` for related techniques.