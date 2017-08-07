rem This is the list of commands that make invoked in order to build nimi-python. If you want to reproduce the build but don't have GNU Make setup in your system, you can invoke this script.
rm -Rf /mnt/d/GitHub/nimi-python/generated/nidmm
mkdir -p /mnt/d/GitHub/nimi-python/generated/nidmm
cp -Rf /mnt/d/GitHub/nimi-python/bin/nidmm/nidmm/* /mnt/d/GitHub/nimi-python/generated/nidmm
cp -Rf /mnt/d/GitHub/nimi-python/bin/nidmm/setup.py /mnt/d/GitHub/nimi-python/generated/nidmm
rm -Rf /mnt/d/GitHub/nimi-python/generated/nimodinst
mkdir -p /mnt/d/GitHub/nimi-python/generated/nimodinst
cp -Rf /mnt/d/GitHub/nimi-python/bin/nimodinst/nimodinst/* /mnt/d/GitHub/nimi-python/generated/nimodinst
cp -Rf /mnt/d/GitHub/nimi-python/bin/nimodinst/setup.py /mnt/d/GitHub/nimi-python/generated/nimodinst
python3 -msphinx -M html "/mnt/d/GitHub/nimi-python/docs" "/mnt/d/GitHub/nimi-python/bin/docs" 
cd /mnt/d/GitHub/nimi-python/bin/nidmm && tox -e flake8
cd /mnt/d/GitHub/nimi-python/bin/nimodinst && tox -e flake8
