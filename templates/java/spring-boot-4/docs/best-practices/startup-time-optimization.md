# Application Startup / Spin-up Time Reduction (Java 25 + Spring Boot 4)

**Last updated:** 2026-06-14

Fast startup is especially important in cloud / Kubernetes environments (scaling, rolling updates, FaaS-style workloads).

## Top Wins in Java 25 + Spring Boot 4

### 1. Lazy Initialization (Huge Impact)

```yaml
spring:
  main:
    lazy-initialization: true
```

This is the single biggest lever in most Spring Boot applications. Combine with `@Lazy` on specific heavy beans when full laziness causes issues.

### 2. GraalVM Native Images (AOT)

Spring Boot 4 has first-class AOT support.

```bash
./mvnw -Pnative native:compile
```

Expect startup times dropping from 5–15 seconds to < 100–300 ms.

**Trade-offs**: Longer build time, some reflection limitations (use `@RegisterReflectionForBinding`, etc.).

### 3. Classpath & Component Scanning

- Minimize dependencies in your `pom.xml` / `build.gradle`.
- Use explicit base packages:
  ```java
  @SpringBootApplication(scanBasePackages = "com.example.myapp")
  ```
- Avoid broad `@ComponentScan`.

### 4. Database & Infrastructure

- Use connection pool pre-warming or lazy connection acquisition.
- Defer Flyway / Liquibase migrations if possible (run them asynchronously or in a separate init container).
- For PostgreSQL/Mongo: use connection validation that doesn't block startup.

### 5. Java 25 Specific

- Virtual threads have almost zero creation cost compared to platform threads → reduces initialization of thread pools.
- Improved CDS (Class Data Sharing) and AOT compilation in the JDK.

## Recommended Spring Boot 4 Settings

```yaml
spring:
  main:
    lazy-initialization: true
    cloud:
      compatibility-verifier:
        enabled: false   # Can slow startup in some cases
  lifecycle:
    timeout-per-shutdown-phase: 30s
```

## Diagnostic Commands

```bash
# Measure startup time
time java -jar myapp.jar

# With detailed timing
java -Dspring.output.ansi.enabled=always -jar myapp.jar --debug
```

Use Spring Boot's `ApplicationStartup` (with `BufferingApplicationStartup`) to get bean creation timelines.

## Kubernetes Tips

- Set appropriate readiness/liveness probes (don't use startup probe as a crutch for slow apps).
- Use `startupProbe` for applications that legitimately take time.
- Consider sidecar or init containers for heavy setup work.

## Target Numbers

- JVM mode (Java 25 + SB4): < 3–5 seconds on modern hardware for a typical web service.
- Native mode: < 200–500 ms.

If your app takes > 10–15s, you have a problem that will hurt autoscaling and developer experience.

---

Cross-reference:
- Memory optimization guide (many techniques help both memory and startup).
- Monolith-to-microservices migration (each new service needs to start fast).