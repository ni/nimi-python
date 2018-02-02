#!/usr/bin/python

import argparse
import nifgen
import sys
import time


def example(argsv):
    supported_waveforms = list(nifgen.Waveform.__members__.keys())[:-1]  # no support for user-defined waveforms in example
    parser = argparse.ArgumentParser(description='Generates the standard function.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource_name', default='PXI1Slot2', help='Resource name of a National Instruments Function Generator')
    parser.add_argument('-w', '--waveform', default=supported_waveforms[0], choices=supported_waveforms, type=str.upper, help='Standard waveform')
    parser.add_argument('-f', '--frequency', default=1000, type=float, help='Frequency (Hz)')
    parser.add_argument('-a', '--amplitude', default=1.0, type=float, help='Amplitude (Vpk-pk)')
    parser.add_argument('-o', '--offset', default=0.0, type=float, help='DC offset (V)')
    parser.add_argument('-p', '--phase', default=0.0, type=float, help='Start phase (deg)')
    parser.add_argument('-t', '--time', default=5.0, type=float, help='Generation time (s)')
    parser.add_argument('-op', '--option_string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)

    with nifgen.Session(resource_name=args.resource_name, option_string=args.option_string) as session:
        session.output_mode = nifgen.OutputMode.FUNC
        session.configure_standard_waveform(waveform=nifgen.Waveform[args.waveform], amplitude=args.amplitude, frequency=args.frequency, dc_offset=args.offset, start_phase=args.phase)
        with session.initiate():
            time.sleep(args.time)


def _main():
    example(sys.argv)


def test_example():
    cmd_line = ['-op', 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe', ]
    example(cmd_line)


if __name__ == '__main__':
    _main()


