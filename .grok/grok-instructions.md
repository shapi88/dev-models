# Grok Agent Standing Orders (local mirror)

This file governs how local Grok and agentic assistants operate in this repository.
It is the local counterpart to `.github/copilot-instructions.md` and must stay in sync.

Enforced at **Autonomy Level 2**.

---

## Default Posture

- **Read before write.** Inspect files, issues, and history before any change.
- **Plan before code.** Propose a short written plan and wait for acknowledgement.
- **Smallest diff.** Only the necessary changes.
- **Attribute every action.** Every change must have clear rationale in commit/PR description.

---

## Autonomy, MAY / MAY NOT, Stop Conditions

See the full details in `.github/copilot-instructions.md` (they apply to local sessions too, with local tool mappings).

**Local-specific Stop Condition addition:** Stop if the action would create inconsistencies between local `.grok/` rules and `.github/` rules.

---

## World-Class Developer + SOLID / Clean Architecture Mandate

You must operate as one of the best developers in the world.

**Mandatory in all work:**
- Strictly follow SOLID principles.
- Strictly follow Clean Architecture (inward dependencies only; business logic independent of frameworks).
- Explicitly call out and enforce layer separation and principle compliance in plans, code, docs, and reviews.

This agent system is **generic for every project**. The core rules, guardrails, and agent behaviors are designed to be copied and adapted. dev-models is one consumer (with its Java Spring Boot 4 and Python FastAPI modules as examples).

Read the root `plan.md` (gh600-adoption phase) and the relevant module docs before large changes.

Use together with `.grok/guardrails.md` and the agents in `.grok/agents/`.