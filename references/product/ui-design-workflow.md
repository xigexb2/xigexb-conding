# UI design, review, and component implementation

**English** | [简体中文](../zh-CN/product/ui-design-workflow.md) | [Standards index](../translations.md)

Use the sections relevant to the current task. Carry decisions forward through the project's existing design documents, theme tokens and components. See [visual design](visual-design.md) for exploration and [UI/UX standards](ui-ux.md) for interaction and accessibility.

## UW01 Define the design brief

- Identify the product audience, main task, platform, target stack and primary success condition. Map the main flow and relevant loading, empty, error and permission states before choosing a layout.
- When consulting a design reference database, search for one decision at a time with a product, platform or interaction constraint. Check that the recommendation fits the actual stack and task. Record the chosen rule and where it applies.
- Record shared tokens and component rules in the project's authoritative design document. Keep page-specific departures near the affected page with their rationale. Preview representative controls and theme combinations before adopting token changes. Use the [DESIGN.md guide](design-md.md) when the project needs that exchange format. [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/b73ee96f8d4ff7bbc279c52dadcd907ffe23629c/.claude/skills/ui-ux-pro-max/SKILL.md)

## UW02 Redesign from the product content

- Establish which screen regions and behaviors are in scope. Keep the approved navigation, actions and data semantics intact during a visual redesign unless the brief calls for changing them.
- Build the visual hierarchy around the primary task and real content. Choose layout, density, type, color and emphasis for the surface. For example, a product page can lead with a concrete product image, while a console should make its current state and next action easy to find.
- Compare a representative view before and after. Open the result in the target browser or app, then check long content, narrow layouts and the established action paths. Use motion where it clarifies feedback or a state change. [Taste Skill](https://github.com/Leonxlnx/taste-skill/blob/d1a2bb41d927083ac7118f60cfc9cdf711810ea0/skills/taste-skill/SKILL.md)

## UW03 Review usability and implementation

- Scope the review to a route or screen, user journey, representative data, theme and viewport or device. Review hierarchy, discoverability and task completion. Use separate evidence from rendered interaction checks, accessibility tooling or source inspection to substantiate findings.
- Audit keyboard focus, accessible names, contrast, theming, responsive layout, touch behavior and performance where applicable. For native screens use the target platform and accessibility tools. Record which states and devices were exercised.
- Describe each finding with the trigger, observed behavior, impact and fix. Prioritize blocked tasks, lost data or severe accessibility issues before cosmetic issues. Reproduce the reported issue and rerun the relevant check after the fix. [Impeccable critique](https://github.com/pbakaus/impeccable/blob/2fc5e1459efbbf06d92c7306517c286bf12490cf/.agents/skills/impeccable/reference/critique.md) · [Impeccable audit](https://github.com/pbakaus/impeccable/blob/2fc5e1459efbbf06d92c7306517c286bf12490cf/.agents/skills/impeccable/reference/audit.md)

## UW04 Compose, integrate and verify components

- For shadcn/ui projects, inspect `components.json`, the installed primitive family, aliases, project theme and framework conventions. Compose existing form, dialog, table and chart primitives with the project's tokens. Keep component variants in their established owner.
- Before importing or updating a registry item, check source, dependencies, target paths and diffs for local modifications. Review the resulting aliases, client/server boundaries, styling and accessibility on the target stack.
- For data tables, explicitly define who owns sorting, filtering, pagination and row selection. With server pagination, tie selection to stable row IDs and define cross-page behavior. Check loading, empty, errors, permission-dependent actions, focus restoration and keyboard operation. [shadcn skill](https://github.com/shadcn-ui/ui/blob/0e5b2e621a9ee4cf6a604bbe6c5c0d5b70561eb4/skills/shadcn/SKILL.md) · [shadcn data table](https://github.com/shadcn-ui/ui/blob/0e5b2e621a9ee4cf6a604bbe6c5c0d5b70561eb4/apps/v4/content/docs/components/radix/data-table.mdx)

See [third-party attribution](../../THIRD_PARTY_NOTICES.md#ui-design-workflow-sources) for the reviewed sources and licenses.
