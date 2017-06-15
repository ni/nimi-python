# Python 3 is required for build.py
rm -Rf bin
mkdir bin

# Create Create Python zipped application for ease of use
# Needs Python 3.5+ for zipapp
python -m zipapp -o bin/build.pyz build

# Needs Python 3.5+ for pkg_resources
python bin/build.pyz clean make make_installer -v --metadata src/nidmm/metadata



