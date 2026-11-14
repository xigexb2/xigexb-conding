# Modern web performance and measurement

**English** | [简体中文](../zh-CN/web/performance.md) | [Standards index](../translations.md)

## WP01 Measure actual user experience

- Establish representative field and lab baselines for LCP, INP and CLS, segmented by page, device, network and release; use current metric definitions and report sample limitations
- Diagnose LCP by separating server response, resource discovery, load delay, transfer and render delay; locate the actual LCP element before changing priorities
- Diagnose INP by identifying the slow interaction, input delay, handler time, presentation delay, long tasks and layout/render work; verify improvements on representative devices
- Diagnose CLS using layout-shift attribution; reserve media/embed space, handle dynamically inserted content and font fallback metrics, and account for legitimate interaction exclusions

## WP02 Loading and rendering

- Make important initial content and the LCP resource discoverable early; avoid lazy-loading the actual LCP image and reserve image/video dimensions
- Use responsive images, modern formats, compression and caching according to content and target devices; test visual quality, CPU, bytes and accessibility
- Limit `fetchpriority="high"`, preload, preconnect and prefetch to demonstrably important resources; over-prioritization and speculative fetching can cause contention or privacy costs
- Use `defer`, module scripts or `async` according to ordering needs; avoid blocking parsing and unnecessary third-party work. Inline critical CSS only when measured benefits outweigh cache/CSP/maintenance costs
- Defer genuinely off-screen work and use `content-visibility` with suitable intrinsic sizing when supported; verify find-in-page, accessibility and layout stability
- Cache assets with appropriate cache-control and versioning; test stale content, rollback and CDN behavior instead of blindly caching personalized responses

## WP03 Scheduling and observability

- Break up long main-thread tasks at safe boundaries; evaluate `scheduler.yield()`, priority APIs, workers or compatible fallbacks without assuming cancellation or ordering semantics
- Batch DOM reads and writes; remove excessive JavaScript and rerendering before adding complex caching or animation machinery
- Deprioritize noncritical network and background work, bound concurrency, and avoid downloading data for unrequested features
- Collect performance telemetry only with appropriate authorization, privacy controls, sampling and data minimization; do not send URLs, identifiers or user input unnecessarily
- Prefer measured outcomes over blanket bans on libraries or automatic polyfills; verify load, interaction, error and accessibility regressions

## WP04 Verification

Use browser performance tools and real-user measurements where authorized; compare baseline and changes under representative devices, network conditions and user flows. The [upstream catalog](catalog.md) links individual LCP, INP, CLS, scheduling, images and navigation guides.

Adapted from [GoogleChrome Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/SKILL.md) and the linked catalog; changes integrate project constraints and compatibility/security review. Guide content is [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); extension reference material follows upstream Apache-2.0. See [notices](../../THIRD_PARTY_NOTICES.md).
