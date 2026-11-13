# Vue, web, and cross-platform components

**English** | [简体中文](../zh-CN/languages/vue.md) | [Standards index](../translations.md)

Each package/directory directly owns at most 20 same-family source files, including tests, declarations, and first-party generated files. Design cohesive subpackages according to the [shared directory standards](../directory-structure.md).

## V01 Versions and responsibilities

- Identify Vue, Vite/Nuxt, Router, Pinia, component library, target platforms; SFCs at most 360 lines
- Prefer Composition API/script setup for new Vue 3 work; preserve required Options API without unrelated migration
- Follow actual TypeScript choices rather than rewriting JavaScript projects for small fixes
- Pages own layout/use-case coordination, components stable interactions, composables reusable state/effects
- Props flow down/events up; define props, emits, slots, two-way contracts without mutating props
- Do not split meaningless template fragments for line limits; identify state owners/component boundaries first

## V02 Reactivity and state

- Minimize source state, derive with computed, use watch for side effects rather than duplicated data
- Check version-specific destructuring of reactive/props/Pinia; use storeToRefs for state/getters when needed
- Use shallowRef for deliberately shallow objects with clear replacement policies rather than replacing every ref
- Keys represent stable identity; do not use indices for reorderable entity lists
- Avoid unjustified deep watching of large data; bound dependencies, frequency, resources
- Keep page-local state out of global stores; isolate SSR state per request against user-data leaks
- Clean requests, listeners, timers, observers, connections on navigation, unmount, parameter changes

## V03 Requests, routing, security

- Parameter changes may reuse components without remounting; reload from parameters/actual lifecycle
- Handle search/pagination races; stale responses cannot override current queries; debounce is not cancellation/version validation
- Route guards support UX while backends authorize; hidden buttons are not security controls
- Use v-html only for context-sanitized trusted contents; preserve CSP/URL validation
- Distinguish expired login, forbidden access, offline, timeout, empty, service errors
- Use browser APIs in suitable SSR lifecycles; preserve hydration consistency/server data isolation

## V04 UX and performance

- Select one primary system using [UI standards](../product/ui-ux.md) and [design systems](../product/design-systems.md)
- Preserve filters, pagination, selection, scroll; define cross-page batch scope and partial failures
- Follow library contracts for forms, dates, dialogs, uploads; centralize themes through tokens/config providers
- Assess pagination, virtualization, chunking, shallow reactivity for large lists; keep-alive alone does not fix problems
- Base route lazy loading, dependency size, image dimensions, caching on real build analysis
- Choose Nuxt SSR/SSG/CSR by first paint, SEO, permissions, deployment cost rather than universal SSR
- Uni-app/mini-programs differ from browsers; check events, permissions, privacy, subpackages, native bridges, background behavior

## V05 Verification

- Run project formatting, lint, types, production builds; test component/end-to-end behavior by risk
- Check narrow screens, long text, keyboards, loading/errors, slow networks
- Verify H5, target mini-program, Android/iOS separately; one platform does not prove all
- Check reordered requests, quick navigation, repeated clicks, permission changes, post-unmount callbacks

See [sources](../sources.md): Vue, Pinia, Vue Router, Vite, Nuxt, DCloud.
