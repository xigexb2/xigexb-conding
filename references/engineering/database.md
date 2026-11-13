# Data modeling, SQL, and persistence

**English** | [简体中文](../zh-CN/engineering/database.md) | [Standards index](../translations.md)

See [SQL](../languages/sql.md) for dialect details and [security](security.md) for controls.

## DB01 Models and constraints

- Define primary keys, uniqueness, foreign keys, state constraints, tenant scope, lifecycle from business invariants
- Use database uniqueness for identity links, orders, idempotency records; Redis locks and application check-then-insert are insufficient
- Specify units, ranges, nullability, defaults, time zones, retention; do not conflate unknown values with real zero through magic values
- Design soft deletion together with uniqueness, relationships, archival, privacy deletion
- Separate high-volume audits from primary business state according to queries, retention, transactions; prevent unbounded growth
- Use JSON columns for suitable extension data rather than replacing all structured constraints/query models

## DB02 Transactions and concurrency

- Define transaction boundaries, isolation, lock order, retryable errors, maximum duration
- Identically named isolation levels can differ between databases; verify phantoms, write skew, read/write conflicts for the actual version
- Avoid slow external calls inside transactions; address commit/message dual writes with outbox or equivalent
- Optimistic updates check versions/old state and affected rows; conflicts are not success
- Retry deadlocks/serialization failures within idempotent boundaries, bounded by backoff and total budget
- Size pools by database capacity and service instance count rather than enlarging them to hide slow queries
- Release session locks/variables before returning connections; destroy uncertain connections according to pool contracts and verify cleanup

## DB03 Queries and indexes

- Design indexes from real filters, joins, sorting, selectivity; assess column order and write amplification
- Inspect plans, estimated/actual rows, caches, I/O, statistics, lock waits
- Sequential scans may be optimal for small tables or queries returning a large fraction of rows; analysis takes precedence over requiring an index
- Bound online result sets/scans; budget diagnostics, offline jobs, migrations separately
- Use bounded batches and stable cursors for aggregation, exports, recovery; avoid deep pagination and starvation of later records
- Avoid N+1 with controlled batching; joins/eager loading must not create unbounded intermediate results
- Define replica lag and read-your-writes for read/write splitting; critical reads must not silently use stale replicas

## DB04 Security and tenancy

- Bind values and allowlist dynamic identifiers; never concatenate external SQL fragments directly
- Obtain tenant IDs from trusted authentication context; apply scope to queries, mutations, joins, caches, exports
- Verify actual roles and bypass conditions for PostgreSQL RLS and similar mechanisms; they do not replace every application authorization check
- Give application accounts least privilege; separate administration, migration, read-only identities; exclude credentials from source/logs
- Read sensitive fields minimally for the purpose; backups, logs, test copies require equivalent protection

## DB05 Migration and recovery

- Leave no ad hoc SQL files; create formal migrations only when explicitly authorized by the task
- Assess DDL locks, index creation, backfills, version coexistence, rollback limits using representative data sizes
- Expand fields, backfill in batches, switch reads/writes, then contract after confirmation; avoid requiring simultaneous deployment/database changes
- Define RPO/RTO; completed backups do not prove recoverability, so rehearse restoration and application usability
- Production repairs need explicit scope, preview, affected-row checks, audit, recovery path; general coding authorization does not authorize production writes
