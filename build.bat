rem Python 3 is required for build.py
rmdir /S /q bin
mkdir bin

rem Create Python zipped application for ease of use
rem Needs Python 3.5+ for zipapp
python -m zipapp -o bin/build.pyz build

rem Needs Python 3.5+ for pkg_resources
python bin/build.pyz clean make make_installer -v --metadata src/nidmm/metadata



