# .grok - Local Agent Configuration for dev-models

This directory provides repo-local equivalents of `~/.grok` for use with the Grok Build TUI, CLI, or local agents.

## Structure
- `agents/` - Additional or overridden agent personas
- `skills/` - Local skill definitions (YAML)
- `memory/` - Project-specific persistent memory / context
- `config/` - MCP config, preToolUse guards, etc.

Use these together with the `.github/` versions for a complete local + CI agent experience.

See the root `plan.md` for the overall agent enhancement plan.