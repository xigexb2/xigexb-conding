# Framework and infrastructure integration

**English** | [简体中文](../zh-CN/engineering/frameworks.md) | [Standards index](../translations.md)

Load only rules for frameworks actually used. Official documentation and repository-pinned versions determine version behavior, lifecycles, threading, upgrades.

## F01 Java service frameworks

- Identify Spring Boot/Spring Security, Quarkus, Jakarta separately and avoid mixing framework assumptions
- Use constructor injection, validated configuration, controlled startup, graceful shutdown; no implicit unsupervised initialization threads
- For Spring transactions inspect proxies, self-invocation, propagation, isolation, rollback, threading; reactive transactions follow actual context propagation
- Isolate blocking libraries from WebFlux/event loops; returning Mono/Future does not make internals nonblocking
- For Hibernate/JPA inspect query size, lazy loading, N+1, entity state; for MyBatis inspect parameterization and tenant predicates

## F02 Netty and high-performance networking

- Do not block or run long computations on event loops; bound offloading and preserve required per-connection ordering
- Define reference-counted ownership/transfers separately for reads, consumption, forwarding, asynchronous retention, outbound writes
- SimpleChannelInboundHandler, decoders, encoders may release automatically; prevent double release according to concrete contracts
- Choose retain, retained slices, copying by shared backing memory/lifetime rather than zero-copy slogans
- Release consumed, unforwarded references on all exits; do not unconditionally release after forwarding; define ownership on submission failure
- Do not use safeRelease to hide routine reference-count errors; expose leak detection and failure evidence
- Check callback threads, buffer validity, write ownership, shutdown semantics separately for gnalloy, gnet, netpoll, and similar libraries

## F03 Go / Rust / Python frameworks

- Gin, Echo, Fiber, net/http have different request context/object lifecycles; copy necessary data before asynchronous work
- Budget Tokio, Axum, Actix by runtime threads, blocking pools, extractor limits, connection-close contracts
- Distinguish sync/async handlers, ORM sessions, background-task lifecycles in FastAPI, Django, Flask
- Background work must not depend on released requests/connections; reliable jobs need durable queues and supervision
- Inspect default timeouts, body limits, connections, authentication instead of assuming production suitability

## F04 Frontend and component ecosystems

- Follow existing Vue, React, Angular, Svelte stacks; adopting a skill does not justify replacing the framework
- In React inspect pure rendering, effect cleanup, stable identity, concurrent requests; avoid storing every derived value through effects
- In Angular inspect change detection, subscriptions, DI lifecycles, template types; use Svelte's actual version-specific reactivity
- Choose SSR/SSG/CSR by first paint, SEO, authorization, caching, deployment capabilities
- Centralize component versions, design tokens, icons, forms, accessibility; see [design systems](../product/design-systems.md)

## F05 Redis, caching, and locks

- Define key namespaces, tenant/permission dimensions, capacity, TTL, null behavior, invalidation for every cache
- Avoid large/hot keys, unbounded collections, online full KEYS; scans still require limits and budgets
- Lua, transactions, atomic commands guarantee only their specified scope rather than cross-system atomicity
- Verify lock owners on release; renewal/process pauses affect leases; protect critical side effects with fencing or idempotency
- Redis caches/distributed locks do not replace durable uniqueness constraints

## F06 Kafka, RabbitMQ, MQTT

- Distinguish producer acknowledgments, broker durability, consumer acknowledgments, business transaction commits
- Bound retries/dead letters with reasons, retention, replay policies; inspect duplicate side effects
- Kafka ordering is partition-scoped; verify rebalance and committed-offset behavior
- RabbitMQ ack/nack/requeue/prefetch must prevent poison-message loops and consumer memory growth
- MQTT QoS, retained messages, sessions do not establish business completion; bind topic ACLs to identities

## F07 Storage and private infrastructure

- Specify MinIO/S3 permissions, presigned expiry, multipart uploads, checksums, lifecycles, streaming for large objects
- Limit GitLab/Artifactory exposure and permissions; define backup, upgrade, trusted artifact sources
- Define consistency, compensation, deletion propagation between indexes, object stores, databases
- Configure only selected integrations; disabled dependencies must not unexpectedly connect or open listeners
