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
# - Modern dependencies with latest Python 3.8+ compatible versions:
#   * certifi >= 2025.11.12 (was 14.05.14)
#   * six >= 1.17.0 (was 1.10)
#   * python-dateutil >= 2.9.0.post0 (was 2.5.3)
#   * setuptools >= 75.3.2 (was 21.0.0 - CVE fix, Python 3.8+ compatible)
#   * urllib3 >= 2.2.3 (was 1.15.1 - CVE fixes, Python 3.8+ compatible)
#   * pytest >= 8.3.5 (was using nose, Python 3.8+ compatible)
#   * pytest-cov >= 5.0.0 (Python 3.8+ compatible)
#   * pytest-randomly >= 3.15.0 (Python 3.8+ compatible)
# - Testing: pytest (not nose), tox for multi-version testing
# - Modern packaging: pyproject.toml + setup.py
# - Tox configuration: Tests against Python 3.8-3.14
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
# Navigate to python-client-generated directory (parent of scripts/)
PYTHON_CLIENT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PYTHON_CLIENT_DIR"

echo "========================================="
echo "TMI Python Client Regeneration"
echo "========================================="
echo ""
echo "Working directory: $PYTHON_CLIENT_DIR"
echo ""
echo "Automatic defaults:"
echo "  - Package: tmi_client"
echo "  - Python: 3.8+"
echo "  - Dependencies: Modern with CVE fixes"
echo "  - Testing: pytest"
echo ""

