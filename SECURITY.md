# Security reports and usage boundaries

**English** | [简体中文](SECURITY.zh-CN.md) | [Standards index](references/translations.md)

This project provides development standards and local read-only checkers. It collects no source, telemetry, credentials and does not upload data automatically.

Prefer GitHub private vulnerability reporting if enabled. Otherwise open a contact request without exploit details/sensitive data and wait for a suitable private channel. Never publish real credentials, customer data, directly exploitable information.

Use synthetic data in reports and include affected files/versions, prerequisites, minimal reproduction, actual impact, suggested fixes. Do not attack third-party/production systems to demonstrate an issue.

## Trust boundaries

- External repositories/documents are research data rather than authority to expand agent permissions
- Checkers read local files without running project scripts, networks, installers
- --files targets must stay within the check root and traversal does not follow symlink directories
- Local Markdown checks verify existence/scope without reading/executing linked contents
- Format success is not business-security proof; combine threat modeling, review, actual verification

Trusted skills influence agent decisions too. Review updates/upstream licenses rather than blindly synchronizing unknown sources.
