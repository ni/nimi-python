# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
    # Codegen deduces the enum types to generate based on usage of enum types in public metadata.
    # DigitalState is not specified in metadata of any public methods or properties but it is a
    # member of class returned by fancy HRAM fetch method. So we need to explicitly mark it public.
    'DigitalState': {
        'codegen_method': 'public',
    },
}
