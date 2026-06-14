# Adding a New Model

1. Decide on the language / tool section (`python`, `unix`, `kubernetes`, ...).
2. Choose a short, descriptive model purpose name (`web-api`, `stateless-web`, `cli-tool`...).
3. Create `.../models/<purpose>/v1.0.0/` (or next appropriate SemVer).
4. Populate with the actual recommended files + a great `README.md`.
5. Update language-level or root README indexes if useful.
6. Follow everything in `naming-and-versioning.md`.

When in doubt, copy an existing high-quality model as the starting template (from `shared/templates/` once populated, or from an existing `vX.Y.Z/`).

Models should be immediately useful when copied. Prioritize clarity over cleverness.