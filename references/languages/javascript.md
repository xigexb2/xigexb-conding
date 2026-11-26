# JavaScript

**English** | [简体中文](../zh-CN/languages/javascript.md) | [Standards index](../translations.md)

Each package/directory directly owns at most 20 same-family source files, including tests, declarations, and first-party generated files. Design cohesive subpackages according to the [shared directory standards](../directory-structure.md).

- Identify browsers, Node.js, module type, bundler, minimum runtime; .js files at most 360 lines
- Use const for stable bindings, let for rebinding; avoid var scope pitfalls
- Avoid implicit-conversion/truthiness confusion among 0, empty strings, null, undefined
- Object/array spread is shallow copying rather than deep immutability
- Evaluate structuredClone, non-mutating array methods and AbortSignal timeout/composition against target runtimes. Check supported types and data semantics before deep copies. Pass cancellation signals to the actual I/O.
- Keep IDs/money within Number precision or explicitly define BigInt JSON/protocol conversion
- Await, return, or supervise promises rather than unhandled fire-and-forget
- Promise.all does not cancel sibling requests; define failure/cancellation/partial-success semantics
- Use actual I/O cancellation such as AbortSignal; ignoring results does not abort requests
- Prevent stale search/pagination/router responses overwriting current state using cancellation/generations
- Measure main-thread interaction latency; split long tasks and assess workers, scheduler APIs or compatible fallbacks for conversions, compression and parsing; see [web performance](../web/performance.md)
- Clean listeners, timers, observers, connections, subscriptions at lifecycle end
- Do not feed user input to eval, Function, dangerous HTML or shell; apply context-appropriate sanitization and CSP/Trusted Types where supported, as specified in [web security](../web/security.md)
- Bound Node request bodies, concurrency, timeouts, output and respect streaming backpressure
- Preserve the chosen package manager/lockfile rather than mixing npm/pnpm/yarn
- Imports must not implicitly start services/change global configuration; separate configuration assembly from business logic
- Run existing lint, formatting, behavior tests, production builds, real-page verification beyond syntax alone

See [sources](../sources.md): ECMAScript, MDN, Node.js.
