echo Testing %1
pushd generated\%1
rem We don't need no spinner - mainly because we aren't running tox interactively
set TOX_PARALLEL_NO_SPINNER=1
rem Run up to 3 environments in parallel, but still send the output to stdout
rem We only run the tests if the tox file exists
python.exe -m tox -c tox-system_tests.ini --parallel 1 --parallel-live
popd


