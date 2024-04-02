from .codegen_helper import filter_parameters
from .codegen_helper import get_params_snippet
from .documentation_snippets import attr_note_text
from .documentation_snippets import enum_note_text
from .documentation_snippets import func_note_text
from .documentation_snippets import rep_cap_attr_desc
from .documentation_snippets import rep_cap_method_desc
from .helper import get_array_type_for_api_type
from .helper import get_numpy_type_for_api_type
from .parameter_usage_options import ParameterUsageOptions

import pprint
import re
import sys

pp = pprint.PrettyPrinter(indent=4, width=80)


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
    for line in d_lines:
        if len(ret_val) > 0:
            ret_val += '\n'
            if len(line.rstrip()) > 0:
                ret_val += (' ' * indent)
        ret_val += line.rstrip()
    return ret_val


def get_rst_header_snippet(t, header_level='='):
    '''Get rst formatted heading'''
    ret_val = t + '\n'
    ret_val += header_level * len(t)
    return ret_val


def get_rst_picture_reference(tag, url, title, link, indent=0):
    '''Get rst formatted snippet that represents a picture'''
    ret_val = (' ' * indent) + f'.. |{tag}| image:: {url}\n'
    ret_val += (' ' * (indent + 4)) + f':alt: {title}\n'
    ret_val += (' ' * (indent + 4)) + f':target: {link}\n'
    return ret_val


def _get_rst_table_snippet(node, d, config, indent=0, make_link=True):
    '''Returns an rst table snippet if table_header and/or table_body are in the dictionary'''
    if 'table_body' in d:
        table_body = d['table_body']
    else:
        return ''

    if len(table_body) == 0:
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
            contents = _fix_references(node, i, config, make_link)
            header_contents.append(contents)
        table_contents.append(header_contents)

    for t in table_body:
        line_contents = []
        for i in t:
            contents = _fix_references(node, i, config, make_link)
            line_contents.append(contents)
        table_contents.append(line_contents)

    table = as_rest_table(table_contents, header=header)
    return get_indented_docstring_snippet(table, indent)


def get_rst_admonition_snippet(node, admonition, d, config, indent=0):
    '''Returns a rst formatted admonition if the given admonition ('note', 'caution') exists in the dictionary'''
    if admonition in d:
        admonition_content = d[admonition]
        if not isinstance(admonition_content, list):
            admonition_content = [admonition_content]
        a = ''
        for admonition_text in admonition_content:
            a += '\n\n' + (' ' * indent) + f'.. {admonition}:: '
            a += get_indented_docstring_snippet(_fix_references(node, admonition_text, config, make_link=True), indent + 4)
        return a
    else:
        return ''


def add_attribute_rep_cap_tip(attr, config):
    '''Add the appropriate docstring formatted repeated capability tip for an attribute'''
    if 'supported_rep_caps' in attr:
        if 'documentation' not in attr:
            attr['documentation'] = {}

        multi_capability = get_attribute_repeated_caps_with_conjunction(attr)
        single_capability = attr['supported_rep_caps'][0]
        attr['documentation']['tip'] = rep_cap_attr_desc.format(config['module_name'], multi_capability, single_capability, attr['python_name'])


