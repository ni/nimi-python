
from .codegen_helper import filter_parameters
from .codegen_helper import get_params_snippet
from .parameter_usage_options import ParameterUsageOptions

import re
import string
import sys


# Python 2/3 compatibility
def _normalize_string_type(d):
    '''Normalize string type between python2 & python3'''
    if sys.version_info.major < 3:
        if type(d) is dict:
            for k in d:
                d[k] = _normalize_string_type(d[k])
        elif type(d) is str:
            d = d.decode('utf-8')
    return d


def get_indented_docstring_snippet(d, indent=4):
    '''Returns a docstring with the correct amount of indentation.

    First line is not indented.

    Can't use similar construct as get_dictionary_snippet
    ('\n' + (' ' * indent)).join(d_lines) because empty lines would get
    the spaces, which violates pep8 and causes the flake8 step to fail

    Args:
        docstring (str): multiline string to format
        indent (int): How much to indent lines 2+

    Returns:
        str: formatted string
    '''
    d_lines = d.strip().splitlines()
    ret_val = ''
    for l in d_lines:
        if len(ret_val) > 0:
            ret_val += '\n'
            if len(l.rstrip()) > 0:
                ret_val += (' ' * indent)
        ret_val += _normalize_string_type(l.rstrip())
    return ret_val


def get_rst_header_snippet(t, header_level='='):
    '''Get rst formatted heading'''
    ret_val = t + '\n'
    ret_val += header_level * len(t)
    return ret_val


def _get_rst_table_snippet(d, config, indent=0, make_link=True):
    '''Returns an rst table snippet if table_header and/or table_body are in the dictionary'''
    if 'table_body' in d:
        table_body = d['table_body']
    else:
        return ''

    header = False
    # If there is no body, then we ignore the header
    if 'table_header' in d:
        table_header = d['table_header']
        header = True

    table_contents = []
    if header:
        header_contents = []
        for i in table_header:
            contents = _fix_references(i, config, make_link)
            header_contents.append(contents)
        table_contents.append(header_contents)

    for t in table_body:
        line_contents = []
        for i in t:
            contents = _fix_references(i, config, make_link)
            line_contents.append(contents)
        table_contents.append(line_contents)

    table = as_rest_table(table_contents, header=header)
    return get_indented_docstring_snippet(table, indent)


def get_rst_admonition_snippet(admonition, d, config, indent=0):
    '''Returns a rst formatted admonition if the given admonition ('note', 'caution') exists in the dictionary'''
    if admonition in d:
        a = '\n\n' + (' ' * indent) + '.. {0}:: '.format(admonition)
        a += get_indented_docstring_snippet(_fix_references(d[admonition], config, make_link=True), indent + 4)
        return a
    else:
        return ''


def get_documentation_for_node_rst(node, config, indent=0):
    '''Returns any documentaion information formatted for rst

    Documentation will be in the following order (if existing)
    - 'caution' admonition
    - 'description'
    - table made of 'table_header' and 'table_body'
    - 'note' admonition

    Args:
        node (dict) - Node possibly containing documentation
        config (dict) - build configuration
        indent (int) - how much each line should be indented

    Returns:
        str - formatted documentation, empty string if none
    '''
    doc = ''
    if 'documentation' not in node:
        return doc

    nd = node['documentation']
    doc += get_rst_admonition_snippet('caution', nd, config, indent)
    if 'description' in nd:
        doc += '\n\n' + (' ' * indent) + get_indented_docstring_snippet(_fix_references(nd['description'], config, make_link=True), indent)

    doc += '\n\n' + (' ' * indent) + _get_rst_table_snippet(nd, config, indent)
    doc += get_rst_admonition_snippet('note', nd, config, indent)
    doc += '\n'
    doc += get_rst_admonition_snippet('tip', nd, config, indent)
    doc += '\n'

    return doc


