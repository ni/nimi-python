#!/usr/bin/python

import argparse
import nidmm
import sys

parser = argparse.ArgumentParser(description='Performs a multipoint measurement using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='PXI1Slot2', help='Resource name of a National Instruments Digital Multimeter.')
parser.add_argument('-f', '--function', default='DC_VOLTS', choices=nidmm.Function.__members__.keys(), type=str.upper, help='Measurement function.')
parser.add_argument('-r', '--range', default=10, type=float, help='Measurement range.')
parser.add_argument('-d', '--digits', default=6.5, type=float, help='Digits of resolution for the measurement.')
parser.add_argument('-s', '--samples', default=10, type=int, help='The number of measurements the DMM makes.')
parser.add_argument('-t', '--triggers', default=1, type=int, help='Sets the number of triggers you want the DMM to receive before returning to the Idle state.')
args = parser.parse_args()

try:
    with nidmm.Session(args.name) as session:
        session.configure_measurement_digits(nidmm.Function[args.function], args.range, args.digits)
        session.configure_multi_point(args.triggers, args.samples, nidmm.SampleTrigger.IMMEDIATE, sample_interval=-1)
        measurements, numberOfMeasurements = session.read_multi_point(maximum_time=-1, array_size=args.samples)
        print('Number of measurements: ', numberOfMeasurements)
        print('Measurements: ', measurements)
except nidmm.Error as e:
    sys.stderr.write(str(e))
    sys.exit(e.code)
