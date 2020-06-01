import argparse
import json
import pathlib
import subprocess
import tempfile
import time
import urllib.request
import zipfile


parser = argparse.ArgumentParser(
    description="""
Prepares the environment for running system tests by downloading the release
artifacts from latest release on nimi-python.
""",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
args = parser.parse_args()


print('****Installing tox to Python.****')
results = subprocess.run(["python", '-m', 'pip', 'install', '--disable-pip-version-check', '--upgrade', 'pip', 'tox'], check=True)


print('****Parsing releases on nimi-python GitHub repo to obtain the latest zip file URL.****')
release_url = 'https://api.github.com/repos/ni/nimi-python/releases'
with urllib.request.urlopen(release_url) as response:
    html = response.read()
url_data = json.loads(html.decode('utf-8'))
zip_url = url_data[0]['zipball_url']
print(zip_url)


print('****Downloading latest zip file from GitHub.****')
try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve
working_directory = pathlib.Path.cwd()
zip_file = pathlib.Path(working_directory).joinpath('system_tests.zip')
urlretrieve(zip_url, zip_file)
print('Download complete.')


print('****Unzipping Zip file.****')
zip_folder = pathlib.Path(working_directory).joinpath('system_tests')
zip_ref = zipfile.ZipFile(zip_file, 'r')
zip_ref.extractall(zip_folder)
zip_ref.close()
print(zip_folder)
