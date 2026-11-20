"""
Demonstrates how to perform common TMU measurement types using the
NI-Digital Pattern Driver API. This example shows three simple measurement
configurations:
        - Period: time between two consecutive identical events on the same channel
            (rising-edge to rising-edge)
        - Duty Cycle High: time the signal spends above a threshold on a single
            channel (rising-edge to falling-edge)
        - Skew: time difference between the same event on two different channels
            (inter-channel timing)
The TMU is not limited by these measurement configurations.

Each measurement uses Edge arm to guarantee deterministic results. To use
Immediate arm instead, remove the edge arm configuration and change the arm
type to IMMEDIATE.

Note: The DUT must be generating signals on the configured channels for TMU
measurements to complete. In simulate mode, the driver returns simulated
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
    dut_pin2 = "DUTPin2"

    # Initialize the digital pattern instrument session. The reset input is
    # TRUE to ensure the instrument starts in a known state.
    with nidigital.Session(
        RESOURCE_NAME, id_query=True, reset_device=True, options=OPTIONS
    ) as session:
        # Load the pin map for the instrument to allow referencing of pin names
        # in the channel list of select driver functions.
        session.load_pin_map(str(PIN_MAP_PATH))

        # Configure voltage levels for all channels. The VOL and VOH levels
        # define the thresholds used by the TMU for SOURCE_EVENT_VOL and
        # SOURCE_EVENT_VOH events respectively.
        session.configure_voltage_levels(0.0, 5.0, 0.5, 2.4, 0.0)

        # Select TMU0 from its instrument context.
        instrument = session.instruments[RESOURCE_NAME]
        tmu = instrument.time_measurement_units[0]

        # Enable the TMU.
        tmu.tmu_enabled = True

        # Configure sample count and timeout (shared by all measurements).
        tmu.tmu_arm_type = nidigital.enums.TMUArmType.EDGE
        tmu.tmu_samples_to_acquire = 100
        tmu.tmu_sample_timeout = 10.0

        # ===================================================================
        # Measurement 1: Period
        # ===================================================================
        # Measures the time between two consecutive identical events on the
        # same channel. Both start and stop sources are configured to the same
        # channel with the same event and polarity.
        #
        # Configuration:
        #   Start: DUTPin1, VOL threshold, Rising Edge
        #   Stop:  DUTPin1, VOL threshold, Rising Edge (same as start)
        #   Arm:   matches start/stop (Rising Edge at VOL on DUTPin1)
        #
        # The TMU captures the first rising-edge VOL crossing as the start,
        # then the next one as the stop. The difference is one full period.
        print("--- Measurement 1: Period ---")

        # Configure Edge arm.
        # Start source: DUTPin1, VOL threshold, Rising Edge.
        tmu.tmu_start_source = dut_pin1
        tmu.tmu_start_source_event = nidigital.enums.TMUSourceEvent.VOL
        tmu.tmu_start_source_event_polarity = nidigital.enums.TMUPolarity.RISING

        # Stop source: same channel, same event/polarity for Period.
        tmu.tmu_stop_source = dut_pin1
        tmu.tmu_stop_source_event = nidigital.enums.TMUSourceEvent.VOL
        tmu.tmu_stop_source_event_polarity = nidigital.enums.TMUPolarity.RISING

        # Edge arm matches start/stop.
        tmu.tmu_edge_arm_source = "DUTPin1"
        tmu.tmu_edge_arm_source_event = nidigital.enums.TMUSourceEvent.VOL
        tmu.tmu_edge_arm_polarity = nidigital.enums.TMUPolarity.RISING
        tmu.tmu_initiate()
        period_measurement = tmu.tmu_fetch_averaged_measurement(10.0)
        print(f"Period: {period_measurement:.6e} seconds")
        tmu.tmu_abort()

        # ===================================================================
        # Measurement 2: Duty Cycle High
        # ===================================================================
        # Measures the high portion of a duty cycle on a single channel. The
        # start event is the signal rising above a threshold, and the stop event
        # is the signal falling below the same threshold.
        #
        # Configuration:
        #   Start: DUTPin1, VOH threshold, Rising Edge
        #   Stop:  DUTPin1, VOH threshold, Falling Edge
        #   Arm:   matches start (Rising Edge at VOH on DUTPin1)
        #
        # The arm event guarantees the rising edge is captured first, so the
        # measurement is always the time the signal spends above VOH.
        print("\n--- Measurement 2: Duty Cycle High ---")

        # Start source: DUTPin1, VOH threshold, Rising Edge.
        tmu.tmu_start_source = dut_pin1
        tmu.tmu_start_source_event = nidigital.enums.TMUSourceEvent.VOH
        tmu.tmu_start_source_event_polarity = nidigital.enums.TMUPolarity.RISING

        # Stop source: same channel, VOH threshold, Falling Edge.
        tmu.tmu_stop_source = dut_pin1
        tmu.tmu_stop_source_event = nidigital.enums.TMUSourceEvent.VOH
        tmu.tmu_stop_source_event_polarity = nidigital.enums.TMUPolarity.FALLING
        tmu.tmu_edge_arm_source = "DUTPin1"
        tmu.tmu_edge_arm_source_event = nidigital.enums.TMUSourceEvent.VOH
        tmu.tmu_edge_arm_polarity = nidigital.enums.TMUPolarity.RISING
        tmu.tmu_initiate()
        duty_cycle_measurement = tmu.tmu_fetch_averaged_measurement(10.0)
        print(f"Duty Cycle High: {duty_cycle_measurement:.6e} seconds")
        tmu.tmu_abort()

        # ===================================================================
        # Measurement 3: Skew
        # ===================================================================
        # Measures the time difference between the same event on two different
        # channels. The start source is on one channel and the stop source is
        # on a different channel. The result represents the inter-channel
        # timing skew.
        #
        # Configuration:
        #   Start: DUTPin1, VOL threshold, Rising Edge
        #   Stop:  DUTPin2, VOL threshold, Rising Edge
        #   Arm:   matches start (Rising Edge at VOL on DUTPin1)
        #
        # The arm event on DUTPin1 guarantees the start event on DUTPin1 is
        # captured first, then the TMU waits for the corresponding event on
        # DUTPin2 as the stop.
        print("\n--- Measurement 3: Skew ---")

        # Start source: DUTPin1, VOL threshold, Rising Edge.
        tmu.tmu_start_source = dut_pin1
        tmu.tmu_start_source_event = nidigital.enums.TMUSourceEvent.VOL
        tmu.tmu_start_source_event_polarity = nidigital.enums.TMUPolarity.RISING

        # Stop source: DUTPin2 (different channel), VOL threshold, Rising Edge.
        tmu.tmu_stop_source = dut_pin2
        tmu.tmu_stop_source_event = nidigital.enums.TMUSourceEvent.VOL
        tmu.tmu_stop_source_event_polarity = nidigital.enums.TMUPolarity.RISING
        tmu.tmu_edge_arm_source = "DUTPin1"
        tmu.tmu_edge_arm_source_event = nidigital.enums.TMUSourceEvent.VOL
        tmu.tmu_edge_arm_polarity = nidigital.enums.TMUPolarity.RISING
        tmu.tmu_initiate()
        skew_measurement = tmu.tmu_fetch_averaged_measurement(10.0)
        print(f"Skew: {skew_measurement:.6e} seconds")
        tmu.tmu_abort()

        session.pins[""].selected_function = nidigital.enums.SelectedFunction.DISCONNECT


if __name__ == "__main__":
    main()
