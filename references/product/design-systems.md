# Design languages, component libraries, and enterprise references

**English** | [简体中文](../zh-CN/product/design-systems.md) | [Standards index](../translations.md)

These are candidates for different product contexts rather than dependencies to install together. Choose a primary system and adapt brand through consistent tokens, components, interactions. A public product appearance is not automatically a reusable official specification.

## DS01 Sources and applicability

| System | Official entry | Useful reference | Boundaries |
| --- | --- | --- | --- |
| Ant Design / Ant Design Vue | [Ant](https://ant.design/), [Vue implementation](https://antdv.com/) | Enterprise tools, forms, tables, information/action hierarchy | Check React/Vue implementations separately; APIs differ |
| Tencent TDesign | [TDesign](https://tdesign.tencent.com/) | Enterprise Vue/React, mobile, mini-program consistency | Select actual platform/version |
| ByteDance Arco Design | [Arco](https://arco.design/) | Dense enterprise data, themes, tokens | Distinguish React/Vue and maintenance status |
| ByteDance Semi Design | [Semi](https://semi.design/) | Enterprise tools, themes, forms, workbenches | Not a universal mandate for all ByteDance/Douyin products |
| JetBrains Int UI | [IntelliJ Platform UI](https://plugins.jetbrains.com/docs/intellij/ui-guidelines-welcome.html) | IDEs, desktop tools, density, keyboard efficiency | Desktop/plugin rules are not mobile rules |
| Google Material Design | [Material 3](https://m3.material.io/) | Android, adaptive layout, semantic colors, states | Follow target/SDK capabilities rather than forcing Android styling on all Web apps |
| Apple Human Interface Guidelines | [HIG](https://developer.apple.com/design/human-interface-guidelines/) | Native iOS/iPadOS/macOS behavior/accessibility | Verify platforms, versions, brand licenses |
| IBM Carbon | [Carbon](https://carbondesignsystem.com/) | Enterprise density, accessibility, composability | Select supported implementations without mixing visual baselines |
| Oracle Redwood | [Redwood](https://redwood.oracle.com/) | Enterprise experiences, content/business hierarchy | Public entry does not expose every internal rule |
| JD JDesign | [JDesign](https://jdesign.jd.com/) | E-commerce/enterprise design discovery | Verify access/component licenses; do not invent inaccessible details |
| Douyin Open Platform | [Developer documentation](https://developer.open-douyin.com/) | Mini-program/platform capabilities, interactions, reviews | Consumer-app private rules are not assumed public |
| OpenAI Apps SDK | [Design guidelines](https://developers.openai.com/apps-sdk/concepts/design-guidelines/) | Conversational tools, results, confirmation | Scoped to Apps SDK rather than a universal OpenAI design system |
| Anthropic / Claude | [Public skills](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Intent, content, visual coherence, AI interactions | Public skills/product observations are not a complete HIG |

Names belong to their owners. This project does not represent those companies or bundle fonts, logos, screenshots, unlicensed assets.

## DS02 Selection order

1. Preserve mature existing systems; local features do not justify component-library migration.
2. Native mobile first follows HIG/Material/platform interaction; express brand through semantic tokens/content.
3. Choose enterprise Ant/TDesign/Arco/Semi/Carbon by stack, coverage, accessibility, theming, maintenance, internationalization.
4. Start consumer/e-commerce/content products from tasks, architecture, trust rather than copying enterprise form density.
5. Reference JetBrains keyboard, density, contextual-information practices for IDEs, operations consoles, protocol/debugging tools.
6. Compare Carbon/Redwood workflow/hierarchy for large business systems; technology/licenses determine components.

## DS03 Unified design contracts

- Maintain semantic color, type, spacing, radius, hierarchy, motion, breakpoint tokens
- Map base to semantic to component tokens with centralized theme switching
- Where tools need to exchange design tokens, export DTCG JSON or CSS custom properties using the existing toolchain. Preview resolved theme values and preserve existing tokens.
- Keep action names, position, colors, shortcuts consistent across pages
- Preserve component accessibility/extension contracts when wrapping business behavior rather than reimplementing everything
- Validate density, dark mode, focus, disabled, error, loading, selection as a state matrix
- Record migration scope/visual regressions and check upgraded APIs, styles, screen-reader behavior
- Do not turn repository preferences such as mandatory dark themes, banned hamburger menus, full-screen sections into universal rules

For token extraction, `DESIGN.md`, and prototype-to-code handoff, see the [Google Stitch workflow](stitch-workflow.md).

## DS04 AI products and conversational tools

- Distinguish generation, sources, tool status, actual external results
- Define streaming, stop, retry, edit, recovery; stopping generation does not undo completed actions
- Execute external effects under explicit authorization and explain targets, scope, consequences
- Do not invent progress, citations, successful status to increase perceived trust
- Design long responses, code, tables, attachments, small screens with keyboard, copy, screen-reader support
- Do not infer/promote undisclosed OpenAI/Claude implementations/design standards

## DS05 Review output

Record the primary design system, component versions, token entry points, platform differences, visual acceptance. Findings identify pages, states, triggers rather than vague claims about lacking sophistication.
