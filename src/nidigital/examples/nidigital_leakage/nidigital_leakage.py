#!/usr/bin/python

import argparse
import nidigital
import os
import sys


def example(resource_name, options, power_supply_voltage, test_input_voltages, current_limit):

    with nidigital.Session(resource_name=resource_name, reset_device=True, options=options) as session:

        pin_map_filename = os.path.join(os.path.dirname(__file__), 'PinMap.pinmap')
        session.load_pin_map(pin_map_filename)

        ppmu_pins = 'Power,Digital_In'
        input_pins = 'Digital_In'
        power_pins = 'Power'
        ppmu_channels = session.channels[ppmu_pins]
        input_channels = session.channels[input_pins]
        power_channels = session.channels[power_pins]

        try:
            ppmu_channels.selected_function = nidigital.SelectedFunction.PPMU
            ppmu_channels.ppmu_aperture_time = 20e-6
            ppmu_channels.ppmu_aperture_time_units = nidigital.PPMUApertureTimeUnits.SECONDS

            input_channels.ppmu_output_function = nidigital.PPMUOutputFunction.VOLTAGE
            input_channels.ppmu_current_limit_range = 10e-6

            power_channels.ppmu_output_function = nidigital.PPMUOutputFunction.VOLTAGE
            power_channels.ppmu_current_limit_range = 10e-3
            power_channels.ppmu_voltage_level = power_supply_voltage
            power_channels.ppmu_source()

            pin_info = input_channels.get_pin_results_pin_information()

            for voltage in test_input_voltages:
                input_channels.ppmu_voltage_level = voltage
                input_channels.ppmu_source()
                current_measurements = input_channels.ppmu_measure(nidigital.PPMUMeasurementType.CURRENT)

                for pin, current in zip(pin_info, current_measurements):
                    result = 'PASS' if abs(current) <= current_limit else 'FAIL'
                    print(f'Site {pin.site_number}, pin {pin.pin_name}: {current:g} A at {voltage:g} V, {result}')
        finally:
            session.selected_function = nidigital.SelectedFunction.DISCONNECT

    print('Done measuring leakage')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Demonstrates how to measure leakage on selected NI-Digital input pins.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2,PXI1Slot3', help='Resource name of NI digital pattern instruments. Ensure the resource names match the pin map.')
    parser.add_argument('-s', '--simulate', default='True', choices=['True', 'False'], help='Whether to run on simulated hardware or real hardware')
    parser.add_argument('-pv', '--power-supply-voltage', default=3.3, type=float, help='Power supply voltage applied to the DUT in volts')
    parser.add_argument('-tv', '--test-input-voltages', default=[0.0, 3.0], type=float, nargs='+', help='Test voltages applied to the digital input pins in volts')
    parser.add_argument('-cl', '--current-limit', default=25e-6, type=float, help='Maximum absolute leakage current for a passing result in amps')
    args = parser.parse_args(argsv)

    options = 'Simulate=1, DriverSetup=Model:6570' if args.simulate == 'True' else ''
    example(args.resource_name, options, args.power_supply_voltage, args.test_input_voltages, args.current_limit)


def main():
    _main(sys.argv[1:])


def test_main():
    _main([])
    _main(['--power-supply-voltage', '3.0', '--test-input-voltages', '0', '1.5', '3', '--current-limit', '10e-6'])


def test_example():
    resource_name = 'PXI1Slot2,PXI1Slot3'
    options = {'simulate': True, 'driver_setup': {'Model': '6570'}, }
    power_supply_voltage = 3.3
    test_input_voltages = [0.0, 3.0]
    current_limit = 25e-6
    example(resource_name, options, power_supply_voltage, test_input_voltages, current_limit)


if __name__ == '__main__':
    main()
