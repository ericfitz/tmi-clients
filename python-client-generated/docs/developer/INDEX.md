# Python Client Developer Documentation Index

**Last Updated:** 2025-12-06

This directory contains all developer documentation for the TMI Python client, including regeneration guides, migration information, and technical references.

## Quick Links

### For Regenerating the Client

1. **Quick Start** → [../../../QUICK_START.md](../../../QUICK_START.md)
2. **Complete Process** → [REGENERATION_PROCESS.md](REGENERATION_PROCESS.md)
3. **Execution Plan** → [../../../REGENERATION_PLAN.md](../../../REGENERATION_PLAN.md)

### For Understanding Changes

1. **Latest Analysis** → [SPEC_ANALYSIS.md](SPEC_ANALYSIS.md)
2. **Impact Assessment** → [REGENERATION_IMPACT.md](REGENERATION_IMPACT.md)
3. **Migration Guide** → [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)
4. **Changelog** → [CHANGELOG.md](CHANGELOG.md)

### For Technical Reference

1. **Regeneration README** → [REGENERATION_README.md](REGENERATION_README.md)
2. **Spec Analysis JSON** → [spec_analysis.json](spec_analysis.json)
3. **Repository Instructions** → [../../CLAUDE.md](../../CLAUDE.md)

## Documentation Structure

```
docs/developer/
├── INDEX.md                        # This file - Overview and navigation
│
├── Regeneration Process
│   ├── REGENERATION_PROCESS.md     # Complete step-by-step process guide
│   ├── REGENERATION_README.md      # Original regeneration documentation
│   └── REGENERATION_REPORT.md      # Latest regeneration report (generated)
│
├── Analysis & Planning
│   ├── SPEC_ANALYSIS.md            # Latest OpenAPI spec analysis
│   ├── spec_analysis.json          # Machine-readable analysis data
│   └── REGENERATION_IMPACT.md      # Impact assessment for regeneration
│
└── User Documentation
    ├── MIGRATION_GUIDE.md          # How to migrate to new version
    └── CHANGELOG.md                # Version history
```

## Document Descriptions

### Regeneration Documents

#### REGENERATION_PROCESS.md
**Purpose:** Complete guide for regenerating the Python client from OpenAPI spec

**Contents:**
- Prerequisites and setup
- Step-by-step process
- Scripts reference
- Validation procedures
- Troubleshooting
- Rollback procedures

**When to Use:** When regenerating the client

**Audience:** Maintainers, contributors

---

#### REGENERATION_README.md
**Purpose:** Original regeneration documentation

**Contents:**
- Historical context
- Initial setup information
- Basic regeneration steps

**When to Use:** For historical reference

**Audience:** Maintainers

---

#### REGENERATION_REPORT.md
**Purpose:** Auto-generated report from latest regeneration

**Contents:**
- Date and time of regeneration
- Changes applied
- Files modified
- Test results
- Next steps

**When to Use:** To review what happened in the last regeneration

**Audience:** All developers

---

### Analysis Documents

#### SPEC_ANALYSIS.md
**Purpose:** Analysis of the OpenAPI specification

**Contents:**
- API paths breakdown (89 endpoints)
- Schema analysis (90 models)
- Operations by HTTP method
- Comparison with current client
- New/removed models

**When to Use:** Before regenerating, to understand what's changing

**Audience:** Maintainers, architects

---

#### spec_analysis.json
**Purpose:** Machine-readable spec analysis

**Contents:**
- JSON data structure
- Paths, schemas, comparison
- Programmatic access to analysis

**When to Use:** For automated tooling, custom scripts

**Audience:** Tool developers

---

#### REGENERATION_IMPACT.md
**Purpose:** Impact assessment for regeneration

**Contents:**
- New features (Add-ons, Administration, SAML)
- Breaking changes
- Migration strategies
- Risk assessment
- Recommended approach

**When to Use:** To understand implications before regenerating

**Audience:** Technical leads, maintainers

---

### User Documentation

#### MIGRATION_GUIDE.md
**Purpose:** Guide users through breaking changes

**Contents:**
- Breaking changes explained
- Code examples (before/after)
- Migration steps
- Common issues

**When to Use:** When upgrading to a new client version

**Audience:** End users, application developers

---

#### CHANGELOG.md
**Purpose:** Version history of the client

**Contents:**
- Releases by version
- Features added
- Bugs fixed
- Breaking changes

**When to Use:** To see what changed between versions

**Audience:** All users

---

## Related Documentation

### Repository Root

