# Plan: dev-models — Developer Handbook & Companion

**Target location:** `/Users/andreleitao/MyProjects/dev-models`

**Current state (as of this revision):** The directory contains only a legacy README.md (from a previous interpretation) and a `.git` repo. We will treat this as a fresh start for the correct vision.

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
  - Spring Boot 4 (new APIs, changes from 3.x, recommended patterns, migration notes)
  - Similar treatment for other high-demand stacks
- **API documentation & design** (REST/HTTP API guidelines, versioning strategies, OpenAPI examples, error handling, pagination, etc.)

### "Models" Interpretation
In this context, **"programming languages models"** refers to **reference models** and **handbook sections** per language/platform:
- Architectural reference models (monolith model, microservices model)
- Implementation models / patterns for that language
- Versioned framework guides

The repo is a **living knowledge base**, not a collection of runnable boilerplate projects (although small, focused example snippets or minimal "model" apps are welcome inside versioned sections).

**Target users:** Junior developers (and anyone ramping up on a new high-demand stack).

**High-demand platforms focus** (based on user's previous mention of languages + Spring Boot 4):
- Java (Spring Boot 4 as flagship)
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

### Recommended Directory Structure (with versioning)

```bash
dev-models/
├── README.md
├── plan.md
├── architectures/
│   ├── monolith/
│   │   └── v1/
│   │       ├── overview.md
│   │       ├── structure.md
│   │       ├── when-to-use.md
│   │       └── migration-to-microservices.md
│   └── microservices/
│       ├── v1/
│       └── v2/                    # updated model (new patterns, better boundaries, etc.)
│           ├── service-design.md
│           ├── communication.md
│           └── observability.md
├── spring-boot/
│   ├── 3/                         # reference / migration from
│   └── 4/                         # focus area (new API versions)
│       ├── README.md
│       ├── getting-started.md
│       ├── migration-from-3.md
│       ├── api/
│       │   ├── rest-controller-best-practices.md
│       │   ├── versioning.md          # API versioning strategies
│       │   ├── error-handling.md
│       │   └── openapi.md
│       ├── best-practices/
│       │   ├── security.md
│       │   ├── testing.md
│       │   ├── configuration.md
│       │   └── performance.md
│       └── examples/                  # small, focused code snippets (not full projects)
│           ├── rest-api/
│           └── event-driven/
├── java/
│   ├── best-practices/
│   │   └── general.md
│   └── spring-boot-4/                 # language-specific companion section
├── javascript/
│   └── best-practices/
│       └── api-design.md
├── python/
│   └── ...
├── api-design/                        # cross-cutting
│   ├── rest/
│   │   └── versioning-strategies.md
│   └── general/
│       └── best-practices.md
├── onboarding/
│   ├── junior-developer-guide.md
│   └── high-demand-platforms.md
└── docs/                              # meta
    └── contributing.md
```

### Versioning Rules (to document in the handbook itself)

- **Framework versions** (Spring Boot 4, etc.): Use the major version as a directory (`4/`, `3/`). Inside, you can have minor sections if needed.
- **Architectural models**: Use `v1/`, `v2/`. Bump when the recommended model fundamentally changes.
- **Best practices & instructions**: Version only when they evolve significantly (`best-practices/security/v2/` or just keep latest with a "Last updated" + changelog note). Prefer lightweight versioning here.
- **API documentation**: Tie to the producing framework version (Spring Boot 4 REST API patterns live under `spring-boot/4/api/`).

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
- **Spring Boot 4**: New features in 4.x, changed defaults, recommended project setup, controller/service patterns, configuration with the new approach, testing improvements, etc.
- **Best practices**: Concrete, enforceable rules ("We use records for DTOs", "All public APIs must have OpenAPI docs", "Use constructor injection", etc.).
- **API docs**: Consistent patterns for request/response, pagination, filtering, error codes, versioning (URL vs header), deprecation policy.

### Small code examples
Keep them minimal and focused. Put them under `examples/` inside the relevant versioned folder. Do **not** turn this repo into a giant collection of full starter projects (that's a different concern).

---

## Phased Rollout Plan

### Phase 1 — Foundation (MVP)
1. Update root `README.md` to clearly describe the handbook purpose.
2. Create the top-level folder structure as shown above.
3. Write the core architectural models:
   - `architectures/monolith/v1/`
   - `architectures/microservices/v1/` (or v2 if you already have strong opinions)
4. Create `spring-boot/4/` with:
   - Getting started / project setup
   - Migration notes from Spring Boot 3
   - First API section (REST best practices + versioning)
5. Add a strong `onboarding/junior-developer-guide.md`
6. Write `docs/contributing.md` and update this `plan.md` if needed.

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