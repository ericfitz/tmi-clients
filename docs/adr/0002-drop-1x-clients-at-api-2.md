# ADR 0002: Stop maintaining 1.x clients when the API moves to 2.0.0

- **Status:** Accepted
- **Date:** 2026-10-07
- **Decision by:** Eric Fitzgerald (human-made architectural decision)

## Context

TMI #956 flattens the diagram schemas: `Cell`, `BaseDiagram`,
`BaseDiagramInput` and the deprecated `Diagram` wrapper are removed, and
`DfdDiagram`, `DfdDiagramInput`, `Node` and `Edge` become standalone schemas.
The JSON on the wire is unchanged, but the generated client type names change,
so the API schema version bumps from 1.16.1 to 2.0.0. `versions.json` builds
only from `main`, so the first regeneration after the bump prunes the 1.16.1
client directories.

## Decision

Do not add a `release/1.x` branch to `versions.json`. The 1.16.1 clients are
dropped from the tree when the 2.0.0 clients are generated, and only 2.x
clients are maintained from then on.

## Consequences

- Nothing is unpublished. `tmi-client` 1.16.1 (PyPI), `@tmi-dev/client` 1.16.1
  (npm) and the `go-client-generated/v1_16_1` Go module (v1.16.1) stay
  available for 1.x servers; they just stop receiving fixes.
- Codegen patches that only applied to the 1.x schema shapes are removed:
  `patch_self_referential_discriminator` (Python), `patch_embedded_pointer_assignment`
  and `patch_embedded_model_unmarshal` (Go), and `patch_optional_extends`
  (TypeScript). Regenerating from the 2.0.0 spec with and without them produced
  identical output. Their regression checks stay, as behavior tests.
- Consumers that pick "the newest client at or above a floor" move to 2.0.0
  automatically and must handle the renamed types.
- Supporting a 1.x server again would mean re-adding a branch and restoring the
  removed patches from git history.
