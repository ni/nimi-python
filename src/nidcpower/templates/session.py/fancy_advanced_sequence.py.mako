<%page args="f, config, method_template"/>\
<%
    '''Implements Fancy Advanced Sequence'''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']

    # precalculate some lists
    attrs = helper.filter_codegen_attributes(config['attributes'])
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        from enum import Enum

        _ATTRIBUTE_LOOKUP = {
% for attr_id in attrs:
            "${config['attributes'][attr_id]['python_name']}": {
                'id': ${attr_id},
                'set_function': self._set_attribute_${helper.camelcase_to_snakecase(config['attributes'][attr_id]['type'])},
            },
% endfor
        }

        # First we need to get all possible properties we might be setting
        attribute_ids_used = set()
        for s in sequence:
            for key in s:
                attribute_ids_used.add(_ATTRIBUTE_LOOKUP[key]['id'])

        # Create the sequence with the list of attr ids we have
        self._create_advanced_sequence(sequence_name, list(attribute_ids_used), set_as_active_sequence)

        # Create and configure the steps
        for s in sequence:
            self._create_advanced_sequence_step()
            for key, value in s.items():
                value_to_use = value.value if isinstance(value, Enum) else value
                _ATTRIBUTE_LOOKUP[key]['set_function'](_ATTRIBUTE_LOOKUP[key]['id'], value_to_use)

