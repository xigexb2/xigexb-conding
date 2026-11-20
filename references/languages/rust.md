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

## R06 Organization, imports, and formatting

- Follow the project's Rust edition, toolchain, rustfmt configuration and native conventions; retain the 360-line source limit and 20 same-family files per directory including tests and generated first-party files
- Keep crates and modules cohesive by actual capability; non-leaf modules primarily declare/re-export, with limited integration code when needed. Name leaf modules for their primary item where meaningful
- Prefer explicit imports; glob imports are acceptable for inline test modules, enum variants in narrow scopes, deliberate non-leaf re-exports, approved preludes or interop where their tradeoffs are clear
- Group imports from one module per `use` where practical; import traits locally when used only locally. Prefer module-qualified external free-function calls and directly imported type/trait names unless conflicts, generated code, established conventions or clarity justify otherwise
- Use rustfmt and check its settings against the project's stable toolchain/MSRV. Use `#[rustfmt::skip]` only for a concrete readability or generated-code need, not personal formatting preference
- Chromium-only flat-crate layout and `chromium::import!` apply only in the relevant Chromium build context; they do not override this skill's required package/directory limits or Cargo layout

## R07 API design, types, and traits

- Distinguish reusable library contracts from application code: libraries should provide suitable flexibility and stability; applications favor direct solutions over speculative abstraction
- Accept `&str`, `&[T]`, `&Path`, and `&T` when borrowed data suffices rather than unnecessarily requiring `&String`, `&Vec<T>`, `&PathBuf`, or `&Box<T>`; retain concrete types when their semantics are needed
- For reusable APIs, consider iterators or `IntoIterator` when only iteration is required; return iterators when lazy consumption is appropriate. Keep slices or owned collections when callers need indexing, ownership, natural construction, or simpler application code
- Consider `impl Into<T>` for important library ergonomics only after accounting for generic code size, inference and API complexity; avoid applying it mechanically to application functions
- Use a meaningful enum when a boolean argument would obscure intent; prefer named fields for multi-value domain data and newtypes for distinct semantics/invariants, retaining clear local tuples and single-field newtypes
- Implement standard traits when their full semantic contracts apply; derive implementations when equivalent. Add `Copy`, `Clone`, `Default`, `Eq`, `Ord`, and `Hash` only when their meaning, cost, invariants and future compatibility support them
- Use inherent methods for type-specific behavior; introduce traits for actual polymorphism, generic APIs or well-justified extension points. Name extension traits with `Ext` and consider ownership and method collisions
- Select generics or `dyn Trait` based on dispatch, object compatibility, binary size, compilation and extensibility; avoid claiming one is always faster
- Follow idiomatic accessor names such as `foo`, `foo_mut`, `set_foo`, `take_foo`, `replace_foo`, `with_foo`; provide `is_empty` alongside public `len` when applicable. Closure accessors must document lock/reentrancy and panic behavior
- Treat external `#[doc(hidden)]` items as non-public implementation details. Make public `const fn` a deliberate compatibility commitment; use operator overloading only for natural, documented semantics
- Assess `#[non_exhaustive]` for evolving public enums/structs and its effect on downstream construction and matching; stable closed models can remain exhaustive. Use `#[must_use]` when discarding the result is likely an error, accounting for already annotated return types

## R08 Diagnostics, safety, and platform scope

- Use `Option` for expected absence when no further detail is useful, `Result` for actionable recoverable failures, and panic for genuine violated invariants only when the target permits it
- Prefer pattern matching or `let-else` to checking and then unwrapping. If an invariant truly requires a panic, prefer `expect` with a meaningful explanation; do not replace recoverable errors with panics
- Assertion messages explain the violated invariant or misuse and relevant safe context; do not log secrets. Avoid long iterator chains when a named intermediate or loop is clearer
- A poisoned mutex signals a possible broken invariant; do not blindly recover its contents. Recovery requires an explicit, validated invariant-repair policy and the actual mutex implementation's semantics
- Minimize `unsafe`; document each unsafe block's safety argument and every unsafe API's caller obligations in Simplified Chinese using Rust's `SAFETY` / `# Safety` conventions. Explain why safe alternatives are insufficient; support performance justification with measurements
- Do not introduce unstable features unless explicitly permitted by the project and justified for its actual toolchain/target. `catch_unwind` works only for unwinding panics and is not a substitute for error handling, resource invariants, abort behavior, or FFI safety
- Chromium-specific restrictions on async, standard threads, build/import and tests, and Fuchsia-specific synchronization/testing apply only when the actual target project adopts them. Embedded `no_std` and hardware validation continue to follow target-specific requirements

The [Google Rust Style Guide](https://google.github.io/styleguide/rustguide.html) was reviewed at [this fixed source revision](https://github.com/google/styleguide/blob/cceb297e93677c31053e5e75de6b701a9204fc03/rustguide.md). These rules adapt its guidance to the user's conventions; project-specific Google rules are not general Rust language requirements. See [source and license notes](../sources.md).

See [sources](../sources.md): Rust Reference, Rustonomicon, API Guidelines, Cargo.
