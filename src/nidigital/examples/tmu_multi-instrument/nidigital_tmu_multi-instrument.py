"""
Demonstrates how to use the NI-Digital Pattern Driver API to work with TMU
resources in a multi-instrument session. This example shows:
        - TMU naming conventions: each device has its own set of TMUs, and in
            multi-instrument sessions, TMU contexts are device-qualified
        - How GetDisabledTMUContexts returns device-qualified TMU context strings
            so you can identify which device each TMU belongs to
        - Using TMU resources across multiple devices in the same session
        - TMU is per-device: each device has independent TMU hardware that can be
            configured and operated separately

Note: In simulate mode, the driver returns simulated measurement values. With
real hardware, each device's TMU operates independently on its own DIO channels.
"""

from pathlib import Path

import nidigital


RESOURCE_NAMES = "PXI1Slot5,PXI1Slot6"
OPTIONS = {"Simulate": True, "DriverSetup": {"Model": "6571"}}
PIN_MAP_PATH = Path(__file__).with_name("PinMap.pinmap")


def get_tmu_contexts_per_device(session):
    """Discover available TMU contexts and return one TMU context per device."""

    # GetDisabledTMUContexts returns device-qualified TMU context strings.
    # Each TMU context includes the device resource name as a prefix, e.g.:
    # "PXI1Slot5/tmu0"
    #
    # This tells you:
    #   - Which device each TMU belongs to
    #   - How many TMUs are available per device
    #   - The full context string needed to address each TMU
    #
    # TMU is per-device: each PXIe-6570/6571 instrument has its own TMU
    # hardware. TMUs on different devices operate independently and can
    # measure different channels simultaneously.
    disabled_contexts = session.tmu_get_disabled_tmu_contexts()
    if not disabled_contexts:
        raise RuntimeError("No TMU contexts are available. Ensure the instruments support TMU.")

    print("TMU contexts in multi-instrument session (all initially disabled):")
    print(f"  {', '.join(disabled_contexts)}\n")

    # The Python API returns the driver contexts as a list of strings. Select
    # one TMU per device; join() above is used only to display that list.
    print("TMU resources per device:")
    contexts_by_device = {}
    for context in disabled_contexts:
        print(f"  {context}")
        device, _, _ = context.partition("/tmu")
        contexts_by_device.setdefault(device, context)

    if len(contexts_by_device) < 2:
        raise RuntimeError("Two instruments with available TMUs are required.")

    tmu_context1, tmu_context2 = list(contexts_by_device.values())[:2]
    print(f"Using TMU context 1: {tmu_context1}")
    print(f"Using TMU context 2: {tmu_context2}\n")
    return tmu_context1, tmu_context2


