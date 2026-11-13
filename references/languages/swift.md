# Swift

**English** | [简体中文](../zh-CN/languages/swift.md) | [Standards index](../translations.md)

Each package/directory directly owns at most 20 same-family source files, including tests, declarations, and first-party generated files. Design cohesive subpackages according to the [shared directory standards](../directory-structure.md).

- Identify Swift mode, SDK, deployment target, strict-concurrency settings; at most 380 lines per file
- Follow Swift API Design Guidelines; Chinese documentation specifies parameters, failures, isolation, lifecycle
- Prefer value semantics and explicit optional handling rather than forced unwraps hiding uncertainty
- ARC does not reclaim strong cycles; inspect closure, delegate, timer, subscription captures
- Choose weak/unowned by actual lifetimes; unowned is not an arbitrary cycle fix
- Follow version-specific Sendable, actor, main-actor isolation; unchecked annotations require proven race safety
- Own async/await tasks and cancellation paths, including cooperative checks
- Actors may reenter at await; revalidate business invariants across suspension
- SwiftUI needs stable identity, correct state owners, observable models; no unmanaged effects in body
- Follow main-thread/actor UI contracts; keep network/heavy computation off the UI
- Unregister UIKit/AppKit delegates, notifications, callbacks and handle safe areas/text scaling
- Express errors through throws/Result and UI states; cancellation is not a regular service failure
- Verify actual targets, dark mode, Dynamic Type, VoiceOver, background recovery, denied permissions

Combine [mobile](../product/mobile.md), Apple HIG, official Swift concurrency guidance.
