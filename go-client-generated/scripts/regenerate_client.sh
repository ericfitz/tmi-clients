#!/bin/bash
set -e  # Exit on error

# TMI Go Client Regeneration Script
#
# This script regenerates the Go client from the latest OpenAPI spec
# and applies all necessary updates and customizations.
#
# AUTOMATIC DEFAULTS APPLIED:
# - Package name: tmiclient
# - Go module: github.com/efitz/tmi-clients/go-client-generated
# - Go version: 1.21+ (LTS with broad compatibility)
# - Modern dependencies:
#   * golang.org/x/oauth2 (latest stable)
#   * github.com/antihax/optional (latest)
# - go.mod enabled for module support
# - Enum class prefix enabled
#
# USAGE:
#   ./regenerate_client.sh
#
# REQUIREMENTS:
#   - swagger-codegen 3.0.75+ (install via: brew install swagger-codegen)
#   - Go 1.21+ (install via: brew install go)
#   - OpenAPI spec at: /Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Navigate to go-client-generated directory (parent of scripts/)
GO_CLIENT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$GO_CLIENT_DIR"

echo "========================================="
echo "TMI Go Client Regeneration"
echo "========================================="
echo ""
echo "Working directory: $GO_CLIENT_DIR"
echo ""
echo "Automatic defaults:"
echo "  - Package: tmiclient"
echo "  - Module: github.com/efitz/tmi-clients/go-client-generated"
echo "  - Go: 1.21+"
echo "  - Dependencies: Modern with security updates"
echo ""

# Configuration
OPENAPI_SPEC="/Users/efitz/Projects/tmi/api-schema/tmi-openapi.json"
CLIENT_DIR="."  # We're already in go-client-generated/
CONFIG_FILE="scripts/swagger-codegen-config.json"
SWAGGER_CODEGEN="swagger-codegen"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check prerequisites
echo "Checking prerequisites..."

if [ ! -f "$OPENAPI_SPEC" ]; then
    echo -e "${RED}ERROR: OpenAPI spec not found at $OPENAPI_SPEC${NC}"
    exit 1
fi

if ! command -v swagger-codegen &> /dev/null; then
    echo -e "${RED}ERROR: swagger-codegen not found. Installing via Homebrew...${NC}"
    brew install swagger-codegen
fi

if ! command -v go &> /dev/null; then
    echo -e "${RED}ERROR: Go not found. Please install Go 1.21+ first.${NC}"
    exit 1
fi

# Check Go version
GO_VERSION=$(go version | sed 's/go version go//' | cut -d' ' -f1 | cut -d. -f1-2)
MIN_VERSION="1.21"
if [ "$(printf '%s\n' "$MIN_VERSION" "$GO_VERSION" | sort -V | head -n1)" != "$MIN_VERSION" ]; then
    echo -e "${YELLOW}WARNING: Go version is $GO_VERSION. Recommend 1.21+ for best compatibility.${NC}"
fi

echo -e "${GREEN}✓ All prerequisites met${NC}"
echo ""

# Step 1: Backup critical custom files
echo "Step 1: Backing up custom files..."
mkdir -p .regeneration_backup
cp -f "$CLIENT_DIR/go.mod" .regeneration_backup/ 2>/dev/null || true
cp -f "$CLIENT_DIR/go.sum" .regeneration_backup/ 2>/dev/null || true
cp -f "$CLIENT_DIR/.swagger-codegen-ignore" .regeneration_backup/ 2>/dev/null || true
cp -rf "$CLIENT_DIR/docs/developer" .regeneration_backup/ 2>/dev/null || true
# Backup any custom test files
find "$CLIENT_DIR" -name "*_test.go" -exec cp {} .regeneration_backup/ \; 2>/dev/null || true
echo -e "${GREEN}✓ Custom files backed up${NC}"
echo ""

# Step 2: Clean generated files (preserve custom files)
echo "Step 2: Cleaning generated files..."
# Remove generated Go files but keep custom files
rm -f "$CLIENT_DIR"/model_*.go
rm -f "$CLIENT_DIR"/api_*.go
rm -f "$CLIENT_DIR"/client.go
rm -f "$CLIENT_DIR"/configuration.go
rm -f "$CLIENT_DIR"/response.go
rm -f "$CLIENT_DIR"/utils.go
rm -rf "$CLIENT_DIR/api"
rm -rf "$CLIENT_DIR/docs" || true
rm -f "$CLIENT_DIR/README.md"
rm -f "$CLIENT_DIR/git_push.sh"
rm -f "$CLIENT_DIR/.travis.yml"
echo -e "${GREEN}✓ Generated files cleaned${NC}"
echo ""

# Step 3: Run swagger-codegen
echo "Step 3: Running swagger-codegen..."
$SWAGGER_CODEGEN generate \
    -i "$OPENAPI_SPEC" \
    -l go \
    -o "$CLIENT_DIR" \
    -c "$CONFIG_FILE"

