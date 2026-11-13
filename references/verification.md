# Verification, debugging, and delivery evidence

**English** | [简体中文](zh-CN/verification.md) | [Standards index](translations.md)

## Q01 Select evidence by risk

| Change | Minimum verification to assess |
| --- | --- |
| Documentation/formatting | Encoding, links, examples, scoped diffs |
| Business behavior | Boundaries, errors, permissions, invariants, regressions |
| Concurrency | Cancellation, timeouts, races, shutdown, duplicate completion, leaks |
| Protocols | Known wire vectors, malformed lengths, direction, independent interoperability |
| Databases | Constraints, transactions, conflicts, plans, migration effects |
| UI | Main tasks, states, responsiveness, keyboard, screen readers, real data |
| Systems/hardware | Target builds, simulation, timing/board checks, explicit gaps |
| Performance | Baseline, representative loads, resources, tail latency |

Follow personal conventions: no new repository Java unit tests; Go behavior changes need corresponding tests. This distinction does not remove necessary runtime verification.

## Q02 Meaningful tests

- Test observable results/invariants instead of mirroring private implementations/text
- Cover representative boundaries, fault injection, cancellation, duplicates, reordering, cleanup
- Use independent properties/reference implementations for property/differential checks rather than shared errors
- Control clocks, seeds, dependencies and isolate temporary directories/ports; long sleeps must not hide synchronization defects
- Mocks verify assumptions, not real database/network/device integration
- Use synthetic data without real secrets/customers and isolate temporary verification artifacts

## Q03 Systematic debugging

1. Record symptoms, expectations, versions, reproduction, necessary logs/captures.
2. Trace input, transformations, state, calls, responses to the first divergence.
3. Form falsifiable hypotheses and minimal experiments changing one key factor at a time.
4. Fix causes/boundaries rather than hiding failures with swallowed errors, longer timeouts, blind retries.
5. Recheck triggers/adjacent risks and report evidence/remaining unknowns.

Timeouts, scans, exceptions do not automatically establish offline devices, successful attacks, lost data. Retain alternative explanations when evidence is insufficient.

## Q04 Final checks

- Final scoped diffs match requirements and preserve existing user work
- Verify UTF-8 without BOM, LF, final newline, source length, Java width, all-language directory family limits
- Inspect dependencies, versions, locks, defaults, licenses, secrets
- Reproduce commands, exit codes, key outcomes; distinguish environment and implementation failures
- Judge final code/actual runs rather than earlier passing versions
- Do not repeat/broaden passing checks without cause; new changes/unresolved risks justify targeted additions

## Q05 Evidence levels

Report actual levels: static checks, compilation, unit/temporary tests, real-component integration, simulation, device/board tests, representative loads. None automatically implies the next or justifies blanket production-ready/vulnerability-free claims.

## Q06 Skill behavior acceptance scenarios

During maintenance, manually review these decisions and record contradictory rules:

- Preserve gofmt tabs and Java spaces rather than overriding them with generic formatting
- Split all-language packages above 20 same-family sources by responsibility; tests/mixed suffixes/first-party generation cannot bypass
- Explicit unknown-language groups enter discovery/size checks; strict YAML rejects syntax errors, duplicate keys, invalid types
- Java 25 synchronized is not mechanically replaced using outdated pinning claims; preview APIs are not enabled by default
- Respect Netty forwarding, auto-release, async retention ownership without double release
- Commit-only requests do not authorize push; preparing public materials does not authorize uploading private code
- Local Vue fixes do not impose migrations/API styles; stale requests cannot overwrite new state
- Device dispatch is not execution success and timeout preserves unknown outcomes
- iOS pt, Android dp, Web CSS px are not interchangeable
- ERC/DRC, RTL simulation, firmware compilation are not hardware sign-off/board acceptance
- Cache locks do not replace SQL parameterization, tenant isolation, unique constraints

These are maintenance expectations rather than evidence of independent agent evaluations or certification.
