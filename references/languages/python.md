# Python

**English** | [简体中文](../zh-CN/languages/python.md) | [Standards index](../translations.md)

Each package/directory directly owns at most 20 same-family source files, including tests, declarations, and first-party generated files. Design cohesive subpackages according to the [shared directory standards](../directory-structure.md).

## PY01 Readability and types

- Follow pyproject.toml, supported versions, dependency locks; at most 380 lines per file
- Follow PEP 8/257 with four spaces by default; Chinese docstrings describe contracts/failures
- Annotate public APIs/complex data flows; type checking is not runtime input validation
- Use dataclass, TypedDict, Protocol for actual models without imposing validation frameworks
- Avoid mutable defaults, implicit globals, import-time networking, intricate nested comprehensions
- Separate text/bytes and specify encodings, time zones, Decimal precision, serialization boundaries

## PY02 Errors and resources

- Catch specific exceptions and preserve causal chains with raise ... from ...
- Do not swallow failures with bare except or except Exception: pass; preserve exit/cancellation signals
- Use context managers for files, connections, locks, temporary resources; roll back/clean up on failures
- Use subprocess argument lists and check status; avoid shell by default and user-input concatenation
- Use pathlib and resolved-boundary checks against symlinks, traversal, TOCTOU
- Do not deserialize untrusted pickle or parse business input with eval/exec

## PY03 Async and concurrency

- Asyncio provides cooperative I/O; keep blocking libraries/long CPU work off its loop
- Use TaskGroup and similar features according to minimum Python version and actual child-task/exception-group contracts
- Supervise every task, await cancellation cleanup, observe failures
- Catch cancellation for cleanup and propagate by contract; explain post-cancellation ownership when shielding
- Bound pools/concurrent requests; cancelling await does not necessarily stop running thread work
- Do not rely on the GIL for compound business invariants; assess interpreters/free-threaded builds by version
- Define multiprocessing serialization, start methods, shared memory, child exits beyond fork-only verification

## PY04 Performance and dependencies

- Stream large files and use bounded batches rather than full reads/large temporary lists
- Confirm hotspots/capacity before caching parsing; generators must manage held file resources
- Prefer standard/existing libraries over large runtimes for small features
- Isolate virtual environments and direct/development dependencies using chosen lock/install tools
- Profile with cProfile, sampling, suitable benchmarks; consider vectorization, processes, native extensions when needed

## PY05 Verification

```text
python -m compileall -q src
python -m unittest discover -s tests
```

- Adapt directories/frameworks and reuse configured pytest, Ruff, mypy/pyright
- Test input boundaries, errors, cleanup, cancellation; avoid mirror tests for pure text changes
- Isolate temporary paths, avoid real user configuration/credentials, production dependencies
- Verify syntax/dependency matrices against minimum supported versions

See [sources](../sources.md): Python documentation, PEP 8/257, typing, asyncio.
