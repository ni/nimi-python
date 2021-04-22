#!/usr/bin/python

import argparse
import hightime
import nidcpower
import sys


def print_fetched_measurements(measurements):
    print('             Voltage : {:f} V'.format(measurements[0].voltage))
    print('              Current: {:f} A'.format(measurements[0].current))
    print('        In compliance: {0}'.format(measurements[0].in_compliance))


def example(resource_name, channels, options, voltage1, voltage2, delay):
    timeout = hightime.timedelta(seconds=(delay + 1.0))

    with nidcpower.Session(resource_name=resource_name, channels=channels, options=options) as session:

        # Configure the session.
        session.source_mode = nidcpower.SourceMode.SINGLE_POINT
        session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
        session.current_limit = .06
        session.voltage_level_range = 5.0
        session.current_limit_range = .06
        session.source_delay = hightime.timedelta(seconds=delay)
        session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
        session.voltage_level = voltage1

        with session.initiate():
            print('Voltage 1:')
            print_fetched_measurements(session.fetch_multiple(count=1, timeout=timeout))
            session.voltage_level = voltage2  # on-the-fly set
            print('Voltage 2:')
            print_fetched_measurements(session.fetch_multiple(count=1, timeout=timeout))
            session.output_enabled = False


def _main(argsv):
    parser = argparse.ArgumentParser(description='Outputs voltage 1, waits for source delay, and then takes a measurement. Then orepeat with voltage 2.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of a NI SMU')
    parser.add_argument('-c', '--channels', default='0', help='Channel(s) to use')
    parser.add_argument('-v1', '--voltage1', default=1.0, type=float, help='Voltage level 1 (V)')
    parser.add_argument('-v2', '--voltage2', default=2.0, type=float, help='Voltage level 2 (V)')
    parser.add_argument('-d', '--delay', default=0.05, type=float, help='Source delay (s)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.channels, args.option_string, args.voltage1, args.voltage2, args.delay)


def main():
    _main(sys.argv[1:])


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe', ]
    _main(cmd_line)


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4162', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', '0', options, 1.0, 2.0, 0.05)


if __name__ == '__main__':
    main()


