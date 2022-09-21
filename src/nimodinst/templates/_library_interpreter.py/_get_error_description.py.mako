    def get_error_description(self, session_handle, encoding, error_code):
        '''get_error_description

        Returns the error description.
        '''
        # We hand-maintain the code that calls into the cfunc rather than leverage code-generation
        # because niModInst_GetExtendedErrorInfo() does not properly do the IVI-dance.
        # See https://github.com/ni/nimi-python/issues/166
        error_info_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_info_ctype = None  # case C050
        error_code = self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size_ctype, error_info_ctype)
        if error_code <= 0:
            return 'Failed to retrieve error description.'
        error_info_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_info_ctype = (_visatype.ViChar * error_info_buffer_size_ctype.value)()  # case C060
        # Note we don't look at the return value. This is intentional as niModInst returns the
        # original error code rather than 0 (VI_SUCCESS).
        self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size_ctype, error_info_ctype)
        return error_info_ctype.value.decode("ascii")
