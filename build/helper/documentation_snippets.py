# Different documentation snippets we add to the generated documentation

rep_cap_method_desc = '''
This method requires repeated capabilities ({1}). If called directly on the
{0}.Session object, then the method will use all repeated capabilities in the session.
You can specify a subset of repeated capabilities using the Python index notation on an
{0}.Session repeated capabilities container, and calling this method on the result.:
'''

rep_cap_attr_desc = '''
This property can use repeated capabilities ({1}). If set or get directly on the
{0}.Session object, then the set/get will use all repeated capabilities in the session.
You can specify a subset of repeated capabilities using the Python index notation on an
{0}.Session repeated capabilities container, and calling set/get value on the result.:
'''

rep_cap_attr_desc_rst_r = rep_cap_attr_desc + '''
.. code:: python

    var = session.{1}[0,1].{2}
'''

rep_cap_attr_desc_rst_w = rep_cap_attr_desc + '''
.. code:: python

    session.{1}[0,1].{2} = var
'''

rep_cap_attr_desc_rst_rw = rep_cap_attr_desc + '''
.. code:: python

    session.{1}[0,1].{2} = var
    var = session.{1}[0,1].{2}
'''

rep_cap_attr_desc_docstring_r = rep_cap_attr_desc + '''
    var = session.{1}[0,1].{2}
'''

rep_cap_attr_desc_docstring_w = rep_cap_attr_desc + '''
    session.{1}[0,1].{2} = var
'''

rep_cap_attr_desc_docstring_rw = rep_cap_attr_desc + '''
    session.{1}[0,1].{2} = var
    var = session.{1}[0,1].{2}
'''

rep_cap_method_desc_rst = rep_cap_method_desc + '''
.. code:: python

    session.{1}[0,1].{2}({3})
'''

rep_cap_method_desc_docstring = rep_cap_method_desc + '''
    session.{1}[0,1].{2}({3})
'''

func_note_text = '''
One or more of the referenced functions are not in the Python API for this driver.
'''

attr_note_text = '''
One or more of the referenced attributes are not in the Python API for this driver.
'''

enum_note_text = '''
One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
'''

session_return_text = '''
A session object representing the device.
'''

options_table_header = ['Attribute', 'Default']
options_table_body = [
    ['range_check', 'True'],
    ['query_instrument_status', 'False'],
    ['cache', 'True'],
    ['simulate', 'False'],
    ['record_value_coersions', 'False'],
    ['driver_setup', '{}'],
]

options_text = '''
Specifies the initial value of certain attributes for the session. The
syntax for **options** is a dictionary of attributes with an assigned
value. For example:

{ 'simulate': False }

You do not have to specify a value for all the attributes. If you do not
specify a value for an attribute, the default value is used.

Advanced Example:
{ 'simulate': True, 'driver_setup': { 'Model': '<model number>',  'BoardType': '<type>' } }
'''

default_close_function_doc = '''
Closes the driver session and cleans up.
'''

close_function_note = '''
This function is not needed when using the session context manager
'''

def close_function_def_for_doc(functions):
    # This is very specific to IVI. We look for a 'close' function and if we find it,
    # We will copy that and modify it to be what we need for documentation
    if 'close' in functions:
        import copy
        function_def = copy.deepcopy(functions['close'])
        if 'documentation' not in function_def:
            function_def['documentation'] = {}
        if 'description' not in function_def['documentation']:
            function_def['documentation']['description'] = default_close_function_doc
        if 'note' not in function_def['documentation']:
            function_def['documentation']['note'] = []
        if type(function_def['documentation']['note']) is not list:
            function_def['documentation']['note'] = [function_def['documentation']['note']]
        function_def['documentation']['note'].append(close_function_note)
        function_def['python_name'] = 'close'
    else:
        function_def = {
            'documentation': {
                'description': default_close_function_doc,
                'note': [close_function_note],
            },
            'method_templates': [{
                    'documentation_filename': '/default_method', 'method_python_name_suffix': '', 'session_filename': '/default_method',
            },],
            'name': 'close',
            'parameters': [],
            'has_repeated_capability': False,
            'python_name': 'close',
            'returns': 'ViStatus',
        }

    return function_def

