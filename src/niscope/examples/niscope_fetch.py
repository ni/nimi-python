#!/usr/bin/python

import argparse
import niscope
import pprint

pp = pprint.PrettyPrinter(indent=4, width=80)

parser = argparse.ArgumentParser(description='Acquires one record from the given channels.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='PXI1Slot2', help='Resource name of a National Instruments Digitizer')
parser.add_argument('-c', '--channels', default='0', help='Channel(s) to use')
parser.add_argument('-l', '--length', default='1000', type=int, help='Measure record length')
parser.add_argument('-v', '--voltage', default=1.0, type=float, help='Voltage range')
args = parser.parse_args()

with niscope.Session(args.name, False, False, '') as session:
    session.configure_vertical(args.voltage, 0.0, 0, 1.0, True)
    session.configure_horizontal_timing(50000000, args.length, 50.0, 1, True)
    with session.initiate():
        wfm, wfm_infos = session[args.channels].fetch(1, args.length)
    print('Number of samples acquired: {:,}\n'.format(len(wfm)))
    print('Number of samples acquired: {:,}\n'.format(len(wfm)))
    for i in range(len(wfm_infos)):
        print('Waveform {0} information:'.format(i))
        print(wfm_infos[i] + '\n\n')


