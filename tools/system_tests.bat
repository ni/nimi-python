echo Testing %1
pushd generated\%1
set TOX_PARALLEL_NO_SPINNER=1
c:\python38\python.exe -m tox -c tox-system_tests.ini --parallel auto
popd


