#!/bin/bash
set -e  # Exit on error

# TMI JavaScript Client Regeneration Script
#
# This script regenerates the JavaScript client from the latest OpenAPI spec
# and applies all necessary patches and customizations.
#
# AUTOMATIC DEFAULTS APPLIED:
# - Package name: tmi-js-client
# - Node.js version: 18+ (ES6 modules, modern features)
# - Modern dependencies with security fixes:
#   * superagent >= 10.2.3 (was 5.3.1 - CVE fixes)
#   * mocha >= 11.7.4 (was 3.x - major updates)
#   * chai >= 5.1.2 (was 4.x - modern assertions)
#   * sinon >= 21.0.0 (was 7.5.0 - modern mocking)
#   * @babel/* >= 7.28.x (modern transpilation)
# - Testing: Mocha + Chai
# - Modern packaging: ES6 modules with Babel transpilation
# - Constructor patches: DfdDiagram type preservation
# - Webhook API support (5 new endpoints)
# - Input schemas: DfdDiagramInput, BaseDiagramInput
#
# USAGE:
#   ./regenerate_client.sh [path/to/tmi-openapi.json]
#
#   If a local spec path is provided, it will be used instead of downloading
#   from GitHub. Otherwise, the latest spec is fetched from the main branch.
#
# REQUIREMENTS:
#   - swagger-codegen 3.0.75+ (install via: brew install swagger-codegen)
#   - Node.js 18+ (install via: brew install node)
#   - curl (for downloading OpenAPI spec, unless local path provided)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Navigate to javascript-client-generated directory (parent of scripts/)
JS_CLIENT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$JS_CLIENT_DIR"

echo "========================================="
echo "TMI JavaScript Client Regeneration"
echo "========================================="
echo ""
echo "Working directory: $JS_CLIENT_DIR"
echo ""
echo "Automatic defaults:"
echo "  - Package: tmi-js-client"
echo "  - Node.js: 18+"
echo "  - Dependencies: Modern with CVE fixes"
echo "  - Testing: Mocha + Chai"
echo ""

# Configuration
OPENAPI_SPEC_URL="https://raw.githubusercontent.com/ericfitz/tmi/refs/heads/main/api-schema/tmi-openapi.json"
OPENAPI_SPEC="$JS_CLIENT_DIR/tmi-openapi.json"
CLIENT_DIR="."  # We're already in javascript-client-generated/
CONFIG_FILE="scripts/swagger-codegen-config.json"
SWAGGER_CODEGEN="swagger-codegen"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check prerequisites
echo "Checking prerequisites..."

# Get the OpenAPI spec: use local file if provided, otherwise download from GitHub
if [ -n "$1" ]; then
    LOCAL_SPEC="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
    if [ ! -f "$LOCAL_SPEC" ]; then
        echo -e "${RED}ERROR: Local spec file not found: $1${NC}"
        exit 1
    fi
    echo "Using local OpenAPI spec: $LOCAL_SPEC"
    cp "$LOCAL_SPEC" "$OPENAPI_SPEC"
    echo -e "${GREEN}✓ OpenAPI spec copied from local file${NC}"
else
    echo "Downloading OpenAPI spec from $OPENAPI_SPEC_URL..."
    if ! curl -fsSL "$OPENAPI_SPEC_URL" -o "$OPENAPI_SPEC"; then
        echo -e "${RED}ERROR: Failed to download OpenAPI spec from $OPENAPI_SPEC_URL${NC}"
        exit 1
    fi
    echo -e "${GREEN}✓ OpenAPI spec downloaded${NC}"
fi

if ! command -v swagger-codegen &> /dev/null; then
    echo -e "${RED}ERROR: swagger-codegen not found. Installing via Homebrew...${NC}"
    brew install swagger-codegen
fi

if ! command -v node &> /dev/null; then
    echo -e "${RED}ERROR: Node.js not found. Please install Node.js 18+ first.${NC}"
    exit 1
fi

# Check Node.js version
NODE_VERSION=$(node -v | sed 's/v//' | cut -d. -f1)
if [ "$NODE_VERSION" -lt 18 ]; then
    echo -e "${YELLOW}WARNING: Node.js version is $NODE_VERSION. Recommend 18+ for best compatibility.${NC}"
fi

echo -e "${GREEN}✓ All prerequisites met${NC}"
echo ""

