# Browser extensions and Chrome Manifest V3

**English** | [简体中文](../zh-CN/web/extensions.md) | [Standards index](../translations.md)

## WX01 Manifest, permissions, and distribution

- Confirm the target browser/version and current Manifest V3 contracts; define only needed API permissions and narrowly scoped host access, using optional permissions or `activeTab` where they satisfy the actual interaction
- Verify effective `activeTab`, host permissions and `tabs` access for the exact API, context, gesture, browser version and target URL; avoid claiming that one permission always covers every access path
- Manifest paths, popup, icons, side panel, options, DevTools and service-worker assets must exist and match actual packaging; verify browser API feature/version support
- Prepare store listing, privacy policy, data-use disclosure, permission justifications, screenshots and review information from actual behavior; publishing and external communication require the applicable task authorization

## WX02 Service workers and state

- Register event listeners at top level and assume extension service workers can stop/restart; persist state needed across events and choose local, session, sync or IndexedDB according to lifecycle, quota and sensitivity
- Concurrent read-modify-write operations require deliberate serialization or transactional storage; writing to `chrome.storage` alone does not make compound updates atomic
- Use alarms for work that must survive worker suspension, while treating delivery timing as non-exact; ensure handlers are idempotent and recover after restart
- Separate background, popup, options, side panel, content scripts and page contexts; validate message sender, origin, schema, permissions and error/timeout behavior

## WX03 Injection and safety

- Apply the actual extension CSP and Manifest V3 remote-code restrictions; do not weaken CSP, use `eval`, or treat Blob/srcdoc as a general CSP bypass
- If untrusted execution is truly required, design a permitted sandbox with minimal capabilities, constrained messaging, validated sources and an explicit threat model; do not copy unsafe wildcard examples
- Minimize injected code, host scope and accessible data; respect isolated/main-world differences and avoid leaving listeners or scripts active after teardown
- Side-panel opening and action-click behavior depend on manifest configuration, popup presence, user gesture and API availability; verify the exact target browser rather than assuming every combination works
- Handle authentication redirect URIs, extension IDs, development/store registration and credential storage according to the actual provider and Chrome documentation

## WX04 Verification

Load the unpacked extension in supported browsers and test service-worker suspension/restart, permission grant/revocation, popup/side-panel entry, message validation, CSP, storage concurrency, upgrades and removal. Use the [upstream catalog](catalog.md) for all extension topics.

Adapted from [GoogleChrome Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/chrome-extensions/SKILL.md) and the linked catalog; changes integrate project constraints and compatibility/security review. Guide content is [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); extension reference material follows upstream Apache-2.0. See [notices](../../THIRD_PARTY_NOTICES.md).