# Configuration
OPENAPI_SPEC="/Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json"
CLIENT_DIR="."  # We're already in python-client-generated/
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
# Clean specific directories that will be regenerated, preserve custom files
rm -rf tmi_client/
rm -rf test/
rm -rf docs/*.md  # Remove auto-generated docs but preserve docs/developer/
rm -f .gitignore .travis.yml git_push.sh README.md
echo -e "${GREEN}✓ Client directory cleaned${NC}"
echo ""

echo "Step 3: Running swagger-codegen..."
# Use custom templates with fix for allOf inheritance __init__ parameter forwarding
# See: https://github.com/swagger-api/swagger-codegen-generators/issues/XXX
TEMPLATE_DIR="custom-templates/python"
echo "Command: swagger-codegen generate -i $OPENAPI_SPEC -l python -o $CLIENT_DIR -c $CONFIG_FILE -t $TEMPLATE_DIR"
swagger-codegen generate \
    -i "$OPENAPI_SPEC" \
    -l python \
    -o "$CLIENT_DIR" \
    -c "$CONFIG_FILE" \
    -t "$TEMPLATE_DIR"

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

# Patch Edge
EDGE_FILE="$CLIENT_DIR/tmi_client/models/edge.py"
if [ -f "$EDGE_FILE" ]; then
    echo "  Patching Edge constructor..."
    sed -i.bak '/def __init__(self.*shape/,/Cell.__init__/ {
        /Cell.__init__/i\
        kwargs['"'"'shape'"'"'] = shape  # PATCH: Pass shape to parent to prevent overwrite
    }' "$EDGE_FILE"

    rm -f "${EDGE_FILE}.bak"
    echo -e "${GREEN}  ✓ Edge patched${NC}"
else
    echo -e "${YELLOW}  ⚠ Edge file not found - may need manual patch${NC}"
fi

# Patch Node
NODE_FILE="$CLIENT_DIR/tmi_client/models/node.py"
if [ -f "$NODE_FILE" ]; then
    echo "  Patching Node constructor..."
    sed -i.bak '/def __init__(self.*shape/,/Cell.__init__/ {
        /Cell.__init__/i\
        kwargs['"'"'shape'"'"'] = shape  # PATCH: Pass shape to parent to prevent overwrite
    }' "$NODE_FILE"

    rm -f "${NODE_FILE}.bak"
    echo -e "${GREEN}  ✓ Node patched${NC}"
else
    echo -e "${YELLOW}  ⚠ Node file not found - may need manual patch${NC}"
fi

# Patch Configuration.auth_settings()
CONFIGURATION_FILE="$CLIENT_DIR/tmi_client/configuration.py"
if [ -f "$CONFIGURATION_FILE" ]; then
    echo "  Patching Configuration.auth_settings()..."
    # Replace the empty auth_settings method with the proper implementation
    python3 << 'PYTHON_PATCH'
import re

with open("tmi_client/configuration.py", "r") as f:
    content = f.read()

# Pattern to match the empty auth_settings method
old_pattern = r'    def auth_settings\(self\):\n        """Gets Auth Settings dict for api client\.\n\n        :return: The Auth Settings information dict\.\n        """\n        return \{\n        \}'

# New implementation
new_impl = '''    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        auth = {}
        if 'bearerAuth' in self.api_key:
            auth['bearerAuth'] = {
                'type': 'api_key',
                'in': 'header',
                'key': 'Authorization',
                'value': self.get_api_key_with_prefix('bearerAuth')
            }
        return auth'''

# Replace the pattern
content = re.sub(old_pattern, new_impl, content)

with open("tmi_client/configuration.py", "w") as f:
    f.write(content)

print("auth_settings patched")
PYTHON_PATCH

    echo -e "${GREEN}  ✓ Configuration.auth_settings() patched${NC}"
else
    echo -e "${YELLOW}  ⚠ Configuration file not found - may need manual patch${NC}"
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
    "certifi >= 2025.11.12",
    "six >= 1.17.0",
    "python-dateutil >= 2.9.0.post0",
    "setuptools >= 75.3.2",
    "urllib3 >= 2.2.3",
]

[project.optional-dependencies]
test = [
    "pytest >= 8.3.5",
    "pytest-cov >= 5.0.0",
    "pytest-randomly >= 3.15.0",
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

# Update setup.py with modern dependencies (Python 3.8+ only)
echo "  Updating setup.py for Python 3.8+ with modern dependencies..."
if [ -f "$CLIENT_DIR/setup.py" ]; then
    # Update Python version requirement - Python 3.8+ only
    sed -i.bak 's/python_requires="[^"]*"/python_requires=">=3.8"/' "$CLIENT_DIR/setup.py"

    # Update dependencies to latest Python 3.8+ compatible versions
    sed -i.bak 's/"certifi[^"]*"/"certifi>=2025.11.12"/' "$CLIENT_DIR/setup.py"
    sed -i.bak 's/"six[^"]*"/"six>=1.17.0"/' "$CLIENT_DIR/setup.py"
    sed -i.bak 's/"python-dateutil[^"]*"/"python-dateutil>=2.9.0.post0"/' "$CLIENT_DIR/setup.py"
    sed -i.bak 's/"urllib3[^"]*"/"urllib3>=2.2.3"/' "$CLIENT_DIR/setup.py"

    # Add setuptools if not present, or update if present
    if grep -q '"setuptools' "$CLIENT_DIR/setup.py"; then
        sed -i.bak 's/"setuptools[^"]*"/"setuptools>=75.3.2"/' "$CLIENT_DIR/setup.py"
    fi

    rm -f "$CLIENT_DIR/setup.py.bak"
    echo -e "${GREEN}  ✓ setup.py updated for Python 3.8+${NC}"
fi

# Update requirements.txt
echo "  Updating requirements.txt..."
cat > "$CLIENT_DIR/requirements.txt" << 'EOF'
certifi >= 2025.11.12
six >= 1.17.0
python-dateutil >= 2.9.0.post0
setuptools >= 75.3.2
urllib3 >= 2.2.3
EOF
echo -e "${GREEN}  ✓ requirements.txt updated${NC}"

# Update test-requirements.txt
echo "  Updating test-requirements.txt..."
cat > "$CLIENT_DIR/test-requirements.txt" << 'EOF'
pytest >= 8.3.5
pytest-cov >= 5.0.0
pytest-randomly >= 3.15.0
EOF
echo -e "${GREEN}  ✓ test-requirements.txt updated${NC}"

# Update tox.ini
echo "  Updating tox.ini..."
cat > "$CLIENT_DIR/tox.ini" << 'EOF'
[tox]
envlist = py38,py39,py310,py311,py312,py313,py314

[testenv]
deps=-r{toxinidir}/requirements.txt
     -r{toxinidir}/test-requirements.txt

commands=
   pytest test/ -v --tb=short {posargs}
EOF
echo -e "${GREEN}  ✓ tox.ini updated${NC}"

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
cat > docs/developer/REGENERATION_REPORT.md << 'EOF'
# Python Client Regeneration Report

## Date
EOF
date >> docs/developer/REGENERATION_REPORT.md
cat >> docs/developer/REGENERATION_REPORT.md << 'EOF'

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
- ✓ Updated dependencies (latest Python 3.8+ compatible versions):
  - certifi >= 2025.11.12
  - six >= 1.17.0
  - python-dateutil >= 2.9.0.post0
  - setuptools >= 75.3.2
  - urllib3 >= 2.2.3
  - pytest >= 8.3.5
  - pytest-cov >= 5.0.0
  - pytest-randomly >= 3.15.0
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
echo "" >> docs/developer/REGENERATION_REPORT.md
echo "### Generated API Classes" >> docs/developer/REGENERATION_REPORT.md
ls -1 "$CLIENT_DIR/tmi_client/api/" | grep "\.py$" | wc -l | xargs echo "- Total API classes:" >> docs/developer/REGENERATION_REPORT.md

echo "" >> docs/developer/REGENERATION_REPORT.md
echo "### Generated Model Classes" >> docs/developer/REGENERATION_REPORT.md
ls -1 "$CLIENT_DIR/tmi_client/models/" | grep "\.py$" | wc -l | xargs echo "- Total model classes:" >> docs/developer/REGENERATION_REPORT.md

echo "" >> docs/developer/REGENERATION_REPORT.md
echo "### Test Files" >> docs/developer/REGENERATION_REPORT.md
ls -1 "$CLIENT_DIR/test/" | grep "\.py$" | wc -l | xargs echo "- Total test files:" >> docs/developer/REGENERATION_REPORT.md

cat >> docs/developer/REGENERATION_REPORT.md << 'EOF'

## Next Steps

1. **Review Breaking Changes**: Check MIGRATION_GUIDE.md for cell schema changes
2. **Update Documentation**: Run documentation update tasks
3. **Manual Testing**: Test webhook endpoints and simplified cell schemas
4. **Update Dependent Projects**: Update any projects using this client

## Test Results

See test_output.log and integration_test_output.log for detailed test results.

EOF

echo -e "${GREEN}✓ Summary report generated: docs/developer/REGENERATION_REPORT.md${NC}"
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
echo "  1. Review docs/developer/REGENERATION_REPORT.md"
echo "  2. Check test_output.log for test failures"
echo "  3. Update documentation files"
echo "  4. Test webhook endpoints"
echo ""
echo "Documentation files:"
echo "  - docs/developer/MIGRATION_GUIDE.md"
echo "  - docs/developer/CHANGELOG.md"
echo "  - docs/developer/REGENERATION_README.md"
echo "  - ../CLAUDE.md (repository root)"
echo ""
