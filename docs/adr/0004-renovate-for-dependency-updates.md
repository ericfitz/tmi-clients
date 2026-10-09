# ADR 0004: Use deps-bump-bot (Renovate) for dependency updates; Dependabot for alerts only

- **Status:** Accepted
- **Date:** 2026-10-08
- **Decision by:** Eric Fitzgerald (human-made architectural decision)

## Context

`.github/dependabot.yml` configures version updates only for GitHub Actions.
Nothing updates the npm, uv or Go dependencies of the committed clients
between regenerations. Dependabot security updates were enabled, and after
#63 deleted the 1.x client directories they kept failing with
`dependency_file_not_found`, because the urllib3 alerts against the deleted
`uv.lock` files stayed open (alerts 31–51, dismissed as `not_used` on
2026-10-08).

`ericfitz/deps-bump-bot` is a self-hosted Renovate runner (App
`ericfitz-deps-bot`) with a shared preset (its ADR 0001). The preset groups
updates by ecosystem, auto-merges patch/minor/pin/digest updates once
required checks pass, holds majors for Dependency Dashboard approval, and
opens fix PRs from Dependabot alerts.

## Decision

- Adopt deps-bump-bot as this repo's version updater via
  `.github/renovate.json` extending `github>ericfitz/deps-bump-bot`.
- Keep Dependabot **alerts** on. Turn off Dependabot **security updates**
  (Renovate opens alert fix PRs; both would duplicate) and delete
  `.github/dependabot.yml`: its only entry was `updates:` (GitHub Actions),
  the schema requires that key, and alerts are a repository setting.

## Repo-specific configuration required

1. **Generator scripts are the source of versions.** `regenerate_ts.py`
   hard-codes the TypeScript devDependency ranges and `regenerate_go.py`
   sets `GO_VERSION`; regeneration overwrites bumps made only in a client
   directory. Add Renovate regex custom managers so these constants are
   bumped in the scripts.
2. **Published-library ranges.** Python: lockfile-only updates
   (`rangeStrategy: update-lockfile`); do not raise `pyproject.toml` floors
   automatically. Treat Go `require` bumps in the published module with the
   same caution.
3. GitHub auto-merge is disabled on this repo: set
   `"platformAutomerge": false` so Renovate merges once checks (including
   the CodeQL check `main` requires) are green.
4. openapi-generator's boilerplate CI files under `python-client-generated/`
   (`.github/workflows/python.yml`, `.gitlab-ci.yml`) are disabled:
   regeneration overwrites them and this repo's CI does not run them.
5. The `ericfitz-deps-bot` App must be installed on `ericfitz/tmi-clients`.

## Consequences

- One weekly PR per ecosystem instead of none; security fixes open within a
  day of an alert.
- Security floors in published package metadata (e.g. urllib3, #68) remain a
  deliberate change in the generator scripts, not an automatic bump.
