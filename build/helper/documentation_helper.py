from .codegen_helper import filter_parameters
from .codegen_helper import get_params_snippet
from .documentation_snippets import attr_note_text
from .documentation_snippets import enum_note_text
from .documentation_snippets import func_note_text
from .documentation_snippets import rep_cap_attr_desc_docstring_r
from .documentation_snippets import rep_cap_attr_desc_docstring_rw
from .documentation_snippets import rep_cap_attr_desc_docstring_w
from .documentation_snippets import rep_cap_attr_desc_rst_r
from .documentation_snippets import rep_cap_attr_desc_rst_rw
from .documentation_snippets import rep_cap_attr_desc_rst_w
from .documentation_snippets import rep_cap_method_desc_docstring
from .documentation_snippets import rep_cap_method_desc_rst
from .helper import get_array_type_for_api_type
from .helper import get_numpy_type_for_api_type
from .parameter_usage_options import ParameterUsageOptions

import pprint
import re
import string
import sys

pp = pprint.PrettyPrinter(indent=4, width=80)


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


def get_rst_picture_reference(tag, url, title, link, indent=0):
    '''Get rst formatted snippet that represents a picture'''
    ret_val = (' ' * indent) + '.. |{0}| image:: {1}\n'.format(tag, url)
    ret_val += (' ' * (indent + 4)) + ':alt: {0}\n'.format(title)
    ret_val += (' ' * (indent + 4)) + ':target: {0}\n'.format(link)
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
            a += '\n\n' + (' ' * indent) + '.. {0}:: '.format(admonition)
            a += get_indented_docstring_snippet(_fix_references(node, admonition_text, config, make_link=True), indent + 4)
        return a
    else:
        return ''


def add_attribute_rep_cap_tip_rst(attr, config):
    '''Add the appropriate (r/w/rw/none) rst formatted tip for an attribute'''
    if 'repeated_capability_type' in attr:
        if attr['access'] == 'read only':
            tip = rep_cap_attr_desc_rst_r
        elif attr['access'] == 'write only':
            tip = rep_cap_attr_desc_rst_w
        else:
            assert attr['access'] == 'read-write'
            tip = rep_cap_attr_desc_rst_rw

        if 'documentation' not in attr:
            attr['documentation'] = {}

        attr['documentation']['tip'] = tip.format(config['module_name'], attr['repeated_capability_type'], attr["name"].lower())


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
            admonition_text = '{0}: {1}'.format(admonition.title(), admonition_text)
            admonition_text = _fix_references(node, admonition_text, config, make_link=False)
            a += '\n' + extra_newline + (' ' * indent) + get_indented_docstring_snippet(admonition_text, indent)
            extra_newline = '\n'
        return a
    else:
        return ''


def add_attribute_rep_cap_tip_docstring(attr, config):
    '''Add the appropriate (r/w/rw/none) docstring formatted tip for an attribute'''
    if 'repeated_capability_type' in attr:
        if attr['access'] == 'read only':
            tip = rep_cap_attr_desc_docstring_r
        elif attr['access'] == 'write only':
            tip = rep_cap_attr_desc_docstring_w
        else:
            assert attr['access'] == 'read-write'
            tip = rep_cap_attr_desc_docstring_rw

        if 'documentation' not in attr:
            attr['documentation'] = {}

        attr['documentation']['tip'] = tip.format(config['module_name'], attr['repeated_capability_type'], attr["name"].lower())


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
        ename = '{0}_VAL_{1}'.format(config['module_name'].upper(), ename.replace('\\', ''))
        enum, value = find_enum_by_value(config['enums'], ename, start_enum)
        if enum and enum['codegen_method'] != 'no':
            ename = enum['python_name'] + '.' + value['python_name']

    if config['make_link']:
        return ':py:data:`~{0}.{1}`'.format(config['module_name'], ename)
    else:
        return '{0}'.format(ename)


