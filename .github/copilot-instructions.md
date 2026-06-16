# Copilot / Agent Standing Orders for dev-models

This repository is a **Developer Manual + multi-language template collection**.

## Core Principles for Agents
- Maintain consistency across language modules (Java Spring Boot 4 is the reference).
- When adding Python/FastAPI or other stacks, mirror the structure: getting-started, api/, best-practices/, persistence/, migration/.
- All new docs must be junior-developer friendly and reference the cross-cutting `manual/architectures/` and `manual/onboarding/`.
- Prefer versioned directories where platform versions matter.
- Never break existing links without updating references.

Read the root `plan.md` and `manual/README.md` before making large changes.