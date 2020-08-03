import argparse
import os
import pathlib
import subprocess


base_dir = next(pathlib.Path.cwd().glob('system_tests/*nimi-python*'))
src_dir = base_dir.joinpath('src')

parser = argparse.ArgumentParser(description='Runs system tests for the specified nimi-python module.',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-m', '--module', required=True, type=str,
                    help='nimi-python module name.',
                    choices=[x.name for x in src_dir.iterdir() if x.is_dir()])
parser.add_argument('-pv', '--python-version', required=False, type=str,
                    help='Python version to be run. This is used to invoke the appropriate tox environment.',
                    choices=['py35', 'py36', 'py37', 'py38', ], default='py38')
parser.add_argument('-pb', '--python-bitness', required=False, type=str,
                    help="""
                    Python bitness to be run. "32" means pass "--32" to tox, which
                    will force 32 bit. "any" does not pass anything to tox, so it
                    will used whatever bitness is installed, preferring 64 if available""",
                    choices=['32', 'any'], default='any')  # We disallow None and force 'any' to be the default
args = parser.parse_args()


tox_dir = base_dir.joinpath('generated', args.module)
os.chdir(tox_dir)
command = ['python', '-m', 'tox']
if args.python_bitness != 'any':  # This means it must be '32'
    command.append('--32')

drivers_using_other_driver = ['niscope', 'nifgen', 'nidigital', 'nitclk', ]
if args.module in drivers_using_other_driver:
    # Creating the wheel for the other required module only uses Python 3.8
    command += ['-e', 'py38-{0}-wheel_dep,'.format(args.module)]

command += ['-e', '{0}-{1}-system_tests'.format(args.python_version, args.module)]
command += ['-c', 'tox-system_tests.ini']

print('****Running system tests in tox.****')
print(command)
results = subprocess.run(command, check=True)

