# xigexb Coding

**English** | [简体中文](README.zh-CN.md)

An engineering standards skill for coding agents, covering architecture, implementation, UI/UX, performance, security, and delivery across software and hardware projects.

Built around clear responsibilities, explicit contracts, bounded resources, and verifiable results. Use it to design, implement, refactor, and review enterprise applications, consumer products, web and mobile apps, IoT platforms, embedded systems, and low-level infrastructure.

## Installation

Clone the repository into a skill directory supported by your coding agent. For agents that discover project skills under `.agents/skills`, run this from your project root:

```bash
git clone https://github.com/xigexb2/xigexb-conding.git .agents/skills/xigexb-coding
```

Keep `SKILL.md`, `references/`, `scripts/`, and `agents/` together. Use the agent's supported discovery directory for global installation.

## Usage

Invoke the skill with a task and the relevant language, framework, or platform:

```text
Use $xigexb-coding to design a Go gateway with bounded concurrency,
cancellation, backpressure, and graceful shutdown.
```

```text
Use $xigexb-coding to build a Vue device-management page with TDesign,
including bulk actions, permission states, and weak-network recovery.
```

```text
Use $xigexb-coding to review a Java + Netty service for buffer ownership,
thread safety, API contracts, and failure recovery.
```

The skill loads the core conventions first, then selects references for the task's languages and engineering domains.

## Core standards

These are the skill's default conventions. Current task and repository instructions determine their application; language, protocol, and platform contracts remain authoritative.

| Area | Convention |
| --- | --- |
| Text format | UTF-8 without BOM, LF line endings, one final newline, no trailing whitespace |
| Code comments | Professional Simplified Chinese; native documentation syntax and required tool markers |
| Source file size | At most 360 lines for the primary language extensions and 380 for other maintained source files, including comments and blank lines; see [exact limits](references/profile.md) |
| Package size | **At most 20 directly owned source files of the same family per package or directory, across all languages** |
| File counting | Count production files, tests, declarations, headers, platform variants, and first-party generated sources together; count child directories separately |
| Module boundaries | Split by domain, capability, protocol, or lifecycle before reaching the limit; maintain cohesive responsibilities and explicit dependency direction |
| Design | Single responsibility, high cohesion, low coupling, stable contracts, and models that reflect business and physical processes |
| Design patterns | Select patterns for concrete variation points and lifecycle needs; account for complexity and maintenance cost |
| Concurrency | Explicit ownership, bounded queues and execution, cancellation, timeouts, backpressure, and orderly shutdown |
| Performance | Define budgets, measure realistic workloads, identify bottlenecks, and verify improvements |
| Java | Target 100 columns, maximum 120; no new repository unit tests, with compilation and appropriate verification still required |
| Go | Use `gofmt`; add or update unit tests for behavior and concurrency changes |
| SQL | Parameterized queries, explicit transaction boundaries, query-plan review, and no leftover SQL files; formal migrations require task authorization |
| Git | Focused changes, meaningful commits, protected existing work, and explicit authorization for commits and pushes |

Mixed extensions belonging to the same source family are counted together, including JavaScript/TypeScript and C/C++ sources and headers. See [directory and package standards](references/directory-structure.md).

## Engineering coverage

| Domain | Standards |
| --- | --- |
| [Architecture](references/engineering/architecture.md) | Domain boundaries, interfaces and implementations, modularity, dependency direction, state machines, and architectural decisions |
| [Design patterns](references/engineering/design-patterns.md) | Creational, structural, behavioral, and architectural patterns; selection criteria and language-specific application |
| [Backend](references/engineering/backend.md) | API contracts, validation, authentication, authorization, tenancy, idempotency, transactions, and recovery |
| [Algorithms](references/engineering/algorithms.md) | Complexity, data structures, numerical boundaries, correctness, and workload-based selection |
| [Concurrency and performance](references/engineering/concurrency-performance.md) | Memory models, synchronization, bounded resources, profiling, benchmarks, latency, throughput, and capacity |
| [Databases](references/engineering/database.md) | Data modeling, constraints, indexes, isolation, locking, migrations, and cache consistency |
| [Protocols and distributed systems](references/engineering/protocols-distributed.md) | Message semantics, retries, ordering, consistency, ownership, failover, and execution status |
| [Security](references/engineering/security.md) | Threat modeling, access control, tenant isolation, secrets, cryptography, supply chains, device security, and AI/agent tool boundaries |
| [Systems](references/engineering/systems.md) | Memory safety, ABI/FFI, IPC, virtual memory, SMP, network I/O, and resource lifecycles |
| [Frameworks](references/engineering/frameworks.md) | Version-aware use of frontend, backend, persistence, messaging, and networking frameworks |
| [Git](references/engineering/git.md) and [delivery](references/engineering/delivery.md) | Branches, commits, reviews, CI/CD, versioning, release evidence, rollback, and operations |

