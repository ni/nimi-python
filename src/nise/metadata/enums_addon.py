# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here.
# We are not code genning enums that have been marked as obsolete prior to the initial
# Python API bindings release
# We also do not codegen enums associated with P2P or External Calibration since neither 
# are supported in Python
enums_codegen_method = {
}

# Need additional enums for functions that use enums. Enum names & values come from LabVIEW API
enums_additional_enums = {
}
