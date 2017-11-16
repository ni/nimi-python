#!/usr/bin/python

import argparse
import nifgen

supported_waveforms = list(nifgen.Waveform.__members__.keys())[:-1]  # no support for user-defined waveforms in example
parser = argparse.ArgumentParser(description='Generates the standard function.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='PXI1Slot2', help='Resource name of a National Instruments Function Generator')
parser.add_argument('-w', '--waveform', default=supported_waveforms[0], choices=supported_waveforms, type=str.upper, help='Standard waveform')
parser.add_argument('-f', '--frequency', default=1000, type=float, help='Frequency (Hz)')
parser.add_argument('-a', '--amplitude', default=1.0, type=float, help='Amplitude (Vpk-pk)')
parser.add_argument('-o', '--offset', default=0.0, type=float, help='DC Offset (V)')
parser.add_argument('-p', '--phase', default=0.0, type=float, help='Start Phase (deg)')
args = parser.parse_args()

with nifgen.Session(args.name) as session:
    session.output_mode = nifgen.OutputMode.FUNC
    session.configure_standard_waveform(waveform=nifgen.Waveform[args.waveform], amplitude=args.amplitude, frequency=args.frequency, dc_offset=args.offset, start_phase=args.phase)
    with session.initiate():
        try:
            input("Press Enter to abort generation...")
        except SyntaxError:
            pass
