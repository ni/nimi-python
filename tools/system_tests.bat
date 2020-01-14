rem @echo off

echo Testing %1
pushd generated\%1
c:\python38\python.exe -m tox -c tox-driver.ini
popd


