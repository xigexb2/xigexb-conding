# Requirements and acceptance mapping

**English** | [简体中文](zh-CN/requirements-matrix.md) | [Standards index](translations.md)

This table maps explicit requirements; existing directories alone do not establish content quality or behavior. Projects must still provide versions, requirements, verification resources.

| Requirement | Implementation | Acceptance criteria |
| --- | --- | --- |
| Personal coding habits | [Conventions](profile.md) | Encoding, comments, size, testing, SQL, Git are explicit |
| All languages: at most 20 same-family sources per package/directory | [Directory standards](directory-structure.md) | Mixed suffixes/tests/first-party generated files combined; design-time splitting; CLI supports unknown groups |
| Java, Go, Rust, C, C++, Python | [Languages](languages/) | Separate topics with contracts, resources, concurrency, verification |
| Vue, JavaScript, TypeScript | [Languages](languages/) | Separate topics without forced framework/style migration |
| SQL, web, native development | [SQL](languages/sql.md), [HTML/CSS](languages/html-css.md), [Kotlin](languages/kotlin.md), [Swift](languages/swift.md) | Distinct dialect/browser/lifecycle/platform contracts |
| Architecture and patterns | [Architecture](engineering/architecture.md), [patterns](engineering/design-patterns.md) | Actual variation, responsibilities, costs, language mappings |
| Concurrency, performance, algorithms | [Concurrency/performance](engineering/concurrency-performance.md), [algorithms](engineering/algorithms.md) | Bounds, correctness, invariants, complexity, measurement |
| Backend/public enterprise practices | [Backend](engineering/backend.md), [frameworks](engineering/frameworks.md) | Enterprise/consumer, APIs, transactions, recovery, versions, tradeoffs |
| UI, interaction, pages, color | [UI](product/ui-ux.md) | Tasks, states, tokens, contrast, keyboard, responsiveness, recovery |
| Vendor design languages | [Systems](product/design-systems.md) | Public sources, applicability, differences, access limitations |
| iOS, Android, Web, hybrid, mini-programs | [Platforms](product/mobile.md) | HIG/Material, permissions, lifecycle, weak networks, upgrades |
| Enterprise, consumer, IoT, internet | [Backend](engineering/backend.md), [protocols](engineering/protocols-distributed.md) | Context differences; acceptance is not execution |
| Low-level systems | [Systems](engineering/systems.md) | ABI, memory, SMP, interrupts, I/O, evidence levels |
| Embedded and communication | [Embedded](hardware/embedded.md), [communication](hardware/communications.md) | RTOS, drivers, signals, interfaces, wireless, real-board boundaries |
| Circuits and PCB | [Hardware](hardware/electronics-pcb.md) | Parts, power, schematics, layout, manufacturing, measurements |
| Chip design | [RTL/chips](hardware/chip-design.md), [analog ICs](hardware/analog-ic.md) | Timing, CDC/RDC, analog specs, PVT/mismatch, extraction, sign-off |
| Security | [Security](engineering/security.md) | Identity, authorization, data, inputs, supply chain, devices, AI tools |
| Git and releases | [Git](engineering/git.md), [delivery](engineering/delivery.md) | Authorization, atomic changes, PRs, versions, traceable artifacts |
| GitHub research/adoption | [Research](github-research.md), [open source](open-source.md) | Snapshots, fixed commits, licenses, decisions, maintenance |
| Discoverable/installable skill | [Entry](../SKILL.md), [README](../README.md) | Metadata, on-demand routing, relative resources, UI metadata |
| Executable checks | [Verification](verification.md) | Text/directory checks, strict YAML, behavioral tests, CI |
| Complete bilingual skill | [Language index](translations.md), [tools](tooling.md) | English default, complete Chinese counterparts, reciprocal navigation, metadata variants, CI coverage |

## What general standards alone cannot prove

- Every rule for every language/framework, or measurable 99% coverage without a complete denominator
- Private company rules beyond legally available sources and clearly identified product observations
- Real throughput, compliance, board functionality, chip sign-off without project data/tools/experiments
- Whether third-party agents always comply; format/script checks do not replace independent behavioral evaluations

These boundaries do not exempt explicit mandatory rules. Add suffixes/topics for new languages and invariants/acceptance for new business contexts rather than abandoning engineering standards outside examples.
