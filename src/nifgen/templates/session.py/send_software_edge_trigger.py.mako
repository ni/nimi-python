<%page args="f, config"/>\
<%
    '''Need different behavior depending on whether we are called on a rep cap container or not'''
    import build.helper as helper
%>\
    def send_software_edge_trigger(self, trigger=None, trigger_id=None):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        if trigger is None or trigger_id is None:
            import warnings
            warnings.warn('trigger and trigger_id should now always be passed in to the function', category=DeprecationWarning)

            # We look at whether we are called directly on the session or a repeated capability container to determine how to behave
            if len(self._repeated_capability) > 0:
                trigger_id = self._repeated_capability
                trigger = enums.Trigger.SCRIPT
            else:
                trigger_id = "None"
                trigger = enums.Trigger.START

        elif trigger is not None and trigger_id is not None:
            pass  # This is how the function should be called

        else:
            raise ValueError('Both trigger ({0}) and trigger_id ({1}) should be passed in to the function'.format(str(trigger), str(trigger_id)))

        if type(trigger) is not enums.Trigger:
            raise TypeError('Parameter trigger must be of type ' + str(enums.Trigger))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_ctype = _visatype.ViInt32(trigger)  # case S130
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_SendSoftwareEdgeTrigger(vi_ctype, trigger_ctype, trigger_id_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

