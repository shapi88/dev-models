# MongoDB with Spring Data MongoDB (Java 25 + Spring Boot 4)

## Configuration

```yaml
spring:
  data:
    mongodb:
      uri: mongodb://localhost:27017/mydb
      auto-index-creation: false   # Create indexes explicitly in production
```

## Repository Example

```java
@Document(collection = "orders")
public record Order(
    @Id String id,
    String customerId,
    List<OrderItem> items,
    Instant createdAt
) {}

public interface OrderRepository extends MongoRepository<Order, String> {
    List<Order> findByCustomerId(String customerId);
}
```

## Key Differences from JPA

- No transactions across multiple documents by default (use MongoDB transactions for multi-document atomicity when needed).
- Embed vs Reference: Prefer embedding for data that is always loaded together.
- Use `@CompoundIndex` annotations or create them via Mongo shell / migration scripts.

## Recommended Patterns

- Use **records** for documents where possible.
- Projection queries for large documents.
- Change streams (with virtual threads) for reactive/event-driven use cases.

## Performance & Memory

- Avoid loading entire large documents when you only need a few fields.
- Use aggregation pipelines instead of pulling data into the application for heavy processing.
- Monitor with Spring Boot Actuator MongoDB metrics.

See the general persistence README and memory optimization guide.