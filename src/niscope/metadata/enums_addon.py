# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning enums that have been marked as obsolete prior to the initial
# Python API bindings release
# We also do not codegen enums associated with P2P or External Calibration since neither
# are supported in Python
enums_codegen_method = {
}

enums_additional_enums = {
}

# Override names that can't be directly converted from C names into valid Python names
enums_override_values = {
}

# We explicitly don't start with enums_ since we don't want this merged. These will replace the existing enums
# Once NI Internal CAR #675174 is fixed, this can be removed along with the overwrite code in __init__.py
# (TODO): Jaleel: Update dictionary_name after issue#624
replacement_enums = {
}
