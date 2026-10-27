#!/usr/bin/python

import argparse
import nifgen
import sys
import time


def example(resource_name, options, waveform, amplitude, frequency, offset, phase, gen_time):
    with nifgen.Session(resource_name=resource_name, channel_name='0', options=options) as session:
        session.output_mode = nifgen.OutputMode.FUNC
        session.configure_standard_waveform(waveform=nifgen.Waveform[waveform], amplitude=amplitude, frequency=frequency, dc_offset=offset, start_phase=phase)
        session.output_enabled = True
        with session.initiate():
            print('Generating {} waveform for {} seconds:'.format(waveform, gen_time))
            print('  Frequency: {} Hz, amplitude: {} Vpk-pk, DC offset: {} V, start phase: {} degrees'.format(frequency, amplitude, offset, phase))
            time.sleep(gen_time)


def _main(argsv):
    supported_waveforms = list(nifgen.Waveform.__members__.keys())[:-1]  # no support for user-defined waveforms in example
    parser = argparse.ArgumentParser(description='Generates a standard function waveform.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Specifies the NI-FGEN resource name or alias to initialize.')
    parser.add_argument('-w', '--waveform', default=supported_waveforms[0], choices=supported_waveforms, type=str.upper, help='Specifies the standard waveform shape to generate, such as SINE or SQUARE.')
    parser.add_argument('-a', '--amplitude', default=1.0, type=float, help='Specifies the peak-to-peak output amplitude in volts.')
    parser.add_argument('-f', '--frequency', default=1000000, type=float, help='Specifies the output frequency of the waveform in hertz.')
    parser.add_argument('-o', '--offset', default=0.0, type=float, help='Specifies the DC voltage offset applied to the waveform.')
    parser.add_argument('-p', '--phase', default=0.0, type=float, help='Specifies the starting phase angle of the waveform in degrees.')
    parser.add_argument('-t', '--time', default=5.0, type=float, help='Specifies how long to generate the waveform before stopping, in seconds.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Specifies NI-FGEN initialization options, such as simulation and driver setup.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.waveform, args.amplitude, args.frequency, args.offset, args.phase, args.time)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5433 (2CH)', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'SINE', 1.0, 1000000, 0.0, 0.0, 0.1)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe', '--time', '0.1', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
