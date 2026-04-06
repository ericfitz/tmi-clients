#!/usr/bin/env bash
# Release the Python client to PyPI via GitHub Release.
#
# Usage:
#   ./release_python.sh              # uses version from pyproject.toml
#   ./release_python.sh 1.2.0        # override version
#   ./release_python.sh --dry-run    # validate without publishing
#
# Prerequisites:
#   - gh CLI authenticated
#   - PyPI trusted publishing configured for this repo
#
set -euo pipefail

cd "$(dirname "$0")"

DRY_RUN=false
VERSION=""

for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=true ;;
    *) VERSION="$arg" ;;
  esac
done

# Read version from pyproject.toml if not provided
if [ -z "$VERSION" ]; then
  VERSION=$(python3 -c "
import re
with open('python-client-generated/pyproject.toml') as f:
    m = re.search(r'^version\s*=\s*\"(.+?)\"', f.read(), re.M)
    print(m.group(1))
")
fi

TAG="python-v${VERSION}"

echo "==> Python client release: ${VERSION} (tag: ${TAG})"

# Check for uncommitted changes
if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "ERROR: Uncommitted changes. Commit or stash first."
  exit 1
fi

# Check tag doesn't already exist
if git rev-parse "$TAG" >/dev/null 2>&1; then
  echo "ERROR: Tag ${TAG} already exists."
  exit 1
fi

# Build and validate
echo "==> Building package..."
rm -rf python-client-generated/dist/
(cd python-client-generated && uv build 2>&1)

echo "==> Validating package..."
python3 -m twine check python-client-generated/dist/*

# Run tests
echo "==> Running tests..."
(cd python-client-generated && uv run --with pytest python3 -m pytest test/ -v --tb=short -q)

if [ "$DRY_RUN" = true ]; then
  echo ""
  echo "==> Dry run complete. Package is valid."
  echo "    To publish: ./release_python.sh ${VERSION}"
  exit 0
fi

# Tag and push
echo "==> Creating tag ${TAG}..."
git tag -a "$TAG" -m "Release Python client v${VERSION}"
git push origin "$TAG"

# Create GitHub Release (triggers the publish workflow)
echo "==> Creating GitHub Release..."
gh release create "$TAG" \
  --title "Python client v${VERSION}" \
  --notes "Release of \`tmi-client\` v${VERSION} to PyPI." \
  python-client-generated/dist/*

echo ""
echo "==> Release created! GitHub Actions will publish to PyPI."
echo "    Monitor: gh run watch"
echo "    PyPI:    https://pypi.org/project/tmi-client/${VERSION}/"
