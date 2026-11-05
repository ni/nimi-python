#!/usr/bin/python

import argparse
import nidigital
import os
import sys


def example(resource_name, options, force_current, high_limit, low_limit):

    with nidigital.Session(resource_name=resource_name, reset_device=True, options=options) as session:

        pin_map_filename = os.path.join(os.path.dirname(__file__), 'PinMap.pinmap')
        session.load_pin_map(pin_map_filename)

        all_pins = 'All_Pins'
        power_pins = 'Power'
        continuity_pins = 'Digital_In,Digital_Out'

        try:
            session.channels[all_pins].selected_function = nidigital.SelectedFunction.PPMU
            session.channels[all_pins].ppmu_aperture_time = 20e-6
            session.channels[all_pins].ppmu_aperture_time_units = nidigital.PPMUApertureTimeUnits.SECONDS

            session.channels[power_pins].ppmu_output_function = nidigital.PPMUOutputFunction.VOLTAGE
            session.channels[power_pins].ppmu_current_limit_range = 10e-3
            session.channels[power_pins].ppmu_voltage_level = 0
            session.channels[power_pins].ppmu_source()

            session.channels[continuity_pins].ppmu_output_function = nidigital.PPMUOutputFunction.CURRENT
            session.channels[continuity_pins].ppmu_current_level_range = 32e-6
            session.channels[continuity_pins].ppmu_voltage_limit_high = 1.5
            session.channels[continuity_pins].ppmu_voltage_limit_low = -1.5

            pin_info = session.channels[continuity_pins].get_pin_results_pin_information()

            session.channels[continuity_pins].ppmu_current_level = force_current
            session.channels[continuity_pins].ppmu_source()
            positive_measurements = session.channels[continuity_pins].ppmu_measure(nidigital.PPMUMeasurementType.VOLTAGE)

            session.channels[continuity_pins].ppmu_current_level = -force_current
            session.channels[continuity_pins].ppmu_source()
            negative_measurements = session.channels[continuity_pins].ppmu_measure(nidigital.PPMUMeasurementType.VOLTAGE)

            for pin, positive_voltage, negative_voltage in zip(pin_info, positive_measurements, negative_measurements):
                passed = low_limit <= positive_voltage <= high_limit and -high_limit <= negative_voltage <= -low_limit
                result = 'PASS' if passed else 'FAIL'
                print(f'Site {pin.site_number}, pin {pin.pin_name}: '
                      f'positive {positive_voltage:.6f} V, negative {negative_voltage:.6f} V, {result}')
        finally:
            session.selected_function = nidigital.SelectedFunction.DISCONNECT

    print('Done measuring continuity')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Demonstrates how to measure continuity on selected NI-Digital pins.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2,PXI1Slot3', help='Resource name of NI digital pattern instruments. Ensure the resource names match the pin map.')
    parser.add_argument('-s', '--simulate', default='True', choices=['True', 'False'], help='Whether to run on simulated hardware or real hardware')
    parser.add_argument('-fc', '--force-current', default=25e-6, type=float, help='Magnitude of the force current in amps')
    parser.add_argument('-hl', '--high-limit', default=0.8, type=float, help='High diode forward-voltage limit in volts')
    parser.add_argument('-ll', '--low-limit', default=0.4, type=float, help='Low diode forward-voltage limit in volts')
    args = parser.parse_args(argsv)

    options = 'Simulate=1, DriverSetup=Model:6570' if args.simulate == 'True' else ''
    example(args.resource_name, options, args.force_current, args.high_limit, args.low_limit)


def main():
    _main(sys.argv[1:])


def test_main():
    _main([])


def test_example():
    resource_name = 'PXI1Slot2,PXI1Slot3'
    options = {'simulate': True, 'driver_setup': {'Model': '6570'}, }
    force_current = 25e-6
    high_limit = 0.8
    low_limit = 0.4
    example(resource_name, options, force_current, high_limit, low_limit)


if __name__ == '__main__':
    main()