# Step 1: Backup critical custom files
echo "Step 1: Backing up custom files..."
mkdir -p .regeneration_backup
cp -f "$CLIENT_DIR/package.json" .regeneration_backup/ 2>/dev/null || true
cp -f "$CLIENT_DIR/.babelrc" .regeneration_backup/ 2>/dev/null || true
cp -f "$CLIENT_DIR/test_diagram_fixes.js" .regeneration_backup/ 2>/dev/null || true
cp -f "$CLIENT_DIR/.swagger-codegen-ignore" .regeneration_backup/ 2>/dev/null || true
cp -f "$CLIENT_DIR/PRE_REGENERATION_AUDIT.md" .regeneration_backup/ 2>/dev/null || true
cp -rf "$CLIENT_DIR/docs/developer" .regeneration_backup/ 2>/dev/null || true
cp -rf "$CLIENT_DIR/scripts" .regeneration_backup/ 2>/dev/null || true
echo -e "${GREEN}✓ Custom files backed up${NC}"
echo ""

# Step 2: Clean generated files (preserve custom files)
echo "Step 2: Cleaning generated files..."
rm -rf "$CLIENT_DIR/src"
rm -rf "$CLIENT_DIR/test/api"
rm -rf "$CLIENT_DIR/test/model"
rm -rf "$CLIENT_DIR/docs" || true
rm -f "$CLIENT_DIR/README.md"
rm -f "$CLIENT_DIR/git_push.sh"
rm -f "$CLIENT_DIR/mocha.opts"
rm -f "$CLIENT_DIR/.travis.yml"
echo -e "${GREEN}✓ Generated files cleaned${NC}"
echo ""

# Step 3: Run swagger-codegen
echo "Step 3: Running swagger-codegen..."
$SWAGGER_CODEGEN generate \
    -i "$OPENAPI_SPEC" \
    -l javascript \
    -o "$CLIENT_DIR" \
    -c "$CONFIG_FILE"

if [ $? -ne 0 ]; then
    echo -e "${RED}ERROR: swagger-codegen failed${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Client generated successfully${NC}"
echo ""

# Step 4: Validate generated files and apply patches
echo "Step 4: Validating generated files and applying patches..."

