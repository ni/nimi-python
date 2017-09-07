<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    c_function_prefix = config['c_function_prefix']

    functions = template_parameters['metadata'].functions
    functions = helper.add_all_metadata(functions)
    functions = helper.extract_codegen_functions(functions)
%>\
.. py:currentmodule:: ${module_name}

% for fname in sorted(functions):
%    if functions[fname]['codegen_method'] == 'public':
${helper.get_function_rst(fname, config, indent=0)}

%    endif
% endfor

