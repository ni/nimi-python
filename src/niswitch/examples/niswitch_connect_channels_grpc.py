#!/usr/bin/python

import argparse
import grpc
import niswitch
import sys


def example(resource_name, channel1, channel2, topology, simulate, address, port):
    # if we are simulating resource name must be blank
    resource_name = '' if simulate else resource_name
    session_name = ''  # user-specified name; empty string means use a new, unnamed session

    # Connect to the grpc server
    channel = grpc.insecure_channel(f'{address}:{port}')
    session_options = niswitch.GrpcSessionOptions(channel, session_name, niswitch.SessionInitializationBehavior.AUTO)

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
    parser.add_argument('-a', '--address', default='localhost', help='Server address.')
    parser.add_argument('-p', '--port', default='31763', help='Server port.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.channel1, args.channel2, args.topology, args.simulate, args.address, args.port)

# TODO(danestull) Add example and main tests once the gRPC server is started automatically


def main():
    _main(sys.argv[1:])


if __name__ == '__main__':
    main()


