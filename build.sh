rm -Rf bin
mkdir bin
mkdir bin/nidmm

python3 src/codegen/generateTemplate.py \
    --template src/codegen/templates/library.py.mako \
    --driver NI-DMM \
    --dest-dir bin/nidmm -v -v

python3 src/codegen/generateTemplate.py \
    --template src/codegen/templates/attributes.py.mako \
    --driver NI-DMM \
    --dest-dir bin/nidmm -v -v

python3 src/codegen/generateTemplate.py \
    --template src/codegen/templates/enums.py.mako \
    --driver NI-DMM \
    --dest-dir bin/nidmm -v -v

python3 src/codegen/generateTemplate.py \
    --template src/codegen/templates/session.py.mako \
    --driver NI-DMM \
    --dest-dir bin/nidmm -v -v

cp src/nidmm/nidmm/__init__.py     bin/nidmm/__init__.py
cp src/nidmm/nidmm/errors.py       bin/nidmm/errors.py

