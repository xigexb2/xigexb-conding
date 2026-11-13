# Analog, mixed-signal, and RF IC design

**English** | [简体中文](../zh-CN/hardware/analog-ic.md) | [Standards index](../translations.md)

Apply separately from [digital RTL](chip-design.md) and [board circuits](electronics-pcb.md). This chapter defines design/evidence requirements rather than replacing PDKs, device models, process rules, restricted IP.

## AIC01 Specifications and process

- Specify supplies, I/O ranges, bandwidth, accuracy, noise, linearity, power, area, load, temperature
- Establish system error/noise budgets before allocating them to front ends, references, amplification, conversion, digital calibration
- Verify PDK, device options, model versions, operating ratings, reliability, layout rules; generic SPICE models cannot replace sign-off models
- Distinguish typical/worst-case/yield/calibrated specifications and define measurement bandwidth/conditions

## AIC02 Circuit implementation

- Verify bias/reference startup, sequencing, supply variation, drift, loading, low-power states
- Check amplifier I/O swing, common mode, gain, stability, slew, noise, distortion, load range
- Analyze feedback stability at applicable operating points rather than one typical-load phase margin for every condition
- Define ADC/DAC sampling, quantization, reference, jitter, INL/DNL, SNR/SNDR, ENOB, bandwidth measurement
- Assess phase noise, jitter, lock, spurs, matching, parasitics for PLL/clock/RF blocks with specification-matched simulation
- Handle mixed-signal levels, supply domains, isolation, digital switching noise, coupling to sensitive analog nodes
- Bound fixed-point calibration/digital compensation, convergence, storage, failure, uncalibratable cases

## AIC03 Simulation and statistics

- Choose DC, AC, transient, noise, periodic-steady-state analyses from circuits/specifications instead of requiring every tool command
- Define a matrix of PVT corners, supply, temperature, load, startup states
- Distinguish global process variation/device mismatch in Monte Carlo and report sample counts, seeds, failure definitions, confidence ranges
- Typical-corner success does not prove yield; zero failures in finite samples does not mean zero defects
- Trace models, simulators, tolerances, initial conditions, convergence warnings, scripts; address conclusion-relevant warnings

## AIC04 Layout and reliability

- Consider gradients, orientation, proximity, dummies, connection parasitics for matching; common-centroid is not universal
- Analyze parasitics, shielding, isolation, returns for supplies, ground, references, sensitive nodes according to process/frequency
- Complete DRC/LVS and necessary extraction; cover critical/worst-case performance in post-layout simulation
- Check EM, IR, ESD, latch-up, stress, aging under process rules; distinguish analysis from certification
- Review analog, digital, power, packaging together; bare-die simulation is not finished-product performance

## AIC05 Measurement and delivery

- Test plans include instrument capability, calibration, fixtures, parasitics, probes, temperature, uncertainty
- Distinguish pre-layout/post-layout, wafer, packaged-part, board results and map specifications to evidence
- Validate extraction, calibration, binning, production tests against actual yield/failures rather than one sample
- Without PDKs, sign-off tools, real devices, report general constraints/missing conditions instead of fabricated tape-out guarantees
