@echo off

echo The current working directory
pwd

echo Testing %1
pushd generated\%1
c:\python38\python.exe -m tox -c tox-driver.ini
popd


