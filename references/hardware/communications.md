# Communication engineering, protocol stacks, and signal algorithms

**English** | [简体中文](../zh-CN/hardware/communications.md) | [Standards index](../translations.md)

## COM01 Layers and contracts

- Separate physical, link, network, transport, application responsibilities and state actual layers/cross-layer constraints
- Implement Ethernet, IP, TCP/UDP, TLS, HTTP/MQTT, Modbus, BACnet, SNMP, CAN against specific standard versions
- Model framing, addressing, sequencing, retries, flow/congestion control, timeout, reconnect separately
- Specify private-protocol vectors, timing, boundaries, errors rather than inferring all semantics from one successful capture

## COM02 Wired interfaces

- Specify UART levels, baud, data bits, parity, stop bits, buffering; TTL is not RS-232/RS-485
- Define RS-485 half-duplex direction, termination, bias, topology, idle detection with line-timing-based timeouts
- Handle I2C pullups, capacitance, clock stretching, address conflicts, recovery; define SPI mode, CS, bit order, frequency
- Verify CAN/CAN FD bitrate, sample points, termination, error frames, bus-off, recovery
- Follow PHY, impedance, length, reference-design requirements for USB/Ethernet high-speed links beyond generic routing experience

## COM03 Wireless and RF

- Specify band, channel/index, bandwidth, modulation, coding, transmit power, sensitivity, antenna
- Include path loss, gains, cable loss, fading/interference margins in link budgets with model/environment
- Use state machines for provisioning, joining, reconnecting, roaming, key renewal against retry storms
- Record distance, surroundings, packet size, power, instruments for RSSI, SNR, PER/BER, throughput, latency
- Apply regional regulation, bands, duty cycles, emission limits; laboratory settings are not automatically saleable configurations

## COM04 DSP and control

- Define sampling rate, bandwidth, anti-aliasing, quantization, windows, filter delay
- Verify FFT resolution, amplitude normalization, leakage, fixed-point overflow across the data chain
- Explain stability, initialization, saturation, anti-windup, discretization for filters, estimators, PID
- Provide fixed-point widths, scaling, rounding, error budgets and compare high-precision references
- Validate floating-point simulation, software/hardware-in-loop, real sensors separately rather than trusting smooth plots

## COM05 Tools and acceptance

- Build cross-layer evidence with captures, logic analyzers, oscilloscopes, spectrum analyzers, protocol analysis, error-rate statistics
- Distinguish queueing, transmission, device execution, observation time; estimate synchronization error separately
- Cover loss, duplicates, reordering, invalid checksums, power-cycle reconnect, noise, full loads
- Establish interoperability with independent implementations/certification tools rather than two copies sharing code
