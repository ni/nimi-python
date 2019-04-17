# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_codegen_method = {
}

functions_enums = {
}

# NI Switch Executive uses outputs as inputs for size in string functions. We had to change the size function to be a pointer.
# The easiest way to do this was to use an array of size 1. We use the value in that array to set the size of the string.
# See test_find_route_different_length for how to change the length.
functions_buffer_info = {
}

functions_is_error_handling = {
}

functions_default_value = {
}

functions_converters = {
}

# Switch executive is bad and uses an output as an input. Need to create pointer (array) to use API, but it needs to be input so it can be set by the user.
functions_bad_source_metadata = {
}
