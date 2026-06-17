# Guardrails Policy (local .grok mirror)

This document defines the complete guardrail framework for agentic AI operations when using local Grok tools in this repository.
It mirrors `.github/guardrails.md` for consistency between local and CI environments.
Local changes to this file require human review.

---

## Autonomy Matrix

| Level | Agent capability | Allowed actions | Required controls |
| --- | --- | --- | --- |
| 0 — Suggest only | Read and propose text | Read files, post comments | No write access; human executes |
| 1 — Draft content | Create drafts, plans, artifacts | Open draft PRs, upload artifacts | Human approval before any state change |
| **2 — Limited repo changes** | Create/edit files, open PRs | Branch-scoped writes, PR comments | Branch restriction, required checks, human review before merge |
| 3 — Broad repo automation | Labels, issue updates, multi-file edits | Issues:write, broader contents:write | Tight permissions, audit trail, approval gate, rollback plan |
| 4 — Deployment-affecting | Trigger deploys, modify environments | Actions:write, environment access | Environments API, required reviewers, OIDC, incident controls |

**This repository operates at Level 2 by default for local agents too.**

---

## Hard Stops — Never-Do List (Local + CI)

The following actions are unconditionally prohibited:

| # | Prohibited action | Reason |
| --- | --- | --- |
| 1 | Modify `.github/workflows/` or equivalent local configs | Escalates privileges |
| 2 | Modify `CODEOWNERS` | Removes other guardrails |
| 3 | Modify `.github/copilot-instructions.md`, `.grok/grok-instructions.md`, or guardrails | Undermines policies |
| 4 | Push directly to `main` | Bypasses review |
| 5 | Expose secrets/credentials | Irreversible leakage |
| 6 | Call unapproved MCP server | Unreviewed attack surface |
| 7 | Approve or merge own changes | Removes human-in-the-loop |
| 8 | Delete branch with open PR | Destroys audit trail |
| 9 | Modify evaluation baselines | Corrupts data |
| 10 | Trigger production deployment | Requires human gate |

**Project-Specific Hard Stop:** Never violate SOLID or Clean Architecture without documented human waiver.

---

## SOLID Principles and Clean Architecture Mandate

All agents (local or CI) must act as world-class developers:

**SOLID (in every action):**
- Single Responsibility
- Open/Closed
- Liskov Substitution
- Interface Segregation
- Dependency Inversion

**Clean Architecture:**
- Strict inward dependency rule.
- Entities and Use Cases independent of frameworks (Spring, FastAPI, DBs, etc.).
- Use ports/adapters and explicit layers.
- Document layer boundaries in plans and code.

Reviewer agents must always produce a "SOLID & Clean Architecture Assessment".

This system is **generic** — designed to be copied to any project. Customize only `project-memory.md` and project-specific sections.

---

## Required Audit Trail & Rollback

Same as `.github/guardrails.md`. Local actions must produce equivalent evidence (e.g., local plan file + commit message with rationale).

See `.github/INCIDENT_RESPONSE.md` for handling harmful local actions (adapt the runbook for local context).

Violations are caught via local review skills or manual inspection.