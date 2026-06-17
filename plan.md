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

## Execution Status: .grok Adaptation Phase (Previous)
- (Completed in prior step) Structural parity between .grok and .github achieved.

## Execution Status: gh600-Standards + SOLID + Clean Architecture + Genericity Phase (Current)
**Major updates performed:**
- `.github/guardrails.md` fully rewritten to match gh600-exam structure (Autonomy Matrix Levels 0-4, detailed Hard Stops table, Required Audit Trail, Rollback Procedures, Policy Enforcement Mapping, Review Schedule) + added explicit "SOLID Principles and Clean Architecture Mandate" as a project-specific extension (non-negotiable for agents; violations are hard stops with waiver process).
- `.github/copilot-instructions.md` fully rewritten to match gh600-exam (Default Posture: Read before write / Plan before code / Smallest diff; Autonomy Level table; MAY / MAY NOT lists; expanded Stop Conditions including SOLID/Clean Arch violation; Required Audit Trail; Sensitive-Path Reference; Rollback; World-Class Developer Mandate + SOLID/Clean Arch requirements; explicit note that the system is **generic for every project**).
- `.grok/guardrails.md` updated to mirror the new gh600-style guardrails (local adaptations noted, same autonomy, hard stops, SOLID/Clean Arch mandate, generic language).
- `.grok/grok-instructions.md` updated to mirror the new gh600-style copilot-instructions (local parity, added SOLID/Clean Arch and "generic for every project" language).
- `.grok/README.md` updated with clear "Generic gh600-Style" positioning, parity rule, key enhancements, and "How to Use in This (or Any) Project" adoption instructions.
- Created `.github/branch-protection.md` (full gh600-style documented settings with verification and restore commands).
- Created `.github/INCIDENT_RESPONSE.md` (full gh600-style runbook with severity, contain/investigate/update/post-mortem/verify steps, adapted for the generic agent system).
- Agent files (.github and .grok) already had strong Core Directives; the governance files now explicitly require agents to behave as "best developers in the world" enforcing SOLID + Clean Architecture in *every* plan/review/implementation.
- The changes remove or generalize most dev-models-specific language in the core governance, making the agent system portable.

All core files now align with gh600-exam best practices while elevating agent behavior with SOLID and Clean Architecture as first-class concerns, and positioning the entire setup as a generic, copyable asset for any project.

## Overall Project Status
- Agent scaffolding now at full gh600 standards with world-class developer principles (SOLID + Clean Architecture) baked in at the governance and prompt level.
- System is explicitly designed and documented as **generic for every project** (see README updates and plan).
- Supporting gh600 artifacts (branch-protection.md, INCIDENT_RESPONSE.md) added.
- Previous phases (templates/ separation, Python FastAPI module, prior .grok alignment) remain intact and benefit from the higher-quality agent governance.

Ready for broader use and extraction. Next recommended steps: Create `templates/agent-system/` as a clean, standalone reusable package with adoption guide; add remaining gh600 skills (multi-agent-planner, run-eval, triage-issue) and workflows; add evaluation baselines; update CODEOWNERS and other supporting files if missing.

## Phase: Adopt GitHub-600 (gh600-exam) Standards + SOLID + Clean Architecture for Generic, World-Class Agent Templates

### Vision
Transform the agent scaffolding in this repository (and extract it for reuse) so that:
- `.github/` and `.grok/` follow the **exact standards, guidelines, and best practices** established in `gh600-exam` (the reference "github-600" project).
- Every agent (Planner, Executor, Reviewer) behaves like one of the **best developers in the world**.
- Agents **relentlessly apply SOLID principles** and **Clean Architecture rules** in every plan, review, and implementation.
- The entire system is **generic and portable** — easily copyable to *any* project (not dev-models specific). dev-models will "eat its own dogfood" by using the generic templates for its own multi-language handbook and template work.

This makes the agent system a first-class, reusable "AI developer team" kit.

