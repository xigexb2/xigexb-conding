# iOS, Android, native, hybrid, and mini-program apps

**English** | [简体中文](../zh-CN/product/mobile.md) | [Standards index](../translations.md)

## M01 Platform selection and contracts

- Choose Swift/Kotlin, Flutter, React Native, Uni-app, WebView, mini-programs by capability, performance, team, distribution
- Share domain logic/data contracts without forcing every interaction to be shared; respect platform navigation, permissions, lifecycles
- Identify minimum OS, devices, SDK, build, store/privacy requirements and compatibility matrices before changes
- Code reuse percentages do not replace startup, memory, scrolling, native-capability, maintenance measurements

## M02 Apple platforms

- Follow HIG navigation, hierarchy, controls, safe areas, back gestures, platform expectations
- Generally design iOS touch targets at least 44 by 44 pt per platform guidance rather than CSS px
- Use semantic colors, system text styles, Dynamic Type, VoiceOver, appropriate SF Symbols with license/version checks
- Verify text scaling, orientation, split views within supported product scope beyond one fixed screenshot
- Respect SwiftUI state/identity/actors and UIKit lifecycles; keep networking/heavy computation off main threads
- Adapt dark mode, reduced motion, contrast/transparency accessibility settings
- Request ATT, location, camera, photos, notifications by actual needs/platform rules before collecting data

## M03 Android and Material

- Use semantic Material colors/states; choose dynamic-color behavior and fallbacks by product/system support
- Generally provide at least 48 by 48 dp targets, allowing different visible-icon/hit-area dimensions
- Handle target-version edge-to-edge, system bars, IME insets, gestures, predictive back
- Adapt phone/tablet/foldable layouts and bars/rails by window size/task
- Collect state lifecycle-aware and persist/reconstruct after process death/background restoration
- Choose WorkManager/foreground services appropriately without bypassing battery/permission restrictions
- Check TalkBack, font scaling, dark mode, touch, keyboards beyond rounded/color appearance

## M04 Cross-platform, hybrid, WebView

- Identify JS/native, Dart/native, platform-channel async/threading/serialization/error boundaries
- Allowlist bridge operations, origins, parameters; do not expose arbitrary files, commands, reflection
- Control WebView navigation, external URLs, file access, JS interfaces, certificates, mixed content instead of enabling all
- Clean subscriptions/pending calls across backgrounding, destruction, remounting, bridge reconnect
- Validate memory, permissions, cleanup of scrolling, cameras, Bluetooth, serial, location on real devices
- Version offline bundles/hot updates against native compatibility and distribution/signature rules
- Native permission success does not prove synchronized Web state; confirm callbacks/restoration

## M05 Mini-programs and external login

- Follow official login-code purpose, lifetime, server exchange, identity-linking contracts
- Validate authorization intent/uniqueness when linking phones/external IDs to existing accounts; do not default to registration/merging
- Keep privacy declarations aligned with API use and distinguish denied authorization, user refusal, missing configuration
- Use platform tools for package/subpackage, plugin, background, review checks; static checks do not replace IDE quality scans
- Mini-program, website QR, native-SDK login are distinct capabilities

## M06 Weak networks, upgrades, data

- Diagnose network switching, DNS, proxies, certificates, redirects, CDNs, platform policies separately rather than guessing by phone brand
- Separate manifest requests, version parsing, download, verification, installation, rollback
- Trust update metadata/artifacts through signatures or reliable trust chains; mutable same-origin checksums alone are insufficient
- Define resume, insufficient space, cancellation, backgrounding, repeated clicks; confirm installation through platform results
- Align local migrations, credential storage, backups, uninstall policies with platform security

## M07 Acceptance matrix

Cover target OS versions, representative real devices, denied permissions, weak/offline networks, foreground/background, process recreation, themes, font scaling, screen readers, deep links, upgrades. State simulator/single-device validation scope.