def main():
    # Multi-instrument session: specify multiple device resource names separated
    # by commas. Each device contributes its own TMU resources to the session.

    # Initialize the digital pattern instrument session with multiple devices.
    # The session aggregates all devices and their TMU resources.
    with nidigital.Session(
        RESOURCE_NAMES, id_query=True, reset_device=True, options=OPTIONS
    ) as session:
        # Load the pin map for the multi-instrument configuration. The pin map
        # defines how pins are mapped to channels across all instruments.
        session.load_pin_map(str(PIN_MAP_PATH))

        # Configure voltage levels for all channels. The VOL and VOH levels
        # define the thresholds used by the TMU for SOURCE_EVENT_VOL and
        # SOURCE_EVENT_VOH events respectively.
        session.configure_voltage_levels(0.0, 5.0, 0.5, 2.4, 0.0)

        # Discover TMU Resources.
        tmu_context1, tmu_context2 = get_tmu_contexts_per_device(session)

        # ===================================================================
        # Configure TMUs on Different Devices
        # ===================================================================
        # In a multi-instrument session, you must use device-qualified TMU
        # context strings when setting attributes and calling TMU functions.
        #
        # Here we configure one TMU on each device to perform independent
        # measurements. Each device's TMU can only measure channels connected
        # to that same device.

        # --- Device 1: Period measurement on DUTPin1 ---
        # DUTPin1 is connected to the first device's channel 0 (per the pin
        # map). We use the first TMU context from GetDisabledTMUContexts.
        print(f"--- Device 1 ({tmu_context1}): Period on DUTPin1 ---")
        device1, tmu_id1 = tmu_context1.split("/", maxsplit=1)
        tmu1 = session.instruments[device1].time_measurement_units[tmu_id1]
        tmu1.tmu_enabled = True
        tmu1.tmu_arm_type = nidigital.enums.TMUArmType.IMMEDIATE
        tmu1.tmu_start_source = "DUTPin1"
        tmu1.tmu_start_source_event = nidigital.enums.TMUSourceEvent.VOL
        tmu1.tmu_start_source_event_polarity = nidigital.enums.TMUPolarity.RISING
        tmu1.tmu_stop_source = "DUTPin1"
        tmu1.tmu_stop_source_event = nidigital.enums.TMUSourceEvent.VOL
        tmu1.tmu_stop_source_event_polarity = nidigital.enums.TMUPolarity.RISING
        tmu1.tmu_samples_to_acquire = 100
        tmu1.tmu_sample_timeout = 10.0

        # --- Device 2: Period measurement on DUTPin3 ---
        # DUTPin3 is connected to the second device's channel (per the pin map).
        # We use the second TMU context from GetDisabledTMUContexts. Each
        # device's TMU operates independently, so both measurements can be
        # configured and run in the same session.
        print(f"--- Device 2 ({tmu_context2}): Period on DUTPin3 ---")
        device2, tmu_id2 = tmu_context2.split("/", maxsplit=1)
        tmu2 = session.instruments[device2].time_measurement_units[tmu_id2]
        tmu2.tmu_enabled = True
        tmu2.tmu_arm_type = nidigital.enums.TMUArmType.IMMEDIATE
        tmu2.tmu_start_source = "DUTPin3"
        tmu2.tmu_start_source_event = nidigital.enums.TMUSourceEvent.VOL
        tmu2.tmu_start_source_event_polarity = nidigital.enums.TMUPolarity.RISING
        tmu2.tmu_stop_source = "DUTPin3"
        tmu2.tmu_stop_source_event = nidigital.enums.TMUSourceEvent.VOL
        tmu2.tmu_stop_source_event_polarity = nidigital.enums.TMUPolarity.RISING
        tmu2.tmu_samples_to_acquire = 100
        tmu2.tmu_sample_timeout = 10.0

        # This code snippet demonstrates that GetDisabledTMUContexts returns
        # only the context strings for TMUs that have not been enabled. Because
        # two TMUs have been enabled, one on each instrument,
        # GetDisabledTMUContexts returns two fewer context strings.
        #
        # Note: This call triggers attribute verification for all TMUs. If any
        # TMU has an invalid configuration, it will appear as disabled.
        print("\n--- Checking disabled TMUs after configuration ---")
        remaining_contexts = session.tmu_get_disabled_tmu_contexts()
        if remaining_contexts:
            print(f"Still disabled TMU contexts:\n  {', '.join(remaining_contexts)}")
        else:
            print("All TMUs are enabled.")

        # ===================================================================
        # Initiate and Fetch Measurements on Both Devices
        # ===================================================================
        # Each device's TMU can be initiated independently. The TMU hardware on
        # each device operates in parallel.
        print("\n--- Initiating measurements on both devices ---")

        # Initiate TMU on device 1.
        tmu1.tmu_initiate()

        # Initiate TMU on device 2.
        tmu2.tmu_initiate()

        # Fetch measurement from device 1.
        measurement1 = tmu1.tmu_fetch_averaged_measurement(10.0)
        measurement2 = tmu2.tmu_fetch_averaged_measurement(10.0)
        print(f"{tmu_context1} Period: {measurement1:.6e} seconds")

        # Fetch measurement from device 2.
        print(f"{tmu_context2} Period: {measurement2:.6e} seconds")

        # Abort both TMU acquisitions.
        tmu1.tmu_abort()
        tmu2.tmu_abort()

        # Disconnect all channels using programmable onboard switching.
        session.pins[""].selected_function = nidigital.enums.SelectedFunction.DISCONNECT


if __name__ == "__main__":
    main()
