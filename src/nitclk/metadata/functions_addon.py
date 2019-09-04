# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
}

functions_locking = {
}

# Attach the given parameter to the given enum from enums.py
functions_enums = {
}

# This is the additional metadata needed by the code generator in order create code that can properly handle buffer allocation.
functions_buffer_info = {
}

# These are functions we mark as "error_handling":True. The generator uses this information to
# change how error handling is done within those functions themselves - basically, if an error occurs,
# dont try to handle it, since the functions are only used within the context of error handling.
functions_is_error_handling = {
}

# There are some parameters that are needed in the C function call we use under the hood, but that we do not want in the Python API
functions_remove_from_python_api = {
}

# Default values for method parameters
functions_default_value = {
}

# Parameter that need to be array.array
functions_array = {
}

# We want to use a common name for self_cal across all drivers
functions_name = {
}

# Functions not in original metadata.
functions_additional_functions = {
}

# Converted parameters
functions_converters = {
}

# The extracted metadata is incorrect. Patch it here.
functions_bad_source_metadata = {
}

