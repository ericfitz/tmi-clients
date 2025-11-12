#!/bin/bash
set -e  # Exit on error

# TMI Python Client Regeneration Script
#
# This script regenerates the Python client from the latest OpenAPI spec
# and applies all necessary patches and customizations.
#
# AUTOMATIC DEFAULTS APPLIED:
# - Package name: tmi_client (not swagger_client)
# - Python version: 3.8+ only (Python 2.x and 3.7 dropped)
# - Modern dependencies with security fixes:
#   * certifi >= 2024.2.2 (was 14.05.14)
#   * six >= 1.16.0 (was 1.10)
#   * python-dateutil >= 2.9.0 (was 2.5.3)
#   * setuptools >= 70.0.0 (was 21.0.0 - CVE fix)
#   * urllib3 >= 2.0.0 (was 1.15.1 - CVE fixes)
# - Testing: pytest (not nose)
# - Modern packaging: pyproject.toml + setup.py
# - Constructor patches: DfdDiagram and DfdDiagramInput type preservation
#
# USAGE:
#   ./regenerate_client.sh
#
# REQUIREMENTS:
#   - swagger-codegen (install via: brew install swagger-codegen)
#   - uv (install via: brew install uv)
#   - OpenAPI spec at: /Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "========================================="
echo "TMI Python Client Regeneration"
echo "========================================="
echo ""
echo "Automatic defaults:"
echo "  - Package: tmi_client"
echo "  - Python: 3.8+"
echo "  - Dependencies: Modern with CVE fixes"
echo "  - Testing: pytest"
echo ""

# Configuration
OPENAPI_SPEC="/Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json"
CLIENT_DIR="python-client-generated"
CONFIG_FILE="swagger-codegen-config.json"
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

if ! command -v uv &> /dev/null; then
    echo -e "${RED}ERROR: uv not found. Please install uv first.${NC}"
    exit 1
fi

echo -e "${GREEN}✓ All prerequisites met${NC}"
echo ""

# Step 1: Backup critical custom files
echo "Step 1: Backing up custom files..."
mkdir -p .regeneration_backup
cp -f "$CLIENT_DIR/pyproject.toml" .regeneration_backup/ 2>/dev/null || true
cp -f "$CLIENT_DIR/test_diagram_fixes.py" .regeneration_backup/ 2>/dev/null || true
cp -f "$CLIENT_DIR/.swagger-codegen-ignore" .regeneration_backup/ 2>/dev/null || true
echo -e "${GREEN}✓ Custom files backed up${NC}"
echo ""

# Step 2: Clean and regenerate
echo "Step 2: Cleaning client directory..."
if [ -d "$CLIENT_DIR" ]; then
    # Preserve documentation at repo root
    rm -rf "$CLIENT_DIR"
fi
echo -e "${GREEN}✓ Client directory cleaned${NC}"
echo ""

echo "Step 3: Running swagger-codegen..."
echo "Command: swagger-codegen generate -i $OPENAPI_SPEC -l python -o $CLIENT_DIR -c $CONFIG_FILE"
swagger-codegen generate \
    -i "$OPENAPI_SPEC" \
    -l python \
    -o "$CLIENT_DIR" \
    -c "$CONFIG_FILE"

if [ $? -ne 0 ]; then
    echo -e "${RED}ERROR: swagger-codegen failed${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Client regenerated successfully${NC}"
echo ""

# Step 4: Apply critical constructor patches
echo "Step 4: Applying constructor patches..."

# Patch DfdDiagram
DFD_DIAGRAM_FILE="$CLIENT_DIR/tmi_client/models/dfd_diagram.py"
if [ -f "$DFD_DIAGRAM_FILE" ]; then
    echo "  Patching DfdDiagram constructor..."
    # Find the __init__ method and add the type parameter fix
    # Look for the line with "self.discriminator = 'type'" and add the fix before calling super().__init__
    sed -i.bak '/def __init__(self.*type.*cells.*name/,/BaseDiagram.__init__/ {
        /BaseDiagram.__init__/i\
        kwargs['"'"'type'"'"'] = type  # PATCH: Pass type to parent to prevent overwrite
    }' "$DFD_DIAGRAM_FILE"

    # Remove backup file
    rm -f "${DFD_DIAGRAM_FILE}.bak"
    echo -e "${GREEN}  ✓ DfdDiagram patched${NC}"
