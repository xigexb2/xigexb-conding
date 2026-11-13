# SQL and database dialects

**English** | [简体中文](../zh-CN/languages/sql.md) | [Standards index](../translations.md)

Each package/directory directly owns at most 20 same-family source files, including tests, declarations, and first-party generated files. Design cohesive subpackages according to the [shared directory standards](../directory-structure.md).

SQL is declarative; correctness depends on models, NULL, transactions, dialects. See [database design](../engineering/database.md) for persistence architecture.

- Identify PostgreSQL, MySQL, SQL Server, Oracle, SQLite versions; do not mix dialect/isolation assumptions
- Bind values through drivers; MyBatis values use #{}, never user values in ${}
- Tables, columns, sort directions need server-side allowlisted mappings rather than ordinary value binding
- Select explicit columns to control disclosure/transfer; assess small controlled diagnostic queries by context
- Reason about NULL's three-valued logic in NOT IN, comparisons, aggregates, outer joins
- Filter placement in JOIN/WHERE/HAVING affects results; do not relocate merely for plans
- Use stable sufficiently unique pagination ordering; assess keysets for deep pages and define concurrent-change visibility
- Bound bulk transaction duration, parameters, message size, locks
- Scope updates/deletes by tenant/business conditions, check affected rows, handle optimistic conflicts
- Use unique/foreign-key/CHECK constraints for expressible invariants rather than application check-then-write alone
- Choose suitable temporal, monetary, ID, JSON types and verify encodings/collations
- EXPLAIN ANALYZE may execute statements; select safe authorized verification for writes/expensive queries
- Assess indexes/statistics using actual queries/write costs; sequential scans are not automatically errors
- Define execution/rollback boundaries for migrations, procedures, triggers; leave no ad hoc SQL files
- Follow actual database documentation for transactional DDL, implicit commits, online indexes, locks

The skill does not automatically create .sql files; formal migrations needing them follow the explicitly authorized exception in the personal conventions.
