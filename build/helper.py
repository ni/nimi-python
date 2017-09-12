# TODO(marcoskirsch): This file should definitely not live here but I had trouble getting import to work.
# TODO(marcoskirsch): Figure out unit test for this.

from contextlib import contextmanager
from enum import Enum
import importlib
import pprint
import re
import string
import sys

pp = pprint.PrettyPrinter(indent=4)

# Coding convention transformation functions.


# TODO(marcoskirsch): not being used
def shoutcase_to_camelcase(shout_string):
    '''Converts a C-style SHOUT_CASE string to camelCase'''
    components = shout_string.split('_')
    return components[0].lower() + "".join(component.title() for component in components[1:])


def camelcase_to_snakecase(camelcase_string):
    '''Converts a camelCase string to lower_case_snake_case'''
    # https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camelcase_string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


# TODO(marcoskirsch): not being used
def function_to_method_name(f):
    '''Returns an appropriate session method name for a given function'''
    # Method name is camelCase.
    return f['name'][0].lower() + f['name'][1:]

# Filters


def extract_codegen_functions(functions):
    '''Returns function metadata only for those functions to be included in codegen'''
    funcs = {}
    for x in functions:
        if functions[x]['codegen_method'] != 'no':
            funcs[x] = functions[x]
    return funcs


def extract_input_parameters(parameters, session_name='vi'):
    '''Returns list of parameters that includes only input parameters, except the session parameter if it exists'''
    return [x for x in parameters if x['direction'] == 'in' and x['name'] != session_name]


def extract_output_parameters(parameters):
    '''Returns list of parameters that includes only output parameters, except the ivi-dance parameter if it exists'''
    return [x for x in parameters if x['direction'] == 'out' and x['size']['mechanism'] != 'ivi-dance']


def extract_enum_parameters(parameters):
    '''Returns a list of parameters whose type is an enum'''
    return [x for x in parameters if x['enum'] is not None]


def extract_ivi_dance_parameter(parameters):
    '''Returns the ivi-dance parameter of a session method if there is one. This is the parameter whose size is determined at runtime.'''
    param = [x for x in parameters if x['size']['mechanism'] == 'ivi-dance']
    assert len(param) <= 1, '{0} ivi-dance parameters. No more than one is allowed'.format(len(param))
    if len(param) == 0:
        return None
    assert param[0]['direction'] == 'out', "ivi-dance parameter must have 'direction':'out'. Check your metadata."
    assert param[0]['is_buffer'], "ivi-dance parameter must have 'is_buffer':True. Check your metadata."
    return param[0]

# Find utilities


def find_parameter(name, parameters):
    parameter = [x for x in parameters if x['name'] == name]
    assert len(parameter) == 1, 'Parameter {0} not found. Check your metadata.'.format(name)
    return parameter[0]


def find_size_parameter(parameter, parameters):
    '''Returns the parameter that is used to specify the size of another parameter. Applies to 'ivi-dance' and 'passed-in'.'''
    if not parameter:
        return None
    return find_parameter(parameter['size']['value'], parameters)

# Python 2/3 compatibility


def normalize_string_type(d):
    '''Normalize string type between python2 & python3'''
    if sys.version_info.major < 3:
        if type(d) is dict:
            for k in d:
                d[k] = normalize_string_type(d[k])
        elif type(d) is str:
            d = d.decode('utf-8')
    return d


# Functions that return snippets that can be placed directly in the templates.
class ParamListType(Enum):
    '''Type of parameter list to return'''
    API_METHOD = 1
    '''Used for methods param list for the public API'''
    IMPL_METHOD = 2
    '''Used for methods param list for implementation'''
    DISPLAY_METHOD = 3
    '''Used for methods param list for disple (rst)'''
    LIBRARY_METHOD = 4
    '''Used for methods param list when calling library'''


