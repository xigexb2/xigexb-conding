# Coverage and boundaries

**English** | [简体中文](zh-CN/coverage.md) | [Standards index](translations.md)

## Supported engineering workflow

| Domain | Coverage | Primary references |
| --- | --- | --- |
| Requirements/architecture | Invariants, contracts, domains, patterns, modules, evolution | engineering/architecture.md, engineering/backend.md |
| Backend | Enterprise/consumer, APIs, transactions, jobs, instances, frameworks | engineering/backend.md, engineering/frameworks.md |
| Languages | Java, Go, Rust, C, C++, Python, JS, TS, Vue, Kotlin, Swift, SQL, HTML/CSS | languages/ |
| Product/UI | Information architecture, colors, type, forms, tables, states, accessibility | product/ui-ux.md, product/design-systems.md |
| Platforms | Web, native, hybrid, cross-platform, mini-programs, weak networks, upgrades | product/mobile.md, engineering/frameworks.md |
| Algorithms/performance | Complexity, structures, numbers, concurrency, backpressure, measurement | engineering/algorithms.md, engineering/concurrency-performance.md |
| Systems | Memory, SMP, interrupts, files, network I/O, diagnosis | engineering/systems.md |
| IoT/communication | Protocols, messages, device state, physical links, DSP, wireless | engineering/protocols-distributed.md, hardware/communications.md |
| Embedded | BSP, RTOS, drivers, DMA, boot, updates, board tests | hardware/embedded.md |
| Hardware | Components, circuits, power, PCB, manufacturing, testing | hardware/electronics-pcb.md |
| Chips | RTL, CDC/RDC, timing, analog/mixed signal, PVT, post-layout, sign-off boundaries | hardware/chip-design.md, hardware/analog-ic.md |
| Data | Models, constraints, SQL, indexes, transactions, migrations, recovery | engineering/database.md, languages/sql.md |
| Security | Threats, identity, authorization, input, cryptography, supply chain, incidents | engineering/security.md |
| Collaboration/operations | Git, PRs, builds, CI, releases, operations, evidence | engineering/git.md, engineering/delivery.md, verification.md |

## Interpreting a comprehensive skill

See [requirements mapping](requirements-matrix.md), [pattern selection](engineering/design-patterns.md), [open-source adoption](open-source.md).
This is an engineering entry point with shared rules and on-demand references, not simultaneous injection of every document. The matrix describes breadth; project-specific official resources, implementation, verification provide depth.

No statistical 99% promise is made. Such a percentage requires a complete requirement set, version scope, acceptance data.

## Areas requiring task-specific materials

- Specific chips, BSPs, PDKs, boards, private protocols, experiments
- Medical, automotive, aviation, functional safety, payment, other regulated certification
- Detailed analog/RF ICs, advanced packaging, process sign-off, restricted IP
- Large-model training, professional cryptographic proofs, unlisted languages/frameworks
- Undisclosed internal company standards/design systems

Apply shared safety/engineering principles and legally available official/industry materials, state missing resources, never invent clauses/certification.

## Maintaining rules

- Put preferences in profile.md, language rules in their topics, framework/platform rules in relevant chapters
- Explain sources, versions, reasons old rules fail
- Check conflicts before new mandates; do not accumulate unlimited exceptions from one historical failure
- Keep tool scope aligned with documentation rather than claiming automated business/security/aesthetic checks
- Make new domains discoverable from SKILL.md and this matrix without hidden files/local environments
