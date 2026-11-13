# Circuits, schematics, PCB, and hardware delivery

**English** | [简体中文](../zh-CN/hardware/electronics-pcb.md) | [Standards index](../translations.md)

This chapter provides design/review methods alongside device datasheets, product standards, manufacturing constraints, actual measurements.

## HW01 Requirements and components

- Specify input ranges, power, loads, environment, dimensions, interfaces, reliability, cost, manufacturability
- Establish power/clock trees, interface/system diagrams with interface voltage, current, direction, protection
- Check ratings/absolute maxima, thermal derating, tolerance, lifecycle, alternatives, supply chain
- Match datasheets, reference designs, errata to actual packages/orderable parts rather than symbol names alone
- BOMs include manufacturer numbers, parameters, packages, substitution constraints, assembly variants

## HW02 Schematics

- Design appropriate reverse-polarity, surge, overcurrent, ESD, undervoltage protection from actual operating calculations
- Check LDO/switching stability, dropout, ripple, inductor saturation, loops, transients, thermal budgets
- Follow reset, boot-pin, crystal, debug/programming recommendations and retain needed test points
- Configure pullups/pulldowns, open-drain, level shifts, unused pins by datasheets against floating/back-powering
- Specify reference, input range, bias, bandwidth, noise, protection for ADC/DAC, sensors, front ends
- Define connector keying, pinouts, shielding, grounding; consider hotplug/failure propagation
- Calculate creepage, clearance, isolation, safety levels from voltage, environment, applicable standards rather than universal numbers
- Resolve ERC warnings with documented waivers rather than blanket suppression

## HW03 PCB and signal integrity

- Establish stackup, reference planes, impedance, thickness, copper, drills, fabrication capabilities first
- Preserve critical return continuity and avoid high-speed plane splits; control loops by actual spectra
- Place decoupling near power pins with optimized loops and device/frequency-appropriate capacitance
- Budget differential routing, length, impedance, vias, termination from interfaces/simulation rather than matching every trace
- Manage coupling around switching nodes, sensitive analog/RF/crystal circuits, high-di/dt loops
- Decide analog/digital grounding from returns/devices/reference designs rather than mechanically splitting grounds
- Verify current, drops, temperature rise, cooling with calculations/measurement beyond experience tables
- Adjust RF feeds, matching, antenna clearance, enclosure effects using reference designs/measurement
- Use actual manufacturer DRC rules and document each waiver's location, reason, review

## HW04 Manufacturing, tests, versions

- Verify symbols, footprints, pin numbers, polarity, courtyards, 3D/mechanical interference
- Keep Gerber/ODB++, drills, stackup, BOM, placement, assembly drawings consistent and generate authorized deliverables
- Trace board revisions, assembly variants, firmware, calibration, serial numbers
- Include spacing, solderability, test points, fixtures, programming, rework in DFM/DFA/DFT
- Bring up first boards in order: current-limited power, rails/clocks/reset, programming, interfaces, full load
- Test thermal, EMC/ESD, environment, lifetime by product requirements; ERC/DRC does not establish those results
- Record instruments, probing, bandwidth, calibration, environment, loads and measurement-induced effects

## HW05 Tools and standards

- Preserve native KiCad/Altium formats/versions and review library/footprint changes
- State SPICE models, tolerances, conditions, limitations; typical success does not prove worst-case behavior
- Obtain applicable IPC/IEC/IEEE editions; do not invent paid-standard clauses/certification without access
