#!/usr/bin/python

import argparse
import nidigital
import os
import sys
import time


def example(resource_name, options, channels, aperture_time, settling_time, current_level_range, current_level,
            voltage_limit_high, voltage_limit_low):

    with nidigital.Session(resource_name=resource_name, options=options) as session:

        dir = os.path.join(os.path.dirname(__file__), 'ppmu_source_and_measure_files')

        # Load pin map (.pinmap) created using Digital Pattern Editor
        pin_map_filename = os.path.join(dir, 'PinMap.pinmap')
        session.load_pin_map(pin_map_filename)

        # Configure PPMU measurements
        session.channels[channels].ppmu_aperture_time = aperture_time
        session.channels[channels].ppmu_aperture_time_units = nidigital.PPMUApertureTimeUnits.SECONDS

        session.channels[channels].ppmu_output_function = nidigital.PPMUOutputFunction.CURRENT

        session.channels[channels].ppmu_current_level_range = current_level_range
        session.channels[channels].ppmu_current_level = current_level
        session.channels[channels].ppmu_voltage_limit_high = voltage_limit_high
        session.channels[channels].ppmu_voltage_limit_low = voltage_limit_low

        session.channels[channels].ppmu_source()

        # Settling time between sourcing and measuring
        time.sleep(settling_time)

        current_measurements = session.channels[channels].ppmu_measure(nidigital.PPMUMeasurementType.CURRENT)
        voltage_measurements = session.channels[channels].ppmu_measure(nidigital.PPMUMeasurementType.VOLTAGE)

        pin_info = session.channels[channels].get_pin_results_pin_information()

        print('{:,<6} {:,<20} {:,<10} {:,<10}'.format('Site', 'Pin Name', 'Current', 'Voltage'))

        for pin, current, voltage in zip(pin_info, current_measurements, voltage_measurements):
            print('{:<6d} {:<20} {:<10f} {:<10f}'.format(pin.site_number, pin.pin_name, current, voltage))

        # Disconnect all channels using programmable onboard switching
        session.channels[channels].selected_function = nidigital.SelectedFunction.DISCONNECT


def _main(argsv):
    parser = argparse.ArgumentParser(description='Demonstrates how to configure and source/measure voltage/current using the PPMU on selected channels/pins of the digital pattern instrument',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2,PXI1Slot3', help='Resource name of a NI digital pattern instrument, ensure the resource name matches the instrument name in the pinmap file.')
    parser.add_argument('-s', '--simulate', default=True, type=bool, help='Whether to run on hardware or run on software simulation')
    parser.add_argument('-c', '--channels', default='DUTPin1, SystemPin1', help='Channel(s)/Pin(s) to use')
    parser.add_argument('-at', '--aperture-time', default=0.000004, type=float, help='Aperture time in seconds')
    parser.add_argument('-st', '--settling-time', default=0.01, type=float, help='Settling time in seconds')
    parser.add_argument('-clr', '--current-level-range', default=0.000002, type=float, help='Current level range in amps')
    parser.add_argument('-cl', '--current-level', default=0.000002, type=float, help='Current level in amps')
    parser.add_argument('-vlh', '--voltage-limit-high', default=3.3, type=float, help='Voltage limit high in volts')
    parser.add_argument('-vll', '--voltage-limit-low', default=0, type=float, help='Voltage limit low in volts')
    args = parser.parse_args(argsv)
    example(
        args.resource_name,
        'Simulate=1, DriverSetup=Model:6571' if args.simulate else '',
        args.channels,
        args.aperture_time,
        args.settling_time,
        args.current_level_range,
        args.current_level,
        args.voltage_limit_high,
        args.voltage_limit_low)


def main():
    _main(sys.argv[1:])


def test_main():
    _main([])


def test_example():
    resource_name = 'PXI1Slot2,PXI1Slot3'
    options = {'simulate': True, 'driver_setup': {'Model': '6571'}, }
    channels = 'DUTPin1, SystemPin1'
    aperture_time = 0.000004
    settling_time = 0.01
    current_level_range = 0.000002
    current_level = 0.000002
    voltage_limit_high = 3.3
    voltage_limit_low = 0

    example(resource_name, options, channels, aperture_time, settling_time, current_level_range, current_level,
            voltage_limit_high, voltage_limit_low)


if __name__ == '__main__':
    main()
