# .grok - Local Agent Configuration for dev-models

This directory provides repo-local equivalents of `~/.grok` for use with the Grok Build TUI, CLI, or local agents.

**Important:** .grok uses the **exact same rule set structure and strategy** as .github/ for full consistency (same agent frontmatter, Core Directives, skill schemas, guardrails, etc.). .grok/ is the *local execution environment* view; .github/ is the *CI / GitHub Actions* view. Agents and skills are designed to behave identically whether invoked locally or in workflows.

## Structure
- `agents/` - Agent personas (same format as .github/agents/, with local tool adaptations)
- `skills/` - Local skill definitions (YAML, same schema as .github/skills/)
- `memory/` - Project-specific persistent memory / context
- `config/` - MCP config, preToolUse guards, etc. (mirrors reference where applicable)
- `guardrails.md` and `grok-instructions.md` - Local governance (mirrors .github/ versions)

## Usage
Load agents and skills from here when using local Grok tools. Combine with .github/ for hybrid local+CI development.

See the root `plan.md` (section "Phase: Adapt .grok to Use the Same Rule Set Structure and Strategy as .github") for details on the alignment.

Also see the cross-cutting templates/ structure for the developer manual and language-specific modules (Java Spring Boot 4 reference + Python FastAPI).