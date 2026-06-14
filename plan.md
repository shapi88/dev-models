# Plan: dev-models — Developer Manual (Java 25 + Spring Boot 4 Focus)

**Target location:** `/Users/andreleitao/MyProjects/dev-models`

**Current state (as of this revision):** Handbook structure with architectures and Spring Boot 4 content exists. This revision checks the plan against the new requirements and reorganizes for a proper **Developer's Manual** centered on **Java 25 + Spring Boot 4**.

The previous plan was solid for a general handbook. This update:
- Makes **Java 25 + Spring Boot 4** the flagship platform (high-demand enterprise stack).
- Rebrands the main deliverable as a "Developer Manual".
- Reorganizes the folder structure for better navigability as a manual (clear chapters, TOC-friendly).
- Updates all references, versioning, and content guidelines for Java 25 baseline.

---

## Corrected Vision & Goals

The user wants a **Developer Handbook** (primarily a collection of Markdown files) that serves as a **practical companion / onboarding accelerator** for junior developers.

### Core Purpose
- Flatten the learning curve when joining or working with **high-demand platforms**.
- Provide quick, reliable reference material instead of hunting through scattered docs, wikis, or outdated Confluence pages.
- Focus on **"how we do things here"** — architectural models, best practices, and concrete instructions.

### Key Content Themes (from user)
- **Instructions** and guides (getting started, common workflows)
- **Architectural models**:
  - Monolith architectures (when to use, structure, trade-offs, migration paths)
  - Microservice architectures (service boundaries, communication, deployment, observability)
- **Best practices** (coding standards, testing, security, performance, deployment, documentation, etc.)
- **Versioned framework / API documentation**, with strong emphasis on modern versions:
  - **Java 25 + Spring Boot 4** (new APIs in both Java and Spring Boot, recommended patterns, migration notes, Java 25 features like improved Virtual Threads, Records, Pattern Matching)
  - Similar treatment for other high-demand stacks
- **API documentation & design** (REST/HTTP API guidelines, versioning strategies, OpenAPI examples, error handling, pagination, etc.)

The manual is specifically adapted for developers working on platforms using **Java 25 and Spring Boot 4** as the primary high-demand technology stack.

### "Models" Interpretation
In this context, **"programming languages models"** refers to **reference models** and **handbook sections** per language/platform:
- Architectural reference models (monolith model, microservices model)
- Implementation models / patterns for that language
- Versioned framework guides

The repo is a **living knowledge base**, not a collection of runnable boilerplate projects (although small, focused example snippets or minimal "model" apps are welcome inside versioned sections).

**Target users:** Junior developers (and anyone ramping up on a new high-demand stack).

