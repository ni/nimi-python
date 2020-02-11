echo Testing %1
rem Make sure the junit folder exists, otherwise we can have a race condition creating it in parallel
mkdir generated\junit
pushd generated\%1
rem We don't need no spinner - mainly because we aren't running tox interactively
rem set TOX_PARALLEL_NO_SPINNER=1
rem Run up to 3 environments in parallel, but still send the output to stdout
c:\python38\python.exe -m tox -c tox-system_tests.ini --parallel 3
popd


