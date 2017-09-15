#!/usr/bin/python

import argparse
import niswitch
import sys

parser = argparse.ArgumentParser(description='Performs a connection with NI-SWITCH Channels.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='PXI1Slot2', help='Resource name of a National Instruments Switch.')
args = parser.parse_args()

try:
    with niswitch.Session(args.name) as session:
        print("Device Name: ", session.io_resource_descriptor)
        print("Device Model: ", session.instrument_model)
        print("Driver Revision: ", session.specific_driver_revision)
        print("Channel count: ", session.channel_count)
        print("Relay count: ", session.number_of_relays)
        print('')
        print('Relay Info')
        row_format = "{:<15}" * (3)
        print(row_format.format("Number", "Name", "Position"))
        for i in range(1, session.number_of_relays + 1):
            print(row_format.format(i, session.get_relay_name(i), session.get_relay_position(session.get_relay_name(i))))
except niswitch.Error as e:
    sys.stderr.write(str(e))
    sys.exit(e.code)