def find_attribute_by_name(attributes, name):
    '''Returns the attribute with the given name if there is one

    There should only be one so return that individual parameter and not a list
    '''
    attr = [attributes[x] for x in attributes if attributes[x]['name'] == name]
    assert len(attr) <= 1, '{0} attributes with name {1}. No more than one is allowed'.format(len(attr), name)
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
            return ':py:attr:`{0}.SessionReference.{1}`'.format(config['module_name'], aname)
        else:
            return ':py:attr:`{0}.Session.{1}`'.format(config['module_name'], aname)
    else:
        return '{0}'.format(aname)


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
            print('Warning: "{0}" not found in function metadata. Typo? Generated code will be funky!'.format(fname))
    else:
        print('Unknown function name: {0}'.format(f_match.group(1)))
        print(config['functions'])

    if config['make_link']:
        if config['module_name'] == 'nitclk':
            return ':py:func:`{0}.{1}`'.format(config['module_name'], fname)
        else:
            return ':py:meth:`{0}.Session.{1}`'.format(config['module_name'], fname)
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

    attr_search_string = '{0}_ATTR_([A-Z0-9_]+)'.format(config['module_name'].upper())
    func_search_string = '{0}_([A-Za-z0-9_]+)'.format(config['c_function_prefix'].replace('_', ''))
    func_search_string_lower = '{0}_([A-Za-z0-9_]+)'.format(config['c_function_prefix'].lower().replace('_', ''))
    enum_search_string = '{0}_VAL_([A-Z0-9_]+)'.format(config['module_name'].upper())
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
            url_re = re.compile(r'{0}\((.+?)\)'.format(url_key))
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
        p_type = ':py:data:`{0}.{1}`'.format(config['module_name'], param['enum'])
    else:
        p_type = param['type_in_documentation']

    if param['is_string'] is True:
        p_type = 'str'
    elif param['is_buffer'] is True and numpy is True:
        p_type = 'numpy.array(dtype=numpy.{0})'.format(get_numpy_type_for_api_type(param['type'], config))
    elif param['use_list'] is True:
        p_type = 'list of ' + p_type
    elif param['use_array'] is True:
        p_type = 'array.array("{0}")'.format(get_array_type_for_api_type(param['type']))

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
    output_parameters = ParameterUsageOptions.OUTPUT_PARAMETERS_FOR_DOCS
    if numpy:
        session_declaration = ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION

    if function['has_repeated_capability'] is True:
        function['documentation']['tip'] = rep_cap_method_desc_rst.format(config['module_name'], function['repeated_capability_type'], function['python_name'], get_params_snippet(function, session_method))

    rst = '.. py:{0}:: {1}{2}('.format(method_or_function, function['python_name'], suffix)
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
    else:
        p_type = param['type_in_documentation']

    # We assume everything that is a buffer of ViChar is really a string (otherwise
    # it would end up as 'list of int'
    if param['is_string'] is True:
        p_type = 'str'
    elif param['is_buffer'] is True and numpy is True:
        p_type = 'numpy.array(dtype=numpy.{0})'.format(get_numpy_type_for_api_type(param['type'], config))
    elif param['use_list'] is True:
        p_type = 'list of ' + p_type
    elif param['use_array'] is True:
        p_type = 'array.array("{0}")'.format(get_array_type_for_api_type(param['type']))

    return p_type


def get_function_docstring(function, numpy, config, indent=0):
    '''Gets formatted documentation for given function that can be used as a docstring

    Args:
        function (dict): function dictionary
        config (dict): configuration dictoionary (from metadata)
        numpy (boolean): Is the entry we are processing a numpy based method
        indent (int): default 0 - initial indentation

    Returns:
        str: docstring formatted documentation
    '''
    session_method = ParameterUsageOptions.DOCUMENTATION_SESSION_METHOD
    session_declaration = ParameterUsageOptions.SESSION_METHOD_DECLARATION
    output_parameters = ParameterUsageOptions.OUTPUT_PARAMETERS_FOR_DOCS
    if numpy:
        session_declaration = ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION

    docstring = ''
    if function['has_repeated_capability'] is True:
        function['documentation']['tip'] = rep_cap_method_desc_docstring.format(config['module_name'], function['repeated_capability_type'], function['python_name'], get_params_snippet(function, session_method))

    docstring += get_documentation_for_node_docstring(function, config, indent)

    input_params = filter_parameters(function, session_declaration)
    if len(input_params) > 0:
        docstring += '\n\n' + (' ' * indent) + 'Args:'
    for p in input_params:
        docstring += '\n' + (' ' * (indent + 4)) + '{0} ({1}):'.format(p['python_name'], _format_type_for_docstring(p, numpy, config))
        ds = get_documentation_for_node_docstring(p, config, indent + 8)
        if len(ds) > 0:
            docstring += ' ' + ds
        docstring += '\n'

    output_params = filter_parameters(function, output_parameters)
    if len(output_params) > 0:
        docstring += '\n\n' + (' ' * indent) + 'Returns:'
        for p in output_params:
            docstring += '\n' + (' ' * (indent + 4)) + '{0} ({1}):'.format(p['python_name'], _format_type_for_docstring(p, numpy, config))
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
    func_re = re.compile('{0}_([A-Za-z0-9_]+)'.format(config['c_function_prefix'].replace('_', '')))
    for m in func_re.finditer(nd):
        fname = m.group(1).replace('.', '').replace(',', '').replace('\\', '')
        try:
            config['functions'][fname]['python_name']
        except KeyError:
            return True

    return False