def get_documentation_for_node_docstring(node, config, indent=0):
    '''Returns any documentaion information formatted for docstring

    Documentation will be in the following order (if existing)
    - 'caution' admonition
    - 'description'
    - table made of 'table_header' and 'table_body'
    - 'note' admonition
    - 'tip' admonition

    Args:
        node (dict) - Node possibly containing documentation
        config (dict) - build configuration
        indent (int) - how much each line should be indented

    Returns:
        str - formatted documentation, empty string if none
    '''
    doc = ''
    if 'documentation' not in node:
        return doc

    nd = node['documentation']
    extra_newline = ''
    if 'caution' in nd:
        doc += '\n' + extra_newline + (' ' * indent) + get_indented_docstring_snippet(_fix_references('Caution: ' + nd['caution'], config, make_link=False), indent)
        extra_newline = '\n'

    if 'description' in nd:
        doc += '\n' + extra_newline + (' ' * indent) + get_indented_docstring_snippet(_fix_references(nd['description'], config, make_link=False), indent)
        extra_newline = '\n'

    tbl = _get_rst_table_snippet(nd, config, indent, make_link=False)
    if len(tbl) > 0:
        doc += '\n' + extra_newline + (' ' * indent) + tbl
        extra_newline = '\n'

    if 'note' in nd:
        doc += '\n' + extra_newline + (' ' * indent) + get_indented_docstring_snippet(_fix_references('Note: ' + nd['note'], config, make_link=False), indent)

    if 'tip' in nd:
        doc += '\n' + extra_newline + (' ' * indent) + get_indented_docstring_snippet(_fix_references('Tip: ' + nd['tip'], config, make_link=False), indent)

    return doc.strip()


# We need this in the global namespace so we can reference it from the sub() callback
config = None


def _find_attribute_by_name(attributes, name):
    '''Returns the attribute with the given name if there is one

    There should only be one so return that individual parameter and not a list
    '''
    attr = [attributes[x] for x in attributes if attributes[x]['name'] == name]
    assert len(attr) <= 1, '{0} attributes with name {1}. No more than one is allowed'.format(len(attr), name)
    if len(attr) == 0:
        return None
    return attr[0]


def _replace_attribute_python_name(a_match):
    '''callback function for regex sub command when link not needed

    Args:
        m (match object): Match object from the attribute substitution command

    Returns:
        str: python name of the attribute
    '''
    aname = "Unknown"
    if a_match:
        attr = _find_attribute_by_name(config['attributes'], a_match.group(1))
        aname = a_match.group(1)
        if attr:
            aname = attr['name'].lower()

    if config['make_link']:
        return ':py:data:`{0}.{1}`'.format(config['module_name'], aname)
    else:
        return '{0}'.format(aname)


def _replace_func_python_name(f_match):
    '''callback function for regex sub command when link needed

    Args:
        f_match (match object): Match object from the function substitution command

    Returns:
        str: rst link to function using python name
    '''
    fname = "Unknown"
    if f_match:
        fname = f_match.group(1).replace('.', '').replace(',', '').replace('\\', '')
        try:
            fname = config['functions'][fname]['python_name']
        except KeyError:
            print('Warning: "{0}" not found in function metadata. Typo? Generated code will be funky!'.format(fname))
    else:
        print('Unknown function name: {0}'.format(f_match.group(1)))
        print(config['functions'])

    if config['make_link']:
        return ':py:func:`{0}.{1}`'.format(config['module_name'], fname)
    else:
        return '{0}'.format(fname)


def _replace_urls(u_match):
    '''callback function for regex when url link needed

    Args:
        u_match (match object): Match object from the function substitution command

    Returns:
        str: replacement url
    '''
    if config['make_link']:
        pages = u_match.group(1)
        pages_list = pages.split(',')
        url_template = config['driver_urls'][config['url_key']]
        url = url_template.format(*pages_list)
        return url
    else:
        return u_match.group(1)


def _fix_references(doc, cfg, make_link=False):
    '''Replace ATTR and function mentions in documentation

    Args:
        doc (str): documentation string to be updated
        config (dict): config dictionary from metadata
        make_link (bool): Default False
            True - references are replaced with a rst style link
            False - references are replaced with just the python name

    Returns:
        str: documentation with references replaces based on make_link
    '''

    global config
    config = cfg

    config['make_link'] = make_link

    attr_re = re.compile('{0}\\\\_ATTR\\\\_([A-Z0-9\\\\_]+)'.format(config['module_name'].upper()))
    func_re = re.compile('{0}\\\\_([A-Za-z0-9\\\\_]+)'.format(config['c_function_prefix'].replace('_', '')))

    doc = attr_re.sub(_replace_attribute_python_name, doc)
    doc = func_re.sub(_replace_func_python_name, doc)

    if 'driver_urls' in cfg:
        for url_key in cfg['driver_urls']:
            url_re = re.compile('{0}\((.+?)\)'.format(url_key))
            config['url_key'] = url_key
            doc = url_re.sub(_replace_urls, doc)

    if not make_link:
        doc = doc.replace('\_', '_')
    return doc


