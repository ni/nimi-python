# Python 3 is required for build.py
rm -Rf bin
mkdir bin

# Create Python zipped application for ease of use
# Needs Python 3.5+ for zipapp
python3 -m zipapp -o bin/build.pyz build

# Needs Python 3.5+ for pkg_resources
python3 bin/build.pyz clean make make_installer -v --metadata src/nidmm/metadata
python3 bin/build.pyz clean make make_installer -v --metadata src/nimodinst/metadata