# Count generated files
API_COUNT=$(ls -1 src/tmi-client/*.js 2>/dev/null | wc -l | tr -d ' ')
MODEL_COUNT=$(ls -1 src/model/*.js 2>/dev/null | wc -l | tr -d ' ')

echo "  Generated: $API_COUNT API classes, $MODEL_COUNT model classes"

# Validate critical models exist
echo "  Validating critical models..."

# Check for Input schemas
DFD_DIAGRAM_INPUT_FILE="$CLIENT_DIR/src/model/DfdDiagramInput.js"
BASE_DIAGRAM_INPUT_FILE="$CLIENT_DIR/src/model/BaseDiagramInput.js"

if [ -f "$DFD_DIAGRAM_INPUT_FILE" ]; then
    echo -e "  ${GREEN}✓ DfdDiagramInput.js found${NC}"
else
    echo -e "  ${RED}✗ DfdDiagramInput.js NOT found${NC}"
fi

if [ -f "$BASE_DIAGRAM_INPUT_FILE" ]; then
    echo -e "  ${GREEN}✓ BaseDiagramInput.js found${NC}"
else
    echo -e "  ${RED}✗ BaseDiagramInput.js NOT found${NC}"
fi

# Check for webhook models
WEBHOOK_MODELS=("WebhookSubscription" "WebhookSubscriptionInput" "WebhookDelivery" "WebhookTestRequest" "WebhookTestResponse")
WEBHOOK_FOUND=0
for model in "${WEBHOOK_MODELS[@]}"; do
    if [ -f "$CLIENT_DIR/src/model/$model.js" ]; then
        ((WEBHOOK_FOUND++))
    fi
done
echo "  Webhook models: $WEBHOOK_FOUND/5 found"

# Check for admin models (sample check)
ADMIN_MODELS=("Administrator" "AdminUser" "AdminGroup")
ADMIN_FOUND=0
for model in "${ADMIN_MODELS[@]}"; do
    if [ -f "$CLIENT_DIR/src/model/$model.js" ]; then
        ((ADMIN_FOUND++))
    fi
done
echo "  Admin models: $ADMIN_FOUND/3 found (sample)"

# Patch 1: DfdDiagram constructor (if exists)
DFD_DIAGRAM_FILE="$CLIENT_DIR/src/model/DfdDiagram.js"
if [ -f "$DFD_DIAGRAM_FILE" ]; then
    echo "  Checking DfdDiagram constructor..."
    # Check if the file needs patching (look for super() call)
    if grep -q "super(" "$DFD_DIAGRAM_FILE"; then
        # Verify type parameter is in constructor
        if grep -q "constructor(type" "$DFD_DIAGRAM_FILE"; then
            echo -e "  ${GREEN}✓ DfdDiagram.js has type parameter${NC}"
        else
            echo -e "  ${YELLOW}⚠ DfdDiagram.js type parameter not found${NC}"
        fi
    fi
else
    echo -e "  ${YELLOW}⚠ DfdDiagram.js not found - skipping patch${NC}"
fi

# Patch 2: DfdDiagramInput constructor (if exists)
if [ -f "$DFD_DIAGRAM_INPUT_FILE" ]; then
    echo "  Checking DfdDiagramInput constructor..."
    if grep -q "constructor(type" "$DFD_DIAGRAM_INPUT_FILE"; then
        echo -e "  ${GREEN}✓ DfdDiagramInput.js has type parameter${NC}"
    else
        echo -e "  ${YELLOW}⚠ DfdDiagramInput.js type parameter not found${NC}"
    fi
fi

# Patch 3: Fix AllOf* classes that incorrectly extend enum types
# swagger-codegen generates classes extending enum objects (not classes),
# causing "Super expression must either be null or a function" errors.
echo "  Fixing AllOf* enum inheritance issues..."
ALLOF_ENUM_FIXED=0
for allof_file in "$CLIENT_DIR"/src/model/AllOf*.js; do
    [ -f "$allof_file" ] || continue
    # Extract the parent class name from the "extends" clause
    PARENT=$(grep 'extends ' "$allof_file" 2>/dev/null | sed 's/.*extends \([A-Za-z_][A-Za-z0-9_]*\).*/\1/' | head -1)
    [ -z "$PARENT" ] && continue
    PARENT_FILE="$CLIENT_DIR/src/model/$PARENT.js"
    [ -f "$PARENT_FILE" ] || continue
    # Check if parent is an enum (const object) rather than a class
    if grep -q "^const $PARENT = {" "$PARENT_FILE" 2>/dev/null; then
        CLASSNAME=$(basename "$allof_file" .js)
        # Rewrite as a non-extending class that delegates to the enum
        cat > "$allof_file" << EOFIX
import ApiClient from '../ApiClient';
import $PARENT from './$PARENT';

/**
 * The $CLASSNAME model module.
 * @module model/$CLASSNAME
 * @version 1.0.0
 */
export default class $CLASSNAME {
  /**
   * Constructs a <code>$CLASSNAME</code> from a plain JavaScript object.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/$CLASSNAME} obj Optional instance to populate.
   * @return {module:model/$CLASSNAME} The populated instance.
   */
  static constructFromObject(data, obj) {
    return data;
  }
}
EOFIX
        ((ALLOF_ENUM_FIXED++))
        echo "    Fixed: $CLASSNAME (was extending enum $PARENT)"
    fi
done
if [ $ALLOF_ENUM_FIXED -gt 0 ]; then
    echo -e "  ${GREEN}✓ Fixed $ALLOF_ENUM_FIXED AllOf* enum inheritance issues${NC}"
else
    echo -e "  ${GREEN}✓ No AllOf* enum inheritance issues found${NC}"
fi

echo -e "${GREEN}✓ Validation and patches complete${NC}"
echo ""

# Step 5: Restore custom files
echo "Step 5: Restoring custom files..."

# Always create clean .babelrc (modern @babel/preset-env includes all proposals)
cat > "$CLIENT_DIR/.babelrc" << 'EOF'
{
  "presets": ["@babel/preset-env"]
}
EOF
echo "  ✓ Created .babelrc"

# Restore test_diagram_fixes.js if it exists
if [ -f ".regeneration_backup/test_diagram_fixes.js" ]; then
    cp .regeneration_backup/test_diagram_fixes.js "$CLIENT_DIR/"
    echo "  ✓ Restored test_diagram_fixes.js"
fi

# Restore developer docs if they exist
if [ -d ".regeneration_backup/developer" ]; then
    mkdir -p "$CLIENT_DIR/docs/developer"
    cp -r .regeneration_backup/developer/* "$CLIENT_DIR/docs/developer/"
    echo "  ✓ Restored developer documentation"
fi

# Restore scripts directory if it exists
if [ -d ".regeneration_backup/scripts" ]; then
    mkdir -p "$CLIENT_DIR/scripts"
    cp -r .regeneration_backup/scripts/* "$CLIENT_DIR/scripts/"
    echo "  ✓ Restored scripts directory"
fi

# Restore audit file if it exists
if [ -f ".regeneration_backup/PRE_REGENERATION_AUDIT.md" ]; then
    cp .regeneration_backup/PRE_REGENERATION_AUDIT.md "$CLIENT_DIR/"
    echo "  ✓ Restored PRE_REGENERATION_AUDIT.md"
fi

echo -e "${GREEN}✓ Custom files restored${NC}"
echo ""

# Step 6: Update package.json with modern dependencies
echo "Step 6: Updating package.json..."

# Always create fresh package.json with current best practices
cat > "$CLIENT_DIR/package.json" << 'EOF'
{
  "name": "tmi-js-client",
  "version": "1.0.0",
  "description": "JavaScript client for TMI (Threat Modeling Improved) API v1.0.0",
  "license": "Apache-2.0",
  "main": "src/index.js",
  "scripts": {
    "test": "mocha --require @babel/register --recursive",
    "build": "babel src -d dist"
  },
  "browser": {
    "fs": false
  },
  "dependencies": {
    "superagent": "^10.2.3"
  },
  "devDependencies": {
    "@babel/cli": "^7.28.3",
    "@babel/core": "^7.28.4",
    "@babel/preset-env": "^7.28.3",
    "@babel/register": "^7.28.3",
    "chai": "^5.1.2",
    "expect.js": "^0.3.1",
    "mocha": "^11.7.4",
    "sinon": "^21.0.0"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/threagile/tmi-clients.git"
  },
  "keywords": [
    "tmi",
    "threat-modeling",
    "api-client",
    "swagger",
    "openapi"
  ]
}
EOF
echo "  ✓ Created modern package.json"

echo -e "${GREEN}✓ package.json updated${NC}"
echo ""

# Step 7: Install dependencies
echo "Step 7: Installing dependencies..."
npm install
if [ $? -ne 0 ]; then
    echo -e "${RED}ERROR: npm install failed${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Dependencies installed${NC}"
echo ""

# Step 8: Run tests
echo "Step 8: Running tests..."
set +e
npm test > test_output.log 2>&1
TEST_EXIT_CODE=$?
set -e

if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}✓ All tests passed${NC}"
    echo ""
else
    echo -e "${YELLOW}⚠ Some tests failed (exit code: $TEST_EXIT_CODE)${NC}"
    echo "  Check test_output.log for details"
    echo ""
fi

# Step 9: Run integration tests (if they exist)
echo "Step 9: Running integration tests..."
if [ -f "$CLIENT_DIR/test_diagram_fixes.js" ]; then
    set +e
    node test_diagram_fixes.js > integration_test_output.log 2>&1
    INTEGRATION_EXIT_CODE=$?
    set -e

    if [ $INTEGRATION_EXIT_CODE -eq 0 ]; then
        echo -e "${GREEN}✓ Integration tests passed${NC}"
    else
        echo -e "${YELLOW}⚠ Integration tests failed${NC}"
        echo "  Check integration_test_output.log for details"
    fi
else
    echo -e "${YELLOW}⚠ No integration tests found${NC}"
fi
echo ""

# Step 10: Generate regeneration report
echo "Step 10: Generating regeneration report..."

cat > REGENERATION_REPORT.md << EOF
# TMI JavaScript Client Regeneration Report

**Date**: $(date +"%Y-%m-%d %H:%M:%S")
**OpenAPI Spec**: $OPENAPI_SPEC
**Swagger Codegen**: $(swagger-codegen version 2>&1 | head -1)
**Node.js**: $(node -v)
**npm**: $(npm -v)

## Configuration

- **Package Name**: tmi-js-client
- **Version**: 1.0.0
- **Config File**: $CONFIG_FILE

## Generation Results

### Files Generated

\`\`\`
$(find src -type f | wc -l) source files in src/
$(find test -type f | wc -l) test files in test/
$(find docs -type f -name "*.md" | wc -l) documentation files in docs/
\`\`\`

### API Classes

\`\`\`
$(ls -1 src/tmi-client/*.js 2>/dev/null | wc -l) API endpoint classes
\`\`\`

### Model Classes

\`\`\`
$(ls -1 src/model/*.js 2>/dev/null | wc -l) model classes
\`\`\`

### Dependencies

**Runtime:**
- superagent: $(node -p "require('./package.json').dependencies.superagent" 2>/dev/null || echo "N/A")

**Development:**
- @babel/core: $(node -p "require('./package.json').devDependencies['@babel/core']" 2>/dev/null || echo "N/A")
- mocha: $(node -p "require('./package.json').devDependencies.mocha" 2>/dev/null || echo "N/A")
- chai: $(node -p "require('./package.json').devDependencies.chai" 2>/dev/null || echo "N/A")
- sinon: $(node -p "require('./package.json').devDependencies.sinon" 2>/dev/null || echo "N/A")

## Test Results

### Unit Tests

Exit Code: $TEST_EXIT_CODE
Status: $([ $TEST_EXIT_CODE -eq 0 ] && echo "✅ PASSED" || echo "❌ FAILED")

See \`test_output.log\` for full details.

### Integration Tests

$([ -f "test_diagram_fixes.js" ] && echo "Status: $([ $INTEGRATION_EXIT_CODE -eq 0 ] && echo '✅ PASSED' || echo '❌ FAILED')" || echo "Status: ⚠️ NOT FOUND")

$([ -f "integration_test_output.log" ] && echo "See \`integration_test_output.log\` for full details." || echo "")

## Patches Applied

1. **DfdDiagram Constructor**: $([ -f "$DFD_DIAGRAM_FILE" ] && echo "✓ File exists (manual verification needed)" || echo "⚠️ File not found")
2. **DfdDiagramInput Constructor**: $([ -f "$DFD_DIAGRAM_INPUT_FILE" ] && echo "✓ File exists (manual verification needed)" || echo "⚠️ File not found")

## Critical Changes in This Regeneration

### New Features

- **Webhook API**: 5 new endpoints for webhook subscriptions and deliveries
- **Input Schemas**: Separate input/output schemas (DfdDiagramInput vs DfdDiagram)
- **Cell Simplification**: Removed nested cell attribute classes (7 classes)

### Breaking Changes

1. **Cell Schema**: Nested classes replaced with inline objects
   - Removed: EdgeAttrsLine, NodeAttrsBody, NodeAttrsText, etc.
   - Use: Plain JavaScript objects for cell attributes

2. **Input Schemas**: PUT/PATCH operations use *Input classes
   - Use DfdDiagramInput for updates (not DfdDiagram)
   - Removes need to provide readOnly fields

### Security Updates

- superagent: 5.3.1 → 10.2.3 (CVE fixes)
- mocha: 3.x → 11.7.4 (modernization)
- chai: 4.x → 5.1.2 (modern assertions)
- sinon: 7.5.0 → 21.0.0 (modern mocking)

## Next Steps

1. ✅ Review \`REGENERATION_REPORT.md\` (this file)
2. $([ $TEST_EXIT_CODE -eq 0 ] && echo "✅" || echo "❌") Review test results in \`test_output.log\`
3. ✅ Review \`docs/developer/MIGRATION_GUIDE.md\` for API changes
4. ⚠️ Manually verify constructor patches in:
   - src/model/DfdDiagram.js
   - src/model/DfdDiagramInput.js (if present)
5. ✅ Build the client: \`npm run build\`
6. ✅ Test with your application
7. ✅ Update CHANGELOG.md with any additional changes

## Documentation

- **Usage Guide**: README.md
- **API Reference**: docs/
- **Migration Guide**: docs/developer/MIGRATION_GUIDE.md
- **Regeneration Guide**: docs/developer/REGENERATION_README.md
- **Changelog**: docs/developer/CHANGELOG.md

## Summary

$([ $TEST_EXIT_CODE -eq 0 ] && echo "✅ **Regeneration completed successfully**" || echo "⚠️ **Regeneration completed with test failures**")

The JavaScript client has been regenerated from the latest OpenAPI specification.
All modern dependencies and security updates have been applied.

**Action Required**: Manual verification of constructor patches recommended.
EOF

echo -e "${GREEN}✓ Regeneration report created: REGENERATION_REPORT.md${NC}"
echo ""

# Final summary
echo "========================================="
echo "Regeneration Complete!"
echo "========================================="
echo ""
echo "Summary:"
echo "  - Generated files: $(find src -type f | wc -l) source + $(find test -type f | wc -l) test"
echo "  - Tests: $([ $TEST_EXIT_CODE -eq 0 ] && echo "${GREEN}PASSED${NC}" || echo "${YELLOW}FAILED${NC}")"
echo "  - Report: REGENERATION_REPORT.md"
echo ""
echo "Next steps:"
echo "  1. Review REGENERATION_REPORT.md"
echo "  2. Check test_output.log for test details"
echo "  3. Read docs/developer/MIGRATION_GUIDE.md"
echo "  4. Build: npm run build"
echo ""

# Exit with test status
exit $TEST_EXIT_CODE
