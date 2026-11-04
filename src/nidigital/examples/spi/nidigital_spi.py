#!/usr/bin/python

import argparse
import nidigital
import os
import sys


def example(resource_name, options, start_label='SPI_Pattern'):

    with nidigital.Session(resource_name=resource_name, options=options) as session:

        dir = os.path.join(os.path.dirname(__file__))

        # Load the pin map (.pinmap) created using the Digital Pattern Editor
        pin_map_filename = os.path.join(dir, 'PinMap.pinmap')
        session.load_pin_map(pin_map_filename)

        # Load the specifications (.specs), levels (.digilevels), and timing (.digitiming) sheets created using the Digital Pattern Editor
        spec_filename = os.path.join(dir, 'Specifications.specs')
        levels_filename = os.path.join(dir, 'PinLevels.digilevels')
        timing_filename = os.path.join(dir, 'Timing.digitiming')
        session.load_specifications_levels_and_timing(spec_filename, levels_filename, timing_filename)

        # Apply the settings from the levels and timing sheets we just loaded to the session
        session.apply_levels_and_timing(levels_filename, timing_filename)

        # Load the pattern file (.digipat) created using the Digital Pattern Editor
        pattern_filename = os.path.join(dir, 'Pattern.digipat')
        session.load_pattern(pattern_filename)

        # Burst the pattern from the start label and block until the pattern is done bursting
        # The returned dictionary maps each site number to its pass/fail result
        site_pass_fail_results = session.burst_pattern(start_label=start_label)

        # Disconnect all channels using programmable onboard switching
        session.selected_function = nidigital.SelectedFunction.DISCONNECT

    for site, passed in site_pass_fail_results.items():
        print('Site {}: {}'.format(site, 'Pass' if passed else 'Fail'))


def _main(argsv):
    parser = argparse.ArgumentParser(description='Demonstrates how to burst an SPI pattern on the digital pattern instrument and display the pass/fail result for each site.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2,PXI1Slot3', help='Resource name of a NI digital pattern instrument. Ensure the resource name matches the instrument name in the pinmap file.')
    parser.add_argument('-s', '--simulate', default='True', choices=['True', 'False'], help='Whether to run on simulated hardware or real hardware')
    parser.add_argument('-l', '--start-label', default='SPI_Pattern', help='Pattern label or name of the pattern from which to start bursting.')
    args = parser.parse_args(argsv)

    example(args.resource_name,
            'Simulate=1, DriverSetup=Model:6570' if args.simulate == 'True' else '',
            args.start_label)


def main():
    _main(sys.argv[1:])


def test_main():
    _main([])


def test_example():
    resource_name = 'PXI1Slot2,PXI1Slot3'
    options = {'simulate': True, 'driver_setup': {'Model': '6570'}, }
    start_label = 'SPI_Pattern'
    example(resource_name, options, start_label)


if __name__ == '__main__':
    main()
