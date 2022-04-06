#!/usr/bin/python

import argparse
import nidcpower
import sys


def print_measurements(measurements):
    print('V DC: {0}'.format(measurements[0].vdc))
    print('I DC: {0}'.format(measurements[0].idc))
    print('Stimulus frequency: {0}'.format(measurements[0].stimulus_frequency))
    print('AC voltage: {0}'.format(measurements[0].ac_voltage))
    print('AC current: {0}'.format(measurements[0].ac_current))
    print('Z: {0}'.format(measurements[0].z))
    print('Z magnitude: {0}'.format(measurements[0].z_magnitude))
    print('Z phase: {0}'.format(measurements[0].z_phase))
    print('Y: {0}'.format(measurements[0].y))
    print('Y magnitude: {0}'.format(measurements[0].y_magnitude))
    print('Y phase: {0}'.format(measurements[0].y_phase))
    print('Ls: {0}'.format(measurements[0].ls))
    print('Cs: {0}'.format(measurements[0].cs))
    print('Rs: {0}'.format(measurements[0].rs))
    print('Lp: {0}'.format(measurements[0].lp))
    print('Cp: {0}'.format(measurements[0].cp))
    print('Rp: {0}'.format(measurements[0].rp))
    print('D: {0}'.format(measurements[0].d))
    print('Q: {0}'.format(measurements[0].q))
    print('Measurement mode: {0}'.format(measurements[0].measurement_mode))
    print('DC in compliance: {0}'.format(measurements[0].dc_in_compliance))
    print('AC in compliance: {0}'.format(measurements[0].ac_in_compliance))
    print('Unbalanced: {0}'.format(measurements[0].unbalanced))


def example(
        resource_name,
        frequency,
        lcr_impedance_range,
        cable_length,
        lcr_voltage_rms,
        lcr_dc_bias_source,
        lcr_dc_bias_voltage_level,
        lcr_dc_bias_current_level,
        lcr_measurement_time,
        lcr_custom_measurement_time,
        lcr_open_compensation_enabled,
        lcr_short_compensation_enabled,
        additional_frequencies,
        options):
    with nidcpower.Session(resource_name=resource_name, options=options) as session:

        if cable_length == nidcpower.CableLength.CUSTOM_AS_CONFIGURED:
            sys.exit('WARNING!, Cable Length - (Custom) As Configured is selected. This cable length option is not supported in this example. Search ni.com for information about NI power supplies/SMUs and the NI-DCPower API.')

        input('\nAction is required! Set up an open connection between the LCR Meter\'s LO CUR, LO POT and HI CUR, HI POT terminals, then press "Enter" to perform LCR open compensation.')
        print('\nPerforming LCR open compensation...')
        session.cable_length = cable_length
        # Call Perform LCR Open Compensation. Calling this function resets most session properties to their default values.
        session.perform_lcr_open_compensation(additional_frequencies)

        input('\nAction is required! Set up a short connection between the LCR Meter\'s LO CUR, LO POT and HI CUR, HI POT terminals, then press "Enter" to perform LCR short compensation.')
        print('\nPerforming LCR short compensation...')
        session.cable_length = cable_length
        # Call Perform LCR Short Compensation. Calling this function resets most session properties to their default values.
        session.perform_lcr_short_compensation(additional_frequencies)

        input('\nAction is required! Set up a connection between the LCR meter and your DUT. Then press "Enter" to proceed to take LCR measurements.\n')

        # Configure the session.
        session.instrument_mode = nidcpower.InstrumentMode.LCR
        session.lcr_stimulus_function = nidcpower.LCRStimulusFunction.VOLTAGE
        session.lcr_frequency = frequency
        session.lcr_impedance_range = lcr_impedance_range
        session.cable_length = cable_length
        session.lcr_voltage_amplitude = lcr_voltage_rms
        session.lcr_dc_bias_source = lcr_dc_bias_source
        session.lcr_dc_bias_voltage_level = lcr_dc_bias_voltage_level
        session.lcr_dc_bias_current_level = lcr_dc_bias_current_level
        session.lcr_measurement_time = lcr_measurement_time
        session.lcr_custom_measurement_time = lcr_custom_measurement_time
        session.lcr_open_short_load_compensation_data_source = nidcpower.LCROpenShortLoadCompensationDataSource.ONBOARD_STORAGE
        # Set LCR Open Compensation Enabled and LCR Short Compensation Enabled to True to apply the open and short LCR compensation corrections to your LCR measurements.
        session.lcr_open_compensation_enabled = lcr_open_compensation_enabled
        session.lcr_short_compensation_enabled = lcr_short_compensation_enabled

        with session.initiate():
            session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE, 21.0)
            measurements = session.measure_multiple_lcr()
            print_measurements(measurements)

        session.reset()


def _main(argsv):
    parser = argparse.ArgumentParser(description='Performs the LCR open compensation, LCR short compensation and retrieves the LCR measurements', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2/0', help='Resource names of National Instruments SMUs')
    parser.add_argument('-f', '--frequency', default=10e3, type=float, help='LCR frequeny')
    parser.add_argument('-i', '--lcr-impedance-range', default=100.0, type=float, help='LCR impedance range')
    parser.add_argument('-cl', '--cable-length', default=nidcpower.CableLength.NI_STANDARD_2M, type=int, help='Cable length')
    parser.add_argument('-vr', '--lcr-voltage-rms', default=700.0e-3, type=float, help='LCR voltage RMS')
    parser.add_argument('-ds', '--lcr-dc-bias-source', default=nidcpower.LCRDCBiasSource.OFF, type=int, help='LCR DC bias source')
    parser.add_argument('-dv', '--lcr-dc-bias-voltage_level', default=0.0, type=float, help='LCR DC bias voltage')
    parser.add_argument('-dc', '--lcr-dc-bias-current_level', default=0.0, type=float, help='LCR DC bias current')
    parser.add_argument('-mt', '--lcr-measurement-time', default=nidcpower.LCRMeasurementTime.MEDIUM, type=int, help='LCR measurement time')
    parser.add_argument('-cmt', '--lcr-custom-measurement-time', default=0.0, type=float, help='LCR custom measurement time seconds')
    parser.add_argument('-oce', '--lcr-open-compensation-enabled', default=True, type=bool, help='LCR open compensation enabled')
    parser.add_argument('-sce', '--lcr-short-compensation-enabled', default=True, type=bool, help='LCR short compensation enabled')
    parser.add_argument('-af', '--additional-frequencies', default=[11.0e3, 12.0e3], nargs='+', type=int, help='Additional LCR frequencies')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(
        args.resource_name,
        args.frequency,
        args.lcr_impedance_range,
        args.cable_length,
        args.lcr_voltage_rms,
        args.lcr_dc_bias_source,
        args.lcr_dc_bias_voltage_level,
        args.lcr_dc_bias_current_level,
        args.lcr_measurement_time,
        args.lcr_custom_measurement_time,
        args.lcr_open_compensation_enabled,
        args.lcr_short_compensation_enabled,
        args.additional_frequencies,
        args.option_string
    )


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4190', 'BoardType': 'PXIe', }, }
    example(
        'PXI1Slot2/0',
        10e3,
        100.0,
        nidcpower.CableLength.NI_STANDARD_2M,
        700.0e-3,
        nidcpower.LCRDCBiasSource.OFF,
        0.0,
        0.0,
        nidcpower.LCRMeasurementTime.MEDIUM,
        0.0,
        True,
        True,
        [11.0e3, 12.0e3],
        options
    )


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4190; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
