# Concurrency, resource lifecycles, and performance

**English** | [简体中文](../zh-CN/engineering/concurrency-performance.md) | [Standards index](../translations.md)

## CP01 Concurrency correctness

- Specify shared-data owners, read/write paths, synchronization; prefer immutable data, message passing, local sharding
- A concurrent container does not make compound business operations atomic; inspect check-then-act, read-modify-write, cross-key invariants
- Explain state machines, memory visibility, ABA risks before atomics; lock-free code needs progress and reclamation reasoning
- Maintain consistent lock order and short critical sections; do not invoke external callbacks, wait for futures, or perform network/disk I/O under shared-state locks
- If I/O must be serialized, define a dedicated serial channel and owner rather than incidentally using a global state lock
- Thread, coroutine, task switches do not automatically propagate MDC, transactions, authorization context, thread-local resources
- Passing race detection does not prove freedom from deadlocks, logical races, starvation, linearizability errors

## CP02 Bounded resources

| Resource | Required bounds |
| --- | --- |
| Queue | Capacity, full behavior, wait deadline, shutdown, backlog handling |
| Cache | Entries/weight, expiry, eviction, stampede protection, origin concurrency |
| In-flight requests | Global count, tenant quotas, deadlines, cancellation, cleanup |
| Connections/threads | Limits, waiting, isolation, idle cleanup, exit behavior |
| Batches | Count, bytes, wait time, partial failure, splitting |
| Retries | Conditions, attempts/total deadline, backoff, jitter, idempotency |
| Static read-only tables | Maximum expected size, release-time validation, immutability |

Virtual threads and goroutines are finite resources. Cheap tasks must not hide exhausted database connections, downstream limits, or heap growth.

## CP03 Deadlines and cancellation

- Establish an overall incoming deadline; downstream budgets fit the remaining time rather than resetting a full timeout at every layer
- Propagate cancellation to actual I/O/tasks; if cancellation is impossible, record continuing work and clean up observer-side resources
- Resolve timeout/completion/cancellation races to one final outcome; repeated completion has no side effects
- Clean subscriptions, timers, request tables, buffers on every terminal path
- Avoid stacked retries; promptly reject overload instead of amplifying requests
- Define shutdown order: stop admission, stop dispatch, wait within bounds, cancel remaining work, release resources

## CP04 Performance design

- Identify whether bottlenecks are CPU, I/O, lock contention, memory, GC, serialization, network round trips, downstream capacity
- Improve algorithms/access patterns first: batch reads, reduce N+1, coalesce requests, improve locality, avoid repeated parsing
- Reduce copying with immutable data/exclusive ownership; reference safety across asynchronous boundaries takes precedence over zero-copy slogans
- Pool objects only when allocation/resource costs are demonstrated and lifecycles clear; assess contention, cleanup, retained memory
- Avoid hot-path reflection scans, unbounded collection creation, repeated serialization, unnecessary full sorting
- Define cache authority, invalidation, consistency windows; cache failures must not bypass authorization
- Shard with hot spots, tenant fairness, ordering in mind; concurrency must fit the weakest downstream budget

## CP05 Measurement

- Record baseline, hardware, OS, runtime, compiler flags, data size, request distribution, dependency state
- Separate microbenchmarks from end-to-end loads; warm up, repeat samples, account for dead-code elimination and constant folding
- Report throughput, p50/p95/p99, errors, queuing, CPU, peak memory, allocation rates
- Check coordinated omission, client saturation, unrealistic hit rates; explain open-loop/closed-loop choices
- Assess steady loads, bursts, cold starts, long runs, recovery from degradation
- Use Little's law to guide budgets where applicable; averages cannot replace tail-latency/burst validation
- Check correctness, leaks, fairness alongside performance rather than comparing one elapsed-time sample

## CP06 Observability

- Logs explain events, metrics describe trends, traces locate cross-service paths
- Avoid unbounded device/user IDs and full URLs as metric labels
- Capture/restore context to prevent thread-reuse contamination; sampling must preserve required security/financial audits
- Rate-limit or aggregate repeated failures; avoid full INFO payloads for every device message
- Alert on user impact and resource saturation with actionable responses
