rem This is the list of commands that make invoked in order to build nimi-python. If you want to reproduce the build but don't have GNU Make setup in your system, you can invoke this script.
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nifake
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nifake/nifake
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nifake/nifake/tests
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nifake/log
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nifake/system_tests
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nifake/examples
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/enums.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nifake/nifake/ --metadata  /Users/kirsch/Developer/nimi-python/src/nifake/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/library.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nifake/nifake/ --metadata  /Users/kirsch/Developer/nimi-python/src/nifake/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/session.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nifake/nifake/ --metadata  /Users/kirsch/Developer/nimi-python/src/nifake/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/errors.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nifake/nifake/ --metadata  /Users/kirsch/Developer/nimi-python/src/nifake/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/ctypes_library.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nifake/nifake/ --metadata  /Users/kirsch/Developer/nimi-python/src/nifake/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/mock_helper.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nifake/nifake/tests/ --metadata  /Users/kirsch/Developer/nimi-python/src/nifake/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/__init__.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nifake/nifake/ --metadata  /Users/kirsch/Developer/nimi-python/src/nifake/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/setup.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nifake/ --metadata  /Users/kirsch/Developer/nimi-python/src/nifake/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/session.rst.mako --dest-dir  /Users/kirsch/Developer/nimi-python/docs/nifake/ --metadata  /Users/kirsch/Developer/nimi-python/src/nifake/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/enums.rst.mako --dest-dir  /Users/kirsch/Developer/nimi-python/docs/nifake/ --metadata  /Users/kirsch/Developer/nimi-python/src/nifake/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/attributes.rst.mako --dest-dir  /Users/kirsch/Developer/nimi-python/docs/nifake/ --metadata  /Users/kirsch/Developer/nimi-python/src/nifake/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/functions.rst.mako --dest-dir  /Users/kirsch/Developer/nimi-python/docs/nifake/ --metadata  /Users/kirsch/Developer/nimi-python/src/nifake/metadata 
cp /Users/kirsch/Developer/nimi-python/src/nifake/tests/test_session.py /Users/kirsch/Developer/nimi-python/bin/nifake/nifake/tests/test_session.py
touch  /Users/kirsch/Developer/nimi-python/bin/nifake/log/generated_files_copy_done
rm  /Users/kirsch/Developer/nimi-python/bin/nifake/log/generated_files_copy_done
 rm -Rf /Users/kirsch/Developer/nimi-python/generated/nifake/* && cp -Rf /Users/kirsch/Developer/nimi-python/bin/nifake/nifake/* /Users/kirsch/Developer/nimi-python/generated/nifake && cp -Rf /Users/kirsch/Developer/nimi-python/bin/nifake/setup.py /Users/kirsch/Developer/nimi-python/generated/nifake 
touch  /Users/kirsch/Developer/nimi-python/bin/nifake/log/generated_files_copy_done
cp /Users/kirsch/Developer/nimi-python/README.rst /Users/kirsch/Developer/nimi-python/bin/nifake/README.rst
touch /Users/kirsch/Developer/nimi-python/bin/nifake/log/wheel_build_done
rm /Users/kirsch/Developer/nimi-python/bin/nifake/log/wheel_build_done
cd /Users/kirsch/Developer/nimi-python/bin/nifake && python3 setup.py bdist_wheel --universal > /Users/kirsch/Developer/nimi-python/bin/nifake/log/wheel.log
touch /Users/kirsch/Developer/nimi-python/bin/nifake/log/wheel_build_done
touch /Users/kirsch/Developer/nimi-python/bin/nifake/log/sdist_build_done
rm /Users/kirsch/Developer/nimi-python/bin/nifake/log/sdist_build_done
cd /Users/kirsch/Developer/nimi-python/bin/nifake && python3 setup.py sdist > /Users/kirsch/Developer/nimi-python/bin/nifake/log/sdist.log
touch /Users/kirsch/Developer/nimi-python/bin/nifake/log/sdist_build_done
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nidmm
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/tests
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nidmm/log
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nidmm/system_tests
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nidmm/examples
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/enums.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/library.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/session.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/errors.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/ctypes_library.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/mock_helper.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/tests/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/__init__.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/setup.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/session.rst.mako --dest-dir  /Users/kirsch/Developer/nimi-python/docs/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/enums.rst.mako --dest-dir  /Users/kirsch/Developer/nimi-python/docs/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/attributes.rst.mako --dest-dir  /Users/kirsch/Developer/nimi-python/docs/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/functions.rst.mako --dest-dir  /Users/kirsch/Developer/nimi-python/docs/nidmm/ --metadata  /Users/kirsch/Developer/nimi-python/src/nidmm/metadata 
cp /Users/kirsch/Developer/nimi-python/src/nidmm/tests/test_session.py /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/tests/test_session.py
touch  /Users/kirsch/Developer/nimi-python/bin/nidmm/log/generated_files_copy_done
rm  /Users/kirsch/Developer/nimi-python/bin/nidmm/log/generated_files_copy_done
 rm -Rf /Users/kirsch/Developer/nimi-python/generated/nidmm/* && cp -Rf /Users/kirsch/Developer/nimi-python/bin/nidmm/nidmm/* /Users/kirsch/Developer/nimi-python/generated/nidmm && cp -Rf /Users/kirsch/Developer/nimi-python/bin/nidmm/setup.py /Users/kirsch/Developer/nimi-python/generated/nidmm 
touch  /Users/kirsch/Developer/nimi-python/bin/nidmm/log/generated_files_copy_done
cp /Users/kirsch/Developer/nimi-python/src/nidmm/system_tests/test_system_nidmm.py /Users/kirsch/Developer/nimi-python/bin/nidmm/system_tests/test_system_nidmm.py
cp /Users/kirsch/Developer/nimi-python/src/nidmm/examples/nidmm_measurement.py /Users/kirsch/Developer/nimi-python/bin/nidmm/examples/nidmm_measurement.py
cp /Users/kirsch/Developer/nimi-python/README.rst /Users/kirsch/Developer/nimi-python/bin/nidmm/README.rst
touch /Users/kirsch/Developer/nimi-python/bin/nidmm/log/wheel_build_done
rm /Users/kirsch/Developer/nimi-python/bin/nidmm/log/wheel_build_done
cd /Users/kirsch/Developer/nimi-python/bin/nidmm && python3 setup.py bdist_wheel --universal > /Users/kirsch/Developer/nimi-python/bin/nidmm/log/wheel.log
touch /Users/kirsch/Developer/nimi-python/bin/nidmm/log/wheel_build_done
touch /Users/kirsch/Developer/nimi-python/bin/nidmm/log/sdist_build_done
rm /Users/kirsch/Developer/nimi-python/bin/nidmm/log/sdist_build_done
cd /Users/kirsch/Developer/nimi-python/bin/nidmm && python3 setup.py sdist > /Users/kirsch/Developer/nimi-python/bin/nidmm/log/sdist.log
touch /Users/kirsch/Developer/nimi-python/bin/nidmm/log/sdist_build_done
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nimodinst
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nimodinst/nimodinst
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nimodinst/nimodinst/tests
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nimodinst/log
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nimodinst/system_tests
mkdir -p /Users/kirsch/Developer/nimi-python/bin/nimodinst/examples
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/library.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nimodinst/nimodinst/ --metadata  /Users/kirsch/Developer/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/errors.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nimodinst/nimodinst/ --metadata  /Users/kirsch/Developer/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/ctypes_library.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nimodinst/nimodinst/ --metadata  /Users/kirsch/Developer/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/mock_helper.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nimodinst/nimodinst/tests/ --metadata  /Users/kirsch/Developer/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/__init__.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nimodinst/nimodinst/ --metadata  /Users/kirsch/Developer/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/setup.py.mako --dest-dir  /Users/kirsch/Developer/nimi-python/bin/nimodinst/ --metadata  /Users/kirsch/Developer/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/session.rst.mako --dest-dir  /Users/kirsch/Developer/nimi-python/docs/nimodinst/ --metadata  /Users/kirsch/Developer/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/attributes.rst.mako --dest-dir  /Users/kirsch/Developer/nimi-python/docs/nimodinst/ --metadata  /Users/kirsch/Developer/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /Users/kirsch/Developer/nimi-python/build/templates/functions.rst.mako --dest-dir  /Users/kirsch/Developer/nimi-python/docs/nimodinst/ --metadata  /Users/kirsch/Developer/nimi-python/src/nimodinst/metadata 
cp /Users/kirsch/Developer/nimi-python/src/nimodinst/tests/test_modinst.py /Users/kirsch/Developer/nimi-python/bin/nimodinst/nimodinst/tests/test_modinst.py
touch  /Users/kirsch/Developer/nimi-python/bin/nimodinst/log/generated_files_copy_done
rm  /Users/kirsch/Developer/nimi-python/bin/nimodinst/log/generated_files_copy_done
 rm -Rf /Users/kirsch/Developer/nimi-python/generated/nimodinst/* && cp -Rf /Users/kirsch/Developer/nimi-python/bin/nimodinst/nimodinst/* /Users/kirsch/Developer/nimi-python/generated/nimodinst && cp -Rf /Users/kirsch/Developer/nimi-python/bin/nimodinst/setup.py /Users/kirsch/Developer/nimi-python/generated/nimodinst 
touch  /Users/kirsch/Developer/nimi-python/bin/nimodinst/log/generated_files_copy_done
cp /Users/kirsch/Developer/nimi-python/src/nimodinst/system_tests/test_system_nimodinst.py /Users/kirsch/Developer/nimi-python/bin/nimodinst/system_tests/test_system_nimodinst.py
cp /Users/kirsch/Developer/nimi-python/src/nimodinst/examples/nimodinst_all_devices.py /Users/kirsch/Developer/nimi-python/bin/nimodinst/examples/nimodinst_all_devices.py
cp /Users/kirsch/Developer/nimi-python/README.rst /Users/kirsch/Developer/nimi-python/bin/nimodinst/README.rst
touch /Users/kirsch/Developer/nimi-python/bin/nimodinst/log/wheel_build_done
rm /Users/kirsch/Developer/nimi-python/bin/nimodinst/log/wheel_build_done
cd /Users/kirsch/Developer/nimi-python/bin/nimodinst && python3 setup.py bdist_wheel --universal > /Users/kirsch/Developer/nimi-python/bin/nimodinst/log/wheel.log
touch /Users/kirsch/Developer/nimi-python/bin/nimodinst/log/wheel_build_done
touch /Users/kirsch/Developer/nimi-python/bin/nimodinst/log/sdist_build_done
rm /Users/kirsch/Developer/nimi-python/bin/nimodinst/log/sdist_build_done
cd /Users/kirsch/Developer/nimi-python/bin/nimodinst && python3 setup.py sdist > /Users/kirsch/Developer/nimi-python/bin/nimodinst/log/sdist.log
touch /Users/kirsch/Developer/nimi-python/bin/nimodinst/log/sdist_build_done
