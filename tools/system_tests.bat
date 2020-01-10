pushd generated\niscope
c:\python38\python.exe -m tox -c tox-driver.ini
popd

pushd generated\nidmm
c:\python38\python.exe -m tox -c tox-driver.ini
popd

pushd generated\nimodinst
c:\python38\python.exe -m tox -c tox-driver.ini
popd


