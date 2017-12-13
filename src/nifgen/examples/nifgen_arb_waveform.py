#!/usr/bin/python

import argparse
import math
import nifgen
import time

supported_waveforms = list(nifgen.Waveform.__members__.keys())[:-1]  # no support for user-defined waveforms in example
parser = argparse.ArgumentParser(description='Continuously generates an arbitrary waveform.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--resource_name', default='PXI1Slot2', help='Resource name of a National Instruments Arbitrary Waveform Generator')
parser.add_argument('-s', '--samples', default=100000, type=int, help='Number of samples')
parser.add_argument('-g', '--gain', default=1.0, type=float, help='Gain')
parser.add_argument('-o', '--offset', default=0.0, type=float, help='DC offset (V)')
parser.add_argument('-t', '--time', default=5.0, type=float, help='Generation time (s)')
parser.add_argument('-op', '--option_string', default='', type=str, help='Option string')
args = parser.parse_args()


def create_waveform_data(number_of_samples):
    waveform_data = []
    angle_per_sample = (2 * math.pi) / number_of_samples
    for i in range(number_of_samples):
        waveform_data.append(math.sin(i * angle_per_sample) * math.sin(i * angle_per_sample * 20))
    return waveform_data


waveform_data = create_waveform_data(args.samples)
with nifgen.Session(resource_name=args.resource_name, option_string=args.option_string) as session:
    session.output_mode = nifgen.OutputMode.ARB
    waveform = session.create_waveform(waveform_data_array=waveform_data)
    session.configure_arb_waveform(waveform_handle=waveform, gain=args.gain, offset=args.offset)
    with session.initiate():
        time.sleep(args.time)
