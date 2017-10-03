#!/usr/bin/python

import argparse
import nidcpower
import sys


parser = argparse.ArgumentParser(description='Outputs the specified Voltage Level, then takes multiple voltage and current readings.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='PXI1Slot2', help='Resource name of a National Instruments SMU')
parser.add_argument('-l', '--length', default='100', type=int, help='Measure record length')
parser.add_argument('-v', '--voltage', default=5.0, type=float, help='Voltage level')
args = parser.parse_args()

try:
    with nidcpower.Session(args.name) as session:
        # Placeholder. Use "NI-DCPower Advanced Sequence Changing Output Function.vi" as reference
        pass
except nidcpower.Error as e:
    sys.stderr.write(str(e))
    sys.exit(e.code)