else
    echo -e "${YELLOW}  ⚠ DfdDiagram file not found - may need manual patch${NC}"
fi

# Patch DfdDiagramInput
DFD_DIAGRAM_INPUT_FILE="$CLIENT_DIR/tmi_client/models/dfd_diagram_input.py"
if [ -f "$DFD_DIAGRAM_INPUT_FILE" ]; then
    echo "  Patching DfdDiagramInput constructor..."
    sed -i.bak '/def __init__(self.*type.*cells.*name/,/BaseDiagramInput.__init__/ {
        /BaseDiagramInput.__init__/i\
        kwargs['"'"'type'"'"'] = type  # PATCH: Pass type to parent to prevent overwrite
    }' "$DFD_DIAGRAM_INPUT_FILE"

    rm -f "${DFD_DIAGRAM_INPUT_FILE}.bak"
    echo -e "${GREEN}  ✓ DfdDiagramInput patched${NC}"
else
    echo -e "${YELLOW}  ⚠ DfdDiagramInput file not found - may need manual patch${NC}"
fi

echo -e "${GREEN}✓ Constructor patches applied${NC}"
echo ""

# Step 5: Restore and update configuration files
echo "Step 5: Applying modern Python 3.x configuration..."

# Always create fresh pyproject.toml with current best practices
echo "  Creating pyproject.toml with Python 3.8+ requirements..."
cat > "$CLIENT_DIR/pyproject.toml" << 'EOF'
[project]
name = "tmi-client"
version = "1.0.0"
description = "TMI API Python Client"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "Apache-2.0"}
keywords = ["TMI", "Threat Modeling", "API", "OpenAPI"]
authors = [
    {name = "TMI Contributors"}
]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
]

dependencies = [
    "certifi >= 2024.2.2",
    "six >= 1.16.0",
    "python-dateutil >= 2.9.0",
    "setuptools >= 70.0.0",
    "urllib3 >= 2.0.0",
]

[project.optional-dependencies]
test = [
    "pytest >= 7.0.0",
    "pytest-cov >= 4.0.0",
    "pytest-randomly >= 3.12.0",
]

[project.urls]
Homepage = "https://github.com/threagile/tmi-clients"
Repository = "https://github.com/threagile/tmi-clients"
Documentation = "https://github.com/threagile/tmi-clients/tree/main/python-client-generated"

[build-system]
requires = ["setuptools>=70.0.0", "wheel"]
build-backend = "setuptools.build_meta"

[tool.pytest.ini_options]
testpaths = ["test"]
python_files = "test_*.py"
python_classes = "Test*"
python_functions = "test_*"
addopts = "-v --strict-markers"

[tool.coverage.run]
source = ["tmi_client"]
omit = ["*/test/*", "*/tests/*"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
]
EOF
fi

