echo %JENKINS_URL%
echo %ghprbSourceBranch%
echo %GIT_BRANCH%
echo %ghprbActualCommit%
echo %GIT_COMMIT%
echo %CHANGE_ID%
echo %BRANCH_NAME%
echo %BUILD_NUMBER%
echo %ghprbPullId%
echo %BUILD_URL%

pushd generated\niscope
c:\python38\python.exe -m tox -c tox-driver.ini
popd

pushd generated\nidmm
c:\python38\python.exe -m tox -c tox-driver.ini
popd

pushd generated\nimodinst
c:\python38\python.exe -m tox -c tox-driver.ini
popd


