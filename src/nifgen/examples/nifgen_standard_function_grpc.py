#!/usr/bin/python

import argparse
import grpc
import nifgen
import sys
import time


def example(resource_name, options, waveform, frequency, amplitude, offset, phase, gen_time, address, port):
    session_name = ''  # user-specified name; empty string means use a new, unnamed session

    # Connect to the NI gRPC Device Server
    channel = grpc.insecure_channel(f'{address}:{port}')
    session_options = nifgen.GrpcSessionOptions(channel, session_name)

    with nifgen.Session(resource_name=resource_name, options=options, _grpc_options=session_options) as session:
        session.output_mode = nifgen.OutputMode.FUNC
        session.configure_standard_waveform(waveform=nifgen.Waveform[waveform], amplitude=amplitude, frequency=frequency, dc_offset=offset, start_phase=phase)
        with session.initiate():
            time.sleep(gen_time)


def _main(argsv):
    supported_waveforms = list(nifgen.Waveform.__members__.keys())[:-1]  # no support for user-defined waveforms in example
    parser = argparse.ArgumentParser(description='Generates the standard function.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI function generator.')
    parser.add_argument('-w', '--waveform', default=supported_waveforms[0], choices=supported_waveforms, type=str.upper, help='Standard waveform')
    parser.add_argument('-f', '--frequency', default=1000, type=float, help='Frequency (Hz)')
    parser.add_argument('-a', '--amplitude', default=1.0, type=float, help='Amplitude (Vpk-pk)')
    parser.add_argument('-o', '--offset', default=0.0, type=float, help='DC offset (V)')
    parser.add_argument('-p', '--phase', default=0.0, type=float, help='Start phase (deg)')
    parser.add_argument('-t', '--time', default=5.0, type=float, help='Generation time (s)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    parser.add_argument('--address', default='localhost', help='Server address.')
    parser.add_argument('--port', default='31763', help='Server port.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.waveform, args.frequency, args.amplitude, args.offset, args.phase, args.time, args.address, args.port)


def main():
    _main(sys.argv[1:])


if __name__ == '__main__':
    main()