def format_type_for_rst_documentation(param, numpy, config):
    if numpy and param['numpy']:
        p_type = param['numpy_type']
    elif param['enum'] is not None:
        p_type = ':py:data:`{0}.{1}`'.format(config['module_name'], param['enum'])
    elif 'python_api_converter_type' in param:
        p_type = param['python_api_converter_type']
    else:
        p_type = param['python_type']

    # We assume everything that is a buffer of ViChar is really a string (otherwise
    # it would end up as 'list of int'
    if param['type'] == 'ViChar' and param['is_buffer'] is True:
        p_type = 'string'
    elif param['is_buffer'] is True and numpy is True:
        p_type = 'numpy array of ' + p_type
    elif param['is_buffer'] is True:
        p_type = 'list of ' + p_type
    return p_type


rep_cap_method_desc = '''
This method requires repeated capabilities (usually channels). If called directly on the
{0}.Session object, then the method will use all repeated capabilities in the session.
You can specify a subset of repeated capabilities using the Python index notation on an
{0}.Session instance, and calling this method on the result.:
'''
rep_cap_method_desc_rst = rep_cap_method_desc + '''
.. code:: python

    session.channel[[0, 1]].{1}({2})
'''


def get_function_rst(function, method_template, numpy, config, indent=0):
    '''Gets formatted documentation for given function that can be used in rst documentation

    Args:
        function (dict): function dictionary
        config (dict): configuration dictoionary (from metadata)
        method_template (dict): entry from function['methos_temlates'] that corresponds to specific entry we are processon
        numpy (boolean): Is the entry we are processing a numpy based method
        indent (int): default 0 - initial indentation

    Returns:
        str: rst formatted documentation
    '''

    suffix = method_template['method_python_name_suffix']
    session_method = ParameterUsageOptions.DOCUMENTATION_SESSION_METHOD
    session_declaration = ParameterUsageOptions.SESSION_METHOD_DECLARATION
    output_parameters = ParameterUsageOptions.OUTPUT_PARAMETERS
    if numpy:
        session_declaration = ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION

    if function['has_repeated_capability'] is True:
        function['documentation']['tip'] = rep_cap_method_desc_rst.format(config['module_name'], function['python_name'], get_params_snippet(function, session_method))

    rst = '.. function:: ' + function['python_name'] + suffix + '('
    rst += get_params_snippet(function, session_method) + ')'
    indent += 4
    rst += get_documentation_for_node_rst(function, config, indent)

    input_params = filter_parameters(function, session_declaration)
    if len(input_params) > 0:
        rst += '\n'
    for p in input_params:
        rst += '\n' + (' ' * indent) + ':param {0}:'.format(p['python_name']) + '\n'
        rst += get_documentation_for_node_rst(p, config, indent + 4)

        p_type = format_type_for_rst_documentation(p, numpy, config)
        rst += '\n' + (' ' * indent) + ':type {0}: '.format(p['python_name']) + p_type

    output_params = filter_parameters(function, output_parameters)
    if len(output_params) > 1:
        rst += '\n\n' + (' ' * indent) + ':rtype: tuple (' + ', '.join([p['python_name'] for p in output_params]) + ')\n\n'
        rst += (' ' * (indent + 4)) + 'WHERE\n'
        for p in output_params:
            p_type = format_type_for_rst_documentation(p, numpy, config)
            rst += '\n' + (' ' * (indent + 4)) + '{0} ({1}): '.format(p['python_name'], p_type) + '\n'
            rst += get_documentation_for_node_rst(p, config, indent + 8)
    elif len(output_params) == 1:
        p = output_params[0]
        p_type = format_type_for_rst_documentation(p, numpy, config)
        rst += '\n\n' + (' ' * indent) + ':rtype: ' + p_type + '\n'
        rst += (' ' * indent) + ':return:\n' + get_documentation_for_node_rst(p, config, indent + 8)

    return rst