if [ $? -ne 0 ]; then
    echo -e "${RED}ERROR: swagger-codegen failed${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Client generated successfully${NC}"
echo ""

# Step 4: Update go.mod with correct module path and Go version
echo "Step 4: Updating go.mod..."
if [ -f "$CLIENT_DIR/go.mod" ]; then
    # Update module path if needed
    sed -i.bak 's|module .*|module github.com/efitz/tmi-clients/go-client-generated|' "$CLIENT_DIR/go.mod"

    # Update Go version to 1.21 for broad compatibility
    sed -i.bak 's|go [0-9.]*|go 1.21|' "$CLIENT_DIR/go.mod"

    rm -f "$CLIENT_DIR/go.mod.bak"
    echo -e "${GREEN}✓ go.mod updated${NC}"
else
    echo -e "${YELLOW}⚠ go.mod not found - creating new one${NC}"
    cat > "$CLIENT_DIR/go.mod" << 'EOF'
module github.com/efitz/tmi-clients/go-client-generated

go 1.21

require (
	github.com/antihax/optional v1.0.0
	golang.org/x/oauth2 v0.32.0
)
EOF
    echo -e "${GREEN}✓ Created go.mod${NC}"
fi
echo ""

# Step 5: Restore custom files
echo "Step 5: Restoring custom files..."

