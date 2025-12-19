# TMI Go Client Regeneration Guide

This directory contains automated tools for regenerating the TMI Go client from the OpenAPI specification with intelligent defaults.

## Quick Start

```bash
cd go-client-generated
./scripts/regenerate_client.sh
```

That's it! The script automatically applies all modern Go configurations and dependency updates.

## Automatic Defaults

The regeneration process automatically applies these intelligent defaults:

### Package Configuration
- **Package name**: `tmiclient`
- **Module path**: `github.com/efitz/tmi-clients/go-client-generated`
- **Package version**: `1.0.0`
- **Enum class prefix**: `true` (for type safety)
- **go.mod enabled**: `true` (modern module support)

### Go Version
- **Minimum Go**: `1.21+`
- **Recommended**: Go 1.21 or higher for LTS support
- **Reason**: Modern generics support, performance improvements, security fixes

### Dependency Versions (Modern & Secure)

All dependencies are automatically managed via go.mod:

| Package | Version | Reason |
|---------|---------|--------|
| `golang.org/x/oauth2` | v0.32.0+ | Latest OAuth2 support, security fixes |
| `github.com/antihax/optional` | v1.0.0 | Optional parameter support |

### Code Generation Settings
- **with Go codegen comment**: `true` (transparency)
- **with XML**: `false` (JSON-only API)
- **prepend form/body parameters**: `false` (cleaner method signatures)
- **is Go submodule**: `false` (standalone module)

### Critical Features

The script handles:
1. ✅ Automatic backup of custom files (go.mod, tests, docs)
2. ✅ Clean regeneration (removes old generated files)
3. ✅ Module path configuration
4. ✅ Dependency management (`go mod tidy`)
5. ✅ Build verification
6. ✅ Test execution (if tests exist)
7. ✅ Detailed report generation

## Files

### Configuration Files

#### `scripts/swagger-codegen-config.json`
```json
{
  "packageName": "tmiclient",
  "packageVersion": "1.0.0",
  "enumClassPrefix": true,
  "withGoCodegenComment": true,
  "withXml": false,
  "prependFormOrBodyParameters": false,
  "isGoSubmodule": false,
  "withGoMod": true
}
```

**Purpose**: Tells swagger-codegen how to generate the Go client with correct naming and module support.

### Regeneration Script

#### `scripts/regenerate_client.sh`
**Purpose**: Fully automated regeneration with all updates.

**What it does**:
1. ✅ Validates prerequisites (swagger-codegen, Go 1.21+)
2. ✅ Backs up custom files (go.mod, tests, docs)
3. ✅ Cleans generated Go files
4. ✅ Runs swagger-codegen with configuration
5. ✅ Updates go.mod with correct module path and Go version
6. ✅ Runs `go mod tidy` to update dependencies
7. ✅ Verifies build with `go build ./...`
8. ✅ Runs tests if they exist
9. ✅ Runs integration tests if they exist
10. ✅ Generates summary report

**Exit codes**:
- `0`: Success - build passed
- `1`: Failure - build failed, check logs

## Prerequisites

### Required Tools

```bash
# Install swagger-codegen
brew install swagger-codegen

# Install Go 1.21+
brew install go

# Verify installations
swagger-codegen version  # Should be >= 3.0.75
go version              # Should be >= 1.21.0
```

### Required Files

- OpenAPI spec: `/Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json`
- Must be valid OpenAPI 3.0+ specification

## Usage

### Basic Regeneration

```bash
# From the go-client-generated directory
./scripts/regenerate_client.sh
```

### Verify Results

```bash
# Check the report
cat REGENERATION_REPORT.md

# Build manually
go build ./...

# Run tests manually
go test -v ./...

# Check dependencies
go list -m all
```

### Output Files

After regeneration, you'll find:

```
go-client-generated/
├── model_*.go              # 100+ model files
├── api_*.go                # 14+ API service files
├── client.go               # Main API client
├── configuration.go        # Client configuration
├── response.go             # Response utilities
├── go.mod                  # Module definition (updated)
├── go.sum                  # Dependency checksums
├── docs/                   # Auto-generated documentation
│   └── developer/          # Custom developer docs (preserved)
├── *_test.go               # Test files (if created)
└── diagram_fixes_test.go   # Integration tests (if created)

REGENERATION_REPORT.md      # Detailed report
build_output.log            # Build results
test_output.log             # Test results (if tests exist)
integration_test_output.log # Integration test results (if tests exist)
```

## What Gets Preserved

The script automatically preserves:

- ✅ `go.mod` (module path and dependencies)
- ✅ `go.sum` (dependency checksums)
- ✅ `*_test.go` (custom test files)
- ✅ `docs/developer/` (custom documentation)
- ✅ `.swagger-codegen-ignore` (if exists)

All other files are regenerated from scratch.

## What Gets Updated

### Always Updated
- All model files (`model_*.go`)
- All API files (`api_*.go`)
- Core client files (`client.go`, `configuration.go`, `response.go`)
- Auto-generated documentation (`docs/*.md`)

### Automatically Updated
- `go.mod` - Module path and Go version corrected
- Dependencies - Updated via `go mod tidy`

## Customization

