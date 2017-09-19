#!/usr/bin/python

import argparse
import niswitch
import sys

parser = argparse.ArgumentParser(description='Gets device information from a specified switch module.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='PXI1Slot2', help='Resource name of a National Instruments Switch.')
parser.add_argument('-i', '--information', default=False, action='store_true', help='Provides relay name, position, and count for all relays on a switch')
args = parser.parse_args()

try:
    with niswitch.Session(args.name) as session:
        row_format = '{:<18}' * (2)
        print(row_format.format('Device Name: ', session.io_resource_descriptor))
        print(row_format.format('Device Model: ', session.instrument_model))
        print(row_format.format('Driver Revision: ', session.specific_driver_revision))
        print(row_format.format('Channel count: ', session.channel_count))
        print(row_format.format('Relay count: ', session.number_of_relays))
        print('Relay Info:')
        if args.information:
            row_format = '{:6}' + ' ' * 12 + '{:<15}{:<22}{:6}'
            print(row_format.format('Number', 'Name', 'Position', 'Count'))
            for i in range(1, session.number_of_relays + 1):
                relay_name = session.get_relay_name(i)
                print(row_format.format(i, relay_name, session.get_relay_position(relay_name), session.get_relay_count(relay_name)))
except niswitch.Error as e:
    sys.stderr.write(str(e))
    sys.exit(e.code)
