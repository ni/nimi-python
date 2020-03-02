import argparse
import os
import subprocess

parser = argparse.ArgumentParser(description='Runs system tests on the specified driver.',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-d', '--driver', required=True, type=str,
                    help='Python package name.',
                    choices=os.listdir('src'))
parser.add_argument('-pv', '--python-version', required=False, type=str,
                    help='Python version to be run. This is used to invoke the appropriate tox environment.',
                    choices=['py35', 'py36', 'py37', 'py38', ], default='py38')
parser.add_argument('-pb', '--python-bitness', required=False, type=str,
                    help='Python bitness to be run. This is passed to tox.',
                    choices=[None, '--32'], default=None)
args = parser.parse_args()


command = ['python', '-m', 'tox']
if args.python_bitness is not None:
    command.append(args.python_bitness)

drivers_using_other_driver = ['niscope', 'nifgen', 'nidigital', 'nitclk', ]
if args.driver in drivers_using_other_driver:
    # Creating the wheel for the other required driver only uses Python 3.8
    command += ['-e', 'py38-{0}-wheel_dep,'.format(args.driver)]

command += ['-e', '{0}-{1}-system_tests'.format(args.python_version, args.driver)]
command += ['-c', 'tox-system_tests.ini']

print('****Running system tests in tox.****')
results = subprocess.run(command, check=True)

