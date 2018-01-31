#!/usr/bin/python

import nimodinst


def example():
    with nimodinst.Session('') as session:
        if len(session) > 0:
            print("%d items" % len(session))
            print("{: >20} {: >15} {: >10}".format('Name', 'Model', 'S/N'))
        for d in session:
            print('_index = {0}'.format(d._index))
            print("{: >20} {: >15} {: >10}".format(d.device_name, d.device_model, d.serial_number))


def _main():
    example()


def test_example():
    example()


if __name__ == '__main__':
    _main()


