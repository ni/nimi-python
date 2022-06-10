#!/usr/bin/python

import argparse
import nidcpower
import sys


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
        lcr_source_delay_mode,
        lcr_source_delay,
        options):
    with nidcpower.Session(resource_name=resource_name, options=options) as session:

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
        session.lcr_source_delay_mode = lcr_source_delay_mode
        session.source_delay = lcr_source_delay

        with session.initiate():
            session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE, 21.0)
            measurements = session.measure_multiple_lcr()
            print(measurements)

        session.reset()


def _main(argsv):
    parser = argparse.ArgumentParser(description='Uses the LCR AC Voltage Output function to force an output AC voltage to retrieve LCR measurements', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
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
    parser.add_argument('-sdm', '--lcr-source-delay-mode', default=nidcpower.LCRSourceDelayMode.AUTOMATIC, type=int, help='LCR source delay mode')
    parser.add_argument('-sd', '--lcr-source-delay', default=16.66e-3, type=float, help='Source delay')
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
        args.lcr_source_delay_mode,
        args.lcr_source_delay,
        args.option_string,
    )


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4190', 'BoardType': 'PXIe', }, }
    example(
        'PXI1Slot2/0',
        0,
        10e3,
        100.0,
        nidcpower.CableLength.NI_STANDARD_2M,
        700.0e-3,
        nidcpower.LCRDCBiasSource.OFF,
        0.0,
        0.0,
        nidcpower.LCRMeasurementTime.MEDIUM,
        0.0,
        nidcpower.LCRSourceDelayMode.AUTOMATIC,
        16.66e-3,
        options
    )


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4190; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
