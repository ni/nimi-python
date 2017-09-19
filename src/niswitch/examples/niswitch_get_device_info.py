#!/usr/bin/python

import argparse
import niswitch
import sys

parser = argparse.ArgumentParser(description='Prints information for the specified National Instruments Switch module.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='PXI1Slot2', help='Resource name of a National Instruments Switch.')
parser.add_argument('-d', '--device-info', default=False, action='store_true', help='Prints information for the device')
parser.add_argument('-c', '--channel-info', default=False, action='store_true', help='Prints information for all relays on the device')
parser.add_argument('-r', '--relay-info', default=False, action='store_true', help='Prints information for all channels on the device')
args = parser.parse_args()

if not (args.device_info or args.channel_info or args.relay_info):
    parser.print_help()
    sys.exit()

try:
    with niswitch.Session(args.name) as session:

        if args.device_info:
            row_format = '{:<18}' * (2)
            print(row_format.format('Device Name: ', session.io_resource_descriptor))
            print(row_format.format('Device Model: ', session.instrument_model))
            print(row_format.format('Driver Revision: ', session.specific_driver_revision))
            print(row_format.format('Channel count: ', session.channel_count))
            print(row_format.format('Relay count: ', session.number_of_relays))
            print('Relay Info:')

        if args.channel_info:
            row_format = '{:6}' + ' ' * 12 + '{:<15}{:<22}{:6}'
            print(row_format.format('Number', 'Name', 'Is Configuration', 'Is Source'))
            for i in range(1, session.channel_count + 1):
                channel_name = session.get_channel_name(i)
                with session[channel_name] as channel:
                    print(row_format.format(i, channel_name, str(channel.is_configuration_channel), str(channel.is_source_channel)))

        if args.relay_info:
            row_format = '{:6}' + ' ' * 12 + '{:<15}{:<22}{:6}'
            print(row_format.format('Number', 'Name', 'Position', 'Count'))
            for i in range(1, session.number_of_relays + 1):
                relay_name = session.get_relay_name(i)
                print(row_format.format(i, relay_name, session.get_relay_position(relay_name), session.get_relay_count(relay_name)))

except niswitch.Error as e:
    sys.stderr.write(str(e))
    sys.exit(e.code)
