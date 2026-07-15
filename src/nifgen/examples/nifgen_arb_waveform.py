#!/usr/bin/python

import argparse
import math
import nifgen
import sys
import time


def create_waveform_data(number_of_samples):
    waveform_data = []
    angle_per_sample = (2 * math.pi) / number_of_samples
    for i in range(number_of_samples):
        waveform_data.append(math.sin(i * angle_per_sample) * math.sin(i * angle_per_sample * 20))
    return waveform_data


def example(resource_name, options, samples, gain, offset, gen_time):
    waveform_data = create_waveform_data(samples)
    with nifgen.Session(resource_name=resource_name, options=options) as session:
        session.output_mode = nifgen.OutputMode.ARB
        waveform = session.create_waveform(waveform_data_array=waveform_data)
        session.configure_arb_waveform(waveform_handle=waveform, gain=gain, offset=offset)
        with session.initiate():
            time.sleep(gen_time)


def _main(argsv):
    parser = argparse.ArgumentParser(description='Continuously generates an arbitrary waveform.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI arbitrary waveform generator.')
    parser.add_argument('-s', '--samples', default=100000, type=int, help='Number of samples')
    parser.add_argument('-g', '--gain', default=1.0, type=float, help='Gain')
    parser.add_argument('-o', '--offset', default=0.0, type=float, help='DC offset (V)')
    parser.add_argument('-t', '--time', default=5.0, type=float, help='Generation time (s)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.samples, args.gain, args.offset, args.time)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5433 (2CH)', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 100000, 1.0, 0.0, 5.0)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()


