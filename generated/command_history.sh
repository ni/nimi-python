# This is the list of commands that make invoked in order to build nimi-python. If you want to reproduce the build but don't have GNU Make setup in your system, you can invoke this script.
rm -Rf /mnt/d/GitHub/nimi-python/generated/nidmm
mkdir -p /mnt/d/GitHub/nimi-python/generated/nidmm
cp -Rf /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/* /mnt/d/GitHub/nimi-python/generated/nidmm
cp -Rf /mnt/d/GitHub/nimi-python/bin/nidmm/setup.py /mnt/d/GitHub/nimi-python/generated/nidmm
cd /mnt/d/GitHub/nimi-python/bin/nidmm && python3 setup.py bdist_wheel --universal > /mnt/d/GitHub/nimi-python/bin/nidmm/log/wheel.log
cd /mnt/d/GitHub/nimi-python/bin/nidmm && python3 setup.py sdist > /mnt/d/GitHub/nimi-python/bin/nidmm/log/sdist.log
rm -Rf /mnt/d/GitHub/nimi-python/generated/nimodinst
mkdir -p /mnt/d/GitHub/nimi-python/generated/nimodinst
cp -Rf /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst/* /mnt/d/GitHub/nimi-python/generated/nimodinst
cp -Rf /mnt/d/GitHub/nimi-python/bin/nimodinst/setup.py /mnt/d/GitHub/nimi-python/generated/nimodinst
cd /mnt/d/GitHub/nimi-python/bin/nimodinst && python3 setup.py bdist_wheel --universal > /mnt/d/GitHub/nimi-python/bin/nimodinst/log/wheel.log
cd /mnt/d/GitHub/nimi-python/bin/nimodinst && python3 setup.py sdist > /mnt/d/GitHub/nimi-python/bin/nimodinst/log/sdist.log
