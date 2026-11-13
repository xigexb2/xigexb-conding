# Protocols, communication, and distributed behavior

**English** | [简体中文](../zh-CN/engineering/protocols-distributed.md) | [Standards index](../translations.md)

## PD01 Wire protocols

- Read specifications, versions, message direction, reference implementations before changes; resolve conflicts among screenshots, historical code, formal documents against actual authority
- Specify every field's order, width, endianness, signedness, scaling, optional conditions, reserved values, checksum coverage
- Validate lengths before reads/allocations; bound frames, nesting, decompression ratios, batches
- TCP is a byte stream: handle partial/coalesced/multiple frames and disconnects; UDP requires loss, duplicates, ordering, MTU handling
- Checksums/CRC detect transmission errors without providing authentication/tamper resistance
- Verify codecs using known byte vectors, independent implementations, boundaries rather than self round trips alone
- Organize protocol types/constants, common frames, uplink/downlink messages by repository responsibilities without imposing fixed package names

## PD02 Commands and state

- Separate local acceptance, queue submission, transport acknowledgment, gateway acknowledgment, device reply, business completion
- Define correlation IDs, session/device ownership, deadlines, duplicate and late responses for each operation
- Unicast/multicast/broadcast have different acknowledgment capabilities; successful sending cannot establish per-device execution results
- Normalize identities according to protocol width, leading zeros, case, reserved addresses; do not truncate based on display strings
- Isolate old-session replies across disconnect/reconnect; request-table cleanup must preserve still-valid state
- Model offline, timeout, rejection, cancellation, unknown outcome separately; missing replies do not prove non-execution

## PD03 MQTT and events

- QoS 0/1/2 specifies protocol delivery rather than automatic business exactly-once
- Design publish acknowledgment, consumer processing, persistence commit, downstream side effects separately
- Bind topic ACLs to tenants/devices; configure wildcard subscriptions, retained messages, wills, session expiry for actual business needs
- Deduplicate with stable business keys rather than connection-local packet IDs alone
- Bound and audit retries, dead letters, poison messages, manual replay with error classification
- Verify framework-specific rebalance, partition ordering, batch commits for duplicates/missed processing

## PD04 Distributed coordination

- Define lock/lease holders, scope, renewal, expiry, reclamation, partition behavior
- The protected resource must validate fencing tokens; generating tokens alone does not prevent stale writers
- Idempotency requires atomic storage and request digests rather than check-then-execute races
- Do not promise arbitrary consistency and availability during partitions; define rejection, waiting, degradation by business needs
- Do not assume synchronized distributed clocks; use local monotonic time for timeouts and explicit coordination for ordering/leases
- Make recovery scans bounded/fair instead of repeatedly scanning the same prefix
- Retry at a defined layer with budgets, backoff, jitter; inquire/reconcile before retrying unknown non-idempotent operations

## PD05 HTTP, RPC, and realtime channels

- Follow HTTP RFC semantics; decide retries from methods, idempotency keys, transmitted data
- Define RPC deadlines, cancellation, status codes, message sizes, flow control, compatibility
- Handle heartbeats, reconnection, authentication expiry, backpressure, resume cursors for WebSocket/SSE
- Apply identity changes/permission revocation promptly to persistent connections, rather than checking only at connection establishment
- Explain waiting, dispatched, completed states in the UX; optimistic interfaces must not fabricate completion

See [communication engineering](../hardware/communications.md) for hardware interfaces and signal details.
