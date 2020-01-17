<%page args="f, config"/>\
<%
    '''Need different behavior depending on whether we are called on a rep cap container or not'''
    import build.helper as helper
%>\
    def send_software_edge_trigger(self):
        '''send_software_edge_trigger

        Sends a command to trigger the Digital Pattern Instrument. This method can act as an
        override for an external edge trigger.

        If called directly on the session, this will send a software start trigger.

            session.send_software_edge_trigger()

        If called using the conditional jump trigger repeated capability container, this will
        send a software trigger to the specified conditional jump trigger

            session.conditional_jump_triggers[1].send_software_edge_trigger()
        '''
        # We look at whether we are called directly on the session or a repeated capability container to determine how to behave
        trigger_identifier = self._repeated_capability
        if len(self._repeated_capability) > 0:
            trigger = 2001  # Conditional Jump Trigger
        else:
            trigger = 2000  # Start Trigger

        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_ctype = _visatype.ViInt32(trigger)  # case S150
        trigger_identifier_ctype = ctypes.create_string_buffer(trigger_identifier.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_SendSoftwareEdgeTrigger(vi_ctype, trigger_ctype, trigger_identifier_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

