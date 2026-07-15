#!/usr/bin/python

import argparse
import nidigital
import os
import pytest
import sys
import time


def example(resource_name, options, channels, measure, aperture_time,
            source=None, settling_time=None, current_level_range=None, current_level=None,
            voltage_limit_high=None, voltage_limit_low=None, current_limit_range=None, voltage_level=None):

    with nidigital.Session(resource_name=resource_name, options=options) as session:

        dir = os.path.join(os.path.dirname(__file__))

        # Load pin map (.pinmap) created using Digital Pattern Editor
        pin_map_filename = os.path.join(dir, 'PinMap.pinmap')
        session.load_pin_map(pin_map_filename)

        # Configure the PPMU measurement aperture time
        session.channels[channels].ppmu_aperture_time = aperture_time
        session.channels[channels].ppmu_aperture_time_units = nidigital.PPMUApertureTimeUnits.SECONDS

        # Configure and source
        if source == 'source-current':
            session.channels[channels].ppmu_output_function = nidigital.PPMUOutputFunction.CURRENT

            session.channels[channels].ppmu_current_level_range = current_level_range
            session.channels[channels].ppmu_current_level = current_level
            session.channels[channels].ppmu_voltage_limit_high = voltage_limit_high
            session.channels[channels].ppmu_voltage_limit_low = voltage_limit_low

            session.channels[channels].ppmu_source()

            # Settling time between sourcing and measuring
            time.sleep(settling_time)

        elif source == 'source-voltage':
            session.channels[channels].ppmu_output_function = nidigital.PPMUOutputFunction.VOLTAGE

            session.channels[channels].ppmu_current_limit_range = current_limit_range
            session.channels[channels].ppmu_voltage_level = voltage_level

            session.channels[channels].ppmu_source()

            # Settling time between sourcing and measuring
            time.sleep(settling_time)

        pin_info = session.channels[channels].get_pin_results_pin_information()

        # Measure
        if measure == 'current':
            current_measurements = session.channels[channels].ppmu_measure(nidigital.PPMUMeasurementType.CURRENT)

            print('{:<6} {:<20} {:<10}'.format('Site', 'Pin Name', 'Current'))

            for pin, current in zip(pin_info, current_measurements):
                print(f'{pin.site_number:<6d} {pin.pin_name:<20} {current:<10f}')
        else:
            voltage_measurements = session.channels[channels].ppmu_measure(nidigital.PPMUMeasurementType.VOLTAGE)

            print('{:<6} {:<20} {:<10}'.format('Site', 'Pin Name', 'Voltage'))

            for pin, voltage in zip(pin_info, voltage_measurements):
                print(f'{pin.site_number:<6d} {pin.pin_name:<20} {voltage:<10f}')

        # Disconnect all channels using programmable onboard switching
        session.channels[channels].selected_function = nidigital.SelectedFunction.DISCONNECT


def _main(argsv):
    parser = argparse.ArgumentParser(description='Demonstrates how to source/measure voltage/current using the PPMU on selected channels/pins of the digital pattern instrument',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2,PXI1Slot3', help='Resource name of a NI digital pattern instrument, ensure the resource name matches the instrument name in the pinmap file.')
    parser.add_argument('-s', '--simulate', default='True', choices=['True', 'False'], help='Whether to run on simulated hardware or on real hardware')
    parser.add_argument('-c', '--channels', default='DUTPin1, SystemPin1', help='Channel(s)/Pin(s) to use')
    parser.add_argument('-m', '--measure', default='voltage', choices=['voltage', 'current'], help='Measure voltage or measure current')
    parser.add_argument('-at', '--aperture-time', default=0.000004, type=float, help='Aperture time in seconds')
    subparser = parser.add_subparsers(dest='source', help='Sub-command help, by default it measures voltage and does not source')

    source_current = subparser.add_parser('source-current', help='Source current')
    source_current.add_argument('-clr', '--current-level-range', default=0.000002, type=float, help='Current level range in amps')
    source_current.add_argument('-cl', '--current-level', default=0.000002, type=float, help='Current level in amps')
    source_current.add_argument('-vlh', '--voltage-limit-high', default=3.3, type=float, help='Voltage limit high in volts')
    source_current.add_argument('-vll', '--voltage-limit-low', default=0, type=float, help='Voltage limit low in volts')
    source_current.add_argument('-st', '--settling-time', default=0.01, type=float, help='Settling time in seconds')

    source_voltage = subparser.add_parser('source-voltage', help='Source voltage')
    source_voltage.add_argument('-clr', '--current-limit-range', default=0.000002, type=float, help='Current limit range in amps')
    source_voltage.add_argument('-vl', '--voltage-level', default=3.3, type=float, help='Voltage level in volts')
    source_voltage.add_argument('-st', '--settling-time', default=0.01, type=float, help='Settling time in seconds')

    args = parser.parse_args(argsv)

    if args.source == 'source-current':
        example(
            args.resource_name,
            'Simulate=1, DriverSetup=Model:6571' if args.simulate == 'True' else '',
            args.channels,
            args.measure,
            args.aperture_time,
            args.source,
            args.settling_time,
            args.current_level_range,
            args.current_level,
            args.voltage_limit_high,
            args.voltage_limit_low)
    elif args.source == 'source-voltage':
        example(
            args.resource_name,
            'Simulate=1, DriverSetup=Model:6571' if args.simulate == 'True' else '',
            args.channels,
            args.measure,
            args.aperture_time,
            args.source,
            args.settling_time,
            current_limit_range=args.current_limit_range,
            voltage_level=args.voltage_level)
    else:
        if args.measure == 'current':
            raise ValueError('Cannot measure current on a channel that is not sourcing voltage or current')
        example(
            args.resource_name,
            'Simulate=1, DriverSetup=Model:6571' if args.simulate == 'True' else '',
            args.channels,
            args.measure,
            args.aperture_time)


def main():
    _main(sys.argv[1:])


def test_main():
    _main([])
    _main(['-m', 'voltage'])
    with pytest.raises(Exception):
        _main(['-m', 'current'])
    _main(['-m', 'voltage', 'source-current'])
    _main(['-m', 'current', 'source-current'])
    _main(['-m', 'voltage', 'source-voltage'])
    _main(['-m', 'current', 'source-voltage'])


def test_example():
    resource_name = 'PXI1Slot2,PXI1Slot3'
    options = {'simulate': True, 'driver_setup': {'Model': '6571'}, }
    channels = 'DUTPin1, SystemPin1'
    aperture_time = 0.000004

    example(resource_name, options, channels, 'voltage',
            aperture_time)
    with pytest.raises(Exception):
        example(resource_name, options, channels, 'current',
                aperture_time)

    settling_time = 0.01
    current_level_range = 0.000002
    current_level = 0.000002
    voltage_limit_high = 3.3
    voltage_limit_low = 0
    example(resource_name, options, channels, 'voltage',
            aperture_time, 'source-current', settling_time,
            current_level_range, current_level,
            voltage_limit_high, voltage_limit_low)
    example(resource_name, options, channels, 'current',
            aperture_time, 'source-current', settling_time,
            current_level_range, current_level,
            voltage_limit_high, voltage_limit_low)

    current_limit_range = 0.000002
    voltage_level = 3.3
    example(resource_name, options, channels, 'voltage',
            aperture_time, 'source-voltage', settling_time,
            current_limit_range=current_limit_range,
            voltage_level=voltage_level)
    example(resource_name, options, channels, 'current',
            aperture_time, 'source-voltage', settling_time,
            current_limit_range=current_limit_range,
            voltage_level=voltage_level)


if __name__ == '__main__':
    main()