def _format_type_for_docstring(param, numpy, config):
    if numpy and param['numpy']:
        p_type = param['numpy_type']
    elif 'python_api_converter_type' in param:
        p_type = param['python_api_converter_type'] + ' or ' + param['python_type']
    else:
        p_type = param['python_type']

    # We assume everything that is a buffer of ViChar is really a string (otherwise
    # it would end up as 'list of int'
    if param['type'] == 'ViChar' and param['is_buffer'] is True:
        p_type = 'string'
    elif param['is_buffer'] is True and numpy is True:
        p_type = 'numpy array of ' + p_type
    elif param['is_buffer'] is True:
        p_type = 'list of ' + p_type
    return p_type


rep_cap_method_desc_docstring = rep_cap_method_desc + '''
    session.channel[[0, 1]].{1}({2})
'''


def get_function_docstring(function, method_template, numpy, config, indent=0):
    '''Gets formatted documentation for given function that can be used as a docstring

    Args:
        function (dict): function dictionary
        config (dict): configuration dictoionary (from metadata)
        method_template (dict): entry from function['methos_temlates'] that corresponds to specific entry we are processon
        numpy (boolean): Is the entry we are processing a numpy based method
        indent (int): default 0 - initial indentation

    Returns:
        str: docstring formatted documentation
    '''
    session_method = ParameterUsageOptions.DOCUMENTATION_SESSION_METHOD
    session_declaration = ParameterUsageOptions.SESSION_METHOD_DECLARATION
    output_parameters = ParameterUsageOptions.OUTPUT_PARAMETERS
    if numpy:
        session_declaration = ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION

    docstring = ''
    if function['has_repeated_capability'] is True:
        function['documentation']['tip'] = rep_cap_method_desc_docstring.format(config['module_name'], function['python_name'], get_params_snippet(function, session_method))

    docstring += get_documentation_for_node_docstring(function, config, indent)

    input_params = filter_parameters(function, session_declaration)
    if len(input_params) > 0:
        docstring += '\n\n' + (' ' * indent) + 'Args:'
    for p in input_params:
        docstring += '\n' + (' ' * (indent + 4)) + '{0} ({1}):'.format(p['python_name'], _format_type_for_docstring(p, numpy, config))
        ds = get_documentation_for_node_docstring(p, config, indent + 8)
        if len(ds) > 0:
            docstring += ' ' + ds

    output_params = filter_parameters(function, output_parameters)
    if len(output_params) > 0:
        docstring += '\n\n' + (' ' * indent) + 'Returns:'
        for p in output_params:
            docstring += '\n' + (' ' * (indent + 4)) + '{0} ({1}):'.format(p['python_name'], _format_type_for_docstring(p, numpy, config))
            ds = get_documentation_for_node_docstring(p, config, indent + 8)
            if len(ds) > 0:
                docstring += ' ' + ds

    return docstring


