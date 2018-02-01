#!/usr/bin/python

import argparse
import niswitch
import sys


def example(argsv):
    parser = argparse.ArgumentParser(description='Performs a connection with NI-SWITCH Channels.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource_name', default='PXI1Slot2', help='Resource name of a National Instruments Switch.')
    parser.add_argument('-ch1', '--channel1', default='c0', help='Channel One.')
    parser.add_argument('-ch2', '--channel2', default='r0', help='Channel Two.')
    parser.add_argument('-t', '--topology', default='Configured Topology', help='Topology.')
    parser.add_argument('-s', '--simulate', default=False, action='store_true', help='Simulate device.')
    args = parser.parse_args(argsv)
    # if we are simulating resource name must be blank
    resource_name = '' if args.simulate else args.resource_name

    with niswitch.Session(resource_name=resource_name, topology=args.topology, simulate=args.simulate) as session:
        session.connect(channel1=args.channel1, channel2=args.channel2)
        print('Channel ', args.channel1, ' and ', args.channel2, ' are now connected.')
        session.disconnect(channel1=args.channel1, channel2=args.channel2)
        print('Channel ', args.channel1, ' and ', args.channel2, ' are now disconnected.')


def _main():
    example(sys.argv)


def test_example():
    cmd_line = ['--topology', '2737/2-Wire 4x64 Matrix', '--simulate']
    example(cmd_line)


if __name__ == '__main__':
    _main()


