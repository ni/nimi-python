
rm bin/*

python3 codegen/generateTemplate.py --template codegen/templates/library.py.mako --metadata metadata/nidmm/nidmm_metadata.py --dest-file bin/nidmm.py -v -v
