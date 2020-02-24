import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.request
import zipfile

parser = argparse.ArgumentParser(description='Downloads the latest release nimi-python and runs system tests on the specified driver.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-d', '--driver', required=True, type=str, help='Driver Name.')
parser.add_argument('-pv', '--python-version', required=False, type=str, help='Python version to be run.', default='py38')  # pass py36 if wanted to run on python-3.6
parser.add_argument('-pb', '--python-bitness', required=False, type=str, help='Python bitness to be run.', default=None)  # pass '--32' if you want to run on a 32bit python if both available
args = parser.parse_args()


command = ['python', '-m', 'tox']
if args.python_bitness is not None:
    command.append(args.python_bitness)

drivers_using_other_driver = ['niscope', 'nifgen', 'nidigital', 'nitclk', ]
if args.driver in drivers_using_other_driver:
    # Creating the wheel for the other required driver only uses Python 3.8
    command.append(['-e', 'py38-{0}-wheel_dep,'.format(args.driver)])

command.append(['-e', '{0}-{1}-system_tests'.format(args.python_version, args.driver)])
command.append(['-c', 'tox-system_tests.ini'])

print('****Running system tests in tox.****')
results = subprocess.run(command, check=True)

