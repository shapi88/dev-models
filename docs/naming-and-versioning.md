# Naming and Versioning

This document defines the **official conventions** for the dev-models repository.

The goal is a highly predictable structure so any developer (or future script) can instantly find and use the right reference "model".

## Core Principles
- **Language-first navigation** for the programming languages.
- **Models are versioned** — the version is visible and part of the path.
- Lowercase + hyphens only (no underscores, camelCase, or spaces in paths).
- Semantic Versioning (SemVer) for every model.
- Old versions are **never deleted** — they remain useful historical references.
- The repo name itself (`dev-models`) is versionless. Use Git tags / GitHub Releases for overall repo versioning.

## Directory Layout (Canonical)

```
dev-models/
├── python/
│   └── models/
│       ├── web-api/
│       │   ├── v1.0.0/          # The actual model files live inside the version dir
│       │   ├── v1.1.0/
│       │   └── v1.2.0/
│       ├── cli-tool/
│       │   └── vX.Y.Z/
│       └── library/
│           └── ...
├── javascript/
│   └── models/
│       └── ...
├── java/
├── kotlin/
├── c/
├── unix/
│   ├── models/
│   └── commands/
├── kubernetes/
│   ├── models/
│   └── commands/
├── shared/
├── scripts/
├── docs/
│   └── naming-and-versioning.md   # (this file)
└── README.md
```

**Why this shape?**
- Direct language folders at the root make "organized with programming languages models" obvious.
- `models/` subfolder under each language (and under unix/kubernetes) makes the intent unmistakable.
- `vX.Y.Z/` directories give clear, browsable versioning.
- `unix/` and `kubernetes/` sit at the same level as the languages (as "additionally" requested) but use the same model/versioning discipline.

## Model Naming (the middle segment)
Use descriptive, lowercase, hyphenated names that describe the **common use case** or pattern:

Good examples:
- `web-api`
- `cli-tool`
- `library`
- `microservice`
- `data-processing`
- `fullstack-app`
- `clean-architecture`
- `system-tool` (for C)
- `backup-utility` (unix)
- `stateless-web` (kubernetes)

Avoid:
- Framework names in the model name unless the model is deliberately framework-specific (`fastapi-web` is usually worse than `web-api`).
- Very long names.

## Versioning Rules (SemVer)

Use `vMAJOR.MINOR.PATCH` directory names.

- **MAJOR** (`v2.0.0`): Breaking changes to the recommended structure, idioms, or layout. Consumers should treat this as a new starting point rather than an in-place upgrade.
- **MINOR** (`v1.1.0`): Backward-compatible additions or meaningful improvements (new recommended folder, better defaults, extra documentation).
- **PATCH** (`v1.0.1`): Fixes, typo corrections, small comment improvements, updated compatibility notes.

Inside each version directory you should have (at minimum):
- `README.md` — purpose, when to use this model, copy instructions, compatibility, rationale.
- The real files/folders that constitute the model (so the contents of `vX.Y.Z/` can often be copied directly).

Additional recommended files (per version or at the model level):
- `CHANGELOG.md`
- `manifest.yaml` (lightweight metadata — see shared/templates)

### Compatibility Notes
Every model README **must** clearly state what it targets:
- Language / runtime version (e.g. "Python 3.11+", "C11 + POSIX.1-2008")
- Tooling versions (e.g. "kubectl 1.28–1.32", "bash 5+ / zsh")
- Any notable external dependencies or assumptions

Example snippet for a model README:

> **Compatibility**
> - Python 3.11+
> - Uses the src/ layout + pyproject.toml (PEP 621)
> - Tested with uv 0.4+ and Python 3.12

## Unix & Kubernetes Specifics
These sections follow the exact same rules:
- `unix/models/backup-utility/v1.0.0/`
- `kubernetes/models/stateless-web/v1.2.0/`
- Command material lives in `commands/` subdirectories and can also be versioned when the command surface or best practices change significantly (`commands/kubectl/v1.30/` or simply well-organized folders with compatibility notes in the files).

## How to Name a New Model Version
1. Copy an existing good `vX.Y.Z/` as the starting point for the new version (or use the scripts in `scripts/` once they exist).
2. Increment the version according to the rules above.
3. Update the inner `README.md` and any `CHANGELOG.md`.
4. Update any index tables in parent `README.md` files (or run the generator script).
5. Commit with a clear message, e.g. `feat(python): add web-api v1.2.0 (observability folder + modern pyproject)`.

## File Naming Inside Models
- Use the conventions natural to the language/ecosystem.
- Keep file names clean and conventional (`pyproject.toml`, `Makefile`, `deployment.yaml`, etc.).
- Documentation files inside the model are usually `README.md`.

## Future-Proofing
- The structure is intentionally simple so it can be consumed by small scripts (the `copy-model.sh` helper, index generators, etc.).
- If we ever add a manifest per model version, the path pattern `*/models/*/v*/*.yaml` will make discovery trivial.

Questions or proposed changes to these rules should be discussed via issues or PRs and then reflected in this document.

This policy exists so the repository remains a reliable, low-friction helper for years.