<%page args="function, config, method_template, indent"/>\
<%
    import build.helper as helper
    sparameters_param = [p for p in function['parameters'] if p['python_name'] == 'sparameters'][0]
    function_doc = helper.get_documentation_for_node_rst(function, config, indent).strip('\n')
    return_doc = helper.get_documentation_for_node_rst(sparameters_param, config, indent + 8).strip('\n')
%>\
    .. py:method:: ${function['python_name']}()

${function_doc}

        :rtype: numpy.array(dtype=numpy.complex128)
        :return:

${return_doc}