import argparse
import nirfsg
import numpy as np
import sys


def example(resource_name, options, frequency, power_level, number_of_samples):
    waveform_data = np.full(number_of_samples, 1 + 0j, dtype=np.complex128)
    with nirfsg.Session(resource_name=resource_name, id_query=False, reset_device=False, options=options) as session:
        session.configure_rf(
            frequency,
            power_level
        )
        session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        session.write_arb_waveform('wfm', waveform_data, False)
        with session.initiate():
            session.check_generation_status()


def _main(argsv):
    parser = argparse.ArgumentParser(description='Continuously generates an arbitrary waveform using NI-RFSG.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='5841', help='Resource name of the NI RF signal generator.')
    parser.add_argument('-f', '--frequency', default=1e9, type=float, help='Frequency in Hz.')
    parser.add_argument('-p', '--power-level', default=-10.0, type=float, help='Power level in dBm.')
    parser.add_argument('-n', '--number-of-samples', default=1000, type=int, help='Number of samples.')
    parser.add_argument('-op', '--option-string', default='Simulate=1, DriverSetup=Model:5841', type=str, help='Option string for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.frequency, args.power_level, args.number_of_samples)


def main():
    _main(sys.argv[1:])


def test_example():
    options = "Simulate=1, DriverSetup=Model:5841"
    example('5841', options, 1e9, -10.0)


def test_main():
    cmd_line = ['--resource-name', '5841', '--frequency', '1e9', '--power-level', '-10', '--number-of-samples', '1000', '--option-string', 'Simulate=1, DriverSetup=Model:5841']
    _main(cmd_line)


if __name__ == '__main__':
    main()