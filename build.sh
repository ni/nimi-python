
# Python 3 is required for build.py
rm -Rf bin
mkdir bin

# Create fake build.py that is an executable zip file and use that for subsequent steps
# Needs Python 3.5+ for zipapp
python -m zipapp -o bin/build.pyz build

# Needs Python 3.5+ for pkg_resources
python bin/build.pyz clean make local_install -v --metadata src/nidmm/metadata