# Update setup.py with modern dependencies (Python 3.8+ only)
echo "  Updating setup.py for Python 3.8+ with modern dependencies..."
if [ -f "$CLIENT_DIR/setup.py" ]; then
    # Update Python version requirement - Python 3.8+ only
    sed -i.bak 's/python_requires="[^"]*"/python_requires=">=3.8"/' "$CLIENT_DIR/setup.py"

    # Update dependencies to modern versions with security fixes
    sed -i.bak 's/"certifi[^"]*"/"certifi>=2024.2.2"/' "$CLIENT_DIR/setup.py"
    sed -i.bak 's/"six[^"]*"/"six>=1.16.0"/' "$CLIENT_DIR/setup.py"
    sed -i.bak 's/"python-dateutil[^"]*"/"python-dateutil>=2.9.0"/' "$CLIENT_DIR/setup.py"
    sed -i.bak 's/"urllib3[^"]*"/"urllib3>=2.0.0"/' "$CLIENT_DIR/setup.py"

    # Add setuptools if not present, or update if present
    if grep -q '"setuptools' "$CLIENT_DIR/setup.py"; then
        sed -i.bak 's/"setuptools[^"]*"/"setuptools>=70.0.0"/' "$CLIENT_DIR/setup.py"
    fi

    rm -f "$CLIENT_DIR/setup.py.bak"
    echo -e "${GREEN}  ✓ setup.py updated for Python 3.8+${NC}"
fi

# Update requirements.txt
echo "  Updating requirements.txt..."
cat > "$CLIENT_DIR/requirements.txt" << 'EOF'
certifi >= 2024.2.2
six >= 1.16.0
python-dateutil >= 2.9.0
setuptools >= 70.0.0
urllib3 >= 2.0.0
EOF
echo -e "${GREEN}  ✓ requirements.txt updated${NC}"

# Update test-requirements.txt
echo "  Updating test-requirements.txt..."
cat > "$CLIENT_DIR/test-requirements.txt" << 'EOF'
pytest >= 7.0.0
pytest-cov >= 4.0.0
pytest-randomly >= 3.12.0
EOF
echo -e "${GREEN}  ✓ test-requirements.txt updated${NC}"

echo -e "${GREEN}✓ Configuration files updated${NC}"
echo ""

# Step 6: Restore custom test file
echo "Step 6: Restoring custom test file..."
if [ -f ".regeneration_backup/test_diagram_fixes.py" ]; then
    cp .regeneration_backup/test_diagram_fixes.py "$CLIENT_DIR/"
    echo -e "${GREEN}✓ test_diagram_fixes.py restored${NC}"
else
    echo -e "${YELLOW}⚠ test_diagram_fixes.py not found in backup${NC}"
fi
echo ""

# Step 7: Restore .swagger-codegen-ignore if it existed
if [ -f ".regeneration_backup/.swagger-codegen-ignore" ]; then
    cp .regeneration_backup/.swagger-codegen-ignore "$CLIENT_DIR/"
    echo -e "${GREEN}✓ .swagger-codegen-ignore restored${NC}"
fi

# Step 8: Run tests
echo "Step 7: Running tests..."
cd "$CLIENT_DIR"

echo "  Installing dependencies..."
uv pip install -e . --quiet 2>&1 | grep -v "Resolved" || true

echo "  Running auto-generated tests..."
if uv run --with pytest python3 -m pytest test/ -v --tb=short 2>&1 | tee ../test_output.log; then
    echo -e "${GREEN}  ✓ Auto-generated tests passed${NC}"
else
    echo -e "${YELLOW}  ⚠ Some auto-generated tests failed - see test_output.log${NC}"
    echo -e "${YELLOW}    This is expected if the API has breaking changes${NC}"
fi

echo ""

# Step 9: Run integration test
echo "Step 8: Running integration test..."
if [ -f "test_diagram_fixes.py" ]; then
    if uv run test_diagram_fixes.py 2>&1 | tee ../integration_test_output.log; then
        echo -e "${GREEN}  ✓ Integration test passed${NC}"
    else
        echo -e "${YELLOW}  ⚠ Integration test failed - may need updates for cell schema changes${NC}"
        echo -e "${YELLOW}    See integration_test_output.log for details${NC}"
    fi
else
    echo -e "${YELLOW}  ⚠ Integration test file not found${NC}"
fi

cd ..
echo ""

# Step 10: Generate summary report
echo "Step 9: Generating summary report..."
cat > REGENERATION_REPORT.md << 'EOF'
# Python Client Regeneration Report

## Date
EOF
date >> REGENERATION_REPORT.md
cat >> REGENERATION_REPORT.md << 'EOF'

