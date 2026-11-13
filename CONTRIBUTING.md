# Contributing and maintaining standards

**English** | [简体中文](CONTRIBUTING.zh-CN.md) | [Standards index](references/translations.md)

## Before changes

- Identify personal preferences, official contracts, framework-version behavior, engineering advice
- Read relevant references/sources and explain scope and the old rule's problem
- Do not turn isolated historical failures into universal prohibitions or copy entire upstream skills/unclear-license content
- Exclude internal environments, real customer data, credentials, private protocols, restricted materials

## Documentation and code

- Use UTF-8 without BOM, LF, one final newline, no trailing whitespace, Chinese code comments
- Keep the entry concise; put rules in relevant references and update routes/coverage
- Resolve local links and substantiate version-specific claims; do not invent performance/certification
- Python tools use the standard library where practical, typing, error handling, separated responsibilities, at most 380 lines per file
- Add meaningful tests for new scripts/behavior rather than text-matching/implementation-mirroring assertions
- Verbatim third-party licenses retain original text rather than source-format/size conventions

## Verification

```text
python scripts/check_repo.py . --require-skill
python -m pip install -r requirements-dev.txt
python scripts/validate_skill.py .
python scripts/check_translations.py .
python -m unittest discover -s tests -v
```

Validate YAML through validate_skill.py in CI; basic regex is not complete YAML parsing. Use applicable client skill validators as well.

For rule changes walk through verification.md scenarios against authorization, native formatting, ownership, platform semantics. Complex changes may warrant independent agent evaluations; manual document review is not an executed model evaluation.

## Bilingual maintenance

- English is canonical at default paths; Chinese references mirror them under references/zh-CN, while root documents use .zh-CN.md
- Maintain both languages in one change, preserving rule IDs, requirements, examples, sources, version-specific qualifications
- Every document links to its exact counterpart; Chinese internal navigation stays in the Chinese tree
- Run the translation checker for counterpart coverage, reverse navigation, rule IDs, external links, code-fence balance, language-tree integrity
- Keep code comments in Chinese and original legal license texts verbatim; English explanations accompany tool usage
- See [translation index](references/translations.md) and [tools](references/tooling.md)

## Commits and review

- Describe the concrete defect, scope, final changes, verification in each PR
- Use Conventional Commits with type(scope) and Simplified Chinese summaries; see [Git](references/engineering/git.md)
- Pin upstream references to commits/files/licenses and document decisions; handle copyright/NOTICE for introduced code/prose
- Links do not prove full review and stars do not justify unverified rules
