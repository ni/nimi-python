#!/usr/bin/python

import argparse
import nidcpower
import sys


parser = argparse.ArgumentParser(description='Outputs voltage 1, waits for source delay, and then takes a measurement. Then orepeat with voltage 2.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='PXI1Slot2', help='Resource name of a National Instruments SMU')
parser.add_argument('-c', '--channels', default='0', help='Channel(s) to use')
parser.add_argument('-v1', '--voltage1', default=1.0, type=float, help='Voltage level 1 (volts)')
parser.add_argument('-v2', '--voltage2', default=2.0, type=float, help='Voltage level 2 (volts)')
parser.add_argument('-d', '--delay', default=0.05, type=float, help='Source delay (seconds)')
args = parser.parse_args()

def print_fetched_measurements(voltage_measurements, current_measurements, in_compliance, actual_count):
    assert actual_count == 1
    print('             Voltage : {:f} V'.format(voltage_measurements[0]))
    print('              Current: {:f} A'.format(current_measurements[0]))
    print('        In compliance: {0}'.format(in_compliance[0]))

timeout = args.delay + 1.0

try:
    with nidcpower.Session(args.name, channels=args.channels) as session:

        # Configure the session.
        session.source_mode = nidcpower.SourceMode.SINGLE_POINT
        session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
        session.current_limit = .1
        session.voltage_level_range = 5.0
        session.current_limit_range = .1
        session.source_delay = args.delay
        session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
        session.voltage_level = args.voltage1

        with session.initiate():
            print('Voltage 1:')
            print_fetched_measurements(*session.fetch_multiple(1, timeout))
            session.voltage_level = args.voltage2 # on-the-fly set
            print('Voltage 2:')
            print_fetched_measurements(*session.fetch_multiple(1, timeout))
            session.output_enabled = False

except nidcpower.Error as e:
    sys.stderr.write(str(e))
    sys.exit(e.code)
