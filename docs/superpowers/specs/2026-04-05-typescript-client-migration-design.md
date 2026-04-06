# TypeScript Client Migration Design

**Date**: 2026-04-05
**Status**: Approved

## Summary

Migrate the JavaScript API client from swagger-codegen to openapi-generator with TypeScript output using the `typescript-fetch` generator. This is a rename-in-place migration: `javascript-client-generated/` becomes `typescript-client-generated/`.

## Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Generator variant | `typescript-fetch` | Zero runtime deps, native fetch works in Node 18+ and all modern browsers |
| Package name | `@tmiclient/client` | Keep existing name |
| Migration strategy | Rename-in-place | No custom business logic to preserve; clean swap |
| TypeScript target | ES2022 | Node 16+, modern browser support, top-level await |
| Approach | Minimal migration (A) | Matches successful Python migration pattern |

## Directory Structure

```
typescript-client-generated/
├── src/
│   ├── apis/                  # One file per API tag
│   ├── models/                # One file per schema
│   ├── runtime.ts             # Base HTTP client (fetch-based)
│   └── index.ts               # Barrel exports
├── scripts/
│   └── openapi-generator-config.json
├── package.json               # @tmiclient/client, ES2022
├── tsconfig.json
├── .openapi-generator-ignore
└── docs/
```

Key differences from the current JS client:

- No `superagent` dependency -- uses native `fetch`
- No Babel -- TypeScript compiler handles transpilation
- No `dist/` checked in -- consumers build from source or use compiled output

## Regeneration Script

Replace `regenerate_js.py` with `regenerate_ts.py`. Workflow:

1. Check prerequisites (`openapi-generator`, `node` 18+)
2. Download spec from GitHub (or accept local path)
3. Backup custom files (`.openapi-generator-ignore`, docs/developer/)
4. Clean old generated files (src/, docs/*.md)
5. Run `openapi-generator generate -g typescript-fetch`
6. Apply patches (initially none; add as codegen bugs surface)
7. Overwrite `package.json` and `tsconfig.json` with our canonical versions (openapi-generator's defaults lack our package name, ES2022 target, and dev tooling)
8. Restore backed-up custom files
9. Install deps via `npm install`
10. Build via `npx tsc` to verify compilation
11. Run tests if generated
12. Generate `REGENERATION_REPORT.md`
13. Cleanup backup directory

### openapi-generator Config

```json
{
  "npmName": "@tmiclient/client",
  "npmVersion": "1.0.0",
  "supportsES6": true,
  "typescriptThreePlus": true,
  "withInterfaces": true
}
```

### Patches

The three swagger-codegen patches are dropped (AllOf enum inheritance, enum export wrapping, constructor parameter forwarding) -- they were swagger-codegen-specific bugs. New patches will be added as openapi-generator bugs are discovered, following the same pattern as the Python client's `patch_regex_validators()` and `patch_test_return_types()`.

## Repo Updates

- Delete `javascript-client-generated/` directory entirely
- Delete `regenerate_js.py`
- Create `typescript-client-generated/` via openapi-generator
- Create `regenerate_ts.py`
- Update root `CLAUDE.md`:
  - Replace `javascript-client-generated/` references with `typescript-client-generated/`
  - Update generator references: swagger-codegen for Go only; openapi-generator for Python and TypeScript
  - Update regeneration commands section
- No end-user migration guide needed (JS client was never published to npm)

## Out of Scope

- Custom openapi-generator templates (can be added later if defaults are insufficient)
- Publishing to npm
- Changes to the Go client
- Changes to the Python client
