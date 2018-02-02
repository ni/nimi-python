#!/usr/bin/python

import argparse
import niscope
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4, width=80)


def example(argsv):
    parser = argparse.ArgumentParser(description='Acquires one record from the given channels.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource_name', default='PXI1Slot2', help='Resource name of a National Instruments Digitizer')
    parser.add_argument('-c', '--channels', default='0', help='Channel(s) to use')
    parser.add_argument('-l', '--length', default='1000', type=int, help='Measure record length')
    parser.add_argument('-v', '--voltage', default=1.0, type=float, help='Voltage range (V)')
    parser.add_argument('-op', '--option_string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)

    with niscope.Session(resource_name=args.resource_name, option_string=args.option_string) as session:
        session.configure_vertical(range=args.voltage, coupling=niscope.VerticalCoupling.AC)
        session.configure_horizontal_timing(min_sample_rate=50000000, min_num_pts=args.length, ref_position=50.0, num_records=1, enforce_realtime=True)
        with session.initiate():
            wfm, wfm_infos = session[args.channels].fetch(num_samples=args.length)
        print('Number of samples acquired: {:,}\n'.format(len(wfm)))
        for i in range(len(wfm_infos)):
            print('Waveform {0} information:'.format(i))
            print(str(wfm_infos[i]) + '\n\n')


def _main():
    example(sys.argv)


def test_example():
    cmd_line = ['-op', 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', ]
    example(cmd_line)


if __name__ == '__main__':
    _main()


