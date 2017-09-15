#!/usr/bin/python

import argparse
import niswitch
import sys

parser = argparse.ArgumentParser(description='Performs relay control with NI-SWITCH relays.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='PXI1Slot2', help='Resource name of a National Instruments Switch.')
parser.add_argument('-rn', '--relay_name', default='k0', type=str, help='Relay Name.')
parser.add_argument('-ra', '--relay_action', default='close', type=str, help='Relay Action. Accepts "open" and "close"')
args = parser.parse_args()

try:
    if args.relay_action == 'open':
        action = niswitch.RelayAction.OPEN_RELAY
    elif args.relay_action == 'close':
        action = niswitch.RelayAction.CLOSE_RELAY
    else:
        raise Exception('Invalid relay action')
    with niswitch.Session(args.name) as session:
        session.relay_control(args.relay_name, action)
        print('Relay ', args.relay_name, ' has had the action ', args.relay_action, ' performed.')
except niswitch.Error as e:
    sys.stderr.write(str(e))
    sys.exit(e.code)
