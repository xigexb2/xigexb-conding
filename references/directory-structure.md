# Mandatory package and directory limits for all languages

**English** | [简体中文](zh-CN/directory-structure.md) | [Standards index](translations.md)

## DIR01 Hard limit

Each package/directory directly owns at most 20 same-family source files. This applies to all languages, components, styles, interface definitions, infrastructure code, HDL rather than Go/Java alone.

- Include first-party production, tests, declarations, headers, platform variants, generated sources in their family
- Count child/grandchild/deeper directories independently; the whole project is not limited to 20 files
- Do not bypass by suffixes, generated labels, vendor/build placement, same-directory tests, numbered folders
- Original third-party dependencies, build output, non-source assets are outside first-party package design; identify scope without reorganizing vendors arbitrarily
- Organize documentation/configuration by responsibility too; this skill avoids piling references into one directory

## DIR02 Source families

| Family | Combined count |
| --- | --- |
| Java | .java including tests/first-party generated files |
| Go | .go including _test.go, platform/build-tag variants |
| Rust | .rs including module production/tests |
| C/C++ | .c, .h, .cpp, .cc, .cxx, .hpp, .hh, .hxx |
| Python | .py, .pyi |
| JavaScript/TypeScript | .js, .jsx, .mjs, .cjs, .ts, .tsx, .mts, .cts |
| Vue | .vue; separate script/style files follow their own families |
| Kotlin | .kt, .kts |
| Swift, Dart, C#, PHP, Lua, Zig, SQL, etc. | Source/tests of each language together |
| HTML | .html, .htm |
| Styles | .css, .scss, .sass, .less |
| Verilog/SystemVerilog | .v, .sv, .vh, .svh |
| VHDL | .vhd, .vhdl |
| Shell/PowerShell, etc. | Related scripts/modules of each family |
| Other languages | Group actual language families; register unknown suffixes rather than exempting them |

Combine C/C++ to avoid header-ownership ambiguity. Logical packages spanning physical directories still need responsibility/dependency review; counts alone do not prove sound modularity.

## DIR03 Prevent violations during design

1. Identify capabilities, inputs/outputs, state owners, reasons to change.
2. Estimate growth in production, tests, platform, generated files beyond current implementation.
3. Select independently describable/evolving/verifiable boundaries such as scheduling, routing, persistence, codecs, transport.
4. Collaborate through explicit APIs, restrict internals, keep dependencies acyclic.
5. Check target size before changes; split cohesively before continuing near 20.
6. Verify imports, builds, tests, resources, generator configuration, public compatibility.

Do not merely create model/service/util buckets that continue growing, or hide incoherent responsibilities under deeper nesting.

## DIR04 Automated checks and scope

- scripts/source_catalog.py centralizes recognized suffixes, families, size rules
- Even --files selecting one file checks complete directly owned recognized families in that source directory
- Mixed suffixes, tests, generated names cannot bypass family counts
- Unknown languages, logical namespaces, responsibility still need review; mechanical success is not complete conformance
- Register --source-group 'Nim=.nim,.nims' to include discovery, 380-line limits, 20-file counts for that invocation; built-in families cannot be overridden/split
- Defaults exclude actual dependency/build directories; excluded first-party deliverable code does not gain exemption
