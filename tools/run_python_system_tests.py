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
parser.add_argument('-pv', '--python_version', required=False, type=str, help='Python version to be run.', default='py27')  # pass py36 if wanted to run on python-3.6
parser.add_argument('-pb', '--python_bitness', required=False, type=str, help='Python bitness to be run.', default=' ')  # pass '--32' if you want to run on a 32bit python if both available
args = parser.parse_args()


print('****Installing tox to Python.****')
subprocess.check_call(["python", '-m', 'pip', 'install', '--upgrade', 'pip'])
subprocess.check_call(["python", '-m', 'pip', 'install', '--upgrade', 'tox'])


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


print('****Running system tests in tox.****')
tox_dir = os.path.join(zip_folder, os.listdir(zip_folder)[0])
os.chdir(tox_dir)
result = os.system('tox ' + args.python_bitness + ' -e ' + args.python_version + '-' + args.driver + '_system_tests')
sys.exit(result)
