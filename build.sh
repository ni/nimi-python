
# Python 3 is required for build.py

rm -Rf bin
mkdir bin

# Create fake build.py that is an executable zip file and use that for subsequent steps
py -m zipapp -o bin/build.pyz build

py bin/build.pyz clean make local_install -v --metadata src/nidmm/metadata


