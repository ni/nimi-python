<%page args="config"/>\
<%
    import build.helper as helper

    get_error_func = config['functions']['GetError']
    get_error_params = helper.filter_parameters(get_error_func['parameters'], helper.ParameterUsageOptions.INTERPRETER_METHOD_CALL)
    assert all(p.get('default_value') for p in get_error_params), [[p['name'], p.get('default_value')] for p in get_error_params]
    get_error_params_snippet = ", ".join(str(p['default_value']) for p in get_error_params)
%>\
    def get_error_description(self, error_code):
        '''get_error_description

        Returns the error description.
        '''
        try:
            returned_error_code, error_string = self.get_error(${get_error_params_snippet})
            if returned_error_code == error_code:
                return error_string
        except errors.Error:
            pass
% if 'error_message' in config['functions']:

        try:
            # It is possible that the session is valid but the returned_error_code unequal to error_code
            error_string = self.error_message(error_code)
            return error_string
        except errors.Error:
            pass

        try:
            '''
            It is expected for get_error to raise when the session is invalid
            (IVI spec requires GetError to fail).
            Use error_message instead. It doesn't require a session.
            '''
            save_vi = self.get_session_handle()
            self.set_session_handle()
            error_string = self.error_message(error_code)
            return error_string
        except errors.Error:
            pass
        finally:
            self.set_session_handle(save_vi)
% endif
        return "Failed to retrieve error description."
