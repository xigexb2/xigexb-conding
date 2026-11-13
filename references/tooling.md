# Checker usage and agent metadata

**English** | [简体中文](zh-CN/tooling.md) | [Standards index](translations.md)

## TOOL01 Run from the skill root

Python 3.11 or later is required. Basic text/directory checks use the standard library; strict YAML validation and developer tests need the pinned development dependency.

```text
python scripts/check_repo.py . --require-skill
python -m pip install -r requirements-dev.txt
python scripts/validate_skill.py .
python scripts/check_translations.py .
python -m unittest discover -s tests -v
```

The repository and metadata checkers default to English diagnostics. Select Chinese with --lang zh-CN; help includes both languages. The translation checker reports bilingual findings.

```text
python scripts/check_repo.py . --require-skill --lang zh-CN
python scripts/validate_skill.py . --lang zh-CN
```

Code comments/docstrings remain in Simplified Chinese according to the coding convention; identifiers, command options, and machine schemas retain their native forms.

## TOOL02 Check business repositories

Resolve scripts from the installed skill, then pass the actual business root. File arguments are relative to that root:

```text
python /path/to/xigexb-coding/scripts/check_repo.py /path/to/project --files src/main.go src/worker_test.go
python /path/to/xigexb-coding/scripts/check_repo.py /path/to/project --source-group 'Nim=.nim,.nims'
python scripts/check_repo.py --help
```

- --files requires existing in-root files and still counts all same-family files directly in affected source directories
- --source-group adds suffixes for one invocation with a 380-line/20-file limit; built-in groups cannot be overridden
- --exclude accepts repeatable case-sensitive root-relative POSIX globs; exclusions cannot exempt first-party deliverable code
- Default exclusions cover .git, dependencies, build output, tool caches; .gitignore is not automatically loaded and directory symlinks are not followed
- Bash/PowerShell quoting follows the actual shell

## TOOL03 Scope and diagnostic meanings

| Diagnostic category | Meaning and response |
| --- | --- |
| Encoding/line endings | Save UTF-8 without BOM and LF, remove NUL/trailing whitespace, retain one final newline |
| Source lines/Java width | Split cohesive responsibilities and follow source limits; Java columns count Unicode characters with tabs expanded to four |
| Directory family count | Split the actual package before exceeding 20; mixed suffixes/tests/first-party generation count together |
| Source-group errors | Correct Name=.ext,.ext2; do not override an existing family |
| Local-link errors | Correct missing/out-of-root paths; anchors and complex reference-style links are outside this checker |
| YAML/metadata errors | Fix syntax, duplicate keys, allowed fields/types, name/description limits, agent prompts, matching localized metadata |
| Translation errors | Restore counterparts, reciprocal links, stable rule IDs, source URLs, closed fences, language-consistent navigation |

Checkers are read-only. Repository checks return 0 for success, 1 for findings, 2 for argument/scope errors; other validators return nonzero on failure. Dependency installation is a separate explicit command.

Mechanical translation checks establish coverage and structure rather than semantic equivalence; review both texts for requirements, qualifiers, examples, and version-sensitive claims.

## TOOL04 English and Chinese agent metadata

- [openai.yaml](../agents/openai.yaml) is the active default English UI configuration
- [openai.zh-CN.yaml](../agents/openai.zh-CN.yaml) is the equivalent Chinese configuration supplied for manual selection; clients do not automatically discover this alternative filename
- To use Chinese UI metadata, copy the alternative contents into agents/openai.yaml in your own installation and refresh/reload skills according to the client
- Invoke the Chinese reference tree directly through `SKILL.zh-CN.md`, or request Chinese when using $xigexb-coding
- Both variants keep the same skill name, invocation behavior, rule identifiers, and technical requirements

The original [LICENSE](../LICENSE) and third-party license files remain verbatim. [Chinese license explanation](../LICENSE.zh-CN.md) is a reading aid; original legal texts govern.
