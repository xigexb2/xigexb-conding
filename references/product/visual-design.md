# Visual design exploration and prototyping

**English** | [简体中文](../zh-CN/product/visual-design.md) | [Standards index](../translations.md)

## VD01 Choose a visual direction

Start from the real content, existing product and design system, audience, and delivery medium. Verify material claims and use official or authorized assets. Choose a focal point that shows how the product works, what the data says, or what distinguishes the subject.

When the brief leaves direction open, use three starting points: a design approach suited to the subject, a strong reference in the same medium, and an unexpected treatment. For substantial exploration, sketch up to six candidates and develop up to three distinct directions with representative screens, slides, or keyframes. Compare structure, density, hierarchy and interaction. If the user delegates selection, choose the best fit and explain the assumption. Focused iterations follow the selected direction.

Borrow the reference's way of organizing information. Build the palette, typography, composition and imagery around the actual subject. Use authentic or licensed images where needed and label missing content. Verify claims, metrics, and testimonials before presenting them.

## VD02 Design for the deliverable

| Medium | Design and delivery checks |
| --- | --- |
| Web and dashboards | Show the product in use. Check responsive layout and key interactions. Apply the project's production Web rules when implementing the actual product. |
| App and mini-program prototypes | Include primary, loading, empty, error and permission states. Respect platform navigation, safe areas and controls. |
| Store screenshots and social carousels | Plan the reading sequence. Check cropping, legibility and platform dimensions. Use accurate product captures and copy. |
| Presentations and editable PPTX | Use representative slides to establish direction. Check legibility at viewing distance and confirm editable text and objects in the exported file. |
| Infographics | Verify data, units, scales and labels. Pick an encoding suited to the comparison and provide an accessible explanation where needed. |
| Motion and video | Storyboard the message and pacing. Inspect rendered keyframes and confirm the requested format and audio. |

## VD03 Review the rendered result

Inspect the real viewport, slide or frame at its intended size. Identify the few issues with the most impact, fix them and review the new render. Check hierarchy, typography, overflow, assets, accessibility and the main task. Exercise keyboard, touch and failure paths where applicable. Open export files in the target viewer to check rendering and editability.

Adapted from Huashu Design 3.5.0. The number of alternatives and review rounds scales with the task. The project's file limits and asset permissions apply.

## VD04 Choose UI design references by task

Start with the screen problem that needs a decision. Carry approved flows, visual direction and design tokens forward when the work spans multiple stages.

| Situation | Method and deliverable |
| --- | --- |
| Requirements or user flows are unclear | Use [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/b73ee96f8d4ff7bbc279c52dadcd907ffe23629c) to define users, tasks, key states and recovery. Deliver a page outline and a low-fidelity flow. Walk through the main task before settling on a visual direction. |
| An existing prototype or screen needs a redesign | Use [Taste Skill](https://github.com/Leonxlnx/taste-skill/tree/d1a2bb41d927083ac7118f60cfc9cdf711810ea0) as a reference for hierarchy, composition, typography and color using real content. Show representative before-and-after screens. Recheck existing actions, long content and narrow viewports. |
| A mature reference or an existing screen needs analysis | Use [Impeccable](https://github.com/pbakaus/impeccable/blob/2fc5e1459efbbf06d92c7306517c286bf12490cf/README.md) to examine content order, action priority, component composition and responsive layout. Rank issues by impact on the task. Check navigation, focus, theming and performance. |
| An admin console, dashboard or SaaS workspace needs implementation | Evaluate [shadcn/ui](https://github.com/shadcn-ui/ui) for tables, forms, dialogs and charts when the stack supports it and component selection is in scope. Reuse the project's components and tokens where established. Verify keyboard use, empty states, errors and permissions. |
| An approved design needs a presentation or handoff | Apply the article's Design MD Collection handoff approach. Use the project's [DESIGN.md guide](design-md.md) for reusable tokens and component rules. In a case study, connect the goal, design decisions, representative screens and verification results. |

The use cases are adapted from Jason's article. The article names Design MD Collection. This workflow uses the existing `DESIGN.md` format for its handoff. [Original article](https://mp.weixin.qq.com/s/IgzOThFw1Bqx8zu4FKEzBQ)

For the steps behind the brief, redesign, review and component integration, see [UI design, review, and component implementation](ui-design-workflow.md).

## Upstream references

- [SKILL.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/SKILL.md)
- [references/directions.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/directions.md)
- [references/polish-loop.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/polish-loop.md)
- [references/brand-asset-protocol.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/brand-asset-protocol.md)
- [references/modules/web.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/modules/web.md)
- [references/app-prototype.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/app-prototype.md)
- [references/modules/miniprogram.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/modules/miniprogram.md)
- [references/modules/appstore.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/modules/appstore.md)
- [references/modules/deck.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/modules/deck.md)
- [references/editable-pptx.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/editable-pptx.md)
- [references/modules/infographic.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/modules/infographic.md)
- [references/modules/xiaohongshu.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/modules/xiaohongshu.md)
- [references/modules/motion.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/modules/motion.md)
- [references/design-styles.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/design-styles.md)
