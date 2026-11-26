# Google Stitch design and implementation workflow

**English** | [简体中文](../zh-CN/product/stitch-workflow.md) | [Standards index](../translations.md)

Use this workflow for AI-assisted screen design, design system extraction, multi-page iteration and implementation. The steps also work with local prototypes and the project's existing design tools. If using the Stitch service, follow the current [MCP setup](https://stitch.withgoogle.com/docs/mcp/setup/) and inspect its available tools before calling them.

## ST01 Define the design task

- Capture the audience, main task, device, expected content, viewport range and acceptance criteria. Specify the relevant loading, empty, error, disabled and permission states.
- Choose new screen, reference-based generation, targeted edit or variants. For a targeted edit, identify the screen, region and requested change, and carry forward existing navigation, copy and tokens outside that scope.
- Where the brief needs exploration, compare directions against task completion, accessibility and brand fit. Turn the selected direction into a screen-level brief with concrete component and layout constraints. See [visual design exploration](visual-design.md).

## ST02 Record design decisions

- Read the existing theme, components and token definitions. When a design handoff needs a `DESIGN.md`, map color roles, typography, spacing, radius, elevation, breakpoints and motion to the project token sources. Include key component states, theme differences and exceptions.
- For extraction from code, inspect available routes, shared layouts, CSS variables, framework theme configuration and computed styles. For extraction from a preview, record the sampled route, viewport, theme and UI state. Distinguish observed values from proposals. Verify representative components across any supported themes.
- Use the project token source to resolve drift. Update that source and the handoff together when an approved change affects both. See [design system contracts](design-systems.md).

## ST03 Iterate and hand off

- For multi-page work, record the sitemap, shared navigation and backlog in `SITE.md` or the project's existing planning document. Use one page or flow per iteration with a defined target and an acceptance check.
- Record the route or screen ID, design revision, assets, open decisions, verification and next task. Track the status of each route so a retry updates the intended design or implementation.
- For code-to-design delivery, capture a representative page state and pair the static HTML or screenshot with `DESIGN.md`. Preview the export at the intended viewport and review its assets. A remote upload requires user authorization for the destination project and the material being transferred. Use representative data and remove private values from the output.

## ST04 Implement and verify

- Translate structure and behavior into the target stack. For Vue or React, map reusable visual regions to existing components, semantic HTML and tokens. For React Native, use native layout, text and touch primitives and verify safe areas and system text scaling.
- Reuse existing component libraries and inspect any imported registry dependencies. For dashboards, keep asynchronous data fetching and caching outside presentational components and verify table semantics, formatting, empty states and recovery.
- Compare the actual render to the approved design on representative devices and themes. Exercise keyboard or touch navigation, focus, form validation, contrast, reduced motion, and loading, failure and permission states where applicable. For product walkthroughs, verify timing, text legibility and exported playback. See [UI and interaction](ui-ux.md).

## Upstream skill index

Each entry links to its original implementation at the reviewed revision. Stitch-specific tool schemas and plugin setup are maintained by the upstream project. See [source and licensing](../../THIRD_PARTY_NOTICES.md#google-stitch-skills).

| Plugin | Upstream skill | Application in this skill |
| --- | --- | --- |
| stitch-build | [react-components](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-build/skills/react-components/SKILL.md) | Map screen regions to reusable React components, typed props and local tokens. Verify the rendered component and its interactions. |
| stitch-build | [react-native](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-build/skills/react-native/SKILL.md) | Map HTML intent to native views, text, scrolling and touch. Verify safe areas, dynamic type and TalkBack or VoiceOver on target devices. |
| stitch-build | [react-vite-dashboard](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-build/skills/react-vite-dashboard/SKILL.md) | Keep remote data and caching in the data layer. Define loading, empty, failure and stale data, and preserve semantic tables. |
| stitch-build | [remotion](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-build/skills/remotion/SKILL.md) | Use an approved screen sequence and frame timeline for walkthroughs. Check captions, audio sync and rendered output. |
| stitch-build | [shadcn-ui](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-build/skills/shadcn-ui/SKILL.md) | Reuse project primitives and variants. Review registry source, dependencies and keyboard behavior before adding components. |
| stitch-design | [code-to-design](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-design/skills/code-to-design/SKILL.md) | Combine a rendered snapshot and a design-system document for product design iteration. |
| stitch-design | [extract-design-md](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-design/skills/extract-design-md/SKILL.md) | Derive roles and states from frontend source or an authorized live preview. Record sampled routes and open questions. |
| stitch-design | [extract-static-html](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-design/skills/extract-static-html/SKILL.md) | Capture an explicit route, viewport and UI state with its styles and permitted assets. Open the export to verify fidelity. |
| stitch-design | [generate-design](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-design/skills/generate-design/SKILL.md) | Choose text, reference image, targeted edit or variants by intent. Supply concrete layout and state constraints. |
| stitch-design | [manage-design-system](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-design/skills/manage-design-system/SKILL.md) | Retrieve or draft a design system, map semantic roles and review the affected screens when applying it. |
| stitch-design | [upload-to-stitch](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-design/skills/upload-to-stitch/SKILL.md) | Confirm the target project, asset scope and authorization for the transfer. Record the resulting asset or screen IDs. |
| stitch-utilities | [design-md](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-utilities/skills/design-md/SKILL.md) | Record visible design rules and their mapping to project tokens in DESIGN.md. |
| stitch-utilities | [enhance-prompt](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-utilities/skills/enhance-prompt/SKILL.md) | Turn fuzzy requests into a brief with audience, task, screen structure, states and review criteria. |
| stitch-utilities | [site-md](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-utilities/skills/site-md/SKILL.md) | Record scope, page relationships, shared navigation and remaining work in SITE.md when a multi-page handoff needs it. |
| stitch-utilities | [stitch-loop](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-utilities/skills/stitch-loop/SKILL.md) | Hand off one bounded page or flow with its scope, verification results and next step. |
| stitch-utilities | [taste-design](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-utilities/skills/taste-design/SKILL.md) | Make typography, composition, accent colors and motion serve the product task and accessibility. |
