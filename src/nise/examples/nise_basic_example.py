#!/usr/bin/python
#FRANKTODO
import argparse
import nise
import sys


def example(virtual_device_name, connection, options):
    with nise.Session(virtual_device_name = virtual_device_name, options=options) as session:
        print('Opening session to', virtual_device_name)
        session.connect(connection)
        print(connection, ' is now connected.')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Connects the specified connection specification', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--virtual-device', default='SwitchExecutiveExample', help='NI Switch Executive Virtual Device name')
    parser.add_argument('-c', '--connection', default='DIOToUUT', help='Connection Specification')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.virtual_device, args.connection, args.option_string)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {}
    example('SwitchExecutiveExample', 'DIOToUUT')


def test_main():
    cmd_line = ['--option-string', '', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()


