#!/usr/bin/python

import argparse
import niswitch
import sys

parser = argparse.ArgumentParser(description='Performs a connection with NI-SWITCH Channels.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='PXI1Slot2', help='Resource name of a National Instruments Switch.')
parser.add_argument('-ch1', '--channel1', default='c0', type=str, help='Channel One.')
parser.add_argument('-ch2', '--channel2', default='r0', type=str, help='Channel Two.')
args = parser.parse_args()

try:
    with niswitch.Session(args.name) as session:
        session.connect(args.channel1, args.channel2)
        print('Channel ', args.channel1, ' and ', args.channel2, ' are now connected.')
        session.disconnect(args.channel1, args.channel2)
        print('Channel ', args.channel1, ' and ', args.channel2, ' are now disconnected.')
except niswitch.Error as e:
    sys.stderr.write(str(e))
    sys.exit(e.code)
