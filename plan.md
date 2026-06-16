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

## Phase: Adapt .grok to Use the Same Rule Set Structure and Strategy as .github

### Current State Analysis
- `.github/` follows the mature gh600-exam pattern:
  - `agents/*.agent.md`: Strict YAML frontmatter (`name`, `description`, `tools: [...]`), followed by rich, structured Markdown (`# Title`, detailed persona, `## Core Directives` with numbered rules, research requirements, output formats, `## Hard Stops`, `## Hand-off Protocol`).
  - `skills/*.yml`: Consistent schema with `name`, `description`, `autonomy_level`, `trigger` (GitHub event-based), `input_schema` (typed objects with descriptions), `output_schema`.
  - Supporting governance: `guardrails.md` (hard/soft rules), `copilot-instructions.md` (standing orders), `project-memory.md`, workflows that invoke skills.
- `.grok/` (intended for local Grok TUI, CLI, and local agent execution) is currently lighter and inconsistent:
  - `agents/executor.agent.md`: Has frontmatter but uses "LocalExecutor" naming, shorter/less structured body (no Core Directives section, no hand-off, minimal rules).
  - `skills/generate-language-module.yml`: Flatter keys, no rich descriptions or typed schema like the .github counterpart.
  - Missing full governance parity (`guardrails.md` is only in .github, no local equivalent instructions).
- Result: Agents/skills developed for one environment may behave differently or be harder to maintain in the other. This breaks the "same rule set" goal for a repo that is itself about consistent templates across languages.

### Goals of Adaptation
- **Full structural parity**: .grok files must be drop-in compatible in format with .github so the same agent "personality" and skill definitions can be loaded locally or in CI with identical behavior and safety rules.
- **Strategy alignment**: Local agents must follow the exact same "thinking process" (research first, structured output, hard stops on protected files like .github/.grok, consistency enforcement across java/python modules) as their CI counterparts.
- **Local vs CI differentiation only where necessary**: GitHub-specific `trigger` fields can be optional or local-only (e.g., "manual" or "cli-invoked"). Local tools can map (write_to_file instead of GitHub write actions).
- **Benefits for dev-models**:
  - Reliable local generation of new modules (e.g., "add Rust + Axum template" using the exact same planning/review rules the PR reviewer agent would apply).
  - Easier maintenance: Edit once, the rule set applies everywhere.
  - Better support for the Grok Build TUI / local workflows mentioned in the system context.
- **Non-goals**: Do not duplicate every workflow file into .grok; workflows are CI-specific. Focus on agents + skills + shared governance.

### Detailed Adaptation Plan

