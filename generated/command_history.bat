rem This is the list of commands that make invoked in order to build nimi-python. If you want to reproduce the build but don't have GNU Make setup in your system, you can invoke this script.
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/tests
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/system_tests
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/examples
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
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/tests_passed
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/tests_passed
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake && python3 -m pytest -s > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/test_results.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/tests_passed
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/setup.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/generated_files_copied
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/generated_files_copied
rm -Rf /c/Users/Administrator/Desktop/Git/nimi-python/generated/nifake
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/generated/nifake
cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/* /c/Users/Administrator/Desktop/Git/nimi-python/generated/nifake
cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/setup.py /c/Users/Administrator/Desktop/Git/nimi-python/generated/nifake
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/generated_files_copied
cp /c/Users/Administrator/Desktop/Git/nimi-python/README.rst /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/README.rst
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/wheel_built
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/wheel_built
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake && python3 setup.py bdist_wheel --universal > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/wheel.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/wheel_built
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/sdist_built
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/sdist_built
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake && python3 setup.py sdist > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/sdist.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/sdist_built
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/tests
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/system_tests
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/examples
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
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/tests_passed
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/tests_passed
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm && python3 -m pytest -s > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/test_results.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/tests_passed
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/setup.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/generated_files_copied
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/generated_files_copied
rm -Rf /c/Users/Administrator/Desktop/Git/nimi-python/generated/nidmm
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/generated/nidmm
cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/* /c/Users/Administrator/Desktop/Git/nimi-python/generated/nidmm
cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/setup.py /c/Users/Administrator/Desktop/Git/nimi-python/generated/nidmm
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/generated_files_copied
cp /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/system_tests/test_system_nidmm.py /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/system_tests/test_system_nidmm.py
cp /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/examples/nidmm_measurement.py /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/examples/nidmm_measurement.py
cp /c/Users/Administrator/Desktop/Git/nimi-python/README.rst /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/README.rst
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/wheel_built
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/wheel_built
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm && python3 setup.py bdist_wheel --universal > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/wheel.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/wheel_built
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/sdist_built
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/sdist_built
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm && python3 setup.py sdist > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/sdist.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/sdist_built
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/niswitch
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/niswitch/tests
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/log
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/system_tests
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/examples
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/enums.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/niswitch/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/niswitch/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/library.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/niswitch/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/niswitch/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/session.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/niswitch/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/niswitch/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/errors.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/niswitch/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/niswitch/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/ctypes_library.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/niswitch/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/niswitch/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/mock_helper.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/niswitch/tests/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/niswitch/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/__init__.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/niswitch/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/niswitch/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/session.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/niswitch/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/niswitch/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/enums.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/niswitch/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/niswitch/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/attributes.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/niswitch/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/niswitch/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/functions.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/niswitch/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/niswitch/metadata 
cp /c/Users/Administrator/Desktop/Git/nimi-python/src/niswitch/tests/test_fake.py /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/niswitch/tests/test_fake.py
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/log/tests_passed
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/log/tests_passed
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch && python3 -m pytest -s > /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/log/test_results.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/log/tests_passed
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/setup.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/niswitch/metadata 
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/log/generated_files_copied
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/log/generated_files_copied
rm -Rf /c/Users/Administrator/Desktop/Git/nimi-python/generated/niswitch
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/generated/niswitch
cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/niswitch/* /c/Users/Administrator/Desktop/Git/nimi-python/generated/niswitch
cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/setup.py /c/Users/Administrator/Desktop/Git/nimi-python/generated/niswitch
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/log/generated_files_copied
cp /c/Users/Administrator/Desktop/Git/nimi-python/src/niswitch/system_tests/test_system_niswitch.py /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/system_tests/test_system_niswitch.py
cp /c/Users/Administrator/Desktop/Git/nimi-python/src/niswitch/examples/niswitch_connectchannels.py /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/examples/niswitch_connectchannels.py
cp /c/Users/Administrator/Desktop/Git/nimi-python/README.rst /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/README.rst
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/log/wheel_built
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/log/wheel_built
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch && python3 setup.py bdist_wheel --universal > /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/log/wheel.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/log/wheel_built
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/log/sdist_built
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/log/sdist_built
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch && python3 setup.py sdist > /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/log/sdist.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/niswitch/log/sdist_built
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/tests
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/system_tests
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/examples
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/library.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/errors.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/ctypes_library.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/mock_helper.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/tests/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/__init__.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/session.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/attributes.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/functions.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
cp /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/tests/test_modinst.py /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/tests/test_modinst.py
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/tests_passed
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/tests_passed
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst && python3 -m pytest -s > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/test_results.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/tests_passed
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/setup.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/generated_files_copied
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/generated_files_copied
rm -Rf /c/Users/Administrator/Desktop/Git/nimi-python/generated/nimodinst
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/generated/nimodinst
cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/* /c/Users/Administrator/Desktop/Git/nimi-python/generated/nimodinst
cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/setup.py /c/Users/Administrator/Desktop/Git/nimi-python/generated/nimodinst
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/generated_files_copied
cp /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/system_tests/test_system_nimodinst.py /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/system_tests/test_system_nimodinst.py
cp /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/examples/nimodinst_all_devices.py /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/examples/nimodinst_all_devices.py
cp /c/Users/Administrator/Desktop/Git/nimi-python/README.rst /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/README.rst
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/wheel_built
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/wheel_built
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst && python3 setup.py bdist_wheel --universal > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/wheel.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/wheel_built
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/sdist_built
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/sdist_built
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst && python3 setup.py sdist > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/sdist.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/sdist_built
