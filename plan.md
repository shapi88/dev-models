# Plan: dev-models — Programming Languages Models (Developer Helper Repo)

**Target repo location:** `/Users/andreleitao/MyProjects/dev-models`

This document lives inside the repo it describes so it can be versioned, referenced, and followed during implementation.

## Vision & Goals
Create a clean, practical **developer helper repository** that organizes **"models"** for a specific set of technologies.

In this context, **"models"** = reusable reference assets a developer can quickly copy or consult:
- Recommended **project structures** and folder layouts (the "model" way to organize a project in that language).
- Small, complete **starter templates / boilerplates** (skeletons for CLI apps, libraries, web services, etc.).
- **Idiomatic reference implementations** and common patterns (data models, build setups, example code with explanations).
- For commands/ops: well-organized, version-aware "model" command sets, script templates, and manifest patterns.

**Exact technologies (per user):**
- javascript
- python
- java
- kotlin
- c
- unix (shell commands, scripting models, everyday one-liners and patterns)
- kubernetes (kubectl commands, manifest models, common operational patterns)

**Primary value:** A developer opens the repo, navigates by language (or unix/kubernetes), picks a clearly named and **versioned model**, and gets an immediately usable, high-quality starting point or reference.

The repo must feature a **recommended name structure that prominently includes versions**.

## Current Repo State (as of planning)
- Path: `/Users/andreleitao/MyProjects/dev-models`
- Current content: minimal `README.md` with title + one-line description ("Programming languages helper for developers").
- Opportunity: Use this plan to bootstrap the full professional structure on top of the existing skeleton.

## Recommended Repository Name
The directory is already `dev-models` — this is excellent and matches the primary recommendation from earlier analysis.

**Why it works:**
- Short, lowercase + hyphen (GitHub convention).
- "dev" = developer helper.
- "models" = directly uses the user's terminology.
- Neutral and extensible (easy to add more languages or tools later).

Keep the name as-is. Update the root `README.md` to be much richer once the structure is in place (this plan can drive that).

## Name Structure Recommendations (with Versions)
This is the key deliverable for the user's request.

### Principles
- Lowercase, hyphen-separated (`web-api`, `cli-tool`).
- **Versions are first-class and visible in directory names** using semantic versioning: `v1.0.0/`, `v2.1.3/`.
- Never version the top-level repo name (use Git tags/releases for the overall repo).
- Every model can evolve independently.

### Canonical patterns

**Languages:**
```
<language>/
  models/
    <model-purpose>/
      vX.Y.Z/               # <--- the versioned model lives here
        ...actual files & folders...
      README.md             # explains this model version
      CHANGELOG.md
```

Real examples:
- `python/models/web-api/v1.2.0/`
- `javascript/models/cli-tool/v2.0.0/`
- `java/models/library/v1.1.0/`
- `kotlin/models/microservice/v1.0.0/`
- `c/models/system-tool/v1.3.0/`

**Unix & Kubernetes (parallel, equally important sections):**
```
unix/
  models/                     # script "models" or script project structures
    backup-utility/
      v1.0.0/
    monitoring-script/
      v1.1.0/
  commands/                   # categorized references + model usage examples
    file-ops/
    process-mgmt/
    ...

kubernetes/
  models/                     # full small "model" deployments / patterns
    stateless-web/
      v1.2.0/                 # contains the manifests + supporting files + README
    stateful-service/
      v2.0.0/
  commands/
    kubectl/
    troubleshooting/
```

**Inside a versioned model directory (`vX.Y.Z/`):**
- This directory **is** the model. It should contain the real files/folders a developer would have in their project (so they can copy the whole `vX.Y.Z/` or its contents directly).
- Must include at minimum:
  - `README.md` (purpose, when to use, copy instructions, compatibility notes, rationale for structure/choices).
  - The actual code/config files laid out exactly as intended.
- Nice-to-have: `manifest.yaml` (light metadata for future scripting/indexing), `examples/`, `CHANGELOG.md` (per version or at model level).

**Recommended model purpose names (the middle segment):**
- `web-api`
- `cli-tool`
- `library`
- `fullstack-app` (JS)
- `microservice`
- `data-processor`
- `clean-architecture` (or `domain-model`)
- `simple-script` (for unix)

**Versioning rules (document these in `docs/naming-and-versioning.md`):**
- MAJOR (`v2.0.0`): Breaking layout or idiomatic changes.
- MINOR: Non-breaking additions or improvements.
- PATCH: Fixes, docs, small refinements, updated compatibility notes.
- Always record compatibility (target language version, K8s version range, shell, etc.).
- Old versions stay forever — they are historical references.

This structure makes navigation trivial:
- "I need a Python web project model" → `python/models/web-api/` → pick latest `vX.Y.Z/`.
- "I need current Kubernetes deployment patterns" → `kubernetes/models/stateless-web/v1.2.0/`.

