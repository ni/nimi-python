# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning attributes that have been marked as obsolete prior to the initial
# Python API bindings release
attributes_codegen_method = {
}

# If the associated enum represents boolean values only, disconnect
attributes_remove_enum = {
    1150020: { "enum": None,                        },  # POWER_LINE_FREQUENCY, Don't use enum since simple value will do
    1150016: { 'enum': None, 'python_type': 'bool', },  # CURRENT_LIMIT_AUTORANGE, Don't use the enum because a bool will do
    1150017: { 'enum': None, 'python_type': 'bool', },  # CURRENT_LEVEL_AUTORANGE, Don't use the enum because a bool will do
    1150015: { 'enum': None, 'python_type': 'bool', },  # VOLTAGE_LEVEL_AUTORANGE, Don't use the enum because a bool will do
    1150018: { 'enum': None, 'python_type': 'bool', },  # CURRENT_LIMIT_AUTORANGE, Don't use the enum because a bool will do
}