def _need_attr_note(nd, config):
    '''Determine if we need the extra note about attribute names not matching anything in Python'''
    attr_re = re.compile('{0}_ATTR_([A-Z0-9_]+)'.format(config['module_name'].upper()))
    for m in attr_re.finditer(nd):
        aname = m.group(1).replace('\\', '')
        attr = find_attribute_by_name(config['attributes'], aname)
        if not attr:
            return True

    return False


def _need_enum_note(nd, config, start_enum=None):
    '''Determine if we need the extra note about enum names not matching anything in Python'''
    enum_re = re.compile('{0}_VAL_([A-Z0-9_]+)'.format(config['module_name'].upper()))
    for m in enum_re.finditer(nd):
        ename = '{0}_VAL_{1}'.format(config['module_name'].upper(), m.group(1).replace('\\', ''))
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
                    'type_in_documentation': 'int',
                    'ctypes_variable_name': 'vi_ctype',
                    'ctypes_type': 'ViSession',
                    'ctypes_type_library_call': 'ViSession',
                    'size': {
                        'mechanism': 'fixed',
                        'value': 1
                    },
                    'is_buffer': False,
                    'is_string': False,
                    'use_list': False,
                    'use_array': False,
                    'python_name_with_default': 'vi',
                    'python_name_with_doc_default': 'vi',
                    'is_repeated_capability': False,
                    'is_session_handle': True,
                    'library_method_call_snippet': 'self._vi',
                    'use_in_python_api': True,
                },
                {
                    'direction': 'in',
                    'enum': 'Turtle',
                    'name': 'turtleType',
                    'type': 'ViInt32',
                    'documentation': {
                        'description': '''Specifies the type of Turtle type
wanted to choose.''',
                        'note': 'You wont be able to import NIFAKE_VAL_RAPHAEL',
                        'table_body': [
                            ['NIFAKE_VAL_LEONARDO (default)', '0', 'LEONARDO'],
                            ['NIFAKE_VAL_DONATELLO', '1', 'DONATELLO'],
                            ['NIFAKE_VAL_RAPHAEL', '2', 'RAPHAEL'],
                            ['NIFAKE_VAL_MICHELANGELO', '3', 'MICHELANGELO']
                        ]
                    },
                    'python_name': 'turtle_type',
                    'python_type': 'Turtle',
                    'type_in_documentation': 'Turtle',
                    'ctypes_variable_name': 'turtle_type_ctype',
                    'ctypes_type': 'ViInt32',
                    'ctypes_type_library_call': 'ViInt32',
                    'size': {
                        'mechanism': 'fixed',
                        'value': 1
                    },
                    'is_buffer': False,
                    'is_string': False,
                    'use_list': False,
                    'use_array': False,
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
                    'type_in_documentation': 'float',
                    'ctypes_variable_name': 'turtleId_ctype',
                    'ctypes_type': 'ViReal64',
                    'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
                    'size': {
                        'mechanism': 'fixed',
                        'value': 1
                    },
                    'is_buffer': False,
                    'is_string': False,
                    'use_list': False,
                    'use_array': False,
                    'python_name_with_default': 'turtleId',
                    'python_name_with_doc_default': 'turtleId',
                    'is_repeated_capability': False,
                    'is_session_handle': False,
                    'library_method_call_snippet': 'ctypes.pointer(turtleId_ctype)',
                    'use_in_python_api': True,
                }
            ],
            'documentation': {
                'description': 'Returns the **ID** of selected Turtle Type. See `NIFAKE help <REPLACE_DRIVER_SPECIFIC_URL_1(fake_functional_overview)>`__',
                'note': [
                    'The NIFAKE_VAL_RAPHAEL Turtles dont have an ID.',
                    'DO NOT call niFake_FetchWaveform after calling this function.',
                    'NIFAKE_ATTR_READ_WRITE_BOOL will have an incorrect value after this calling this function',
                ]
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
                    'is_string': False,
                    'use_list': False,
                    'use_array': False,
                    'is_repeated_capability': False,
                    'is_session_handle': True,
                    'library_method_call_snippet': 'vi_ctype',
                    'name': 'vi',
                    'numpy': False,
                    'python_name': 'vi',
                    'python_name_with_default': 'vi',
                    'python_name_with_doc_default': 'vi',
                    'python_type': 'int',
                    'type_in_documentation': 'int',
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
                    'is_string': False,
                    'use_list': False,
                    'use_array': False,
                    'is_repeated_capability': False,
                    'is_session_handle': False,
                    'library_method_call_snippet': 'number_of_samples_ctype',
                    'name': 'numberOfSamples',
                    'numpy': False,
                    'python_name': 'number_of_samples',
                    'python_name_with_default': 'number_of_samples',
                    'python_name_with_doc_default': 'number_of_samples',
                    'python_type': 'int',
                    'type_in_documentation': 'int',
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
                    'is_string': False,
                    'use_list': False,
                    'use_array': True,
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
                    'type_in_documentation': 'float',
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
                    'is_string': False,
                    'use_list': False,
                    'use_array': False,
                    'is_repeated_capability': False,
                    'is_session_handle': False,
                    'library_method_call_snippet': 'ctypes.pointer(actual_number_of_samples_ctype)',
                    'name': 'actualNumberOfSamples',
                    'numpy': False,
                    'python_name': 'actual_number_of_samples',
                    'python_name_with_default': 'actual_number_of_samples',
                    'python_name_with_doc_default': 'actual_number_of_samples',
                    'python_type': 'int',
                    'type_in_documentation': 'int',
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
    'driver_urls': {
        'REPLACE_DRIVER_SPECIFIC_URL_1': 'http://zone.ni.com/reference/en-XX/help/370384T-01/fake/{0}/',
    },
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
    'attributes': {
        1000000: {
            'access': 'read-write',
            'channel_based': 'False',
            'enum': None,
            'lv_property': 'Fake attributes:Read Write Bool',
            'name': 'READ_WRITE_BOOL',
            'resettable': 'No',
            'type': 'ViBoolean',
            'documentation': {
                'description': 'An attribute of type bool with read/write access.',
            },
        },
    },
    'enums': {
        'Turtle': {
            'codegen_method': 'public',
            'python_name': 'Turtle',
            'values': [
                {
                    'name': 'NIFAKE_VAL_LEONARDO',
                    'python_name': 'LEONARDO',
                    'value': 0,
                    'documentation': {
                        'description': 'Wields two katanas.',
                    }
                },
                {
                    'name': 'NIFAKE_VAL_DONATELLO',
                    'python_name': 'DONATELLO',
                    'value': 1,
                    'documentation': {
                        'description': 'Uses a bo staff.',
                    }
                },
                {
                    'name': 'NIFAKE_VAL_RAPHAEL',
                    'python_name': 'RAPHAEL',
                    'value': 2,
                    'documentation': {
                        'description': 'Has a pair of sai.',
                    }
                },
                {
                    'name': 'NIFAKE_VAL_MICHELANGELO',
                    'python_name': 'MICHELANGELO',
                    'value': 3,
                    'documentation': {
                        'description': 'Owns nunchucks.',
                    }
                },
            ],
        },
    },
}