def get_documentation_for_node_rst(node, config, indent=0):
    '''Returns any documentation information formatted for rst

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
    doc += get_rst_admonition_snippet(node, 'caution', nd, config, indent)
    if 'description' in nd:
        doc += '\n\n' + (' ' * indent) + get_indented_docstring_snippet(_fix_references(node, nd['description'], config, make_link=True), indent)

    doc += '\n\n' + (' ' * indent) + _get_rst_table_snippet(node, nd, config, indent)
    doc += get_rst_admonition_snippet(node, 'note', nd, config, indent)
    doc += '\n'
    doc += get_rst_admonition_snippet(node, 'tip', nd, config, indent)
    doc += '\n'

    return doc


def get_docstring_admonition_snippet(node, admonition, d, config, indent=0, extra_newline='\n'):
    '''Returns a docstring formatted admonition if the given admonition ('note', 'caution') exists in the dictionary

    Args:
        admonition (str) - admonition to check and format. I.e. 'note', 'tip', etc.
        d (dict) - documentation note dictionary
        config (dict) - build configuration
        indent (int) - how much each line should be indented
        extra_newline (str) - empty string or newline - needed to keep docstring formatting correct

    Returns:
        str - empty string if no admonition, else formatted string with one or more admonitions
    '''
    if admonition in d:
        admonition_content = d[admonition]
        if not isinstance(admonition_content, list):
            admonition_content = [admonition_content]
        a = ''
        for admonition_text in admonition_content:
            admonition_text = f'{admonition.title()}: {admonition_text}'
            admonition_text = _fix_references(node, admonition_text, config, make_link=False)
            a += '\n' + extra_newline + (' ' * indent) + get_indented_docstring_snippet(admonition_text, indent)
            extra_newline = '\n'
        return a
    else:
        return ''


def get_documentation_for_node_docstring(node, config, indent=0):
    '''Returns any documentation information formatted for docstring

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
        doc += get_docstring_admonition_snippet(node, 'caution', nd, config, indent, extra_newline)
        extra_newline = '\n'

    if 'description' in nd:
        doc += '\n' + extra_newline + (' ' * indent) + get_indented_docstring_snippet(_fix_references(node, nd['description'], config, make_link=False), indent)
        extra_newline = '\n'

    tbl = _get_rst_table_snippet(node, nd, config, indent, make_link=False)
    if len(tbl) > 0:
        doc += '\n' + extra_newline + (' ' * indent) + tbl
        extra_newline = '\n'

    doc += get_docstring_admonition_snippet(node, 'note', nd, config, indent, extra_newline)

    doc += get_docstring_admonition_snippet(node, 'tip', nd, config, indent, extra_newline)

    return doc.strip()


# We need this in the global namespace so we can reference it from the sub() callback
config = None


def find_enum_by_value(enums, value, start_enum=None):
    '''Returns the enum that contains the given value if there is one

    There should only be one so return that individual parameter and not a list
    '''
    enum = []
    values = []
    if start_enum:
        e = enums[start_enum]
        for v in e['values']:
            if v['name'] == value:
                enum.append(e)
                values.append(v)
        if len(enum) == 1:
            return enum[0], values[0]

    for e_name in enums:
        e = enums[e_name]
        for v in e['values']:
            if v['name'] == value:
                enum.append(e)
                values.append(v)

    if len(enum) == 0 or len(enum) > 1:
        return None, None
    return enum[0], values[0]


def _replace_enum_python_name(e_match):
    '''callback function for enum value regex sub command

    Args:
        m (match object): Match object from the attribute substitution command

    Returns:
        str: python name of the enum value, possibly set to sphinx python domain data item link
    '''
    ename = e_match.group(1)
    start_enum = config['start_enum']
    if e_match:
        ename = '{}_VAL_{}'.format(config['module_name'].upper(), ename.replace('\\', ''))
        enum, value = find_enum_by_value(config['enums'], ename, start_enum)
        if enum and enum['codegen_method'] != 'no':
            ename = enum['python_name'] + '.' + value['python_name']

    if config['make_link']:
        return ':py:data:`~{}.{}`'.format(config['module_name'], ename)
    else:
        return f'{ename}'


def find_attribute_by_name(attributes, name):
    '''Returns the attribute with the given name if there is one

    There should only be one so return that individual parameter and not a list
    '''
    attr = [attributes[x] for x in attributes if attributes[x]['name'] == name]
    assert len(attr) <= 1, f'{len(attr)} attributes with name {name}. No more than one is allowed'
    if len(attr) == 0:
        return None
    return attr[0]


def _replace_attribute_python_name(a_match):
    '''callback function for attribute regex sub command

    Args:
        m (match object): Match object from the attribute substitution command

    Returns:
        str: python name of the attribute, possibly set to sphinx python domain data item link
    '''
    aname = "Unknown"
    if a_match:
        aname = a_match.group(1).replace('\\', '')
        attr = find_attribute_by_name(config['attributes'], aname)
        if attr:
            aname = attr['name'].lower()

    if config['make_link']:
        if config['module_name'] == 'nitclk':
            return ':py:attr:`{}.SessionReference.{}`'.format(config['module_name'], aname)
        else:
            return ':py:attr:`{}.Session.{}`'.format(config['module_name'], aname)
    else:
        return f'{aname}'


