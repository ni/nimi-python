#!/usr/bin/python

import nimodinst


def example():
    with nimodinst.Session('') as session:
        if len(session) > 0:
            print("%d items" % len(session))
            print("{: >20} {: >15} {: >10}".format('Name', 'Model', 'S/N'))
        for d in session:
            print(f"{d.device_name: >20} {d.device_model: >15} {d.serial_number: >10}")


def _main():
    example()


def test_example():
    example()


if __name__ == '__main__':
    _main()


