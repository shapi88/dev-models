# Guardrails Policy

This document defines the complete guardrail framework for agentic AI operations in this repository.
It is both machine-readable (for automated checks) and human-readable (for governance review).
CODEOWNERS review is required to modify this file.

---

## Autonomy Matrix

| Level | Agent capability | Allowed actions | Required controls |
| --- | --- | --- | --- |
| 0 — Suggest only | Read and propose text | Read files, post comments | No write access; human executes |
| 1 — Draft content | Create drafts, plans, artifacts | Open draft PRs, upload artifacts | Human approval before any state change |
| **2 — Limited repo changes** | Create/edit files, open PRs | Branch-scoped writes, PR comments | Branch restriction, required checks, human review before merge |
| 3 — Broad repo automation | Labels, issue updates, multi-file edits | Issues:write, broader contents:write | Tight permissions, audit trail, approval gate, rollback plan |
| 4 — Deployment-affecting | Trigger deploys, modify environments | Actions:write, environment access | Environments API, required reviewers, OIDC, incident controls |

**This repository operates at Level 2 by default.**  
Level 3 or 4 actions require explicit human escalation and must not be triggered autonomously.

---

## Hard Stops — Never-Do List

The following actions are unconditionally prohibited for all agents at all autonomy levels:

| # | Prohibited action | Reason |
| --- | --- | --- |
| 1 | Modify `.github/workflows/` | Workflow changes can escalate privileges |
| 2 | Modify `CODEOWNERS` | Removing owners removes all other guardrails |
| 3 | Modify `.github/copilot-instructions.md` or `.grok/grok-instructions.md` | Modifying standing orders undermines all policies |
| 4 | Push directly to `main` | Bypasses required review |
| 5 | Expose a secret, token, or credential in a log, comment, or artifact | Irreversible credential leakage |
| 6 | Call an MCP server not in `.github/mcp-config.json` | Unreviewed attack surface |
| 7 | Approve or merge a PR the agent itself authored | Removes human-in-the-loop entirely |
| 8 | Delete a branch that has an open PR | Destroys audit trail |
| 9 | Modify or delete an existing evaluation baseline | Corrupts benchmark data |
| 10 | Trigger a deployment to the `production` environment | Must always have a human approval gate |

**Additional Project-Specific Hard Stop:** Agents must never violate SOLID principles or Clean Architecture dependency rule in generated or reviewed code/docs without explicit human waiver documented in the PR.

---

## Required Audit Trail by Action Type

| Action type | Required evidence |
| --- | --- |
| File creation or edit | PR with non-empty description (rationale + scope summary) |
| Issue label applied | Issue comment explaining label rationale |
| Workflow run triggered | Workflow summary with task, trigger, and actor |
| Artifact uploaded | Artifact metadata (name, retention, workflow run link) |
| Plan generated | Plan JSON artifact with `generated_at` and `requires_human_approval: true` |
| Multi-agent handoff | Handoff artifact conforming to `templates/artifact-schema.json` |
| Evaluation run | Results artifact with pass/fail per dimension |

---

## Rollback Procedures

### Scenario A: Bad commit on an agent branch

```bash
# 1. Identify the bad commit
git log --oneline copilot/<branch>

# 2. Revert
git revert <bad-sha> --no-edit
git push origin copilot/<branch>

# 3. Close the associated PR and delete the branch
gh pr close <pr-number> --delete-branch
```

### Scenario B: Bad commit merged to main

```bash
# 1. Create a revert PR
git checkout -b revert/agent-harm-<short-sha>
git revert <bad-sha> --no-edit
git push origin revert/agent-harm-<short-sha>
gh pr create --title "Revert: agent-caused harm <short-sha>" --body "Revert of bad agent commit. See incident issue."
```

### Scenario C: Leaked credential

```bash
# 1. Rotate the credential IMMEDIATELY (do not wait for the revert).
# 2. Revoke the old token in the relevant service's settings.
# 3. Remove the credential from commit history using BFG or git filter-repo.
# 4. Force-push the cleaned history (requires branch protection override — admin only).
# 5. File a security incident report.
```

---

## Policy Enforcement Mapping

| Policy | Enforcement mechanism |
| --- | --- |
| No direct push to main | Branch protection — restrict pushes |
| Require human review | Branch protection — required approving reviews |
| Sensitive-path review | CODEOWNERS + branch protection — require code owner review |
| Status checks pass | Branch protection — required status checks (guardrails-check, scope-control, secret-scan) |
| No bypass for admins | Branch protection — do not allow bypassing |
| Least-privilege token | Workflow `permissions:` block on every workflow and job |
| MCP allowlist | `.github/mcp-config.json` + agent stop condition |
| Deployment approval gate | `environment: agent-execution` with Required Reviewer |
| SOLID / Clean Architecture | Reviewer agent mandatory section + guardrails hard stop (with waiver process) |

---

## Review Schedule

This policy must be reviewed:
- When a new autonomy level is requested.
- After any security incident involving the agent.
- When new MCP servers are added.
- When SOLID or Clean Architecture rules are updated.
- At least every 6 months.

Last reviewed: 2026-06-14 by Grok (adapted from gh600-exam)

---

## SOLID Principles and Clean Architecture Mandate (Project-Specific Extension)

All agents **must** behave as world-class developers and strictly follow:

**SOLID Principles (in every plan, code change, and review):**
- **S**ingle Responsibility Principle
- **O**pen/Closed Principle
- **L**iskov Substitution Principle
- **I**nterface Segregation Principle
- **D**ependency Inversion Principle

**Clean Architecture Rules:**
- Dependency rule: Dependencies must point inward (Entities → Use Cases → Interface Adapters → Frameworks & Drivers).
- Business logic (entities, use cases) must not depend on frameworks (Spring, FastAPI, DBs, etc.).
- Use ports and adapters, dependency injection, and clear layer separation in all templates and examples.

The Reviewer Agent **must** include a "SOLID & Clean Architecture Assessment" in every review.
The Planner must explicitly map proposed changes to these principles.
Violations are treated as hard stops unless waived with human approval and documented rationale.

This makes the agents suitable for *any* project.