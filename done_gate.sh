#!/usr/bin/env bash
# Done gate: run locally what .github/workflows/ci.yml runs, for every
# committed client version directory. Exit 0 only if every step passes.
#
#   bash done_gate.sh
#
# Needs uv, go and node/npm on PATH (with nvm: `. ~/.nvm/nvm.sh` first).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

missing=()
for tool in uv go node npm; do
  command -v "$tool" >/dev/null 2>&1 || missing+=("$tool")
done
if ((${#missing[@]})); then
  echo "done_gate: missing on PATH: ${missing[*]} (for node/npm with nvm: . ~/.nvm/nvm.sh)" >&2
  exit 2
fi

shopt -s nullglob
py_dirs=("$ROOT"/python-client-generated/v[0-9]*/)
ts_dirs=("$ROOT"/typescript-client-generated/v[0-9]*/)
go_dirs=("$ROOT"/go-client-generated/v[0-9]*/)
if ((${#py_dirs[@]} == 0 || ${#ts_dirs[@]} == 0 || ${#go_dirs[@]} == 0)); then
  echo "done_gate: no client version directories found under $ROOT" >&2
  exit 2
fi

step() { printf '\n== %s\n' "$*"; }

for dir in "${py_dirs[@]}"; do
  step "python ${dir#"$ROOT"/}"
  code=0
  (cd "$dir" && uv run --with pytest python3 -m pytest test/ -q) || code=$?
  # pytest exit 5 = no tests collected; CI treats that as success.
  if ((code != 0 && code != 5)); then exit "$code"; fi
  (cd "$dir" && uv run python3 test_diagram_fixes.py)
done

for dir in "${ts_dirs[@]}"; do
  step "typescript ${dir#"$ROOT"/}"
  (cd "$dir" && npm ci --silent && npm run build --silent \
    && npm run typecheck --if-present --silent \
    && npm run test --if-present --silent -- --passWithNoTests)
done

for dir in "${go_dirs[@]}"; do
  step "go ${dir#"$ROOT"/}"
  (cd "$dir" && go build ./... && go vet ./... && go test ./...)
done

step "release scripts"
(cd "$ROOT" && uv run --with pytest python3 -m pytest .github/scripts/ -q)

printf '\ndone_gate: all checks passed\n'