# From http://code.activestate.com/recipes/579054-generate-sphinx-table/
def as_rest_table(data, header=True):
    """Create rst formatted table

    >>> data = [('what', 'how', 'who'),
    ...         ('lorem', 'that is a long value', 3.1415),
    ...         ('ipsum', 89798, 0.2)]
    >>> print(as_rest_table(data))
    +-------+----------------------+--------+
    | what  | how                  | who    |
    +=======+======================+========+
    | lorem | that is a long value | 3.1415 |
    +-------+----------------------+--------+
    | ipsum |                89798 |    0.2 |
    +-------+----------------------+--------+
    >>> print(as_rest_table(data, header=False))
    +-------+----------------------+--------+
    | what  | how                  | who    |
    +-------+----------------------+--------+
    | lorem | that is a long value | 3.1415 |
    +-------+----------------------+--------+
    | ipsum |                89798 |    0.2 |
    +-------+----------------------+--------+
    """
    data = data if data else [['No Data']]
    table = []
    # max size of each column
    sizes = map(max, zip(*[[len(str(elt)) for elt in member] for member in data]))
    if sys.version_info.major >= 3:
        sizes = list(sizes)
    num_elts = len(sizes)

    start_of_line = '| '
    vertical_separator = ' | '
    end_of_line = ' |'
    line_marker = '-'

    meta_template = vertical_separator.join(['{{{{{0}:{{{0}}}}}}}'.format(i) for i in range(num_elts)])
    template = '{0}{1}{2}'.format(start_of_line, meta_template.format(*sizes), end_of_line)
    # determine top/bottom borders
    to_separator = {ord('|'): '+', ord(' '): '-'}
    if sys.version_info.major < 3:
        to_separator = string.maketrans('| ', '+-')

    start_of_line = start_of_line.translate(to_separator)
    vertical_separator = vertical_separator.translate(to_separator)
    end_of_line = end_of_line.translate(to_separator)
    separator = '{0}{1}{2}'.format(start_of_line, vertical_separator.join([x * line_marker for x in sizes]), end_of_line)
    # determine header separator
    th_separator_tr = {ord('-'): '='}
    if sys.version_info.major < 3:
        th_separator_tr = string.maketrans('-', '=')
    start_of_line = start_of_line.translate(th_separator_tr)
    line_marker = line_marker.translate(th_separator_tr)
    vertical_separator = vertical_separator.translate(th_separator_tr)
    end_of_line = end_of_line.translate(th_separator_tr)
    th_separator = '{0}{1}{2}'.format(start_of_line, vertical_separator.join([x * line_marker for x in sizes]), end_of_line)
    # prepare result
    table.append(separator)
    # set table header
    titles = data[0]
    table.append(template.format(*titles))

    if header:
        table.append(th_separator)
    else:
        table.append(separator)

    for d in data[1:-1]:
        table.append(template.format(*d))
        table.append(separator)
    table.append(template.format(*data[-1]))
    table.append(separator)
    return '\n'.join(table)


# Unit Tests


def _remove_trailing_whitespace(s):
    '''Removes trailing whitespace and empty lines in multi-line strings.'''
    initial_lines = s.strip().splitlines()
    fixed_lines = []
    blank_lines = 0
    for l in initial_lines:
        stripped_line = l.strip()
        if len(stripped_line) == 0 and blank_lines == 0:
            fixed_lines.append(stripped_line)
            blank_lines = 1
        if len(stripped_line) > 0:
            fixed_lines.append(stripped_line)
            blank_lines = 0

    return fixed_lines


def assert_rst_strings_are_equal(expected, actual):
    '''Asserts rst formatted strings (multiline) are equal. Ignores trailing whitespace and empty lines.'''
    expected = _remove_trailing_whitespace(expected)
    actual = _remove_trailing_whitespace(actual)
    for expected_line, actual_line in zip(expected, actual):
        assert expected_line == actual_line, 'Difference found:\n{0}\n{1}'.format(expected_line, actual_line)


