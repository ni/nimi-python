rem @echo off

echo Testing %1
pushd generated\%1
dir
c:\python38\python.exe -m tox -c tox-driver.ini
popd


