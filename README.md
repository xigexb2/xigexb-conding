# xigexb Coding

**English** | [简体中文](README.zh-CN.md) | [Skill entry](SKILL.md) | [Standards index](references/translations.md) | [Changelog](CHANGELOG.md)

An engineering standards skill for coding agents, covering architecture, implementation, UI/UX, performance, security, and delivery across software and hardware projects.

Built around clear responsibilities, explicit contracts, bounded resources, and verifiable results. Use it to design, implement, refactor, and review enterprise applications, consumer products, web and mobile apps, IoT platforms, embedded systems, and low-level infrastructure.

## Installation

Clone the repository into a skill directory supported by your coding agent. For agents that discover project skills under `.agents/skills`, run this from your project root:

```bash
git clone https://github.com/xigexb2/xigexb-conding.git .agents/skills/xigexb-coding
```

This command installs the default branch. To pin a version, add `--branch <tag>` to `git clone` and choose a tag from [GitHub Releases](https://github.com/xigexb2/xigexb-conding/releases).

Keep the complete directory when installing. The agent discovers the English entry and task index through `SKILL.md`. For Simplified Chinese, request Chinese when invoking the skill, or open `SKILL.zh-CN.md` and its `references/zh-CN/` tree. See the [tooling guide](references/tooling.md) for the default and alternate agent UI metadata.

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

```text
Use $xigexb-coding to extract tokens from an existing Vue app, prepare DESIGN.md,
and verify button states, theme contrast, and Tailwind export.
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

| Task | Project guide |
| --- | --- |
| Design enterprise or consumer screens with accessible color, hierarchy, navigation, forms, tables, and state feedback | [UI/UX standards](references/product/ui-ux.md) |
| Apply four upstream workflows to design briefs, redesigns, usability reviews, and component integration | [UI design, review, and component implementation](references/product/ui-design-workflow.md) |
| Choose UI design references by task, explore visual directions, prototype, and review deliverables | [Visual design exploration and prototyping](references/product/visual-design.md) |
| Choose and apply a design system in an existing product using Ant Design, TDesign, Arco/Semi, JetBrains Int UI, Material 3, Apple HIG, IBM Carbon, or Oracle Redwood as references | [Design systems](references/product/design-systems.md) |
| Write `DESIGN.md` with YAML design tokens, then lint, diff, and export DTCG JSON or Tailwind with the CLI | [Google DESIGN.md format and bilingual example](references/product/design-md.md) |
| Go from a screen brief, extracted design system, and multi-page prototype to implementation and verification in Vue, React, or React Native | [Google Stitch workflow and index of 16 upstream skills](references/product/stitch-workflow.md) |
| Handle navigation, permissions, offline behavior, and lifecycle on iOS, Android, hybrid apps, and mini-programs | [Mobile and cross-platform standards](references/product/mobile.md) |

The Stitch workflow supports local prototyping. When using the Google Stitch service, follow its tool setup and project permissions.

## Modern web standards

The project adapts GoogleChrome Modern Web Guidance into six bilingual references for [Web foundations](references/web/foundations.md), [forms and accessible interaction](references/web/interaction.md), [performance](references/web/performance.md), [security and privacy](references/web/security.md), [PWA and emerging APIs](references/web/advanced.md), and [browser extensions](references/web/extensions.md). The [pinned topic catalog](references/web/catalog.md) links to the upstream originals.

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

Run these checks from the skill root with Python 3.11 or later. The first command uses the standard library. Install the development dependency for full YAML validation and the test suite.

```bash
python -X utf8 scripts/check_repo.py . --require-skill
python -m pip install -r requirements-dev.txt
python -X utf8 scripts/validate_skill.py .
python -X utf8 scripts/check_translations.py .
python -X utf8 -m unittest discover -s tests -v
```

The checks cover text format, source file and directory limits, local links, Skill and agent metadata, bilingual navigation, and checker regressions. To check an application repository, pass its root to the installed skill's checker. See the [tooling guide](references/tooling.md) for options.

## Documentation

- [Standards coverage](references/coverage.md) · [Requirements and acceptance matrix](references/requirements-matrix.md)
- [Official standards and sources](references/sources.md) · [Open-source adoption](references/open-source.md) · [Upstream alignment record](references/upstream-alignment.md)
- [Contributing](CONTRIBUTING.md) · [Security reporting](SECURITY.md) · [Third-party notices](THIRD_PARTY_NOTICES.md)

## License

[MIT](LICENSE) for original work; adapted web guidance is attributed under CC BY 4.0, with other third-party materials under their respective licenses. See [notices](THIRD_PARTY_NOTICES.md).
