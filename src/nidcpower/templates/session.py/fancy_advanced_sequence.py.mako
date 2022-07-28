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
        # The way the NI-DCPower C API is designed, we need to know all the attribute ID's upfront in order to call
        # `niDCPower_CreateAdvancedSequence`. In order to find the attribute ID of each property, we look at the
        # member Attribute objects of Session. We use a set since we don't have to worry about is it already there.
        attribute_ids_used = set()
        for prop in property_names:
            if prop not in Session.__base__.__dict__:
                raise KeyError('{0} is not an property on the nidcpower.Session'.format(prop))
            if not isinstance(Session.__base__.__dict__[prop], _attributes.Attribute):
                raise TypeError('{0} is not a valid property: {1}'.format(prop, type(Session.__base__.__dict__[prop])))
            attribute_ids_used.add(Session.__base__.__dict__[prop]._attribute_id)

        self._create_advanced_sequence_with_channels(sequence_name, list(attribute_ids_used), set_as_active_sequence)