def _replace_func_python_name(f_match):
    '''callback function for function regex sub command

    Args:
        f_match (match object): Match object from the function substitution command

    Returns:
        str: rst link to function using python name, possibly set to sphinx python domain meth item link
    '''
    fname = "Unknown"
    if f_match:
        fname = f_match.group(1).replace('.', '').replace(',', '').replace('\\', '')
        try:
            if 'method_name_for_documentation' in config['functions'][fname]:
                fname = config['functions'][fname]['method_name_for_documentation']
            else:
                fname = config['functions'][fname]['python_name']
        except KeyError:
            print(f'Warning: "{fname}" not found in function metadata. Typo? Generated code will be funky!')
    else:
        print(f'Unknown function name: {f_match.group(1)}')
        print(config['functions'])

    if config['make_link']:
        if config['module_name'] == 'nitclk':
            return ':py:func:`{}.{}`'.format(config['module_name'], fname)
        else:
            return ':py:meth:`{}.Session.{}`'.format(config['module_name'], fname)
    else:
        return f'{fname}'


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


def _fix_references(node, doc, cfg, make_link=False):
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

    # We have to put config into the global namespace because we need the information in the search
    # callbacks but cannot pass them in via the search command itself
    global config
    config = cfg

    config['make_link'] = make_link
    config['start_enum'] = None
    if 'enum' in node:
        config['start_enum'] = node['enum']

    attr_search_string = '{}_ATTR_([A-Z0-9_]+)'.format(config['module_name'].upper())
    func_search_string = '{}_([A-Za-z0-9_]+)'.format(config['c_function_prefix'].replace('_', ''))
    func_search_string_lower = '{}_([A-Za-z0-9_]+)'.format(config['c_function_prefix'].lower().replace('_', ''))
    enum_search_string = '{}_VAL_([A-Z0-9_]+)'.format(config['module_name'].upper())
    attr_re = re.compile(attr_search_string)
    func_re = re.compile(func_search_string)
    func_lower_re = re.compile(func_search_string_lower)
    enum_re = re.compile(enum_search_string)

    doc = attr_re.sub(_replace_attribute_python_name, doc)
    doc = func_re.sub(_replace_func_python_name, doc)
    doc = func_lower_re.sub(_replace_func_python_name, doc)
    doc = enum_re.sub(_replace_enum_python_name, doc)

    if 'driver_urls' in cfg:
        for url_key in cfg['driver_urls']:
            url_re = re.compile(fr'{url_key}\((.+?)\)')
            config['url_key'] = url_key
            doc = url_re.sub(_replace_urls, doc)

    # Clean up config
    del config['make_link']
    del config['start_enum']

    # Several other standard replacements
    doc = re.sub(r'\bVI_FALSE\b', 'False', doc)
    doc = re.sub(r'\bVI_TRUE\b', 'True', doc)
    doc = re.sub(r'\ban attribute\b', 'a property', doc)
    doc = re.sub(r'\bAn attribute\b', 'A property', doc)
    doc = re.sub(r'\bAn Attribute\b', 'A Property', doc)
    doc = re.sub(r'\battribute\b', 'property', doc)
    doc = re.sub(r'\battributes\b', 'properties', doc)
    doc = re.sub(r'\bAttribute\b', 'Property', doc)
    doc = re.sub(r'\bAttributes\b', 'Properties', doc)
    doc = re.sub(r'\bfunction\b', 'method', doc)
    doc = re.sub(r'\bfunctions\b', 'methods', doc)
    doc = re.sub(r'\bFunction\b', 'Method', doc)
    doc = re.sub(r'\bFunctions\b', 'Methods', doc)

    return doc


def format_type_for_rst_documentation(param, numpy, config):
    if numpy and param['numpy']:
        p_type = param['numpy_type']
    elif param['enum'] is not None:
        p_type = ':py:data:`{}.{}`'.format(config['module_name'], param['enum'])
    else:
        p_type = param['type_in_documentation']

    # If type_in_documentation was set in metadata, we use it as is
    if param['type_in_documentation_was_calculated'] or numpy:
        if param['is_string'] is True and param['enum'] is None:
            p_type = 'str'
        elif param['is_buffer'] is True and numpy is True:
            p_type = 'numpy.array(dtype=numpy.{})'.format(get_numpy_type_for_api_type(param['type'], config))
        elif param['use_list'] is True:
            p_type = 'list of ' + p_type
        elif param['use_array'] is True:
            p_type = 'array.array("{}")'.format(get_array_type_for_api_type(param['type']))

    return p_type


