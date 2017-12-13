#!/usr/bin/python

import argparse
import niswitch

parser = argparse.ArgumentParser(description='Performs a connection with NI-SWITCH Channels.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='PXI1Slot2', help='Resource name of a National Instruments Switch.')
parser.add_argument('-ch1', '--channel1', default='c0', type=str, help='Channel One.')
parser.add_argument('-ch2', '--channel2', default='r0', type=str, help='Channel Two.')
parser.add_argument('-t', '--topology', default='Configured Topology', type=str, help='Topology.')
parser.add_argument('-s', '--simulate', default=False, type=bool, help='Simulate Device.')
args = parser.parse_args()

with niswitch.Session(resource_name=args.name, topology=args.topology, simulate=args.simulate) as session:
    session.connect(channel1=args.channel1, channel2=args.channel2)
    print('Channel ', args.channel1, ' and ', args.channel2, ' are now connected.')
    session.disconnect(channel1=args.channel1, channel2=args.channel2)
    print('Channel ', args.channel1, ' and ', args.channel2, ' are now disconnected.')