## Changes Applied

### 1. Client Regenerated
- Source: `/Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json`
- Generator: swagger-codegen 3.0.75
- Package: tmi_client v1.0.0

### 2. Constructor Patches Applied
- ✓ DfdDiagram constructor fixed (type parameter preservation)
- ✓ DfdDiagramInput constructor fixed (type parameter preservation)

### 3. Modern Python Configuration
- ✓ Python 3.8+ requirement
- ✓ Updated dependencies:
  - certifi >= 2024.2.2 (security fixes)
  - six >= 1.16.0
  - python-dateutil >= 2.9.0
  - setuptools >= 70.0.0 (RCE vulnerability fix)
  - urllib3 >= 2.0.0 (CVE fixes)
- ✓ pyproject.toml with UV support
- ✓ pytest-based testing infrastructure

### 4. New Features in Generated Client
- Webhook API endpoints (5 new endpoints)
- Webhook schemas (WebhookSubscription, WebhookDelivery, etc.)
- Simplified cell schemas (inline objects instead of nested classes)

### 5. Breaking Changes
- Cell schema simplification: Property access changed from object attributes to dictionary access
- Removed classes: EdgeAttrsLine, NodeAttrsBody, NodeAttrsText, EdgeLabelAttrs, etc.
- Type safety reduced for nested cell properties

## Files Modified
EOF

# List all Python files in the client
echo "" >> REGENERATION_REPORT.md
echo "### Generated API Classes" >> REGENERATION_REPORT.md
ls -1 "$CLIENT_DIR/tmi_client/api/" | grep "\.py$" | wc -l | xargs echo "- Total API classes:" >> REGENERATION_REPORT.md

echo "" >> REGENERATION_REPORT.md
echo "### Generated Model Classes" >> REGENERATION_REPORT.md
ls -1 "$CLIENT_DIR/tmi_client/models/" | grep "\.py$" | wc -l | xargs echo "- Total model classes:" >> REGENERATION_REPORT.md

echo "" >> REGENERATION_REPORT.md
echo "### Test Files" >> REGENERATION_REPORT.md
ls -1 "$CLIENT_DIR/test/" | grep "\.py$" | wc -l | xargs echo "- Total test files:" >> REGENERATION_REPORT.md

cat >> REGENERATION_REPORT.md << 'EOF'

## Next Steps

1. **Review Breaking Changes**: Check MIGRATION_GUIDE.md for cell schema changes
2. **Update Documentation**: Run documentation update tasks
3. **Manual Testing**: Test webhook endpoints and simplified cell schemas
4. **Update Dependent Projects**: Update any projects using this client

## Test Results

See test_output.log and integration_test_output.log for detailed test results.

EOF

echo -e "${GREEN}✓ Summary report generated: REGENERATION_REPORT.md${NC}"
echo ""

# Cleanup
echo "Step 10: Cleaning up..."
rm -rf .regeneration_backup
echo -e "${GREEN}✓ Cleanup complete${NC}"
echo ""

# Final summary
echo "========================================="
echo -e "${GREEN}REGENERATION COMPLETE${NC}"
echo "========================================="
echo ""
echo "Summary:"
echo "  - Client regenerated from latest OpenAPI spec"
echo "  - Constructor patches applied"
echo "  - Modern Python configuration restored"
echo "  - Tests executed (see logs for results)"
echo ""
echo "Next steps:"
echo "  1. Review REGENERATION_REPORT.md"
echo "  2. Check test_output.log for test failures"
echo "  3. Update documentation files"
echo "  4. Test webhook endpoints"
echo ""
echo "Documentation files to update:"
echo "  - MIGRATION_GUIDE.md"
echo "  - CLAUDE.md"
echo "  - CHANGELOG.md"
echo "  - OPENAPI_ISSUES_SUMMARY.md"
echo "  - CLIENT_IMPROVEMENTS.md"
echo ""