config = {
    'functions': {
        'GetTurtleID': {
            'codegen_method': 'public',
            'returns': 'ViStatus',
            'method_templates': [{'filename': '/default_method', 'method_python_name_suffix': '', }, ],
            'parameters': [
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'vi',
                    'type': 'ViSession',
                    'documentation': {
                        'description': 'Identifies a particular instrument session.'
                    },
                    'python_name': 'vi',
                    'python_type': 'int',
                    'ctypes_variable_name': 'vi_ctype',
                    'ctypes_type': 'ViSession',
                    'ctypes_type_library_call': 'ViSession',
                    'size': {
                        'mechanism': 'fixed',
                        'value': 1
                    },
                    'is_buffer': False,
                    'python_name_with_default': 'vi',
                    'python_name_with_doc_default': 'vi',
                    'is_repeated_capability': False,
                    'is_session_handle': True,
                    'library_method_call_snippet': 'self._vi',
                    'use_in_python_api': True,
                },
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'turtleType',
                    'type': 'ViInt32',
                    'documentation': {
                        'description': '''Specifies the type of Turtle type
wanted to choose.''',
                        'note': 'You wont be able to import RAPHAEL',
                        'table_body': [
                            ['NIFake\\_VAL\\_LEONARDO (default)', '0', 'LEONARDO'],
                            ['NIFake\\_VAL\\_DONATELLO', '1', 'DONATELLO'],
                            ['NIFake\\_VAL\\_RAPHAEL', '2', 'RAPHAEL'],
                            ['NIFake\\_VAL\\_MICHELANGELO', '3', 'MICHELANGELO']
                        ]
                    },
                    'python_name': 'turtle_type',
                    'python_type': 'int',
                    'ctypes_variable_name': 'turtle_type_ctype',
                    'ctypes_type': 'ViInt32',
                    'ctypes_type_library_call': 'ViInt32',
                    'size': {
                        'mechanism': 'fixed',
                        'value': 1
                    },
                    'is_buffer': False,
                    'python_name_with_default': 'turtle_type',
                    'python_name_with_doc_default': 'turtle_type',
                    'is_repeated_capability': False,
                    'is_session_handle': False,
                    'library_method_call_snippet': 'turtle_type',
                    'use_in_python_api': True,
                },
                {
                    'direction': 'out',
                    'enum': None,
                    'name': 'turtleId',
                    'type': 'ViReal64',
                    'documentation': {
                        'description': 'Returns the **ID** of selected turtle.'
                    },
                    'python_name': 'turtle_id',
                    'python_type': 'float',
                    'ctypes_variable_name': 'turtleId_ctype',
                    'ctypes_type': 'ViReal64',
                    'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
                    'size': {
                        'mechanism': 'fixed',
                        'value': 1
                    },
                    'is_buffer': False,
                    'python_name_with_default': 'turtleId',
                    'python_name_with_doc_default': 'turtleId',
                    'is_repeated_capability': False,
                    'is_session_handle': False,
                    'library_method_call_snippet': 'ctypes.pointer(turtleId_ctype)',
                    'use_in_python_api': True,
                }
            ],
            'documentation': {
                'description': 'Returns the **ID** of selected Turtle Type.',
                'note': 'The RAPHAEL Turtles dont have an ID.'
            },
            'name': 'GetTurtleID',
            'python_name': 'get_turtle_id',
            'is_error_handling': False,
            'has_repeated_capability': False
        },
        'FetchWaveform': {
            'codegen_method': 'public',
            'documentation': {'description': 'Returns waveform data.'},
            'has_repeated_capability': False,
            'is_error_handling': False,
            'method_templates': [{'filename': '/default_method', 'method_python_name_suffix': ''}, {'filename': '/numpy_method', 'method_python_name_suffix': '_into'}],
            'name': 'FetchWaveform',
            'parameters': [
                {
                    'ctypes_type': 'ViSession',
                    'ctypes_type_library_call': 'ViSession',
                    'ctypes_variable_name': 'vi_ctype',
                    'direction': 'in',
                    'documentation': {'description': 'Identifies a particular instrument session.'},
                    'enum': None,
                    'is_buffer': False,
                    'is_repeated_capability': False,
                    'is_session_handle': True,
                    'library_method_call_snippet': 'vi_ctype',
                    'name': 'vi',
                    'numpy': False,
                    'python_name': 'vi',
                    'python_name_with_default': 'vi',
                    'python_name_with_doc_default': 'vi',
                    'python_type': 'int',
                    'size': {'mechanism': 'fixed', 'value': 1},
                    'type': 'ViSession',
                    'use_in_python_api': True,
                },
                {
                    'ctypes_type': 'ViInt32',
                    'ctypes_type_library_call': 'ViInt32',
                    'ctypes_variable_name': 'number_of_samples_ctype',
                    'direction': 'in',
                    'documentation': {'description': 'Number of samples to return'},
                    'enum': None,
                    'is_buffer': False,
                    'is_repeated_capability': False,
                    'is_session_handle': False,
                    'library_method_call_snippet': 'number_of_samples_ctype',
                    'name': 'numberOfSamples',
                    'numpy': False,
                    'python_name': 'number_of_samples',
                    'python_name_with_default': 'number_of_samples',
                    'python_name_with_doc_default': 'number_of_samples',
                    'python_type': 'int',
                    'size': {'mechanism': 'fixed', 'value': 1},
                    'type': 'ViInt32',
                    'use_in_python_api': True,
                },
                {
                    'ctypes_type': 'ViReal64',
                    'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
                    'ctypes_variable_name': 'waveform_data_ctype',
                    'direction': 'out',
                    'documentation': {'description': 'Samples fetched from the device. Array should be numberOfSamples big.'},
                    'enum': None,
                    'is_buffer': True,
                    'is_repeated_capability': False,
                    'is_session_handle': False,
                    'library_method_call_snippet': 'waveform_data_ctype',
                    'name': 'waveformData',
                    'numpy': True,
                    'numpy_type': 'float64',
                    'original_type': 'ViReal64[]',
                    'python_name': 'waveform_data',
                    'python_name_with_default': 'waveform_data',
                    'python_name_with_doc_default': 'waveform_data',
                    'python_type': 'float',
                    'size': {'mechanism': 'passed-in', 'value': 'numberOfSamples'},
                    'type': 'ViReal64',
                    'use_in_python_api': True,
                },
                {
                    'ctypes_type': 'ViInt32',
                    'ctypes_type_library_call': 'ctypes.POINTER(ViInt32)',
                    'ctypes_variable_name': 'actual_number_of_samples_ctype',
                    'direction': 'out',
                    'documentation': {'description': 'Number of samples actually fetched.'},
                    'enum': None,
                    'is_buffer': False,
                    'is_repeated_capability': False,
                    'is_session_handle': False,
                    'library_method_call_snippet': 'ctypes.pointer(actual_number_of_samples_ctype)',
                    'name': 'actualNumberOfSamples',
                    'numpy': False,
                    'python_name': 'actual_number_of_samples',
                    'python_name_with_default': 'actual_number_of_samples',
                    'python_name_with_doc_default': 'actual_number_of_samples',
                    'python_type': 'int',
                    'size': {'mechanism': 'fixed', 'value': 1},
                    'type': 'ViInt32',
                    'use_in_python_api': True,
                }
            ],
            'python_name': 'fetch_waveform',
            'render_in_session_base': False,
            'returns': 'ViStatus'
        },
    },
    'metadata_version': '1.0',
    'module_name': 'nifake',
    'module_version': '0.3.0.dev0',
    'c_function_prefix': 'niFake_',
    'driver_name': 'NI-FAKE',
    'session_class_description': 'An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation',
    'session_handle_parameter_name': 'vi',
    'library_info':
    {
        'Windows': {
            '32bit': {'name': 'nifake_32.dll', 'type': 'windll'},
            '64bit': {'name': 'nifake_64.dll', 'type': 'cdll'},
        },
        'Linux': {
            '64bit': {'name': 'libnifake.so', 'type': 'cdll'},
        },
    },
    'context_manager_name': {
        'task': 'acquisition',
        'initiate_function': 'Initiate',
        'abort_function': 'Abort',
    },
    'init_function': 'InitWithOptions',
}


