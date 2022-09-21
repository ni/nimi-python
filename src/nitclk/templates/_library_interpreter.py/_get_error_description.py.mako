    def get_error_description(self, session_handle, encoding, error_code):
        '''get_error_description

        Returns the error description.
        '''
        try:
            error_string = self.get_extended_error_info(session_handle, encoding)
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."
