#!/usr/bin/python

import argparse
import nidigital
import os
import sys


def example(resource_name, options, source, rising_edge):

    with nidigital.Session(resource_name=resource_name, options=options) as session:

        dir = os.path.dirname(__file__)

        # Configure the session by loading pin map (.pinmap) created in the Digital Pattern Editor on the instrument
        pin_map_filename = os.path.join(dir, 'burst_with_start_trigger_files', 'pin_map.pinmap')
        session.load_pin_map(pin_map_filename)

        # Configure the session by loading the specifications (.sepcs), levels (.digilevels), and timing (.digitiming) files created in the Digital Pattern Editor on the instrument
        spec_filename = os.path.join(dir, 'burst_with_start_trigger_files', 'specifications.specs')
        levels_filename = os.path.join(dir, 'burst_with_start_trigger_files', 'pin_levels.digilevels')
        timing_filename = os.path.join(dir, 'burst_with_start_trigger_files', 'timing.digitiming')
        session.load_specifications_levels_and_timing(spec_filename, levels_filename, timing_filename)

        # Apply the settings from the levels and timing files we just loaded on the instrument.
        session.apply_levels_and_timing(levels_filename, timing_filename)

        # Configure the session by loading the pattern file (.digipat) created in the Digital Pattern Editor on the instrument.
        pattern_filename = os.path.join(dir, 'burst_with_start_trigger_files', 'pattern.digipat')
        session.load_pattern(pattern_filename)

        # Specify a source and edge for the external start trigger
        session.digital_edge_start_trigger_source = source
        session.digital_edge_start_trigger_edge = nidigital.DigitalEdge.RISING if rising_edge else nidigital.DigitalEdge.FALLING

        # Waiting for the trigger to start bursting and then blocks until the pattern is done bursting
        session.burst_pattern('new_pattern')

        # Disconnect all channels using programmable onboard switching
        session.selected_function = nidigital.SelectedFunction.DISCONNECT


def _main(argsv):
    parser = argparse.ArgumentParser(description='Demonstrates how to create and configure an instrument session and to burst a pattern on the digital pattern instrument using a start trigger.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2,PXI1Slot3', help='Resource name of a National Instruments digital pattern instrument')
    parser.add_argument('-s', '--simulated', default=True, type=bool, help='Whether to run on hardware or run on software simulation')
    parser.add_argument('-src', '--source', default='/PXI1Slot2/PXI_Trig0', help='Source terminal where the external signal is connected')
    parser.add_argument('-re', '--rising-edge', default=True, type=bool, help='Trigger on rising edge or falling edge of the signal')
    args = parser.parse_args(argsv)
    example(args.resource_name, 'Simulate=1, DriverSetup=Model:6570' if args.simulated else '', args.source, args.rising_edge)


def main():
    _main(sys.argv[1:])


def test_main():
    _main([])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '6570'}, }
    source = '/PXI1Slot2/PXI_Trig0'
    rising_edge = True
    example('PXI1Slot2,PXI1Slot3', options, source, rising_edge)


if __name__ == '__main__':
    main()
