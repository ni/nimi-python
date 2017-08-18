# This is the list of commands that make invoked in order to build nimi-python. If you want to reproduce the build but don't have GNU Make setup in your system, you can invoke this script.
cp /Users/kirsch/Developer/nimi-python/src/nifake/tests/test_session.py /Users/kirsch/Developer/nimi-python/bin/nifake/nifake/tests/test_session.py
rm -Rf /Users/kirsch/Developer/nimi-python/generated/nifake
mkdir -p /Users/kirsch/Developer/nimi-python/generated/nifake
cp -Rf /Users/kirsch/Developer/nimi-python/bin/nifake/nifake/* /Users/kirsch/Developer/nimi-python/generated/nifake
cp -Rf /Users/kirsch/Developer/nimi-python/bin/nifake/setup.py /Users/kirsch/Developer/nimi-python/generated/nifake
cd /Users/kirsch/Developer/nimi-python/bin/nifake && python3 -m pytest -s > /Users/kirsch/Developer/nimi-python/bin/nifake/log/test_results.log
cd /Users/kirsch/Developer/nimi-python/bin/nifake && python3 setup.py bdist_wheel --universal > /Users/kirsch/Developer/nimi-python/bin/nifake/log/wheel.log
cd /Users/kirsch/Developer/nimi-python/bin/nifake && python3 setup.py sdist > /Users/kirsch/Developer/nimi-python/bin/nifake/log/sdist.log
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nidmm
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/tests
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nidmm/log
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/enums.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/library.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/session.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/errors.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/ctypes_library.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/mock_helper.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/tests/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/__init__.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/session.rst.mako --dest-dir  /Users/kirsch/Developer/nimi-python/docs/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/enums.rst.mako --dest-dir  /Users/kirsch/Developer/nimi-python/docs/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/attributes.rst.mako --dest-dir  /Users/kirsch/Developer/nimi-python/docs/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/functions.rst.mako --dest-dir  /Users/kirsch/Developer/nimi-python/docs/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
cp /Users/kirsch/Developer/nimi-python/src/nidmm/tests/test_session.py /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/tests/test_session.py
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/setup.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
rm -Rf /Users/kirsch/Developer/nimi-python/generated/nidmm
mkdir -p /Users/kirsch/Developer/nimi-python/generated/nidmm
cp -Rf /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/* /Users/kirsch/Developer/nimi-python/generated/nidmm
cp -Rf /Users/kirsch/Developer/nimi-python/bin/nidmm/setup.py /Users/kirsch/Developer/nimi-python/generated/nidmm
cp /Users/kirsch/Developer/nimi-python/README.rst /Users/kirsch/Developer/nimi-python/bin/nidmm/README.rst
cd /Users/kirsch/Developer/nimi-python/bin/nidmm && python3 -m pytest -s > /Users/kirsch/Developer/nimi-python/bin/nidmm/log/test_results.log
cd /Users/kirsch/Developer/nimi-python/bin/nidmm && python3 setup.py bdist_wheel --universal > /Users/kirsch/Developer/nimi-python/bin/nidmm/log/wheel.log
cd /Users/kirsch/Developer/nimi-python/bin/nidmm && python3 setup.py sdist > /Users/kirsch/Developer/nimi-python/bin/nidmm/log/sdist.log
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nimodinst
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nimodinst/nimodinst
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nimodinst/nimodinst/tests
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nimodinst/log
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/library.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nimodinst/nimodinst/ --metadata  /Users/kirsch/Developer/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/errors.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nimodinst/nimodinst/ --metadata  /Users/kirsch/Developer/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/ctypes_library.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nimodinst/nimodinst/ --metadata  /Users/kirsch/Developer/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/mock_helper.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nimodinst/nimodinst/tests/ --metadata  /Users/kirsch/Developer/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/__init__.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nimodinst/nimodinst/ --metadata  /Users/kirsch/Developer/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/session.rst.mako --dest-dir  /Users/kirsch/Developer/nimi-python/docs/nimodinst/ --metadata  /Users/kirsch/Developer/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/attributes.rst.mako --dest-dir  /Users/kirsch/Developer/nimi-python/docs/nimodinst/ --metadata  /Users/kirsch/Developer/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/functions.rst.mako --dest-dir  /Users/kirsch/Developer/nimi-python/docs/nimodinst/ --metadata  /Users/kirsch/Developer/nimi-python/src/nimodinst/metadata 
cp /Users/kirsch/Developer/nimi-python/src/nimodinst/tests/test_modinst.py /Users/kirsch/Developer/nimi-python/bin/nimodinst/nimodinst/tests/test_modinst.py
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/setup.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nimodinst/ --metadata  /Users/kirsch/Developer/nimi-python/src/nimodinst/metadata 
rm -Rf /Users/kirsch/Developer/nimi-python/generated/nimodinst
mkdir -p /Users/kirsch/Developer/nimi-python/generated/nimodinst
cp -Rf /Users/kirsch/Developer/nimi-python/bin/nimodinst/nimodinst/* /Users/kirsch/Developer/nimi-python/generated/nimodinst
cp -Rf /Users/kirsch/Developer/nimi-python/bin/nimodinst/setup.py /Users/kirsch/Developer/nimi-python/generated/nimodinst
cp /Users/kirsch/Developer/nimi-python/README.rst /Users/kirsch/Developer/nimi-python/bin/nimodinst/README.rst
cd /Users/kirsch/Developer/nimi-python/bin/nimodinst && python3 -m pytest -s > /Users/kirsch/Developer/nimi-python/bin/nimodinst/log/test_results.log
cd /Users/kirsch/Developer/nimi-python/bin/nimodinst && python3 setup.py bdist_wheel --universal > /Users/kirsch/Developer/nimi-python/bin/nimodinst/log/wheel.log
cd /Users/kirsch/Developer/nimi-python/bin/nimodinst && python3 setup.py sdist > /Users/kirsch/Developer/nimi-python/bin/nimodinst/log/sdist.log
