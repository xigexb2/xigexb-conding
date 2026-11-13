# C

**English** | [简体中文](../zh-CN/languages/c.md) | [Standards index](../translations.md)

Each package/directory directly owns at most 20 same-family source files, including tests, declarations, and first-party generated files. Design cohesive subpackages according to the [shared directory standards](../directory-structure.md).

## C01 Standards, ABI, interfaces

- Identify C version, compiler, target ABI, freestanding/hosted environment, extensions
- Limit .c and maintained headers to 360 lines; headers are self-contained with guards/stable public types
- Specify pointer lengths, capacity, nullability, ownership, failed output state
- Use appropriate fixed-width/size types and matching formats; account for size_t/pointer width
- Do not use padding, bitfield layout, native byte order as persistence/network formats
- Prevent repeated macro evaluation/precedence bugs; prefer functions/static inline when sufficient
- Public headers must not expose unrelated platform details/internal mutable globals

## C02 Memory and undefined behavior

- Check multiplication/addition overflow, maximum sizes, allocation failures; protect realloc with temporary pointers
- Define each resource owner/deallocator; callers must not free after ownership transfer
- Initialize before use and check bounds, alignment, object lifetime, effective-type/aliasing rules
- Prevent use-after-free, double free, stack-address returns; nulling one pointer does not repair dangling aliases
- Distinguish string capacity, length, terminators and handle truncation; strncpy is not universally safe
- Use memcpy only for nonoverlap and memmove for possible overlap, with validated lengths
- Check shift width/signedness and signed overflow rather than relying on UB
- Centralized goto cleanup is valid for multi-resource initialization; release acquired resources in reverse order

## C03 Concurrency and low-level access

- Volatile supplies its specified access semantics rather than synchronization, atomicity, CPU/DMA barriers
- Establish happens-before with C atomics/locks; interrupt sharing also follows hardware/RTOS contracts
- ISRs must not block, use ordinary locks, allocate unbounded memory, or call unsuitable logging; use platform ISR-safe APIs
- Handle alignment, cache lines, false sharing, DMA coherence when required by hardware or measured bottlenecks
- Use platform MMIO interfaces rather than pointer casts that omit barriers/access-width requirements
- Signal handlers use async-signal-safe operations; thread safety is not signal safety

## C04 Build and verification

- Enable compatible GCC/Clang warnings such as -Wall -Wextra; fix progressively rather than suppress blindly
- Use ASan/UBSan where supported and separate TSan configurations; avoid incompatible tool combinations
- Apply static analysis, fuzzing, protocol vectors, failure injection by risk
- Verify Debug/Release, optimization levels, architectures, ABIs; optimization-only failures may expose UB
- Inspect linker scripts, section layouts, stack/heap budgets, startup, map files, reproducibility
- Compilation/simulation do not replace peripheral, timing, power, RF, board validation

See [sources](../sources.md): WG14, POSIX, SEI CERT C, compiler/platform documentation.
