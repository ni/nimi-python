<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    c_function_prefix = config['c_function_prefix']

    functions = template_parameters['metadata'].functions
    functions = helper.filter_codegen_functions(functions)

%>\
${helper.get_rst_header_snippet(module_name + '.Session methods', '=')}

.. py:currentmodule:: ${module_name}.Session

% for fname in sorted(functions):
%    if functions[fname]['codegen_method'] == 'public':
% for method_template in functions[fname]['method_templates']:
<%include file="${'/functions.rst' + method_template['documentation_filename'] + '.rst.mako'}" args="function=functions[fname], config=config, method_template=method_template, indent=0" />\
% endfor

%    endif
% endfor

