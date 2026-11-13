# Personal coding habits and default conventions

**English** | [简体中文](zh-CN/profile.md) | [Standards index](translations.md)

This document records xigexb's explicit preferences and existing conventions. They are author choices rather than language standards or universal industry mandates. Repositories/current tasks may tighten them; explain actual differences when adapting.

## P01 Text and formatting

- New/modified code, scripts, configuration, documentation use UTF-8 without BOM and LF
- Nonempty files end with one LF without extra trailing blank lines or whitespace
- Default to spaces in maintained code; Go uses gofmt and syntax exceptions such as Makefile recipe tabs follow official tools
- Java defaults to four spaces, JSON/YAML two; other languages use existing formatters
- Java targets 100 columns with a hard limit of 120; do not compress statements, error handling, comments to fit
- Use actual repository formatting configurations, not nonexistent IDEA files or unrelated bulk formatting

## P02 File and package size

| File type | Maintained-file limit including comments and blank lines |
| --- | --- |
| .java, .kt, .go, .rs, .c, .h, .cpp, .hpp, .js, .vue | 360 lines |
| .py, .ts, .tsx, .jsx, .swift, scripts, other mainstream source files | 380 lines |

- No maintained source file exceeds 380 lines; constant-only enums have no unlimited exemption
- **Every language/implementation technology: at most 20 directly owned same-family source files per package/directory, including production, tests, declarations, headers, first-party generated files; subpackages/directories count separately**
- Estimate growth during design and split by domain, capability, protocol, lifecycle before the limit; avoid arbitrary moves or empty part1/part2 folders afterward
- Preserve package responsibilities/dependency direction in named-package languages; use cohesive directories/stable exports elsewhere
- Merge JS/TS extensions, C/C++ sources/headers, Python source/stubs, style variants; changing suffixes/test names/generated labels cannot bypass counts
- Single-class enums, protocol constants, platform variants, generated first-party code are included; generators must emit into appropriate cohesive subpackages
- Preserve original third-party dependency/artifact/lockfile structure with explicit scope; never disguise first-party code in excluded directories
- See [directory standards](directory-structure.md) for grouping/design; unknown languages still follow the rule and require suffix registration
- Split by stable responsibilities rather than meaningless helpers/interfaces, cycles, fragmented roles

## P03 Simplified Chinese comments

- Handwritten code/documentation comments use professional Simplified Chinese; API identifiers/tool markers such as SAFETY may remain
- Explain responsibilities, contracts, units, ranges, nullability, ownership, concurrency, failure conditions, non-obvious reasons
- Use multiline Java Javadoc for interfaces, classes, records, enums, annotations, constructors, methods, fields; explain locals according to complexity
- Interfaces define behavioral contracts and implementations explain differences; inheritDoc still needs implementation-specific thread/resource constraints
- Go exported comments start with identifiers and continue in Chinese; Python/Rust use native documentation forms
- Default comment paragraphs/commit summaries omit final periods; protocol quotations, URLs, code, original third-party licenses retain their text
- Java class documentation defaults to @author xigexb, actual versions/creation dates; do not copy example dates or 1.0.0 mechanically
- Match @param names; constructors/void methods omit @return; @throws describes actual failure contracts

## P04 Implementation and design

- Single responsibility, high cohesion, low coupling; interfaces express stable contracts and implementations concrete behavior
- Abstract system boundaries, replaceable strategies, test isolation rather than pairing every class with an interface
- Reflect actual business objects, states, ownership, physical processes in models
- Reuse standard libraries, approved dependencies, mature frameworks instead of rewriting reliable existing capabilities
- Base performance on bounded resources, suitable algorithms, batching, fewer round trips, measured results
- Handle inputs, errors, boundaries, exceptional cleanup comprehensively rather than making unproven bug-free promises

## P05 Java and logging

- Evaluate Java 25 for new projects; existing toolchains govern without automatic upgrades
- Use SLF4J with a private static final field named logger
- Log prose/business dynamic labels use Chinese, with parameter format such as `设备编号[{}],错误信息[{}]`
- Avoid log string concatenation, pass exceptions last, prevent repeated logging of one failure through layers
- Preserve stable machine-readable structured/MDC keys such as traceId/deviceId
- Specify business time zones and elapsed-time units; measure durations monotonically
- Fory JSON is a choice in some existing Java projects only, not a mandatory dependency everywhere

## P06 Verification, SQL, Git

- Add no repository Java unit tests; still compile, run existing checks, temporary executions, necessary integration verification
- Add/update Go unit tests for behavior/concurrency changes; run existing checks for formatting/comments only
- Select Rust/C/C++/Python/frontend tests by risk, not assertions that simply restate implementation
- Leave no ad hoc SQL files; prefer read-only database checks and keep temporary statements out of source repositories
- Create formal migration SQL only when the current task explicitly authorizes that exception
- Git commit/push each require explicit authorization; a commit-only request produces a local commit only
- Use `type(scope): 简体中文摘要`, lowercase English types, first line at most 72 characters, no final period
- Types: feat, fix, refactor, perf, docs, style, test, build, ci, chore, revert
- Stage explicit paths/review staged diffs; preserve user/other-task changes without destructive overwrites

## P07 Product experience

- Make pages useful: clear primary tasks, prompt feedback, readable hierarchy, recoverable errors
- Validate colors by context, brand, platform, contrast, semantics rather than universal color claims
- Follow individual Web/iOS/Android/mini-program interactions instead of copying one desktop page

## Public-release boundary

Publish general standards and selected engineering experience only. Exclude work servers, internal addresses, accounts, credentials, private repository identifiers, device keys, customer data, conversation history.