def test_get_function_rst_default():
    function = config['functions']['GetTurtleID']
    method_template = function['method_templates'][0]
    actual_function_rst = get_function_rst(function, method_template=method_template, numpy=False, config=config, indent=0)
    expected_fuction_rst = '''.. py:method:: get_turtle_id(turtle_type)

    Returns the **ID** of selected Turtle Type. See `NIFAKE help <http://zone.ni.com/reference/en-XX/help/370384T-01/fake/fake_functional_overview/>`__

    .. note:: The :py:data:`~nifake.Turtle.RAPHAEL` Turtles dont have an ID.

    .. note:: DO NOT call :py:meth:`nifake.Session.fetch_waveform` after calling this method.

    .. note:: :py:attr:`nifake.Session.read_write_bool` will have an incorrect value after this calling this method

    :param turtle_type:

    Specifies the type of Turtle type
    wanted to choose.

    +----------------------------------------------+---+--------------+
    | :py:data:`~nifake.Turtle.LEONARDO` (default) | 0 | LEONARDO     |
    +----------------------------------------------+---+--------------+
    | :py:data:`~nifake.Turtle.DONATELLO`          | 1 | DONATELLO    |
    +----------------------------------------------+---+--------------+
    | :py:data:`~nifake.Turtle.RAPHAEL`            | 2 | RAPHAEL      |
    +----------------------------------------------+---+--------------+
    | :py:data:`~nifake.Turtle.MICHELANGELO`       | 3 | MICHELANGELO |
    +----------------------------------------------+---+--------------+

    .. note:: You wont be able to import :py:data:`~nifake.Turtle.RAPHAEL`

    :type turtle_type: :py:data:`nifake.Turtle`

    :rtype: float
    :return:

        Returns the **ID** of selected turtle.
'''
    assert_rst_strings_are_equal(expected_fuction_rst, actual_function_rst)


