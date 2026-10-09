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
2. The `tmi-dev` organization (scope `@tmi-dev`) must exist on npmjs.com
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
# Regenerate all clients from the branches listed in versions.json
python3 regenerate_all.py

# Or one language, or one spec file
python3 regenerate_all.py --language python
python3 regenerate_ts.py --spec path/to/tmi-openapi.json --output-dir typescript-client-generated/v2.2.0
```

The regeneration scripts extract the version from the OpenAPI spec's `info.version` field, name the client directory for it, and update all package configs.

### 2. Land the Change

Regenerated clients land through a pull request (a ruleset on `main` blocks direct pushes of the large diff); `regenerate_all.py` opens it for you. Merge it before creating the release.

### 3. Create a GitHub Release

One release per language; the tag prefix selects the workflow:

```bash
# Creating the release creates and pushes the tag, and triggers the workflow
gh release create python-v2.2.0 --title "Python v2.2.0" --notes "Release tracking TMI API v2.2.0"
gh release create ts-v2.2.0     --title "TypeScript v2.2.0" --notes "Release tracking TMI API v2.2.0"
gh release create go-v2.2.0     --title "Go v2.2.0" --notes "Release tracking TMI API v2.2.0"
```

Or create the release via the GitHub web UI: https://github.com/ericfitz/tmi-clients/releases/new

### Client-only fix releases

A fix to a client whose spec version is already published (a generator patch,
a hand-written file) has no new spec version to release under. Merge the fix,
then release the **next free patch** of that major.minor, with no version-bump
commit:

```bash
gh release create go-v2.2.1 --title "Go v2.2.1" --notes "Fix: <what changed>"
```

The release tag names the release version R. Each publish workflow runs
`.github/scripts/resolve_client_dir.py`, which picks the committed directory
with the same major.minor as R and the highest patch <= R's patch (R = 2.2.1
with only `v2.2.0` committed builds `v2.2.0`; R = 2.2.5 with `v2.2.0` and
`v2.2.3` builds `v2.2.3`). No such directory fails the workflow, so a new
major.minor needs a regenerated client first. The committed files keep the
spec version; the workflow stamps R into the package metadata of its checkout
before building:

- **Python:** `.github/scripts/stamp_python_version.py` rewrites `pyproject.toml`, `setup.py`, `tmi_client/__init__.py`, the user agent in `api_client.py` and the "SDK Package Version" in `configuration.py`. "Version of the API" strings and docs keep the spec version.
- **npm:** `npm version R --no-git-tag-version` updates `package.json` and `package-lock.json`.
- **Go:** nothing is stamped; the module tag `go-client-generated/<dir>/vR` (e.g. `go-client-generated/v2_2_0/v2.2.1`) is the version. The embedded user agent keeps the spec version because the tag must point at a committed tree.

Published packages can therefore carry a version that appears nowhere in the
repo; the release tag is the record. See `docs/adr/0003-client-fix-release-versions.md`.

**Collision:** if a later spec version equals an already-released fix version
(spec 2.2.1 regenerated after fix release 2.2.1), the new release fails on the
registry (PyPI/npm reject the duplicate) or the Go module-tag check (the tag
exists at a different commit). Release that spec client under the next free
patch instead, e.g. `2.2.2`, which still resolves to the new `v2.2.1`
directory. Each language's release is independent: use the next free patch per
language.

Re-running a release with the same R is safe for Go when the tag already
points at the release commit (the step is a no-op); a different commit fails.
The TestPyPI upload uses `skip-existing`, so a Python re-run reaches PyPI,
which rejects a duplicate version (as does npm), so a re-run after a
successful publish fails at the publish step. A release tag that points at an older
commit builds that commit's tree, so the resolver sees only the directories
that existed then.

### 4. Verify Publication

After the workflows complete:

- **PyPI:** https://pypi.org/project/tmi-client/
- **npm:** https://www.npmjs.com/package/@tmi-dev/client
- **Go:** `go get github.com/ericfitz/tmi-clients/go-client-generated/v2_2_0/v2@v2.2.0`

## What Happens Automatically

When you publish a GitHub release with a `python-v*`, `ts-v*`, or `go-v*` tag, the matching workflow runs:

1. **publish-python.yml** — builds and publishes `tmi-client` to PyPI via trusted publishing (OIDC)
2. **publish-js.yml** — builds and publishes `@tmi-dev/client` to npm via trusted publishing (provenance is automatic)
3. **publish-go.yml** — on a `go-vX.Y.Z` release, builds and tests the resolved directory (`go-client-generated/vX_Y_Z` for the same major.minor, see Client-only fix releases), then pushes the Go module tag `go-client-generated/vX_Y_Z/vX.Y.Z` at the release commit. Go resolves a subdirectory module's versions only from tags with that prefix; the proxy serves modules straight from git. From 2.0.0 on, the module path carries Go's major-version suffix (`go get github.com/ericfitz/tmi-clients/go-client-generated/v2_2_0/v2@v2.2.0`); the tag keeps the directory prefix (`go-client-generated/v2_2_0/v2.2.0`).

Each workflow runs tests before publishing. If tests fail, publishing is skipped.

## Validating the Publish Workflows Without a Release

Each publish workflow accepts a `workflow_dispatch` that builds and tests a
committed client without publishing, so action-version bumps can be
validated without cutting a release:

```bash
gh workflow run publish-python.yml -f version=2.2.1
gh workflow run publish-js.yml     -f version=2.2.1
gh workflow run publish-go.yml     -f version=2.2.1   # dotted, not underscored
```

A dry run cannot reach `gh-action-pypi-publish` itself — that action only does
anything on a real upload. To exercise it, dispatch the Python workflow with
`publish_testpypi=true`:

```bash
gh workflow run publish-python.yml -f version=2.2.1 -f publish_testpypi=true
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
npm install @tmi-dev/client

# Go
go get github.com/ericfitz/tmi-clients/go-client-generated/v2_2_0/v2@v2.2.0
```

## Troubleshooting

### PyPI publish fails with "trusted publisher not configured"
Ensure the pending publisher is configured on PyPI with the exact workflow filename, environment name, and repository owner.

### npm publish fails with ENEEDAUTH/401/403/404
Check that the trusted publisher on the package's npm settings names the exact owner, repository, workflow filename, and environment, and that the job runs on Node >= 22.14 (npm >= 11.5.1).

### Go module not found after release
The Go module proxy may take a few minutes to index new tags. You can force it with:
```bash
GOPROXY=proxy.golang.org go get github.com/ericfitz/tmi-clients/go-client-generated/v2_2_0/v2@v2.2.0
```

### Workflow not triggered
Each publish workflow filters on its own tag prefix: `python-v*`, `ts-v*`, `go-v*` (e.g., `go-v2.2.0`).
