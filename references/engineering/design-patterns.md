# Design-pattern selection and implementation constraints

**English** | [简体中文](../zh-CN/engineering/design-patterns.md) | [Standards index](../translations.md)

Patterns solve actual variation, ownership, and collaboration problems. Describe the variation and a minimal counterexample before selecting a pattern; do not require every class to demonstrate one.

## DP01 Creational patterns

| Pattern | Applicable variation | Constraints and costs |
| --- | --- | --- |
| Factory method | Construct different implementations under one contract | Define construction failures, registration conflicts, and cleanup; avoid repeated hot-path scanning |
| Abstract factory | Compatible families of implementations | Prevent mixed protocol/platform families; avoid a factory layer for one object |
| Builder | Multi-step construction and cross-field invariants | Validate completeness at build time; prevent partially initialized objects escaping |
| Prototype | Copy expensive configuration or object templates | Specify deep/shallow copying, shared resources, identity, and non-copyable locks |
| Singleton | A genuinely process-wide unique resource | Define initialization, concurrency, and shutdown; not distributed uniqueness or request-context storage |

## DP02 Structural patterns

| Pattern | Applicable variation | Constraints and costs |
| --- | --- | --- |
| Adapter | Translate an external interface into an internal port | Preserve errors, timeouts, and ownership; never turn failure into default success |
| Bridge | Two independently evolving dimensions | Introduce only for real variation in both dimensions; control combinations and assembly complexity |
| Composite | Uniform handling of tree objects | Detect cycles and bound depth/work; distinguish leaf and container constraints |
| Decorator | Stack metrics, caching, authorization, or similar behavior | Specify order, repeated application, and error propagation; do not cache unauthorized results |
| Facade | Stable access to a complex subsystem | Hide complexity without becoming an all-purpose service owning all state and business logic |
| Flyweight | Many objects sharing immutable intrinsic state | Keep external context separate and caches bounded; require memory evidence |
| Proxy | Access control, remote access, lazy loading | Specify remote failure and lifecycle; remote calls do not have local-call reliability |

## DP03 Behavioral patterns

| Pattern | Applicable variation | Constraints and costs |
| --- | --- | --- |
| Strategy | Replaceable algorithms, billing, routing | Preserve common pre/postconditions; separate selection from execution |
| State | Explicit legal transitions and event handling | Define terminal states, duplicates, concurrency, persistence; avoid implicit boolean combinations |
| Command | Queuing, auditing, retry, undo | Carry stable intent and idempotency keys; undo is not cross-system atomic rollback |
| Chain of responsibility | Composable validation/processing stages | Define short-circuiting, order, mandatory stages, and unhandled results; authorization cannot be skipped |
| Observer | Notify multiple subscribers | Define unsubscribe, ordering, buffers, failure isolation; avoid implicit synchronous cascades |
| Mediator | Central coordination among objects | Orchestrate only; domain rules remain in their owning modules |
| Iterator | Hide traversal structure | Define snapshots, concurrent changes, pagination, and handle closure; avoid unbounded materialization |
| Template method | Vary steps in a fixed workflow | Bound inheritance depth and callback timing; prefer function composition where simpler |
| Visitor | Extend operations over stable structures | Frequent node-type changes increase maintenance; preserve encapsulation and permissions |
| Memento | Recoverable local state snapshots | Limit sensitive content, size, versions, expiry; not a database-backup replacement |
| Interpreter | Simple constrained rule languages | Bound syntax, depth, time, capabilities; use mature parsers for complex languages |

## DP04 Architectural and distributed patterns

These operate at a different level from object patterns; select according to system risk:

- Repository/Unit of Work: isolate persistence and transaction coordination; avoid meaningless ORM wrappers
- Ports and adapters: isolate real external variation behind stable domain contracts; adapters own framework lifecycles
- CQRS: use when read/write models have distinct load or evolution requirements; accept synchronization and operational costs
- Outbox/Inbox: address transaction/message dual-write windows while retaining deduplication, replay, and backlog recovery
- Saga: define steps, failures, compensation, reconciliation; do not claim every side effect is reversible
- Bulkhead/circuit breaker/rate limiter: isolate resources and failures; define degradation, recovery, half-open behavior, and retry amplification controls
- Event sourcing: consider when event history is the authoritative fact; account for schema evolution, projections, and repairs

## DP05 Language mappings

- Java/Kotlin: interfaces serve stable variation points; choose constructor injection and sealed types by the model, without mechanically pairing every class with an interface
- Go: define small interfaces at the consumer; prefer functions and composition over Java-style inheritance structures
- Rust: choose enums, traits, generics, and trait objects by ownership, extension, and cost; do not use clone to avoid design
- C: express contracts with explicit contexts, function tables, opaque handles; pair initialization/destruction and avoid a global pseudo-object system
- C++: combine value semantics, RAII, templates, runtime polymorphism as needed without breaking lifecycles to fit patterns
- Python/JS/TS: use functions, protocols, lightweight objects when sufficient; avoid elaborate inheritance for simple flows
- Vue/native UI: assign responsibilities to components, state owners, composable logic; views must not directly own databases or global transport

## DP06 Acceptance

Identify the real variation solved, callers unchanged by replacement, added complexity, and cleanup conditions. Consider removing a wrapper if doing so loses no contract or isolation.

Every pattern implementation still follows the 20 same-family source files per directory limit; do not fragment one business capability into cyclic pieces just to house pattern roles.
