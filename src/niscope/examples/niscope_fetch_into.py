#!/usr/bin/python

import argparse
import niscope
import numpy
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4, width=80)


def example(resource_name, channels, options, length, voltage):
    # fetch_into() allows you to preallocate and reuse the destination of the fetched waveforms, which can result in better performance at the expense of the usability of fetch().
    channels = [ch.strip() for ch in channels.split(",")]
    num_channels = len(channels)
    num_records = 5
    total_num_wfms = num_channels * num_records
    # preallocate a single array for all samples in all waveforms
    # Supported array types are: numpy.float64, numpy.int8, numpy.int16, numpy.int32
    # int8, int16, int32 are for fetching unscaled data, which is the fastest way to fetch.
    # Gain and Offset are stored in the returned WaveformInfo objects and can be applied to the data by the user later.
    wfm = numpy.ndarray(length * total_num_wfms, dtype=numpy.float64)
    with niscope.Session(resource_name=resource_name, options=options) as session:
        session.configure_vertical(range=voltage, coupling=niscope.VerticalCoupling.AC)
        session.configure_horizontal_timing(min_sample_rate=50000000, min_num_pts=length, ref_position=50.0, num_records=num_records, enforce_realtime=True)
        with session.initiate():
            waveforms = session.channels[channels].fetch_into(waveform=wfm, num_records=num_records)
        for i in range(len(waveforms)):
            print(f'Waveform {i} information:')
            print(f'{waveforms[i]}\n\n')
            print(f'Samples: {waveforms[i].samples.tolist()}')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Fetches data directly into a preallocated numpy array.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI digitizer.')
    parser.add_argument('-c', '--channels', default='0', help='Channel(s) to use')
    parser.add_argument('-l', '--length', default=100, type=int, help='Measure record length')
    parser.add_argument('-v', '--voltage', default=1.0, type=float, help='Voltage range (V)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.channels, args.option_string, args.length, args.voltage)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5164', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', '0, 1', options, 100, 1.0)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()

