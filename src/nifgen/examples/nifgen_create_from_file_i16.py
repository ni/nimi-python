#!/usr/bin/python

import argparse
import nifgen
from pathlib import Path
import sys
import time


def example(resource_name, options, sample_rate, file_path, byte_order, gen_time):
    waveform_path = (Path(__file__).resolve().parent / file_path).resolve(strict=True)

    with nifgen.Session(resource_name=resource_name, channel_name='0', options=options) as session:
        session.output_mode = nifgen.OutputMode.ARB
        session.arb_sample_rate = sample_rate
        waveform = session.create_waveform_from_file_i16(file_name=str(waveform_path), byte_order=nifgen.ByteOrder[byte_order])
        session.arb_waveform_handle = waveform
        with session.initiate():
            print('Generating waveform. Press Ctrl+C to stop.')
            start_time = time.monotonic()
            while time.monotonic() - start_time < gen_time:
                session.is_done()
                time.sleep(0.1)


def _main(argsv):
    parser = argparse.ArgumentParser(description='Generates an arbitrary waveform from a file storing I16 data.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Specifies the resource name of the device to initialize.')
    parser.add_argument('-r', '--sample-rate', default=40e6, type=float, help='Specifies the rate at which the signal generator outputs the points in arbitrary waveforms.')
    parser.add_argument('-f', '--file-path', default='data/SineI16BigEndian_1000.bin', help='The full path and name of the file where the waveform data resides. Relative paths are resolved beside this example.')
    parser.add_argument('-b', '--byte-order', default='BIG', choices=nifgen.ByteOrder.__members__.keys(), type=str.upper, help='Specifies the byte order of the data in the file.')
    parser.add_argument('-t', '--time', default=5.0, type=float, help='Generation time (s)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Specifies the initial value of certain properties for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.sample_rate, args.file_path, args.byte_order, args.time)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5433 (2CH)', 'BoardType': 'PXIe'}}
    example('PXI1Slot2', options, 40e6, 'data/SineI16BigEndian_1000.bin', 'BIG', 5.0)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe']
    _main(cmd_line)


if __name__ == '__main__':
    main()
