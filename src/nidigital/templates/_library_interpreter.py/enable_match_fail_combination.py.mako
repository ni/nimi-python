
    def enable_match_fail_combination(self, sessions, sync_session):  # noqa: N802
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_ctype = _get_ctypes_pointer_for_buffer(value=sessions, library_type=_visatype.ViSession)  # case B550
        sync_session_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_EnableMatchFailCombination(session_count_ctype, sessions_ctype, sync_session_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return
