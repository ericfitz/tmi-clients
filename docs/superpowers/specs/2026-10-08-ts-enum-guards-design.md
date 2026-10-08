# TypeScript client: check enum values in all instanceOf guards

## Problem

openapi-generator (typescript-fetch) emits a value check in `instanceOfX()` for a
required enum property only when the enum has a single value (`Edge.shape === 'flow'`).
For multi-value enums it emits a presence check only, so `instanceOfNode()` returned
true for an edge. `patch_enum_guards` in `regenerate_ts.py` covered only
`Node.shape` and `MinimalNode.shape` from a hand table; 41 other required
multi-value enum guards (e.g. `Asset.type`, `Authorization.role`,
`JsonPatchDocumentInner.op`) were still presence-only.

## Decision (human-made, Eric, 2026-10-08)

Tighten every required multi-value enum guard, discovered automatically from each
model file, except `EdgeRouterOneOf.name` and `EdgeConnectorOneOf.name`, which stay
presence-only. Released later as ts-v2.0.2.

## Exemption rationale

Those two guards drive oneOf dispatch in `EdgeRouter.ts` / `EdgeConnector.ts`. The
object member is paired only with a string, and the fallback is `return {} as any`.
Tightening them would turn an unrecognized router or connector name from a future
API version into a silently emptied object instead of passing it through.

## Behavior change

`instanceOfX()` now returns false for a required enum property whose value is unknown
to this client version. Code that used these guards to accept objects from a newer
server will see them rejected. `FromJSON` conversions are unaffected (no other
generated code calls these guards; dispatch uses only the two exempt ones).

## Safeguards

- `patch_enum_guards` warns (exit 2) if an exempt entry disappears or discovery finds
  zero guards, and skips (with a warning) enums with non-string or escaped values.
- `codegen_fixes.test.ts` scans the models at test time and fails if any required
  multi-value enum guard other than the two exempt ones is presence-only.
