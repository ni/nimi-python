    def _get_error_description(self, error_code):
        '''_get_error_description

        Returns the error description.
        '''
        try:
            '''
            It is expected for _get_error to raise when the session is invalid
            (IVI spec requires GetError to fail).
            Use _error_message instead. It doesn't require a session.
            '''
            error_string = self._get_extended_error_info()
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."
