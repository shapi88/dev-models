# Migrating from Spring Boot 3 to Java 25 + Spring Boot 4 (Stub)

This page will contain the practical migration guide.

## High-Level Changes

- Java 21 baseline
- Changes in configuration property binding (records work great)
- AOT / native improvements
- Observability API changes (Micrometer Observation)
- Security configuration updates (Lambda DSL is preferred)
- Removal of deprecated items

## Recommended Migration Order

1. Update Java version + dependencies.
2. Run the application and fix compilation / startup errors.
3. Address configuration changes.
4. Update security configuration.
5. Adopt new observability patterns.
6. Clean up any remaining deprecations.

For detailed steps, see the official Spring Boot 4 migration guide + add platform-specific notes here.

**Status**: This is a placeholder. Real migration experience will be documented here as teams move to Spring Boot 4.