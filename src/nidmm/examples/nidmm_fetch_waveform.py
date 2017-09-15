#!/usr/bin/python

import argparse
import nidmm
import sys
import time

parser = argparse.ArgumentParser(description='Performs a single measurement using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='PXI1Slot2', help='Resource name of a National Instruments Digital Multimeter.')
parser.add_argument('-f', '--function', default='WAVEFORM_VOLTAGE', choices=nidmm.Function.__members__.keys(), type=str.upper, help='Measurement function.')
parser.add_argument('-r', '--range', default=10, type=float, help='Measurement range.')
parser.add_argument('-d', '--digits', default=6.5, type=float, help='Digits of resolution for the measurement.')
parser.add_argument('-s', '--samples', default=10, type=int, help='The number of measurements the DMM makes.')
parser.add_argument('-sr', '--sample_rate', default=1000, type=int, help='The number of measurements the DMM makes.')
parser.add_argument('-to', '--timeout', default=-1, type=int, help='Specifies the maximum_time allowed for this function to complete in milliseconds.')
parser.add_argument('-tc', '--trigger_count', default=1, type=int, help='Sets the number of triggers you want the DMM to receive before returning to the Idle state.')
args = parser.parse_args()


try:
    with nidmm.Session(args.name) as session:
        session.configure_waveform_acquisition(nidmm.Function[args.function], args.range, args.sample_rate, args.samples)
        with session.initiate():
            while True:
                time.sleep(0.1)
                backlog, acquisition_state = session.read_status()
                if (acquisition_state == nidmm.AcquisitionStatus.FINISHED_WITH_NO_BACKLOG):
                    break
                measurements = session.fetch_waveform(args.timeout, backlog)
                print(measurements)


except nidmm.Error as e:
    sys.stderr.write(str(e))
    sys.exit(e.code)
