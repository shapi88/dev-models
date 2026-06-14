# Error Handling — Spring Boot 4

## Standard Approach: Problem Details (RFC 9457)

We return structured error responses using Spring's `ProblemDetail`.

Example response:

```json
{
  "type": "https://our-platform/errors/validation-error",
  "title": "Validation failed",
  "status": 400,
  "detail": "One or more fields are invalid",
  "instance": "/api/v1/orders",
  "errors": [
    {
      "field": "customerId",
      "message": "must not be blank"
    }
  ]
}
```

## Implementation Pattern

Create a `@RestControllerAdvice` that catches common exceptions and turns them into `ProblemDetail`.

Controllers should rarely throw raw exceptions to the client.

See the controller best practices for the expected controller behavior.

**TODO**: Add concrete code example of the advice class + custom error types.