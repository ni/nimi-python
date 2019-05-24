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

functions_send_software_edge_trigger = {
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

# Functions not in original metadata.
functions_additional_functions = {
}


# Override the 'python' name for some functions.
functions_python_name = {
}

functions_method_templates = {
}

# We keep this information because we will need it again if we ever enable OSP and need this function
# 'GetFIRFilterCoefficients':     { 'method_templates': [
#     { 'session_filename': 'get_fir_filter_coefficients', 'documentation_filename': 'get_fir_filter_coefficients', 'method_python_name_suffix': '', },
# ], },

functions_numpy = {
}

# Parameter that need to be array.array
functions_array = {
}


