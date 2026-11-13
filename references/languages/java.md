# Java

**English** | [简体中文](../zh-CN/languages/java.md) | [Standards index](../translations.md)

Each package/directory directly owns at most 20 same-family source files, including tests, declarations, and first-party generated files. Design cohesive subpackages according to the [shared directory standards](../directory-structure.md).

Applies to the actual target JDK; evaluate Java 25 for new projects. Inspect pom.xml, Gradle toolchains, framework BOMs, deployment images first.

## J01 Types, interfaces, formatting

- Use existing IDEA/Checkstyle/other formatting; four spaces, target 100 columns, maximum 120, at most 360 source lines
- Group normal/static imports; use simple imported names except for local qualification to resolve collisions
- Follow Java naming conventions, lowercase packages, meaningful constants/enum values
- Use generics; avoid raw types and unchecked casts that conceal type errors
- Records suit value carriers but may reference mutable objects; define defensive copying at construction/access boundaries
- Keep equals/hashCode consistent and comparators contractual; do not mutate hash keys while stored
- Define public nullability; Optional mainly represents absent return values rather than mechanically spreading to entity fields/parameters
- Specify BigDecimal precision, scale, rounding; use java.time for instants, zones, durations
- Follow personal comment/Javadoc conventions for classes, methods, fields; constructors do not have return values

## J02 Errors and resources

- Add business-stage context and preserve causes; translate errors at boundaries without repeatedly logging one stack
- Do not catch Throwable to hide serious JVM failures; broad catches require explicit task-isolation/top-level boundaries
- Propagate interruption or restore its flag and terminate work according to contract rather than swallowing it
- Use try-with-resources for files, streams, connections; pooled connection close follows pool contracts
- Avoid exceptions for ordinary frequent branches; verify actual hotspot improvements
- Validate or use value types for money, identity, permissions, device addresses rather than arbitrary strings everywhere

## J03 Concurrency and Java 25

- Evaluate virtual threads for blocking I/O; design CPU work/event loops according to actual execution models
- Do not pool virtual threads; bound downstream concurrency with semaphores, connections, rate limits, in-flight tables
- JDK 24 JEP 491 removed the main synchronized-related virtual-thread pinning issue; do not mechanically replace synchronized with ReentrantLock
- Analyze remaining pinning such as native calls using actual-runtime diagnostics rather than lock-type guesses
- Java 25 StructuredTaskScope remains preview; use only where approved and fully enabled by the toolchain
- Specify CompletableFuture executors, composition, failures, cancellation, timeouts; cancelling futures does not guarantee I/O cancellation
- Keep blocking work out of common ForkJoinPool computation paths; avoid unintentionally occupying framework I/O threads in callbacks
- ConcurrentHashMap is not a cross-key transaction; keep compute callbacks short and free of external I/O
- Explicitly propagate/restore ThreadLocal, MDC, transaction, security contexts across async boundaries
- Volatile provides specified visibility/ordering rather than compound atomicity

## J04 Frameworks and dependencies

- Follow actual Spring, Quarkus, Jakarta dependencies; do not combine annotations into a supposedly generic solution
- Prefer constructor injection and inspect responsibility for cycles; validate configuration ranges/defaults
- Check Spring proxies, self-invocation, rollback rules, asynchronous boundaries; do not wait for slow external services in transactions
- Inspect JPA/MyBatis N+1, lazy loading, pagination, session lifecycles; bound batch counts/bytes
- Use BOM-approved JSON versions and disable unnecessary arbitrary-type/untrusted polymorphic construction
- Follow Netty ownership transfers/handler auto-release rather than unconditional finally release

## J05 Verification

```text
./mvnw -pl affected-module -am -DskipTests compile
./gradlew :affected-module:compileJava
```

- Adapt compilation commands to repository/OS; compilation does not prove integration, concurrency, performance
- Add no repository Java unit tests; run applicable existing checks and temporary protocol-vector, real-component, integration verification
- Align compiler/runtime JDK and preview flags; inspect dependency trees/bytecode targets when needed
- Use JFR, async-profiler, JMH where appropriate; microbenchmarks do not replace end-to-end loads
- Locate allocation, GC, locks, blocking, connection waits, N+1 before optimizing

See [sources](../sources.md): JLS, JDK API, JEP 491/505, official framework documentation.
