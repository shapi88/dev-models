#!/usr/bin/env bash
#
# copy-model.sh
# Helper to copy a specific versioned model to a destination.
#
# Usage:
#   ./scripts/copy-model.sh python web-api v1.0.0 ~/projects/my-new-api
#   ./scripts/copy-model.sh kubernetes models/stateless-web v1.0.0 ./k8s-configs
#
# The script copies the *contents* of the version directory so the
# destination becomes a ready-to-use project root.

set -euo pipefail

if [ "$#" -ne 4 ]; then
  echo "Usage: $0 <lang-or-tool> <model-name> <version> <dest-dir>"
  echo "Example: $0 python web-api v1.0.0 ~/my-api"
  echo "Example: $0 kubernetes stateless-web v1.0.0 ./deploy"
  exit 1
fi

LANG_OR_TOOL=$1
MODEL_NAME=$2
VERSION=$3
DEST=$4

# The repo root is the directory containing this script's parent
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

SRC="${REPO_ROOT}/${LANG_OR_TOOL}/models/${MODEL_NAME}/${VERSION}"

if [ ! -d "$SRC" ]; then
  echo "Error: Source model not found: $SRC"
  echo "Check that the language/tool, model name, and version are correct."
  exit 2
fi

mkdir -p "$DEST"

# Copy contents (not the version dir itself) so DEST becomes the project root
cp -a "${SRC}/." "$DEST/"

echo "Copied ${LANG_OR_TOOL}/models/${MODEL_NAME}/${VERSION} -> ${DEST}"
echo "Next steps: cd ${DEST} and read the README.md inside it."