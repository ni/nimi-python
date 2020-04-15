# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
import ctypes
import datetime  # noqa: F401
# Used by @ivi_synchronized
from functools import wraps

import nidigital._attributes as _attributes
import nidigital._converters as _converters
import nidigital._library_singleton as _library_singleton
import nidigital._visatype as _visatype
import nidigital.enums as enums
import nidigital.errors as errors

import nidigital.history_ram_cycle_information as history_ram_cycle_information  # noqa: F401

import nitclk

# Used for __repr__
import pprint
pp = pprint.PrettyPrinter(indent=4)


# Helper functions for creating ctypes needed for calling into the driver DLL
def get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
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


def get_ctypes_and_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class _Burst(object):
    def __init__(self, session):
        self._session = session
        self._session._initiate()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.abort()


# From https://stackoverflow.com/questions/5929107/decorators-with-parameters
def ivi_synchronized(f):
    @wraps(f)
    def aux(*xs, **kws):
        session = xs[0]  # parameter 0 is 'self' which is the session object
        with session.lock():
            return f(*xs, **kws)
    return aux


class _Lock(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        # _lock_session is called from the lock() function, not here
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.unlock()


class _RepeatedCapabilities(object):
    def __init__(self, session, prefix, current_repeated_capability_list):
        self._session = session
        self._prefix = prefix
        # We need at least one element. If we get an empty list, make the one element an empty string
        self._current_repeated_capability_list = current_repeated_capability_list if len(current_repeated_capability_list) > 0 else ['']
        # Now we know there is at lease one entry, so we look if it is an empty string or not
        self._separator = '/' if len(self._current_repeated_capability_list[0]) > 0 else ''

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        rep_caps_list = _converters.convert_repeated_capabilities(repeated_capability, self._prefix)
        complete_rep_cap_list = [current_rep_cap + self._separator + rep_cap for current_rep_cap in self._current_repeated_capability_list for rep_cap in rep_caps_list]

        return _SessionBase(vi=self._session._vi, repeated_capability_list=complete_rep_cap_list, library=self._session._library, encoding=self._session._encoding, freeze_it=True)


# This is a very simple context manager we can use when we need to set/get attributes
# or call functions from _SessionBase that require no channels. It is tied to the specific
# implementation of _SessionBase and how repeated capabilities are handled.
class _NoChannel(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        self._repeated_capability_cache = self._session._repeated_capability
        self._session._repeated_capability = ''

    def __exit__(self, exc_type, exc_value, traceback):
        self._session._repeated_capability = self._repeated_capability_cache


class _SessionBase(object):
    '''Base class for all NI-Digital Pattern Driver sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    active_load_ioh = _attributes.AttributeViReal64(1150013)
    '''Type: float

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    active_load_iol = _attributes.AttributeViReal64(1150012)
    '''Type: float

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    active_load_vcom = _attributes.AttributeViReal64(1150014)
    '''Type: float

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    cache = _attributes.AttributeViBoolean(1050004)
    channel_count = _attributes.AttributeViInt32(1050203)
    clock_generator_frequency = _attributes.AttributeViReal64(1150073)
    '''Type: float

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    clock_generator_is_running = _attributes.AttributeViBoolean(1150074)
    '''Type: bool

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    conditional_jump_trigger_terminal_name = _attributes.AttributeViString(1150040)
    '''Type: str

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    conditional_jump_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1150033)
    '''Type: enums.TriggerType

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    cycle_number_history_ram_trigger_cycle_number = _attributes.AttributeViInt64(1150044)
    digital_edge_conditional_jump_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DigitalEdge, 1150035)
    '''Type: enums.DigitalEdge

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    digital_edge_conditional_jump_trigger_source = _attributes.AttributeViString(1150034)
    '''Type: str

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    digital_edge_start_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DigitalEdge, 1150031)
    digital_edge_start_trigger_source = _attributes.AttributeViString(1150030)
    driver_setup = _attributes.AttributeViString(1050007)
    exported_conditional_jump_trigger_output_terminal = _attributes.AttributeViString(1150036)
    '''Type: str

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    exported_pattern_opcode_event_output_terminal = _attributes.AttributeViString(1150041)
    '''Type: str

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    exported_start_trigger_output_terminal = _attributes.AttributeViString(1150032)
    frequency_counter_measurement_time = _attributes.AttributeViReal64TimeDeltaSeconds(1150069)
    '''Type: float in seconds or datetime.timedelta

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    group_capabilities = _attributes.AttributeViString(1050401)
    halt_on_keep_alive_opcode = _attributes.AttributeViBoolean(1150062)
    history_ram_buffer_size_per_site = _attributes.AttributeViInt64(1150079)
    history_ram_cycles_to_acquire = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.HistoryRAMCyclesToAcquire, 1150047)
    history_ram_max_samples_to_acquire_per_site = _attributes.AttributeViInt32(1150077)
    history_ram_number_of_samples_is_finite = _attributes.AttributeViBoolean(1150078)
    history_ram_pretrigger_samples = _attributes.AttributeViInt32(1150048)
    history_ram_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.HistoryRAMTriggerType, 1150043)
    instrument_firmware_revision = _attributes.AttributeViString(1050510)
    '''Type: str

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    instrument_manufacturer = _attributes.AttributeViString(1050511)
    instrument_model = _attributes.AttributeViString(1050512)
    interchange_check = _attributes.AttributeViBoolean(1050021)
    io_resource_descriptor = _attributes.AttributeViString(1050304)
    is_keep_alive_active = _attributes.AttributeViBoolean(1150063)
    logical_name = _attributes.AttributeViString(1050305)
    mask_compare = _attributes.AttributeViBoolean(1150060)
    '''Type: bool

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    pattern_label_history_ram_trigger_cycle_offset = _attributes.AttributeViInt64(1150045)
    pattern_label_history_ram_trigger_label = _attributes.AttributeViString(1150046)
    pattern_label_history_ram_trigger_vector_offset = _attributes.AttributeViInt64(1150052)
    pattern_opcode_event_terminal_name = _attributes.AttributeViString(1150042)
    '''Type: str

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    ppmu_allow_extended_voltage_range = _attributes.AttributeViBoolean(1150076)
    '''Type: bool

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    ppmu_aperture_time = _attributes.AttributeViReal64(1150037)
    '''Type: float

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    ppmu_aperture_time_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PPMUApertureTimeUnits, 1150038)
    '''Type: enums.PPMUApertureTimeUnits

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    ppmu_current_level = _attributes.AttributeViReal64(1150019)
    '''Type: float

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    ppmu_current_level_range = _attributes.AttributeViReal64(1150020)
    '''Type: float

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    ppmu_current_limit = _attributes.AttributeViReal64(1150054)
    '''Type: float

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    ppmu_current_limit_behavior = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PPMUCurrentLimitBehavior, 1150064)
    '''Type: enums.PPMUCurrentLimitBehavior

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    ppmu_current_limit_range = _attributes.AttributeViReal64(1150017)
    '''Type: float

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    ppmu_current_limit_supported = _attributes.AttributeViBoolean(1150055)
    '''Type: bool

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    ppmu_output_function = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PPMUOutputFunction, 1150015)
    '''Type: enums.PPMUOutputFunction

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    ppmu_voltage_level = _attributes.AttributeViReal64(1150016)
    '''Type: float

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    ppmu_voltage_limit_high = _attributes.AttributeViReal64(1150022)
    '''Type: float

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    ppmu_voltage_limit_low = _attributes.AttributeViReal64(1150021)
    '''Type: float

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    query_instrument_status = _attributes.AttributeViBoolean(1050003)
    range_check = _attributes.AttributeViBoolean(1050002)
    record_coercions = _attributes.AttributeViBoolean(1050006)
    selected_function = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.SelectedFunction, 1150004)
    '''Type: enums.SelectedFunction

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    sequencer_flag_terminal_name = _attributes.AttributeViString(1150059)
    serial_number = _attributes.AttributeViString(1150001)
    '''Type: str

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    simulate = _attributes.AttributeViBoolean(1050005)
    specific_driver_class_spec_major_version = _attributes.AttributeViInt32(1050515)
    specific_driver_class_spec_minor_version = _attributes.AttributeViInt32(1050516)
    specific_driver_description = _attributes.AttributeViString(1050514)
    specific_driver_prefix = _attributes.AttributeViString(1050302)
    specific_driver_revision = _attributes.AttributeViString(1050551)
    specific_driver_vendor = _attributes.AttributeViString(1050513)
    start_label = _attributes.AttributeViString(1150023)
    start_trigger_terminal_name = _attributes.AttributeViString(1150039)
    start_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1150029)
    supported_instrument_models = _attributes.AttributeViString(1050327)
    tdr_endpoint_termination = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TDREndpointTermination, 1150081)
    tdr_offset = _attributes.AttributeViReal64TimeDeltaSeconds(1150051)
    '''Type: float in seconds or datetime.timedelta

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    termination_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TerminationMode, 1150006)
    '''Type: enums.TerminationMode

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    timing_absolute_delay = _attributes.AttributeViReal64TimeDeltaSeconds(1150072)
    '''Type: float in seconds or datetime.timedelta

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    timing_absolute_delay_enabled = _attributes.AttributeViBoolean(1150071)
    vih = _attributes.AttributeViReal64(1150008)
    '''Type: float

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    vil = _attributes.AttributeViReal64(1150007)
    '''Type: float

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    voh = _attributes.AttributeViReal64(1150010)
    '''Type: float

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    vol = _attributes.AttributeViReal64(1150009)
    '''Type: float

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''
    vterm = _attributes.AttributeViReal64(1150011)
    '''Type: float

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.
    '''

    def __init__(self, repeated_capability_list, vi, library, encoding, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
        self._vi = vi
        self._library = library
        self._encoding = encoding

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("repeated_capability_list=" + pp.pformat(repeated_capability_list))
        param_list.append("vi=" + pp.pformat(vi))
        param_list.append("library=" + pp.pformat(library))
        param_list.append("encoding=" + pp.pformat(encoding))
        self._param_list = ', '.join(param_list)

        # Instantiate any repeated capability objects
        self.channels = _RepeatedCapabilities(self, '', repeated_capability_list)
        self.pins = _RepeatedCapabilities(self, '', repeated_capability_list)
        self.instruments = _RepeatedCapabilities(self, '', repeated_capability_list)
        self.pattern_opcode_events = _RepeatedCapabilities(self, 'patternOpcodeEvent', repeated_capability_list)
        self.conditional_jump_triggers = _RepeatedCapabilities(self, 'conditionalJumpTrigger', repeated_capability_list)
        self.sites = _RepeatedCapabilities(self, 'site', repeated_capability_list)

        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('nidigital', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    def _get_error_description(self, error_code):
        '''_get_error_description

        Returns the error description.
        '''
        try:
            _, error_string = self._get_error()
            return error_string
        except errors.Error:
            pass

        try:
            '''
            It is expected for _get_error to raise when the session is invalid
            (IVI spec requires GetError to fail).
            Use _error_message instead. It doesn't require a session.
            '''
            error_string = self._error_message(error_code)
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."

    ''' These are code-generated '''

    @ivi_synchronized
    def apply_levels_and_timing(self, levels_sheet, timing_sheet, initial_state_high_pins="", initial_state_low_pins="", initial_state_tristate_pins=""):
        r'''apply_levels_and_timing

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            levels_sheet (str):

            timing_sheet (str):

            initial_state_high_pins (str):

            initial_state_low_pins (str):

            initial_state_tristate_pins (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        levels_sheet_ctype = ctypes.create_string_buffer(levels_sheet.encode(self._encoding))  # case C020
        timing_sheet_ctype = ctypes.create_string_buffer(timing_sheet.encode(self._encoding))  # case C020
        initial_state_high_pins_ctype = ctypes.create_string_buffer(initial_state_high_pins.encode(self._encoding))  # case C020
        initial_state_low_pins_ctype = ctypes.create_string_buffer(initial_state_low_pins.encode(self._encoding))  # case C020
        initial_state_tristate_pins_ctype = ctypes.create_string_buffer(initial_state_tristate_pins.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_ApplyLevelsAndTiming(vi_ctype, site_list_ctype, levels_sheet_ctype, timing_sheet_ctype, initial_state_high_pins_ctype, initial_state_low_pins_ctype, initial_state_tristate_pins_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def apply_tdr_offsets(self, offsets):
        r'''apply_tdr_offsets

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            offsets (list of float in seconds or datetime.timedelta):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        num_offsets_ctype = _visatype.ViInt32(0 if offsets is None else len(offsets))  # case S160
        offsets_ctype = get_ctypes_pointer_for_buffer(value=_converters.convert_timedeltas_to_seconds_real64(offsets), library_type=_visatype.ViReal64)  # case B520
        error_code = self._library.niDigital_ApplyTDROffsets(vi_ctype, channel_list_ctype, num_offsets_ctype, offsets_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _burst_pattern(self, start_label, select_digital_function=True, wait_until_done=True, timeout=datetime.timedelta(seconds=10.0)):
        r'''_burst_pattern

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            start_label (str):

            select_digital_function (bool):

            wait_until_done (bool):

            timeout (float in seconds or datetime.timedelta):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        start_label_ctype = ctypes.create_string_buffer(start_label.encode(self._encoding))  # case C020
        select_digital_function_ctype = _visatype.ViBoolean(select_digital_function)  # case S150
        wait_until_done_ctype = _visatype.ViBoolean(wait_until_done)  # case S150
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        error_code = self._library.niDigital_BurstPattern(vi_ctype, site_list_ctype, start_label_ctype, select_digital_function_ctype, wait_until_done_ctype, timeout_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def clock_generator_abort(self):
        r'''clock_generator_abort

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_ClockGenerator_Abort(vi_ctype, channel_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def clock_generator_generate_clock(self, frequency, select_digital_function=True):
        r'''clock_generator_generate_clock

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            frequency (float):

            select_digital_function (bool):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        frequency_ctype = _visatype.ViReal64(frequency)  # case S150
        select_digital_function_ctype = _visatype.ViBoolean(select_digital_function)  # case S150
        error_code = self._library.niDigital_ClockGenerator_GenerateClock(vi_ctype, channel_list_ctype, frequency_ctype, select_digital_function_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_active_load_levels(self, iol, ioh, vcom):
        r'''configure_active_load_levels

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            iol (float):

            ioh (float):

            vcom (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        iol_ctype = _visatype.ViReal64(iol)  # case S150
        ioh_ctype = _visatype.ViReal64(ioh)  # case S150
        vcom_ctype = _visatype.ViReal64(vcom)  # case S150
        error_code = self._library.niDigital_ConfigureActiveLoadLevels(vi_ctype, channel_list_ctype, iol_ctype, ioh_ctype, vcom_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_pattern_burst_sites(self):
        r'''configure_pattern_burst_sites

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_ConfigurePatternBurstSites(vi_ctype, site_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_time_set_compare_edges_strobe(self, time_set_name, strobe_edge):
        r'''configure_time_set_compare_edges_strobe

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            time_set_name (str):

            strobe_edge (float in seconds or datetime.timedelta):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        strobe_edge_ctype = _converters.convert_timedelta_to_seconds_real64(strobe_edge)  # case S140
        error_code = self._library.niDigital_ConfigureTimeSetCompareEdgesStrobe(vi_ctype, pin_list_ctype, time_set_name_ctype, strobe_edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_time_set_compare_edges_strobe2x(self, time_set_name, strobe_edge, strobe2_edge):
        r'''configure_time_set_compare_edges_strobe2x

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            time_set_name (str):

            strobe_edge (float in seconds or datetime.timedelta):

            strobe2_edge (float in seconds or datetime.timedelta):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        strobe_edge_ctype = _converters.convert_timedelta_to_seconds_real64(strobe_edge)  # case S140
        strobe2_edge_ctype = _converters.convert_timedelta_to_seconds_real64(strobe2_edge)  # case S140
        error_code = self._library.niDigital_ConfigureTimeSetCompareEdgesStrobe2x(vi_ctype, pin_list_ctype, time_set_name_ctype, strobe_edge_ctype, strobe2_edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_time_set_drive_edges(self, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge):
        r'''configure_time_set_drive_edges

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            time_set_name (str):

            format (enums.DriveFormat):

            drive_on_edge (float in seconds or datetime.timedelta):

            drive_data_edge (float in seconds or datetime.timedelta):

            drive_return_edge (float in seconds or datetime.timedelta):

            drive_off_edge (float in seconds or datetime.timedelta):

        '''
        if type(format) is not enums.DriveFormat:
            raise TypeError('Parameter format must be of type ' + str(enums.DriveFormat))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        format_ctype = _visatype.ViInt32(format.value)  # case S130
        drive_on_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_on_edge)  # case S140
        drive_data_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_data_edge)  # case S140
        drive_return_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_return_edge)  # case S140
        drive_off_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_off_edge)  # case S140
        error_code = self._library.niDigital_ConfigureTimeSetDriveEdges(vi_ctype, pin_list_ctype, time_set_name_ctype, format_ctype, drive_on_edge_ctype, drive_data_edge_ctype, drive_return_edge_ctype, drive_off_edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_time_set_drive_edges2x(self, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge):
        r'''configure_time_set_drive_edges2x

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            time_set_name (str):

            format (enums.DriveFormat):

            drive_on_edge (float in seconds or datetime.timedelta):

            drive_data_edge (float in seconds or datetime.timedelta):

            drive_return_edge (float in seconds or datetime.timedelta):

            drive_off_edge (float in seconds or datetime.timedelta):

            drive_data2_edge (float in seconds or datetime.timedelta):

            drive_return2_edge (float in seconds or datetime.timedelta):

        '''
        if type(format) is not enums.DriveFormat:
            raise TypeError('Parameter format must be of type ' + str(enums.DriveFormat))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        format_ctype = _visatype.ViInt32(format.value)  # case S130
        drive_on_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_on_edge)  # case S140
        drive_data_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_data_edge)  # case S140
        drive_return_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_return_edge)  # case S140
        drive_off_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_off_edge)  # case S140
        drive_data2_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_data2_edge)  # case S140
        drive_return2_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_return2_edge)  # case S140
        error_code = self._library.niDigital_ConfigureTimeSetDriveEdges2x(vi_ctype, pin_list_ctype, time_set_name_ctype, format_ctype, drive_on_edge_ctype, drive_data_edge_ctype, drive_return_edge_ctype, drive_off_edge_ctype, drive_data2_edge_ctype, drive_return2_edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_time_set_drive_format(self, time_set_name, drive_format):
        r'''configure_time_set_drive_format

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            time_set_name (str):

            drive_format (enums.DriveFormat):

        '''
        if type(drive_format) is not enums.DriveFormat:
            raise TypeError('Parameter drive_format must be of type ' + str(enums.DriveFormat))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        drive_format_ctype = _visatype.ViInt32(drive_format.value)  # case S130
        error_code = self._library.niDigital_ConfigureTimeSetDriveFormat(vi_ctype, pin_list_ctype, time_set_name_ctype, drive_format_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_time_set_edge(self, time_set_name, edge, time):
        r'''configure_time_set_edge

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            time_set_name (str):

            edge (enums.TimeSetEdgeType):

            time (float in seconds or datetime.timedelta):

        '''
        if type(edge) is not enums.TimeSetEdgeType:
            raise TypeError('Parameter edge must be of type ' + str(enums.TimeSetEdgeType))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge.value)  # case S130
        time_ctype = _converters.convert_timedelta_to_seconds_real64(time)  # case S140
        error_code = self._library.niDigital_ConfigureTimeSetEdge(vi_ctype, pin_list_ctype, time_set_name_ctype, edge_ctype, time_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_time_set_edge_multiplier(self, time_set_name, edge_multiplier):
        r'''configure_time_set_edge_multiplier

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            time_set_name (str):

            edge_multiplier (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        edge_multiplier_ctype = _visatype.ViInt32(edge_multiplier)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetEdgeMultiplier(vi_ctype, pin_list_ctype, time_set_name_ctype, edge_multiplier_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_voltage_levels(self, vil, vih, vol, voh, vterm):
        r'''configure_voltage_levels

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            vil (float):

            vih (float):

            vol (float):

            voh (float):

            vterm (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        vil_ctype = _visatype.ViReal64(vil)  # case S150
        vih_ctype = _visatype.ViReal64(vih)  # case S150
        vol_ctype = _visatype.ViReal64(vol)  # case S150
        voh_ctype = _visatype.ViReal64(voh)  # case S150
        vterm_ctype = _visatype.ViReal64(vterm)  # case S150
        error_code = self._library.niDigital_ConfigureVoltageLevels(vi_ctype, channel_list_ctype, vil_ctype, vih_ctype, vol_ctype, voh_ctype, vterm_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def create_capture_waveform_parallel(self, waveform_name):
        r'''create_capture_waveform_parallel

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_name (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_CreateCaptureWaveformParallel(vi_ctype, pin_list_ctype, waveform_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def create_capture_waveform_serial(self, waveform_name, sample_width, bit_order):
        r'''create_capture_waveform_serial

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_name (str):

            sample_width (int):

            bit_order (enums.BitOrder):

        '''
        if type(bit_order) is not enums.BitOrder:
            raise TypeError('Parameter bit_order must be of type ' + str(enums.BitOrder))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        sample_width_ctype = _visatype.ViUInt32(sample_width)  # case S150
        bit_order_ctype = _visatype.ViInt32(bit_order.value)  # case S130
        error_code = self._library.niDigital_CreateCaptureWaveformSerial(vi_ctype, pin_list_ctype, waveform_name_ctype, sample_width_ctype, bit_order_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def create_source_waveform_parallel(self, waveform_name, data_mapping):
        r'''create_source_waveform_parallel

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_name (str):

            data_mapping (enums.SourceDataMapping):

        '''
        if type(data_mapping) is not enums.SourceDataMapping:
            raise TypeError('Parameter data_mapping must be of type ' + str(enums.SourceDataMapping))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        data_mapping_ctype = _visatype.ViInt32(data_mapping.value)  # case S130
        error_code = self._library.niDigital_CreateSourceWaveformParallel(vi_ctype, pin_list_ctype, waveform_name_ctype, data_mapping_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def create_source_waveform_serial(self, waveform_name, data_mapping, sample_width, bit_order):
        r'''create_source_waveform_serial

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_name (str):

            data_mapping (enums.SourceDataMapping):

            sample_width (int):

            bit_order (enums.BitOrder):

        '''
        if type(data_mapping) is not enums.SourceDataMapping:
            raise TypeError('Parameter data_mapping must be of type ' + str(enums.SourceDataMapping))
        if type(bit_order) is not enums.BitOrder:
            raise TypeError('Parameter bit_order must be of type ' + str(enums.BitOrder))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        data_mapping_ctype = _visatype.ViInt32(data_mapping.value)  # case S130
        sample_width_ctype = _visatype.ViUInt32(sample_width)  # case S150
        bit_order_ctype = _visatype.ViInt32(bit_order.value)  # case S130
        error_code = self._library.niDigital_CreateSourceWaveformSerial(vi_ctype, pin_list_ctype, waveform_name_ctype, data_mapping_ctype, sample_width_ctype, bit_order_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def disable_sites(self):
        r'''disable_sites

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_DisableSites(vi_ctype, site_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def enable_sites(self):
        r'''enable_sites

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_EnableSites(vi_ctype, site_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def burst_pattern(self, start_label, select_digital_function=True, wait_until_done=True, timeout=datetime.timedelta(seconds=10.0)):
        '''burst_pattern

        Uses the start_label you specify to burst the pattern on the sites you specify. If you
        specify wait_until_done as True, waits for the burst to complete, and returns comparison results for each site.

        Digital pins retain their state at the end of a pattern burst until the first vector of the pattern burst, a call to
        write_static, or a call to apply_levels_and_timing.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            start_label (str):

            select_digital_function (bool):

            wait_until_done (bool):

            timeout (float in seconds or datetime.timedelta):


        Returns:
            pass_fail ({ int: bool, int: bool, ... }): Dictionary where each key is a site number and value is pass/fail,
                if wait_until_done is specified as True. Else, None.

        '''
        self._burst_pattern(start_label, select_digital_function, wait_until_done, timeout)

        if wait_until_done:
            return self.get_site_pass_fail()
        else:
            return None

    @ivi_synchronized
    def _fetch_capture_waveform(self, waveform_name, samples_to_read, timeout):
        # This is slightly modified codegen from the function
        # We cannot use codegen without major modifications to the code generator
        # This function uses two 'ivi-dance' parameters and then multiplies them together - see
        # the (modified) line below
        # Also, we want to return the two sized that normally wouldn't be returned
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        samples_to_read_ctype = _visatype.ViInt32(samples_to_read)  # case S150
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        data_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        data_ctype = None  # case B610
        actual_num_waveforms_ctype = _visatype.ViInt32()  # case S220
        actual_samples_per_waveform_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_FetchCaptureWaveformU32(vi_ctype, site_list_ctype, waveform_name_ctype, samples_to_read_ctype, timeout_ctype, data_buffer_size_ctype, data_ctype, None if actual_num_waveforms_ctype is None else (ctypes.pointer(actual_num_waveforms_ctype)), None if actual_samples_per_waveform_ctype is None else (ctypes.pointer(actual_samples_per_waveform_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        data_buffer_size_ctype = _visatype.ViInt32(actual_num_waveforms_ctype.value * actual_samples_per_waveform_ctype.value)  # case S200 (modified)
        data_size = actual_num_waveforms_ctype.value * actual_samples_per_waveform_ctype.value  # case B620 (modified)
        data_array = array.array("L", [0] * data_size)  # case B620
        data_ctype = get_ctypes_pointer_for_buffer(value=data_array, library_type=_visatype.ViUInt32)  # case B620
        error_code = self._library.niDigital_FetchCaptureWaveformU32(vi_ctype, site_list_ctype, waveform_name_ctype, samples_to_read_ctype, timeout_ctype, data_buffer_size_ctype, data_ctype, None if actual_num_waveforms_ctype is None else (ctypes.pointer(actual_num_waveforms_ctype)), None if actual_samples_per_waveform_ctype is None else (ctypes.pointer(actual_samples_per_waveform_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return data_array, actual_num_waveforms_ctype.value, actual_samples_per_waveform_ctype.value  # (modified)

    def fetch_capture_waveform(self, waveform_name, samples_to_read, timeout=datetime.timedelta(seconds=10.0)):
        '''fetch_capture_waveform

        Returns dictionary where each key is the site number and the value is array.array of unsigned int

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_name (str):

            samples_to_read (int):

            timeout (float or datetime.timedelta):


        Returns:
            waveform ({ site: data, site: data, ... }): Dictionary where each key is the site number and the value is array.array of unsigned int

        '''
        data, actual_num_waveforms, actual_samples_per_waveform = self._fetch_capture_waveform(waveform_name, samples_to_read, timeout)

        # Get the site list
        site_list = self._get_site_results_site_numbers(enums._SiteResultType.CAPTURE_WAVEFORM)
        assert len(site_list) == actual_num_waveforms

        waveforms = {}

        mv = memoryview(data)

        for i in range(actual_num_waveforms):
            start = i * actual_samples_per_waveform
            end = start + actual_samples_per_waveform
            waveforms[site_list[i]] = mv[start:end]

        return waveforms

    @ivi_synchronized
    def fetch_history_ram_cycle_information(self, position, samples_to_read):
        '''fetch_history_ram_cycle_information

        Returns the pattern information acquired for the specified cycles.

        If the pattern is using the edge multiplier feature, cycle numbers represent tester cycles, each of which may
        consist of multiple DUT cycles. When using pins with mixed edge multipliers, pins may return
        PinState.PIN_STATE_NOT_ACQUIRED for DUT cycles where those pins do not have edges defined.

        Site number on which to retrieve pattern information must be specified via sites repeated capability.
        The method returns an error if more than one site is specified.

        Pins for which to retrieve pattern information must be specified via pins repeated capability.
        If pins are not specified, pin list from the pattern containing the start label is used. Call
        get_pattern_pin_names with the start label to retrieve the pins associated with the pattern burst:

        .. code:: python

         session.sites[0].pins['PinA', 'PinB'].fetch_history_ram_cycle_information(0, -1)

        Note:
        Before bursting a pattern, you must configure the History RAM trigger and specify which cycles to acquire.

        history_ram_trigger_type should be used to specify the trigger condition on which History RAM
        starts acquiring pattern information.

        If History RAM trigger is configured as HistoryRAMTriggerType.CYCLE_NUMBER,
        cycle_number_history_ram_trigger_cycle_number should be used to specify the cycle number on which
        History RAM starts acquiring pattern information.

        If History RAM trigger is configured as HistoryRAMTriggerType.PATTERN_LABEL,
        pattern_label_history_ram_trigger_label should be used to specify the pattern label from which to
        start acquiring pattern information.
        pattern_label_history_ram_trigger_vector_offset should be used to specify the number of vectors
        following the specified pattern label from which to start acquiring pattern information.
        pattern_label_history_ram_trigger_cycle_offset should be used to specify the number of cycles
        following the specified pattern label and vector offset from which to start acquiring pattern information.

        For all History RAM trigger conditions, history_ram_pretrigger_samples should be used to specify
        the number of samples to acquire before the trigger conditions are met. If you configure History RAM to only
        acquire failed cycles, you must set history_ram_pretrigger_samples to 0.

        history_ram_cycles_to_acquire should be used to specify which cycles History RAM acquires after
        the trigger conditions are met.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            position (int): Sample index from which to start fetching pattern information.

            samples_to_read (int): Number of samples to fetch. A value of -1 specifies to fetch all available samples.


        Returns:
            history_ram_cycle_information (list of HistoryRAMCycleInformation): Returns a list of class instances with
                the following information about each pattern cycle:

                -  **pattern_name** (str)  Name of the pattern for the acquired cycle.
                -  **time_set_name** (str) Time set for the acquired cycle.
                -  **vector_number** (int) Vector number within the pattern for the acquired cycle. Vector numbers start
                   at 0 from the beginning of the pattern.
                -  **cycle_number** (int) Cycle number acquired by this History RAM sample. Cycle numbers start at 0
                   from the beginning of the pattern burst.
                -  **scan_cycle_number** (int) Scan cycle number acquired by this History RAM sample. Scan cycle numbers
                   start at 0 from the first cycle of the scan vector. Scan cycle numbers are -1 for cycles that do not
                   have a scan opcode.
                -  **expected_pin_states** (list of list of enums.PinState) Pin states as expected by the loaded
                   pattern in the order specified in the pin list. Pins without defined edges in the specified DUT cycle
                   will have a value of PinState.PIN_STATE_NOT_ACQUIRED.
                   Length of the outer list will be equal to the value of edge multiplier for the given vector.
                   Length of the inner list will be equal to the number of pins requested.
                -  **actual_pin_states** (list of list of enums.PinState) Pin states acquired by History RAM in the
                   order specified in the pin list. Pins without defined edges in the specified DUT cycle will have a
                   value of PinState.PIN_STATE_NOT_ACQUIRED.
                   Length of the outer list will be equal to the value of edge multiplier for the given vector.
                   Length of the inner list will be equal to the number of pins requested.
                -  **per_pin_pass_fail** (list of list of bool) Pass fail information for pins in the order specified in
                   the pin list. Pins without defined edges in the specified DUT cycle will have a value of pass (True).
                   Length of the outer list will be equal to the value of edge multiplier for the given vector.
                   Length of the inner list will be equal to the number of pins requested.

        '''
        # Extract the site number and pin list from repeated capability
        repeated_capability_lists = _converters.convert_chained_repeated_capability_to_parts(self._repeated_capability)
        site = repeated_capability_lists[0]
        if not site.startswith('site'):
            raise ValueError('Site number on which to retrieve pattern information must be specified via sites repeated capability.')
        pins = '' if len(repeated_capability_lists) == 1 else repeated_capability_lists[1]

        # Put site back into repeated capability container; it will be used by other
        # sites-rep-cap-based methods that will be called later.
        self._repeated_capability = site

        if position < 0:
            raise ValueError('position should be greater than or equal to 0.')

        if samples_to_read < -1:
            raise ValueError('samples_to_read should be greater than or equal to -1.')

        # site is passed as repeated capability
        samples_available = self.get_history_ram_sample_count()
        if position > samples_available:
            raise ValueError('position: Specified value = {0}, Maximum value = {1}.'.format(position, samples_available - 1))

        if samples_to_read == -1:
            with _NoChannel(session=self):
                if not self.history_ram_number_of_samples_is_finite:
                    raise RuntimeError(
                        'Specifying -1 to fetch all History RAM samples is not supported when the digital pattern instrument is '
                        'configured for continuous History RAM acquisition. You must specify an exact number of samples to fetch.')
            samples_to_read = samples_available - position

        if position + samples_to_read > samples_available:
            raise ValueError(
                'position: Specified value = {0}, samples_to_read: Specified value = {1}; Samples available = {2}.'
                .format(position, samples_to_read, samples_available - position))

        pattern_names = {}
        time_set_names = {}
        cycle_infos = []
        for _ in range(samples_to_read):

            # site is passed as repeated capability
            pattern_index, time_set_index, vector_number, cycle_number, num_dut_cycles = self._fetch_history_ram_cycle_information(position)

            if pattern_index not in pattern_names:
                # Repeated capability is not used
                pattern_names[pattern_index] = self.get_pattern_name(pattern_index)
            pattern_name = pattern_names[pattern_index]

            if time_set_index not in time_set_names:
                # Repeated capability is not used
                time_set_names[time_set_index] = self.get_time_set_name(time_set_index)
            time_set_name = time_set_names[time_set_index]

            # site is passed as repeated capability
            scan_cycle_number = self._fetch_history_ram_scan_cycle_number(position)

            vector_expected_pin_states = []
            vector_actual_pin_states = []
            vector_per_pin_pass_fail = []
            for dut_cycle_index in range(num_dut_cycles):
                # site is passed as repeated capability
                cycle_expected_pin_states, cycle_actual_pin_states, cycle_per_pin_pass_fail = self._fetch_history_ram_cycle_pin_data(pins, position, dut_cycle_index)
                vector_expected_pin_states.append(cycle_expected_pin_states)
                vector_actual_pin_states.append(cycle_actual_pin_states)
                vector_per_pin_pass_fail.append(cycle_per_pin_pass_fail)

            cycle_infos.append(history_ram_cycle_information.HistoryRAMCycleInformation(
                pattern_name=pattern_name,
                time_set_name=time_set_name,
                vector_number=vector_number,
                cycle_number=cycle_number,
                scan_cycle_number=scan_cycle_number,
                expected_pin_states=vector_expected_pin_states,
                actual_pin_states=vector_actual_pin_states,
                per_pin_pass_fail=vector_per_pin_pass_fail))
            position += 1

        return cycle_infos

    @ivi_synchronized
    def get_pin_results_pin_information(self):
        '''get_pin_results_pin_information

        Returns a list of named tuples (PinInfo) that <FILL IN THE BLANK HERE>

        Fields in PinInfo:

        - **pin_name** (str)
        - **site_number** (int)
        - **channel_name** (str)

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Returns:
            pin_info (list of PinInfo): List of named tuples with fields:

                - **pin_name** (str)
                - **site_number** (int)
                - **channel_name** (str)

        '''
        import collections
        PinInfo = collections.namedtuple('PinInformation', ['pin_name', 'site_number', 'channel_name'])

        pin_indexes, site_numbers, channel_indexes = self._get_pin_results_pin_information()
        assert len(pin_indexes) == len(site_numbers), "length of returned arrays don't match"
        assert len(pin_indexes) == len(channel_indexes), "length of returned arrays don't match"

        pin_infos = []
        for i in range(len(pin_indexes)):
            pin_name = "" if pin_indexes[i] == -1 else self._get_pin_name(pin_indexes[i])
            channel_name = self.get_channel_name(channel_indexes[i])
            pin_infos.append(PinInfo(pin_name=pin_name, site_number=site_numbers[i], channel_name=channel_name))

        return pin_infos

    @ivi_synchronized
    def get_site_pass_fail(self):
        '''get_site_pass_fail

        Returns dictionary where each key is a site number and value is pass/fail

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Returns:
            pass_fail ({ int: bool, int: bool, ... }): Dictionary where each key is a site number and value is pass/fail

        '''
        # For site_list, we just use the repeated capability
        result_list = self._get_site_pass_fail()
        site_list = self._get_site_results_site_numbers(enums._SiteResultType.PASS_FAIL)
        assert len(site_list) == len(result_list)

        return dict(zip(site_list, result_list))

    @ivi_synchronized
    def _fetch_history_ram_cycle_information(self, sample_index):
        r'''_fetch_history_ram_cycle_information

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            sample_index (int):


        Returns:
            pattern_index (int):

            time_set_index (int):

            vector_number (int):

            cycle_number (int):

            num_dut_cycles (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        sample_index_ctype = _visatype.ViInt64(sample_index)  # case S150
        pattern_index_ctype = _visatype.ViInt32()  # case S220
        time_set_index_ctype = _visatype.ViInt32()  # case S220
        vector_number_ctype = _visatype.ViInt64()  # case S220
        cycle_number_ctype = _visatype.ViInt64()  # case S220
        num_dut_cycles_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_FetchHistoryRAMCycleInformation(vi_ctype, site_ctype, sample_index_ctype, None if pattern_index_ctype is None else (ctypes.pointer(pattern_index_ctype)), None if time_set_index_ctype is None else (ctypes.pointer(time_set_index_ctype)), None if vector_number_ctype is None else (ctypes.pointer(vector_number_ctype)), None if cycle_number_ctype is None else (ctypes.pointer(cycle_number_ctype)), None if num_dut_cycles_ctype is None else (ctypes.pointer(num_dut_cycles_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(pattern_index_ctype.value), int(time_set_index_ctype.value), int(vector_number_ctype.value), int(cycle_number_ctype.value), int(num_dut_cycles_ctype.value)

    @ivi_synchronized
    def _fetch_history_ram_cycle_pin_data(self, pin_list, sample_index, dut_cycle_index):
        r'''_fetch_history_ram_cycle_pin_data

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            pin_list (str):

            sample_index (int):

            dut_cycle_index (int):


        Returns:
            expected_pin_states (list of enums.PinState):

            actual_pin_states (list of enums.PinState):

            per_pin_pass_fail (list of bool):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C020
        sample_index_ctype = _visatype.ViInt64(sample_index)  # case S150
        dut_cycle_index_ctype = _visatype.ViInt32(dut_cycle_index)  # case S150
        pin_data_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        expected_pin_states_ctype = None  # case B610
        actual_pin_states_ctype = None  # case B610
        per_pin_pass_fail_ctype = None  # case B610
        actual_num_pin_data_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_FetchHistoryRAMCyclePinData(vi_ctype, site_ctype, pin_list_ctype, sample_index_ctype, dut_cycle_index_ctype, pin_data_buffer_size_ctype, expected_pin_states_ctype, actual_pin_states_ctype, per_pin_pass_fail_ctype, None if actual_num_pin_data_ctype is None else (ctypes.pointer(actual_num_pin_data_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        pin_data_buffer_size_ctype = _visatype.ViInt32(actual_num_pin_data_ctype.value)  # case S200
        expected_pin_states_size = actual_num_pin_data_ctype.value  # case B620
        expected_pin_states_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViUInt8, size=expected_pin_states_size)  # case B620
        actual_pin_states_size = actual_num_pin_data_ctype.value  # case B620
        actual_pin_states_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViUInt8, size=actual_pin_states_size)  # case B620
        per_pin_pass_fail_size = actual_num_pin_data_ctype.value  # case B620
        per_pin_pass_fail_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViBoolean, size=per_pin_pass_fail_size)  # case B620
        error_code = self._library.niDigital_FetchHistoryRAMCyclePinData(vi_ctype, site_ctype, pin_list_ctype, sample_index_ctype, dut_cycle_index_ctype, pin_data_buffer_size_ctype, expected_pin_states_ctype, actual_pin_states_ctype, per_pin_pass_fail_ctype, None if actual_num_pin_data_ctype is None else (ctypes.pointer(actual_num_pin_data_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [enums.PinState(expected_pin_states_ctype[i]) for i in range(pin_data_buffer_size_ctype.value)], [enums.PinState(actual_pin_states_ctype[i]) for i in range(pin_data_buffer_size_ctype.value)], [bool(per_pin_pass_fail_ctype[i]) for i in range(pin_data_buffer_size_ctype.value)]

    @ivi_synchronized
    def _fetch_history_ram_scan_cycle_number(self, sample_index):
        r'''_fetch_history_ram_scan_cycle_number

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            sample_index (int):


        Returns:
            scan_cycle_number (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        sample_index_ctype = _visatype.ViInt64(sample_index)  # case S150
        scan_cycle_number_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niDigital_FetchHistoryRAMScanCycleNumber(vi_ctype, site_ctype, sample_index_ctype, None if scan_cycle_number_ctype is None else (ctypes.pointer(scan_cycle_number_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(scan_cycle_number_ctype.value)

    @ivi_synchronized
    def frequency_counter_measure_frequency(self):
        r'''frequency_counter_measure_frequency

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Returns:
            frequencies (list of float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        frequencies_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        frequencies_ctype = None  # case B610
        actual_num_frequencies_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_FrequencyCounter_MeasureFrequency(vi_ctype, channel_list_ctype, frequencies_buffer_size_ctype, frequencies_ctype, None if actual_num_frequencies_ctype is None else (ctypes.pointer(actual_num_frequencies_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        frequencies_buffer_size_ctype = _visatype.ViInt32(actual_num_frequencies_ctype.value)  # case S200
        frequencies_size = actual_num_frequencies_ctype.value  # case B620
        frequencies_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=frequencies_size)  # case B620
        error_code = self._library.niDigital_FrequencyCounter_MeasureFrequency(vi_ctype, channel_list_ctype, frequencies_buffer_size_ctype, frequencies_ctype, None if actual_num_frequencies_ctype is None else (ctypes.pointer(actual_num_frequencies_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(frequencies_ctype[i]) for i in range(frequencies_buffer_size_ctype.value)]

    @ivi_synchronized
    def _get_attribute_vi_boolean(self, attribute):
        r'''_get_attribute_vi_boolean

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            attribute (int):


        Returns:
            value (bool):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDigital_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(value_ctype.value)

    @ivi_synchronized
    def _get_attribute_vi_int32(self, attribute):
        r'''_get_attribute_vi_int32

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            attribute (int):


        Returns:
            value (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    @ivi_synchronized
    def _get_attribute_vi_int64(self, attribute):
        r'''_get_attribute_vi_int64

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            attribute (int):


        Returns:
            value (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niDigital_GetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    @ivi_synchronized
    def _get_attribute_vi_real64(self, attribute):
        r'''_get_attribute_vi_real64

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            attribute (int):


        Returns:
            value (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDigital_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(value_ctype.value)

    @ivi_synchronized
    def _get_attribute_vi_string(self, attribute):
        r'''_get_attribute_vi_string

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            attribute (int):


        Returns:
            value (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        value_ctype = None  # case C050
        error_code = self._library.niDigital_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_ctype, buffer_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        value_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_ctype, buffer_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return value_ctype.value.decode(self._encoding)

    @ivi_synchronized
    def get_channel_name(self, index):
        r'''get_channel_name

        TBD

        Args:
            index (int):


        Returns:
            name (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        name_ctype = None  # case C050
        error_code = self._library.niDigital_GetChannelName(vi_ctype, index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        name_ctype = (_visatype.ViChar * name_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetChannelName(vi_ctype, index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return name_ctype.value.decode(self._encoding)

    def _get_error(self):
        r'''_get_error

        TBD

        Returns:
            error_code (int):

            error_description (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        error_description_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_description_ctype = None  # case C050
        error_code = self._library.niDigital_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        error_description_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_description_ctype = (_visatype.ViChar * error_description_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), error_description_ctype.value.decode(self._encoding)

    @ivi_synchronized
    def get_fail_count(self):
        r'''get_fail_count

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Returns:
            failure_count (list of int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        failure_count_ctype = None  # case B610
        actual_num_read_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetFailCount(vi_ctype, channel_list_ctype, buffer_size_ctype, failure_count_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_num_read_ctype.value)  # case S200
        failure_count_size = actual_num_read_ctype.value  # case B620
        failure_count_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt64, size=failure_count_size)  # case B620
        error_code = self._library.niDigital_GetFailCount(vi_ctype, channel_list_ctype, buffer_size_ctype, failure_count_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(failure_count_ctype[i]) for i in range(buffer_size_ctype.value)]

    @ivi_synchronized
    def get_history_ram_sample_count(self):
        r'''get_history_ram_sample_count

        Returns the number of samples History RAM acquired on the last pattern burst.

        Note:
        Before bursting a pattern, you must configure the History RAM trigger and specify which cycles to acquire.

        history_ram_trigger_type should be used to specify the trigger condition on which History RAM
        starts acquiring pattern information.

        If History RAM trigger is configured as HistoryRAMTriggerType.CYCLE_NUMBER,
        cycle_number_history_ram_trigger_cycle_number should be used to specify the cycle number on which
        History RAM starts acquiring pattern information.

        If History RAM trigger is configured as HistoryRAMTriggerType.PATTERN_LABEL,
        pattern_label_history_ram_trigger_label should be used to specify the pattern label from which to
        start acquiring pattern information.
        pattern_label_history_ram_trigger_vector_offset should be used to specify the number of vectors
        following the specified pattern label from which to start acquiring pattern information.
        pattern_label_history_ram_trigger_cycle_offset should be used to specify the number of cycles
        following the specified pattern label and vector offset from which to start acquiring pattern information.

        For all History RAM trigger conditions, history_ram_pretrigger_samples should be used to specify
        the number of samples to acquire before the trigger conditions are met. If you configure History RAM to only
        acquire failed cycles, you must set history_ram_pretrigger_samples to 0.

        history_ram_cycles_to_acquire should be used to specify which cycles History RAM acquires after
        the trigger conditions are met.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Returns:
            sample_count (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        sample_count_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niDigital_GetHistoryRAMSampleCount(vi_ctype, site_ctype, None if sample_count_ctype is None else (ctypes.pointer(sample_count_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(sample_count_ctype.value)

    @ivi_synchronized
    def get_pattern_name(self, pattern_index):
        r'''get_pattern_name

        TBD

        Args:
            pattern_index (int):


        Returns:
            name (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pattern_index_ctype = _visatype.ViInt32(pattern_index)  # case S150
        name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        name_ctype = None  # case C050
        error_code = self._library.niDigital_GetPatternName(vi_ctype, pattern_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        name_ctype = (_visatype.ViChar * name_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetPatternName(vi_ctype, pattern_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return name_ctype.value.decode(self._encoding)

    @ivi_synchronized
    def _get_pin_name(self, pin_index):
        r'''_get_pin_name

        TBD

        Args:
            pin_index (int):


        Returns:
            name (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_index_ctype = _visatype.ViInt32(pin_index)  # case S150
        name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        name_ctype = None  # case C050
        error_code = self._library.niDigital_GetPinName(vi_ctype, pin_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        name_ctype = (_visatype.ViChar * name_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetPinName(vi_ctype, pin_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return name_ctype.value.decode(self._encoding)

    @ivi_synchronized
    def _get_pin_results_pin_information(self):
        r'''_get_pin_results_pin_information

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Returns:
            pin_indexes (list of int):

            site_numbers (list of int):

            channel_indexes (list of int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        pin_indexes_ctype = None  # case B610
        site_numbers_ctype = None  # case B610
        channel_indexes_ctype = None  # case B610
        actual_num_values_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetPinResultsPinInformation(vi_ctype, channel_list_ctype, buffer_size_ctype, pin_indexes_ctype, site_numbers_ctype, channel_indexes_ctype, None if actual_num_values_ctype is None else (ctypes.pointer(actual_num_values_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_num_values_ctype.value)  # case S200
        pin_indexes_size = actual_num_values_ctype.value  # case B620
        pin_indexes_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=pin_indexes_size)  # case B620
        site_numbers_size = actual_num_values_ctype.value  # case B620
        site_numbers_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=site_numbers_size)  # case B620
        channel_indexes_size = actual_num_values_ctype.value  # case B620
        channel_indexes_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=channel_indexes_size)  # case B620
        error_code = self._library.niDigital_GetPinResultsPinInformation(vi_ctype, channel_list_ctype, buffer_size_ctype, pin_indexes_ctype, site_numbers_ctype, channel_indexes_ctype, None if actual_num_values_ctype is None else (ctypes.pointer(actual_num_values_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(pin_indexes_ctype[i]) for i in range(buffer_size_ctype.value)], [int(site_numbers_ctype[i]) for i in range(buffer_size_ctype.value)], [int(channel_indexes_ctype[i]) for i in range(buffer_size_ctype.value)]

    @ivi_synchronized
    def _get_site_pass_fail(self):
        r'''_get_site_pass_fail

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Returns:
            pass_fail (list of bool):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        pass_fail_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        pass_fail_ctype = None  # case B610
        actual_num_sites_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetSitePassFail(vi_ctype, site_list_ctype, pass_fail_buffer_size_ctype, pass_fail_ctype, None if actual_num_sites_ctype is None else (ctypes.pointer(actual_num_sites_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        pass_fail_buffer_size_ctype = _visatype.ViInt32(actual_num_sites_ctype.value)  # case S200
        pass_fail_size = actual_num_sites_ctype.value  # case B620
        pass_fail_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViBoolean, size=pass_fail_size)  # case B620
        error_code = self._library.niDigital_GetSitePassFail(vi_ctype, site_list_ctype, pass_fail_buffer_size_ctype, pass_fail_ctype, None if actual_num_sites_ctype is None else (ctypes.pointer(actual_num_sites_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [bool(pass_fail_ctype[i]) for i in range(pass_fail_buffer_size_ctype.value)]

    @ivi_synchronized
    def _get_site_results_site_numbers(self, site_result_type):
        r'''_get_site_results_site_numbers

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            site_result_type (enums.SiteResultType):


        Returns:
            site_numbers (list of int):

        '''
        if type(site_result_type) is not enums._SiteResultType:
            raise TypeError('Parameter site_result_type must be of type ' + str(enums._SiteResultType))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        site_result_type_ctype = _visatype.ViInt32(site_result_type.value)  # case S130
        site_numbers_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        site_numbers_ctype = None  # case B610
        actual_num_site_numbers_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetSiteResultsSiteNumbers(vi_ctype, site_list_ctype, site_result_type_ctype, site_numbers_buffer_size_ctype, site_numbers_ctype, None if actual_num_site_numbers_ctype is None else (ctypes.pointer(actual_num_site_numbers_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        site_numbers_buffer_size_ctype = _visatype.ViInt32(actual_num_site_numbers_ctype.value)  # case S200
        site_numbers_size = actual_num_site_numbers_ctype.value  # case B620
        site_numbers_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=site_numbers_size)  # case B620
        error_code = self._library.niDigital_GetSiteResultsSiteNumbers(vi_ctype, site_list_ctype, site_result_type_ctype, site_numbers_buffer_size_ctype, site_numbers_ctype, None if actual_num_site_numbers_ctype is None else (ctypes.pointer(actual_num_site_numbers_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(site_numbers_ctype[i]) for i in range(site_numbers_buffer_size_ctype.value)]

    @ivi_synchronized
    def get_time_set_drive_format(self, time_set_name):
        r'''get_time_set_drive_format

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            time_set_name (str):


        Returns:
            format (enums.DriveFormat):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        format_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetTimeSetDriveFormat(vi_ctype, pin_ctype, time_set_name_ctype, None if format_ctype is None else (ctypes.pointer(format_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.DriveFormat(format_ctype.value)

    @ivi_synchronized
    def get_time_set_edge(self, time_set_name, edge):
        r'''get_time_set_edge

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            time_set_name (str):

            edge (enums.TimeSetEdgeType):


        Returns:
            time (float):

        '''
        if type(edge) is not enums.TimeSetEdgeType:
            raise TypeError('Parameter edge must be of type ' + str(enums.TimeSetEdgeType))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge.value)  # case S130
        time_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDigital_GetTimeSetEdge(vi_ctype, pin_ctype, time_set_name_ctype, edge_ctype, None if time_ctype is None else (ctypes.pointer(time_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(time_ctype.value)

    @ivi_synchronized
    def get_time_set_edge_multiplier(self, time_set_name):
        r'''get_time_set_edge_multiplier

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            time_set_name (str):


        Returns:
            edge_multiplier (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        edge_multiplier_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetTimeSetEdgeMultiplier(vi_ctype, pin_ctype, time_set_name_ctype, None if edge_multiplier_ctype is None else (ctypes.pointer(edge_multiplier_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(edge_multiplier_ctype.value)

    @ivi_synchronized
    def get_time_set_name(self, time_set_index):
        r'''get_time_set_name

        TBD

        Args:
            time_set_index (int):


        Returns:
            name (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        time_set_index_ctype = _visatype.ViInt32(time_set_index)  # case S150
        name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        name_ctype = None  # case C050
        error_code = self._library.niDigital_GetTimeSetName(vi_ctype, time_set_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        name_ctype = (_visatype.ViChar * name_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetTimeSetName(vi_ctype, time_set_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return name_ctype.value.decode(self._encoding)

    @ivi_synchronized
    def is_site_enabled(self):
        r'''is_site_enabled

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Returns:
            enable (bool):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        enable_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDigital_IsSiteEnabled(vi_ctype, site_ctype, None if enable_ctype is None else (ctypes.pointer(enable_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(enable_ctype.value)

    def lock(self):
        '''lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-Digital Pattern Driver locked the session.
            -  After a call to the lock method returns
               successfully, no other threads can access the device session until
               you call the unlock method or exit out of the with block when using
               lock context manager.
            -  Use the lock method and the
               unlock method around a sequence of calls to
               instrument driver methods if you require that the device retain its
               settings through the end of the sequence.

        You can safely make nested calls to the lock method
        within the same thread. To completely unlock the session, you must
        balance each call to the lock method with a call to
        the unlock method.

        Returns:
            lock (context manager): When used in a with statement, nidigital.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        '''
        self._lock_session()  # We do not call _lock_session() in the context manager so that this function can
        # act standalone as well and let the client call unlock() explicitly. If they do use the context manager,
        # that will handle the unlock for them
        return _Lock(self)

    def _lock_session(self):
        '''_lock_session

        Actual call to driver
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_LockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return

    @ivi_synchronized
    def ppmu_measure(self, measurement_type):
        r'''ppmu_measure

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            measurement_type (enums.PPMUMeasurementType):


        Returns:
            measurements (list of float):

        '''
        if type(measurement_type) is not enums.PPMUMeasurementType:
            raise TypeError('Parameter measurement_type must be of type ' + str(enums.PPMUMeasurementType))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        measurement_type_ctype = _visatype.ViInt32(measurement_type.value)  # case S130
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        measurements_ctype = None  # case B610
        actual_num_read_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_PPMU_Measure(vi_ctype, channel_list_ctype, measurement_type_ctype, buffer_size_ctype, measurements_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_num_read_ctype.value)  # case S200
        measurements_size = actual_num_read_ctype.value  # case B620
        measurements_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=measurements_size)  # case B620
        error_code = self._library.niDigital_PPMU_Measure(vi_ctype, channel_list_ctype, measurement_type_ctype, buffer_size_ctype, measurements_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(measurements_ctype[i]) for i in range(buffer_size_ctype.value)]

    @ivi_synchronized
    def ppmu_source(self):
        r'''ppmu_source

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_PPMU_Source(vi_ctype, channel_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def read_static(self):
        r'''read_static

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Returns:
            data (list of enums.PinState):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        data_ctype = None  # case B610
        actual_num_read_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_ReadStatic(vi_ctype, channel_list_ctype, buffer_size_ctype, data_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_num_read_ctype.value)  # case S200
        data_size = actual_num_read_ctype.value  # case B620
        data_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViUInt8, size=data_size)  # case B620
        error_code = self._library.niDigital_ReadStatic(vi_ctype, channel_list_ctype, buffer_size_ctype, data_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [enums.PinState(data_ctype[i]) for i in range(buffer_size_ctype.value)]

    @ivi_synchronized
    def _set_attribute_vi_boolean(self, attribute, value):
        r'''_set_attribute_vi_boolean

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            attribute (int):

            value (bool):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViBoolean(value)  # case S150
        error_code = self._library.niDigital_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _set_attribute_vi_int32(self, attribute, value):
        r'''_set_attribute_vi_int32

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            attribute (int):

            value (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt32(value)  # case S150
        error_code = self._library.niDigital_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _set_attribute_vi_int64(self, attribute, value):
        r'''_set_attribute_vi_int64

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            attribute (int):

            value (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt64(value)  # case S150
        error_code = self._library.niDigital_SetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _set_attribute_vi_real64(self, attribute, value):
        r'''_set_attribute_vi_real64

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            attribute (int):

            value (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViReal64(value)  # case S150
        error_code = self._library.niDigital_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _set_attribute_vi_string(self, attribute, value):
        r'''_set_attribute_vi_string

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            attribute (int):

            value (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = ctypes.create_string_buffer(value.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def tdr(self, apply_offsets=True):
        r'''tdr

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            apply_offsets (bool):


        Returns:
            offsets (list of datetime.timedelta):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        apply_offsets_ctype = _visatype.ViBoolean(apply_offsets)  # case S150
        offsets_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        offsets_ctype = None  # case B610
        actual_num_offsets_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_TDR(vi_ctype, channel_list_ctype, apply_offsets_ctype, offsets_buffer_size_ctype, offsets_ctype, None if actual_num_offsets_ctype is None else (ctypes.pointer(actual_num_offsets_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        offsets_buffer_size_ctype = _visatype.ViInt32(actual_num_offsets_ctype.value)  # case S200
        offsets_size = actual_num_offsets_ctype.value  # case B620
        offsets_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=offsets_size)  # case B620
        error_code = self._library.niDigital_TDR(vi_ctype, channel_list_ctype, apply_offsets_ctype, offsets_buffer_size_ctype, offsets_ctype, None if actual_num_offsets_ctype is None else (ctypes.pointer(actual_num_offsets_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_seconds_real64_to_timedeltas([float(offsets_ctype[i]) for i in range(offsets_buffer_size_ctype.value)])

    def unlock(self):
        '''unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_UnlockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return

    @ivi_synchronized
    def _write_source_waveform_site_unique_u32(self, waveform_name, num_waveforms, samples_per_waveform, waveform_data):
        r'''_write_source_waveform_site_unique_u32

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_name (str):

            num_waveforms (int):

            samples_per_waveform (int):

            waveform_data (array.array("L")):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        num_waveforms_ctype = _visatype.ViInt32(num_waveforms)  # case S150
        samples_per_waveform_ctype = _visatype.ViInt32(samples_per_waveform)  # case S150
        waveform_data_array = get_ctypes_and_array(value=waveform_data, array_type="L")  # case B550
        waveform_data_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_visatype.ViUInt32)  # case B550
        error_code = self._library.niDigital_WriteSourceWaveformSiteUniqueU32(vi_ctype, site_list_ctype, waveform_name_ctype, num_waveforms_ctype, samples_per_waveform_ctype, waveform_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def write_static(self, state):
        r'''write_static

        TBD

        Tip:
        This method requires repeated capabilities. If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.

        Args:
            state (enums.WriteStaticPinState):

        '''
        if type(state) is not enums.WriteStaticPinState:
            raise TypeError('Parameter state must be of type ' + str(enums.WriteStaticPinState))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        state_ctype = _visatype.ViUInt8(state.value)  # case S130
        error_code = self._library.niDigital_WriteStatic(vi_ctype, channel_list_ctype, state_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _error_message(self, error_code):
        r'''_error_message

        TBD

        Args:
            error_code (int):


        Returns:
            error_message (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niDigital_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)


class Session(_SessionBase):
    '''An NI-Digital Pattern Driver session'''

    def __init__(self, resource_name, id_query=False, reset_device=False, options={}):
        r'''An NI-Digital Pattern Driver session

        TBD

        Args:
            resource_name (str):

            id_query (bool):

            reset_device (bool):

            options (dict): Specifies the initial value of certain properties for the session. The
                syntax for **options** is a dictionary of properties with an assigned
                value. For example:

                { 'simulate': False }

                You do not have to specify a value for all the properties. If you do not
                specify a value for a property, the default value is used.

                Advanced Example:
                { 'simulate': True, 'driver_setup': { 'Model': '<model number>',  'BoardType': '<type>' } }

                +-------------------------+---------+
                | Property                | Default |
                +=========================+=========+
                | range_check             | True    |
                +-------------------------+---------+
                | query_instrument_status | False   |
                +-------------------------+---------+
                | cache                   | True    |
                +-------------------------+---------+
                | simulate                | False   |
                +-------------------------+---------+
                | record_value_coersions  | False   |
                +-------------------------+---------+
                | driver_setup            | {}      |
                +-------------------------+---------+


        Returns:
            new_vi (int):

        '''
        super(Session, self).__init__(repeated_capability_list=[], vi=None, library=None, encoding=None, freeze_it=False)
        options = _converters.convert_init_with_options_dictionary(options)
        self._library = _library_singleton.get()
        self._encoding = 'windows-1251'

        # Call specified init function
        self._vi = 0  # This must be set before calling _init_with_options().
        self._vi = self._init_with_options(resource_name, id_query, reset_device, options)

        self.tclk = nitclk.SessionReference(self._vi)

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("resource_name=" + pp.pformat(resource_name))
        param_list.append("reset_device=" + pp.pformat(reset_device))
        param_list.append("options=" + pp.pformat(options))
        self._param_list = ', '.join(param_list)

        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def initiate(self):
        '''initiate

        TBD

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        '''
        return _Burst(self)

    def close(self):
        '''close

        TBD

        Note:
        This method is not needed when using the session context manager
        '''
        try:
            self._close()
        except errors.DriverError:
            self._vi = 0
            raise
        self._vi = 0

    ''' These are code-generated '''

    @ivi_synchronized
    def abort(self):
        r'''abort

        TBD
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def abort_keep_alive(self):
        r'''abort_keep_alive

        TBD
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_AbortKeepAlive(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def commit(self):
        r'''commit

        TBD
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_Commit(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_time_set_period(self, time_set_name, period):
        r'''configure_time_set_period

        TBD

        Args:
            time_set_name (str):

            period (float in seconds or datetime.timedelta):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        period_ctype = _converters.convert_timedelta_to_seconds_real64(period)  # case S140
        error_code = self._library.niDigital_ConfigureTimeSetPeriod(vi_ctype, time_set_name_ctype, period_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def create_capture_waveform_from_file_digicapture(self, waveform_name, waveform_file_path):
        r'''create_capture_waveform_from_file_digicapture

        TBD

        Args:
            waveform_name (str):

            waveform_file_path (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        waveform_file_path_ctype = ctypes.create_string_buffer(waveform_file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_CreateCaptureWaveformFromFileDigicapture(vi_ctype, waveform_name_ctype, waveform_file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def create_source_waveform_from_file_tdms(self, waveform_name, waveform_file_path, write_waveform_data=True):
        r'''create_source_waveform_from_file_tdms

        TBD

        Args:
            waveform_name (str):

            waveform_file_path (str):

            write_waveform_data (bool):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        waveform_file_path_ctype = ctypes.create_string_buffer(waveform_file_path.encode(self._encoding))  # case C020
        write_waveform_data_ctype = _visatype.ViBoolean(write_waveform_data)  # case S150
        error_code = self._library.niDigital_CreateSourceWaveformFromFileTDMS(vi_ctype, waveform_name_ctype, waveform_file_path_ctype, write_waveform_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def create_time_set(self, name):
        r'''create_time_set

        TBD

        Args:
            name (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        name_ctype = ctypes.create_string_buffer(name.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_CreateTimeSet(vi_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def delete_all_time_sets(self):
        r'''delete_all_time_sets

        TBD
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_DeleteAllTimeSets(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _call_method_with_iterable(self, method, files):
        if files is None:
            return
        if isinstance(files, str):
            files = [files]
        for f in files:
            method(f)

    def load_specifications_levels_and_timing(self, specifications_file_paths=None, levels_file_paths=None, timing_file_paths=None):
        '''load_specifications_levels_and_timing

        Loads settings in specifications, levels, and timing sheets. These settings are not
        applied to the digital pattern instrument until apply_levels_and_timing is called.

        If the levels and timing sheets contains formulas, they are evaluated at load time.
        If the formulas refer to variables, the specifications sheets that define those
        variables must be loaded either first, or at the same time as the levels and timing sheets.

        Args:
            specifications_file_paths (str or iterable of str): Absolute file path of one or more specifications files.

            levels_file_paths (str or iterable of str): Absolute file path of one or more levels sheet files.

            timing_file_paths (str or iterable of str): Absolute file path of one or more timing sheet files.

        '''
        self._call_method_with_iterable(self._load_specifications, specifications_file_paths)
        self._call_method_with_iterable(self._load_levels, levels_file_paths)
        self._call_method_with_iterable(self._load_timing, timing_file_paths)

    @ivi_synchronized
    def self_test(self):
        '''self_test

        TBD
        '''
        code, msg = self._self_test()
        if code:
            raise errors.SelfTestError(code, msg)
        return None

    @ivi_synchronized
    def unload_specifications(self, file_paths):
        '''unload_specifications

        Unloads the given specifications sheets present in the previously loaded
        specifications files that you select.

        You must call load_specifications_levels_and_timing to reload the files with updated
        specifications values. You must then call apply_levels_and_timing in order to apply
        the levels and timing values that reference the updated specifications values.

        Args:
            file_paths (str or iterable of str): Absolute file path of one or more loaded specifications files.

        '''
        self._call_method_with_iterable(self._unload_specifications, file_paths)

    @ivi_synchronized
    def write_source_waveform_site_unique(self, waveform_name, waveform_data):
        '''write_source_waveform_site_unique

        TBD

        Args:
            waveform_name (str):

            waveform_data ({ site: data, site: data, ... }): Dictionary where each key is the site number and the value is array.array of unsigned int

        '''
        site_list = []
        # We assume all the entries are the same length (we'll check later) to make the array the correct size
        # Get an entry from the dictionary from https://stackoverflow.com/questions/30362391/how-do-you-find-the-first-key-in-a-dictionary
        if len(waveform_data) == 0:
            actual_samples_per_waveform = 0
        else:
            actual_samples_per_waveform = len(waveform_data[next(iter(waveform_data))])
        data = array.array('L', [0] * (len(waveform_data) * actual_samples_per_waveform))
        mv = memoryview(data)

        i = 0
        for site in waveform_data:
            if len(waveform_data[site]) != actual_samples_per_waveform:
                raise ValueError('Mismatched length of waveforms. All must be the same length.')
            # Check the type by using string comparison so that we don't import numpy unnecessarily.
            if str(type(waveform_data[site])).find("'numpy.ndarray'") != -1:
                import numpy
                if waveform_data[site].dtype == numpy.uint32:
                    wfm = array.array('L', waveform_data[site])
                else:
                    raise TypeError("Unsupported dtype for waveform_data array element type. Is {0}, expected {1}".format(waveform_data[site].dtype, numpy.int32))

            elif isinstance(waveform_data[site], array.array):
                if waveform_data[site].typecode == 'L':
                    wfm = waveform_data[site]
                else:
                    raise TypeError('Wrong waveform_data array element type. Must be unsigned 32 bit int ("L"), was {}'.format(waveform_data[site].typecode))

            elif isinstance(waveform_data[site], list):
                wfm = array.array('L', waveform_data[site])

            else:
                raise TypeError('Unknown array type: {}'.format(type(waveform_data[site])))

            site_list.append(site)

            start = i * actual_samples_per_waveform
            end = start + actual_samples_per_waveform
            mv[start:end] = wfm

            i += 1

        self.sites[site_list]._write_source_waveform_site_unique_u32(waveform_name, len(waveform_data), actual_samples_per_waveform, data)

    @ivi_synchronized
    def get_channel_name_from_string(self, index):
        r'''get_channel_name_from_string

        TBD

        Args:
            index (str):


        Returns:
            name (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        index_ctype = ctypes.create_string_buffer(index.encode(self._encoding))  # case C020
        name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        name_ctype = None  # case C050
        error_code = self._library.niDigital_GetChannelNameFromString(vi_ctype, index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        name_ctype = (_visatype.ViChar * name_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetChannelNameFromString(vi_ctype, index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return name_ctype.value.decode(self._encoding)

    @ivi_synchronized
    def get_pattern_pin_names(self, start_label):
        r'''get_pattern_pin_names

        TBD

        Args:
            start_label (str):


        Returns:
            pin_list (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        start_label_ctype = ctypes.create_string_buffer(start_label.encode(self._encoding))  # case C020
        pin_list_buffer_size_ctype = _visatype.ViInt32()  # case S170
        pin_list_ctype = None  # case C050
        error_code = self._library.niDigital_GetPatternPinList(vi_ctype, start_label_ctype, pin_list_buffer_size_ctype, pin_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        pin_list_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        pin_list_ctype = (_visatype.ViChar * pin_list_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetPatternPinList(vi_ctype, start_label_ctype, pin_list_buffer_size_ctype, pin_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_comma_separated_string_to_list(pin_list_ctype.value.decode(self._encoding))

    @ivi_synchronized
    def get_time_set_period(self, time_set_name):
        r'''get_time_set_period

        TBD

        Args:
            time_set_name (str):


        Returns:
            period (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        period_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDigital_GetTimeSetPeriod(vi_ctype, time_set_name_ctype, None if period_ctype is None else (ctypes.pointer(period_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(period_ctype.value)

    def _init_with_options(self, resource_name, id_query=False, reset_device=False, option_string=""):
        r'''_init_with_options

        TBD

        Args:
            resource_name (str):

            id_query (bool):

            reset_device (bool):

            option_string (dict):


        Returns:
            new_vi (int):

        '''
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(_converters.convert_init_with_options_dictionary(option_string).encode(self._encoding))  # case C040
        new_vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niDigital_InitWithOptions(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if new_vi_ctype is None else (ctypes.pointer(new_vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(new_vi_ctype.value)

    @ivi_synchronized
    def _initiate(self):
        r'''_initiate

        TBD
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_Initiate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def is_done(self):
        r'''is_done

        TBD

        Returns:
            done (bool):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        done_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDigital_IsDone(vi_ctype, None if done_ctype is None else (ctypes.pointer(done_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(done_ctype.value)

    @ivi_synchronized
    def _load_levels(self, file_path):
        r'''_load_levels

        TBD

        Args:
            file_path (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadLevels(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def load_pattern(self, file_path):
        r'''load_pattern

        TBD

        Args:
            file_path (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadPattern(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def load_pin_map(self, file_path):
        r'''load_pin_map

        TBD

        Args:
            file_path (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadPinMap(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _load_specifications(self, file_path):
        r'''_load_specifications

        TBD

        Args:
            file_path (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadSpecifications(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _load_timing(self, file_path):
        r'''_load_timing

        TBD

        Args:
            file_path (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadTiming(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def read_sequencer_flag(self, flag):
        r'''read_sequencer_flag

        TBD

        Args:
            flag (enums.SequencerFlag):


        Returns:
            value (bool):

        '''
        if type(flag) is not enums.SequencerFlag:
            raise TypeError('Parameter flag must be of type ' + str(enums.SequencerFlag))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        flag_ctype = ctypes.create_string_buffer(flag.value.encode(self._encoding))  # case C030
        value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDigital_ReadSequencerFlag(vi_ctype, flag_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(value_ctype.value)

    @ivi_synchronized
    def read_sequencer_register(self, reg):
        r'''read_sequencer_register

        TBD

        Args:
            reg (enums.SequencerRegister):


        Returns:
            value (int):

        '''
        if type(reg) is not enums.SequencerRegister:
            raise TypeError('Parameter reg must be of type ' + str(enums.SequencerRegister))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        reg_ctype = ctypes.create_string_buffer(reg.value.encode(self._encoding))  # case C030
        value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_ReadSequencerRegister(vi_ctype, reg_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    @ivi_synchronized
    def reset_device(self):
        r'''reset_device

        TBD
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_ResetDevice(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def self_calibrate(self):
        r'''self_calibrate

        TBD
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_SelfCalibrate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def send_software_edge_trigger(self, trigger, trigger_identifier):
        r'''send_software_edge_trigger

        Forces a particular edge-based trigger to occur regardless of how the
        specified trigger is configured. You can use this method as a software override.

        Args:
            trigger (enums.SoftwareTrigger): Trigger specifies the trigger you want to override.

                +----------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
                | Defined Values                   |                                                                                                                                 |
                +==================================+=================================================================================================================================+
                | SoftwareTrigger.START            | Overrides the Start trigger. You must specify an empty string in the trigger_identifier parameter.                              |
                +----------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
                | SoftwareTrigger.CONDITIONAL_JUMP | Specifies to route a conditional jump trigger. You must specify a conditional jump trigger in the trigger_identifier parameter. |
                +----------------------------------+---------------------------------------------------------------------------------------------------------------------------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            trigger_identifier (str): Trigger Identifier specifies the instance of the trigger you want to override.
                If trigger is specified as NIDIGITAL_VAL_START_TRIGGER, this parameter must be an empty string. If trigger is
                specified as NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER, allowed values are conditionalJumpTrigger0,
                conditionalJumpTrigger1, conditionalJumpTrigger2, and conditionalJumpTrigger3.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        if type(trigger) is not enums.SoftwareTrigger:
            raise TypeError('Parameter trigger must be of type ' + str(enums.SoftwareTrigger))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_ctype = _visatype.ViInt32(trigger.value)  # case S130
        trigger_identifier_ctype = ctypes.create_string_buffer(trigger_identifier.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_SendSoftwareEdgeTrigger(vi_ctype, trigger_ctype, trigger_identifier_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def unload_all_patterns(self, unload_keep_alive_pattern=False):
        r'''unload_all_patterns

        TBD

        Args:
            unload_keep_alive_pattern (bool):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        unload_keep_alive_pattern_ctype = _visatype.ViBoolean(unload_keep_alive_pattern)  # case S150
        error_code = self._library.niDigital_UnloadAllPatterns(vi_ctype, unload_keep_alive_pattern_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _unload_specifications(self, file_path):
        r'''_unload_specifications

        TBD

        Args:
            file_path (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_UnloadSpecifications(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def wait_until_done(self, timeout=datetime.timedelta(seconds=10.0)):
        r'''wait_until_done

        TBD

        Args:
            timeout (float in seconds or datetime.timedelta):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        error_code = self._library.niDigital_WaitUntilDone(vi_ctype, timeout_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def write_sequencer_flag(self, flag, value):
        r'''write_sequencer_flag

        TBD

        Args:
            flag (enums.SequencerFlag):

            value (bool):

        '''
        if type(flag) is not enums.SequencerFlag:
            raise TypeError('Parameter flag must be of type ' + str(enums.SequencerFlag))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        flag_ctype = ctypes.create_string_buffer(flag.value.encode(self._encoding))  # case C030
        value_ctype = _visatype.ViBoolean(value)  # case S150
        error_code = self._library.niDigital_WriteSequencerFlag(vi_ctype, flag_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def write_sequencer_register(self, reg, value):
        r'''write_sequencer_register

        TBD

        Args:
            reg (enums.SequencerRegister):

            value (int):

        '''
        if type(reg) is not enums.SequencerRegister:
            raise TypeError('Parameter reg must be of type ' + str(enums.SequencerRegister))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        reg_ctype = ctypes.create_string_buffer(reg.value.encode(self._encoding))  # case C030
        value_ctype = _visatype.ViInt32(value)  # case S150
        error_code = self._library.niDigital_WriteSequencerRegister(vi_ctype, reg_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def write_source_waveform_broadcast(self, waveform_name, waveform_data):
        r'''write_source_waveform_broadcast

        TBD

        Args:
            waveform_name (str):

            waveform_data (list of int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data is None else len(waveform_data))  # case S160
        waveform_data_ctype = get_ctypes_pointer_for_buffer(value=waveform_data, library_type=_visatype.ViUInt32)  # case B550
        error_code = self._library.niDigital_WriteSourceWaveformBroadcastU32(vi_ctype, waveform_name_ctype, waveform_size_ctype, waveform_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def write_source_waveform_data_from_file_tdms(self, waveform_name, waveform_file_path):
        r'''write_source_waveform_data_from_file_tdms

        TBD

        Args:
            waveform_name (str):

            waveform_file_path (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        waveform_file_path_ctype = ctypes.create_string_buffer(waveform_file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_WriteSourceWaveformDataFromFileTDMS(vi_ctype, waveform_name_ctype, waveform_file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self):
        r'''_close

        TBD
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def reset(self):
        r'''reset

        TBD
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _self_test(self):
        r'''_self_test

        TBD

        Returns:
            test_result (int):

            test_message (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        test_result_ctype = _visatype.ViInt16()  # case S220
        test_message_ctype = (_visatype.ViChar * 2048)()  # case C070
        error_code = self._library.niDigital_self_test(vi_ctype, None if test_result_ctype is None else (ctypes.pointer(test_result_ctype)), test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(test_result_ctype.value), test_message_ctype.value.decode(self._encoding)



