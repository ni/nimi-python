# This is the list of commands that make invoked in order to build nimi-python. If you want to reproduce the build but don't have GNU Make setup in your system, you can invoke this script.
mkdir -p /mnt/d/GitHub/nimi-python/bin/nidmm
mkdir -p /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm
mkdir -p /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/tests
mkdir -p /mnt/d/GitHub/nimi-python/bin/nidmm/log
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/enums.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/library.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/session.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/errors.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/ctypes_library.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/mock_helper.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/tests/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/__init__.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/session.rst.mako --dest-dir  /mnt/d/GitHub/nimi-python/docs/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/enums.rst.mako --dest-dir  /mnt/d/GitHub/nimi-python/docs/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/attributes.rst.mako --dest-dir  /mnt/d/GitHub/nimi-python/docs/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
cp /mnt/d/GitHub/nimi-python/src/nidmm/tests/test_session.py /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/tests/test_session.py
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/setup.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nidmm/ --metadata  /mnt/d/GitHub/nimi-python/src/nidmm/metadata 
rm -Rf /mnt/d/GitHub/nimi-python/generated/nidmm
mkdir -p /mnt/d/GitHub/nimi-python/generated/nidmm
cp -Rf /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/* /mnt/d/GitHub/nimi-python/generated/nidmm
cp -Rf /mnt/d/GitHub/nimi-python/bin/nidmm/setup.py /mnt/d/GitHub/nimi-python/generated/nidmm
cp /mnt/d/GitHub/nimi-python/README.rst /mnt/d/GitHub/nimi-python/bin/nidmm/README.rst
cd /mnt/d/GitHub/nimi-python/bin/nidmm && python3 -m pytest -s > /mnt/d/GitHub/nimi-python/bin/nidmm/log/test_results.log
cd /mnt/d/GitHub/nimi-python/bin/nidmm && python3 setup.py bdist_wheel --universal > /mnt/d/GitHub/nimi-python/bin/nidmm/log/wheel.log
cd /mnt/d/GitHub/nimi-python/bin/nidmm && python3 setup.py sdist > /mnt/d/GitHub/nimi-python/bin/nidmm/log/sdist.log
mkdir -p /mnt/d/GitHub/nimi-python/bin/nimodinst
mkdir -p /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst
mkdir -p /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst/tests
mkdir -p /mnt/d/GitHub/nimi-python/bin/nimodinst/log
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/library.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst/ --metadata  /mnt/d/GitHub/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/errors.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst/ --metadata  /mnt/d/GitHub/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/ctypes_library.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst/ --metadata  /mnt/d/GitHub/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/mock_helper.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst/tests/ --metadata  /mnt/d/GitHub/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/__init__.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst/ --metadata  /mnt/d/GitHub/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/session.rst.mako --dest-dir  /mnt/d/GitHub/nimi-python/docs/nimodinst/ --metadata  /mnt/d/GitHub/nimi-python/src/nimodinst/metadata 
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/attributes.rst.mako --dest-dir  /mnt/d/GitHub/nimi-python/docs/nimodinst/ --metadata  /mnt/d/GitHub/nimi-python/src/nimodinst/metadata 
cp /mnt/d/GitHub/nimi-python/src/nimodinst/tests/test_modinst.py /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst/tests/test_modinst.py
python3 -m build --template  /mnt/d/GitHub/nimi-python/build/templates/setup.py.mako --dest-dir  /mnt/d/GitHub/nimi-python/bin/nimodinst/ --metadata  /mnt/d/GitHub/nimi-python/src/nimodinst/metadata 
rm -Rf /mnt/d/GitHub/nimi-python/generated/nimodinst
mkdir -p /mnt/d/GitHub/nimi-python/generated/nimodinst
cp -Rf /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst/* /mnt/d/GitHub/nimi-python/generated/nimodinst
cp -Rf /mnt/d/GitHub/nimi-python/bin/nimodinst/setup.py /mnt/d/GitHub/nimi-python/generated/nimodinst
cp /mnt/d/GitHub/nimi-python/README.rst /mnt/d/GitHub/nimi-python/bin/nimodinst/README.rst
cd /mnt/d/GitHub/nimi-python/bin/nimodinst && python3 -m pytest -s > /mnt/d/GitHub/nimi-python/bin/nimodinst/log/test_results.log
cd /mnt/d/GitHub/nimi-python/bin/nimodinst && python3 setup.py bdist_wheel --universal > /mnt/d/GitHub/nimi-python/bin/nimodinst/log/wheel.log
cd /mnt/d/GitHub/nimi-python/bin/nimodinst && python3 setup.py sdist > /mnt/d/GitHub/nimi-python/bin/nimodinst/log/sdist.log
python3 -msphinx -M html "/mnt/d/GitHub/nimi-python/docs" "/mnt/d/GitHub/nimi-python/bin/docs" 
cp /mnt/d/GitHub/nimi-python/tox.ini /mnt/d/GitHub/nimi-python/bin/nidmm/tox.ini
cd /mnt/d/GitHub/nimi-python/bin/nidmm && tox -e flake8
cp /mnt/d/GitHub/nimi-python/tox.ini /mnt/d/GitHub/nimi-python/bin/nimodinst/tox.ini
cd /mnt/d/GitHub/nimi-python/bin/nimodinst && tox -e flake8
