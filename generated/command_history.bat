rem This is the list of commands that make invoked in order to build nimi-python. If you want to reproduce the build but don't have GNU Make setup in your system, you can invoke this script.
rm -Rf /mnt/d/GitHub/nimi-python/generated/nifake
mkdir -p /mnt/d/GitHub/nimi-python/generated/nifake
cp -Rf /mnt/d/GitHub/nimi-python/bin/nifake/nifake/* /mnt/d/GitHub/nimi-python/generated/nifake
cp -Rf /mnt/d/GitHub/nimi-python/bin/nifake/setup.py /mnt/d/GitHub/nimi-python/generated/nifake
cd /mnt/d/GitHub/nimi-python/bin/nifake && python3 setup.py bdist_wheel --universal > /mnt/d/GitHub/nimi-python/bin/nifake/log/wheel.log
cd /mnt/d/GitHub/nimi-python/bin/nifake && python3 setup.py sdist > /mnt/d/GitHub/nimi-python/bin/nifake/log/sdist.log
rm -Rf /mnt/d/GitHub/nimi-python/generated/nidmm
mkdir -p /mnt/d/GitHub/nimi-python/generated/nidmm
cp -Rf /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/* /mnt/d/GitHub/nimi-python/generated/nidmm
cp -Rf /mnt/d/GitHub/nimi-python/bin/nidmm/setup.py /mnt/d/GitHub/nimi-python/generated/nidmm
cp /mnt/d/GitHub/nimi-python/src/nidmm/system_tests/test_system_nidmm.py /mnt/d/GitHub/nimi-python/bin/nidmm/system_tests/test_system_nidmm.py
cd /mnt/d/GitHub/nimi-python/bin/nidmm && python3 setup.py bdist_wheel --universal > /mnt/d/GitHub/nimi-python/bin/nidmm/log/wheel.log
cd /mnt/d/GitHub/nimi-python/bin/nidmm && python3 setup.py sdist > /mnt/d/GitHub/nimi-python/bin/nidmm/log/sdist.log
rm -Rf /mnt/d/GitHub/nimi-python/generated/nimodinst
mkdir -p /mnt/d/GitHub/nimi-python/generated/nimodinst
cp -Rf /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst/* /mnt/d/GitHub/nimi-python/generated/nimodinst
cp -Rf /mnt/d/GitHub/nimi-python/bin/nimodinst/setup.py /mnt/d/GitHub/nimi-python/generated/nimodinst
cd /mnt/d/GitHub/nimi-python/bin/nimodinst && python3 setup.py bdist_wheel --universal > /mnt/d/GitHub/nimi-python/bin/nimodinst/log/wheel.log
cd /mnt/d/GitHub/nimi-python/bin/nimodinst && python3 setup.py sdist > /mnt/d/GitHub/nimi-python/bin/nimodinst/log/sdist.log
python3 -msphinx -M html "/mnt/d/GitHub/nimi-python/docs" "/mnt/d/GitHub/nimi-python/bin/docs" 
cd /mnt/d/GitHub/nimi-python/bin/nifake && tox -e flake8
cd /mnt/d/GitHub/nimi-python/bin/nidmm && tox -e flake8
cp /mnt/d/GitHub/nimi-python/tox.ini /mnt/d/GitHub/nimi-python/bin/nimodinst/tox.ini
cd /mnt/d/GitHub/nimi-python/bin/nimodinst && tox -e flake8
