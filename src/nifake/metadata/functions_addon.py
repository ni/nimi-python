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

# Default values for method parameters
functions_default_value = {
}

# Converted parameters
functions_converters = {
}

# Manually provided Python names for methods, rather than deriving from original names.
functions_custom_python_name = {
}

# There are some parameters that are needed in the C function call we use under the hood, but that we do not want in the Python API
functions_remove_from_python_api = {
}

functions_method_templates = {
}

functions_numpy = {
}

# Parameter that need to be array.array
functions_array = {
}

# Functions not in original metadata.
functions_additional_functions = {
}


