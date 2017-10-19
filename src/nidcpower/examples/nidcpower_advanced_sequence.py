#!/usr/bin/python

import argparse
import nidcpower
import sys


parser = argparse.ArgumentParser(description='Performs voltage sweep then a current sweep.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='PXI1Slot2', help='Resource name of a National Instruments SMU')
parser.add_argument('-c', '--channels', default='0', help='Channel(s) to use')
parser.add_argument('-s', '--steps', default='10', type=int, help='Number of steps per sweep')
parser.add_argument('-v0', '--voltage_start', default=1.0, type=float, help='Voltage level at which sweep starts')
parser.add_argument('-vf', '--voltage_final', default=3.0, type=float, help='Voltage level at which sweep ends')
parser.add_argument('-c0', '--current_start', default=100e-6, type=float, help='Current level at which sweep starts')
parser.add_argument('-cf', '--current_final', default=300e-6, type=float, help='Current level at which sweep ends')
args = parser.parse_args()

# The Python API should provide these values. But it doesn't. Issue #504. For now, put magic values here.
attribute_ids = [
    1150008,  # output_function
    1250001,  # voltage_level
    1150009,  # current_level
]

with nidcpower.Session(args.name, channels=args.channels) as session:

    session.source_mode = nidcpower.SourceMode.SEQUENCE
    session.source_delay = 0.1
    session.voltage_level_autorange = nidcpower.VoltageLevelAutorange.ON
    session.current_level_autorange = nidcpower.CurrentLevelAutorange.ON
    session.create_advanced_sequence('my_sequence', attribute_ids)

    for v in range(args.v0, args.vf, (args.vf-args.v0 / args.steps)):
        print(v)
        session.create_advanced_sequence_step()
        session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
        session.voltage_level = v

    for c in range(args.c0, args.cf, (args.cf-args.c0 / args.steps)):
        print(c)
        session.create_advanced_sequence_step()
        session.output_function = nidcpower.OutputFunction.DC_CURRENT
        session.current_level = c

    with session.initiate():
        session.wait_for_event(nidcpower.EventId.SEQUENCE_ENGINE_DONE_EVENT)
        print(session.fetch_multiple(args.steps*2))

