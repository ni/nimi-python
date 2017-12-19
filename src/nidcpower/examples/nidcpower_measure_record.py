#!/usr/bin/python

import argparse
import nidcpower

parser = argparse.ArgumentParser(description='Outputs the specified voltage, then takes the specified number of voltage and current readings.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--resource_name', default='PXI1Slot2', help='Resource name of a National Instruments SMU')
parser.add_argument('-c', '--channels', default='0', help='Channel(s) to use')
parser.add_argument('-l', '--length', default='20', type=int, help='Measure record length')
parser.add_argument('-v', '--voltage', default=5.0, type=float, help='Voltage level (V)')
parser.add_argument('-op', '--option_string', default='', type=str, help='Option string')
args = parser.parse_args()

with nidcpower.Session(resource_name=args.resource_name, channels=args.channels, option_string=args.option_string) as session:

    # Configure the session.
    session.measure_record_length = args.length
    session.measure_record_length_is_finite = True
    session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
    session.voltage_level = args.voltage

    session.commit()
    print('Effective measurement rate: {0} S/s'.format(session.measure_record_delta_time / 1))

    print('  #    Voltage    Current    In Compliance')
    row_format = '{0:3d}:   {1:8.6f}   {2:8.6f}   {3}'
    with session.initiate():
        while samples_acquired < args.length:
            voltage_measurements, current_measurements, in_compliance = session.fetch_multiple(count=session.fetch_backlog)
            for i in zip(range(len(voltage_measurements)), voltage_measurements, current_measurements, in_compliance):
                print(row_format.format(i[0], i[1], i[2], i[3]))

