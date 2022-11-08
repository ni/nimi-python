#!/usr/bin/python

import argparse
import grpc
import nidmm
import sys


def example(resource_name, option_string, function, range, digits, address, port):
    session_name = ''  # user-specified name; empty string means use a new, unnamed session

    # Connect to the grpc server
    channel = grpc.insecure_channel(f'{address}:{port}')
    session_options = nidmm.GrpcSessionOptions(channel, session_name, nidmm.SessionInitializationBehavior.AUTO)

    with nidmm.Session(resource_name=resource_name, options=option_string, _grpc_options=session_options) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function[function], range=range, resolution_digits=digits)
        print(session.read())


def _main(argsv):
    supported_functions = list(nidmm.Function.__members__.keys())
    parser = argparse.ArgumentParser(description='Performs a single measurement using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI digital multimeter.')
    parser.add_argument('-f', '--function', default=supported_functions[0], choices=supported_functions, type=str.upper, help='Measurement function.')
    parser.add_argument('-r', '--range', default=10, type=float, help='Measurement range.')
    parser.add_argument('-d', '--digits', default=6.5, type=float, help='Digits of resolution for the measurement.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    parser.add_argument('-a', '--address', default='localhost', help='Server address.')
    parser.add_argument('-p', '--port', default='31763', help='Server port.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.function, args.range, args.digits, args.address, args.port)

# TODO(danestull) Add example and main tests once the gRPC server is started automatically


def main():
    _main(sys.argv[1:])


if __name__ == '__main__':
    main()


