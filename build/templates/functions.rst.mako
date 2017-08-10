<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    c_function_prefix = config['c_function_prefix']

    functions = template_parameters['metadata'].functions
    functions = helper.extract_codegen_functions(functions)
    functions = helper.add_all_metadata(functions)
%>\
${helper.get_rst_header_snippet(driver_name + ' Functions', '=')}

.. py:currentmodule:: ${module_name}

% for fname in sorted(functions):
<%
    f = functions[fname]
    input_parameters = helper.extract_input_parameters(f['parameters'])
    output_parameters = helper.extract_output_parameters(f['parameters'])
    enum_input_parameters = helper.extract_enum_parameters(input_parameters)
%>
${helper.get_function_rst(fname, config, indent=0)}

% endfor

