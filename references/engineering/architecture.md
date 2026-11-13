# Architecture, requirements, and design patterns

**English** | [简体中文](../zh-CN/engineering/architecture.md) | [Standards index](../translations.md)

## A01 Start with invariants

- Express requirements as observable behavior: who provides what input, under which conditions, with what result and failure presentation
- Separate facts, assumptions, constraints, and pending decisions; define acceptance criteria for capacity, latency, availability, and data correctness
- Describe business invariants before choosing frameworks; money, identity, resource ownership, and state transitions must not be scattered across controllers
- Maintain a shared vocabulary that distinguishes devices, gateways, sessions, users, tenants, and their identity lifecycles
- Fit new requirements into stable existing boundaries; split services when deployment, scaling, failure, or organizational independence requires it

## A02 Modules and interfaces

- Each package/directory across all languages directly owns at most 20 same-family source files, including tests and first-party generated code; plan cohesive subpackages during design; see [directory limits](../directory-structure.md)
- Divide modules by business capability; distinguish entry points, application orchestration, domain rules, ports, and adapters within them
- Simple layering is valid for small CRUD systems; do not impose full DDD, CQRS, or microservice templates
- Direct dependencies toward stable business contracts; domain code must not depend on HTTP requests, ORM sessions, or framework internals
- HTTP/MQTT adapters may use native framework types within their boundaries; domain isolation does not prohibit framework types throughout the system
- Separate DTOs, persistence entities, and protocol messages by contract; reuse identical stable simple types where appropriate instead of duplicating meaningless conversions
- Interfaces express capabilities and failure contracts without exposing executors, connections, locks, or mutable internal collections
- Specify command/query side effects and stable pagination, sorting, null, error-code, and compatibility semantics
- Specify collection immutability and copy depth; an immutable view cannot stop another owner from modifying its backing collection

## A03 Choose patterns

| Actual variation | Candidate pattern | Avoid |
| --- | --- | --- |
| Algorithms, billing, routing | Strategy | Numerous classes for one stable branch |
| Type selection and construction | Registry, factory, builder | Hot-path scanning and global mutable registries |
| External services and protocols | Ports/adapters, adapter | Framework types leaking into the domain |
| Legal state transitions | State machine | Implicit states made from multiple booleans |
| Transparent metrics, limits, enhancement | Decorator | Order dependencies without a composition contract |
| Event notification | Observer, publish/subscribe | Unbounded subscriptions, lost errors, missing unsubscribe |
| Fixed skeleton with limited variation | Template method or function composition | Deep inheritance and implicit superclass-call obligations |
| Compensatable multi-step workflows | Saga, compensation | Claiming database-style atomic rollback |

State the variation and cost first. Prefer composition to deep inheritance; use plain functions and data structures when they express the problem clearly.
See [design patterns](design-patterns.md) for detailed selection, pitfalls, and language mappings.

## A04 State machines and asynchronous flows

- Define states, events, guards, terminal states, persistence points, and duplicate-event behavior
- Cancellation, timeout, execution failure, and unknown outcome are different facts; terminal updates require idempotency or CAS conditions
- A timeout ends observation and does not prove non-execution; define whether background work continues
- Define each operation's idempotency key, lifetime, duplicate response, and inquiry/reconciliation for unknown results
- Assign parallel-task ownership and join conditions; specify child cancellation and cleanup when the parent ends
- Execute initialization, reset, validation, execution, and upload according to business prerequisites; do not infer device state from packet arrival order

## A05 Evolution and compatibility

- Assess compatibility in both directions for APIs, wire protocols, configuration, databases, and deployed versions
- Follow expand, migrate, contract; rolling back code does not automatically undo transformed data
- Treat field deletion, default changes, and narrowed ranges as potential compatibility changes
- Record significant decisions in short ADRs: context, alternatives, decision, costs, and revalidation conditions
- Keep dependency graphs acyclic; shared modules contain stable capabilities rather than business-specific variation
- Introduce abstractions when variation has evidence, rather than anticipating imaginary futures

## A06 Design deliverables

For complex changes, provide useful module, state, or sequence diagrams consistent with the final implementation. Reviewers must be able to identify data ownership, state writers, failure propagation, resource cleanup, and how users confirm results.
