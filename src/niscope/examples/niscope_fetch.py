#!/usr/bin/python

import argparse
import niscope
import pprint

pp = pprint.PrettyPrinter(indent=4, width=80)

parser = argparse.ArgumentParser(description='Outputs the specified voltage, then takes the specified number of voltage and current readings.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='PXI1Slot2', help='Resource name of a National Instruments SMU')
parser.add_argument('-c', '--channels', default='0', help='Channel(s) to use')
parser.add_argument('-l', '--length', default='1000', type=int, help='Measure record length')
parser.add_argument('-v', '--voltage', default=1.0, type=float, help='Voltage range')
args = parser.parse_args()

with niscope.Session(args.name, False, False, 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe') as session:
    session.configure_vertical(args.voltage, 0.0, 0, 1.0, True)
    session.configure_horizontal_timing(50000000, args.length, 50.0, 1, True)
    with session.initiate():
        wfm, wfm_infos = session[args.channels].fetch(1, args.length)
        print(len(wfm))
        for wfm_info in wfm_infos:
            print('Absolute X0: {0}'.format(wfm_info.absolute_initial_x))
            print('Relative X0: {0}'.format(wfm_info.relative_initial_x))
            print('dt: {0}'.format(wfm_info.x_increment))
            print('actual samples: {0}'.format(wfm_info.actual_samples))
            print('offset: {0}'.format(wfm_info.offset))
            print('gain: {0}'.format(wfm_info.gain))
            print('reserved1: {0}'.format(wfm_info.reserved1))
            print('reserved2: {0}'.format(wfm_info.reserved2))

