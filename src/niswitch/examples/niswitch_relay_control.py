#!/usr/bin/python

import argparse
import niswitch
import sys


def example(argsv):
    parser = argparse.ArgumentParser(description='Performs relay control with NI-SWITCH relays.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource_name', default='PXI1Slot2', help='Resource name of a National Instruments Switch.')
    parser.add_argument('-r', '--relay', default='k0', help='Relay Name.')
    parser.add_argument('-a', '--action', default='OPEN', choices=niswitch.RelayAction.__members__.keys(), type=str.upper, help='Relay Action.')
    parser.add_argument('-t', '--topology', default='Configured Topology', help='Topology.')
    parser.add_argument('-s', '--simulate', default=False, action='store_true', help='Simulate device.')
    args = parser.parse_args(argsv)
    # if we are simulating resource name must be blank
    resource_name = '' if args.simulate else args.resource_name

    with niswitch.Session(resource_name=resource_name, topology=args.topology, simulate=args.simulate) as session:
        session.relay_control(relay_name=args.relay, relay_action=niswitch.RelayAction[args.action])
        print('Relay ', args.relay, ' has had the action ', args.action, ' performed.')


def _main():
    example(sys.argv)


def test_example():
    cmd_line = ['--topology', '2737/2-Wire 4x64 Matrix', '--simulate', '--relay', 'kr0c0']
    example(cmd_line)


if __name__ == '__main__':
    _main()


