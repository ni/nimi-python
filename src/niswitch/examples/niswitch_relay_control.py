#!/usr/bin/python

import argparse
import niswitch

parser = argparse.ArgumentParser(description='Performs relay control with NI-SWITCH relays.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='PXI1Slot2', help='Resource name of a National Instruments Switch.')
parser.add_argument('-r', '--relay', default='k0', type=str, help='Relay Name.')
parser.add_argument('-a', '--action', default='OPEN_RELAY', choices=niswitch.RelayAction.__members__.keys(), type=str.upper, help='Relay Action.')
args = parser.parse_args()

with niswitch.Session(args.name) as session:
    session.relay_control(args.relay, niswitch.RelayAction[args.action])
    print('Relay ', args.relay, ' has had the action ', args.action, ' performed.')
