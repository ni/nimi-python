import argparse
import nirfsg
import sys


def example(resource_name, options, frequency, power_level):
    with nirfsg.Session(resource_name=resource_name, id_query=False, reset_device=False, options=options) as session:
        # Configure RF settings
        session.configure_rf(
            frequency,  # Frequency in Hz
            power_level  # Power level in dBm
        )
        session.generation_mode = nirfsg.GenerationMode.CW

        # Start generation
        with session.initiate():
            session.check_generation_status()


def _main(argsv):
    parser = argparse.ArgumentParser(description='Generates a continuous wave (CW) signal using NI-RFSG.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='5841', help='Resource name of the NI RF signal generator.')
    parser.add_argument('-f', '--frequency', default=1e9, type=float, help='Frequency in Hz.')
    parser.add_argument('-p', '--power-level', default=-10.0, type=float, help='Power level in dBm.')
    parser.add_argument('-op', '--option-string', default='Simulate=1, DriverSetup=Model:5841', type=str, help='Option string for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.frequency, args.power_level)


def main():
    _main(sys.argv[1:])


def test_example():
    options = "Simulate=1, DriverSetup=Model:5841"
    example('5841', options, 1e9, -10.0)


def test_main():
    cmd_line = ['--resource-name', '5841', '--frequency', '1e9', '--power-level', '-10', '--option-string', 'Simulate=1, DriverSetup=Model:5841']
    _main(cmd_line)


if __name__ == '__main__':
    main()