## Languages

Each topic applies the shared standards alongside the language's own tooling, runtime, memory model, and ecosystem conventions.

| Category | References |
| --- | --- |
| Backend and general purpose | [Java](references/languages/java.md), [Go](references/languages/go.md), [Python](references/languages/python.md) |
| Systems and native | [Rust](references/languages/rust.md), [C](references/languages/c.md), [C++](references/languages/cpp.md) |
| Web | [JavaScript](references/languages/javascript.md), [TypeScript](references/languages/typescript.md), [Vue](references/languages/vue.md), [HTML/CSS](references/languages/html-css.md) |
| Mobile | [Kotlin](references/languages/kotlin.md), [Swift](references/languages/swift.md) |
| Data | [SQL](references/languages/sql.md) |

## UI, UX, and application design

- [UI/UX standards](references/product/ui-ux.md): information architecture, page hierarchy, color semantics, typography, spacing, navigation, forms, tables, feedback, accessibility, and responsive behavior
- [Design systems](references/product/design-systems.md): Ant Design, TDesign, Arco/Semi, JetBrains Int UI, Google Material Design, Apple HIG, IBM Carbon, Oracle Redwood, and other public design resources
- [Google Stitch design and implementation workflow](references/product/stitch-workflow.md) covers screen briefs, token extraction, multi-page prototyping and frontend implementation.
- [Mobile and cross-platform standards](references/product/mobile.md): iOS, Android, native apps, hybrid apps, mini-programs, platform interaction, permissions, offline behavior, and lifecycle management

Choose a coherent design system for the product. Adapt information density, interaction, and recovery flows to enterprise or consumer tasks and the target platform.

## Modern web standards

The bilingual standards cover browser support, HTML/CSS, forms, accessibility, Web performance, privacy, PWA, emerging APIs and browser extensions. [Web foundations](references/web/foundations.md) and the [pinned topic catalog](references/web/catalog.md) route to the relevant guidance.

## Embedded systems and hardware

- [Embedded development](references/hardware/embedded.md): MCU/RTOS architecture, interrupts, DMA, memory budgets, timing, watchdogs, boot, OTA, and board validation
- [Communication](references/hardware/communications.md): framing, endianness, CRC, retransmission, bus timing, industrial protocols, and interoperability
- [Electronics and PCB](references/hardware/electronics-pcb.md): component selection, power, protection, grounding, signal integrity, EMC, DFM/DFT, and bring-up
- [Digital chip design](references/hardware/chip-design.md): RTL/FPGA, reset, CDC/RDC, constraints, timing analysis, verification, and sign-off
- [Analog and mixed-signal ICs](references/hardware/analog-ic.md): bias, stability, converters, RF considerations, PVT, mismatch, parasitics, reliability, and measurement

## Working process

1. Establish requirements, invariants, interfaces, failure semantics, and acceptance criteria.
2. Inspect the repository, toolchain, dependencies, and existing changes.
3. Design responsibilities, package boundaries, state transitions, security controls, and resource budgets.
4. Implement with explicit error handling, boundary checks, ownership, and cleanup.
5. Verify correctness, compatibility, performance, and platform behavior with evidence appropriate to the change.

See [verification standards](references/verification.md) for software, UI, distributed-system, and hardware validation.

## Repository checks

With Python 3.11 or later, check formatting, source size, directory limits, and local documentation links:

```bash
python scripts/check_repo.py . --require-skill
```

See [contribution guidelines](CONTRIBUTING.md) for metadata validation and checker tests.

## Documentation

- [Bilingual standards index](references/translations.md)
- [Checker usage and agent metadata](references/tooling.md)
- [Skill entry point](SKILL.md)
- [Default coding conventions](references/profile.md)
- [Coverage index](references/coverage.md)
- [Official standards and sources](references/sources.md)
- [Open-source adoption](references/open-source.md)
- [Third-party notices](THIRD_PARTY_NOTICES.md)

The complete standards are available in English and Simplified Chinese, with a language switch on every document.

## License

[MIT](LICENSE) for original work; adapted web guidance is attributed under CC BY 4.0, with other third-party materials under their respective licenses. See [notices](THIRD_PARTY_NOTICES.md).
