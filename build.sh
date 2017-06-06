rm -Rf bin
mkdir bin
mkdir bin/nidmm

python3 src/codegen/generateTemplate.py \
    --template src/codegen/templates/library.py.mako \
    --driver NI-DMM \
    --dest-file bin/nidmm/library.py -v -v

python3 src/codegen/generateTemplate.py \
    --template src/codegen/templates/attributes.py.mako \
    --driver NI-DMM \
    --dest-file bin/nidmm/attributes.py -v -v

python3 src/codegen/generateTemplate.py \
    --template src/codegen/templates/enums.py.mako \
    --driver NI-DMM \
    --dest-file bin/nidmm/enums.py -v -v

python3 src/codegen/generateTemplate.py \
    --template src/codegen/templates/session.py.mako \
    --driver NI-DMM \
    --dest-file bin/nidmm/session.py -v -v

cp src/NI-DMM/nidmm/__init__.py     bin/nidmm/__init__.py
cp src/NI-DMM/nidmm/errors.py       bin/nidmm/errors.py

