#!/usr/bin/env bash
#
# validate-structure.sh
# Basic sanity check that the repo follows the naming/versioning conventions.
#
# Run from repo root.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

errors=0

echo "Validating dev-models structure..."

# Check that we have the expected top-level sections
for d in python javascript java kotlin c unix kubernetes docs scripts shared; do
  if [ ! -d "$d" ]; then
    echo "MISSING: $d/"
    ((errors++))
  fi
done

# Find model version directories and ensure they have a README.md
while IFS= read -r -d '' verdir; do
  if [ ! -f "${verdir}/README.md" ]; then
    echo "Model version missing README.md: $verdir"
    ((errors++))
  fi
  # Simple SemVer-ish check on the leaf directory name
  vername=$(basename "$verdir")
  if [[ ! "$vername" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "Suspicious version directory name (expected vX.Y.Z): $verdir"
    ((errors++))
  fi
done < <(find . -type d -path '*/models/*/*' -print0 2>/dev/null | grep -zE '/v[0-9]+\.[0-9]+\.[0-9]+$' || true)

if [ "$errors" -gt 0 ]; then
  echo "Validation failed with $errors error(s)."
  exit 1
else
  echo "Structure looks good."
fi