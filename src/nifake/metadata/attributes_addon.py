# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning attributes that have been marked as obsolete prior to the initial
# Python API bindings release
attributes_codegen_method = {
}

attributes_converters = {
    1000007: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds', 
               'python_api_converter_type': 'datetime.timedelta', },
    1000008: { 'attribute_class': 'AttributeViInt32TimeDeltaMilliseconds', 
               'python_api_converter_type': 'datetime.timedelta', },
}

