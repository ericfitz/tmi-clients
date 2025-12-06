#!/bin/bash
set -e  # Exit on error

# Backup Script for Python Client Before Regeneration
#
# This script creates a comprehensive backup of the current Python client
# before regeneration, allowing for easy comparison and rollback if needed.
#
# USAGE:
#   ./scripts/backup_before_regen.sh
#
# Creates:
#   - Timestamped backup directory
#   - Archive of entire client
#   - Snapshot of key metrics
#   - List of all current models and APIs

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLIENT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$CLIENT_DIR"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo "========================================="
echo "Python Client Pre-Regeneration Backup"
echo "========================================="
echo ""

# Create backup directory with timestamp
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="../backups/pre-regen-$TIMESTAMP"
mkdir -p "$BACKUP_DIR"

echo -e "${BLUE}Backup directory: $BACKUP_DIR${NC}"
echo ""

# Step 1: Capture current state metrics
echo "Step 1: Capturing current state metrics..."
cat > "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md" << 'EOF'
# Pre-Regeneration Snapshot

## Timestamp
EOF
date >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"

cat >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md" << 'EOF'

## Directory Structure
EOF

echo "" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
echo "### API Modules" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
ls -1 tmi_client/api/ | grep "\.py$" | grep -v "__init__" | wc -l | xargs echo "Total API modules:" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
echo "" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
echo "List:" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
ls -1 tmi_client/api/ | grep "\.py$" | grep -v "__init__" | grep -v "__pycache__" | sed 's/^/  - /' >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"

echo "" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
echo "### Model Classes" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
ls -1 tmi_client/models/ | grep "\.py$" | grep -v "__init__" | wc -l | xargs echo "Total model classes:" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
echo "" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
echo "List:" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
ls -1 tmi_client/models/ | grep "\.py$" | grep -v "__init__" | grep -v "__pycache__" | sed 's/^/  - /' >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"

echo "" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
echo "### Test Files" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
ls -1 test/ | grep "\.py$" | grep -v "__pycache__" | wc -l | xargs echo "Total test files:" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"

echo "" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
echo "## Package Configuration" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
echo "" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
echo "\`\`\`toml" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
cat pyproject.toml >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
echo "\`\`\`" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"

echo "" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
echo "## Dependencies" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
echo "" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
echo "\`\`\`" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
cat requirements.txt >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"
echo "\`\`\`" >> "$BACKUP_DIR/PRE_REGEN_SNAPSHOT.md"

echo -e "${GREEN}✓ Snapshot captured${NC}"

# Step 2: Create full backup archive
echo ""
echo "Step 2: Creating backup archive..."

# Copy entire client directory
cp -r . "$BACKUP_DIR/client_backup/"

# Create tarball for easy storage
tar -czf "$BACKUP_DIR/client_backup.tar.gz" \
    --exclude='.venv' \
    --exclude='__pycache__' \
    --exclude='*.pyc' \
    --exclude='.pytest_cache' \
    --exclude='*.egg-info' \
    -C .. "$(basename $CLIENT_DIR)"

echo -e "${GREEN}✓ Backup archive created${NC}"

# Step 3: Export current API and model lists
echo ""
echo "Step 3: Exporting detailed inventories..."

# API classes
echo "Current API Classes:" > "$BACKUP_DIR/api_classes.txt"
ls -1 tmi_client/api/*.py | grep -v "__init__" | while read file; do
    echo "  - $(basename $file .py)" >> "$BACKUP_DIR/api_classes.txt"
    # Extract class names
    grep "^class " "$file" | sed 's/class \([^(]*\).*/    Class: \1/' >> "$BACKUP_DIR/api_classes.txt"
done

# Model classes
echo "Current Model Classes:" > "$BACKUP_DIR/model_classes.txt"
ls -1 tmi_client/models/*.py | grep -v "__init__" | while read file; do
    echo "  - $(basename $file .py)" >> "$BACKUP_DIR/model_classes.txt"
    # Extract class names and discriminators
    grep "^class " "$file" | sed 's/class \([^(]*\).*/    Class: \1/' >> "$BACKUP_DIR/model_classes.txt"
    grep "discriminator = " "$file" | head -1 | sed 's/^/    /' >> "$BACKUP_DIR/model_classes.txt" 2>/dev/null || true
done

echo -e "${GREEN}✓ Inventories exported${NC}"

# Step 4: Copy critical custom files
echo ""
echo "Step 4: Backing up critical custom files..."
mkdir -p "$BACKUP_DIR/custom_files"

# Custom test file
if [ -f "test_diagram_fixes.py" ]; then
    cp test_diagram_fixes.py "$BACKUP_DIR/custom_files/"
    echo -e "${GREEN}  ✓ test_diagram_fixes.py${NC}"
fi

# Documentation
if [ -d "docs/developer" ]; then
    cp -r docs/developer "$BACKUP_DIR/custom_files/"
    echo -e "${GREEN}  ✓ docs/developer/${NC}"
fi

# Scripts
if [ -d "scripts" ]; then
    cp -r scripts "$BACKUP_DIR/custom_files/"
    echo -e "${GREEN}  ✓ scripts/${NC}"
fi

# Configuration files
for file in pyproject.toml setup.py requirements.txt test-requirements.txt tox.ini .swagger-codegen-ignore; do
    if [ -f "$file" ]; then
        cp "$file" "$BACKUP_DIR/custom_files/"
        echo -e "${GREEN}  ✓ $file${NC}"
    fi
done

echo ""
echo "Step 5: Creating comparison checklist..."

cat > "$BACKUP_DIR/POST_REGEN_CHECKLIST.md" << 'EOF'
# Post-Regeneration Checklist