def test_get_function_rst_default():
    function = config['functions']['GetTurtleID']
    method_template = function['method_templates'][0]
    actual_function_rst = get_function_rst(function, method_template=method_template, numpy=False, config=config, indent=0)
    expected_fuction_rst = '''.. function:: get_turtle_id(turtle_type)

    Returns the **ID** of selected Turtle Type.

    .. note:: The RAPHAEL Turtles dont have an ID.

    :param turtle_type:

    Specifies the type of Turtle type
    wanted to choose.

    +---------------------------------+---+--------------+
    | NIFake\_VAL\_LEONARDO (default) | 0 | LEONARDO     |
    +---------------------------------+---+--------------+
    | NIFake\_VAL\_DONATELLO          | 1 | DONATELLO    |
    +---------------------------------+---+--------------+
    | NIFake\_VAL\_RAPHAEL            | 2 | RAPHAEL      |
    +---------------------------------+---+--------------+
    | NIFake\_VAL\_MICHELANGELO       | 3 | MICHELANGELO |
    +---------------------------------+---+--------------+

    .. note:: You wont be able to import RAPHAEL

    :type turtle_type: int

    :rtype: float
    :return:

        Returns the **ID** of selected turtle.
'''
    assert_rst_strings_are_equal(expected_fuction_rst, actual_function_rst)


