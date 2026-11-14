# UI, interaction, page, and visual design

**English** | [简体中文](../zh-CN/product/ui-ux.md) | [Standards index](../translations.md)

## UX01 Establish usage context

- Identify users, core tasks, frequency, devices, environment, permissions, information density, success criteria
- Enterprise tools prioritize sustained work, keyboard efficiency, complex tables, batches, audit; consumer products prioritize comprehension, trust, mobile interaction, primary flows
- IoT pages show data freshness, connectivity, confirmation levels rather than substituting animation for device facts
- For new pages establish information architecture, states, layout intent before visual language; local fixes preserve mature systems
- Choose a primary [design system](design-systems.md) rather than inconsistent components/icons/interactions

## UX02 Information architecture and layout

- Give each page a title, primary task/action and distinct secondary/destructive hierarchy/placement
- Organize by task/cognition rather than database-field order
- Give top navigation, sidebars, breadcrumbs, page anchors distinct purposes without crowding content
- Use consistent grids, alignment, spacing, dimensions, density tokens according to the project
- Use cards for meaningful groups rather than shadow containers around every text fragment
- Use wide screens effectively and reprioritize narrow layouts rather than shrinking desktop pages
- Handle long text, extreme numbers, empty fields, localization, zoom without breakage
- Fixed bars/floating buttons must not obscure focus, keyboards, content, safe areas
- Keep existing content stable during loading and reserve media dimensions

## UX03 Colors and themes

- Organize base/semantic/component tokens for backgrounds, surfaces, text, borders, brand, success, warning, error, focus
- Define coherent primary/accent relationships; reserve primary colors for key actions/selection instead of every surface
- Generally check normal text at WCAG AA 4.5:1 and large text at 3:1 using WCAG's large-text definition
- Apply non-text contrast to relevant boundaries/graphics and distinguish disabled/decorative elements from actionable controls
- Pair color with text, icons, shapes rather than red/green alone
- Define light/dark semantic hierarchy separately rather than inversion; remeasure contrast after brand changes
- Reserve error red for actual errors/danger; distinguish warnings/information
- Use gradients, glass, shadows, blur, glow for task needs without compromising reading, performance, hierarchy
- Link color decisions to brand/context/validation rather than universal claims about blue professionalism or purple AI

## UX04 Typography, icons, content

- Maintain limited stable heading/body/support/data hierarchy and verify Chinese/Latin fallback fonts
- Align comparative numbers appropriately and use consistent regional dates, money, units
- Preserve contrast for secondary text rather than extremely light gray
- Standardize icon style/stroke/size; label icon buttons accessibly and prefer text for key actions
- Use users' task language instead of internal exceptions/database names/implementation details
- Label actions specifically, such as Save changes or Export selected devices, rather than ambiguous OK/Action
- Explain what failed and how to recover rather than generic errors/raw stacks
- Check font/image/icon licenses and avoid extracting unauthorized brand assets

## UX05 Forms and editing

- Keep labels visible, placeholders illustrative, requirements/formats understandable before action
- Match input types, keyboards, units, ranges, defaults, autofill to actual data
- Validate after appropriate interaction and on submission; synchronize visual and accessible error states and focus the first error or summary; see [web interaction](../web/interaction.md)
- Associate errors with fields, preserve input, provide fixes/error summaries
- Align frontend/backend validation; client checks improve UX rather than replacing server checks
- Distinguish unchanged, saving, saved, failed, conflict; repeated clicks must not duplicate side effects
- Handle unsaved navigation by loss risk with recovery/drafts/confirmation rather than dialogs everywhere
- Explain objects/counts/consequences for destructive actions; favor undo for low-risk reversible operations

## UX06 Tables, search, batches

- Prioritize columns by tasks and control density, pinning, overflow rather than exposing all database fields
- Keep filters, sorting, pages consistent with URLs/back navigation and shareable queries when useful
- Distinguish no input, no matches, request failure, forbidden instead of one empty state
- Specify current-page, selected-item, all-matching selection scope/count across pages
- Show partial success, reasons, retry scope, audits for batches rather than hiding failed items behind one toast
- Use server queries, pagination, virtualization for large data and verify keyboard/screen-reader behavior
- Track asynchronous exports with progress/result location, expiry, permission changes, timeouts

## UX07 States, feedback, async work

Consider applicable initial, loading, empty, normal, partial, forbidden, offline, timeout, failed, successful, unknown-result states for every main flow.

- Load only necessary regions, preserve useful contents, match skeletons to actual layout
- Track long tasks and offer working cancellation only where supported
- Match feedback to actual confirmation levels; dispatch, payment acceptance, execution are distinct
- Use toasts for transient noncritical information; retain important errors/pending work in recoverable locations
- Use optimistic updates only for suitable reversible risk and restore/explain failures
- Provide weak/offline retry, drafts, recovery, freshness without encouraging duplicate unknown-result submissions

## UX08 Navigation and interaction

- Links navigate/buttons act; preserve browser back, new tabs, meaningful URLs
- Dialogs serve short tasks; prefer pages/appropriate drawers for complex multistep editing
- Select native dialog or popover semantics for the task and verify focus entry, modal containment, Esc, light-dismiss, background interaction and restoration; see [web interaction](../web/interaction.md)
- Main flows work by keyboard with logical order and unobscured focus
- Make shortcuts discoverable without overriding common platform behavior; provide drag alternatives
- Consider touch size/spacing rather than mouse precision alone

## UX09 Accessibility and motion

- Target applicable WCAG 2.2 AA with screen-reader/keyboard validation rather than claiming automatic certification
- Provide names, roles, states, semantic headings, live regions; ARIA must not duplicate/replace native semantics
- Check Web target size against WCAG 2.2's 24 CSS px minimum and exceptions; 44 CSS px can be a more comfortable target
- Use platform-specific iOS/Android sizes; pt, dp, CSS px are not interchangeable
- Motion explains transitions/spatial relationships/feedback with consistent timing/easing rather than mandatory hero animation
- Respect reduced motion/system settings, prevent flashing, keep essential content understandable without motion
- Verify screen readers, color-vision differences, zoom, imprecise input, high contrast for target users

## UX10 Acceptance

- Use real/representative data for main tasks, long text, extrema, critical states
- Check breakpoints, touch, keyboard, screen readers, themes, text scaling
- Review tokens, spacing, hierarchy, icons, contrast, focus, recoverability
- Document selected systems, components, states, verification for new pages
- Screenshots show one appearance state rather than proving interactions, accessibility, performance, business usability
