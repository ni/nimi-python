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

functions_render_in_session_base = {
}

# The extracted metadata is incorrect. Patch it here.
# TODO(marcoskirsch): Tracked by NI internal bug 677141. Remove when that's fixed and new metadata is extracted.
functions_bad_source_metadata = {
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

# Set parameter name to Waveform instead of Wfm, even for private functions (for consistency)
functions_parameter_names = {
}

functions_method_templates = {
}

functions_numpy = {
}

# Parameter that need to be array.array
functions_array = {
}

# There are some parameters that are needed in the C function call we use under the hood, but that we do not want in the Python API
functions_remove_from_python_api = {
}