### Analysis of Current State vs. gh600-exam Best Practices
**gh600-exam strengths (to adopt/adapt):**
- **Guardrails.md**: Full Autonomy Matrix (Levels 0-4), explicit "Hard Stops" list (never touch workflows/, CODEOWNERS, copilot-instructions.md, etc.), required audit trails per action, rollback procedures, policy enforcement mapping, review schedule.
- **copilot-instructions.md**: "Read before write", "Plan before code", "Smallest diff", clear MAY/MAY NOT lists, Stop Conditions (7+), required audit trail, sensitive-path reference, rollback instruction.
- **project-memory.md**: Structured persistent context (repo identity, key files, conventions, autonomy constraints, evaluation baselines, approved MCP servers, state checkpoints, idempotency rule, ephemeral memory section that agents must auto-update).
- **branch-protection.md**: Documented, auditable settings + verification/restore commands.
- **INCIDENT_RESPONSE.md**: Full severity classification, step-by-step runbook (identify, contain, investigate, update controls, post-mortem, verify).
- Agents: Structured with frontmatter + very directive-driven prompts emphasizing research, planning, human hand-off, and safety.
- Skills: Declarative YAML with clear schemas, autonomy, triggers.
- Supporting: CODEOWNERS, PULL_REQUEST_TEMPLATE, ISSUE_TEMPLATE/agent-incident.md, dependabot, mcp-config, preToolUse, guardrails-check workflow, etc.
- Overall philosophy: Strong human-in-the-loop at Level 2, least privilege, auditability, "smallest safe change", explicit evaluation.

**Current dev-models state (gaps):**
- Has good partial alignment from previous phases (agents with Core Directives, guardrails, skills, copilot/grok-instructions, project-memory, some workflows).
- Still somewhat dev-models-specific (hard-coded references to "templates/java/spring-boot-4", "python/fastapi", "junior developers handbook").
- Lacks full gh600 artifacts: branch-protection.md, complete INCIDENT_RESPONSE.md, richer project-memory with evaluation baselines/MCP allowlist/idempotency/ephemeral sections, more skills (multi-agent-planner, run-eval, triage-issue), agent-eval workflow, etc.
- Agents are helpful for this repo but not yet "best developer in the world" with explicit, relentless SOLID + Clean Architecture mandates.
- .grok/ mirrors .github/ structurally but governance and prompts need deeper alignment to gh600.
- Not yet packaged as generic/reusable templates.

### Core Principles to Embed (Non-Negotiable for All Agents)
**"Best World Developers" Persona (add to every agent prompt):**
- You are a world-class software engineer who has mastered multiple paradigms.
- You **never** compromise on quality, even for speed.
- You default to **simplicity, clarity, and long-term maintainability**.

**SOLID Principles (enforced in every action):**
- **S**ingle Responsibility: Every class/module/function has one reason to change.
- **O**pen/Closed: Open for extension, closed for modification (use abstraction, composition, interfaces).
- **L**iskov Substitution: Subtypes must be substitutable for their base types without breaking behavior.
- **I**nterface Segregation: Many specific interfaces > one general-purpose one.
- **D**ependency Inversion: Depend on abstractions, not concretions. High-level modules do not depend on low-level modules.

**Clean Architecture Rules (enforced in every plan/review/implementation):**
- **Dependency Rule**: Source code dependencies must point only inward. Inner circles (Entities, Use Cases) know nothing about outer circles (Frameworks, UI, DB, External Services). Details (DB, UI, frameworks) depend on abstractions defined in inner circles.
- Entities contain business rules and are independent of frameworks.
- Use Cases orchestrate the flow of data to and from entities; they are the "application" layer.
- Interface Adapters convert data between use cases and external world (controllers, presenters, gateways).
- Frameworks & Drivers are the outermost layer (DBs, web frameworks, devices).
- When generating or reviewing code/docs:
  - Always draw or describe the dependency direction.
  - Push framework-specific details (Spring annotations, FastAPI routers, SQLAlchemy models) to the outermost layer.
  - Prefer ports/adapters, dependency injection, and interfaces.
  - Never let infrastructure (persistence, web, external APIs) leak into domain logic.
