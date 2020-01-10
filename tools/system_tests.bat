rem First we need a local nitclk wheel so let's build that
pushd generated\nitclk
c:\python38\python.exe setup.py bdist_wheel --universal 
popd

rem Now we run the tests
pushd generated\niscope
c:\python38\python.exe -m tox
popd

pushd generated\nidmm
c:\python38\python.exe -m tox
popd

pushd generated\nimodinst
c:\python38\python.exe -m tox
popd


