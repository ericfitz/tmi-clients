# TMI JavaScript Client Regeneration Guide

This directory contains automated tools for regenerating the TMI JavaScript client from the OpenAPI specification with intelligent defaults.

## Quick Start

```bash
cd javascript-client-generated
./scripts/regenerate_client.sh
```

That's it! The script automatically applies all modern Node.js configurations and security updates.

## Automatic Defaults

The regeneration process automatically applies these intelligent defaults:

### Package Configuration
- **Package name**: `tmi-js-client`
- **Module name**: `TmiJsClient`
- **Version**: `1.0.0`
- **Language**: JavaScript (ES6)
- **HTTP Client**: `superagent`
- **Use Promises**: `true`
- **License**: Apache-2.0

### Node.js Version
- **Minimum Node.js**: `18+`
- **Reason**: Modern ES6+ features, native Promise support, security fixes

### Dependency Versions (Security-Hardened)

All dependencies are automatically updated to secure, modern versions:

| Package | Old Version | New Version | Reason |
|---------|-------------|-------------|--------|
| `superagent` | 5.3.1 | >= 10.2.3 | Multiple CVE fixes (security vulnerabilities) |
| `mocha` | 3.x | >= 11.7.4 | Modern test runner, async/await support |
| `chai` | 4.x | >= 5.1.2 | Modern assertion library |
| `sinon` | 7.5.0 | >= 21.0.0 | Modern test doubles, better async support |
| `@babel/core` | N/A | >= 7.28.4 | Modern JavaScript transpilation |
| `@babel/preset-env` | N/A | >= 7.28.3 | Smart polyfills based on target environments |

### Testing Framework
- **Test runner**: `mocha` (modern async support)
- **Assertions**: `chai` (BDD/TDD assertions)
- **Test doubles**: `sinon` (spies, stubs, mocks)
- **Build tool**: `babel` (ES6+ transpilation)

### Modern Packaging
- **Format**: `package.json` with ES6 modules
- **Build command**: `npm run build` (Babel transpilation)
- **Test command**: `npm test` (Mocha with Babel)
- **Structured metadata**: Repository, keywords, license

### Critical Patches

The script checks for these potential issues (manual verification recommended):

1. **DfdDiagram Constructor**
   - Issue: Type parameter may be overwritten
   - Location: `src/model/DfdDiagram.js`
   - Check: Ensure `type` parameter is passed correctly to parent

2. **DfdDiagramInput Constructor**
   - Same potential issue as DfdDiagram
   - Location: `src/model/DfdDiagramInput.js` (if present)
   - Ensures input schemas work correctly

## Files

### Configuration Files

#### `scripts/swagger-codegen-config.json`
```json
{
  "moduleName": "TmiJsClient",
  "projectName": "tmi-js-client",
  "projectVersion": "1.0.0",
  "projectDescription": "JavaScript client for TMI (Threat Modeling Improved) API",
  "projectLicenseName": "Apache-2.0",
  "sortParamsByRequiredFlag": true,
  "hideGenerationTimestamp": false,
  "usePromises": true,
  "useES6": true,
  "npmName": "tmi-js-client",
  "npmVersion": "1.0.0"
}
```

**Purpose**: Tells swagger-codegen how to generate the client with correct naming and modern JavaScript features.

### Regeneration Script

#### `scripts/regenerate_client.sh`
**Purpose**: Fully automated regeneration with all patches and updates.

**What it does**:
1. ✅ Validates prerequisites (swagger-codegen, Node.js)
2. ✅ Backs up custom files (package.json, tests, docs)
3. ✅ Cleans generated files (preserves custom files)
4. ✅ Runs swagger-codegen with configuration
5. ✅ Applies constructor patches (with warnings for manual verification)
6. ✅ Creates modern package.json with secure dependencies
7. ✅ Creates .babelrc for ES6 transpilation
8. ✅ Installs dependencies via npm
9. ✅ Runs all tests
10. ✅ Runs integration tests (if present)
11. ✅ Generates summary report

**Exit codes**:
- `0`: Success - all tests passing
- `1`: Failure - check logs

## Prerequisites

### Required Tools

```bash
# Install swagger-codegen
brew install swagger-codegen

# Install Node.js 18+
brew install node

# Verify installations
swagger-codegen version  # Should be >= 3.0.75
node -v                  # Should be >= 18.0.0
npm -v
```

### Required Files

- OpenAPI spec: `/Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json`
- Must be valid OpenAPI 3.0+ specification

## Usage

### Basic Regeneration

```bash
# From the javascript-client-generated directory
./scripts/regenerate_client.sh
```

### Verify Results

```bash
# Check the report
cat REGENERATION_REPORT.md

# Run tests manually
npm test

# Run integration tests
node test_diagram_fixes.js
```

### Output Files

After regeneration, you'll find:

```
javascript-client-generated/
├── src/
│   ├── tmi-client/           # API classes (13+ APIs)
│   ├── model/                # Model classes (100+ models)
│   ├── ApiClient.js          # Base API client
│   └── index.js              # Main entry point
├── test/
│   ├── api/                  # API tests
│   └── model/                # Model tests
├── docs/                     # Auto-generated documentation
│   └── developer/            # Custom developer docs (preserved)
├── package.json              # Modern dependencies
├── .babelrc                  # Babel configuration
└── test_diagram_fixes.js     # Integration tests (if created)

REGENERATION_REPORT.md        # Detailed report
test_output.log               # Test results
integration_test_output.log   # Integration test results
```

## What Gets Preserved

The script automatically preserves:

- ✅ `package.json` (custom configuration)
- ✅ `.babelrc` (Babel configuration)
- ✅ `test_diagram_fixes.js` (integration tests)
- ✅ `.swagger-codegen-ignore` (if exists)
- ✅ `docs/developer/` (custom documentation)

