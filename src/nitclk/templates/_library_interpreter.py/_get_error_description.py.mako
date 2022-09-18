    def get_error_description(self, error_code):
        '''get_error_description

        Returns the error description.
        '''
        try:
            error_string = self.get_extended_error_info()
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."