def test_get_function_rst_numpy():
    function = config['functions']['FetchWaveform']
    method_template = function['method_templates'][0]
    actual_function_rst = get_function_rst(function, method_template=method_template, numpy=True, config=config, indent=0)
    expected_fuction_rst = '''.. function:: fetch_waveform(number_of_samples)

    Returns waveform data.

    :param number_of_samples:

        Number of samples to return

    :type number_of_samples: int
    :param waveform_data:

        Samples fetched from the device. Array should be numberOfSamples big.

    :type waveform_data: numpy array of float64

    :rtype: tuple (waveform_data, actual_number_of_samples)

        WHERE

        waveform_data (numpy array of float64):

            Samples fetched from the device. Array should be numberOfSamples big.

        actual_number_of_samples (int):

            Number of samples actually fetched.
'''
    assert_rst_strings_are_equal(expected_fuction_rst, actual_function_rst)


def test_get_function_docstring_default():
    function = config['functions']['GetTurtleID']
    method_template = function['method_templates'][0]
    actual_function_docstring = get_function_docstring(function, method_template=method_template, numpy=False, config=config, indent=0)
    expected_function_docstring = '''Returns the **ID** of selected Turtle Type.

Note: The RAPHAEL Turtles dont have an ID.

Args:
    turtle_type (int): Specifies the type of Turtle type
        wanted to choose.

        +-------------------------------+---+--------------+
        | NIFake_VAL_LEONARDO (default) | 0 | LEONARDO     |
        +-------------------------------+---+--------------+
        | NIFake_VAL_DONATELLO          | 1 | DONATELLO    |
        +-------------------------------+---+--------------+
        | NIFake_VAL_RAPHAEL            | 2 | RAPHAEL      |
        +-------------------------------+---+--------------+
        | NIFake_VAL_MICHELANGELO       | 3 | MICHELANGELO |
        +-------------------------------+---+--------------+

        Note: You wont be able to import RAPHAEL

Returns:
    turtle_id (float): Returns the **ID** of selected turtle.''' # noqa
    assert_rst_strings_are_equal(expected_function_docstring, actual_function_docstring)


def test_get_function_docstring_numpy():
    function = config['functions']['FetchWaveform']
    method_template = function['method_templates'][0]
    actual_function_docstring = get_function_docstring(function, method_template=method_template, numpy=True, config=config, indent=0)
    print(actual_function_docstring)
    expected_fuction_docstring = '''Returns waveform data.

    Args:
        number_of_samples (int): Number of samples to return
        waveform_data (numpy array of float64): Samples fetched from the device. Array should be numberOfSamples big.

    Returns:
        waveform_data (numpy array of float64): Samples fetched from the device. Array should be numberOfSamples big.
        actual_number_of_samples (int): Number of samples actually fetched.
'''
    assert_rst_strings_are_equal(expected_fuction_docstring, actual_function_docstring)


def test_get_rst_header_snippet():
    header = "This will be your method header"
    actual_rst_header = get_rst_header_snippet(header)
    expected_rst_header = """This will be your method header
==============================="""
    assert actual_rst_header == expected_rst_header


def test_get_documentation_for_node_docstring():
    caution = """ this is a very
long string if I had the
energy to type more and more ..."""
    description = """ This string might be
at maximum size I can handle"""
    node = {
        'documentation': {
            'caution': caution,
            'description': description,
            'table_header': ['what', 'how', 'who'],
            'table_body': [
                ['lorem', 'that is a dummy string', 'Place holder string'],
                ['ipsum', 'this is a random strinf', 'Yes, I am a random string']
            ]
        }
    }
    actual_documentation = get_documentation_for_node_docstring(node, config, indent=4)
    expected_documentation = """Caution:  this is a very
    long string if I had the
    energy to type more and more ...

    This string might be
    at maximum size I can handle

    +-------+-------------------------+---------------------------+
    | what  | how                     | who                       |
    +=======+=========================+===========================+
    | lorem | that is a dummy string  | Place holder string       |
    +-------+-------------------------+---------------------------+
    | ipsum | this is a random strinf | Yes, I am a random string |
    +-------+-------------------------+---------------------------+""" # noqa
    assert_rst_strings_are_equal(expected_documentation, actual_documentation)