All other files are regenerated from scratch.

## What Gets Updated

### Always Updated
- All source files (`src/tmi-client/*.js`, `src/model/*.js`)
- All test files (`test/api/*.js`, `test/model/*.js`)
- Auto-generated documentation (`docs/*.md`)
- Base API client (`src/ApiClient.js`)

### Conditionally Updated
- `package.json` - Only if backup doesn't exist
- `.babelrc` - Only if backup doesn't exist
- Test utilities - Auto-generated each time

## Customization

### Change Package Version

Edit `scripts/swagger-codegen-config.json`:
```json
{
  "projectVersion": "1.1.0",  // Change here
  "npmVersion": "1.1.0"       // And here
}
```

### Change Node.js Minimum Version

Edit the warning in `scripts/regenerate_client.sh` (line ~76):
```bash
if [ "$NODE_VERSION" -lt 20 ]; then  # Change from 18 to 20
    echo -e "${YELLOW}WARNING: Node.js version is $NODE_VERSION. Recommend 20+ for best compatibility.${NC}"
fi
```

### Add Custom Dependencies

Edit the package.json template in `scripts/regenerate_client.sh` (around line 204):
```json
"dependencies": {
  "superagent": "^10.2.3",
  "your-custom-package": "^1.0.0"  // Add here
}
```

### Add Custom Patches

Edit `scripts/regenerate_client.sh` around line 125 (after DfdDiagramInput check):
```bash
# Add your custom patch
CUSTOM_FILE="$CLIENT_DIR/src/model/YourModel.js"
if [ -f "$CUSTOM_FILE" ]; then
    echo "  Patching YourModel..."
    # Add sed commands or other modifications
    sed -i.bak 's/old_pattern/new_pattern/' "$CUSTOM_FILE"
    rm -f "${CUSTOM_FILE}.bak"
fi
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

If it's in a different location, edit `scripts/regenerate_client.sh` line 50:
```bash
OPENAPI_SPEC="/path/to/your/tmi-openapi.json"
```

### "Node.js not found"

```bash
brew install node
```

### Tests Failing After Regeneration

1. Check `test_output.log` for details
2. Verify OpenAPI spec is valid
3. Check if new breaking changes in spec
4. Review `REGENERATION_REPORT.md`

### Constructor Patches Need Manual Verification

JavaScript constructor patterns differ from Python. After regeneration:

1. Check `src/model/DfdDiagram.js` constructor
2. Verify `type` parameter is passed correctly to `super()`
3. Check `src/model/DfdDiagramInput.js` (if present)

Example of correct pattern:
```javascript
constructor(type, cells, id, name, createdAt, modifiedAt) {
  super(id, name, type, createdAt, modifiedAt);  // type passed correctly
  this.cells = cells;
}
```

### npm install fails

Try clearing cache:
```bash
rm -rf node_modules package-lock.json
npm cache clean --force
npm install
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Regenerate TMI JavaScript Client

on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly on Sunday
  workflow_dispatch:

jobs:
  regenerate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install swagger-codegen
        run: |
          wget https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.75/swagger-codegen-cli-3.0.75.jar -O swagger-codegen-cli.jar
          echo "alias swagger-codegen='java -jar swagger-codegen-cli.jar'" >> ~/.bashrc

      - name: Regenerate client
        run: |
          cd javascript-client-generated
          ./scripts/regenerate_client.sh

      - name: Create PR
        uses: peter-evans/create-pull-request@v5
        with:
          title: "chore: regenerate TMI JavaScript client"
          body: "Automated client regeneration from latest OpenAPI spec"
          branch: "automated/regenerate-js-client"
```

## Version History

### 1.0.0 (2025-01-12)
- Initial automated regeneration script
- Node.js 18+ support
- Modern dependency versions with CVE fixes
- Constructor patch warnings
- Webhook API support
- Cell schema simplification

## Best Practices

### Before Regeneration
- [ ] Commit any local changes
- [ ] Update OpenAPI spec to latest version
- [ ] Review spec for breaking changes
- [ ] Back up custom code if any

### After Regeneration
- [ ] Review `REGENERATION_REPORT.md`
- [ ] Check test results (all should pass)
- [ ] Review git diff for unexpected changes
- [ ] Manually verify constructor patches
- [ ] Update CHANGELOG.md if needed
- [ ] Test with dependent projects
- [ ] Create PR for review

### Frequency
- **On OpenAPI spec changes**: Always regenerate
- **Security updates**: Monthly dependency check
- **Regular maintenance**: Quarterly regeneration
- **Before releases**: Always regenerate and test

## Key Differences from Python Client

### Constructor Patching
- **Python**: Can use `sed` to insert code before `__init__` call
- **JavaScript**: More complex due to `super()` requirements
- **Solution**: Manual verification recommended after each regeneration

### Dependency Management
- **Python**: `pyproject.toml` + `setup.py` + `requirements.txt`
- **JavaScript**: `package.json` only
- **JavaScript advantage**: Simpler, single source of truth

### Test Framework
- **Python**: `pytest` with fixtures
- **JavaScript**: `mocha` + `chai` with async/await
- **Both**: Modern, well-supported frameworks

### Build Process
- **Python**: No build step (direct interpretation)
- **JavaScript**: Babel transpilation to ES5 for compatibility
- **Trade-off**: Extra build step vs. wider compatibility

## Support

For issues with regeneration:

1. Check this README
2. Review `REGENERATION_REPORT.md` after running
3. Check `test_output.log` for test failures
4. See [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) for API usage
5. See [CHANGELOG.md](CHANGELOG.md) for version history

## License

Apache-2.0 (same as TMI project)
