<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    enums = config['enums']
%>\
${helper.get_rst_header_snippet('Enums', '=')}

Enums used in ${driver_name}

.. py:currentmodule:: ${module_name}

% for enum_name in sorted(enums):


.. py:data:: ${enum_name}
    % for enum_value in enums[enum_name]['values']:

    .. py:attribute:: ${enum_value['name']}

${helper.get_documentation_for_node_rst(enum_value, config, indent=8)}
    % endfor
% endfor
