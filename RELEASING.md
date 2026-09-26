# Releasing TMI API Clients

This document describes how to publish new versions of the TMI API clients to PyPI, npm, and the Go module proxy.

## Prerequisites (One-Time Setup)

### 1. PyPI (Python)

1. Create an account at https://pypi.org
2. Go to your account settings → Publishing → Add a new pending publisher
3. Configure:
   - **Package name:** `tmi-client`
   - **Owner:** `ericfitz`
   - **Repository:** `tmi-clients`
   - **Workflow name:** `publish-python.yml`
   - **Environment name:** `pypi`

### 2. npm (JavaScript)

`publish-js.yml` authenticates through npm trusted publishing (OIDC); there is
no `NPM_TOKEN` secret. See `docs/adr/0001-npm-trusted-publishing.md`.

1. Create an account at https://www.npmjs.com
2. Create the `@tmiclient` organization: https://www.npmjs.com/org/create
3. First publish of a new package: npm can't attach a trusted publisher to a
   package that doesn't exist yet, so publish the first version by hand from
   the client directory (`npm ci && npm run build && npm publish --access public`,
   with 2FA).
4. On the package's Settings → Trusted Publisher, add GitHub Actions:
   - **Organization or user:** `ericfitz`
   - **Repository:** `tmi-clients`
   - **Workflow filename:** `publish-js.yml`
   - **Environment name:** `npm`

### 3. GitHub Environments

1. Go to repo Settings → Environments
2. Create environment `pypi`
   - (Optional) Add deployment protection rules / required reviewers
3. Create environment `npm`
   - (Optional) Add deployment protection rules / required reviewers

## How to Release

### 1. Regenerate Clients (if API spec changed)

```bash
# Regenerate all clients from the latest OpenAPI spec
python3 regenerate_python.py
python3 regenerate_go.py
python3 regenerate_js.py

# Or from a local spec file
python3 regenerate_python.py path/to/tmi-openapi.json
python3 regenerate_go.py path/to/tmi-openapi.json
python3 regenerate_js.py path/to/tmi-openapi.json
```

The regeneration scripts automatically extract the version from the OpenAPI spec's `info.version` field and update all package configs.

### 2. Commit and Push

```bash
git add -A
git commit -m "feat: regenerate clients from tmi vX.Y.Z spec"
git push origin main
```

### 3. Create a GitHub Release

One release per language; the tag prefix selects the workflow:

```bash
# Creating the release creates and pushes the tag, and triggers the workflow
gh release create python-v1.15.0 --title "Python v1.15.0" --notes "Release tracking TMI API v1.15.0"
gh release create ts-v1.15.0     --title "TypeScript v1.15.0" --notes "Release tracking TMI API v1.15.0"
gh release create go-v1.15.0     --title "Go v1.15.0" --notes "Release tracking TMI API v1.15.0"
```

Or create the release via the GitHub web UI: https://github.com/ericfitz/tmi-clients/releases/new

### 4. Verify Publication

After the workflows complete:

- **PyPI:** https://pypi.org/project/tmi-client/
- **npm:** https://www.npmjs.com/package/@tmiclient/client
- **Go:** `go get github.com/ericfitz/tmi-clients/go-client-generated/v1_15_0@v1.15.0`

## What Happens Automatically

When you publish a GitHub release with a `python-v*`, `ts-v*`, or `go-v*` tag, the matching workflow runs:

1. **publish-python.yml** — builds and publishes `tmi-client` to PyPI via trusted publishing (OIDC)
2. **publish-js.yml** — builds and publishes `@tmiclient/client` to npm via trusted publishing (provenance is automatic)
3. **publish-go.yml** — on a `go-vX.Y.Z` release, builds and tests `go-client-generated/vX_Y_Z`, then pushes the Go module tag `go-client-generated/vX_Y_Z/vX.Y.Z` at the release commit. Go resolves a subdirectory module's versions only from tags with that prefix; the proxy serves modules straight from git.

Each workflow runs tests before publishing. If tests fail, publishing is skipped.

## Validating the Publish Workflows Without a Release

Each publish workflow accepts a `workflow_dispatch` that builds and tests a
committed client version without publishing, so action-version bumps can be
validated without cutting a release:

```bash
gh workflow run publish-python.yml -f version=1.8.3
gh workflow run publish-js.yml     -f version=1.8.3
gh workflow run publish-go.yml     -f version=1.8.3   # dotted, not underscored
```

A dry run cannot reach `gh-action-pypi-publish` itself — that action only does
anything on a real upload. To exercise it, dispatch the Python workflow with
`publish_testpypi=true`:

```bash
gh workflow run publish-python.yml -f version=1.8.3 -f publish_testpypi=true
```

That stamps a throwaway `<version>.dev<run_number>` into `pyproject.toml` and
`setup.py` **after** the version-match check and the tests, then uploads to
TestPyPI only. `publish-pypi` stays gated on `release` and is skipped. The
`.devN` suffix matters because TestPyPI rejects a re-upload of a version it
already holds ("file already exists"), and it keeps the real version numbers
unclaimed. These uploads are throwaway; nothing consumes them.

## Package Installation (for consumers)

```bash
# Python
pip install tmi-client

# JavaScript
npm install @tmiclient/client

# Go
go get github.com/ericfitz/tmi-clients/go-client-generated/v1_15_0@v1.15.0
```

## Troubleshooting

### PyPI publish fails with "trusted publisher not configured"
Ensure the pending publisher is configured on PyPI with the exact workflow filename, environment name, and repository owner.

### npm publish fails with ENEEDAUTH/401/403/404
Check that the trusted publisher on the package's npm settings names the exact owner, repository, workflow filename, and environment, and that the job runs on Node >= 22.14 (npm >= 11.5.1).

### Go module not found after release
The Go module proxy may take a few minutes to index new tags. You can force it with:
```bash
GOPROXY=proxy.golang.org go get github.com/ericfitz/tmi-clients/go-client-generated/v1_15_0@v1.15.0
```

### Workflow not triggered
Each publish workflow filters on its own tag prefix: `python-v*`, `ts-v*`, `go-v*` (e.g., `go-v1.15.0`).
