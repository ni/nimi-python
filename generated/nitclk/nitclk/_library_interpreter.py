# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import nitclk._library_singleton as _library_singleton
import nitclk._visatype as _visatype
import nitclk.errors as errors


# Helper functions for creating ctypes needed for calling into the driver DLL
def _get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        return numpy.ctypeslib.as_ctypes(value)
    elif isinstance(value, bytes):
        return ctypes.cast(value, ctypes.POINTER(library_type))
    elif isinstance(value, list):
        assert library_type is not None, 'library_type is required for list'
        return (library_type * len(value))(*value)
    else:
        if library_type is not None and size is not None:
            return (library_type * size)()
        else:
            return None


def _convert_to_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class LibraryInterpreter(object):
    '''Library C<->Python interpreter.

    This class is responsible for interpreting the Library's C API. It is responsible for:
    * Converting ctypes to native Python types.
    * Dealing with string encoding.
    * Allocating memory.
    * Converting errors returned by Library into Python exceptions.
    '''

    def __init__(self, encoding):
        self._encoding = encoding
        self._library = _library_singleton.get()
        # Initialize _session_number to 0 for now.
        # Session will directly update it once the driver runtime init function has been called and
        # we have a valid session handle.
        self.set_session_handle()

    def set_session_handle(self, value=0):
        self._session_number = value

    def get_session_handle(self):
        return self._session_number

    def get_error_description(self, error_code):
        '''get_error_description

        Returns the error description.
        '''
        try:
            error_string = self.get_extended_error_info()
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."

    def configure_for_homogeneous_triggers(self, sessions):  # noqa: N802
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_ctype = _get_ctypes_pointer_for_buffer(value=sessions, library_type=_visatype.ViSession)  # case B550
        error_code = self._library.niTClk_ConfigureForHomogeneousTriggers(session_count_ctype, sessions_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def finish_sync_pulse_sender_synchronize(self, sessions, min_time):  # noqa: N802
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_ctype = _get_ctypes_pointer_for_buffer(value=sessions, library_type=_visatype.ViSession)  # case B550
        min_time_ctype = _visatype.ViReal64(min_time)  # case S150
        error_code = self._library.niTClk_FinishSyncPulseSenderSynchronize(session_count_ctype, sessions_ctype, min_time_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def get_attribute_vi_real64(self, channel_name, attribute_id):  # noqa: N802
        session_ctype = _visatype.ViSession(self._session_number)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niTClk_GetAttributeViReal64(session_ctype, channel_name_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(value_ctype.value)

    def get_attribute_vi_session(self, channel_name, attribute_id):  # noqa: N802
        session_ctype = _visatype.ViSession(self._session_number)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niTClk_GetAttributeViSession(session_ctype, channel_name_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: N802
        session_ctype = _visatype.ViSession(self._session_number)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buf_size_ctype = _visatype.ViInt32()  # case S170
        value_ctype = None  # case C050
        error_code = self._library.niTClk_GetAttributeViString(session_ctype, channel_name_ctype, attribute_id_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buf_size_ctype = _visatype.ViInt32(error_code)  # case S180
        value_ctype = (_visatype.ViChar * buf_size_ctype.value)()  # case C060
        error_code = self._library.niTClk_GetAttributeViString(session_ctype, channel_name_ctype, attribute_id_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return value_ctype.value.decode(self._encoding)

    def get_extended_error_info(self):  # noqa: N802
        error_string_ctype = None  # case C050
        error_string_size_ctype = _visatype.ViUInt32()  # case S170
        error_code = self._library.niTClk_GetExtendedErrorInfo(error_string_ctype, error_string_size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        error_string_size_ctype = _visatype.ViUInt32(error_code)  # case S180
        error_string_ctype = (_visatype.ViChar * error_string_size_ctype.value)()  # case C060
        error_code = self._library.niTClk_GetExtendedErrorInfo(error_string_ctype, error_string_size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_string_ctype.value.decode(self._encoding)

    def initiate(self, sessions):  # noqa: N802
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_ctype = _get_ctypes_pointer_for_buffer(value=sessions, library_type=_visatype.ViSession)  # case B550
        error_code = self._library.niTClk_Initiate(session_count_ctype, sessions_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def is_done(self, sessions):  # noqa: N802
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_ctype = _get_ctypes_pointer_for_buffer(value=sessions, library_type=_visatype.ViSession)  # case B550
        done_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niTClk_IsDone(session_count_ctype, sessions_ctype, None if done_ctype is None else (ctypes.pointer(done_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(done_ctype.value)

    def set_attribute_vi_real64(self, channel_name, attribute_id, value):  # noqa: N802
        session_ctype = _visatype.ViSession(self._session_number)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViReal64(value)  # case S150
        error_code = self._library.niTClk_SetAttributeViReal64(session_ctype, channel_name_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_session(self, channel_name, attribute_id, value):  # noqa: N802
        session_ctype = _visatype.ViSession(self._session_number)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViSession(value)  # case S150
        error_code = self._library.niTClk_SetAttributeViSession(session_ctype, channel_name_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_string(self, channel_name, attribute_id, value):  # noqa: N802
        session_ctype = _visatype.ViSession(self._session_number)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = ctypes.create_string_buffer(value.encode(self._encoding))  # case C020
        error_code = self._library.niTClk_SetAttributeViString(session_ctype, channel_name_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def setup_for_sync_pulse_sender_synchronize(self, sessions, min_time):  # noqa: N802
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_ctype = _get_ctypes_pointer_for_buffer(value=sessions, library_type=_visatype.ViSession)  # case B550
        min_time_ctype = _visatype.ViReal64(min_time)  # case S150
        error_code = self._library.niTClk_SetupForSyncPulseSenderSynchronize(session_count_ctype, sessions_ctype, min_time_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def synchronize(self, sessions, min_tclk_period):  # noqa: N802
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_ctype = _get_ctypes_pointer_for_buffer(value=sessions, library_type=_visatype.ViSession)  # case B550
        min_tclk_period_ctype = _visatype.ViReal64(min_tclk_period)  # case S150
        error_code = self._library.niTClk_Synchronize(session_count_ctype, sessions_ctype, min_tclk_period_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def synchronize_to_sync_pulse_sender(self, sessions, min_time):  # noqa: N802
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_ctype = _get_ctypes_pointer_for_buffer(value=sessions, library_type=_visatype.ViSession)  # case B550
        min_time_ctype = _visatype.ViReal64(min_time)  # case S150
        error_code = self._library.niTClk_SynchronizeToSyncPulseSender(session_count_ctype, sessions_ctype, min_time_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def wait_until_done(self, sessions, timeout):  # noqa: N802
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_ctype = _get_ctypes_pointer_for_buffer(value=sessions, library_type=_visatype.ViSession)  # case B550
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        error_code = self._library.niTClk_WaitUntilDone(session_count_ctype, sessions_ctype, timeout_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return
