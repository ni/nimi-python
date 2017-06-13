
# Python 3 is required for build.py

rm -Rf bin
mkdir bin

# Create fake build.py that is an executable zip file and use that for subsequent steps
# Needs Python 3.5+ for zipapp
# TODO(texasaggie97) change to python when able
py -m zipapp -o bin/build.pyz build

# Needs Python 3.5+ for pkg_resources
# TODO(texasaggie97) change to python when able
py bin/build.pyz clean make local_install -v --metadata src/nidmm/metadata


