# C++

**English** | [简体中文](../zh-CN/languages/cpp.md) | [Standards index](../translations.md)

Each package/directory directly owns at most 20 same-family source files, including tests, declarations, and first-party generated files. Design cohesive subpackages according to the [shared directory standards](../directory-structure.md).

## CXX01 Standards and modeling

- Specify C++ version, library, ABI, exception/RTTI policy, minimum compiler; each file at most 360 lines
- Organize namespaces/modules by domain, keep headers self-contained, omit using namespace from public headers
- Prefer value semantics/Rule of Zero; define/delete resource-owner copy/move consistently when needed
- Use RAII for memory, handles, locks, mappings, transaction guards; destructors generally must not throw
- Inheritance expresses substitutable polymorphism; deletion through bases requires correct destruction contracts
- Express nullability, borrowing, ownership, errors explicitly; raw pointers must not transfer ownership implicitly

## CXX02 Memory and lifecycles

- Prefer unique_ptr for exclusive ownership and shared_ptr only for genuine sharing, with cycle handling
- Pointers, references, span, string_view can express borrowing without extending backing lifetimes
- Avoid dangling references/views and async lambdas capturing expired objects by reference
- Account for iterator/pointer/view invalidation from container growth, deletion, moves
- Do not manage nontrivial-object lifetimes through memset, byte copying, arbitrary reinterpretation
- Depend only on guaranteed moved-from validity rather than assuming moved containers are empty
- Review alignment/lifetimes for custom allocators, placement new, unions, serialization
- Specify pool/arena thread ownership, invalidation, escaping-object constraints

## CXX03 Errors and types

- Follow consistent exceptions/explicit-results policy; consider std::expected only with supported toolchains
- Provide basic/strong exception guarantees, prevent double exceptions during unwinding, make noexcept truthful
- Use enum class, explicit conversion, range checks; avoid narrowing and signed/unsigned mistakes
- Express actual template/concept constraints without excessive hard-to-diagnose metaprogramming
- Do not trade verifiable lifetimes for a few copies; measure before complex expression templates

## CXX04 Concurrency

- Assign thread/task owners; prefer automatically joining wrappers, with cooperative stop-token handling
- Use scoped locks and defined ordering or suitable deadlock-avoiding multi-lock acquisition
- Wait on condition-variable predicates and handle spurious wakeups; notification does not replace protected state
- Prove atomic memory orders from publication relationships; working on x86 alone does not justify relaxed ordering
- Lock-free is neither wait-free nor automatically low latency; explain reclamation, ABA, starvation, platform progress
- Thread-safe shared_ptr control blocks do not make pointee access safe

## CXX05 Verification

- Reuse clang-format, clang-tidy, compilation databases without reformatting unrelated code
- Specify CMake presets, configurations, toolchains; run ASan/UBSan and separate TSan where supported
- Test behavior/cleanup, fuzz parsers, compare complex algorithms with naive references
- Avoid dead-code elimination, incorrect timing, Debug benchmarks; record allocation, caches, contention
- C++ Core Guidelines are engineering guidance rather than the ISO language standard

See [sources](../sources.md): ISO C++, C++ Core Guidelines, SEI CERT C++, compiler documentation.
