# Handbook Naming & Versioning

This document defines how we organize content in the developer handbook (`dev-models`).

## Goals
- Make it obvious where to find current guidance.
- Make evolution visible (especially for frameworks like Spring Boot and architectural recommendations).
- Keep the structure simple enough for juniors to navigate on day one.

## Top-Level Organization

- `architectures/` — Reference models for system design (monolith, microservices, etc.)
- `spring-boot/`, `java/`, `javascript/`, etc. — Platform and language specific handbooks
- `api-design/` — Cross-cutting API design rules
- `onboarding/` — High-level guides for new developers
- `best-practices/` (when cross-cutting) — General rules that don't belong to one framework

## Versioning Rules

### Framework / Technology Versions
Use the major version as a directory:

```
spring-boot/4/
spring-boot/3/   # kept for migration reference
```

Inside these folders you document the APIs, patterns, and best practices that apply **specifically to that version**.

### Architectural Models
Use `v1/`, `v2/`, etc.:

```
architectures/microservices/v1/
architectures/microservices/v2/
```

Bump the version when the recommended model changes in a meaningful way (new patterns, different trade-off recommendations, etc.).

### Best Practices and Guides
- For stable guidance: keep a single file with a "Last updated" date and a small changelog at the top.
- For guidance that has had major shifts: create a new versioned subfolder or clearly mark "v1 (legacy)" / "current".

### File Naming
- Use kebab-case for files: `rest-controller-best-practices.md`
- Keep files focused. One topic per file is better than one giant document.

## Every Versioned Section Should Have

- A clear `README.md` or `overview.md`
- "Last updated" date
- Statement of what the version applies to
- Links to previous version when relevant

This structure lets a junior developer answer questions like:
- "What is the current way we structure microservices?"
- "How do we build REST APIs in Spring Boot 4 specifically?"
- "How has the recommended monolith model changed over time?"

See the root [plan.md](../plan.md) for more context on the overall vision.