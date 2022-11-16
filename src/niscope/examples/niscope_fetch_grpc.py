#!/usr/bin/python

import argparse
import grpc
import niscope
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4, width=80)


def example(resource_name, channels, options, address, port, length, voltage):
    session_name = '' # user-specified name; empty string means use a new , unnamed session

    # Connect to the grpc server
    channel = grpc.insecure_channel(f'{address}:{port}')
    session_options = niscope.GrpcSessionOptions(channel, session_name)
    
    with niscope.Session(resource_name=resource_name, options=options, grpc_options=session_options) as session:
        session.configure_vertical(range=voltage, coupling=niscope.VerticalCoupling.AC)
        session.configure_horizontal_timing(min_sample_rate=50000000, min_num_pts=length, ref_position=50.0, num_records=1, enforce_realtime=True)
        with session.initiate():
            waveforms = session.channels[channels].fetch(num_samples=length)
        for i in range(len(waveforms)):
            print('Waveform {0} information:'.format(i))
            print(str(waveforms[i]) + '\n\n')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Acquires one record from the given channels.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI digitizer.')
    parser.add_argument('-c', '--channels', default='0', help='Channel(s) to use')
    parser.add_argument('-l', '--length', default=1000, type=int, help='Measure record length')
    parser.add_argument('-v', '--voltage', default=1.0, type=float, help='Voltage range (V)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    parser.add_argument('-a', '--address', default='localhost', help='Server address')
    parser.add_argument('-p', '--port', default='31763', help='Server port')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.channels, args.option_string, args.address, args.port, args.length, args.voltage)

# TODO(danestull) Add example and main tests once the gRPC server is started automatically


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5164', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', '0', options, 1000, 1.0)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()

