<%page args="f, config"/>\
<%
    '''Need different behavior depending on whether we are called on a rep cap container or not'''
    import build.helper as helper
%>\
        '''send_software_edge_trigger
    def send_software_edge_trigger(self, trigger=None, trigger_id=None):

        Sends a command to trigger the signal generator. This VI can act as an
        override for an external edge trigger.

        If called directly on the session, this will send a software start trigger.

            session.send_software_edge_trigger()

        If called using the script trigger repeated capability container, this will
        send a software trigger to the specified script trigger

            session.script_triggers[1].send_software_edge_trigger()

        Note:
        This method does not override external digital edge triggers of the
        NI 5401/5411/5431.
        '''
        # We look at whether we are called directly on the session or a repeated capability container to determine how to behave
        if len(self._repeated_capability) > 0:
            trigger_id = self._repeated_capability
            trigger = 103  # enums.Trigger.SCRIPT
        else:
            trigger_id = "None"
            trigger = 1004  # enums.Trigger.START

        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_ctype = _visatype.ViInt32(trigger)  # case S130
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_SendSoftwareEdgeTrigger(vi_ctype, trigger_ctype, trigger_id_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

