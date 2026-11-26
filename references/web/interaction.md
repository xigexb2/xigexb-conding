# Modern web interaction, forms, and accessibility

**English** | [简体中文](../zh-CN/web/interaction.md) | [Standards index](../translations.md)

## WI01 Native interaction and overlays

- Use native controls and semantics before custom widgets; custom implementations must supply equivalent roles, names, states, keyboard handling and assistive-technology behavior
- Use `<dialog>` for appropriate modal tasks and popover semantics for appropriate nonmodal content; explicitly manage opening/closing, focus, Escape, light-dismiss policy, focus restoration and scroll behavior according to the chosen primitive
- Check `showModal()`, popover, top-layer, anchor positioning and declarative controls against browser support; provide tested fallback where required without changing a modal into an inaccessible overlay
- In framework-managed DOM, respect component lifecycle and ownership; use instance-unique IDs/anchor names and clean listeners/observers on unmount
- Design menus, tabs, tooltips, accordions, carousels, drawers and sortable tables with actual semantics, focus/keyboard interactions and non-pointer alternatives; do not apply one widget's key model to another
- Do not trap focus in nonmodal popovers or rely exclusively on hover, gesture, drag, animation or color to convey functionality

When a context menu contains necessary actions, provide a visible control or equivalent keyboard and touch access. Verify positioning, dismissal and focus restoration.

## WI02 Forms, IME, and error feedback

- Give controls persistent labels and correct `type`, `inputmode`, `autocomplete`, names and units; preserve browser/password-manager autofill, including appropriate one-time-code metadata
- Validate after suitable interaction and on submission; synchronize visible feedback, `aria-invalid`, error descriptions and accessible announcement without announcing untouched errors prematurely
- When custom Enter handling exists, return while IME composition is active; assess relevant Safari versions and targeted compatibility handling such as the legacy 229 signal. Preserve native composition and do not prevent its confirmation
- Preserve native form submission, an explicit submit control, appropriate `requestSubmit()` semantics, duplicate-submission protection and user input on failure
- Respect `prefers-reduced-motion`, touch/keyboard/screen-reader needs, text zoom, forced-colors and platform text scaling; browser/device testing determines actual behavior

## WI03 Motion and scrolling

- Prefer CSS/native view or scroll transitions when they improve a real task and meet support requirements; provide a static usable fallback and avoid motion for users requesting reduction
- Measure animation impact; avoid read/write layout thrashing and long work in scroll handlers. Use appropriate observers, scroll completion events or throttling only when they preserve semantics
- Maintain focus, browser history, deep-link targets and state through same-document or cross-document transitions; avoid duplicate transition names and unbounded animations
- Preserve accessible content, keyboard operation and usable fallbacks for hidden/revealed content, sticky headers, carousels and drag/reorder actions

For a teaser, truncate protected content before sending it to the browser. A visual fade does not change what is available to assistive technology or what can be copied. Keep the action visible and outside the fade.

## WI04 Validation

Test opening, closing, cancellation, rapid repetition, focus restoration, native form behavior, IME confirmation, keyboard navigation, screen readers, browser support and reduced-motion paths. Consult the [upstream catalog](catalog.md) for component-specific guidance.

Adapted from [GoogleChrome Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/SKILL.md) and the linked catalog; changes integrate project constraints and compatibility/security review. Guide content is [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); extension reference material follows upstream Apache-2.0. See [notices](../../THIRD_PARTY_NOTICES.md).
