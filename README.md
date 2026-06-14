# dev-models

**Curated, versioned project models, reference structures, and command references for developers.**

A practical daily-driver helper repo organized around real programming languages + essential ops tooling.

## What is a "model" here?

A **model** is a small, high-quality, copyable reference:

- Recommended project layout / folder structure for a specific kind of work
- Starter boilerplate with the "right" modern defaults and idiomatic patterns
- Reference implementation of a common pattern (with explanations)
- For Unix & Kubernetes: well-organized command sets, script templates, and manifest "models"

Everything is **explicitly versioned** so you can see evolution and pin to a known-good state.

## Languages & Topics

- **python**
- **javascript**
- **java**
- **kotlin**
- **c**
- **unix** (commands + scripting models)
- **kubernetes** (manifest models + commands)

## Quick Start

```bash
# Browse the structure
cd dev-models

# Find a Python web project model
ls python/models/web-api/

# Copy the latest version somewhere
cp -r python/models/web-api/v1.0.0/* ~/my-new-project/
cd ~/my-new-project
# ... rename package, init git, etc. (see the model's README)
```

See the full naming rules and philosophy:

- [docs/naming-and-versioning.md](docs/naming-and-versioning.md)
- [plan.md](plan.md) (implementation plan / history of decisions)

## Current Models & References

> This table is maintained manually for now. A generator script is planned.

### Python
| Model         | Latest | Path                                      | Notes                                      |
|---------------|--------|-------------------------------------------|--------------------------------------------|
| web-api       | v1.0.0 | `python/models/web-api/v1.0.0/`           | Modern src/ + pyproject.toml + Dockerfile  |
| cli-tool      | —      | `python/models/cli-tool/`                 | (add your first version)                   |

### JavaScript
| Model         | Latest | Path                                           | Notes                        |
|---------------|--------|------------------------------------------------|------------------------------|
| cli-tool      | v1.0.0 | `javascript/models/cli-tool/v1.0.0/`           | ESM + minimal bin skeleton   |

### Java
| Model         | Latest | Path                           | Notes |
|---------------|--------|--------------------------------|-------|
| (TBD)         | —      | `java/models/`                 | Language README present      |

### Kotlin
| Model         | Latest | Path                           | Notes |
|---------------|--------|--------------------------------|-------|
| (TBD)         | —      | `kotlin/models/`               | Language README present      |

### C
| Model         | Latest | Path                                      | Notes                     |
|---------------|--------|-------------------------------------------|---------------------------|
| system-tool   | v1.0.0 | `c/models/system-tool/v1.0.0/`            | Makefile + src/include skeleton |

### Unix
| Area          | Content                          | Path                           | Notes |
|---------------|----------------------------------|--------------------------------|-------|
| commands      | file-ops, process-mgmt           | `unix/commands/`               | Categorized patterns + examples |
| models        | —                                | `unix/models/`                 | Add script project models |

### Kubernetes
| Area          | Latest | Path                                                | Notes |
|---------------|--------|-----------------------------------------------------|-------|
| models        | v1.0.0 | `kubernetes/models/stateless-web/v1.0.0/`           | Deployment + Service (1.28+) |
| commands      | —      | `kubernetes/commands/`                              | Add useful kubectl references |

## Philosophy & Conventions

- **Versioned models** (`v1.2.0/`) are the atomic unit you copy or reference.
- Old versions stay forever.
- Each model version ships its own excellent `README.md` explaining *why* the structure exists and how to turn it into a real project.
- We favor **language-native** or very common setups over tying models too tightly to specific frameworks (framework notes go in the README).

See the complete rules: [docs/naming-and-versioning.md](docs/naming-and-versioning.md)

## Contributing

Models are meant to be **living references** that improve over time.

1. Open an issue or PR describing the model / improvement.
2. Follow the naming + versioning policy.
3. Include a high-quality README inside the version directory.
4. Update relevant index tables.

More details coming in `CONTRIBUTING.md` and `docs/adding-a-new-model.md`.

## Project Layout (on disk)

```
dev-models/
├── python/
│   └── models/
│       └── web-api/
│           └── v1.0.0/     ← copy this (or any version)
├── javascript/ ...
├── java/ ...
├── kotlin/ ...
├── c/ ...
├── unix/
│   ├── models/
│   └── commands/
├── kubernetes/
│   ├── models/
│   └── commands/
├── shared/
├── scripts/
├── docs/
│   └── naming-and-versioning.md
├── plan.md
└── README.md
```

## Status

Early bootstrap. The structure and naming policy are in place. First real models (starting with Python) are being added.

This repo exists to save you (and future you) time when starting or refactoring projects.

---

**Repo path:** `/Users/andreleitao/MyProjects/dev-models`  
**Plan document:** [plan.md](plan.md) (self-contained in the repo)