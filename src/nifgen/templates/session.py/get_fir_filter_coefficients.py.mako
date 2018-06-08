<%page args="f, config"/>\
<%
    '''Special implementation of get_fir_filter_coefficients(). Not quite IVI-dance since the size is returned in an out parameter instead of the error_code'''
    import build.helper as helper
    # This file is not currently used - will be enabled when OSP is enabled.
%>\
    def get_fir_filter_coefficients(self):
        '''get_fir_filter_coefficients

        | Returns the FIR filter coefficients used by the onboard signal
          processing block. These coefficients are determined by NI-FGEN and
          based on the FIR filter type and corresponding property (Alpha,
          Passband, BT) unless you are using the custom filter. If you are using
          a custom filter, the coefficients returned are those set with the
          configure_custom_fir_filter_coefficients method coerced to the
          quantized values used by the device.
        | Refer to the FIR Filter topic for your device in the *NI Signal
          Generators Help* for more information about FIR filter coefficients.
          This method is supported only for the NI 5441.

        Tip:
        This method requires repeated capabilities (channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session.channels[0,1].get_fir_filter_coefficients()

        Returns:
            coefficients_array (list of float): Specifies the array of data the onboard signal processor uses for the
                FIR filter coefficients. For the NI 5441, provide a symmetric array of
                95 coefficients to this parameter.

                The coefficients should range between -1.00 and +1.00.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        array_size_ctype = _visatype.ViInt32()  # case S170
        coefficients_array_ctype = None  # case B580
        number_of_coefficients_read_ctype = _visatype.ViInt32()  # case S200
        error_code = self._library.niFgen_GetFIRFilterCoefficients(vi_ctype, channel_name_ctype, array_size_ctype, coefficients_array_ctype, ctypes.pointer(number_of_coefficients_read_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        array_size_ctype = _visatype.ViInt32(number_of_coefficients_read_ctype.value)  # special case
        coefficients_array_size = array_size_ctype.value  # case B590
        coefficients_array_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=coefficients_array_size)  # case B590
        error_code = self._library.niFgen_GetFIRFilterCoefficients(vi_ctype, channel_name_ctype, array_size_ctype, coefficients_array_ctype, ctypes.pointer(number_of_coefficients_read_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(coefficients_array_ctype[i]) for i in range(array_size_ctype.value)]