## Recommended Directory Structure
Language-first organization (as requested), with clear parallel sections for the additional unix + kubernetes material.

Proposed layout (create this on top of the existing minimal dir):

```
dev-models/
├── README.md                     # (expand the existing one)
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── plan.md                       # This document (self-hosting the plan is nice)
├── languages/                    # wrapper (optional but clear) OR put language dirs at root
│   ├── python/
│   │   ├── README.md
│   │   └── models/
│   │       ├── web-api/
│   │       │   ├── v1.0.0/
│   │       │   ├── v1.1.0/
│   │       │   └── v1.2.0/
│   │       ├── cli-tool/
│   │       │   └── vX.Y.Z/
│   │       ├── library/
│   │       └── data-processing/
│   ├── javascript/
│   ├── java/
│   ├── kotlin/
│   └── c/
├── unix/
│   ├── README.md
│   ├── models/
│   └── commands/
├── kubernetes/
│   ├── README.md
│   ├── models/
│   └── commands/
├── shared/
│   ├── templates/                # skeletons for rapidly creating new vX.Y.Z models
│   └── schemas/
│       └── model-manifest.schema.json   # optional but useful
├── scripts/
│   ├── validate-structure.sh
│   ├── generate-index.py         # auto-builds tables in READMEs
│   └── copy-model.sh             # very handy helper: copy a specific model version to a new dir
├── docs/
│   ├── naming-and-versioning.md  # critical doc
│   ├── adding-a-new-model.md
│   └── contribution-guide.md
└── .github/ ...
```

**Decision point:** `languages/` wrapper vs. direct `python/`, `javascript/` etc. at root.

- Direct at root = flatter, very common for language-focused repos.
- `languages/` wrapper = slightly more explicit grouping.

Either is fine; the plan recommends evaluating both during bootstrap. Many similar repos go flat for the languages.

For unix/kubernetes, the top-level sections keep them clearly "additional" while still prominent.

## Content Standards for a Good Model
- **Copy-paste ready.** The contents of `vX.Y.Z/` should be directly usable or require only trivial renaming.
- Excellent `README.md` inside the version: motivation, trade-offs, "how I would start a real project from this", links to related official docs.
- Code/comments that teach (why this folder, why this config choice).
- For command areas: executable examples + expected output + version notes.
- Keep models small and focused — one model = one coherent use case.

## Implementation Phases (Suggested)
**MVP (get value fast):**
- Decide flat vs. `languages/` wrapper and create the skeleton directories.
- Write `docs/naming-and-versioning.md`.
- Create 1–2 versioned models for Python (highest leverage) + one solid model for each of the other languages.
- Strong `unix/commands/` (categorized) + at least one or two `kubernetes/models/` + `commands/`.
- Root README with a nice index table + usage instructions.
- Basic `scripts/copy-model.sh` and structure validator.
- Commit the plan.md.

**Follow-up:**
- Add more models per language (different architectures/scenarios).
- Improve index generation.
- Add real usage examples and your personal notes from daily work.
- GitHub Release + nice description/topics.

## Tooling & Polish
- Validation that enforces the `.../models/<name>/vX.Y.Z/` pattern + presence of README.
- Simple copy helper (huge productivity win).
- Auto-generated language/model index tables (prevents staleness).
- Keep everything text-based and git-friendly.

## Open Decisions / Questions
1. Flat language dirs at root, or `languages/` wrapper?
2. Do we start with one primary "model" per language (e.g. the most common project type) or ship several variants immediately?
3. How rich should the initial models be? (full small working skeleton vs. illustrative folder tree + heavy guidance README)
4. Any specific first models you have in mind (e.g. "Python FastAPI web", "TypeScript CLI with oclif or just native", "simple C Makefile project", common K8s deployment + service + ingress pattern)?
5. Target versions for commands (e.g. document compatibility with specific kubectl / bash / python versions)?
6. Do you want a light `manifest.yaml` in every model version from the beginning (for future tooling)?

## Immediate Next Steps (once plan approved)
1. Create the directory skeleton as described.
2. Write/expand the key docs (naming policy first).
3. Populate the first high-value models (start with Python + your most-used language).
4. Update root `README.md` using the structure and index ideas.
5. Add the helper scripts.
6. Commit `plan.md` (this file) along with the initial structure so the history shows the intent.

This plan is now tightly scoped to the exact languages + unix + kubernetes you specified, emphasizes a clear versioned naming structure for the models, and is ready to be executed from the real repo path `/Users/andreleitao/MyProjects/dev-models`.

---

*Grounded in standard GitHub repo organization patterns, real-world project-layout proposals (e.g. Go), Kubernetes GitOps and cheatsheet examples, and multi-language developer reference repositories.*