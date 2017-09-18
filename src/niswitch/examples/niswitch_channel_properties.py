#!/usr/bin/python

import argparse
import niswitch
import sys

parser = argparse.ArgumentParser(description='TODO: write something.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='PXI1Slot2', help='Resource name of a National Instruments Switch.')
args = parser.parse_args()

try:
    with niswitch.Session(args.name) as session:
        with session.channel("Marcos") as chan:
            print('channel {0} bandwidth is {1}'.format(chan, chan.bandwidth))
except niswitch.Error as e:
    sys.stderr.write(str(e))
    sys.exit(e.code)
