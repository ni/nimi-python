<%page args="config"/>\
<%
    import build.helper as helper

    get_error_func = config['functions']['GetError']
    get_error_params = helper.filter_parameters(get_error_func, helper.ParameterUsageOptions.LIBRARY_INTERPRETER_METHOD_CALL)
    assert all(p.get('default_value') for p in get_error_params), [[p['name'], p.get('default_value')] for p in get_error_params]
    get_error_params_snippet = ", ".join(str(p['default_value']) for p in get_error_params)
%>\
    def get_error_description(self, error_code):
        '''get_error_description

        Returns the error description.
        '''
        try:
            _, error_string = self.get_error(${get_error_params_snippet})
            return error_string
        except errors.Error:
% if 'error_message' in config['functions']:
            pass

        try:
            '''
            It is expected for get_error to raise when the session is invalid
            (IVI spec requires GetError to fail).
            Use error_message instead. It doesn't require a session.
            '''
            error_string = self.error_message(error_code)
            return error_string
        except errors.Error:
% endif
            return "Failed to retrieve error description."
