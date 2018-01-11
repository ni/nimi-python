#!/usr/bin/python

import argparse
import niscope
import numpy
import platform
import pprint
import sys
import time

pp = pprint.PrettyPrinter(indent=4, width=80)

parser = argparse.ArgumentParser(description='Acquires one record from the given channels.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--resource_name', default='PXI1Slot2', help='Resource name of a National Instruments Digitizer')
parser.add_argument('-c', '--channels', default='0', help='Channel(s) to use')
parser.add_argument('-v', '--voltage', default=1.0, type=float, help='Voltage range (V)')
parser.add_argument('-op', '--option_string', default='', type=str, help='Option string')
args = parser.parse_args()

record_lens = [1000, 100000, 1000000, 5000000, 8300000, 15000000, 20000000]
with niscope.Session(resource_name=args.resource_name, option_string=args.option_string) as session:
    session.configure_vertical(range=args.voltage, coupling=niscope.VerticalCoupling.AC)
    bitness = platform.architecture()[0]
    py_version = '{0}.{1}.{2}'.format(sys.version_info.major, sys.version_info.minor, sys.version_info.micro)
    print('    * Python {0}, {1}\n'.format(py_version, bitness))
    print('        type | list | array | numpy array')
    print('        --- | --- | --- | ---')

    for rec_len in record_lens:
        session.configure_horizontal_timing(min_sample_rate=50000000, min_num_pts=rec_len, ref_position=50.0, num_records=1, enforce_realtime=True)
        try:
            session.commit()
        except niscope.Error:
            continue
        except MemoryError:
            continue

        with session.initiate():
            while session.acquisition_status() != niscope.AcquisitionStatus.COMPLETE:
                pass
            try:
                list_time_start = time.time()
                wfm, wfm_info = session[args.channels].fetch(num_samples=rec_len)
                list_time = time.time() - list_time_start
            except MemoryError:
                list_time = 0
        with session.initiate():
            while session.acquisition_status() != niscope.AcquisitionStatus.COMPLETE:
                pass
            try:
                array_time_start = time.time()
                wfm, wfm_info = session[args.channels].fetch_array(num_samples=rec_len)
                array_time = time.time() - array_time_start
            except MemoryError:
                array_time = 0
        with session.initiate():
            while session.acquisition_status() != niscope.AcquisitionStatus.COMPLETE:
                pass
            try:
                wfm = numpy.empty(rec_len, dtype=float, order='C')
                numpy_time_start = time.time()
                wfm_info = session[args.channels].fetch_into(wfm)
                numpy_time = time.time() - numpy_time_start
            except MemoryError:
                numpy_time = 0

        print('        {0} | {1:.5f} | {2:.5f} | {3:.5f}'.format(rec_len, list_time, array_time, numpy_time))

    print('\n')


