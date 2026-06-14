# Contributing to dev-models

Thank you for helping make this a better daily reference for developers.

## Core Rules
- Follow the conventions in [docs/naming-and-versioning.md](docs/naming-and-versioning.md) **exactly**.
- Every model version must contain a high-quality `README.md` that explains purpose, rationale, compatibility, and copy instructions.
- Old versions stay. Create a new `vX.Y.Z/` instead of overwriting.
- Keep models small and focused.

## Adding a New Model or Version

1. Create the directory following the pattern:
   `<language-or-tool>/models/<purpose>/vMAJOR.MINOR.PATCH/`
2. Add the real files that represent the model.
3. Write an excellent `README.md` inside the version dir.
4. (Optional but recommended) Add a short entry to any relevant parent README index.
5. Open a PR with a clear description of what problem the model solves and why the structure is good.

## Scripts & Tooling
See the `scripts/` directory. Helpers (copy-model, validation, index generation) are welcome.

## Questions?
Open an issue. This repo exists to be useful — feedback that improves the models or the structure is highly appreciated.

---

See also [plan.md](plan.md) for the original design decisions.