ParamListTypeDefaults = {}
ParamListTypeDefaults[ParamListType.API_METHOD] = {
    'skip_self': False,
    'skip_session_handle': True,
    'skip_output_parameters': True,
    'skip_ivi_dance_size_parameter': True,
    'session_name': 'vi',
}
ParamListTypeDefaults[ParamListType.IMPL_METHOD] = {
    'skip_self': False,
    'skip_session_handle': False,
    'skip_output_parameters': False,
    'skip_ivi_dance_size_parameter': False,
    'session_name': 'vi',
}
ParamListTypeDefaults[ParamListType.DISPLAY_METHOD] = {
    'skip_self': True,
    'skip_session_handle': True,
    'skip_output_parameters': True,
    'skip_ivi_dance_size_parameter': True,
    'session_name': 'vi',
}
ParamListTypeDefaults[ParamListType.LIBRARY_METHOD] = {
    'skip_self': True,
    'skip_session_handle': False,
    'skip_output_parameters': False,
    'skip_ivi_dance_size_parameter': False,
    'session_name': 'vi',
}


def get_params_snippet(function, param_type, options={}):
    '''Get a parameter list snippet based on type and options'''
    if type(param_type) is not ParamListType:
        raise TypeError('param_type must be of type ' + str(ParamListType))
    if type(options) is not dict:
        raise TypeError('param_type must be of type ' + str(dict))

    params_to_use = function['parameters']
    options_to_use = ParamListTypeDefaults[param_type]
    for o in options:
        options_to_use[o] = options[o]

    snippets = ['self']
    ivi_dance_size_parameter = find_size_parameter(extract_ivi_dance_parameter(params_to_use), params_to_use)
    for x in params_to_use:
        skip = False
        if x['direction'] == 'out' and options_to_use['skip_output_parameters']:
            skip = True
        if x == ivi_dance_size_parameter and options_to_use['skip_ivi_dance_size_parameter']:
            skip = True
        if x['name'] == options_to_use['session_name'] and options_to_use['skip_session_handle']:
            skip = True
        if not skip:
            snippets.append(x[name_to_use])
    return ', '.join(snippets)


def get_function_parameters_snippet(parameters, session_name='vi'):
    '''Returns a string suitable for the parameter list of a method given a list of parameter objects

    If session_name set, skip that parameter
    '''
    snippets = []
    for x in parameters:
        if session_name is not None and x['python_name'] == session_name:
            continue
        snippets.append(x['python_name'])
    return ', '.join(snippets)


def get_library_call_parameter_snippet(parameters_list, session_name='vi'):
    '''Returns a string suitable to use as the parameters to the library object, i.e. "self, mode, range, digits_of_resolution"'''
    snippets = []
    for x in parameters_list:
        if x['direction'] == 'in':
            if x['name'] == session_name:
                snippet = 'self.' + session_name
            else:
                snippet = x['python_name']
                snippet += '.value' if x['enum'] is not None else ''
                if x['type'] == 'ViString' or x['type'] == 'ViConstString' or x['type'] == 'ViRsrc':
                    snippet += '.encode(\'ascii\')'
        else:
            assert x['direction'] == 'out', pp.pformat(x)
            if x['size']['mechanism'] == 'ivi-dance':
                snippet = x['ctypes_variable_name']
            elif x['is_buffer']:
                snippet = 'ctypes.cast(' + x['ctypes_variable_name'] + ', ctypes.POINTER(ctypes_types.' + x['ctypes_type'] + '))'
            else:
                snippet = 'ctypes.pointer(' + (x['ctypes_variable_name']) + ')'
        snippets.append(snippet)
    return ', '.join(snippets)


def get_library_call_parameter_types_snippet(parameters_list):
    '''Returns a string suitable to use as the parameters to the library definition object'''
    snippets = []
    for x in parameters_list:
        if x['direction'] == 'out':
            if x['type'] == 'ViString' or x['type'] == 'ViRsrc' or x['type'] == 'ViConstString_ctype':
                # These are defined as c_char_p which is already a pointer!
                snippets.append(x['ctypes_type'])
            else:
                snippets.append("ctypes.POINTER(" + x['ctypes_type'] + ")")
        else:
            assert x['direction'] == 'in', pp.pformat(x)
            snippets.append(x['ctypes_type'])
    return ', '.join(snippets)


