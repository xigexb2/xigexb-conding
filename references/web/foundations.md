# Modern web platform foundations

**English** | [简体中文](../zh-CN/web/foundations.md) | [Standards index](../translations.md)

## WB01 Compatibility policy

- Identify supported browser versions, embedded WebViews, assistive technologies and the project's existing framework/build constraints before choosing APIs
- Use Baseline and browser compatibility data as evidence, not a replacement for the actual target matrix; a feature's support, subfeatures, known bugs, and polyfill limitations can differ
- Prefer native HTML/CSS/DOM features when they satisfy the task, accessibility, and supported browsers; test realistic degradation or a focused fallback when they do not
- Treat origin trials, flags, browser-specific, experimental and fast-changing features as opt-in after explicit project authorization and feature/version checks; never enable them silently
- Avoid installing/running an unpinned network CLI, forcing telemetry, or replacing established framework/components just to apply guidance

## WB02 Semantics, layout, and CSS

- Choose semantic elements, native buttons, links, labels, headings, lists, tables and landmarks first; preserve document and keyboard reading order
- Use responsive layout from content constraints with Grid/Flex, intrinsic sizing, wrapping, container or media queries as appropriate; avoid hardcoded viewport-only scaling
- Choose logical properties when the meaning should follow writing direction; retain physical directions where mirroring would change the intended behavior
- Manage cascade and specificity using the repository's conventions; use layers, scoped selectors, `:where()`, `:is()` and custom properties where supported and useful, without rewriting existing styles wholesale
- Prefer selectors such as `:has()` for suitable state styling when supported, with a tested fallback; do not assume all selector subfeatures work identically
- Centralize semantic design tokens, system theme, `color-scheme`, `prefers-color-scheme`, contrast, forced-colors, text scaling and reduced-motion handling
- Verify newer color spaces, CSS functions, fonts, nesting, scrolling and anchoring against targets; isolate enhancements with `@supports` when appropriate
- Custom elements and Shadow DOM need accessible names, keyboard behavior, lifecycle cleanup, styling boundaries and form integration; consider SSR and upgrade timing before adoption

## WB03 International text and layout

- Keep source text and user content readable under translation, long strings, zoom, RTL and different writing modes; prevent accidental overflow and clipping
- Use language-appropriate formatting for dates, times, numbers, currencies and calendars; model absolute instants, local dates and time zones separately
- Assess `Intl` and `Temporal` availability and timezone data for actual targets; the latter must not be assumed universally available
- Choose fonts and fallback metrics to reduce layout shifts while preserving Chinese/Latin coverage and real licensing

## WB04 Evidence

Check real responsive breakpoints, keyboard order, visible focus, screen reader semantics, zoom, reduced motion, forced colors, supported browsers and framework hydration. See the [upstream catalog](catalog.md) for the complete pinned topic list.

Adapted from [GoogleChrome Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/SKILL.md) and the linked catalog; changes integrate project constraints and compatibility/security review. Guide content is [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); extension reference material follows upstream Apache-2.0. See [notices](../../THIRD_PARTY_NOTICES.md).