def test_get_function_rst_numpy():
    function = config['functions']['FetchWaveform']
    method_template = function['method_templates'][0]
    actual_function_rst = get_function_rst(function, method_template=method_template, numpy=True, config=config, indent=0)
    expected_fuction_rst = '''.. py:method:: fetch_waveform(number_of_samples)

    Returns waveform data.

    :param number_of_samples:

        Number of samples to return

    :type number_of_samples: int
    :param waveform_data:

        Samples fetched from the device. Array should be numberOfSamples big.

    :type waveform_data: numpy.array(dtype=numpy.float64)

    :rtype: tuple (waveform_data, actual_number_of_samples)

        WHERE

        waveform_data (numpy.array(dtype=numpy.float64)):

            Samples fetched from the device. Array should be numberOfSamples big.

        actual_number_of_samples (int):

            Number of samples actually fetched.
'''
    assert_rst_strings_are_equal(expected_fuction_rst, actual_function_rst)


def test_get_function_docstring_default():
    function = config['functions']['GetTurtleID']
    actual_function_docstring = get_function_docstring(function, numpy=False, config=config, indent=0)
    expected_function_docstring = '''Returns the **ID** of selected Turtle Type. See `NIFAKE help <fake_functional_overview>`__

Note: The Turtle.RAPHAEL Turtles dont have an ID.

Note: DO NOT call fetch_waveform after calling this method.

Note: read_write_bool will have an incorrect value after this calling this method

Args:
    turtle_type (Turtle): Specifies the type of Turtle type
        wanted to choose.

        +---------------------------+---+--------------+
        | Turtle.LEONARDO (default) | 0 | LEONARDO     |
        +---------------------------+---+--------------+
        | Turtle.DONATELLO          | 1 | DONATELLO    |
        +---------------------------+---+--------------+
        | Turtle.RAPHAEL            | 2 | RAPHAEL      |
        +---------------------------+---+--------------+
        | Turtle.MICHELANGELO       | 3 | MICHELANGELO |
        +---------------------------+---+--------------+

        Note: You wont be able to import Turtle.RAPHAEL

Returns:
    turtle_id (float): Returns the **ID** of selected turtle.''' # noqa
    assert_rst_strings_are_equal(expected_function_docstring, actual_function_docstring)


