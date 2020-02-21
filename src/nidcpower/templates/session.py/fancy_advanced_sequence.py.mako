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
        # First we need to get all possible properties we might be setting. The way the NI-DCPower C API is designed,
        # we need to know this upfront in order to call `niDCPower_CreateAdvancedSequence`. In order to find the attribute
        # ID of each property, we look at the member Attribute objects of Session.
        attribute_ids_used = set()
        for step in sequence:
            for key in step:
                if key not in Session.__base__.__dict__:
                    raise KeyError('{0} is not an property on the nidcpower.Session'.format(key))
                if not isinstance(Session.__base__.__dict__[key], _attributes.Attribute) and not isinstance(Session.__base__.__dict__[key], _attributes.AttributeEnum):
                    raise TypeError('{0} is not an attribute type: {1}'.format(key, type(Session.__base__.__dict__[key])))
                attribute_ids_used.add(Session.__base__.__dict__[key]._attribute_id)

        # Create the sequence with the list of attr ids we have
        self._create_advanced_sequence(sequence_name, list(attribute_ids_used), set_as_active_sequence)