Use this checklist after regenerating the client to verify everything is correct.

## Files to Compare

- [ ] `pyproject.toml` - Verify dependencies are correct
- [ ] `setup.py` - Check Python version and package config
- [ ] `requirements.txt` - Confirm dependency versions
- [ ] `tox.ini` - Verify test configuration
- [ ] `test_diagram_fixes.py` - Ensure custom test is present

## Code Verification

- [ ] Constructor patches applied (check `tmi_client/models/dfd_diagram.py`)
- [ ] Constructor patches applied (check `tmi_client/models/dfd_diagram_input.py`)
- [ ] No Python 2.x code present (no `unicode`, old-style classes)
- [ ] Proper type hints where expected
- [ ] All `__init__.py` files updated with new models

## API Comparison

Run this to compare:
```bash
# Compare API counts
echo "Old API count: $(cat api_classes.txt | grep -c "\.py")"
echo "New API count: $(ls -1 ../python-client-generated/tmi_client/api/*.py | grep -v __init__ | wc -l)"

# Compare model counts
echo "Old model count: $(cat model_classes.txt | grep -c "\.py")"
echo "New model count: $(ls -1 ../python-client-generated/tmi_client/models/*.py | grep -v __init__ | wc -l)"
```

## New Features to Verify

- [ ] Add-on API present (`tmi_client/api/*addon*`)
- [ ] Administration API present (`tmi_client/api/*admin*`)
- [ ] SAML models present (`tmi_client/models/*saml*`)
- [ ] Webhook quota models present
- [ ] New administrator models present

## Testing

- [ ] Auto-generated tests pass: `uv run --with pytest python3 -m pytest test/ -v`
- [ ] Integration test passes: `uv run test_diagram_fixes.py`
- [ ] Import test: `uv run python3 -c "import tmi_client; print('OK')"`
- [ ] Can instantiate new models without errors
- [ ] Cell schema changes work correctly (dict access)

## Documentation

- [ ] MIGRATION_GUIDE.md updated with cell schema changes
- [ ] CHANGELOG.md updated with breaking changes
- [ ] README.md updated with new features
- [ ] REGENERATION_REPORT.md created
- [ ] CLAUDE.md updated if needed

## Rollback Plan (if needed)

If regeneration fails or causes major issues:

```bash
# Extract backup
cd /Users/efitz/Projects/tmi-clients
tar -xzf backups/pre-regen-YYYYMMDD_HHMMSS/client_backup.tar.gz

# Or copy from backup directory
cp -r backups/pre-regen-YYYYMMDD_HHMMSS/client_backup/* python-client-generated/
```

## Comparison Commands

```bash
# Diff API classes
diff -u backups/pre-regen-TIMESTAMP/api_classes.txt <(ls -1 tmi_client/api/*.py | grep -v __init__)

# Diff model classes
diff -u backups/pre-regen-TIMESTAMP/model_classes.txt <(ls -1 tmi_client/models/*.py | grep -v __init__)

# Diff dependencies
diff -u backups/pre-regen-TIMESTAMP/custom_files/requirements.txt requirements.txt
```

## Sign-off

- [ ] All tests passing
- [ ] All documentation updated
- [ ] Breaking changes documented
- [ ] Migration guide complete
- [ ] Ready for commit

**Reviewer:** _______________
**Date:** _______________
EOF

echo -e "${GREEN}✓ Checklist created${NC}"

# Step 6: Create quick restore script
echo ""
echo "Step 6: Creating restore script..."

cat > "$BACKUP_DIR/restore.sh" << EOF
#!/bin/bash
# Quick restore script for this backup

set -e

BACKUP_DIR="\$(cd "\$(dirname "\${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="/Users/efitz/Projects/tmi-clients/python-client-generated"

echo "========================================="
echo "Restoring Python Client from Backup"
echo "========================================="
echo ""
echo "Backup: \$BACKUP_DIR"
echo "Target: \$TARGET_DIR"
echo ""

read -p "This will overwrite the current client. Continue? (yes/no): " confirm

if [ "\$confirm" != "yes" ]; then
    echo "Restore cancelled."
    exit 0
fi

echo ""
echo "Extracting backup..."
cd "\$(dirname \$TARGET_DIR)"
tar -xzf "\$BACKUP_DIR/client_backup.tar.gz"

echo ""
echo "✓ Restore complete!"
echo ""
echo "Next steps:"
echo "  1. Verify files: cd \$TARGET_DIR && ls -la"
echo "  2. Run tests: uv run --with pytest python3 -m pytest test/ -v"
echo "  3. Test import: uv run python3 -c 'import tmi_client; print(\"OK\")'"
EOF

chmod +x "$BACKUP_DIR/restore.sh"
echo -e "${GREEN}✓ Restore script created${NC}"

# Final summary
echo ""
echo "========================================="
echo -e "${GREEN}BACKUP COMPLETE${NC}"
echo "========================================="
echo ""
echo "Backup location: $BACKUP_DIR"
echo ""
echo "Backed up:"
echo "  - Full client archive (tar.gz)"
echo "  - Current state snapshot"
echo "  - API and model inventories"
echo "  - Custom files and documentation"
echo "  - Post-regeneration checklist"
echo "  - Quick restore script"
echo ""
echo "Archive size:"
du -sh "$BACKUP_DIR/client_backup.tar.gz" | awk '{print "  "$1}'
echo ""
echo "To restore this backup:"
echo "  $BACKUP_DIR/restore.sh"
echo ""
echo "To proceed with regeneration:"
echo "  ./scripts/regenerate_client.sh"
echo ""
