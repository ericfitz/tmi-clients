# Go lenient response decoding and client-only fix releases

- **Date:** 2026-10-08
- **Approved by:** Eric Fitzgerald (human-made decisions marked "Eric")
- **Requested by:** tmi-mcp (agentbus dm 1087)

## Part 1: Go client tolerates unknown response fields

### Problem

The generated Go client (`go-client-generated/v2_0_0`) rejects any response
that contains a field the client's spec does not know. A server newer than
the client that adds one response field (an additive, non-breaking API
change) makes every successful call return `GenericOpenAPIError`.

### Cause

openapi-generator's Go template (`go/model_simple.mustache`, 7.26.0) emits
`decoder.DisallowUnknownFields()` in `UnmarshalJSON` for every model that has
required properties, unless the schema declares `additionalProperties: true`.
The spec's `additionalProperties: false` is not the trigger: `Team` has no
`additionalProperties` key and is strict. 238 of 241 models are strict.
`utils.go`'s `newStrictDecoder`, used by oneOf wrappers, does the same.

### Constraint found while probing

Removing strictness alone breaks diagram cells. Go `Node.Shape` is a plain
`string` with only a regexp tag, and `Node` requires only `id` and `shape`, so
an edge payload decodes as a `Node` too and `DfdDiagramCellsInner` fails with
"data matches more than one schema". Today the unknown-field check on
`source`/`target` is what tells them apart. The other oneOf wrappers pair an
object with a primitive (`float32`/`string`) and stay disjoint.

### Design (Eric approved)

Post-generation patches in `regenerate_go.py`, applied to the committed
`v2_0_0` client without regenerating:

1. `patch_lenient_decoding`: remove `decoder.DisallowUnknownFields()` from
   every `model_*.go` and from `newStrictDecoder` in `utils.go` (keep the
   function name; its callers stay). Required-property checks are separate
   code and remain.
2. `patch_shape_enum_checks`: in `UnmarshalJSON` of `Node`, `MinimalNode`,
   `Edge` and `MinimalEdge`, reject a `shape` outside the schema's enum, with
   values read from the spec, not hard-coded. This replaces strictness as the
   cell discriminator.
3. Both patches are idempotent and warn (exit 2) if their anchor is missing.

Not chosen: stripping `additionalProperties: false` (no effect, see Cause);
`disallowAdditionalPropertiesIfNotPresent=false` (leaves explicit-false models
strict and adds an `AdditionalProperties` map to every struct); a template
override (a 700-line template to carry across generator upgrades).

Out of scope: unknown *enum values* in enum-typed fields still fail to decode.
Python (Pydantic default `extra="ignore"`) and TypeScript (`FromJSON` picks
named fields) already tolerate unknown fields.

## Part 2: Client-only fix releases

### Problem

A client is versioned and placed by its spec's `info.version`
(`v2.0.0/`, `v2_0_0/`). The publish workflows map the release tag version
straight to that directory, so a fix to the 2.0.0 client cannot be released:
`go-v2.0.1` looks for `v2_0_1/`. The version 2.0.0 is already published.

### Decision (Eric: "stamp at release", all three workflows)

Recorded in ADR 0003.

- The release tag (`python-vR`, `ts-vR`, `go-vR`) names the release version R.
- The workflow publishes from the committed directory with the same
  major.minor as R and the highest patch <= R's patch. No such directory is
  an error.
- Directory files keep the spec version. The workflow stamps R into the
  package metadata in its checkout before building (npm: `package.json` and
  `package-lock.json`; Python: every place the package version appears).
  Go has no version in `go.mod`; the module tag
  `go-client-generated/<dir>/vR` is the version.
- When a later spec version collides with a released fix version (spec 2.0.1
  after client fix 2.0.1), its release fails on the registry or tag check and
  takes the next free patch.
- The resolution rule lives in one stdlib-only script with its own tests,
  called by all three workflows.
