# TypeScript client: TypeScript 7 + Oxlint (design)

Status: approved by Eric 2026-11-26. Size: small change (short design).

## Intent

**Human decision (Eric, 2026-11-26): approach A.** Move the generated TypeScript client's dev toolchain
from TypeScript 6 + ESLint/typescript-eslint to TypeScript 7 + Oxlint without type-aware rules. Type-aware
linting (approach B) is deferred to issue #96.

Eric's goals:
1. Don't be pinned to older toolchains that are slow to patch. typescript-eslint 8.74.0 still declares
   peer `typescript ">=4.8.4 <6.1.0"` (typescript-eslint#10940 open), which holds the client on TS 6.
2. Faster builds, without sacrificing static analysis where practical.
3. A smaller toolchain that needs less CI maintenance.

## Current state

- `regenerate_ts.py` writes `package.json` devDependencies `@eslint/js`, `eslint`, `typescript ^6.0`,
  `typescript-eslint`, `vitest`, plus `eslint.config.mjs` (`js.configs.recommended` +
  `tseslint.configs.recommended`, no type-aware rules).
- Lint covers only the hand-written `test/` (one 352-line file); generated `src/` is excluded.
- Lint runs only during regeneration (`LINT_TS7_MARKER` logic skips it under TS 7). CI and `done_gate.sh`
  run build, `tsc -p tsconfig.test.json` and Vitest, not lint.
- The hold is mirrored in `.github/renovate.json` (`allowedVersions: "<7"`) and in
  `check_regen_drift.py` `HOLDS`.
- tsconfigs already use `node16` / `bundler` resolution, so TS 7's removal of `node10` does not bite.

## Approaches considered

| | Toolchain | Static analysis | Trade-off |
|---|---|---|---|
| **A (chosen)** | `typescript ^7`, `oxlint`, `vitest` | TS 7 type-check + Oxlint default correctness rules (roughly today's non-type-aware coverage) | 3 dev deps fewer; native and fast; no TS peer constraint |
| B (deferred, #96) | A + `oxlint-tsgolint` | adds type-aware rules | very frequent releases (Renovate churn); tied to typescript-go |
| C | `typescript ^7`, `vitest` | type-check only | smallest; loses lint rules tsc lacks |

Biome was dropped: its formatter is irrelevant for generated code and it has no type-aware rules.

## Design

1. `regenerate_ts.py`
   - devDependencies: `typescript ^7.0`, `oxlint` (current major caret, 1.x), `vitest ^5.0`. Remove
     `@eslint/js`, `eslint`, `typescript-eslint`.
   - `"lint": "oxlint --deny-warnings test"`; replace `ESLINT_CONFIG` / `eslint.config.mjs` with nothing unless Oxlint
     needs config (builder's call: defaults preferred; add `.oxlintrc.json` only for something concrete,
     e.g. the `process` global).
   - Controller ruling (2026-11-26, during execution, not a human decision): the script passes `--deny-warnings`
     because Oxlint exits 0 on warnings (its default `no-debugger` is a warning), so without the flag
     regeneration, CI and the done gate would pass on findings.
   - Remove the TS 6 pin comment block and the `LINT_TS7_MARKER` / `LINT_TS7_HINT` skip path; a lint
     failure is a regeneration issue (exit 2) like any other.
   - The backup/restore of custom files must not resurrect `eslint.config.mjs` in existing clients;
     regeneration should delete it.
2. Regenerate `typescript-client-generated/v3.0.0` from its committed `tmi-openapi.json` (no spec change;
   upstream spec work by the tmi agent is out of scope). Commit the new `package.json`, lockfile, removed
   `eslint.config.mjs`.
3. CI and done gate (my call, enabled by Oxlint's speed): add `npm run lint --if-present` to the `test-js`
   job in `ci.yml` and to the TypeScript loop in `done_gate.sh`; update the "ESLint cannot run" comment.
4. `.github/renovate.json`: remove the "Hold TypeScript at 6.x" rule. Oxlint falls into the existing
   node-packages group.
5. `check_regen_drift.py`: remove the `typescript` entry from `HOLDS` (keep the mechanism and its tests).

## Goals / non-goals / anti-goals

- Goal: the TS client builds, type-checks, lints and tests on TypeScript 7, locally and in CI.
- Non-goal: publishing a new npm release. Whether build output from TS 7 warrants a client fix release
  (ADR 0003) is Eric's call after this lands.
- Non-goal: changing the Python or Go clients, or type-aware lint (#96).
- Anti-goal: any change to the published package's API or emitted module formats (CJS `dist/` + ESM
  `dist/esm/` with declarations). The builder compares `dist/` file lists and `.d.ts` output before/after.

## Left to the builder

Oxlint config details, exact caret versions at implementation time, and fixing any new Oxlint findings in
`test/codegen_fixes.test.ts`.
