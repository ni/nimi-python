# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning attributes that have been marked as obsolete prior to the initial
# Python API bindings release
attributes_codegen_method = {
}

attributes_converters = {
    1000007: { 'python_api_converter_name_to_driver': 'convert_timedelta_to_seconds', 
               'python_api_converter_name_from_driver': 'convert_seconds_to_timedelta', 
               'python_api_converter_type': 'datetime.timedelta', },
    1000008: { 'python_api_converter_name_to_driver': 'convert_timedelta_to_milliseconds', 
               'python_api_converter_name_from_driver': 'convert_milliseconds_to_timedelta', 
               'python_api_converter_type': 'datetime.timedelta', },
}

