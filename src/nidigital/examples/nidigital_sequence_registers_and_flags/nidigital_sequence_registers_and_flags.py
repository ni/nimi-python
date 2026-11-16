#!/usr/bin/python

import argparse
import nidigital
import os
import sys
import time


def example(resource_name, options):

    with nidigital.Session(resource_name=resource_name, reset_device=True, options=options) as session:

        example_dir = os.path.dirname(__file__)
        pin_map_filename = os.path.join(example_dir, 'PinMap.pinmap')
        session.load_pin_map(pin_map_filename)

        spec_filename = os.path.join(example_dir, 'Specifications.specs')
        levels_filename = os.path.join(example_dir, 'PinLevels.digilevels')
        timing_filename = os.path.join(example_dir, 'Timing.digitiming')
        session.load_specifications_levels_and_timing(spec_filename, levels_filename, timing_filename)
        session.apply_levels_and_timing(levels_filename, timing_filename)

        pattern_filename = os.path.join(example_dir, 'Pattern.digipat')
        session.load_pattern(pattern_filename)

        try:
            session.write_sequencer_register(nidigital.SequencerRegister.REGISTER0, 100)

            print('Start bursting pattern')
            session.burst_pattern(start_label='new_pattern', wait_until_done=False)

            session.write_sequencer_register(nidigital.SequencerRegister.REGISTER1, 50)
            register_value = session.read_sequencer_register(nidigital.SequencerRegister.REGISTER1)

            flag0_state = session.read_sequencer_flag(nidigital.SequencerFlag.FLAG0)
            if session.simulate:
                # Simulated hardware does not update sequencer flag states.
                session.write_sequencer_flag(nidigital.SequencerFlag.FLAG1, True)
            else:
                while not flag0_state:
                    time.sleep(0.01)
                    flag0_state = session.read_sequencer_flag(nidigital.SequencerFlag.FLAG0)
                input('Press Enter to write seqflag1 as True: ')
                session.write_sequencer_flag(nidigital.SequencerFlag.FLAG1, True)

            flag0_state = session.read_sequencer_flag(nidigital.SequencerFlag.FLAG0)
            flag1_state = session.read_sequencer_flag(nidigital.SequencerFlag.FLAG1)
            print(f'reg1 value: {register_value}, seqflag0 state: {flag0_state}, seqflag1 state: {flag1_state}')

            session.wait_until_done()
        finally:
            session.selected_function = nidigital.SelectedFunction.DISCONNECT
    print('Done bursting pattern')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Demonstrates how to read and write sequencer registers and flags during a digital pattern.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2,PXI1Slot3', help='The specified resource name shown in Measurement & Automation Explorer (MAX) for a digital pattern instrument.')
    parser.add_argument('-s', '--simulate', default='True', choices=['True', 'False'], help='Whether to run on simulated hardware or real hardware')
    args = parser.parse_args(argsv)

    options = 'Simulate=1, DriverSetup=Model:6570' if args.simulate == 'True' else ''
    example(args.resource_name, options)


def main():
    _main(sys.argv[1:])


def test_main():
    _main([])


def test_example():
    resource_name = 'PXI1Slot2,PXI1Slot3'
    options = {'simulate': True, 'driver_setup': {'Model': '6570'}, }
    example(resource_name, options)


if __name__ == '__main__':
    main()
