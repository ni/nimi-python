<%page args="f, config, method_template"/>\
<%
    '''Implements Fancy Advanced Sequence'''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        attribute_lookup = {
% for attr_id in config['attributes']:
            "${config['attributes'][attr_id]['python_name']}": {
                'id': ${attr_id},
                'property': self.${config['attributes'][attr_id]['python_name']},
            },
% endfor
        }

        # First we need to get all possible properties we might be setting
        attribute_ids_used = set()
        for s in sequence:
            for key in s:
                attribute_ids_used.add(attribute_lookup[key]['id'])

        # Create the step with the list of attr ids we have
        self._create_advanced_sequence(sequence_name, list(attribute_ids_used), set_as_active_sequence)

        for s in sequence:
            self._create_advanced_sequence_step()
            for key in s:
                attribute_lookup[key]['property'] = s[key]

