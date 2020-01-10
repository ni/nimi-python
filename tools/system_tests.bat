@echo off

echo Testing nidcpower
pushd generated\nidcpower
c:\python38\python.exe -m tox -c tox-driver.ini
popd

echo Testing nidigital
pushd generated\nidigital
c:\python38\python.exe -m tox -c tox-driver.ini
popd

echo Testing niscope
pushd generated\niscope
c:\python38\python.exe -m tox -c tox-driver.ini
popd

echo Testing nidmm
pushd generated\nidmm
c:\python38\python.exe -m tox -c tox-driver.ini
popd

echo Testing nifgen
pushd generated\nifgen
c:\python38\python.exe -m tox -c tox-driver.ini
popd

echo Testing niscope
pushd generated\niscope
c:\python38\python.exe -m tox -c tox-driver.ini
popd

echo Testing niswitch
pushd generated\niswitch
c:\python38\python.exe -m tox -c tox-driver.ini
popd

echo Testing nise
pushd generated\nise
c:\python38\python.exe -m tox -c tox-driver.ini
popd

echo Testing nimodinst
pushd generated\nimodinst
c:\python38\python.exe -m tox -c tox-driver.ini
popd