def _get_output_param_return_snippet(output_parameter, parameters):
    '''Returns the snippet for returning a single output parameter from a Session method, i.e. "reading_ctype.value"'''
    assert output_parameter['direction'] == 'out', pp.pformat(output_parameter)
    return_type_snippet = ''
    if output_parameter['enum'] is not None:
        return_type_snippet = 'enums.' + output_parameter['enum'] + '('
    else:
        return_type_snippet = 'python_types.' + output_parameter['python_type'] + '('

    if output_parameter['is_buffer']:
        if output_parameter['type'] == 'ViChar' or output_parameter['type'] == 'ViString':
            snippet = output_parameter['ctypes_variable_name'] + '.value.decode("ascii")'
        else:
            size_parameter = find_size_parameter(output_parameter, parameters)
            snippet = '[' + return_type_snippet + output_parameter['ctypes_variable_name'] + '[i].value) for i in range(' + size_parameter['python_name'] + ')]'
    else:
        snippet = return_type_snippet + output_parameter['ctypes_variable_name'] + '.value)'

    return snippet


def get_method_return_snippet(parameters):
    '''Returns a string suitable to use as the return argument of a Session method, i.e. "return reading_ctype.value"'''
    snippets = []
    for x in parameters:
        if x['direction'] == 'out' or x['size']['mechanism'] == 'ivi-dance':
            snippets.append(_get_output_param_return_snippet(x, parameters))
    return ('return ' + ', '.join(snippets)).strip()


def get_enum_type_check_snippet(parameter, indent):
    '''Returns python snippet to check that the type of a parameter is what is expected'''
    assert parameter['enum'] is not None, pp.pformat(parameter)
    assert parameter['direction'] == 'in', pp.pformat(parameter)
    return 'if type(' + parameter['python_name'] + ') is not ' + parameter['python_type'] + ':\n' + (' ' * indent) + 'raise TypeError(\'Parameter mode must be of type \' + str(' + parameter['python_type'] + '))'


def get_ctype_variable_declaration_snippet(parameter, parameters):
    '''Returns python snippet to declare and initialize the corresponding ctypes variable'''
    assert parameter['direction'] == 'out', pp.pformat(parameter)
    snippet = parameter['ctypes_variable_name'] + ' = '
    if parameter['is_buffer']:
        if parameter['size']['mechanism'] == 'fixed':
            snippet += '(' + 'ctypes_types.' + parameter['ctypes_type'] + ' * ' + str(parameter['size']['value']) + ')()'
        elif parameter['size']['mechanism'] == 'ivi-dance':
            # TODO(marcoskirsch): remove.
            assert False, "THIS IS DEAD CODE!"
            snippet += 'ctypes_types.' + parameter['ctypes_type'] + '(0)  # TODO(marcoskirsch): Do the IVI-dance!'
        else:
            assert parameter['size']['mechanism'] == 'passed-in', parameter['size']['mechanism']
            size_parameter = find_size_parameter(parameter, parameters)
            snippet += '(' + 'ctypes_types.' + parameter['ctypes_type'] + ' * ' + size_parameter['python_name'] + ')()'
    else:
        snippet += 'ctypes_types.' + parameter['ctypes_type'] + '(0)'
    return snippet


def get_dictionary_snippet(d, indent=4):
    '''Returns a formatted dictionary'''
    d_str = pprint.pformat(d)
    d_lines = d_str.splitlines()
    return ('\n' + (' ' * indent)).join(d_lines)


def sorted_attrs(a):
    return sorted(a, key=lambda k: a[k]['name'])


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
        ret_val += normalize_string_type(l.rstrip())
    return ret_val


