import os
import sys
import pip
import time
import json
import zipfile
import argparse
import tempfile
import urllib.request

parser = argparse.ArgumentParser(description='Downloads the latest release nimi-python and runs system tests on the specified driver.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-d', '--driver', required=True, type=str, help='Driver Name.')
args = parser.parse_args()


print('****Installing tox to Python.****')
pip.main(['install', 'tox'])


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
url_data = json.loads(html.decode('ascii'))
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
result = os.system('python -m tox -e ' + args.driver + '_system_tests')
sys.exit(result)
