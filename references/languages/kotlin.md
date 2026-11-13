# Kotlin

**English** | [简体中文](../zh-CN/languages/kotlin.md) | [Standards index](../translations.md)

Each package/directory directly owns at most 20 same-family source files, including tests, declarations, and first-party generated files. Design cohesive subpackages according to the [shared directory standards](../directory-structure.md).

- Follow Gradle/Kotlin/JDK/Android compatibility matrices; at most 360 lines per file
- Use official naming/project formatting and Chinese KDoc for responsibilities, nullability, suspension
- Prefer immutable values, data classes, sealed types, explicit state over combinations of nullable fields
- Do not conceal input/lifecycle failures with !!; validate Java platform types at boundaries
- Keep scope functions moderate; nested let/run/apply must not obscure receivers/control flow
- Attach coroutines to explicit scopes/Jobs instead of arbitrary GlobalScope
- Suspension does not imply a background thread; use appropriate dispatchers/bounds for blocking I/O/CPU
- Cancellation is cooperative; preserve CancellationException and choose cleanup cancellation scopes deliberately
- Distinguish cold Flow, StateFlow, SharedFlow subscription/replay and bound buffers/caches
- Collect Android state lifecycle-aware; process-death recovery cannot rely on ViewModel memory
- Hoist Compose state to suitable owners/use proper effect APIs; remember is not persistence
- Follow Ktor/Spring server contracts rather than Android lifecycle assumptions
- Verify types, cancellation, recovery, platform builds; reuse ktlint/detekt settings

Combine [mobile](../product/mobile.md), [concurrency](../engineering/concurrency-performance.md), official Kotlin guidance.