def get_rst_header_snippet(t, header_level='='):
    '''Get rst formatted heading'''
    ret_val = t + '\n'
    ret_val += header_level * len(t)
    return ret_val


def get_rst_table_snippet(d, config, indent=0, make_link=True):
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
            contents = fix_references(i, config, make_link)
            header_contents.append(contents)
        table_contents.append(header_contents)

    for t in table_body:
        line_contents = []
        for i in t:
            contents = fix_references(i, config, make_link)
            line_contents.append(contents)
        table_contents.append(line_contents)

    table = as_rest_table(table_contents, full=True, header=header)
    return get_indented_docstring_snippet(table, indent)


def get_rst_admonition_snippet(admonition, d, config, indent=0):
    '''Returns a rst formatted admonition if the given admonition ('note', 'caution') exists in the dictionary'''
    if admonition in d:
        a = '\n\n' + (' ' * indent) + '.. {0}:: '.format(admonition) + get_indented_docstring_snippet(fix_references(d[admonition], config, make_link=True), indent + 4)
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
        doc += '\n\n' + (' ' * indent) + get_indented_docstring_snippet(fix_references(nd['description'], config, make_link=True), indent)

    doc += '\n\n' + (' ' * indent) + get_rst_table_snippet(nd, config, indent)
    doc += get_rst_admonition_snippet('note', nd, config, indent)
    doc += '\n'

    return doc


