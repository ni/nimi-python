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