def test_get_function_docstring_numpy():
    function = config['functions']['FetchWaveform']
    actual_function_docstring = get_function_docstring(function, numpy=True, config=config, indent=0)
    expected_fuction_docstring = '''Returns waveform data.

    Args:
        number_of_samples (int): Number of samples to return

        waveform_data (numpy.array(dtype=numpy.float64)): Samples fetched from the device. Array should be numberOfSamples big.

    Returns:
        waveform_data (numpy.array(dtype=numpy.float64)): Samples fetched from the device. Array should be numberOfSamples big.

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


def test_get_rst_picture_reference():
    actual_pic_ref = get_rst_picture_reference('test1', 'test2', 'test3', 'test4')
    expected_pic_ref = """
    .. |test1| image:: test2
        :alt: test3
        :target: test4
    """
    assert_rst_strings_are_equal(expected_pic_ref, actual_pic_ref)


def test_square_up_tables():
    local_config = config_for_testing.copy()
    functions = {
        'MakeAFoo': {
            'codegen_method': 'public',
            'returns': 'ViStatus',
            'method_templates': [{'session_filename': '/cool_template', 'documentation_filename': '/cool_template', 'method_python_name_suffix': '', }, ],
            'parameters': [
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'vi',
                    'type': 'ViSession',
                    'documentation': {
                        'description': 'Identifies a particular instrument session.',
                    },
                },
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'channelName',
                    'type': 'ViString',
                    'documentation': {
                        'description': 'The channel to call this on.',
                    },
                },
            ],
            'documentation': {
                'description': 'Performs a foo, and performs it well.',
                'table_header': ['Just one'],
                'table_body': [['Just', 'two'], ['this', 'has', 'three']],
            },
        },
    }
    local_config['functions'] = functions
    local_config['attributes'] = {}
    local_config['enums'] = {}

    square_up_tables(local_config)
    assert len(local_config['functions']['MakeAFoo']['documentation']['table_header']) == 3
    for line in local_config['functions']['MakeAFoo']['documentation']['table_body']:
        assert(len(line)) == 3


config_for_testing = {
    'session_handle_parameter_name': 'vi',
    'module_name': 'nifake',
    'functions': {},
    'attributes': {},
    'modules': {
        'metadata.enums_addon': {}
    },
    'custom_types': [],
}


def test_add_notes_re_links():
    local_config = config_for_testing.copy()
    local_config['c_function_prefix'] = 'niFake'
    functions = {
        'MakeAFoo': {
            'codegen_method': 'public',
            'returns': 'ViStatus',
            'method_templates': [{'session_filename': '/cool_template', 'documentation_filename': '/cool_template', 'method_python_name_suffix': '', }, ],
            'parameters': [
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'vi',
                    'type': 'ViSession',
                    'documentation': {
                        'description': 'Identifies a particular instrument session for niFake_MakeAFoo using NIFAKE_ATTR_READ_WRITE_BOOL. You should use NIFAKE_VAL_BLUE',
                    },
                },
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'channelName',
                    'type': 'ViString',
                    'documentation': {
                        'description': 'The channel to call this on. Similar to niFake_TakeAFoo using NIFAKE_ATTR_NOT_HERE. Use NIFAKE_VAL_PURPLE',
                    },
                },
            ],
            'documentation': {
                'description': 'Performs a foo, and performs it well.',
            },
            'python_name': 'make_a_foo',
        },
    }
    attributes = {
        1000000: {
            'access': 'read-write',
            'channel_based': 'False',
            'enum': None,
            'lv_property': 'Fake attributes:Read Write Bool',
            'name': 'READ_WRITE_BOOL',
            'resettable': 'No',
            'type': 'ViBoolean',
            'documentation': {
                'description': 'An attribute of type bool with read/write access.',
            },
        },
    }
    enums = {
        'Color': {
            'values': [
                {
                    'name': 'NIFAKE_VAL_RED',
                    'value': 1,
                    'documentation': {
                        'description': 'Like blood.',
                    }
                },
                {
                    'name': 'NIFAKE_VAL_BLUE',
                    'value': 2,
                    'documentation': {
                        'description': 'Like the sky.',
                    }
                },
                {
                    'name': 'NIFAKE_VAL_YELLOW',
                    'value': 2,
                    'documentation': {
                        'description': 'Like a banana.',
                    }
                },
                {
                    'name': 'NIFAKE_VAL_BLACK',
                    'value': 2,
                    'documentation': {
                        'description': 'Like this developer\'s conscience.',
                    }
                },
            ],
            'codegen_method': 'public',
        },
    }
    local_config['functions'] = functions
    local_config['attributes'] = attributes
    local_config['enums'] = enums

    add_notes_re_links(local_config)

    assert 'note' not in local_config['functions']['MakeAFoo']['parameters'][0]['documentation']
    assert func_note_text in local_config['functions']['MakeAFoo']['parameters'][1]['documentation']['note']
    assert attr_note_text in local_config['functions']['MakeAFoo']['parameters'][1]['documentation']['note']
    assert enum_note_text in local_config['functions']['MakeAFoo']['parameters'][1]['documentation']['note']

