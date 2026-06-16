# Plan: dev-models — Developer Manual + Templates (Multi-Language / Multi-Framework)

**Location:** `/Users/andreleitao/MyProjects/dev-models`

## Reference Validation: gh600-exam/.github

I inspected `/Users/andreleitao/MyProjects/gh600-exam/.github` as requested.

### Summary of the Reference Structure (Validated)

This is a **mature, production-ready agent template** for AI-augmented development (optimized for Grok, Copilot, and multi-agent workflows):

**Core Components:**
- **agents/** (personas):
  - `planner.agent.md`, `executor.agent.md`, `reviewer.agent.md`
  - YAML frontmatter + detailed role instructions + allowed tools.
  - Planner: read-only analysis and planning.
  - Executor: can write files, run commands, create PRs.
  - Reviewer: code review focused.

- **skills/** (reusable, declarative task definitions in YAML):
  - `review-pr.yml`, `multi-agent-planner.yml`, `triage-issue.yml`, `generate-docs.yml`, `run-eval.yml`
  - Each defines: name, description, autonomy_level, trigger (GitHub event), input_schema, output_schema.
  - These are composable building blocks that agents/workflows can invoke.

- **workflows/** (GitHub Actions orchestration):
  - `agent-pr-review.yml`, `agent-multi-agent-planner.yml`, `agent-issue-triage.yml`, `agent-eval.yml`, `guardrails-check.yml`
  - Trigger on PRs, issues, etc., and call the skills/agents.

**Supporting Governance & Memory:**
- `copilot-instructions.md` / `copilot-memory.md` / `project-memory.md`: Standing orders and persistent context for AI assistants.
- `guardrails.md`, `preToolUse.json`, `mcp-config.json`: Safety, tool guards, MCP server config.
- `ISSUE_TEMPLATE/` (bug_report.md, feature_request.md, agent-incident.md)
- `PULL_REQUEST_TEMPLATE.md`
- `dependabot.yml`, `CODEOWNERS`, `branch-protection.md`, `SECURITY.md`, `INCIDENT_RESPONSE.md`

**Strengths:** Safe autonomy levels, human-in-the-loop (plans must be approved), event-driven, reusable skills, excellent for documentation-heavy or template-generation repos.

**Recommendation for dev-models:** Fully replicate this structure (adapted to "maintaining developer manual + generating language/framework templates").

## Enhancement Goals (Current Request)

1. **Add .github/ and .grok/ for agents template structure**
   - Mirror gh600-exam exactly in spirit.
   - Adapt for dev-models use cases: planning new handbook sections, generating FastAPI templates, reviewing docs, triaging "add Python module" issues, etc.
   - `.grok/` for repo-local equivalent of `~/.grok` (skills, agent defs, memory, configs that the local Grok TUI / CLI can load).

2. **Reorganize to separate by framework and language**
   - Current state: Heavy handbook content under `manual/`, with detailed Java 25 + Spring Boot 4 docs (including the recently added monolith-to-microservices migration, memory optimization, startup time, and persistence for Postgres/Mongo/SQL).
   - Introduce clear **templates/** or **frameworks/** separation.
   - Treat each language+framework as a "module" with its own template structure (code skeleton) + docs.

3. **Mirror Spring Boot template + docs for Python 3 + FastAPI**
   - Create equivalent depth:
     - getting-started.md (Python 3.12+/3.13 + FastAPI + uvicorn)
     - api/ best practices (Pydantic v2, dependencies, routers, etc.)
     - best-practices/ (memory with uvicorn/workers, startup time, async patterns)
     - persistence/ (SQLAlchemy + Postgres, async Mongo with Motor/Beanie, general SQL)
     - migration/ (reuse or adapt the monolith-to-microservices guide)
     - examples/ or actual minimal template project
   - Add real starter code skeleton for FastAPI (parallel to whatever "Spring Boot template structure" exists).

## Proposed New Top-Level Organization

```bash
dev-models/
├── .github/                     # Agent template (copied/adapted from gh600-exam)
│   ├── agents/
│   ├── skills/
│   ├── workflows/
│   ├── copilot-instructions.md
│   ├── project-memory.md
│   ├── guardrails.md
│   ├── ISSUE_TEMPLATE/
│   └── ...
├── .grok/                       # Local Grok / agent config (repo version of ~/.grok)
│   ├── agents/
│   ├── skills/
│   ├── memory/
│   └── config/
├── templates/                   # Framework + Language separated modules
│   ├── java/
│   │   └── spring-boot-4/       # Current detailed Java 25 + SB4 content + code template
│   │       ├── template/        # Actual minimal project skeleton (if not present)
│   │       └── docs/            # Or keep flat with the handbook files
│   └── python/
│       └── fastapi/             # NEW - mirrored structure
│           ├── template/        # Basic FastAPI project skeleton
│           │   ├── app/
│           │   │   ├── main.py
│           │   │   ├── dependencies.py
│           │   │   └── routers/
│           │   ├── pyproject.toml
│           │   └── Dockerfile
│           └── docs/            # Full parallel docs
│               ├── getting-started.md
│               ├── api/
│               ├── best-practices/
│               ├── persistence/
│               └── ...
├── manual/                      # Cross-cutting handbook content
│   ├── README.md
│   ├── architectures/           # Monolith v1, Microservices v1 (versioned)
│   ├── onboarding/
│   └── api-design/
├── docs/
│   └── naming-and-versioning.md
├── README.md
└── plan.md
```

This keeps cross-cutting material (architectures, general onboarding) separate while making each language/framework a self-contained "template module" with both code and docs.

## Implementation Phases

**Phase 1: Agent Scaffolding (High Priority)**
- Create `.github/` with agents/, skills/, workflows/ + key governance files (adapt from gh600-exam, customize names for "dev manual + template generation" tasks).
- Create `.grok/` with parallel structure.
- Add basic skills for:
  - "generate-new-language-module"
  - "review-handbook-section"
  - "update-persistence-docs"

**Phase 2: Reorganization**
- Introduce `templates/` directory.
- Move/adapt current `manual/java-25-spring-boot-4/` content into `templates/java/spring-boot-4/`.
- Ensure it is presented as the reference "Spring Boot template structure + docs".

**Phase 3: Python 3 + FastAPI Module (Mirror)**
- Create full parallel under `templates/python/fastapi/`.
- Docs to include (at minimum):
  - getting-started.md (Python 3.12+, FastAPI, uv or poetry, uvicorn)
  - api/ (best practices for routers, Pydantic, dependencies, versioning)
  - best-practices/ (memory optimization for FastAPI, startup time with uvicorn --reload vs workers, async patterns)
  - persistence/ (SQLAlchemy 2.0 + Postgres, async Mongo, general SQL)
  - migration/ (link to the cross-cutting monolith-to-microservices guide)
- Add a real minimal template project skeleton in `templates/python/fastapi/template/`.

**Phase 4: Polish**
- Update all README.md files and the main manual/README.md with new navigation.
- Update plan.md (this file).
- Add cross-references (e.g., architectures are shared).
- Ensure Java 25 + SB4 content remains the "reference implementation" of a complete module.

## Open Decisions

- How much real code vs docs in each template? (Recommendation: small, idiomatic skeleton + heavy docs.)
- Should architectures stay under manual/ or be duplicated/copied into each template?
- Do we want actual runnable "cookiecutter" style or just the documented folder structure?
- Future languages (after Python/FastAPI): JavaScript (Nest/Express), Kotlin, Go?

## Immediate Next Steps

1. Create `.github/` and `.grok/` (copy structure + adapt key files).
2. Reorganize into `templates/` + move Java module.
3. Create Python + FastAPI module (structure + key docs + skeleton).
4. Update READMEs + plan.md.
5. Commit.

This will turn dev-models into a first-class, agent-friendly, multi-language "developer models and templates" repository while preserving all the excellent handbook content already written.
## Status Update (Latest Implementation)

All items from the enhancement request have been executed:

- `.github/` and `.grok/` added with agent template structure (adapted from the validated gh600-exam reference).
- Project reorganized with clear `templates/` separation by language/framework.
- Java 25 + Spring Boot 4 content preserved under `templates/java/spring-boot-4/docs/`.
- Full parallel Python 3 + FastAPI module created under `templates/python/fastapi/` (docs + basic template skeleton).
- All relevant READMEs and TOCs updated.
- This plan.md documents the changes.

The repository is now in a much better state for "models" (templates + docs) per framework/language, with first-class support for agent-driven maintenance.

Next logical work: populate more real code in the Java template skeleton, add more Python FastAPI depth (e.g. full async SQLAlchemy example, testing patterns), or add a third language (e.g. TypeScript/Nest).
