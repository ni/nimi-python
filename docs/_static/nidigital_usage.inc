Usage
------

The following is a basic example of using the **nidigital** module to open a session to a digital pattern instrument,
source current, and measure both voltage and current using the PPMU on selected channels.

.. code-block:: python

    import nidigital
    import time

    with nidigital.Session(resource_name='PXI1Slot2') as session:

        channels = 'PXI1Slot2/0,PXI1Slot2/1'

        # Configure PPMU measurements
        session.channels[channels].ppmu_aperture_time = 0.000004
        session.channels[channels].ppmu_aperture_time_units = nidigital.PPMUApertureTimeUnits.SECONDS

        session.channels[channels].ppmu_output_function = nidigital.PPMUOutputFunction.CURRENT

        session.channels[channels].ppmu_current_level_range = 0.000002
        session.channels[channels].ppmu_current_level = 0.000002
        session.channels[channels].ppmu_voltage_limit_high = 3.3
        session.channels[channels].ppmu_voltage_limit_low = 0

        # Sourcing
        session.channels[channels].ppmu_source()

        # Settling time between sourcing and measuring
        time.sleep(0.01)

        # Measuring
        current_measurements = session.channels[channels].ppmu_measure(nidigital.PPMUMeasurementType.CURRENT)
        voltage_measurements = session.channels[channels].ppmu_measure(nidigital.PPMUMeasurementType.VOLTAGE)

        print('{:<20} {:<10} {:<10}'.format('Channel Name', 'Current', 'Voltage'))
        for channel, current, voltage in zip(channels.split(','), current_measurements, voltage_measurements):
            print('{:<20} {:<10f} {:<10f}'.format(channel, current, voltage))

        # Disconnect all channels using programmable onboard switching
        session.channels[channels].selected_function = nidigital.SelectedFunction.DISCONNECT

Additional examples for NI-Digital Pattern Driver are located in src/nidigital/examples/ directory `on GitHub <https://github.com/ni/nimi-python/tree/master/src/nidigital/examples>`_.