- For documentation/handbook: Explain concepts using Clean Architecture layers. When providing templates, show clear separation (e.g., domain/ vs adapters/ vs infrastructure/).

Agents must **call out violations** of SOLID or Clean Architecture in reviews and refuse to implement plans that would introduce them (or propose refactors to fix).

### Adaptation Strategy
1. **Adopt gh600 Structure & Governance Verbatim (adapted for genericity)**:
   - Copy/adapt `guardrails.md`, `copilot-instructions.md`, `project-memory.md`, `branch-protection.md`, `INCIDENT_RESPONSE.md` into `.github/`.
   - Create parallel versions in `.grok/` (local equivalents: `grok-guardrails.md`, `grok-instructions.md`, enhanced memory with same sections).
   - Add missing supporting files: CODEOWNERS (if not present), more ISSUE_TEMPLATEs (agent-incident), PULL_REQUEST_TEMPLATE enhancements, `templates/artifact-schema.json` or similar for plans/handoffs.
   - Add/enhance workflows: agent-multi-agent-planner, agent-eval, agent-issue-triage, full guardrails-check with scope-control + secret-scan.
   - mcp-config.json + preToolUse.json with explicit allow/deny lists.
   - Autonomy Level 2 as default everywhere, with clear escalation for Level 3/4.

2. **Make Everything Generic (Reusable Across Projects)**:
   - Extract core agent definitions, skills, instructions, guardrails, and memory into a **portable "agent-system" template** (e.g., under `templates/agent-system/` or as a standalone copy-paste package in the repo).
   - Use placeholders/variables in prompts and docs: `{{REPO_NAME}}`, `{{PRIMARY_LANGUAGES}}`, `{{FRAMEWORKS}}`, `{{ARCHITECTURE_STYLE}}`, `{{TEAM_CONVENTIONS}}`.
   - Remove or conditionalize dev-models-specific references (e.g., "Spring Boot 4 / FastAPI" become examples; core logic is "for whatever languages and frameworks this project uses").
   - Make skills like `review-pr`, `generate-docs`, `multi-agent-planner` project-agnostic. dev-models-specific skills (e.g., "generate-language-module") live in a project-specific overlay.
   - Provide clear "How to Adopt in Your Project" instructions in READMEs and plan.md (copy `.github/`, `.grok/`, customize the few project-specific sections in project-memory.md and instructions).
   - Both `.github/` and `.grok/` consume the same base templates so local and CI stay in sync.

3. **Infuse "Best World Developer" Behavior + SOLID + Clean Architecture**:
   - **Update all agent prompts** (in both .github/agents/ and .grok/agents/):
     - Add a permanent "World-Class Developer Mandate" section at the top of every persona.
     - In **PlannerAgent**: 
       - Research must include existing architecture boundaries.
       - Every plan **must** explicitly map proposed changes to SOLID principles and Clean Architecture layers (e.g., "This change keeps Use Cases independent of Spring Data / SQLAlchemy").
       - Output format addition: "SOLID/Clean Arch Compliance" checklist.
     - In **ReviewerAgent**:
       - Mandatory section in every review: "SOLID & Clean Architecture Assessment" (score each principle + specific violations + required fixes).
       - Reject or request changes for any violation.
     - In **ExecutorAgent**:
       - Only implement after confirming plan has proper layer separation and SOLID compliance.
       - When writing code, prefer abstractions, interfaces, dependency injection; push framework details outward.
       - For docs/handbook: Ensure explanations and templates demonstrate Clean Architecture.
   - Add to `guardrails.md` and `copilot/grok-instructions.md`:
     - "SOLID and Clean Architecture are non-negotiable. Any plan or change that violates them is a hard stop unless explicitly waived by human + documented rationale."
   - Add a dedicated skill: `architecture-review.yml` (enforces SOLID + Clean Arch on diffs).
   - Update project-memory.md (both .github and .grok versions) with:
     - Section on "Architectural Principles": List SOLID + Clean Architecture as team invariants.
     - Evaluation baselines that include architecture quality.

