#!/usr/bin/python

import argparse
import grpc
import niswitch
import sys


def example(resource_name, channel1, channel2, topology, simulate):
    # if we are simulating resource name must be blank
    resource_name = '' if simulate else resource_name
    # Connect to an already running server using the following server information
    server_address = "localhost"
    server_port = "31763"
    channel = grpc.insecure_channel(f"{server_address}:{server_port}")
    session_options = niswitch.GrpcSessionOptions(channel, "", niswitch.SessionInitializationBehavior.AUTO)

    with niswitch.Session(resource_name=resource_name, topology=topology, simulate=simulate, _grpc_options=session_options) as session:
        session.connect(channel1=channel1, channel2=channel2)
        print('Channel ', channel1, ' and ', channel2, ' are now connected.')
        session.disconnect(channel1=channel1, channel2=channel2)
        print('Channel ', channel1, ' and ', channel2, ' are now disconnected.')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Performs a connection with NI-SWITCH Channels.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI switch.')
    parser.add_argument('-ch1', '--channel1', default='c0', help='Channel One.')
    parser.add_argument('-ch2', '--channel2', default='r0', help='Channel Two.')
    parser.add_argument('-t', '--topology', default='Configured Topology', help='Topology.')
    parser.add_argument('-s', '--simulate', default=False, action='store_true', help='Simulate device.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.channel1, args.channel2, args.topology, args.simulate)


def main():
    _main(sys.argv[1:])


if __name__ == '__main__':
    main()


