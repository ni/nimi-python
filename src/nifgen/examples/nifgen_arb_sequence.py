#!/usr/bin/python

import argparse
import math
import nifgen
import sys
import time

# Each shape returns a value between -1.0 and +1.0 for a position x in [0, 1) of one cycle.
WAVEFORM_SHAPES = {
    'SINE': lambda x: math.sin(2 * math.pi * x),
    'SQUARE': lambda x: 1.0 if x < 0.5 else -1.0,
    'TRIANGLE': lambda x: 1 - 4 * abs(x - 0.5),
    'DECREASING': lambda x: 1 - 2 * x,
}

# Waveform Information Array: (Waveform Type, Amplitude, # of points), generated in this order.
DEFAULT_WAVEFORMS = [
    ('SINE', 0.75, 256),
    ('TRIANGLE', 1.0, 256),
    ('SQUARE', 0.5, 256),
    ('DECREASING', 0.8, 256),
]


def create_waveform_data(waveform_type, amplitude, number_of_points):
    shape = WAVEFORM_SHAPES[waveform_type]
    return [amplitude * shape(i / number_of_points) for i in range(number_of_points)]


def example(resource_name, options, waveforms, gain, offset, gen_time):
    with nifgen.Session(resource_name=resource_name, options=options, channel_name='0') as session:
        session.output_mode = nifgen.OutputMode.SEQ
        waveform_handles = [session.create_waveform(waveform_data_array=create_waveform_data(*waveform)) for waveform in waveforms]
        loop_counts = [1] * len(waveform_handles)
        sequence_handle = session.create_arb_sequence(waveform_handles_array=waveform_handles, loop_counts_array=loop_counts)
        session.configure_arb_sequence(sequence_handle=sequence_handle, gain=gain, offset=offset)
        with session.initiate():
            print('Generating sequence for {} seconds:'.format(gen_time))
            for waveform_type, amplitude, number_of_points in waveforms:
                print('  {:<10} amplitude {:<5} {} points'.format(waveform_type, amplitude, number_of_points))
            time.sleep(gen_time)


def _main(argsv):
    parser = argparse.ArgumentParser(description='Continuously generates an arbitrary sequence of waveforms.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI arbitrary waveform generator.')
    parser.add_argument('-w', '--waveform', nargs=3, action='append', metavar=('TYPE', 'AMPLITUDE', 'POINTS'), help='Waveform to append to the sequence. Repeat to add more. TYPE is one of {}. If omitted, the sequence is {}'.format(', '.join(WAVEFORM_SHAPES), ', '.join('{} {} {}'.format(*w) for w in DEFAULT_WAVEFORMS)))
    parser.add_argument('-g', '--gain', default=1.0, type=float, help='Gain')
    parser.add_argument('-o', '--offset', default=0.0, type=float, help='DC offset (V)')
    parser.add_argument('-t', '--time', default=5.0, type=float, help='Generation time (s)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    waveforms = [(w_type.upper(), float(amplitude), int(points)) for w_type, amplitude, points in args.waveform or DEFAULT_WAVEFORMS]
    for waveform_type, _, _ in waveforms:
        if waveform_type not in WAVEFORM_SHAPES:
            parser.error('Unsupported waveform type {}. Choose from {}.'.format(waveform_type, ', '.join(WAVEFORM_SHAPES)))
    example(args.resource_name, args.option_string, waveforms, args.gain, args.offset, args.time)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5433 (2CH)', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, DEFAULT_WAVEFORMS, 1.0, 0.0, 5.0)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
