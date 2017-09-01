rem This is the list of commands that make invoked in order to build nimi-python. If you want to reproduce the build but don't have GNU Make setup in your system, you can invoke this script.
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/tests
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/system_tests
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/examples
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/enums.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/library.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/library_singleton.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/session.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/errors.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/mock_helper.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/tests/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/__init__.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/setup.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
cp /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/tests/test_session.py /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/tests/test_session.py
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/session.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/enums.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/attributes.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/functions.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
touch  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/generated_files_copy_done
rm  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/generated_files_copy_done
 rm -Rf /c/Users/Administrator/Desktop/Git/nimi-python/generated/nifake/* && cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/* /c/Users/Administrator/Desktop/Git/nimi-python/generated/nifake && cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/setup.py /c/Users/Administrator/Desktop/Git/nimi-python/generated/nifake 
touch  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/generated_files_copy_done
cp /c/Users/Administrator/Desktop/Git/nimi-python/README.rst /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/README.rst
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/wheel_build_done
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/wheel_build_done
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake && python3 setup.py bdist_wheel --universal > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/wheel.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/wheel_build_done
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/sdist_build_done
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/sdist_build_done
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake && python3 setup.py sdist > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/sdist.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/sdist_build_done
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/tests
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/system_tests
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/examples
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/enums.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/library.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/library_singleton.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/session.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/errors.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/mock_helper.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/tests/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/__init__.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/setup.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/session.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/enums.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/attributes.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/functions.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nidmm/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/metadata 
touch  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/generated_files_copy_done
rm  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/generated_files_copy_done
 rm -Rf /c/Users/Administrator/Desktop/Git/nimi-python/generated/nidmm/* && cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/nidmm/* /c/Users/Administrator/Desktop/Git/nimi-python/generated/nidmm && cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/setup.py /c/Users/Administrator/Desktop/Git/nimi-python/generated/nidmm 
touch  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/generated_files_copy_done
cp /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/system_tests/test_system_nidmm.py /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/system_tests/test_system_nidmm.py
cp /c/Users/Administrator/Desktop/Git/nimi-python/src/nidmm/examples/nidmm_measurement.py /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/examples/nidmm_measurement.py
cp /c/Users/Administrator/Desktop/Git/nimi-python/README.rst /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/README.rst
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/wheel_build_done
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/wheel_build_done
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm && python3 setup.py bdist_wheel --universal > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/wheel.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/wheel_build_done
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/sdist_build_done
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/sdist_build_done
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm && python3 setup.py sdist > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/sdist.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nidmm/log/sdist_build_done
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/tests
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/system_tests
mkdir -p /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/examples
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/library.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/library_singleton.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/errors.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/mock_helper.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/tests/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/__init__.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/setup.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
cp /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/tests/test_modinst.py /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/tests/test_modinst.py
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/session.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/attributes.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/functions.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nimodinst/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/metadata 
touch  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/generated_files_copy_done
rm  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/generated_files_copy_done
 rm -Rf /c/Users/Administrator/Desktop/Git/nimi-python/generated/nimodinst/* && cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/nimodinst/* /c/Users/Administrator/Desktop/Git/nimi-python/generated/nimodinst && cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/setup.py /c/Users/Administrator/Desktop/Git/nimi-python/generated/nimodinst 
touch  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/generated_files_copy_done
cp /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/system_tests/test_system_nimodinst.py /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/system_tests/test_system_nimodinst.py
cp /c/Users/Administrator/Desktop/Git/nimi-python/src/nimodinst/examples/nimodinst_all_devices.py /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/examples/nimodinst_all_devices.py
cp /c/Users/Administrator/Desktop/Git/nimi-python/README.rst /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/README.rst
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/wheel_build_done
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/wheel_build_done
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst && python3 setup.py bdist_wheel --universal > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/wheel.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/wheel_build_done
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/sdist_build_done
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/sdist_build_done
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst && python3 setup.py sdist > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/sdist.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nimodinst/log/sdist_build_done
