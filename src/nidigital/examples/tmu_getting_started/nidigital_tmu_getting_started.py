"""
Demonstrates the minimal workflow to configure and perform a Time
Measurement Unit (TMU) measurement using the NI-Digital Pattern Driver API.
This example walks through every required step:
    1. Initialize the instrument session
    2. Load a pin map
    3. Configure voltage levels (VOL/VOH define TMU thresholds)
    4. Select a TMU from its instrument context
    5. Enable the TMU
    6. Configure a period measurement with Immediate arm
    7. Initiate the TMU acquisition
    8. Fetch the averaged measurement
    9. Abort the TMU and clean up

This is the simplest possible TMU example. For arm type comparison,
multi-measurement workflows, debounce filtering, or multi-instrument sessions,
see the other TMU examples.

Note: The DUT must be generating signals on the configured channel for the TMU
measurement to complete. In simulate mode, the driver returns simulated
measurement values.
"""

from pathlib import Path

import nidigital


RESOURCE_NAME = "PXI1Slot5"
OPTIONS = {"Simulate": True, "DriverSetup": {"Model": "6571"}}
PIN_MAP_PATH = Path(__file__).with_name("PinMap.pinmap")


def main():
    # Initial Device Values
    dut_pin1 = "DUTPin1"

    # Step 1: Initialize the digital pattern instrument session. The reset
    # input is TRUE to ensure the instrument starts in a known state. All
    # channels are in a high-impedance state, and the I/O switches are open.
    with nidigital.Session(
        RESOURCE_NAME, id_query=True, reset_device=True, options=OPTIONS
    ) as session:
        # Step 2: Load the pin map. This allows referencing pin names (e.g.,
        # "DUTPin1") in the channel list of driver functions instead of raw
        # channel numbers.
        session.load_pin_map(str(PIN_MAP_PATH))

        # Step 3: Configure voltage levels for all channels. The VOL and VOH
        # levels define the thresholds used by the TMU for SOURCE_EVENT_VOL and
        # SOURCE_EVENT_VOH events respectively.
        session.configure_voltage_levels(0.0, 5.0, 0.5, 2.4, 0.0)

        # Step 4: Select TMU0 from its instrument context. This constructs the
        # fully qualified driver context PXI1Slot5/tmu0.
        instrument = session.instruments[RESOURCE_NAME]
        tmu = instrument.time_measurement_units[0]

        # Step 5: Enable the TMU. TMUs are disabled by default and must be
        # explicitly enabled before use.
        tmu.tmu_enabled = True

        # Step 6: Configure a period measurement with Immediate arm.
        #
        # Arm Type: Immediate means the TMU begins looking for start/stop events
        # as soon as tmu_initiate is called. No explicit arm event is required.
        #
        # Period measurement: Both start and stop sources are set to the same
        # channel with the same event and polarity. This example measures the
        # time between two consecutive rising-edge VOL threshold crossings,
        # which is the signal period.
        tmu.tmu_arm_type = nidigital.enums.TMUArmType.IMMEDIATE

        # Start source: DUTPin1, VOL threshold, Rising Edge
        tmu.tmu_start_source = dut_pin1
        tmu.tmu_start_source_event = nidigital.enums.TMUSourceEvent.VOL
        tmu.tmu_start_source_event_polarity = nidigital.enums.TMUPolarity.RISING

        # Stop source: same channel, same event, same polarity (period)
        tmu.tmu_stop_source = dut_pin1
        tmu.tmu_stop_source_event = nidigital.enums.TMUSourceEvent.VOL
        tmu.tmu_stop_source_event_polarity = nidigital.enums.TMUPolarity.RISING

        # Configure the number of samples to acquire and average. A higher
        # sample count produces a more stable averaged measurement but takes
        # longer to complete.
        tmu.tmu_samples_to_acquire = 100

        # Configure the per-sample timeout. If a single sample is not acquired
        # within this time, the measurement fails.
        tmu.tmu_sample_timeout = 10.0

        # Step 7: Initiate the TMU acquisition (non-blocking). The TMU begins
        # looking for start/stop events immediately.
        tmu.tmu_initiate()

        # Step 8: Fetch the averaged measurement. This blocks until all
        # configured samples have been acquired and averaged, or the timeout
        # elapses. The result is in seconds.
        period = tmu.tmu_fetch_averaged_measurement(10.0)
        print(f"Period measurement: {period:.6e} seconds")

        # Step 9: Abort the TMU acquisition and clean up.
        tmu.tmu_abort()

        # Disconnect all channels using programmable onboard switching.
        session.pins[""].selected_function = nidigital.enums.SelectedFunction.DISCONNECT


if __name__ == "__main__":
    main()
