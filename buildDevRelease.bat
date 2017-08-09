bash -c "make clean all html flake8 test"

bash -c "twine upload bin/nidmm/dist/* bin/nimodinst/dist/*"

bash -c "python tools/updateDevVersions.py --src-file src/nidmm/metadata/config.py"
bash -c "python tools/updateDevVersions.py --src-file src/nimodinst/metadata/config.py"

