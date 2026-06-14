# General SQL / JDBC Best Practices (Java 25 + Spring Boot 4)

Use this when you need more control than Spring Data JPA provides, or for very high-performance scenarios.

## Spring Boot 4 + Java 25 Recommendations

- Prefer `JdbcClient` (newer, fluent API) over classic `JdbcTemplate` in many cases.
- Use `NamedParameterJdbcTemplate` for readability.
- Virtual threads work very well with JDBC (blocking calls are cheap).

## Example with JdbcClient

```java
@Component
public class OrderJdbcRepository {

    private final JdbcClient jdbcClient;

    public OrderJdbcRepository(JdbcClient jdbcClient) {
        this.jdbcClient = jdbcClient;
    }

    public List<OrderSummary> findRecentOrders(int limit) {
        return jdbcClient.sql("SELECT id, total FROM orders ORDER BY created_at DESC LIMIT :limit")
                .param("limit", limit)
                .query(OrderSummary.class)
                .list();
    }
}
```

## Best Practices

- Always use parameterized queries (never string concatenation).
- Batch operations for bulk inserts/updates.
- Proper connection and statement timeouts.
- Use `try-with-resources` for manual resources.
- For very high throughput: consider R2DBC + virtual threads (reactive) or plain JDBC with virtual threads.

## When to Choose What

- **Spring Data JPA** → Most domain models, good developer productivity.
- **jOOQ** → Complex queries, type-safe SQL.
- **JdbcClient / JdbcTemplate** → Simple queries, maximum performance/control.
- **Spring Data MongoDB** → Document-oriented data, flexible schemas.

Combine them in the same application when appropriate (multi-database setups are common in microservices).