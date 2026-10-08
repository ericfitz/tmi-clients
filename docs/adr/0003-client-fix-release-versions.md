# ADR 0003: Release client-only fixes by stamping the version at publish time

- **Status:** Accepted
- **Date:** 2026-10-08
- **Decision by:** Eric Fitzgerald (human-made architectural decision)

## Context

Each client directory is named for, and its package files carry, the
`info.version` of the spec it was generated from. The publish workflows took
the release tag's version as the directory name, so a fix to an
already-published client (the 2.0.0 Go and TypeScript fixes of 2026-10-08)
had no way to ship: a 2.0.1 tag looked for a 2.0.1 directory, and 2.0.0 was
already on the registries.

Alternatives considered: storing a separate release version in each
directory's package files and preserving it across regeneration; encoding a
fix digit as `major.minor.(patch*100 + fix)`.

## Decision

The release tag names the release version R. The publish workflow builds from
the committed directory with the same major.minor and the highest patch <= R,
and stamps R into that checkout's package metadata before building. Committed
files keep the spec version. This applies to the Python, npm and Go publish
workflows.

## Consequences

- A fix release is: merge the fix, then create a release tagged with the next
  free patch. No version-bump commit.
- Published packages can carry a version that appears nowhere in the repo;
  the release tag is the record.
- The Go module's embedded user agent keeps the spec version, because the
  module tag must point at a committed tree.
- A later spec version can collide with an already-released fix version
  (spec 2.0.1 after fix release 2.0.1). That release fails on the registry or
  module-tag check and is retried with the next free patch, which still
  resolves to the new directory.
