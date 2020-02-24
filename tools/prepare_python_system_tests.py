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
parser.add_argument('-pv', '--python-version', required=False, type=str, help='Python version to be run.', default=None)
parser.add_argument('-pb', '--python-bitness', required=False, type=str, help='Python bitness to be run.', default=None)
args = parser.parse_args()


print('****Installing tox to Python.****')
results = subprocess.run(["python", '-m', 'pip', 'install', '--disable-pip-version-check', '--upgrade', 'pip', 'tox'], check=True)


print('****Creating temporary directory.****')
temp_dir = tempfile.gettempdir()
working_directory = os.path.join(temp_dir, str(time.time()))
if not os.path.exists(working_directory):
    os.makedirs(working_directory)
print(working_directory)


print('****Parsing GitHub releases to obtain the latest zip file URL.****')
release_url = 'https://api.github.com/repos/ni/nimi-python/releases'
with urllib.request.urlopen(release_url) as response:
    html = response.read()
url_data = json.loads(html.decode('utf-8'))
zip_url = url_data[0]['zipball_url']
print(zip_url)

print('****Downloading latest zip file from github.****')
try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve
my_zip_file = os.path.join(working_directory, 'zip.zip')
urlretrieve(zip_url, my_zip_file)
print('Download complete.')


print('****Unzipping Zip file.****')
zip_folder = os.path.join(working_directory, 'zip_folder')
zip_ref = zipfile.ZipFile(my_zip_file, 'r')
zip_ref.extractall(zip_folder)
zip_ref.close()
print(zip_folder)

drivers_using_other_driver = ['niscope', 'nifgen', 'nidigital', 'nitclk', ]
other_driver_env = ''
if args.driver in drivers_using_other_driver:
    # Creating the wheel for the other required driver only uses Python 3.8
    other_driver_env = 'py38-{0}-wheel_dep,'.format(args.driver)

print('****Invoking build specific script****')
tox_dir = os.path.join(zip_folder, os.listdir(zip_folder)[0], 'generated', args.driver)
os.chdir(tox_dir)
command = ['python', '../../tools/run_python_system_tests.py', '-d', args.driver]
if args.python_version is not None:
    command.append('--python-version', args.python_version)
if args.python_bitness is not None:
    command.append('--python-bitness', args.python_bitness)

results = subprocess.run(command, check=True)

