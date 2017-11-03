#!/usr/bin/python

import argparse
import nidcpower


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


def create_sweep(begin_value, end_value, number_of_steps):
    sweep = []
    for i in range(number_of_steps):
        step_size = (end_value - begin_value) / number_of_steps
        sweep.append(begin_value + i * step_size)
    return sweep


with nidcpower.Session(args.name, channels=args.channels) as session:

    session.source_mode = nidcpower.SourceMode.SEQUENCE
    session.source_delay = 0.1
    session.voltage_level_autorange = nidcpower.VoltageLevelAutorange.ON
    session.current_level_autorange = nidcpower.CurrentLevelAutorange.ON
    session.create_advanced_sequence('my_sequence', attribute_ids)
    voltages = create_sweep(args.voltage_start, args.voltage_final, args.steps)
    currents = create_sweep(args.current_start, args.current_final, args.steps)

    for v in voltages:
        session.create_advanced_sequence_step()
        session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
        session.voltage_level = v

    for c in currents:
        session.create_advanced_sequence_step()
        session.output_function = nidcpower.OutputFunction.DC_CURRENT
        session.current_level = c

    with session.initiate():
        session.wait_for_event(nidcpower.Event.SEQUENCE_ENGINE_DONE)
        voltage_measurements, current_measurements, in_compliance, _ = session.fetch_multiple(args.steps * 2)

    # Print a table with the measurements
    programmed_levels = voltages + currents
    units = ['V'] * args.steps + ['A'] * args.steps
    measurements = zip(programmed_levels, units, voltage_measurements, current_measurements, in_compliance)
    row_format = '{:<8} {:4} {:<25} {:<25} {}'
    print(row_format.format('Sourced', '', 'Measured voltage', 'Measured current', 'In-compliance'))
    for m in measurements:
        print(row_format.format(*m))

