rm -Rf bin
mkdir bin
mkdir bin/nidmm

python3 src/codegen/generateTemplate.py \
    --template src/codegen/templates/library.py.mako \
    --metadata src/NI-DMM/metadata/nidmm_metadata.py \
    --dest-file bin/nidmm/library.py -v -v

python3 src/codegen/generateTemplate.py \
    --template src/codegen/templates/attributes.py.mako \
    --metadata src/NI-DMM/metadata/nidmm_metadata.py \
    --dest-file bin/nidmm/attributes.py -v -v

cp src/NI-DMM/nidmm/__init__.py     bin/nidmm/__init__.py
cp src/NI-DMM/nidmm/enums.py        bin/nidmm/enums.py
cp src/NI-DMM/nidmm/errors.py       bin/nidmm/errors.py
cp src/NI-DMM/nidmm/session.py      bin/nidmm/session.py

