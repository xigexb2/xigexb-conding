# Google DESIGN.md format

**English** | [简体中文](../zh-CN/product/design-md.md) | [Standards index](../translations.md)

Use `DESIGN.md` when agents and teams need a shared visual contract. YAML holds exact design tokens. Markdown explains their application, states and exceptions. Google specifies the format as `alpha`. Identify the authoritative token source and synchronization direction when the project already has a theme or token repository.

## DM01 Format and references

- Place tokens in YAML front matter, fenced `yaml` blocks in relevant sections, or both. Define each top-level key once across the document. Use quoted dot-path references such as `"{colors.primary}"`. Components can reference composite typography tokens.
- The pinned specification supports organizational groups in `colors`, `typography`, `rounded` and `spacing`. Check for collisions between flattened names and grouped paths. Apply themes in the target runtime and verify that the chosen tooling supports grouped tokens.
- Keep the recognized English `##` headings in the order shown below for parser compatibility. Localize the prose as needed. Retain applicable sections and use the spec's `omitted` configuration to declare deliberate omissions.
- Reference local handoff material through an inline code span containing `@path[#fragment]`. Resolve references from the directory containing `DESIGN.md`. Markdown fragments match heading slugs. HTML fragments match element IDs or component markers. Keep references within the document directory.

## DM02 Example

Copy the content inside this block as `DESIGN.md` and replace the sample tokens and guidance with the project's design decisions.

```markdown
---
version: alpha
name: Field Console
colors:
  primary: "#15355B"
  on-primary: "#FFFFFF"
typography:
  body-md:
    fontFamily: system-ui
    fontSize: 1rem
rounded:
  control: 6px
spacing:
  control: 12px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.control}"
    padding: "{spacing.control}"
---

## Overview

Support operators reviewing equipment status.

## Colors

Reserve the primary color for the main action.

## Typography

Use the system font for controls and status text.

## Layout

Apply the control spacing between related actions.

## Elevation & Depth

Use borders to distinguish adjacent panels.

## Shapes

Use the control radius on buttons.

## Motion & Micro-interaction

Keep feedback short and respect reduced motion.

## Voice & Content Strategy

Use action verbs that describe the outcome.

## Components

Use the primary button for the main action.

## Do's and Don'ts

Keep labels visible when actions are disabled.
```

## DM03 Validate and export

Use the project's pinned CLI version. The examples use npm release `0.4.0`. Save a baseline as `DESIGN.base.md` before comparing revisions.

The npm 0.4.0 release ignores the upstream `motion` token map. The example records motion in prose so it works with that CLI.

```text
npx @google/design.md@0.4.0 lint DESIGN.md
npx @google/design.md@0.4.0 diff DESIGN.base.md DESIGN.md
npx @google/design.md@0.4.0 export --format dtcg DESIGN.md
npx @google/design.md@0.4.0 export --format css-tailwind DESIGN.md
npx @google/design.md@0.4.0 export --format json-tailwind DESIGN.md
```

- Run `lint` before export. Review schema findings, unresolved references and reported component token contrast. For UI acceptance, check rendered themes, contrast, focus and changing states in the target product.
- Review the `diff` output and corresponding prose changes. Inspect removed or changed tokens for affected components, even when the command exits successfully.
- Choose DTCG JSON, Tailwind v4 CSS or Tailwind v3 JSON according to the target. Inspect warnings and resolved output before applying it. Verify the integrated result, including any runtime theme mapping.

For capturing or generating screens and implementing a design in the target stack, follow the [Stitch workflow](stitch-workflow.md).

[Google format specification](https://github.com/google-labs-code/design.md/blob/db977b3c1d1f309269f43d5d17ae828d54bd6ae3/docs/spec.md) · [Upstream CLI documentation](https://github.com/google-labs-code/design.md/blob/db977b3c1d1f309269f43d5d17ae828d54bd6ae3/README.md) · [Apache-2.0 attribution](../../THIRD_PARTY_NOTICES.md#google-designmd)
