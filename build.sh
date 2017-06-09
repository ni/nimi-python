# Python 3 is required for build.py
python3 build.py -v -v

cp src/nidmm/nidmm/__init__.py     bin/nidmm/__init__.py
cp src/nidmm/nidmm/errors.py       bin/nidmm/errors.py

