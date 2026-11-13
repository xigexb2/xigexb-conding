# Algorithms and data structures

**English** | [简体中文](../zh-CN/engineering/algorithms.md) | [Standards index](../translations.md)

## AL01 Define the problem first

- Specify input size/distribution, permitted error, ordering/stability, online/offline operation, update/query ratio
- Define behavior for empty input, duplicates, extrema, invalid and untrusted input
- State time complexity, extra space, worst cases, and amortization assumptions rather than average complexity alone
- Estimate allocation, cache hits, serialization, and I/O; asymptotic complexity is not the entire performance model

## AL02 Choose structures

| Requirement | Evaluate first | Considerations |
| --- | --- | --- |
| Dense sequential access | Arrays, slices, contiguous vectors | Growth, moves, iterator invalidation |
| Exact-key lookup | Hash tables | Collision degradation, hash attacks, capacity, key stability |
| Range/ordered queries | Balanced trees, sorted arrays, database indexes | Update frequency, comparator consistency |
| Top-K, timers | Heaps, timing wheels | Lazy-deletion buildup, granularity, clock changes |
| FIFO and backpressure | Bounded queues, ring buffers | Full/empty states, producer/consumer model |
| Deduplication/set operations | Sets, bitmaps | Sparse IDs, memory size |
| Probabilistic prefilter | Bloom filters and similar | False positives, deletion support; cannot justify rejecting valid business operations |
| Prefix matching | Tries, sorted search | Unicode, normalization, memory cost |
| Dependency scheduling | DAGs, topological sorting | Cycle detection, partial failure, retries |

Prefer mature standard libraries. Custom concurrent containers, memory pools, skip lists, and lock-free queues require a demonstrated gap and measurements.

## AL03 Numbers and boundaries

- Check overflow before addition, multiplication, indexing, capacity calculation; comparison after overflow is ineffective
- Avoid subtraction-based comparators that can overflow; verify strict weak ordering or the language's comparison contract
- Represent money using specified decimal precision or integer minor units; define rounding and range
- Specify bit width, signedness, endianness for binary protocols; native struct layout is not a wire format
- Model instants, durations, time zones, monotonic clocks separately
- Handle NaN, infinity, negative zero, tolerance; floating-point equality is not a settlement rule
- Distinguish bytes, code points, user-perceived characters; never split UTF-8 sequences

## AL04 Proof and verification

- Explain invariants, termination, bounds checks for loops and state transitions
- Compare known cases, boundaries, generated inputs, properties, and small naive reference implementations
- Useful properties include idempotency, monotonicity, conservation, sorted postconditions, known codec vectors
- Codec round trips do not prove standards conformance; both ends can share one mistake
- Check adversarial worst-case complexity, recursion depth, exponential backtracking, memory growth
- Follow the Java convention of no new repository unit tests; run necessary differential algorithm checks in temporary directories and report results

## AL05 Engineering tradeoffs

State input ranges and maintenance costs when choosing recursion/iteration, exact/approximate, precomputed/on-demand, or space/time tradeoffs. Prefer an explainable, verifiable solution within budget without sacrificing reliability for theoretical optimality.
