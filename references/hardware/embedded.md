# Embedded systems, firmware, and RTOS

**English** | [简体中文](../zh-CN/hardware/embedded.md) | [Standards index](../translations.md)

## EMB01 Platforms and boundaries

- Identify MCU/SoC, cores, board revision, clocks, memory map, peripherals, power, boot
- Separate BSP, HAL, drivers, protocols, domain state, orchestration; interfaces reflect capabilities/resource lifecycles
- Follow vendor manuals, errata, actual silicon revisions rather than assuming same-family register compatibility
- Choose RTOS/bare-metal by timing, RAM/Flash, certification, maintenance; do not blindly migrate languages/schedulers

## EMB02 Realtime and resources

- Define priorities, periods, maximum execution time, deadlines, stacks, blocking budgets per task
- Measure/analyze worst-case timing, jitter, preemption; average throughput is not hard-realtime evidence
- Acknowledge interrupts/move necessary data quickly, defer heavy work, use interrupt-safe APIs
- Bound intertask communication with drop, overwrite, blocking, failure policies rather than unbounded samples
- Explain realtime effects of allocation, logging, Flash erase, networking
- Feed watchdogs from actual health rather than perpetual loops hiding critical-task deadlock
- Observe/recover stack watermarks/overflow, handles, pools, queue high-water marks

## EMB03 Drivers and peripherals

- Follow manual widths, read-modify-write side effects, read-clear/write-one-clear, ordering
- Meet DMA memory accessibility, alignment, cache clean/invalidate, ownership-transfer requirements
- Handle UART/SPI/I2C/CAN timeouts, bus faults, reinitialization, shared-bus arbitration
- Distinguish ticks, hardware timers, RTC, monotonic time and handle wrap/low-power pauses
- Design nonvolatile endurance, power-loss atomicity, CRC, versions, dual-bank/journal strategies
- Match mux, pulls, levels, boot/debug pins to schematics rather than guessing boards from code defaults

## EMB04 Boot and upgrades

- Match startup, linker scripts, vectors, stack/heap layouts to actual binaries
- Define bootloader/application/configuration compatibility and verify image integrity/provenance
- Assess secure boot, A/B, rollback prevention, failure counters, recovery according to hardware
- Test power loss, insufficient space, broken communication, bad signatures, downgrade requests
- Inspect binary-library, startup, scheduler dependencies before rewriting; legacy C ABI dependencies do not disappear automatically

## EMB05 Board validation

- Provide reproducible power, clock, flashing, serial, peripheral checks with expected evidence
- Label frequency index, frequency, bandwidth, power, modulation separately without mixed units
- Inspect reset causes, undervoltage, temperature, long runs, communication recovery, resource levels
- Record host tests, target linking, simulation, hardware-in-loop, physical boards separately
- Without a connected board report builds/analysis only rather than RF, timing, board acceptance
