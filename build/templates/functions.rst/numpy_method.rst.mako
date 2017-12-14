<%page args="function, config, method_template, indent"/>\
<%
    '''Renders a Session method corresponding to the passed-in function metadata.'''

    import build.helper as helper

    parameters = function['parameters']

    if function['has_repeated_capability'] is True:
        function['documentation']['tip'] = helper.rep_cap_method_desc_rst.format(config['module_name'], function['python_name'], helper.get_params_snippet(function, helper.ParameterUsageOptions.DOCUMENTATION_SESSION_METHOD))

    rst = '.. function:: ' + function['python_name'] + method_template['suffix'] + '('
    rst += helper.get_params_snippet(function, helper.ParameterUsageOptions.DOCUMENTATION_SESSION_METHOD) + ')'
    indent += 4
    rst += helper.get_documentation_for_node_rst(function, config, indent)

    input_params = helper.filter_parameters(function, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)
    if len(input_params) > 0:
        rst += '\n'
    for p in input_params:
        rst += '\n' + (' ' * indent) + ':param {0}:'.format(p['python_name']) + '\n'
        rst += helper.get_documentation_for_node_rst(p, config, indent + 4)

        p_type = helper.format_type_for_rst_documentation(p, config)
        rst += '\n' + (' ' * indent) + ':type {0}: '.format(p['python_name']) + p_type

    output_params = helper.filter_parameters(function, helper.ParameterUsageOptions.OUTPUT_PARAMETERS)
    if len(output_params) > 1:
        rst += '\n\n' + (' ' * indent) + ':rtype: tuple (' + ', '.join([p['python_name'] for p in output_params]) + ')\n\n'
        rst += (' ' * (indent + 4)) + 'WHERE\n'
        for p in output_params:
            p_type = helper.format_type_for_rst_documentation(p, config)
            rst += '\n' + (' ' * (indent + 4)) + '{0} ({1}): '.format(p['python_name'], p_type) + '\n'
            rst += helper.get_documentation_for_node_rst(p, config, indent + 8)
    elif len(output_params) == 1:
        p = output_params[0]
        p_type = helper.format_type_for_rst_documentation(p, config)
        rst += '\n\n' + (' ' * indent) + ':rtype: ' + p_type + '\n'
        rst += (' ' * indent) + ':return:\n' + helper.get_documentation_for_node_rst(p, config, indent + 8)

%>\
${rst}
