# TypeScript

**English** | [简体中文](../zh-CN/languages/typescript.md) | [Standards index](../translations.md)

Each package/directory directly owns at most 20 same-family source files, including tests, declarations, and first-party generated files. Design cohesive subpackages according to the [shared directory standards](../directory-structure.md).

Apply [JavaScript](javascript.md) runtime rules first; types do not alter network/browser semantics.

- Limit files to 380 lines and use existing tsconfig, type checker, lint settings
- Prefer strict for new projects; improve legacy code incrementally without unrelated global failures
- Accept external data as unknown and validate at runtime; do not invent trust through as, any, non-null assertions
- Model requests, workflows, async states with discriminated unions and exhaustive legal branches
- Keep public types diagnosable/maintainable; avoid elaborate type gymnastics for simple values
- Readonly mainly constrains types rather than deep freezing/thread synchronization
- Align type imports, aliases, ESM/CJS, declarations with actual runtime/bundling
- Distinguish optional/nullable DTO fields and account for undefined omission in JSON
- Use generics for real call relationships rather than parameterizing everything or merging responsibilities through broad unions
- Choose enums, const objects, literal unions by build tooling without unjustified universal replacement
- Shared schemas need runtime parsing, evolution, independent release boundaries beyond shared .d.ts
- Run tsc --noEmit or existing type commands; Vue uses matching vue-tsc
- Bundling success does not prove type correctness, which does not prove external-data validity

See [sources](../sources.md): TypeScript Handbook, TSConfig Reference.
