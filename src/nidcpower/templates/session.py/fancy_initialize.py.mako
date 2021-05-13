<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the proper initialize method based on input parameters.'''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        if independent_channels:
            resource_string = resource_name  # store potential modifications to resource_name in a separate variable

            if channels:
                # if we have a channels arg, we need to try and combine it with the resource name
                # before calling into initialize with independent channels
                channel_list = (resource_name + "/" + channel for channel in channels.split(","))
                resource_string = ",".join(channel_list)

                import warnings
                warnings.warn(
                    "Attempting to initialize an independent channels session with a channels argument. The resource "
                    "name '" + resource_name + "' will be combined with the channels '" + channels + "' to form the "
                    "fully-qualified channel list '" + resource_string + "'. To avoid this warning, use a "
                    "fully-qualified channel list as the resource name instead of providing a channels argument.",
                    DeprecationWarning
                )

                if "," in resource_name:
                    raise ValueError(
                        "Channels can't be combined with multiple devices in the resource name '" + resource_name + "'. "
                        "Use a single device in the resource name or provide a list of fully-qualified channels as the "
                        "resource name instead of supplying a channels argument."
                    )

            return self._initialize_with_independent_channels(resource_string, reset, option_string)

        else:
            import warnings
            warnings.warn("Initializing session without independent channels enabled.", DeprecationWarning)

            return self._initialize_with_channels(resource_name, channels, reset, option_string)

