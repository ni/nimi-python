echo Testing %1
rem Make sure the junit folder exists, otherwise we can have a race collision creating it in parallel
mkdir generated\junit
pushd generated\%1
set TOX_PARALLEL_NO_SPINNER=1
c:\python38\python.exe -m tox -c tox-system_tests.ini --parallel auto --parallel-live 
popd


