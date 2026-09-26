# ADR 0001: Publish the TypeScript client to npm with trusted publishing

- **Status:** Accepted
- **Date:** 2026-09-26
- **Decision by:** Eric Fitzgerald (human-made architectural decision)

## Context

`publish-js.yml` authenticated to npm with a long-lived `NPM_TOKEN` secret that
was never created, so the `ts-v1.15.0` publish failed with `ENEEDAUTH`. PyPI
publishing already uses OIDC trusted publishing.

## Decision

Publish `@tmi-dev/client` through npm trusted publishing (OIDC from GitHub
Actions, environment `npm`), with no stored npm token.

## Consequences

- No secret to rotate or leak; provenance attestations are generated automatically.
- The publish job needs Node >= 22.14 / npm >= 11.5.1 (the workflow uses Node 24).
- npm can't configure a trusted publisher for a package that doesn't exist, so
  the first version of a new package is published by hand, then the trusted
  publisher is added on the package's settings page.
