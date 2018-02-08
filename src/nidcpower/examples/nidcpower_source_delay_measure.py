#!/usr/bin/python

import argparse
import datetime
import nidcpower
import sys


def print_fetched_measurements(voltage_measurements, current_measurements, in_compliance):
    print('             Voltage : {:f} V'.format(voltage_measurements[0]))
    print('              Current: {:f} A'.format(current_measurements[0]))
    print('        In compliance: {0}'.format(in_compliance[0]))


def example(argsv):
    parser = argparse.ArgumentParser(description='Outputs voltage 1, waits for source delay, and then takes a measurement. Then orepeat with voltage 2.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource_name', default='PXI1Slot2', help='Resource name of a National Instruments SMU')
    parser.add_argument('-c', '--channels', default='0', help='Channel(s) to use')
    parser.add_argument('-v1', '--voltage1', default=1.0, type=float, help='Voltage level 1 (V)')
    parser.add_argument('-v2', '--voltage2', default=2.0, type=float, help='Voltage level 2 (V)')
    parser.add_argument('-d', '--delay', default=0.05, type=float, help='Source delay (s)')
    parser.add_argument('-op', '--option_string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)

    timeout = args.delay + 1.0

    with nidcpower.Session(resource_name=args.resource_name, channels=args.channels, option_string=args.option_string) as session:

        # Configure the session.
        session.source_mode = nidcpower.SourceMode.SINGLE_POINT
        session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
        session.current_limit = .06
        session.voltage_level_range = 5.0
        session.current_limit_range = .06
        session.source_delay = datetime.timedelta(seconds=args.delay)
        session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
        session.voltage_level = args.voltage1

        with session.initiate():
            print('Voltage 1:')
            print_fetched_measurements(*session.fetch_multiple(count=1, timeout=datetime.timedelta(seconds=timeout)))
            session.voltage_level = args.voltage2  # on-the-fly set
            print('Voltage 2:')
            print_fetched_measurements(*session.fetch_multiple(count=1, timeout=datetime.timedelta(seconds=timeout)))
            session.output_enabled = False


def _main():
    example(sys.argv)


def test_example():
    cmd_line = ['-op', 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe', ]
    example(cmd_line)


if __name__ == '__main__':
    _main()


