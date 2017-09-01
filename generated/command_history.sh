# This is the list of commands that make invoked in order to build nimi-python. If you want to reproduce the build but don't have GNU Make setup in your system, you can invoke this script.
mkdir -p /mnt/d/GitHub/nimi-python/bin/nifake
mkdir -p /mnt/d/GitHub/nimi-python/bin/nifake/nifake
mkdir -p /mnt/d/GitHub/nimi-python/bin/nifake/nifake/tests
mkdir -p /mnt/d/GitHub/nimi-python/bin/nifake/log
mkdir -p /mnt/d/GitHub/nimi-python/bin/nifake/system_tests
mkdir -p /mnt/d/GitHub/nimi-python/bin/nifake/examples
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/enums.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nifake/nifake/ --metadata  /mnt/d/GitHub/nimi-python/src/nifake/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/library.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nifake/nifake/ --metadata  /mnt/d/GitHub/nimi-python/src/nifake/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/library_singleton.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nifake/nifake/ --metadata  /mnt/d/GitHub/nimi-python/src/nifake/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/session.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nifake/nifake/ --metadata  /mnt/d/GitHub/nimi-python/src/nifake/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/errors.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nifake/nifake/ --metadata  /mnt/d/GitHub/nimi-python/src/nifake/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/mock_helper.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nifake/nifake/tests/ --metadata  /mnt/d/GitHub/nimi-python/src/nifake/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/__init__.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nifake/nifake/ --metadata  /mnt/d/GitHub/nimi-python/src/nifake/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/setup.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nifake/ --metadata  /mnt/d/GitHub/nimi-python/src/nifake/metadata 
cp /mnt/d/GitHub/nimi-python/src/nifake/tests/test_session.py /mnt/d/GitHub/nimi-python/bin/nifake/nifake/tests/test_session.py
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/session.rst.mako --dest-dir  /mnt/d/GitHub/nimi-python/docs/nifake/ --metadata  /mnt/d/GitHub/nimi-python/src/nifake/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/enums.rst.mako --dest-dir  /mnt/d/GitHub/nimi-python/docs/nifake/ --metadata  /mnt/d/GitHub/nimi-python/src/nifake/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/attributes.rst.mako --dest-dir  /mnt/d/GitHub/nimi-python/docs/nifake/ --metadata  /mnt/d/GitHub/nimi-python/src/nifake/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/functions.rst.mako --dest-dir  /mnt/d/GitHub/nimi-python/docs/nifake/ --metadata  /mnt/d/GitHub/nimi-python/src/nifake/metadata 
touch  /mnt/d/GitHub/nimi-python/bin/nifake/log/generated_files_copy_done
rm  /mnt/d/GitHub/nimi-python/bin/nifake/log/generated_files_copy_done
 rm -Rf /mnt/d/GitHub/nimi-python/generated/nifake/* && cp -Rf /mnt/d/GitHub/nimi-python/bin/nifake/nifake/* /mnt/d/GitHub/nimi-python/generated/nifake && cp -Rf /mnt/d/GitHub/nimi-python/bin/nifake/setup.py /mnt/d/GitHub/nimi-python/generated/nifake 
touch  /mnt/d/GitHub/nimi-python/bin/nifake/log/generated_files_copy_done
cp /mnt/d/GitHub/nimi-python/README.rst /mnt/d/GitHub/nimi-python/bin/nifake/README.rst
touch /mnt/d/GitHub/nimi-python/bin/nifake/log/wheel_build_done
rm /mnt/d/GitHub/nimi-python/bin/nifake/log/wheel_build_done
cd /mnt/d/GitHub/nimi-python/bin/nifake && python3 setup.py bdist_wheel --universal > /mnt/d/GitHub/nimi-python/bin/nifake/log/wheel.log
touch /mnt/d/GitHub/nimi-python/bin/nifake/log/wheel_build_done
touch /mnt/d/GitHub/nimi-python/bin/nifake/log/sdist_build_done
rm /mnt/d/GitHub/nimi-python/bin/nifake/log/sdist_build_done
cd /mnt/d/GitHub/nimi-python/bin/nifake && python3 setup.py sdist > /mnt/d/GitHub/nimi-python/bin/nifake/log/sdist.log
touch /mnt/d/GitHub/nimi-python/bin/nifake/log/sdist_build_done
mkdir -p /mnt/d/GitHub/nimi-python/bin/nidmm
mkdir -p /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm
mkdir -p /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/tests
mkdir -p /mnt/d/GitHub/nimi-python/bin/nidmm/log
mkdir -p /mnt/d/GitHub/nimi-python/bin/nidmm/system_tests
mkdir -p /mnt/d/GitHub/nimi-python/bin/nidmm/examples
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/enums.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/library.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/library_singleton.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/session.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/errors.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/mock_helper.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/tests/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/__init__.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/setup.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
cp /mnt/d/GitHub/nimi-python/src/nidmm/tests/test_session.py /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/tests/test_session.py
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/session.rst.mako --dest-dir  /mnt/d/GitHub/nimi-python/docs/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/enums.rst.mako --dest-dir  /mnt/d/GitHub/nimi-python/docs/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/attributes.rst.mako --dest-dir  /mnt/d/GitHub/nimi-python/docs/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/functions.rst.mako --dest-dir  /mnt/d/GitHub/nimi-python/docs/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
touch  /mnt/d/GitHub/nimi-python/bin/nidmm/log/generated_files_copy_done
rm  /mnt/d/GitHub/nimi-python/bin/nidmm/log/generated_files_copy_done
 rm -Rf /mnt/d/GitHub/nimi-python/generated/nidmm/* && cp -Rf /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/* /mnt/d/GitHub/nimi-python/generated/nidmm && cp -Rf /mnt/d/GitHub/nimi-python/bin/nidmm/setup.py /mnt/d/GitHub/nimi-python/generated/nidmm 
touch  /mnt/d/GitHub/nimi-python/bin/nidmm/log/generated_files_copy_done
cp /mnt/d/GitHub/nimi-python/src/nidmm/system_tests/test_system_nidmm.py /mnt/d/GitHub/nimi-python/bin/nidmm/system_tests/test_system_nidmm.py
cp /mnt/d/GitHub/nimi-python/src/nidmm/examples/nidmm_measurement.py /mnt/d/GitHub/nimi-python/bin/nidmm/examples/nidmm_measurement.py
cp /mnt/d/GitHub/nimi-python/README.rst /mnt/d/GitHub/nimi-python/bin/nidmm/README.rst
touch /mnt/d/GitHub/nimi-python/bin/nidmm/log/wheel_build_done
rm /mnt/d/GitHub/nimi-python/bin/nidmm/log/wheel_build_done
cd /mnt/d/GitHub/nimi-python/bin/nidmm && python3 setup.py bdist_wheel --universal > /mnt/d/GitHub/nimi-python/bin/nidmm/log/wheel.log
touch /mnt/d/GitHub/nimi-python/bin/nidmm/log/wheel_build_done
touch /mnt/d/GitHub/nimi-python/bin/nidmm/log/sdist_build_done
rm /mnt/d/GitHub/nimi-python/bin/nidmm/log/sdist_build_done
cd /mnt/d/GitHub/nimi-python/bin/nidmm && python3 setup.py sdist > /mnt/d/GitHub/nimi-python/bin/nidmm/log/sdist.log
touch /mnt/d/GitHub/nimi-python/bin/nidmm/log/sdist_build_done
mkdir -p /mnt/d/GitHub/nimi-python/bin/nimodinst
mkdir -p /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst
mkdir -p /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst/tests
mkdir -p /mnt/d/GitHub/nimi-python/bin/nimodinst/log
mkdir -p /mnt/d/GitHub/nimi-python/bin/nimodinst/system_tests
mkdir -p /mnt/d/GitHub/nimi-python/bin/nimodinst/examples
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/library.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst/ --metadata  /mnt/d/GitHub/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/library_singleton.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst/ --metadata  /mnt/d/GitHub/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/errors.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst/ --metadata  /mnt/d/GitHub/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/mock_helper.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst/tests/ --metadata  /mnt/d/GitHub/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/__init__.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst/ --metadata  /mnt/d/GitHub/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/setup.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nimodinst/ --metadata  /mnt/d/GitHub/nimi-python/src/nimodinst/metadata 
cp /mnt/d/GitHub/nimi-python/src/nimodinst/tests/test_modinst.py /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst/tests/test_modinst.py
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/session.rst.mako --dest-dir  /mnt/d/GitHub/nimi-python/docs/nimodinst/ --metadata  /mnt/d/GitHub/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/attributes.rst.mako --dest-dir  /mnt/d/GitHub/nimi-python/docs/nimodinst/ --metadata  /mnt/d/GitHub/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/functions.rst.mako --dest-dir  /mnt/d/GitHub/nimi-python/docs/nimodinst/ --metadata  /mnt/d/GitHub/nimi-python/src/nimodinst/metadata 
touch  /mnt/d/GitHub/nimi-python/bin/nimodinst/log/generated_files_copy_done
rm  /mnt/d/GitHub/nimi-python/bin/nimodinst/log/generated_files_copy_done
 rm -Rf /mnt/d/GitHub/nimi-python/generated/nimodinst/* && cp -Rf /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst/* /mnt/d/GitHub/nimi-python/generated/nimodinst && cp -Rf /mnt/d/GitHub/nimi-python/bin/nimodinst/setup.py /mnt/d/GitHub/nimi-python/generated/nimodinst 
touch  /mnt/d/GitHub/nimi-python/bin/nimodinst/log/generated_files_copy_done
cp /mnt/d/GitHub/nimi-python/src/nimodinst/system_tests/test_system_nimodinst.py /mnt/d/GitHub/nimi-python/bin/nimodinst/system_tests/test_system_nimodinst.py
cp /mnt/d/GitHub/nimi-python/src/nimodinst/examples/nimodinst_all_devices.py /mnt/d/GitHub/nimi-python/bin/nimodinst/examples/nimodinst_all_devices.py
cp /mnt/d/GitHub/nimi-python/README.rst /mnt/d/GitHub/nimi-python/bin/nimodinst/README.rst
touch /mnt/d/GitHub/nimi-python/bin/nimodinst/log/wheel_build_done
rm /mnt/d/GitHub/nimi-python/bin/nimodinst/log/wheel_build_done
cd /mnt/d/GitHub/nimi-python/bin/nimodinst && python3 setup.py bdist_wheel --universal > /mnt/d/GitHub/nimi-python/bin/nimodinst/log/wheel.log
touch /mnt/d/GitHub/nimi-python/bin/nimodinst/log/wheel_build_done
touch /mnt/d/GitHub/nimi-python/bin/nimodinst/log/sdist_build_done
rm /mnt/d/GitHub/nimi-python/bin/nimodinst/log/sdist_build_done
cd /mnt/d/GitHub/nimi-python/bin/nimodinst && python3 setup.py sdist > /mnt/d/GitHub/nimi-python/bin/nimodinst/log/sdist.log
touch /mnt/d/GitHub/nimi-python/bin/nimodinst/log/sdist_build_done
