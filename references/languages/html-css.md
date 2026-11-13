# HTML, CSS, and browser layout

**English** | [简体中文](../zh-CN/languages/html-css.md) | [Standards index](../translations.md)

Each package/directory directly owns at most 20 same-family source files, including tests, declarations, and first-party generated files. Design cohesive subpackages according to the [shared directory standards](../directory-structure.md).

- Use semantic HTML: buttons for actions, links for navigation, real labels for controls
- Prefer native controls when suitable; ARIA cannot replace missing keyboard/state behavior
- Align DOM reading/keyboard order; visual CSS reordering must not confuse interaction
- Use project tokens, spacing scales, breakpoints rather than copying arbitrary colors/dimensions
- Prefer Grid/Flex and normal flow over absolute positioning for fixed screenshots
- Design for contents/containers, long Chinese text/English words/numbers, RTL, text zoom
- Keep visible focus and feedback beyond hover; main flows work with touch, keyboard, mouse
- Specify media dimensions/aspect ratios to avoid shifts and meaningful alternate text
- Respect reduced motion, system themes, contrast needs
- Centralize stacking/overlay/z-index scales, focus rings, scroll locking, focus restoration
- Check browser support/fallbacks for container queries, :has(), other new features
- Configure autofill, input types/modes, error association, internationalization from actual needs
- Use repository formatting and at most 380 maintained source lines; split large pages along stable component boundaries

Combine [UI/interaction](../product/ui-ux.md), [design systems](../product/design-systems.md), MDN, WCAG.