1. **Standardize Agent File Format in .grok/agents/**
   - Update all existing .agent.md files (executor, and add planner/reviewer if missing) to use **exact same frontmatter** as .github:
     ```yaml
     ---
     name: ExecutorAgent   # Consistent naming (not "LocalExecutor")
     description: "..."
     tools:
       - write_to_file
       - ...
     ---
     ```
   - Rewrite the Markdown body to mirror structure:
     - `# Executor Agent`
     - Detailed role paragraph (adapt for local: "You execute file changes directly on the local filesystem using the Grok tools...").
     - `## Core Directives` (numbered list):
       - Read research from templates/java/... and templates/python/... before acting.
       - Enforce module separation and mirroring (FastAPI docs must have the same sections as Spring Boot 4).
       - Use structured output when generating plans or code.
       - Hard stops on modifying .github/ and .grok/ without plan approval.
     - `## Execution Protocol` (local version of Hand-off): After planning, directly apply changes or output a patch for review. Log all actions.
   - Create any missing agents in .grok/ by direct adaptation/copy of .github versions (with local tool mappings).

2. **Standardize Skill File Format in .grok/skills/**
   - Update existing skills (generate-language-module.yml) and create new ones to use the **full .github schema**:
     ```yaml
     name: generate-language-module
     description: >
       Long multi-line description explaining purpose, mirroring requirement, and output expectations.
     autonomy_level: 1
     # trigger: omitted or made local-only (e.g. "cli" or "manual-invocation")
     input_schema:
       language:
         type: string
         description: "..."
         required: true
     output_schema:
       plan: string
       files_to_create: list
     ```
   - Add local-friendly skills if useful (e.g., "local-review-module-consistency", "sync-agent-definitions").
   - Keep descriptions verbose and strategy-focused (same as .github).

3. **Add Parallel Governance Files to .grok/**
   - Create `.grok/guardrails.md` (copy/adapt the .github version; emphasize local file system safety and "run plans through local planner first").
   - Create `.grok/grok-instructions.md` (local equivalent of copilot-instructions.md — standing orders for local Grok sessions).
   - Enhance `.grok/memory/project-memory.md` (already exists) with explicit references to the rule set: "When acting, always follow the Core Directives defined in .grok/agents/*.agent.md and the guardrails in this file."
   - Add `.grok/config/preToolUse.json` and `mcp-config.json` if the local Grok supports them (for tool guards and server config).
   - Update `.grok/README.md` to explicitly state: "This directory uses the **exact same rule set structure and strategy** as .github/ for maximum consistency between local development and CI."

4. **Strategy and Behavioral Alignment**
   - **Core Strategy**: Agents must always (a) research existing modules first, (b) enforce mirroring between frameworks, (c) produce structured plans before execution, (d) respect hard stops on agent config files.
   - Document in both guardrails files: "The same agent definitions and skill schemas are authoritative for both environments. .grok/ is the local runtime view; .github/ is the CI/runtime view."
   - Add a note or small helper (e.g., in docs or a script) about keeping them in sync (e.g., "symlink or copy-on-change for shared persona logic").
   - For local invocation: The TUI/CLI should be able to load `.grok/agents/*.agent.md` and `.grok/skills/*.yml` using the identical parser as the GitHub workflows.

5. **Implementation Steps (Recommended Order)**
   1. Update all .grok/agents/*.agent.md files to full frontmatter + Core Directives structure (use .github versions as templates).
   2. Standardize .grok/skills/*.yml files to full schema + rich descriptions.
   3. Create missing governance files in .grok/.
   4. Update .grok/README.md with alignment statement and usage instructions for local Grok.
   5. Add a short "Agent Development" section to plan.md and the root README explaining the dual .github / .grok setup.
   6. Test locally: Invoke a .grok agent (via whatever local mechanism) on a task like "plan addition of a new module" and verify it follows the same rules the .github reviewer would.
   7. (Optional) Add a CI check that verifies structural parity between the two directories (e.g., same agent names, similar schema).

6. **Risks / Considerations**
   - Local tools differ (file system vs GitHub API) — document the mapping in each agent's directives.
   - Over-syncing: Keep GitHub-specific fields out of .grok skills.
   - Maintenance burden: The plan above includes a note on sync strategy.

This phase ensures that whether an agent is "thinking" locally in the Grok environment or running in a GitHub workflow, it applies the **identical rule set** (research → structured plan → safe execution → mirroring enforcement) to tasks like maintaining the multi-framework templates in this repo.

## Next Actions After This Plan Section
- (Executed) File updates for .grok/ completed to achieve parity with .github/.

## Execution Status: .grok Adaptation Phase
- Updated .grok/agents/executor.agent.md to full ExecutorAgent structure matching .github/ (with local tool focus).
- Added .grok/agents/planner.agent.md and reviewer.agent.md (direct adaptation of .github/ versions, preserving Core Directives, Hard Stops, Hand-off Protocol).
- Updated .grok/skills/generate-language-module.yml to full schema with rich description and typed input_schema (matching .github/).
- Added .grok/skills/review-pr.yml and generate-docs.yml for completeness (local-adapted).
- Created .grok/guardrails.md (adapted from .github/ for local FS emphasis).
- Created .grok/grok-instructions.md (local version of copilot-instructions.md).
- Enhanced .grok/memory/project-memory.md with explicit rule set references.
- Updated .grok/README.md to document the "exact same rule set structure and strategy" alignment.
- Added .grok/config/ with mcp-config.json and preToolUse.json (mirroring reference structure).
- All changes ensure local Grok agents use identical frontmatter, directives, schemas, guardrails, and strategy (research → structured plans → enforce module mirroring → hard stops) as CI agents.

The dual setup (local .grok/ + CI .github/) is now aligned for consistent agent behavior across the dev-models repo (templates for Spring Boot 4 / Python FastAPI, etc.).

## Overall Project Status
- Agent scaffolding (.github/ + .grok/) complete and parity achieved.
- Templates/ structure established with Java and Python modules.
- All prior phases executed (see status updates above).

Ready for use/maintenance. Next suggested: expand content or add more skills/workflows.
