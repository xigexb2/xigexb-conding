# Digital chips, RTL, FPGA, and verification

**English** | [简体中文](../zh-CN/hardware/chip-design.md) | [Standards index](../translations.md)

An HDL/RTL engineering framework. See [analog ICs](analog-ic.md) for analog/mixed-signal work; process, PDK, packaging, certification require actual specialist resources rather than being inferred from software rules.

## IC01 Specifications and microarchitecture

- Define functionality, interfaces, registers, throughput, latency, clocks, power domains, area, power targets
- Specify reset, backpressure, concurrency, exceptions, invalid input, error reporting, observable state
- Use legally obtained versioned ISA/bus/peripheral specifications such as RISC-V, AMBA AXI/APB
- Separate datapath, control, registers, domain crossing; provide cycle-level interface contracts
- Specify register read/write side effects, reserved bits, atomic updates, hardware/software access races

## IC02 RTL coding

- Follow actual Verilog/SystemVerilog/VHDL simulator/synthesis/formal support; maintained files default to at most 380 lines
- Separate sequential/combinational logic with appropriate always_ff/always_comb or equivalents
- Make assignment semantics, widths, signedness, truncation, extension, priority explicit
- Cover all combinational paths against unintended latches and define sequential reset policy
- Preserve required ready/valid data/control during backpressure against lost/duplicated transfers and combinational loops
- Validate parameter ranges, zero widths, boundaries, configurations beyond defaults
- Distinguish X/Z, initialization, don't-care simulation/synthesis semantics without hiding actual uncertainty

## IC03 Clocks, resets, low power

- Select synchronizers, handshakes, async FIFOs according to single/multibit, pulse, counter, stream crossings
- Do not synchronize multibit buses merely bit-by-bit with two flops; digital simulation does not remove metastability risks
- Verify RDC, async-reset release, clock gating, reset sequence through appropriate tools/process methods
- Specifically review async FIFO pointer encoding, crossing, full/empty, reset, constraints
- Define clock/power domains, isolation, retention, sequencing in applicable low-power intent

## IC04 Verification

- Trace requirements to tests/assertions with reference models, scoreboards, coverage plans, reproducible seeds
- Direct tests at boundaries, invalid inputs, reset, backpressure, timeouts, simultaneous events, recovery
- Define formal/SVA assumptions, assertions, reachability, bounds against vacuous overconstraint
- Functional/code/assertion coverage has limits; high coverage does not prove complete specifications
- Lint, CDC/RDC, simulation, formal, synthesis, STA are separate evidence
- Record FPGA bitstream, clocks, pins, voltage, board revision, actual I/O results

## IC05 Implementation and sign-off

- Include clocks, I/O delays, false/multicycle paths and justify/review every exception
- Check setup/hold, uncertainty, modes, PVT corners in STA rather than one typical corner
- Assess area, dynamic/static power, congestion, routing, heat; reverify behavior/constraints after optimization
- ASIC DRC/LVS, equivalence, IR drop, EM, DFT, manufacturing sign-off require actual workflow/tool evidence
- List incomplete sign-off explicitly; simulation/FPGA demonstrations are not tape-out guarantees
- Keep PDKs, netlists, customer IP, restricted standards out of the public skill
