#!/usr/bin/python

import argparse
import nidcpower
import sys


def example(
    resource_name,
    options,
    lcr_frequency,
    lcr_impedance_range,
    cable_length,
    lcr_voltage_rms,
    lcr_dc_bias_source,
    lcr_dc_bias_voltage_level,
    lcr_measurement_time,
    lcr_custom_measurement_time,
    lcr_source_delay_mode,
    source_delay,
):
    with nidcpower.Session(resource_name=resource_name, options=options) as session:
        # Configure the session.
        session.instrument_mode = nidcpower.InstrumentMode.LCR
        session.lcr_stimulus_function = nidcpower.LCRStimulusFunction.VOLTAGE
        session.lcr_frequency = lcr_frequency
        session.lcr_impedance_range = lcr_impedance_range
        session.cable_length = cable_length
        session.lcr_voltage_amplitude = lcr_voltage_rms
        session.lcr_dc_bias_source = lcr_dc_bias_source
        session.lcr_dc_bias_voltage_level = lcr_dc_bias_voltage_level
        session.lcr_measurement_time = lcr_measurement_time
        session.lcr_custom_measurement_time = lcr_custom_measurement_time
        session.lcr_source_delay_mode = lcr_source_delay_mode
        session.source_delay = source_delay

        with session.initiate():
            # Low frequencies require longer settling times than the default timeout for
            # wait_for_event(), hence 5.0s is set here as a reasonable timeout value
            session.wait_for_event(event_id=nidcpower.Event.SOURCE_COMPLETE, timeout=5.0)
            measurements = session.measure_multiple_lcr()
            for measurement in measurements:
                print(measurement)

        session.reset()


def _main(argsv):
    parser = argparse.ArgumentParser(
        description='Output the specified AC voltage and DC bias voltage, then takes LCR measurements',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2/0', help='Resource names of NI SMUs')
    parser.add_argument('-f', '--lcr-frequency', default=10.0e3, type=float, help='LCR frequency (Hz)')
    parser.add_argument('-i', '--lcr-impedance-range', default=100.0, type=float, help='LCR impedance range (Ω)')
    parser.add_argument('-c', '--cable-length', default='NI_STANDARD_2M', type=str, choices=tuple(nidcpower.CableLength.__members__.keys()), help='Cable length')
    parser.add_argument('-v', '--lcr-voltage-rms', default=700.0e-3, type=float, help='LCR voltage RMS (V RMS)')
    parser.add_argument('-d', '--lcr-dc-bias-source', default='OFF', type=str, choices=tuple(nidcpower.LCRDCBiasSource.__members__.keys()), help='LCR DC bias source')
    parser.add_argument('-dv', '--lcr-dc-bias-voltage_level', default=0.0, type=float, help='LCR DC bias voltage (V)')
    parser.add_argument('-t', '--lcr-measurement-time', default='MEDIUM', type=str, choices=tuple(nidcpower.LCRMeasurementTime.__members__.keys()), help='LCR measurement time')
    parser.add_argument('-ct', '--lcr-custom-measurement-time', default=10.0e-3, type=float, help='LCR custom measurement time (s)')
    parser.add_argument('-sm', '--lcr-source-delay-mode', default='AUTOMATIC', type=str, choices=tuple(nidcpower.LCRSourceDelayMode.__members__.keys()), help='LCR source delay mode')
    parser.add_argument('-s', '--source-delay', default=16.66e-3, type=float, help='Source delay (s)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(
        resource_name=args.resource_name,
        options=args.option_string,
        lcr_frequency=args.lcr_frequency,
        lcr_impedance_range=args.lcr_impedance_range,
        cable_length=getattr(nidcpower.CableLength, args.cable_length),
        lcr_voltage_rms=args.lcr_voltage_rms,
        lcr_dc_bias_source=getattr(nidcpower.LCRDCBiasSource, args.lcr_dc_bias_source),
        lcr_dc_bias_voltage_level=args.lcr_dc_bias_voltage_level,
        lcr_measurement_time=getattr(nidcpower.LCRMeasurementTime, args.lcr_measurement_time),
        lcr_custom_measurement_time=args.lcr_custom_measurement_time,
        lcr_source_delay_mode=getattr(nidcpower.LCRSourceDelayMode, args.lcr_source_delay_mode),
        source_delay=args.source_delay,
    )


def main():
    _main(sys.argv[1:])


def test_example():
    example(
        resource_name='PXI1Slot2/0',
        options={'simulate': True, 'driver_setup': {'Model': '4190', 'BoardType': 'PXIe', }, },
        lcr_frequency=10.0e3,
        lcr_impedance_range=100.0,
        cable_length=nidcpower.CableLength.NI_STANDARD_2M,
        lcr_voltage_rms=700.0e-3,
        lcr_dc_bias_source=nidcpower.LCRDCBiasSource.OFF,
        lcr_dc_bias_voltage_level=0.0,
        lcr_measurement_time=nidcpower.LCRMeasurementTime.MEDIUM,
        lcr_custom_measurement_time=10.0e-3,
        lcr_source_delay_mode=nidcpower.LCRSourceDelayMode.AUTOMATIC,
        source_delay=16.66e-3,
    )


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4190; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