4. **Ensure Parity and Sync Between .github/ and .grok/**:
   - .grok/ must be a first-class local mirror (same file names where possible, same content structure, same rule enforcement).
   - Add a `sync-agents.sh` or note in plan.md for keeping them aligned.
   - Both must load the same "core agent personality" (SOLID/Clean Arch + gh600 guardrails) while allowing local vs remote tool differences (documented in each agent's "Execution Environment" section).

5. **Enhance for Multi-Project Genericity + Dev-Models Dogfooding**:
   - Create `templates/agent-system/` containing the canonical, parameterized versions of agents/, skills/, guardrails.md, *-instructions.md, project-memory.md template, etc.
   - dev-models uses these templates (with its own overrides for Java/Python handbook work).
   - Document "Adoption Guide for Any Project" (copy the templates/, customize 4-5 files: project-memory, instructions, guardrails paths, add your languages/frameworks).
   - Use the agents *inside* dev-models development (e.g., the Planner must produce plans that follow Clean Architecture for any new handbook section or template).

6. **Supporting Best Practices from gh600**:
   - Add `.github/branch-protection.md` (auditable settings + verification commands).
   - Add full `.github/INCIDENT_RESPONSE.md` (severity, contain/investigate/update/post-mortem).
   - Expand CODEOWNERS, PULL_REQUEST_TEMPLATE, ISSUE_TEMPLATE/agent-incident.md.
   - Add more skills (multi-agent-planner, run-eval, triage-issue) and workflows.
   - Add evaluation baselines in `evals/` (if not present) for agent quality, including architecture compliance.
   - Update dependabot, SECURITY.md, etc., to gh600 style where superior.

7. **Verification & Rollout**:
   - Enhance `guardrails-check.yml` to also validate SOLID/Clean Arch mentions in plans and agent prompts.
   - Add a one-time "architecture compliance" eval using the new skill.
   - Update plan.md and root README with adoption status.
   - After changes, run the agents on a small task (e.g., "plan a small improvement to the Python FastAPI template") and verify they apply the principles.
   - Create a migration PR checklist that includes "Agent prompts updated for SOLID/Clean Arch + gh600 parity".

### Risks & Mitigations
- **Over-generalization**: Some dev-models specifics (e.g., exact module paths) may still need project overlays — mitigate with clear "base + override" pattern in the templates.
- **Prompt bloat**: Keep the "best developer + SOLID/Clean Arch" section concise but mandatory.
- **Maintenance of two systems (.github + .grok)**: Treat the agent-system templates as the single source of truth.
- **Adoption friction for other projects**: Provide copy-paste instructions + a "minimal generic starter" in templates/agent-system/minimal/.

### Implementation Order (Prioritized)
1. Update `.github/guardrails.md`, `copilot-instructions.md`, add `branch-protection.md` and `INCIDENT_RESPONSE.md` to match gh600 (infuse SOLID/Clean Arch mandates).
2. Update `.github/agents/*.agent.md` with "best world developer + SOLID + Clean Architecture" sections (use gh600 agent style + new principles).
3. Do the exact parallel updates for `.grok/` (guardrails, grok-instructions, agents, memory, add config files).
4. Generalize skills (add architecture-review skill; make existing skills use placeholders).
5. Create `templates/agent-system/` with the canonical generic versions (README with adoption guide).
6. Expand workflows, add missing skills from gh600, update project-memory.md in both locations with evaluation baselines and architectural principles.
7. Update plan.md (this section), root README, and any handbook docs that reference the agent system.
8. Add CODEOWNERS/branch protection docs if missing; enhance guardrails-check.
9. Test: Have Planner/Reviewer/Executor run on a task involving both Java and Python modules and a new generic improvement; verify they cite SOLID/Clean Arch.
10. Document how other projects (outside dev-models) can adopt the system.

This phase elevates the agent system from "helpful for this handbook repo" to "a portable, professional-grade AI developer team that any project can use, with world-class engineering principles baked in at the prompt and governance level."

See also the earlier "Phase: Adapt .grok..." section — this new phase builds directly on that structural parity work.