### Change Package Name

Edit `scripts/swagger-codegen-config.json`:
```json
{
  "packageName": "tmi",  // Change here
  "packageVersion": "1.1.0"
}
```

### Change Module Path

Edit `scripts/regenerate_client.sh` around line 109:
```bash
sed -i.bak 's|module .*|module github.com/your-org/tmi-go-client|' "$CLIENT_DIR/go.mod"
```

### Change Go Minimum Version

Edit `scripts/regenerate_client.sh` around line 112:
```bash
sed -i.bak 's|go [0-9.]*|go 1.22|' "$CLIENT_DIR/go.mod"
```

### Add Custom Dependencies

After regeneration, add to go.mod and run:
```bash
go get github.com/your/package@version
go mod tidy
```

## Troubleshooting

### "swagger-codegen not found"

```bash
brew install swagger-codegen
```

### "OpenAPI spec not found"

Check that the spec exists:
```bash
ls -lh /Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json
```

If it's in a different location, edit `scripts/regenerate_client.sh` line 27:
```bash
OPENAPI_SPEC="/path/to/your/tmi-openapi.json"
```

### "Go not found" or version too old

```bash
# Install latest Go
brew install go

# Or upgrade
brew upgrade go

# Verify
go version
```

### Build Fails After Regeneration

1. Check `build_output.log` for details
2. Verify OpenAPI spec is valid
3. Check if new breaking changes in spec
4. Review `REGENERATION_REPORT.md`
5. Try: `go mod tidy && go build ./...`

### Dependency Issues

```bash
# Clean and rebuild
go clean -modcache
go mod tidy
go build ./...
```

### Import Path Errors

If you get import errors, verify `go.mod` has correct module path:
```bash
# Should be:
module github.com/efitz/tmi-clients/go-client-generated
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Regenerate TMI Go Client

on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly on Sunday
  workflow_dispatch:

jobs:
  regenerate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Go
        uses: actions/setup-go@v4
        with:
          go-version: '1.21'

      - name: Install swagger-codegen
        run: |
          wget https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.75/swagger-codegen-cli-3.0.75.jar -O swagger-codegen-cli.jar
          echo "alias swagger-codegen='java -jar swagger-codegen-cli.jar'" >> ~/.bashrc

      - name: Regenerate client
        run: |
          cd go-client-generated
          ./scripts/regenerate_client.sh

      - name: Create PR
        uses: peter-evans/create-pull-request@v5
        with:
          title: "chore: regenerate TMI Go client"
          body: "Automated client regeneration from latest OpenAPI spec"
          branch: "automated/regenerate-go-client"
```

## Version History

### 1.0.0 (2025-01-12)
- Initial automated regeneration script
- Go 1.21+ support
- Modern dependency management
- Webhook API support
- Input schema support

## Best Practices

### Before Regeneration
- [ ] Commit any local changes
- [ ] Update OpenAPI spec to latest version
- [ ] Review spec for breaking changes
- [ ] Back up custom code if any

### After Regeneration
- [ ] Review `REGENERATION_REPORT.md`
- [ ] Check build results (`go build ./...`)
- [ ] Review git diff for unexpected changes
- [ ] Verify new models exist (DfdDiagramInput, webhook models)
- [ ] Update CHANGELOG.md if needed
- [ ] Test with dependent projects
- [ ] Create PR for review

### Frequency
- **On OpenAPI spec changes**: Always regenerate
- **Dependency updates**: Quarterly `go get -u && go mod tidy`
- **Go version updates**: When new LTS released
- **Regular maintenance**: Quarterly regeneration
- **Before releases**: Always regenerate and test

## Go-Specific Considerations

### Type Safety vs. Flexibility

**Go advantages**:
- Strong typing catches errors at compile time
- Excellent IDE support with autocomplete
- Clear interfaces and method signatures

**Trade-offs**:
- Nested cell classes provide type safety (unlike JS inline objects)
- May be more verbose than dynamic languages
- Null/optional handling requires careful consideration

### Pointer vs. Value Types

Generated models use pointers for optional fields:
```go
type DfdDiagram struct {
    Type      *string  // Optional with pointer
    Name      string   // Required without pointer
    Cells     []Cell   // Slice is reference type
    CreatedAt *string  // Optional timestamp
}
```

**Best practice**: Check for nil before dereferencing:
```go
if diagram.CreatedAt != nil {
    fmt.Println(*diagram.CreatedAt)
}
```

### Error Handling

Go API methods return three values:
```go
diagram, resp, err := api.GetThreatModelDiagram(ctx, tmId, diagramId)
if err != nil {
    // Handle error
    return err
}
// Use diagram
```

Always check `err` before using the result.

### Context Support

All API methods accept `context.Context` for cancellation and timeouts:
```go
ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
defer cancel()

diagram, _, err := api.GetThreatModelDiagram(ctx, tmId, diagramId)
```

## Support

For issues with regeneration:

1. Check this README
2. Review `REGENERATION_REPORT.md` after running
3. Check `build_output.log` for build failures
4. See [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) for usage
5. See [CHANGELOG.md](CHANGELOG.md) for version history

## License

Apache-2.0 (same as TMI project)
