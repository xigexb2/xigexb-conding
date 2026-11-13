# JavaScript

**English** | [简体中文](../zh-CN/languages/javascript.md) | [Standards index](../translations.md)

Each package/directory directly owns at most 20 same-family source files, including tests, declarations, and first-party generated files. Design cohesive subpackages according to the [shared directory standards](../directory-structure.md).

- Identify browsers, Node.js, module type, bundler, minimum runtime; .js files at most 360 lines
- Use const for stable bindings, let for rebinding; avoid var scope pitfalls
- Avoid implicit-conversion/truthiness confusion among 0, empty strings, null, undefined
- Object/array spread is shallow copying rather than deep immutability
- Keep IDs/money within Number precision or explicitly define BigInt JSON/protocol conversion
- Await, return, or supervise promises rather than unhandled fire-and-forget
- Promise.all does not cancel sibling requests; define failure/cancellation/partial-success semantics
- Use actual I/O cancellation such as AbortSignal; ignoring results does not abort requests
- Prevent stale search/pagination/router responses overwriting current state using cancellation/generations
- Avoid long CPU work on event loops; assess workers/chunking for conversions, compression, parsing
- Clean listeners, timers, observers, connections, subscriptions at lifecycle end
- Do not feed user input to eval, Function, dangerous HTML, shell
- Bound Node request bodies, concurrency, timeouts, output and respect streaming backpressure
- Preserve the chosen package manager/lockfile rather than mixing npm/pnpm/yarn
- Imports must not implicitly start services/change global configuration; separate configuration assembly from business logic
- Run existing lint, formatting, behavior tests, production builds, real-page verification beyond syntax alone

See [sources](../sources.md): ECMAScript, MDN, Node.js.
