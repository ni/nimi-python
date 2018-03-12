<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    c_function_prefix = config['c_function_prefix']

    functions = template_parameters['metadata'].functions
    functions = helper.filter_codegen_functions(functions)

    doc_list = {}
    for fname in sorted(functions):
        if functions[fname]['codegen_method'] == 'public' or functions[fname]['codegen_method'] == 'python-only':
            for method_template in functions[fname]['method_templates']:
                name =  functions[fname]['python_name'] + method_template['method_python_name_suffix']
                doc_list[name] = { 'filename': method_template['documentation_filename'], 'method_template': method_template, 'function': functions[fname], }

%>\
${helper.get_rst_header_snippet(module_name + '.Session methods', '=')}

.. py:currentmodule:: ${module_name}.Session

% for item in sorted(doc_list):
<%
function_item = doc_list[item]
%>\
<%include file="${'/functions.rst' + function_item['filename'] + '.rst.mako'}" args="function=function_item['function'], config=config, method_template=function_item['method_template'], indent=0" />\

% endfor

