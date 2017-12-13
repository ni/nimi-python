#!/usr/bin/python

import argparse
import niswitch

parser = argparse.ArgumentParser(description='Performs relay control with NI-SWITCH relays.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='PXI1Slot2', help='Resource name of a National Instruments Switch.')
parser.add_argument('-r', '--relay', default='k0', type=str, help='Relay Name.')
parser.add_argument('-a', '--action', default='OPEN', choices=niswitch.RelayAction.__members__.keys(), type=str.upper, help='Relay Action.')
parser.add_argument('-t', '--topology', default='Configured Topology', type=str, help='Topology.')
parser.add_argument('-s', '--simulate', default=False, type=bool, help='Simulate Device.')
args = parser.parse_args()

with niswitch.Session(resource_name=args.name, topology=args.topology, simulate=args.simulate) as session:
    session.relay_control(relay_name=args.relay, relay_action=niswitch.RelayAction[args.action])
    print('Relay ', args.relay, ' has had the action ', args.action, ' performed.')
