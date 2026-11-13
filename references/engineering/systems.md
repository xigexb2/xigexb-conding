# Operating systems, memory, and low-level I/O

**English** | [简体中文](../zh-CN/engineering/systems.md) | [Standards index](../translations.md)

## SYS01 Execution and memory models

- Specify ISA, privilege levels, address spaces, ABI, cache coherence, platform memory model
- Distinguish virtual, physical, bus/DMA addresses rather than assuming numeric equivalence
- Implement page tables, mappings, permissions, TLB invalidation, cross-core synchronization by architecture manuals; record layouts/alignment
- Define allocation context, lifecycle, failure, reclamation; use mechanisms suited to boot, task, interrupt phases
- Reference counting, RCU, epochs, hazard pointers have distinct reclamation conditions; atomic reads/writes alone do not justify freeing objects
- Validate lengths, permissions, address validity, copy failures across kernel/driver/userspace boundaries
- User memory can change after validation; prevent TOCTOU races and copy into controlled snapshots when needed

## SYS02 SMP, interrupts, scheduling

- Interrupts, exceptions, tasks, softirqs, NMIs permit different APIs; do not treat all contexts as threads
- Distinguish sleeping/spin locks and interrupt/preemption/cross-core relations; do not block where sleeping is forbidden
- Document lock ordering/nesting; account for migration/preemption in per-CPU state rather than assuming a fixed CPU
- Distinguish CPU/compiler/MMIO barriers and DMA synchronization
- Handle lost wakeups, wait queues, priority inversion, starvation, exit races in scheduling/wakeup paths
- Emergency records/panic paths must not depend on damaged heaps, ordinary scheduling, globally contended locks
- Single-core tests do not prove SMP correctness; bind multicore evidence to actual symbols/layouts/execution

## SYS03 Network I/O

- Handle partial reads/writes, EINTR, EAGAIN, half-close, resets in POSIX sockets
- epoll level/edge triggering, kqueue, io_uring have different completion/retry contracts
- Edge-triggered I/O typically drains until no progress is possible; manage write interest according to pending output
- Verify io_uring completions, cancellation, fixed resources, buffer lifetimes for kernel/library versions
- File descriptors can be reused; correlate requests through generations/owners rather than old descriptor numbers alone
- Bound receive/send buffers with backpressure so slow clients cannot exhaust all connections
- In zero-copy paths specify memory ownership until completion and reuse timing; submission is not completion

## SYS04 Files and durability

- Distinguish userspace buffering, kernel caches, device submission, persistence guarantees
- Design rename, fsync, directory synchronization, crash consistency according to filesystem/platform semantics
- Handle short writes, full disks, permissions, path races, locks, handle leaks
- Define mmap lifetimes, truncation, concurrent mutation; mappings are not permanently valid

## SYS05 Validation and diagnosis

- Associate build identifiers, ELF/map files, symbol addresses, boot arguments, actual running images
- Build evidence with debuggers, core dumps, sanitizers, traces, perf, lock detection
- Report simulation, QEMU, hardware-in-the-loop, physical-device results separately; none implicitly covers all timing/peripherals
- Inject allocation failure, interrupt races, reboot, I/O errors, cross-core contention, resource exhaustion
- Reliably associate crash records with thread/CPU, exception, PC/SP, memory ranges; report unknown root causes honestly