def get_documentation_for_node_docstring(node, config, indent=0):
    '''Returns any documentaion information formatted for docstring

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
    extra_newline = ''
    if 'caution' in nd:
        doc += '\n' + extra_newline + (' ' * indent) + get_indented_docstring_snippet(fix_references('Caution: ' + nd['caution'], config, make_link=False), indent)
        extra_newline = '\n'

    if 'description' in nd:
        doc += '\n' + extra_newline + (' ' * indent) + get_indented_docstring_snippet(fix_references(nd['description'], config, make_link=False), indent)
        extra_newline = '\n'

    tbl = get_rst_table_snippet(nd, config, indent, make_link=False)
    if len(tbl) > 0:
        doc += '\n' + extra_newline + (' ' * indent) + tbl
        extra_newline = '\n'

    if 'note' in nd:
        doc += '\n' + extra_newline + (' ' * indent) + get_indented_docstring_snippet(fix_references('Note: ' + nd['note'], config, make_link=False), indent)

    return doc.strip()


# We need this in the global namespace so we can reference it from the sub() callback
config = None


def find_attribute_by_name(attributes, name):
    '''Returns the attribute with the given name if there is one

    There should only be one so return that individual parameter and not a list
    '''
    attr = [attributes[x] for x in attributes if attributes[x]['name'] == name]
    assert len(attr) <= 1, '{0} attributes with name {1}. No more than one is allowed'.format(len(attr), name)
    if len(attr) == 0:
        return None
    return attr[0]


def replace_attribute_python_name(a_match):
    '''callback function for regex sub command when link not needed

    Args:
        m (match object): Match object from the attribute substitution command

    Returns:
        str: python name of the attribute
    '''
    aname = "Unknown"
    if a_match:
        attr = find_attribute_by_name(config['attributes'], a_match.group(1))
        aname = a_match.group(1)
        if attr:
            aname = attr['name'].lower()

    if config['make_link']:
        return ':py:data:`{0}.{1}`'.format(config['module_name'], aname)
    else:
        return '{0}'.format(aname)


def replace_func_python_name(f_match):
    '''callback function for regex sub command when link needed

    Args:
        m (match object): Match object from the function substitution command

    Returns:
        str: rst link to function using python name
    '''
    fname = "Unknown"
    if f_match:
        fname = f_match.group(1).replace('.', '').replace(',', '').replace('\\', '')
        fname = config['functions'][fname]['python_name']
    else:
        print('Unknown function name: {0}'.format(f_match.group(1)))
        print(config['functions'])

    if config['make_link']:
        return ':py:func:`{0}.{1}`'.format(config['module_name'], fname)
    else:
        return '{0}'.format(fname)


def fix_references(doc, cfg, make_link=False):
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

    doc = attr_re.sub(replace_attribute_python_name, doc)
    doc = func_re.sub(replace_func_python_name, doc)

    if not make_link:
        doc = doc.replace('\_', '_')
    return doc


def get_function_rst(fname, config, indent=0):
    '''Gets rst formatted documentation for given function

    Args:
        fname (str): Function name - key in function dictionary
        function (dict): function entry correcsponding to fname in function dictionary

    Returns:
        str: rst formatted documentation
    '''
    function = config['functions'][fname]
    rst = '.. function:: ' + function['python_name'] + '('
    rst += get_params_snippet(function, ParamListType.DISPLAY_METHOD) + ')'
    indent += 4
    rst += get_documentation_for_node_rst(function, config, indent)

    input_params = extract_input_parameters(function['parameters'])
    if len(input_params) > 0:
        rst += '\n'
    for p in input_params:
        rst += '\n' + (' ' * indent) + ':param {0}:'.format(p['python_name']) + '\n'
        rst += get_documentation_for_node_rst(p, config, indent + 4)

        p_type = p['intrinsic_type']
        if p_type.startswith('enums.'):
            p_type = p_type.replace('enums.', '')
            p_type = ':py:data:`{0}.{1}`'.format(config['module_name'], p_type)
        rst += '\n' + (' ' * indent) + ':type {0}: '.format(p['python_name']) + p_type

    output_params = extract_output_parameters(function['parameters'])
    if len(output_params) > 1:
        rst += '\n\n' + (' ' * indent) + ':rtype: tuple (' + ', '.join([p['python_name'] for p in output_params]) + ')\n\n'
        rst += (' ' * (indent + 4)) + 'WHERE\n'
        for p in output_params:
            p_type = p['intrinsic_type']
            if p_type.startswith('enums.'):
                p_type = p_type.replace('enums.', '')
                p_type = ':py:data:`{0}.{1}`'.format(config['module_name'], p_type)
            rst += '\n' + (' ' * (indent + 4)) + '{0} ({1}): '.format(p['python_name'], p_type) + '\n'
            rst += get_documentation_for_node_rst(p, config, indent + 8)
    elif len(output_params) == 1:
        p = output_params[0]
        p_type = p['intrinsic_type']
        if p_type.startswith('enums.'):
            p_type = p_type.replace('enums.', '')
            p_type = ':py:data:`{0}.{1}`'.format(config['module_name'], p_type)
        rst += '\n\n' + (' ' * indent) + ':rtype: ' + p_type + '\n'
        rst += (' ' * indent) + ':return:\n' + get_documentation_for_node_rst(p, config, indent + 8)

    return rst


def get_function_docstring(fname, config, indent=0):
    '''Gets formatted documentation for given function that can be used as a docstring

    Args:
        fname (str): Function name - key in function dictionary
        function (dict): function entry correcsponding to fname in function dictionary

    Returns:
        str: docstring formatted documentation
    '''
    docstring = ''
    function = config['functions'][fname]
    docstring += get_documentation_for_node_docstring(function, config, indent)

    input_params = extract_input_parameters(function['parameters'])
    if len(input_params) > 0:
        docstring += '\n\n' + (' ' * indent) + 'Args:'
    for p in input_params:
        docstring += '\n' + (' ' * (indent + 4)) + '{0} ({1}):'.format(p['python_name'], p['intrinsic_type'])
        docstring += get_documentation_for_node_docstring(p, config, indent + 8)

    output_params = extract_output_parameters(function['parameters'])
    if len(output_params) > 0:
        docstring += '\n\n' + (' ' * indent) + 'Returns:'
        for p in output_params:
            docstring += '\n' + (' ' * (indent + 4)) + '{0} ({1}):'.format(p['python_name'], p['intrinsic_type'])
            docstring += get_documentation_for_node_docstring(p, config, indent + 8)

    return docstring


# From http://code.activestate.com/recipes/579054-generate-sphinx-table/
def as_rest_table(data, full=False, header=True):
    """Create rst formatted table

    >>> from report_table import as_rest_table
    >>> data = [('what', 'how', 'who'),
    ...         ('lorem', 'that is a long value', 3.1415),
    ...         ('ipsum', 89798, 0.2)]
    >>> print as_rest_table(data, full=True)
    +-------+----------------------+--------+
    | what  | how                  | who    |
    +=======+======================+========+
    | lorem | that is a long value | 3.1415 |
    +-------+----------------------+--------+
    | ipsum |                89798 |    0.2 |
    +-------+----------------------+--------+

    >>> print as_rest_table(data)
    =====  ====================  ======
    what   how                   who
    =====  ====================  ======
    lorem  that is a long value  3.1415
    ipsum                 89798     0.2
    =====  ====================  ======

    """
    data = data if data else [['No Data']]
    table = []
    # max size of each column
    sizes = map(max, zip(*[[len(str(elt)) for elt in member]
                           for member in data]))
    if sys.version_info.major >= 3:
        sizes = list(sizes)
    num_elts = len(sizes)

    if full:
        start_of_line = '| '
        vertical_separator = ' | '
        end_of_line = ' |'
        line_marker = '-'
    else:
        start_of_line = ''
        vertical_separator = '  '
        end_of_line = ''
        line_marker = '='

    meta_template = vertical_separator.join(['{{{{{0}:{{{0}}}}}}}'.format(i)
                                             for i in range(num_elts)])
    template = '{0}{1}{2}'.format(start_of_line,
                                  meta_template.format(*sizes),
                                  end_of_line)
    # determine top/bottom borders
    if full:
        to_separator = {ord('|'): '+', ord(' '): '-'}
        if sys.version_info.major < 3:
            to_separator = string.maketrans('| ', '+-')
    else:
        to_separator = {ord('|'): '+'}
        if sys.version_info.major < 3:
            to_separator = string.maketrans('|', '+')
    start_of_line = start_of_line.translate(to_separator)
    vertical_separator = vertical_separator.translate(to_separator)
    end_of_line = end_of_line.translate(to_separator)
    separator = '{0}{1}{2}'.format(start_of_line,
                                   vertical_separator.join([x * line_marker for x in sizes]),
                                   end_of_line)
    # determine header separator
    th_separator_tr = {ord('-'): '='}
    if sys.version_info.major < 3:
        th_separator_tr = string.maketrans('-', '=')
    start_of_line = start_of_line.translate(th_separator_tr)
    line_marker = line_marker.translate(th_separator_tr)
    vertical_separator = vertical_separator.translate(th_separator_tr)
    end_of_line = end_of_line.translate(th_separator_tr)
    th_separator = '{0}{1}{2}'.format(start_of_line,
                                      vertical_separator.join([x * line_marker for x in sizes]),
                                      end_of_line)
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
        if full:
            table.append(separator)
    table.append(template.format(*data[-1]))
    table.append(separator)
    return '\n'.join(table)


# We need this to allow us to dynamically add and remove a folder to the search
# path becaise importlib.import_module() won't work with a module hierarchy in python2
@contextmanager
def add_to_path(p):
    import sys
    old_path = sys.path
    sys.path = sys.path[:]
    sys.path.insert(0, p)
    try:
        yield
    finally:
        sys.path = old_path


def get_intrinsic_type_from_visa_type(visa_type):
    '''Returns the underlying intrinsic (python) type from the visa type'''
    if sys.version_info.major < 3:
        with add_to_path('build/templates'):
            p_types = importlib.import_module('python_types')
    else:
        p_types = importlib.import_module('build.templates.python_types')
    v_type = getattr(p_types, visa_type)

    return type(v_type()).__name__


