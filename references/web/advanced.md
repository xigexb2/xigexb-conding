# Progressive web apps and emerging browser capabilities

**English** | [简体中文](../zh-CN/web/advanced.md) | [Standards index](../translations.md)

## WA01 Progressive web apps

- Design manifest identity, scope, start URL, icons and installation behavior for supported browsers; installation must remain a user-controlled browser action
- Service-worker lifecycle, cache versioning, update activation, offline fallback, authentication and logout require explicit strategies; never cache sensitive tenant data without correct isolation
- Browser-specific installation APIs, install prompts and origin migration mechanisms have version-specific support; test feature detection, restrictions, user consent and ordinary browser fallback
- Review origin migration, deep links, service-worker scope, data transfer, rollback and identity before moving an installed application

## WA02 Local AI and browser agent tools

- Treat built-in language models, translation, summarization, language detection and WebMCP as evolving browser capabilities; check secure context, availability, quotas, model download, permissions and user settings on each target
- Do not enable origin trials, flags or preview dependencies without explicit project authorization; handle unavailable or failed capabilities without sending private data to another provider by default
- For client-side browser tools define narrow actions, typed schemas, lifecycle registration/cleanup, validation, authorization and explicit confirmation for consequential side effects; server APIs remain authoritative
- Distinguish generated content, actual tool execution and external results; account for stale UI state, prompt injection, resource limits and cancellation

## WA03 WebAssembly and graphics

- Choose WebAssembly, workers, WebGL or related graphics APIs only for measured workloads; validate supported runtime, CSP, memory limits, asset delivery, cleanup and fallback
- C/C++ compiled to WebAssembly still requires safe native memory, bounds, ABI, ownership and dependency review; sandboxing does not replace source correctness
- Canvas, custom drawing and advanced 3D effects need accessible semantic alternatives, keyboard interaction and real-device performance testing

## WA04 Validation

Check offline and update flows, scope, privacy, browser/runtime versions, permission rejection, unsupported features, resource limits, accessibility and fallback. The [upstream catalog](catalog.md) identifies PWA, AI, WebMCP, graphics and WASM guides.

Adapted from [GoogleChrome Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/SKILL.md) and the linked catalog; changes integrate project constraints and compatibility/security review. Guide content is [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); extension reference material follows upstream Apache-2.0. See [notices](../../THIRD_PARTY_NOTICES.md).
