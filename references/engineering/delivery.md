# Builds, CI/CD, observability, and operations

**English** | [简体中文](../zh-CN/engineering/delivery.md) | [Standards index](../translations.md)

## OPS01 Builds and configuration

- Trace toolchains, dependencies, build parameters; prefer repository wrappers, lockfiles, controlled mirrors
- Separate build/runtime configuration; validate ranges, units, required/default values; startup failures must not silently select unsafe defaults
- Keep only necessary environment differences and inject secrets securely; omit internal infrastructure from public generic examples
- Use suitable unprivileged container users, minimal contents, resource limits, signal handling; audit image tag/digest policies
- Associate artifacts with source, build numbers, dependencies, configuration versions; verify reproducible procedures before release

## OPS02 CI and releases

- Run language-appropriate formatting, type/static checks, compilation, applicable tests, security checks; do not unconditionally ignore failures
- Match check scope to change risk; cache keys include toolchains, lockfiles, other necessary inputs
- Isolate untrusted PRs from release permissions; do not automatically execute installation scripts found in upstream documents
- Complete reviewable artifacts and verification before authorized external actions
- Design staged rollout, health metrics, stop conditions, rollback, database compatibility together
- Distinguish application update manifests, containers, packages, firmware channels and confirm actual targets

## OPS03 Service reliability

- Define user-visible SLI/SLO, error budgets, capacity, dependency budgets from business requirements rather than arbitrary numbers
- Distinguish readiness, liveness, startup probes; downstream failure must not cause repeated cluster-wide restarts
- On shutdown, stop admission before bounded waits/cancellation and connection, session-lock, subscription cleanup
- Define multi-instance task ownership/recovery; process-local tables alone cannot isolate failures
- Select limits, circuit breakers, bulkheads, degradation, caches from actual failure models instead of stacking middleware for patterns
- Correlate logs, metrics, traces, audits while limiting sensitive data, volume, cardinality

## OPS04 Operations and incidents

- Runbooks cover configuration, dependencies, startup, health, backup/restore, scaling, common diagnosis
- Correlate time, versions, configuration, context; distinguish facts, root causes, contributing factors, actions in reviews
- Test actual RPO/RTO through restore/failover exercises; existing backup files are not proof of successful recovery
- Give temporary mitigations expiry and root-cause follow-up; do not permanently disable authentication, certificate validation, logging
- Deployments, data changes, public notifications follow task authorization; general development requests do not authorize production operations
