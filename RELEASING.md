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

1. Create an account at https://www.npmjs.com
2. Create the `@tmiclient` organization: https://www.npmjs.com/org/create
3. Create an automation access token:
   - Go to Access Tokens → Generate New Token → Granular Access Token
   - Set permissions to publish packages under `@tmiclient` scope
4. Add the token as a GitHub repository secret:
   - Go to repo Settings → Secrets and variables → Actions
   - Add secret named `NPM_TOKEN` with the token value

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

```bash
# Tag and push
git tag v1.3.0
git push origin v1.3.0

# Create the release (triggers publishing workflows)
gh release create v1.3.0 --title "v1.3.0" --notes "Release tracking TMI API v1.3.0"
```

Or create the release via the GitHub web UI: https://github.com/ericfitz/tmi-clients/releases/new

### 4. Verify Publication

After the workflows complete:

- **PyPI:** https://pypi.org/project/tmi-client/
- **npm:** https://www.npmjs.com/package/@tmiclient/client
- **Go:** `go get github.com/ericfitz/tmi-clients/go-client-generated@v1.3.0`

## What Happens Automatically

When you publish a GitHub release with a `v*` tag:

1. **publish-python.yml** — builds and publishes `tmi-client` to PyPI via trusted publishing (OIDC)
2. **publish-js.yml** — builds and publishes `@tmiclient/client` to npm with provenance
3. **publish-go.yml** — validates the Go client builds and tests pass (Go modules are served directly from git)

Each workflow runs tests before publishing. If tests fail, publishing is skipped.

## Package Installation (for consumers)

```bash
# Python
pip install tmi-client

# JavaScript
npm install @tmiclient/client

# Go
go get github.com/ericfitz/tmi-clients/go-client-generated@latest
```

## Troubleshooting

### PyPI publish fails with "trusted publisher not configured"
Ensure the pending publisher is configured on PyPI with the exact workflow filename, environment name, and repository owner.

### npm publish fails with 401/403
Check that the `NPM_TOKEN` secret is set in the repository and the token has publish permissions for the `@tmiclient` scope.

### Go module not found after release
The Go module proxy may take a few minutes to index new tags. You can force it with:
```bash
GOPROXY=proxy.golang.org go get github.com/ericfitz/tmi-clients/go-client-generated@v1.3.0
```

### Workflow not triggered
Ensure the release tag starts with `v` (e.g., `v1.3.0`). The workflows filter on `refs/tags/v*`.