def get_function_rst(function, method_template, numpy, config, indent=0, method_or_function='method'):
    '''Gets formatted documentation for given function or method that can be used in rst documentation

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
    output_parameters = ParameterUsageOptions.API_OUTPUT_PARAMETERS
    if numpy:
        session_declaration = ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION
        output_parameters = ParameterUsageOptions.API_NUMPY_OUTPUT_PARAMETERS

    if function['has_repeated_capability'] is True:
        function['documentation']['tip'] = rep_cap_method_desc.format(config['module_name'], function['repeated_capability_type'], function['python_name'])

    rst = '.. py:{}:: {}{}('.format(method_or_function, function['python_name'], suffix)
    rst += get_params_snippet(function, session_method) + ')'
    indent += 4
    rst += get_documentation_for_node_rst(function, config, indent)

    input_params = filter_parameters(function['parameters'], session_declaration)
    if len(input_params) > 0:
        rst += '\n'
    for p in input_params:
        rst += '\n' + (' ' * indent) + ':param {}:'.format(p['python_name']) + '\n'
        rst += get_documentation_for_node_rst(p, config, indent + 4)

        p_type = format_type_for_rst_documentation(p, numpy, config)
        rst += '\n' + (' ' * indent) + ':type {}: '.format(p['python_name']) + p_type

    output_params = filter_parameters(function['parameters'], output_parameters)
    if len(output_params) > 1:
        rst += '\n\n' + (' ' * indent) + ':rtype: tuple (' + ', '.join([p['python_name'] for p in output_params]) + ')\n\n'
        rst += (' ' * (indent + 4)) + 'WHERE\n'
        for p in output_params:
            p_type = format_type_for_rst_documentation(p, numpy, config)
            rst += '\n' + (' ' * (indent + 4)) + '{} ({}): '.format(p['python_name'], p_type) + '\n'
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
    else:
        p_type = param['type_in_documentation']

    # We assume everything that is a buffer of ViChar is really a string (otherwise
    # it would end up as 'list of int'
    # If type_in_documentation was set in metadata, we use it as is
    if param['type_in_documentation_was_calculated'] or numpy:
        if param['is_string'] is True and param['enum'] is None:
            p_type = 'str'
        elif param['is_buffer'] is True and numpy is True:
            p_type = 'numpy.array(dtype=numpy.{})'.format(get_numpy_type_for_api_type(param['type'], config))
        elif param['use_list'] is True:
            p_type = 'list of ' + p_type
        elif param['use_array'] is True:
            p_type = 'array.array("{}")'.format(get_array_type_for_api_type(param['type']))

    return p_type


def get_function_docstring(function, numpy, config, indent=0):
    '''Gets formatted documentation for given function that can be used as a docstring

    Args:
        function (dict): function dictionary
        config (dict): configuration dictionary (from metadata)
        numpy (boolean): Is the entry we are processing a numpy based method
        indent (int): default 0 - initial indentation

    Returns:
        str: docstring formatted documentation
    '''
    session_declaration = ParameterUsageOptions.SESSION_METHOD_DECLARATION
    output_parameters = ParameterUsageOptions.API_OUTPUT_PARAMETERS
    if numpy:
        session_declaration = ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION
        output_parameters = ParameterUsageOptions.API_NUMPY_OUTPUT_PARAMETERS

    docstring = ''
    if function['has_repeated_capability'] is True:
        function['documentation']['tip'] = rep_cap_method_desc.format(config['module_name'], function['repeated_capability_type'], function['python_name'])

    docstring += get_documentation_for_node_docstring(function, config, indent)

    input_params = filter_parameters(function['parameters'], session_declaration)
    if len(input_params) > 0:
        docstring += '\n\n' + (' ' * indent) + 'Args:'
    for p in input_params:
        docstring += '\n' + (' ' * (indent + 4)) + '{} ({}):'.format(p['python_name'], _format_type_for_docstring(p, numpy, config))
        ds = get_documentation_for_node_docstring(p, config, indent + 8)
        if len(ds) > 0:
            docstring += ' ' + ds
        docstring += '\n'

    output_params = filter_parameters(function['parameters'], output_parameters)
    if len(output_params) > 0:
        docstring += '\n\n' + (' ' * indent) + 'Returns:'
        for p in output_params:
            docstring += '\n' + (' ' * (indent + 4)) + '{} ({}):'.format(p['python_name'], _format_type_for_docstring(p, numpy, config))
            ds = get_documentation_for_node_docstring(p, config, indent + 8)
            if len(ds) > 0:
                docstring += ' ' + ds
            docstring += '\n'

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
    template = f'{start_of_line}{meta_template.format(*sizes)}{end_of_line}'
    # determine top/bottom borders
    to_separator = {ord('|'): '+', ord(' '): '-'}

    start_of_line = start_of_line.translate(to_separator)
    vertical_separator = vertical_separator.translate(to_separator)
    end_of_line = end_of_line.translate(to_separator)
    separator = f'{start_of_line}{vertical_separator.join([x * line_marker for x in sizes])}{end_of_line}'
    # determine header separator
    th_separator_tr = {ord('-'): '='}
    start_of_line = start_of_line.translate(th_separator_tr)
    line_marker = line_marker.translate(th_separator_tr)
    vertical_separator = vertical_separator.translate(th_separator_tr)
    end_of_line = end_of_line.translate(th_separator_tr)
    th_separator = f'{start_of_line}{vertical_separator.join([x * line_marker for x in sizes])}{end_of_line}'
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


def _square_up_table(nd):
    '''_square_up_table

    The function we use to generate rst tables requires the table be a rectangle. I.e. all
    rows must have the same number of cells. This will check 'table_header' and 'table_body'
    to get the longest row and then make sure they are all that length
    '''
    if 'table_header' not in nd and 'table_body' not in nd:
        return  # We don't need to do anything

    # First we get max length
    max_len = 0
    table_header = nd['table_header'] if 'table_header' in nd else None
    table_body = nd['table_body']
    if table_header:
        max_len = len(table_header)
    for line in table_body:
        if len(line) > max_len:
            max_len = len(line)

    # Now make sure all lines have the same number of cells
    if table_header:
        while len(table_header) != max_len:
            table_header.append('')
    for line in table_body:
        while len(line) != max_len:
            line.append('')


def square_up_tables(config):
    '''Go through all documentation and make sure tables rows have consistent lengths'''
    # First we go through the function and parameter documentation
    for f_name in config['functions']:
        f = config['functions'][f_name]
        for p in f['parameters']:
            if 'documentation' not in p:
                continue
            _square_up_table(p['documentation'])

        if 'documentation' not in f:
            continue
        _square_up_table(f['documentation'])

    # Check attribute documentation
    for a_id in config['attributes']:
        a = config['attributes'][a_id]
        if 'documentation' not in a:
            continue
        _square_up_table(a['documentation'])

    # Check enum documentation
    for e_name in config['enums']:
        e = config['enums'][e_name]
        if 'documentation' not in e:
            continue
        _square_up_table(e['documentation'])
        for v in e['values']:
            if 'documentation' not in v:
                continue
            _square_up_table(v['documentation'])


def _need_func_note(nd, config):
    '''Determine if we need the extra note about function names not matching anything in Python'''
    func_re = re.compile('{}_([A-Za-z0-9_]+)'.format(config['c_function_prefix'].replace('_', '')))
    for m in func_re.finditer(nd):
        fname = m.group(1).replace('.', '').replace(',', '').replace('\\', '')
        try:
            config['functions'][fname]['python_name']
        except KeyError:
            return True

    return False


def _need_attr_note(nd, config):
    '''Determine if we need the extra note about attribute names not matching anything in Python'''
    attr_re = re.compile('{}_ATTR_([A-Z0-9_]+)'.format(config['module_name'].upper()))
    for m in attr_re.finditer(nd):
        aname = m.group(1).replace('\\', '')
        attr = find_attribute_by_name(config['attributes'], aname)
        if not attr:
            return True

    return False


def _need_enum_note(nd, config, start_enum=None):
    '''Determine if we need the extra note about enum names not matching anything in Python'''
    enum_re = re.compile('{}_VAL_([A-Z0-9_]+)'.format(config['module_name'].upper()))
    for m in enum_re.finditer(nd):
        ename = '{}_VAL_{}'.format(config['module_name'].upper(), m.group(1).replace('\\', ''))
        enum, _ = find_enum_by_value(config['enums'], ename, start_enum=start_enum)
        if not enum or enum['codegen_method'] == 'no':
            return True
    return False


def _check_documentation(nd, config, start_enum=None):
    '''_check_documentation

    Look through all the different documentation pieces for this node documentation object for
    any references to functions, attributes or enums that will not exist in the Python API for
    whatever reason. If we find something, we will add a note admonition stating that.

    Args:
        nd (dict) - documentation dictionary - expected to follow standard layout we have been using
        config (dict) - configuration information'
        start_enum (book) - possible context - used for finding enums based on the value
    '''
    keys_to_check = ['description', 'tip', 'caution', 'note']  # table_body needs special handling
    need_func_note = False
    need_attr_note = False
    need_enum_note = False
    for k in keys_to_check:
        if k in nd:
            try:
                need_func_note = need_func_note or _need_func_note(nd[k], config)
                need_attr_note = need_attr_note or _need_attr_note(nd[k], config)
                need_enum_note = need_enum_note or _need_enum_note(nd[k], config)
            except TypeError:
                # If we get a type error then we will assume it is an iterable (list)
                for n in nd[k]:
                    need_func_note = need_func_note or _need_func_note(n, config)
                    need_attr_note = need_attr_note or _need_attr_note(n, config)
                    need_enum_note = need_enum_note or _need_enum_note(n, config)

    if 'table_body' in nd:
        tb = nd['table_body']
        for line in tb:
            for cell in line:
                need_func_note = need_func_note or _need_func_note(cell, config)
                need_attr_note = need_attr_note or _need_attr_note(cell, config)
                need_enum_note = need_enum_note or _need_enum_note(cell, config)

    if need_func_note or need_attr_note or need_enum_note:
        if 'note' not in nd:
            nd['note'] = []
        elif not isinstance(nd['note'], list):
            nd['note'] = [nd['note']]

    if need_func_note:
        nd['note'].append(func_note_text)
    if need_attr_note:
        nd['note'].append(attr_note_text)
    if need_enum_note:
        nd['note'].append(enum_note_text)


def add_notes_re_links(config):
    '''_add_notes_re_links

    Go through all documentation looking for names that won't exist in the Python API and
    adding a note about it.
    '''
    # First we go through the function and parameter documentation
    for f_name in config['functions']:
        f = config['functions'][f_name]
        for p in f['parameters']:
            start_enum = None
            if 'documentation' not in p:
                continue
            if 'enum' in p:
                start_enum = p['enum']
            _check_documentation(p['documentation'], config, start_enum)

        if 'documentation' not in f:
            continue
        start_enum = None
        if 'enum' in f:
            start_enum = f['enum']
        _check_documentation(f['documentation'], config, start_enum)

    # Check attribute documentation
    for a_id in config['attributes']:
        a = config['attributes'][a_id]
        if 'documentation' not in a:
            continue
        start_enum = None
        if 'enum' in a:
            start_enum = a['enum']
        _check_documentation(a['documentation'], config, start_enum)

    # Check enum documentation
    for e_name in config['enums']:
        e = config['enums'][e_name]
        if 'documentation' not in e:
            continue
        _check_documentation(e['documentation'], config)
        for v in e['values']:
            if 'documentation' not in v:
                continue
            _check_documentation(v['documentation'], config)


def get_attribute_repeated_caps(attr):
    '''Creates a comma-separated string representing the attribute's repeated capabilities. Returns 'None' if there are no repeated capabilities'''
    if 'supported_rep_caps' in attr and len(attr['supported_rep_caps']) > 0:
        supported_rep_caps = attr['supported_rep_caps']
        caps = ', '.join(supported_rep_caps)
    else:
        caps = 'None'
    return caps


def get_attribute_repeated_caps_with_conjunction(attr):
    '''Creates a comma-separated string, with terminating 'and', representing the attribute's repeated capabilities. Returns 'None' if there are no repeated capabilities'''
    if 'supported_rep_caps' in attr and len(attr['supported_rep_caps']) > 0:
        supported_rep_caps = attr['supported_rep_caps']
        num_items = len(supported_rep_caps)
        if num_items > 1:
            caps = ', '.join(supported_rep_caps[:-1]) + ' or ' + supported_rep_caps[num_items - 1]
        else:
            caps = supported_rep_caps[0]
    else:
        caps = 'None'
    return caps


def module_supports_repeated_caps(config):
    if 'repeated_capabilities' in config:
        return len(config['repeated_capabilities']) > 0
    return False

