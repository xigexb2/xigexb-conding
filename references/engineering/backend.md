# Backend, enterprise practices, and business systems

**English** | [简体中文](../zh-CN/engineering/backend.md) | [Standards index](../translations.md)

## BE01 Business and service boundaries

- Establish enterprise/consumer context, tenancy, deployment, peaks, data classification, and failure impact before applying large-company architecture labels
- Distinguish public APIs, application services, domain rules, persistence, integrations; retain a modular monolith as a valid choice
- Name public interfaces by business capability; extend configuration/strategy through stable contracts instead of endless branches or all-purpose services
- Route sensitive mutations through consistent authorization/domain validation, including background jobs and batch endpoints
- Maintain one authoritative data source; mark caches, search indexes, reports as derived data with defined lag

## BE02 API contracts

- Specify inputs, outputs, errors, pagination, limits, compatibility with OpenAPI, schemas, or existing project contracts
- Respect HTTP methods, safety, idempotency, meaningful status codes; do not return indistinguishable success for every failure
- Return trackable operation IDs and status resources for asynchronous work; distinguish accepted, processing, completed, failed, unknown
- Bind idempotency keys to operation, caller, tenant, request digest; reject changed payloads under the same key and claim atomically
- Bound pagination, batches, uploads, exports, callbacks by counts/bytes, timeouts, and partial-failure policies
- Provide stable error identifiers; separate user explanations from internal diagnostics and avoid stack/sensitive-data disclosure
- Prefer additive compatible evolution with deprecation windows; plan migration for removal and semantic changes

## BE03 Enterprise and consumer products

| Scenario | Priorities |
| --- | --- |
| Enterprise administration/approvals | Tenancy, organization permissions, audits, batches, exports, configuration versions, recoverable workflows |
| High-traffic consumer services | Latency budgets, abuse prevention, hot-spot isolation, privacy, staged rollout, conversion flows, weak networks |
| Private deployment | Configurable dependencies, offline installation, upgrade compatibility, backup/restore, minimal operations surface |
| IoT platforms | Device identity, routing, sessions, protocols, late messages, offline state, command acknowledgment semantics |

Scenarios can overlap. Enterprise products still need good UX; consumer products still need accounting invariants rather than blanket eventual consistency.

## BE04 Consistency and background work

- Preserve invariants with constraints, unique keys, transactions, optimistic concurrency; distributed locks do not replace database constraints
- Define outbox, events, compensation, reconciliation across databases/services; ordinary message delivery does not establish end-to-end exactly-once
- Scheduled jobs require ownership, duplicate-trigger policy, failure detection, recovery scanning that does not always examine only the first batch
- Use fencing or downstream idempotency for expired leases and stale instances; a pre-send check alone cannot prove isolation
- Preserve audit facts for unknown outcomes and converge through inquiry/reconciliation instead of marking success or blindly replaying side effects
- Isolate batches by tenant/downstream so one large customer cannot occupy every connection or queue

## BE05 Using public enterprise practices

- Google API Improvement Proposals inform resource/API evolution; Google SRE informs SLI/SLO, capacity, incident reviews
- Microsoft architecture patterns inform retry, isolation, caching, compensation; AWS Well-Architected informs operations, reliability, cost
- Public Alibaba Java guidance informs naming, layering, engineering checks; document conflicts with personal formatting or newer JDK behavior rather than copying obsolete rules
- Uber Go guidance supplements team practice; official Go semantics and tooling remain authoritative
- Framework vendors define their specific contracts; another company's technology use does not establish this project's need
- Select a coherent executable set instead of combining contradictory company practices into universal mandates

## BE06 Acceptance

Check authorization bypass, concurrent duplicates, connection/queue saturation, dependency timeouts, restart recovery, error observability. If only compilation passed, report compilation rather than claiming multi-instance reliability or production capacity.