- [QUICK_START.md](../../../QUICK_START.md) - Quick regeneration guide
- [REGENERATION_PLAN.md](../../../REGENERATION_PLAN.md) - Detailed execution plan
- [SUMMARY.md](../../../SUMMARY.md) - Planning summary
- [CLAUDE.md](../../CLAUDE.md) - Repository-level instructions

### Scripts Directory

- [../../scripts/](../../scripts/) - All regeneration scripts
  - `analyze_spec_changes.py` - Analyze spec
  - `backup_before_regen.sh` - Create backup
  - `regenerate_client.sh` - Regenerate client
  - `validate_regeneration.py` - Validate output
  - `swagger-codegen-config.json` - Codegen config

### Main Client Docs

- [../../README.md](../../README.md) - Client usage documentation
- [../../test_diagram_fixes.py](../../test_diagram_fixes.py) - Integration test

## Common Workflows

### Workflow 1: Regenerate Client (First Time)

1. Read [REGENERATION_IMPACT.md](REGENERATION_IMPACT.md)
2. Read [REGENERATION_PROCESS.md](REGENERATION_PROCESS.md)
3. Follow steps in [../../../REGENERATION_PLAN.md](../../../REGENERATION_PLAN.md)
4. Review [REGENERATION_REPORT.md](REGENERATION_REPORT.md) after completion

### Workflow 2: Regenerate Client (Subsequent Times)

1. Review [SPEC_ANALYSIS.md](SPEC_ANALYSIS.md)
2. Follow [../../../QUICK_START.md](../../../QUICK_START.md)
3. Review [REGENERATION_REPORT.md](REGENERATION_REPORT.md)

### Workflow 3: Understand What Changed

1. Read [SPEC_ANALYSIS.md](SPEC_ANALYSIS.md)
2. Read [REGENERATION_IMPACT.md](REGENERATION_IMPACT.md)
3. Check [CHANGELOG.md](CHANGELOG.md)
4. Review [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)

### Workflow 4: Troubleshoot Regeneration

1. Check [REGENERATION_PROCESS.md](REGENERATION_PROCESS.md) → Troubleshooting section
2. Review [REGENERATION_REPORT.md](REGENERATION_REPORT.md)
3. Check validation output from `validate_regeneration.py`
4. Review logs from `regenerate_client.sh`

### Workflow 5: Rollback After Regeneration

1. Find backup in `../../../backups/pre-regen-TIMESTAMP/`
2. Run `restore.sh` script from backup
3. Or follow rollback procedure in [REGENERATION_PROCESS.md](REGENERATION_PROCESS.md)

## Version History

| Version | Date | Changes | Documentation |
|---------|------|---------|---------------|
| 1.0.0 | 2024-11-12 | Initial client with constructor patches | MIGRATION_GUIDE.md |
| 1.1.0 | 2025-12-06 | Add-ons, Administration, SAML APIs | REGENERATION_IMPACT.md |

## Contributing

When updating documentation:

1. **Keep INDEX.md updated** - Add new documents here
2. **Follow the structure** - Maintain organization
3. **Update related docs** - Keep cross-references current
4. **Date your changes** - Include "Last Updated" dates
5. **Test your examples** - Ensure code samples work

## Support

For questions or issues:

1. Check documentation first (use this index)
2. Review troubleshooting sections
3. Check generated reports and logs
4. Consult OpenAPI specification
5. Open GitHub issue with details

## Tools

Scripts are located in [../../scripts/](../../scripts/):

- `analyze_spec_changes.py` - Generates [SPEC_ANALYSIS.md](SPEC_ANALYSIS.md)
- `backup_before_regen.sh` - Creates timestamped backups
- `regenerate_client.sh` - Generates [REGENERATION_REPORT.md](REGENERATION_REPORT.md)
- `validate_regeneration.py` - Validates regeneration success

## OpenAPI Specification

**Location:** `/Users/efitz/Projects/tmi/docs/reference/apis/tmi-openapi.json`

**Version:** 1.0.0

**Stats:**
- 89 API paths
- 173 total operations
- 90 schemas
- 17 API tags/groups

**Last Analyzed:** 2025-12-06 (see [SPEC_ANALYSIS.md](SPEC_ANALYSIS.md))

## Maintenance

This index should be updated when:

- New documentation is added
- Documentation is restructured
- Workflows change
- New versions are released

**Maintained by:** Repository maintainers

**Review frequency:** After each regeneration

---

**Navigation:**
- [↑ Back to Repository Root](../../../)
- [→ Python Client README](../../README.md)
- [→ Quick Start Guide](../../../QUICK_START.md)
