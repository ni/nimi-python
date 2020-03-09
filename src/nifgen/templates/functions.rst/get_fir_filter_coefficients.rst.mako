<%page args="function, config, method_template, indent"/>\
<%
    import build.helper as helper
    # This file is not currently used - will be enabled when OSP is enabled.
%>\
    .. py:method:: get_fir_filter_coefficients()

            | Returns the FIR filter coefficients used by the onboard signal
              processing block. These coefficients are determined by NI-FGEN and
              based on the FIR filter type and corresponding property (Alpha,
              Passband, BT) unless you are using the custom filter. If you are using
              a custom filter, the coefficients returned are those set with the
              :py:meth:`nifgen.Session.configure_custom_fir_filter_coefficients` method coerced to the
              quantized values used by the device.
            | Refer to the FIR Filter topic for your device in the *NI Signal
              Generators Help* for more information about FIR filter coefficients.
              This method is supported only for the NI 5441.


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nifgen.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nifgen.Session instance, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].get_fir_filter_coefficients(array_size, number_of_coefficients_read)


            :rtype: list of float
            :return:


                    Specifies the array of data the onboard signal processor uses for the
                    FIR filter coefficients. For the NI 5441, provide a symmetric array of
                    95 coefficients to this parameter. 

                    The coefficients should range between -1.00 and +1.00.