**High-demand platforms focus** (based on user's previous mention of languages + Spring Boot 4):
- **Java 25 + Spring Boot 4** (primary flagship — this is the main focus of the manual)
- JavaScript/TypeScript
- Python
- Kotlin (often paired with Spring or Android)
- Others as needed (C# / Go / etc. can be added later)

---

## Recommended Repository Name

The directory name `dev-models` can be kept, with "models" re-interpreted as:

> **Reference models, architectural models, and versioned knowledge models** for developers.

**Rationale for keeping it:**
- Already exists
- Short and professional
- "Models" works well for architectural models + best-practice models

**Better alternative names (if you want to rename the repo/directory later):**
- `developer-handbook`
- `dev-companion`
- `platform-handbook`
- `onboarding-models` (still uses "models")
- `dev-knowledge-base`

For now, we will use `dev-models` and update the README + plan to clearly explain the meaning.

---

## Recommended Name Structure & Versioning

This is the most important part of the user's request.

### Overall Philosophy
- **Handbook-first**: Content lives in clear Markdown files and folders.
- **Versioning is mandatory** for anything that changes with framework/API releases (Spring Boot 4 vs 3, new API versions, evolving architecture recommendations).
- Use **directory-based versioning** so readers can see the evolution and easily compare versions.
- Prefer **framework major versions** as top-level version segments when they introduce significant API or paradigm shifts (e.g. `spring-boot/4/`).
- Use **vX.Y** or calendar-ish versions for architecture models and best practices when they evolve independently.

### Recommended Directory Structure (with versioning) — Reorganized as a Developer Manual

To make this feel like a real **Developer's Manual**, we introduce a top-level `manual/` folder. This acts as the main book-like container with clear chapters.

```bash
dev-models/
├── README.md                          # High-level repo overview
├── plan.md
├── manual/                            # The Developer Manual (main content)
│   ├── README.md                      # Manual title page + Table of Contents
│   ├── getting-started/
│   │   └── index.md
│   ├── architectures/
│   │   ├── monolith/
│   │   │   └── v1/
│   │   │       ├── overview.md
│   │   │       └── ...
│   │   └── microservices/
│   │       └── v1/
│   │           └── overview.md
│   ├── java-25-spring-boot-4/         # Flagship section (Java 25 + Spring Boot 4)
│   │   ├── README.md                  # Section overview + what's new in Java 25 + SB4
│   │   ├── getting-started.md
│   │   ├── migration-from-spring-boot-3.md
│   │   ├── api-development/
│   │   │   ├── rest-best-practices.md
│   │   │   ├── versioning.md
│   │   │   └── error-handling.md
│   │   ├── best-practices/
│   │   │   ├── security.md
│   │   │   ├── testing.md
│   │   │   └── configuration.md
│   │   ├── java-25-features/          # Specific Java 25 integration (Virtual Threads, Records, etc.)
│   │   └── examples/                  # Focused snippets
│   ├── api-design/                    # Cross-cutting
│   │   └── rest/
│   │       └── versioning-strategies.md
│   ├── other-platforms/               # For balance with other languages
│   │   ├── javascript-typescript/
│   │   └── python/
│   └── onboarding/
│       └── junior-developer-guide.md
├── docs/                              # Meta documentation
│   └── naming-and-versioning.md
└── ...
```

**Major reorganization benefits**:
- Everything a developer needs day-to-day lives under `manual/`.
- `java-25-spring-boot-4/` makes the Java 25 + SB4 focus explicit.
- Architectures remain cross-cutting but versioned.
- Easy to add "chapters" for other languages later.

### Versioning Rules (to document in the handbook itself)

- **Java + Framework versions** (Java 25 + Spring Boot 4): Use clear names like `java-25-spring-boot-4/`. For future major versions create `java-26-spring-boot-5/` etc. This makes the exact platform version the developer is targeting immediately obvious.
- **Architectural models**: Use `v1/`, `v2/`. Bump when the recommended model fundamentally changes.
- **Best practices & instructions**: Version only when they evolve significantly. Prefer lightweight "Last updated" + changelog notes inside files unless a major shift occurs.
- **API documentation**: Tied to the `java-25-spring-boot-4/` section. New major API changes in future Java/Spring versions get their own top-level versioned section.

Every versioned folder should contain a `README.md` or `overview.md` that states:
- What version of the platform/technology this covers
- When it was last updated
- Key changes vs previous version
- "This is the current recommended model"

This structure gives juniors a clear mental model:
> "For the new Spring Boot 4 world, look in `spring-boot/4/`."

---

## Content Guidelines

### Style
- **Junior-friendly**: Explain *why*, not just *what*. Use simple language first, then depth.
- Short, scannable Markdown files (use headings, lists, code blocks, callout boxes).
- Include diagrams (Mermaid is perfect for this repo — no external tools needed).
- Link to official docs but provide the "company/platform opinion" on top.

### What to include in sections
- **Architectures**: Trade-offs, when to choose monolith vs microservices, example high-level diagrams, common pitfalls for juniors.
- **Java 25 + Spring Boot 4**: New features in Java 25 (Virtual Threads, Records, Pattern Matching, etc.) + Spring Boot 4 APIs, recommended project setup using Java 25, controller/service patterns, configuration, testing with modern JUnit 5 / Testcontainers, and how Java 25 features integrate with Spring (e.g. virtual threads for web servers).
- **Best practices**: Concrete, enforceable rules ("We use records for DTOs", "All public APIs must have OpenAPI docs", "Use constructor injection", etc.).
- **API docs**: Consistent patterns for request/response, pagination, filtering, error codes, versioning (URL vs header), deprecation policy.

### Small code examples
Keep them minimal and focused. Put them under `examples/` inside the relevant versioned folder. Do **not** turn this repo into a giant collection of full starter projects (that's a different concern).

---

## Phased Rollout Plan

### Phase 1 — Foundation (MVP) — Current state + Reorganization
1. Update root `README.md` and create `manual/README.md` as the main Developer Manual entry point with Table of Contents.
2. Reorganize existing content into the new `manual/` structure (see recommended directory above).
3. Adapt all Spring Boot 4 content to **Java 25 + Spring Boot 4** (update getting-started, add Java 25 features section).
4. Keep core architectural models under `manual/architectures/`.
5. Ensure strong `manual/onboarding/junior-developer-guide.md`.
6. Update `docs/naming-and-versioning.md` and this `plan.md`.

### Phase 2 — Depth
- Expand best practices under each major section (security, testing, observability, deployment).
- Add language-specific companions for JavaScript, Python, Kotlin, etc., focused on their high-demand usage patterns.
- Cross-cutting `api-design/` section with more detail.
- Add more Spring Boot 4 API patterns (validation, security with Spring Security 6, reactive vs servlet, etc.).

### Phase 3 — Polish & Automation
- Add a simple script to generate a table of contents or "latest versions" index.
- Consider GitHub Pages / MkDocs / Docusaurus if the handbook grows very large (but start with plain Markdown + good READMEs).
- Add contribution workflow (templates for new sections).

---

## Open Questions & Decisions

1. **Primary language/platform focus?** Is Java + Spring Boot 4 the #1 high-demand platform this handbook targets, or do you want balanced coverage of JavaScript/Python/Kotlin from day one?
2. **Monolith vs Microservices depth**: How opinionated should the architecture models be? (e.g. "We prefer monolith until X scale" vs neutral comparison)
3. **API documentation scope**: Do you want full example OpenAPI specs, or just guidelines + small controller examples?
4. **Ownership**: Is this meant to be a personal reference that can later become a team/company standard, or purely personal?
5. **Versioning granularity for best practices**: Do you want to version every best-practice folder, or just note "current as of 2026-06" with a changelog at the top of files?
6. **Diagrams & visuals**: Preference for Mermaid (in-repo) or external images?

---

## Immediate Next Steps (after plan approval)

1. Replace the legacy root README with a clear handbook description.
2. Create the `architectures/` and `spring-boot/4/` skeletons with placeholder Markdown files.
3. Write the first substantial content (Monolith model + Microservices model + Spring Boot 4 getting-started + one API best-practice page).
4. Update this plan.md with any decisions from the questions above.
5. Commit the new structure + plan.md.

This revised plan directly addresses the user's clarification:
- Handbook / Markdown instructions focus
- Explicit architectural models (monolith + microservices)
- Best practices
- Versioned framework content (Spring Boot 4 as the concrete example)
- Goal of helping junior developers ramp up quickly on high-demand platforms

The name structure with versions is designed to be clear, browsable, and future-proof for new API/framework versions.

---

*This plan replaces the previous "project model templates" interpretation.*