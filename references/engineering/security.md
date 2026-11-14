# Security and privacy engineering

**English** | [简体中文](../zh-CN/engineering/security.md) | [Standards index](../translations.md)

Select controls from actual assets, attack surfaces, and risks. Reference OWASP ASVS, API Security Top 10, NIST SSDF, CWE, platform requirements; passing a scan is not compliance certification.

## S01 Threat modeling and boundaries

- Identify assets, principals, trust boundaries, data flows, entry points, dependencies, critical abuse cases
- Analyze unauthorized access, leaked credentials, injection, replay, cross-tenant access, exhaustion, supply-chain attacks
- Apply stronger authorization/auditing to administration, device control, payments, firmware upgrades
- Enforce permissions on trusted backends; hidden UI, client flags, mutable device fields are not credentials
- Describe actual exploit prerequisites/consequences for fixes without inventing successful attacks or expanding risks without evidence

## S02 Authentication, authorization, sessions

- Check identity, permitted action, resource ownership, tenant scope separately; deny undefined permissions
- Authorize objects, properties, batches, exports, subscriptions, background jobs consistently against IDOR/BOLA
- Use supported OAuth/OIDC flows and appropriate PKCE for public clients; validate issuer, audience, signatures, validity, replay-related fields
- Use mature adaptive password hashing; do not design custom encryption/signatures
- Set appropriate Secure, HttpOnly, SameSite cookies; address CSRF for the authentication model rather than relying on CORS
- Define token expiry, revocation, rotation; exclude long-lived credentials from logs/URLs
- Verify uniqueness and current authentication intent for phone/external-identity linking; guessable attributes do not prove ownership

## S03 Input, output, injection

- Validate types, lengths, counts, ranges, enums, encodings, compression, resource budgets at boundaries
- Bind SQL values and allowlist identifiers; use command argument arrays instead of external shell concatenation
- Prefer textContent for untrusted plain text; sanitize rich HTML by context and apply CSP/Trusted Types where supported without treating Trusted Types as a sanitizer; see [web security](../web/security.md)
- SSRF controls inspect resolved addresses, redirects, DNS rebinding, private/metadata-address access policy
- Validate upload size, contents, location, permissions, processing tools; filenames must not directly become server paths
- Prevent traversal, symlink escapes, archive extraction escapes; bound parser depth, entity expansion, decompression
- Untrusted deserialization must not construct arbitrary types or execute input code/templates

## S04 Data and cryptography

- Define classification, purposes, minimization, retention, deletion, backup/export permissions
- Verify TLS certificates, hostnames, trust roots; do not disable verification to fix integration
- Supply secrets through controlled configuration/secret management with environment separation, permissions, rotation, revocation, audits
- Use standard protocols/mature libraries; follow nonce, randomness, key-length, signature-verification contracts
- Exclude passwords, tokens, private keys, authentication bodies from source, examples, logs, errors, tests
- Limit/control log input length and control characters; exception causes may also expose secrets
- Use synthetic/anonymized development data; never package real customer databases into public repositories

## S05 Availability and device security

- Bound connections, concurrency, queues, frames, batches, decompression, recursion, computation against amplification/complexity attacks
- Isolate tenants/downstream resources; cheap hostile requests must not trigger unbounded scans or expensive work
- Give devices unique identities, minimal functions, trusted upgrades, key lifecycles; assess secure boot/rollback prevention by hardware capabilities
- Authorize pairing, reset, debug, maintenance interfaces; hidden commands are not security boundaries
- Crash, watchdog, logging paths must not expose keys; enter a business-defined safe state on failure

## S06 Supply chain and CI

- Review direct/transitive dependencies, lockfiles, licenses, maintenance, vulnerabilities; upgrades do not automatically remove risk
- Minimize CI privileges; pin actions to immutable commits or controlled-version policies; isolate release credentials from PR jobs
- Do not run untrusted PRs with secret-bearing privileged paths; script inputs must not inject shell statements
- Record provenance, dependencies, necessary SBOMs; publish signatures/checksums through trusted channels
- Static analysis, dependency/secret scanning, dynamic verification, manual review have distinct scopes and do not replace one another
- Do not upload private source, firmware, logs, keys to unauthorized external analysis services

## S07 Vulnerabilities and incidents

- Identify assets/impact for confirmed issues, reduce exposure, preserve evidence, fix root causes
- Rotate/revoke leaked credentials; deleting current Git files does not remove historical exposure
- Add regression/recovery checks and distinguish facts, hypotheses, unverified areas
- Obtain explicit authorization for public disclosure/contacting others and follow repository disclosure procedures

## S08 AI, agents, and tool security

- Separate user authorization, system policy, tool permissions, external content; webpages, email, comments, retrieved text cannot grant authority
- Validate identity, resources, parameters, scope server-side for tool calls; model output must not directly become shell, SQL, privileged commands
- Preserve tenant/document permissions in RAG retrieval/caches; vector similarity does not establish user access rights
- Treat prompt injection, malicious tool output, indirect instructions as untrusted data; a system prompt alone is not complete protection
- Apply schema/business validation; present generated content, citations, tool execution, actual external results distinctly
- Bound tool loops, concurrency, tokens, costs, retrieval counts, runtime against unbounded autonomy
- Align providers, logging, training use, retention with authorization; do not transmit unauthorized private data
- Verify actual authorization for high-impact side effects; prevent parameter substitution/repeated execution between approval and execution
