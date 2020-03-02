<%page args="f, config"/>\
<%
    '''Need different behavior depending on whether we are called on a rep cap container or not'''
    import build.helper as helper
%>\
    def send_software_edge_trigger(self, trigger=None, trigger_id=None):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''


            session.script_triggers[1].send_software_edge_trigger()

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

