# This is the list of commands that make invoked in order to build nimi-python. If you want to reproduce the build but don't have GNU Make setup in your system, you can invoke this script.
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/tests
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/enums.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/library.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/session.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/errors.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/ctypes_library.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/mock_helper.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/tests/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/__init__.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/session.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/enums.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/attributes.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/functions.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
cp /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/tests/test_session.py /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/tests/test_session.py
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/setup.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
rm -Rf /c/Users/Administrator/Desktop/Git/nimi-python/generated/nifake
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/generated/nifake
cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/* /c/Users/Administrator/Desktop/Git/nimi-python/generated/nifake
cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/setup.py /c/Users/Administrator/Desktop/Git/nimi-python/generated/nifake
cp /c/Users/Administrator/Desktop/Git/nimi-python/README.rst /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/README.rst
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake && python3 -m pytest -s > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/test_results.log
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake && python3 setup.py bdist_wheel --universal > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/wheel.log
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake && python3 setup.py sdist > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/sdist.log
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/tests
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/enums.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/library.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/session.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/errors.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/ctypes_library.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/mock_helper.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/tests/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/__init__.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/session.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/enums.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/attributes.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/functions.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
cp /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/tests/test_session.py /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/tests/test_session.py
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/setup.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
rm -Rf /c/Users/Administrator/Desktop/Git/nimi-python/generated/nidmm
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/generated/nidmm
cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/* /c/Users/Administrator/Desktop/Git/nimi-python/generated/nidmm
cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/setup.py /c/Users/Administrator/Desktop/Git/nimi-python/generated/nidmm
cp /c/Users/Administrator/Desktop/Git/nimi-python/README.rst /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/README.rst
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm && python3 -m pytest -s > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/test_results.log
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm && python3 setup.py bdist_wheel --universal > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/wheel.log
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm && python3 setup.py sdist > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/sdist.log
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/tests
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/library.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/errors.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/ctypes_library.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/mock_helper.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/tests/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/__init__.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/session.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/attributes.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/functions.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
cp /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/tests/test_modinst.py /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/tests/test_modinst.py
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/setup.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
rm -Rf /c/Users/Administrator/Desktop/Git/nimi-python/generated/nimodinst
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/generated/nimodinst
cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/* /c/Users/Administrator/Desktop/Git/nimi-python/generated/nimodinst
cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/setup.py /c/Users/Administrator/Desktop/Git/nimi-python/generated/nimodinst
cp /c/Users/Administrator/Desktop/Git/nimi-python/README.rst /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/README.rst
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst && python3 -m pytest -s > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/test_results.log
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst && python3 setup.py bdist_wheel --universal > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/wheel.log
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst && python3 setup.py sdist > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/sdist.log
