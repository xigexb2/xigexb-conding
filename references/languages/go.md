# Go

**English** | [简体中文](../zh-CN/languages/go.md) | [Standards index](../translations.md)

Each package/directory directly owns at most 20 same-family source files, including tests, declarations, and first-party generated files. Design cohesive subpackages according to the [shared directory standards](../directory-structure.md).

## G01 Idioms and package design

- Follow go.mod, toolchain, actual CI rather than the author's workstation version
- Use gofmt and existing goimports where needed; standard tab indentation is allowed
- Use short lowercase cohesive package names; avoid all-purpose util/common packages and cycles
- Each directory has at most 20 production/test .go files together; each file at most 360 lines
- Define small capability interfaces at consumers; returning concrete types is common but not a universal API mandate
- Prefer meaningful zero values; types needing initialization expose constructors/precondition checks
- Do not copy objects containing mutexes, atomic state, non-copyable resources; choose value/pointer receivers deliberately
- Exported comments start with the identifier and continue in Chinese; do not apply Java Javadoc templates

## G02 Error handling

- Handle meaningful errors rather than silently dropping them; define policies for cleanup errors that cannot affect results
- Wrap context with fmt.Errorf and %w; inspect causes with errors.Is/errors.As
- Do not classify business errors by string matching or log-and-return repeatedly through layers
- Reserve panic for broken invariants/unrecoverable initialization rather than request input
- Recover only at explicit isolation boundaries; do not disguise damaged state as success
- Use named returns only when clearer; avoid naked returns in long functions

## G03 Goroutines and lifecycles

- Every goroutine has a starter, exit condition, cancellation path, necessary waiter
- Context is usually the first parameter; never pass nil or use it as a business-field container/global state
- Call cancel on all applicable paths; downstream budgets fit parent remaining time
- The coordinator of completed sending owns channel closure; arbitrary receivers must not close channels with multiple senders
- Define exits for every blocking send, receive, wait, external call
- Bound workers by CPU/downstream resources; do not start unlimited goroutines waiting for connections deeper in the stack
- Reuse approved errgroup/semaphore dependencies and specify concurrency/first-error behavior
- Protect compound invariants with mutexes instead of splitting them into inconsistent atomics for a lock-free label

## G04 Memory and I/O

- Slice/map copying is shallow; specify backing-array/nested-object ownership across async boundaries
- Do not retain pooled slices or bytes.Buffer.Bytes() after return; clear sensitive/large references before returning
- sync.Pool is a disposable temporary-object cache rather than lifecycle/fixed-capacity management
- Avoid retaining large arrays through small slices; bound preallocation using trusted sizes
- Reuse HTTP transports with limits/timeouts; close response bodies correctly and limit reads
- Defer runs at function exit; use helper functions/explicit close when resources must be released inside long loops
- Require measurements for preallocation, escape optimizations, unsafe; avoid risky zero-copy conversions in ordinary business code

## G05 Tests and verification

```text
gofmt -l .
go vet ./...
go test ./...
go test -race ./...
```

- Behavior changes require new/updated table-driven unit tests for success, boundaries, errors, cancellation, duplicates, cleanup
- Run race checks on critical concurrency paths; disclose unsupported platforms and revalidate where supported
- Prefer controlled clocks/synchronization events to fragile fixed sleeps
- Consider parser fuzzing, go test -bench/allocation metrics, pprof, trace, benchstat
- Go mod tidy mutates module files; inspect its diff instead of calling it read-only
- Verify supported platforms/build tags beyond the local machine

See [sources](../sources.md): Go Specification, Memory Model, Effective Go, official tools.