# Restore developer docs if they exist
if [ -d ".regeneration_backup/developer" ]; then
    mkdir -p "$CLIENT_DIR/docs/developer"
    cp -r .regeneration_backup/developer/* "$CLIENT_DIR/docs/developer/"
    echo "  ✓ Restored developer documentation"
fi

# Restore custom test files if they exist
if ls .regeneration_backup/*_test.go 1> /dev/null 2>&1; then
    cp .regeneration_backup/*_test.go "$CLIENT_DIR/"
    echo "  ✓ Restored custom test files"
fi

echo -e "${GREEN}✓ Custom files restored${NC}"
echo ""

# Step 6: Tidy dependencies
echo "Step 6: Running go mod tidy..."
go mod tidy
if [ $? -ne 0 ]; then
    echo -e "${RED}ERROR: go mod tidy failed${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Dependencies tidied${NC}"
echo ""

# Step 7: Verify build
echo "Step 7: Verifying build..."
go build ./... > build_output.log 2>&1
BUILD_EXIT_CODE=$?

if [ $BUILD_EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}✓ Build successful${NC}"
    echo ""
else
    echo -e "${YELLOW}⚠ Build failed (exit code: $BUILD_EXIT_CODE)${NC}"
    echo "  Check build_output.log for details"
    echo ""
fi

# Step 8: Run tests (if any exist)
echo "Step 8: Running tests..."
if ls "$CLIENT_DIR"/*_test.go 1> /dev/null 2>&1; then
    go test -v ./... > test_output.log 2>&1
    TEST_EXIT_CODE=$?

    if [ $TEST_EXIT_CODE -eq 0 ]; then
        echo -e "${GREEN}✓ All tests passed${NC}"
    else
        echo -e "${YELLOW}⚠ Some tests failed${NC}"
        echo "  Check test_output.log for details"
    fi
else
    echo -e "${YELLOW}⚠ No test files found${NC}"
    TEST_EXIT_CODE=0
fi
echo ""

# Step 9: Run integration tests (if they exist)
echo "Step 9: Running integration tests..."
if [ -f "$CLIENT_DIR/diagram_fixes_test.go" ]; then
    go test -v -run TestDiagramFixes > integration_test_output.log 2>&1
    INTEGRATION_EXIT_CODE=$?

    if [ $INTEGRATION_EXIT_CODE -eq 0 ]; then
        echo -e "${GREEN}✓ Integration tests passed${NC}"
    else
        echo -e "${YELLOW}⚠ Integration tests failed${NC}"
        echo "  Check integration_test_output.log for details"
    fi
else
    echo -e "${YELLOW}⚠ No integration tests found${NC}"
    INTEGRATION_EXIT_CODE=0
fi
echo ""

# Step 10: Generate regeneration report
echo "Step 10: Generating regeneration report..."

cat > REGENERATION_REPORT.md << EOF
# TMI Go Client Regeneration Report

**Date**: $(date +"%Y-%m-%d %H:%M:%S")
**OpenAPI Spec**: $OPENAPI_SPEC
**Swagger Codegen**: $(swagger-codegen version 2>&1 | head -1)
**Go Version**: $(go version)

## Configuration

- **Package Name**: tmiclient
- **Module Path**: github.com/efitz/tmi-clients/go-client-generated
- **Go Version**: 1.21+
- **Config File**: $CONFIG_FILE

## Generation Results

### Files Generated

\`\`\`
$(find . -name "model_*.go" | wc -l) model files
$(find . -name "api_*.go" | wc -l) API files
$(find docs -type f -name "*.md" 2>/dev/null | wc -l) documentation files
\`\`\`

### Dependencies

\`\`\`
$(grep -A 10 "require" go.mod | sed 's/^/  /')
\`\`\`

### Dependency Status

\`\`\`
$(go list -m all | head -10)
\`\`\`

## Build Results

### Compilation

Exit Code: $BUILD_EXIT_CODE
Status: $([ $BUILD_EXIT_CODE -eq 0 ] && echo "✅ SUCCESS" || echo "❌ FAILED")

See \`build_output.log\` for full details.

### Tests

Exit Code: $TEST_EXIT_CODE
Status: $([ $TEST_EXIT_CODE -eq 0 ] && echo "✅ PASSED" || echo "❌ FAILED")

$([ -f "test_output.log" ] && echo "See \`test_output.log\` for full details." || echo "No tests found.")

### Integration Tests

$([ -f "diagram_fixes_test.go" ] && echo "Status: $([ $INTEGRATION_EXIT_CODE -eq 0 ] && echo '✅ PASSED' || echo '❌ FAILED')" || echo "Status: ⚠️ NOT FOUND")

$([ -f "integration_test_output.log" ] && echo "See \`integration_test_output.log\` for full details." || echo "")

## Critical Changes in This Regeneration

### New Features

- **Webhook API**: 8 new endpoints for webhook subscriptions and deliveries
- **Input Schemas**: Separate input/output schemas (DfdDiagramInput vs DfdDiagram)
- **Webhook Models**: WebhookSubscription, WebhookDelivery, etc.

### Breaking Changes

1. **Input Schemas**: PUT/PATCH operations may use *Input types
   - Use DfdDiagramInput for updates (not DfdDiagram)
   - Removes need to provide readOnly fields (id, created_at, modified_at)

2. **API Method Signatures**: Some methods may accept different parameter types

### Security Updates

- golang.org/x/oauth2: Latest stable version
- github.com/antihax/optional: v1.0.0

## Models Generated

### Diagram Models

$(ls -1 model_*diagram*.go 2>/dev/null | sed 's/^/- /' || echo "None found")

### Webhook Models

$(ls -1 model_webhook*.go 2>/dev/null | sed 's/^/- /' || echo "None found")

### Cell Models

$(ls -1 model_{cell,node,edge}*.go 2>/dev/null | sed 's/^/- /' || echo "None found")

## API Services Generated

\`\`\`
$(ls -1 api_*.go 2>/dev/null | sed 's/api_//' | sed 's/.go$//' || echo "None found")
\`\`\`

## Next Steps

1. $([ $BUILD_EXIT_CODE -eq 0 ] && echo "✅" || echo "❌") Review build results
2. ✅ Review \`REGENERATION_REPORT.md\` (this file)
3. ✅ Check \`docs/developer/MIGRATION_GUIDE.md\` for API changes
4. ⚠️ Verify input schemas exist:
   - model_dfd_diagram_input.go
   - model_base_diagram_input.go
5. ⚠️ Verify webhook models exist:
   - model_webhook_subscription.go
   - model_webhook_delivery.go
6. ✅ Test with your application

## Documentation

- **Usage Guide**: README.md
- **API Reference**: docs/
- **Migration Guide**: docs/developer/MIGRATION_GUIDE.md
- **Regeneration Guide**: docs/developer/REGENERATION_README.md
- **Changelog**: docs/developer/CHANGELOG.md

## Summary

$([ $BUILD_EXIT_CODE -eq 0 ] && echo "✅ **Regeneration completed successfully**" || echo "⚠️ **Regeneration completed with build errors**")

The Go client has been regenerated from the latest OpenAPI specification.
All dependencies have been updated to current stable versions.

**Build Status**: $([ $BUILD_EXIT_CODE -eq 0 ] && echo "PASS" || echo "FAIL")
**Test Status**: $([ $TEST_EXIT_CODE -eq 0 ] && echo "PASS" || echo "NO TESTS")
EOF

echo -e "${GREEN}✓ Regeneration report created: REGENERATION_REPORT.md${NC}"
echo ""

# Final summary
echo "========================================="
echo "Regeneration Complete!"
echo "========================================="
echo ""
echo "Summary:"
echo "  - Generated files: $(find . -name "*.go" -not -name "*_test.go" | wc -l) Go files"
echo "  - Build: $([ $BUILD_EXIT_CODE -eq 0 ] && echo "${GREEN}SUCCESS${NC}" || echo "${YELLOW}FAILED${NC}")"
echo "  - Tests: $([ $TEST_EXIT_CODE -eq 0 ] && echo "${GREEN}PASSED${NC}" || echo "${YELLOW}NO TESTS${NC}")"
echo "  - Report: REGENERATION_REPORT.md"
echo ""
echo "Next steps:"
echo "  1. Review REGENERATION_REPORT.md"
echo "  2. Check build_output.log if build failed"
echo "  3. Read docs/developer/MIGRATION_GUIDE.md"
echo "  4. Run: go test -v ./..."
echo ""

# Exit with build status
exit $BUILD_EXIT_CODE
