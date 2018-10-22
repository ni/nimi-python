#!/usr/bin/python
import argparse
import nise
import sys


def example(virtual_device_name, connection):
    with nise.Session(virtual_device_name=virtual_device_name) as session:
        session.connect(connection)
        print(connection, ' is now connected.')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Connects the specified connection specification', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--virtual-device', default='SwitchExecutiveExample', help='NI Switch Executive Virtual Device name')
    parser.add_argument('-c', '--connection', default='DIOToUUT', help='Connection Specification')
    args = parser.parse_args(argsv)
    example(args.virtual_device, args.connection)


def main():
    _main(sys.argv[1:])


def test_example():
    example('SwitchExecutiveExample', 'DIOToUUT')


def test_main():
    cmd_line = []
    _main(cmd_line)


if __name__ == '__main__':
    main()


