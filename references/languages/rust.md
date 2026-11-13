# Rust

**English** | [简体中文](../zh-CN/languages/rust.md) | [Standards index](../translations.md)

Each package/directory directly owns at most 20 same-family source files, including tests, declarations, and first-party generated files. Design cohesive subpackages according to the [shared directory standards](../directory-structure.md).

## R01 Types and ownership

- Inspect edition, MSRV, features, targets, lockfile policy; each file at most 360 lines
- Expose minimal stable public types/traits; use enums/newtypes for states rather than invalid combinations
- Prefer borrowing, immutability, explicit moves; do not hide lifecycle design behind pervasive clone
- Arc shares ownership; interior mutability still needs synchronization and reference counting is not thread-safety proof
- Specify allocation, ordering, ownership, panic contracts for public collections/callbacks
- Choose generics/trait objects by specialization, binary size, extension, hot-path cost
- Do not force all loops into iterator chains; favor clear invariants and optimizable code

## R02 Errors and panic

- Propagate input, network, configuration, persistence failures with Result/Option and ?
- Do not hide recoverable failures with unwrap/expect in production paths; justify proven invariants and impact
- Libraries expose matchable errors and applications add context; do not impose new error libraries purely for style
- Check unwind/abort policies; destructors/FFI boundaries must not assume unknown propagation behavior
- Validate serialization, deserialization, integer conversion ranges, lengths, allocation bounds, untrusted data

## R03 Unsafe and FFI

- Confine unsafe to small modules with safe wrappers and explained preconditions/invariants
- Use Chinese SAFETY explanations for alignment, initialization, validity, aliasing, lifetime, concurrency in critical unsafe blocks
- Implement Send/Sync manually only with proven cross-thread/shared-access contracts
- Use appropriate repr layouts and verify widths, ABI, calling convention, linkage targets
- Pair C strings, callbacks, allocators, deallocators; identify the freeing side and cross-thread permissions
- Review raw pointers, MaybeUninit, set_len, Pin, self-reference, atomics specifically
- Handle panic boundaries by actual ABI/configuration; prevent undefined cross-language unwinding

## R04 Async and concurrency

- Keep the project's runtime; Tokio is not required for every Rust project
- Avoid long blocking on runtime workers; bound blocking pools and explain already-started non-cancellable work
- Review lock types/access patterns across await; avoid unnecessary shared-state guards
- Specify cancellation safety, partial writes, cleanup when futures are dropped
- Own/supervise tasks with JoinHandles or explicit supervisors; inspect panics, errors, shutdown results
- Bound channels/queues and define drain, discard, persistence policies on closure
- Review select! cancellation, starvation, duplicate execution beyond happy paths

## R05 Verification

```text
cargo fmt --check
cargo check --locked
cargo clippy --all-targets -- -D warnings
cargo test --locked
```

- Adapt warning policy to the project rather than introducing global deny into legacy code
- Build feature matrices for mutually exclusive features instead of blindly using --all-features
- Use Miri, sanitizers, fuzzing, properties for unsafe/FFI/parsers according to risk and tool support
- Separate host tests, target linking, simulation, board checks for embedded no_std
- Measure release builds and record target CPU, flags, allocations

See [sources](../sources.md): Rust Reference, Rustonomicon, API Guidelines, Cargo.
