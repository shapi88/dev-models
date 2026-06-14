# REST Controller Best Practices — Spring Boot 4

## Controller Responsibilities (Keep Them Thin)

A good controller in our model does **only** these things:

1. Receive the HTTP request and validate input (DTO + Bean Validation)
2. Delegate to an application service / use case
3. Translate the result into the appropriate HTTP response (including error cases)
4. Nothing else

**Bad** (business logic in controller):
```java
@PostMapping
public ResponseEntity<?> create(@RequestBody OrderRequest req) {
    // 30 lines of validation + calculations + repository calls...
}
```

**Good**:
```java
@PostMapping
public ResponseEntity<OrderResponse> create(@Valid @RequestBody OrderRequest req) {
    OrderResult result = orderService.createOrder(req);
    return ResponseEntity.status(HttpStatus.CREATED).body(OrderResponse.from(result));
}
```

## Use Records for DTOs

```java
public record OrderRequest(
    @NotBlank String customerId,
    @NotEmpty List<OrderItemRequest> items,
    @Valid AddressRequest shippingAddress
) {}
```

Records give you immutability, `equals`/`hashCode`, and clean JSON serialization for free.

## Error Handling — Use Problem Details (RFC 9457)

Spring Boot 4 + Spring 6 makes `ProblemDetail` the standard.

Create a `@RestControllerAdvice` that turns exceptions into proper `ProblemDetail` responses.

Never return raw stack traces or internal exception messages to clients.

See the error handling page (to be expanded).

## Versioning Your API

See `api/versioning.md` in this folder.

## Documentation

- Every public controller should have OpenAPI annotations (`@Operation`, `@ApiResponse`, etc.).
- Use meaningful example values.
- Keep the generated spec in sync with the code (we treat the code as the source of truth).

## Security

- Controllers should not contain security logic (use method security or filters).
- Always validate that the caller is allowed to perform the action on the specific resource (ownership checks belong in the service layer).

## Testing Controllers

- Prefer `@WebMvcTest` + MockMvc for controller slice tests (fast).
- Use `@SpringBootTest` + Testcontainers only for broader integration tests.
- Test both happy path and error cases (including validation errors).

## Summary Checklist for Every New Endpoint

- [ ] Input DTO is a record with proper validation annotations
- [ ] Controller is thin (delegates to service)
- [ ] Uses proper HTTP status codes
- [ ] Returns `ProblemDetail` on errors
- [ ] Has OpenAPI documentation
- [ ] Has at least one controller test

Follow these patterns and you will write code that is easy for the whole team (including future you) to maintain.

---

Related:
- `spring-boot/4/api/versioning.md` (planned)
- `spring-boot/4/best-practices/testing.md`
- `architectures/monolith/v1/` (module boundaries still matter inside the controller package)