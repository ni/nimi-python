#!/usr/bin/python

import argparse
import niscope

parser = argparse.ArgumentParser(description='Outputs the specified voltage, then takes the specified number of voltage and current readings.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='PXI1Slot2', help='Resource name of a National Instruments SMU')
parser.add_argument('-c', '--channels', default='0', help='Channel(s) to use')
parser.add_argument('-l', '--length', default='20', type=int, help='Measure record length')
parser.add_argument('-v', '--voltage', default=5.0, type=float, help='Voltage level')
args = parser.parse_args()

with niscope.Session(args.name, channels=args.channels) as session:
    pass

