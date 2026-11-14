# Modern web security and privacy

**English** | [简体中文](../zh-CN/web/security.md) | [Standards index](../translations.md)

## WS01 Browser trust boundaries

- Prefer `textContent` for plain untrusted text; if accepting markup, use a maintained context-appropriate sanitizer and validate URL schemes and attributes
- Enforce an appropriate CSP and consider Trusted Types for supported clients as defense in depth; an identity or permissive policy does not sanitize input, and unsupported browsers still need secure output handling
- Compare parsed origins by scheme, host and effective port; validate `postMessage` sender origin, source, data schema and intended recipient. Avoid wildcard destinations for sensitive messages
- Limit third-party scripts, network destinations, frames and referrers according to real need. Evaluate Subresource Integrity for compatible static third-party resources, including CORS and update workflows
- Request browser permissions at the point of need, explain purpose and denial behavior, restrict scope, and avoid logging or persisting sensitive data unnecessarily

## WS02 Authentication and privacy

- For passkeys/WebAuthn, use server-generated one-time challenges, validate origin, RP ID, signature, credential and replay/counter rules according to the actual specification and deployment; define registration, recovery and revocation
- Do not treat passkey or federated identity selection as authorization for unrelated resources; tenant and object permissions remain enforced on the server
- Verify email ownership through a time-limited, single-use, purpose-bound channel; do not treat syntactically valid addresses as proof of control
- Apply secure cookie attributes, CSRF protections, privacy-preserving analytics, retention rules and opt-in/consent requirements applicable to the product
- Treat browser-local encryption and WebCrypto as tools within a documented threat model; client-delivered code and keys do not protect against every compromised-origin or malicious-client scenario

## WS03 Compatibility and verification

Experimental controls such as new connection policies and local-network access vary across browsers and versions; assess secure context, permission, feature detection and fallback before use. Test XSS payloads, CSP reporting/enforcement, cross-origin messages, authentication rejection, privacy settings and supported browsers. See the [upstream catalog](catalog.md).

Adapted from [GoogleChrome Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/SKILL.md) and the linked catalog; changes integrate project constraints and compatibility/security review. Guide content is [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); extension reference material follows upstream Apache-2.0. See [notices](../../THIRD_PARTY_NOTICES.md).
