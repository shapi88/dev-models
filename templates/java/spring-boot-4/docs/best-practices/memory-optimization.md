# Memory Usage Reduction Strategies (Java 25 + Spring Boot 4)

**Last updated:** 2026-06-14

Running multiple services (especially after moving toward microservices) makes memory efficiency critical.

## Java 25 Specific Wins

- **Virtual Threads**: Dramatically reduce memory per concurrent request (no more 1MB+ stack per thread). Use them for I/O-bound workloads instead of platform threads.
- **Records**: Lower memory footprint than regular classes (no generated methods overhead in some cases).
- **Scoped Values**: More efficient context propagation than ThreadLocal (especially with virtual threads).
- Better escape analysis and JIT improvements in recent JDKs.

## Spring Boot 4 Configuration for Lower Memory

```yaml
spring:
  main:
    lazy-initialization: true          # Big win for startup + memory
  jpa:
    open-in-view: false                # Avoids unnecessary Hibernate session
  datasource:
    hikari:
      maximum-pool-size: 10            # Tune per service load (don't default to 10 blindly)
```

Use AOT / GraalVM native compilation where possible (Spring Boot 4 has excellent support).

## Practical Techniques

1. **Heap Sizing**
   - Set `-Xmx` explicitly (container-aware).
   - Use `-XX:+UseZGC` or Shenandoah for lower pause times on larger heaps.
   - Monitor with Spring Boot Actuator `/actuator/metrics/jvm.memory.used`.

2. **Reduce Object Allocation**
   - Reuse buffers where safe.
   - Use primitive collections (e.g. Eclipse Collections or fastutil) for hot paths.
   - Avoid autoboxing in high-throughput code.
   - Use `String.intern()` very carefully (or better, avoid).

3. **Spring Context Optimizations**
   - Component scanning: Be explicit with `@ComponentScan` base packages instead of broad scans.
   - Use `@ConditionalOn*` annotations aggressively.
   - Exclude unnecessary auto-configurations:
     ```java
     @SpringBootApplication(exclude = { DataSourceAutoConfiguration.class })
     ```

4. **Database & Caching**
   - Use second-level cache sparingly.
   - Prefer read-only transactions where possible.
   - Size your connection pools correctly (HikariCP defaults can be high).

5. **Observability Overhead**
   - Micrometer + tracing adds overhead — sample traces aggressively in production (`management.tracing.sampling.probability=0.1`).

## Monitoring & Tools

- Spring Boot Actuator + Prometheus + Grafana dashboards for memory.
- `jcmd <pid> VM.native_memory` or VisualVM / JDK Mission Control.
- For containers: `kubectl top pod` + cAdvisor.

## Target Numbers (Reference)

For a typical Spring Boot 4 REST service on Java 25:

- Idle: < 150-250 MB RSS
- Under load: < 512 MB – 1 GB (tune per workload)

If your services are consistently > 1 GB idle, investigate leaks or over-allocation.

---

See also the startup time optimization guide and the monolith-to-microservices migration guide (many small services amplify memory issues).