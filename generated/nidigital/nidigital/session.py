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
    def __init__(self, session, prefix):
        self._session = session
        self._prefix = prefix

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        rep_caps_list = _converters.convert_repeated_capabilities(repeated_capability, self._prefix)

        return _SessionBase(vi=self._session._vi, repeated_capability_list=rep_caps_list, library=self._session._library, encoding=self._session._encoding, freeze_it=True)


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
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].active_load_ioh = var
        var = session.channels[0,1].active_load_ioh
    '''
    active_load_iol = _attributes.AttributeViReal64(1150012)
    '''Type: float

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].active_load_iol = var
        var = session.channels[0,1].active_load_iol
    '''
    active_load_vcom = _attributes.AttributeViReal64(1150014)
    '''Type: float

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].active_load_vcom = var
        var = session.channels[0,1].active_load_vcom
    '''
    cache = _attributes.AttributeViBoolean(1050004)
    channel_count = _attributes.AttributeViInt32(1050203)
    clock_generator_frequency = _attributes.AttributeViReal64(1150073)
    '''Type: float

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].clock_generator_frequency = var
        var = session.channels[0,1].clock_generator_frequency
    '''
    clock_generator_is_running = _attributes.AttributeViBoolean(1150074)
    '''Type: bool

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        var = session.channels[0,1].clock_generator_is_running
    '''
    conditional_jump_trigger_terminal_name = _attributes.AttributeViString(1150040)
    '''Type: str

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        var = session.channels[0,1].conditional_jump_trigger_terminal_name
    '''
    conditional_jump_trigger_type = _attributes.AttributeViInt32(1150033)
    '''Type: int

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].conditional_jump_trigger_type = var
        var = session.channels[0,1].conditional_jump_trigger_type
    '''
    cycle_number_history_ram_trigger_cycle_number = _attributes.AttributeViInt64(1150044)
    digital_edge_conditional_jump_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DigitalEdge, 1150035)
    '''Type: enums.DigitalEdge

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].digital_edge_conditional_jump_trigger_edge = var
        var = session.channels[0,1].digital_edge_conditional_jump_trigger_edge
    '''
    digital_edge_conditional_jump_trigger_source = _attributes.AttributeViString(1150034)
    '''Type: str

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].digital_edge_conditional_jump_trigger_source = var
        var = session.channels[0,1].digital_edge_conditional_jump_trigger_source
    '''
    digital_edge_start_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DigitalEdge, 1150031)
    digital_edge_start_trigger_source = _attributes.AttributeViString(1150030)
    driver_setup = _attributes.AttributeViString(1050007)
    exported_conditional_jump_trigger_output_terminal = _attributes.AttributeViString(1150036)
    '''Type: str

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].exported_conditional_jump_trigger_output_terminal = var
        var = session.channels[0,1].exported_conditional_jump_trigger_output_terminal
    '''
    exported_pattern_opcode_event_output_terminal = _attributes.AttributeViString(1150041)
    '''Type: str

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].exported_pattern_opcode_event_output_terminal = var
        var = session.channels[0,1].exported_pattern_opcode_event_output_terminal
    '''
    exported_start_trigger_output_terminal = _attributes.AttributeViString(1150032)
    frequency_counter_measurement_time = _attributes.AttributeViReal64(1150069)
    '''Type: float

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].frequency_counter_measurement_time = var
        var = session.channels[0,1].frequency_counter_measurement_time
    '''
    group_capabilities = _attributes.AttributeViString(1050401)
    halt_on_keep_alive_opcode = _attributes.AttributeViBoolean(1150062)
    history_ram_buffer_size_per_site = _attributes.AttributeViInt64(1150079)
    history_ram_cycles_to_acquire = _attributes.AttributeViInt32(1150047)
    history_ram_max_samples_to_acquire_per_site = _attributes.AttributeViInt32(1150077)
    history_ram_number_of_samples_is_finite = _attributes.AttributeViBoolean(1150078)
    history_ram_pretrigger_samples = _attributes.AttributeViInt32(1150048)
    history_ram_trigger_type = _attributes.AttributeViInt32(1150043)
    instrument_firmware_revision = _attributes.AttributeViString(1050510)
    '''Type: str

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        var = session.channels[0,1].instrument_firmware_revision
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
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].mask_compare = var
        var = session.channels[0,1].mask_compare
    '''
    pattern_label_history_ram_trigger_cycle_offset = _attributes.AttributeViInt64(1150045)
    pattern_label_history_ram_trigger_label = _attributes.AttributeViString(1150046)
    pattern_label_history_ram_trigger_vector_offset = _attributes.AttributeViInt64(1150052)
    pattern_opcode_event_terminal_name = _attributes.AttributeViString(1150042)
    '''Type: str

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        var = session.channels[0,1].pattern_opcode_event_terminal_name
    '''
    ppmu_allow_extended_voltage_range = _attributes.AttributeViBoolean(1150076)
    '''Type: bool

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].ppmu_allow_extended_voltage_range = var
        var = session.channels[0,1].ppmu_allow_extended_voltage_range
    '''
    ppmu_aperture_time = _attributes.AttributeViReal64(1150037)
    '''Type: float

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].ppmu_aperture_time = var
        var = session.channels[0,1].ppmu_aperture_time
    '''
    ppmu_aperture_time_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ApertureTimeUnits, 1150038)
    '''Type: enums.ApertureTimeUnits

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].ppmu_aperture_time_units = var
        var = session.channels[0,1].ppmu_aperture_time_units
    '''
    ppmu_current_level = _attributes.AttributeViReal64(1150019)
    '''Type: float

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].ppmu_current_level = var
        var = session.channels[0,1].ppmu_current_level
    '''
    ppmu_current_level_range = _attributes.AttributeViReal64(1150020)
    '''Type: float

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].ppmu_current_level_range = var
        var = session.channels[0,1].ppmu_current_level_range
    '''
    ppmu_current_limit = _attributes.AttributeViReal64(1150054)
    '''Type: float

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].ppmu_current_limit = var
        var = session.channels[0,1].ppmu_current_limit
    '''
    ppmu_current_limit_behavior = _attributes.AttributeViInt32(1150064)
    '''Type: int

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].ppmu_current_limit_behavior = var
        var = session.channels[0,1].ppmu_current_limit_behavior
    '''
    ppmu_current_limit_range = _attributes.AttributeViReal64(1150017)
    '''Type: float

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].ppmu_current_limit_range = var
        var = session.channels[0,1].ppmu_current_limit_range
    '''
    ppmu_current_limit_supported = _attributes.AttributeViBoolean(1150055)
    '''Type: bool

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        var = session.channels[0,1].ppmu_current_limit_supported
    '''
    ppmu_output_function = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PPMUOutputFunction, 1150015)
    '''Type: enums.PPMUOutputFunction

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].ppmu_output_function = var
        var = session.channels[0,1].ppmu_output_function
    '''
    ppmu_voltage_level = _attributes.AttributeViReal64(1150016)
    '''Type: float

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].ppmu_voltage_level = var
        var = session.channels[0,1].ppmu_voltage_level
    '''
    ppmu_voltage_limit_high = _attributes.AttributeViReal64(1150022)
    '''Type: float

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].ppmu_voltage_limit_high = var
        var = session.channels[0,1].ppmu_voltage_limit_high
    '''
    ppmu_voltage_limit_low = _attributes.AttributeViReal64(1150021)
    '''Type: float

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].ppmu_voltage_limit_low = var
        var = session.channels[0,1].ppmu_voltage_limit_low
    '''
    query_instrument_status = _attributes.AttributeViBoolean(1050003)
    range_check = _attributes.AttributeViBoolean(1050002)
    record_coercions = _attributes.AttributeViBoolean(1050006)
    selected_function = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.SelectedFunction, 1150004)
    '''Type: enums.SelectedFunction

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].selected_function = var
        var = session.channels[0,1].selected_function
    '''
    sequencer_flag_terminal_name = _attributes.AttributeViString(1150059)
    serial_number = _attributes.AttributeViString(1150001)
    simulate = _attributes.AttributeViBoolean(1050005)
    specific_driver_class_spec_major_version = _attributes.AttributeViInt32(1050515)
    specific_driver_class_spec_minor_version = _attributes.AttributeViInt32(1050516)
    specific_driver_description = _attributes.AttributeViString(1050514)
    specific_driver_prefix = _attributes.AttributeViString(1050302)
    specific_driver_revision = _attributes.AttributeViString(1050551)
    specific_driver_vendor = _attributes.AttributeViString(1050513)
    start_label = _attributes.AttributeViString(1150023)
    start_trigger_terminal_name = _attributes.AttributeViString(1150039)
    start_trigger_type = _attributes.AttributeViInt32(1150029)
    supported_instrument_models = _attributes.AttributeViString(1050327)
    tdr_endpoint_termination = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TDREndpointTermination, 1150081)
    tdr_offset = _attributes.AttributeViReal64(1150051)
    '''Type: float

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].tdr_offset = var
        var = session.channels[0,1].tdr_offset
    '''
    termination_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TerminationMode, 1150006)
    '''Type: enums.TerminationMode

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].termination_mode = var
        var = session.channels[0,1].termination_mode
    '''
    timing_absolute_delay = _attributes.AttributeViReal64(1150072)
    timing_absolute_delay_enabled = _attributes.AttributeViBoolean(1150071)
    vih = _attributes.AttributeViReal64(1150008)
    '''Type: float

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].vih = var
        var = session.channels[0,1].vih
    '''
    vil = _attributes.AttributeViReal64(1150007)
    '''Type: float

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].vil = var
        var = session.channels[0,1].vil
    '''
    voh = _attributes.AttributeViReal64(1150010)
    '''Type: float

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].voh = var
        var = session.channels[0,1].voh
    '''
    vol = _attributes.AttributeViReal64(1150009)
    '''Type: float

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].vol = var
        var = session.channels[0,1].vol
    '''
    vterm = _attributes.AttributeViReal64(1150011)
    '''Type: float

    Tip:
    This property can use repeated capabilities (channels). If set or get directly on the
    nidigital.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nidigital.Session repeated capabilities container, and calling set/get value on the result.:

        session.channels[0,1].vterm = var
        var = session.channels[0,1].vterm
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
    def apply_tdr_offsets(self, offsets):
        r'''apply_tdr_offsets

        TBD

        Tip:
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1].apply_tdr_offsets(offsets)

        Args:
            offsets (list of float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        num_offsets_ctype = _visatype.ViInt32(0 if offsets is None else len(offsets))  # case S160
        offsets_ctype = get_ctypes_pointer_for_buffer(value=offsets, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niDigital_ApplyTDROffsets(vi_ctype, channel_list_ctype, num_offsets_ctype, offsets_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def clock_generator_abort(self):
        r'''clock_generator_abort

        TBD

        Tip:
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1].clock_generator_abort()
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_ClockGenerator_Abort(vi_ctype, channel_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def clock_generator_generate_clock(self, frequency, select_digital_function):
        r'''clock_generator_generate_clock

        TBD

        Tip:
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1].clock_generator_generate_clock(frequency, select_digital_function)

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
    def clock_generator_initiate(self):
        r'''clock_generator_initiate

        TBD

        Tip:
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1].clock_generator_initiate()
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_ClockGenerator_Initiate(vi_ctype, channel_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_active_load_levels(self, iol, ioh, vcom):
        r'''configure_active_load_levels

        TBD

        Tip:
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1].configure_active_load_levels(iol, ioh, vcom)

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
    def configure_time_set_compare_edges_strobe(self, time_set, strobe_edge):
        r'''configure_time_set_compare_edges_strobe

        TBD

        Tip:
        This method requires repeated capabilities (pins). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.pins[0,1].configure_time_set_compare_edges_strobe(time_set, strobe_edge)

        Args:
            time_set (str):

            strobe_edge (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_ctype = ctypes.create_string_buffer(time_set.encode(self._encoding))  # case C020
        strobe_edge_ctype = _visatype.ViReal64(strobe_edge)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetCompareEdgesStrobe(vi_ctype, pin_list_ctype, time_set_ctype, strobe_edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_time_set_compare_edges_strobe2x(self, time_set, strobe_edge, strobe2_edge):
        r'''configure_time_set_compare_edges_strobe2x

        TBD

        Tip:
        This method requires repeated capabilities (pins). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.pins[0,1].configure_time_set_compare_edges_strobe2x(time_set, strobe_edge, strobe2_edge)

        Args:
            time_set (str):

            strobe_edge (float):

            strobe2_edge (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_ctype = ctypes.create_string_buffer(time_set.encode(self._encoding))  # case C020
        strobe_edge_ctype = _visatype.ViReal64(strobe_edge)  # case S150
        strobe2_edge_ctype = _visatype.ViReal64(strobe2_edge)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetCompareEdgesStrobe2x(vi_ctype, pin_list_ctype, time_set_ctype, strobe_edge_ctype, strobe2_edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_time_set_drive_edges(self, time_set, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge):
        r'''configure_time_set_drive_edges

        TBD

        Tip:
        This method requires repeated capabilities (pins). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.pins[0,1].configure_time_set_drive_edges(time_set, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge)

        Args:
            time_set (str):

            format (int):

            drive_on_edge (float):

            drive_data_edge (float):

            drive_return_edge (float):

            drive_off_edge (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_ctype = ctypes.create_string_buffer(time_set.encode(self._encoding))  # case C020
        format_ctype = _visatype.ViInt32(format)  # case S150
        drive_on_edge_ctype = _visatype.ViReal64(drive_on_edge)  # case S150
        drive_data_edge_ctype = _visatype.ViReal64(drive_data_edge)  # case S150
        drive_return_edge_ctype = _visatype.ViReal64(drive_return_edge)  # case S150
        drive_off_edge_ctype = _visatype.ViReal64(drive_off_edge)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetDriveEdges(vi_ctype, pin_list_ctype, time_set_ctype, format_ctype, drive_on_edge_ctype, drive_data_edge_ctype, drive_return_edge_ctype, drive_off_edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_time_set_drive_edges2x(self, time_set, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge):
        r'''configure_time_set_drive_edges2x

        TBD

        Tip:
        This method requires repeated capabilities (pins). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.pins[0,1].configure_time_set_drive_edges2x(time_set, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge)

        Args:
            time_set (str):

            format (int):

            drive_on_edge (float):

            drive_data_edge (float):

            drive_return_edge (float):

            drive_off_edge (float):

            drive_data2_edge (float):

            drive_return2_edge (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_ctype = ctypes.create_string_buffer(time_set.encode(self._encoding))  # case C020
        format_ctype = _visatype.ViInt32(format)  # case S150
        drive_on_edge_ctype = _visatype.ViReal64(drive_on_edge)  # case S150
        drive_data_edge_ctype = _visatype.ViReal64(drive_data_edge)  # case S150
        drive_return_edge_ctype = _visatype.ViReal64(drive_return_edge)  # case S150
        drive_off_edge_ctype = _visatype.ViReal64(drive_off_edge)  # case S150
        drive_data2_edge_ctype = _visatype.ViReal64(drive_data2_edge)  # case S150
        drive_return2_edge_ctype = _visatype.ViReal64(drive_return2_edge)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetDriveEdges2x(vi_ctype, pin_list_ctype, time_set_ctype, format_ctype, drive_on_edge_ctype, drive_data_edge_ctype, drive_return_edge_ctype, drive_off_edge_ctype, drive_data2_edge_ctype, drive_return2_edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_time_set_drive_format(self, time_set, drive_format):
        r'''configure_time_set_drive_format

        TBD

        Tip:
        This method requires repeated capabilities (pins). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.pins[0,1].configure_time_set_drive_format(time_set, drive_format)

        Args:
            time_set (str):

            drive_format (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_ctype = ctypes.create_string_buffer(time_set.encode(self._encoding))  # case C020
        drive_format_ctype = _visatype.ViInt32(drive_format)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetDriveFormat(vi_ctype, pin_list_ctype, time_set_ctype, drive_format_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_time_set_edge(self, time_set, edge, time):
        r'''configure_time_set_edge

        TBD

        Tip:
        This method requires repeated capabilities (pins). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.pins[0,1].configure_time_set_edge(time_set, edge, time)

        Args:
            time_set (str):

            edge (int):

            time (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_ctype = ctypes.create_string_buffer(time_set.encode(self._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge)  # case S150
        time_ctype = _visatype.ViReal64(time)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetEdge(vi_ctype, pin_list_ctype, time_set_ctype, edge_ctype, time_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_time_set_edge_multiplier(self, time_set, edge_multiplier):
        r'''configure_time_set_edge_multiplier

        TBD

        Tip:
        This method requires repeated capabilities (pins). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.pins[0,1].configure_time_set_edge_multiplier(time_set, edge_multiplier)

        Args:
            time_set (str):

            edge_multiplier (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_ctype = ctypes.create_string_buffer(time_set.encode(self._encoding))  # case C020
        edge_multiplier_ctype = _visatype.ViInt32(edge_multiplier)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetEdgeMultiplier(vi_ctype, pin_list_ctype, time_set_ctype, edge_multiplier_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_voltage_levels(self, vil, vih, vol, voh, vterm):
        r'''configure_voltage_levels

        TBD

        Tip:
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1].configure_voltage_levels(vil, vih, vol, voh, vterm)

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
        This method requires repeated capabilities (pins). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.pins[0,1].create_capture_waveform_parallel(waveform_name)

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
        This method requires repeated capabilities (pins). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.pins[0,1].create_capture_waveform_serial(waveform_name, sample_width, bit_order)

        Args:
            waveform_name (str):

            sample_width (int):

            bit_order (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        sample_width_ctype = _visatype.ViUInt32(sample_width)  # case S150
        bit_order_ctype = _visatype.ViInt32(bit_order)  # case S150
        error_code = self._library.niDigital_CreateCaptureWaveformSerial(vi_ctype, pin_list_ctype, waveform_name_ctype, sample_width_ctype, bit_order_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def create_source_waveform_parallel(self, waveform_name, data_mapping):
        r'''create_source_waveform_parallel

        TBD

        Tip:
        This method requires repeated capabilities (pins). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.pins[0,1].create_source_waveform_parallel(waveform_name, data_mapping)

        Args:
            waveform_name (str):

            data_mapping (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        data_mapping_ctype = _visatype.ViInt32(data_mapping)  # case S150
        error_code = self._library.niDigital_CreateSourceWaveformParallel(vi_ctype, pin_list_ctype, waveform_name_ctype, data_mapping_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def create_source_waveform_serial(self, waveform_name, data_mapping, sample_width, bit_order):
        r'''create_source_waveform_serial

        TBD

        Tip:
        This method requires repeated capabilities (pins). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.pins[0,1].create_source_waveform_serial(waveform_name, data_mapping, sample_width, bit_order)

        Args:
            waveform_name (str):

            data_mapping (int):

            sample_width (int):

            bit_order (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        data_mapping_ctype = _visatype.ViInt32(data_mapping)  # case S150
        sample_width_ctype = _visatype.ViUInt32(sample_width)  # case S150
        bit_order_ctype = _visatype.ViInt32(bit_order)  # case S150
        error_code = self._library.niDigital_CreateSourceWaveformSerial(vi_ctype, pin_list_ctype, waveform_name_ctype, data_mapping_ctype, sample_width_ctype, bit_order_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def fetch_history_ram_cycle_information(self, site, position, samples_to_read):
        '''fetch_history_ram_cycle_information

        Returns the pattern information acquired for the specified cycles.

        If the pattern is using the edge multiplier feature, cycle numbers represent tester cycles, each of which may
        consist of multiple DUT cycles. When using pins with mixed edge multipliers, pins may return
        DigitalState.PIN_STATE_NOT_ACQUIRED for DUT cycles where those pins do not have edges defined.

        If pins are not specified, pin list from the pattern containing the start label is used. Call
        get_pattern_pin_list or get_pattern_pin_indexes with the start label to retrieve the pins
        associated with the pattern burst.

        Tip:
        This method requires repeated capabilities (pins). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.pins[0,1].fetch_history_ram_cycle_information(site, position, samples_to_read)

        Args:
            site (str): Site on which to retrieve History RAM data. Specify site as a string in the form of siteN,
                where N is the site number. The VI returns an error if more than one site is specified.

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
                -  **expected_pin_states** (list of list of enums.DigitalState) Pin states as expected by the loaded
                   pattern in the order specified in the pin list. Pins without defined edges in the specified DUT cycle
                   will have a value of DigitalState.PIN_STATE_NOT_ACQUIRED.
                   Length of the outer list will be equal to the value of edge multiplier for the given vector.
                   Length of the inner list will be equal to the number of pins requested.
                -  **actual_pin_states** (list of list of enums.DigitalState) Pin states acquired by History RAM in the
                   order specified in the pin list. Pins without defined edges in the specified DUT cycle will have a
                   value of DigitalState.PIN_STATE_NOT_ACQUIRED.
                   Length of the outer list will be equal to the value of edge multiplier for the given vector.
                   Length of the inner list will be equal to the number of pins requested.
                -  **per_pin_pass_fail** (list of list of bool) Pass fail information for pins in the order specified in
                   the pin list. Pins without defined edges in the specified DUT cycle will have a value of pass (True).
                   Length of the outer list will be equal to the value of edge multiplier for the given vector.
                   Length of the inner list will be equal to the number of pins requested.

        '''
        if position < 0:
            raise ValueError('position should be greater than or equal to 0.')

        if samples_to_read < -1:
            raise ValueError('samples_to_read should be greater than or equal to -1.')

        samples_available = self.get_history_ram_sample_count(site)
        if position >= samples_available:
            raise ValueError('position: Specified value = {0}, Maximum value = {1}.'.format(position, samples_available - 1))

        if samples_to_read == -1:
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

            pattern_index, time_set_index, vector_number, cycle_number, num_dut_cycles = self._fetch_history_ram_cycle_information(site, position)

            if pattern_index not in pattern_names:
                pattern_names[pattern_index] = self.get_pattern_name(pattern_index)
            pattern_name = pattern_names[pattern_index]

            if time_set_index not in time_set_names:
                time_set_names[time_set_index] = self.get_time_set_name(time_set_index)
            time_set_name = time_set_names[time_set_index]

            scan_cycle_number = self._fetch_history_ram_scan_cycle_number(site, position)

            vector_expected_pin_states = []
            vector_actual_pin_states = []
            vector_per_pin_pass_fail = []
            for dut_cycle_index in range(num_dut_cycles):
                cycle_expected_pin_states, cycle_actual_pin_states, cycle_per_pin_pass_fail = self._fetch_history_ram_cycle_pin_data(site, position, dut_cycle_index)
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
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1].get_pin_results_pin_information()

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
            pin_name = "" if pin_indexes[i] == -1 else self.get_pin_name(pin_indexes[i])
            channel_name = self.get_channel_name(channel_indexes[i])
            pin_infos.append(PinInfo(pin_name=pin_name, site_number=site_numbers[i], channel_name=channel_name))

        return pin_infos

    @ivi_synchronized
    def _fetch_history_ram_cycle_pin_data(self, site, sample_index, dut_cycle_index):
        r'''_fetch_history_ram_cycle_pin_data

        TBD

        Tip:
        This method requires repeated capabilities (pins). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.pins[0,1]._fetch_history_ram_cycle_pin_data(site, sample_index, dut_cycle_index)

        Args:
            site (str):

            sample_index (int):

            dut_cycle_index (int):


        Returns:
            expected_pin_states (list of enums.DigitalState):

            actual_pin_states (list of enums.DigitalState):

            per_pin_pass_fail (list of bool):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(self._encoding))  # case C020
        pin_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
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
        return [enums.DigitalState(expected_pin_states_ctype[i]) for i in range(pin_data_buffer_size_ctype.value)], [enums.DigitalState(actual_pin_states_ctype[i]) for i in range(pin_data_buffer_size_ctype.value)], [bool(per_pin_pass_fail_ctype[i]) for i in range(pin_data_buffer_size_ctype.value)]

    @ivi_synchronized
    def frequency_counter_measure_frequency(self):
        r'''frequency_counter_measure_frequency

        TBD

        Tip:
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1].frequency_counter_measure_frequency()

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
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1]._get_attribute_vi_boolean(property)

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
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1]._get_attribute_vi_int32(property)

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
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1]._get_attribute_vi_int64(property)

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
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1]._get_attribute_vi_real64(property)

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
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1]._get_attribute_vi_string(property)

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
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1].get_fail_count()

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
    def get_pin_name(self, pin_index):
        r'''get_pin_name

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
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1]._get_pin_results_pin_information()

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
    def get_time_set_drive_format(self, time_set):
        r'''get_time_set_drive_format

        TBD

        Tip:
        This method requires repeated capabilities (pins). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.pins[0,1].get_time_set_drive_format(time_set)

        Args:
            time_set (str):


        Returns:
            format (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_ctype = ctypes.create_string_buffer(time_set.encode(self._encoding))  # case C020
        format_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetTimeSetDriveFormat(vi_ctype, pin_ctype, time_set_ctype, None if format_ctype is None else (ctypes.pointer(format_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(format_ctype.value)

    @ivi_synchronized
    def get_time_set_edge(self, time_set, edge):
        r'''get_time_set_edge

        TBD

        Tip:
        This method requires repeated capabilities (pins). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.pins[0,1].get_time_set_edge(time_set, edge)

        Args:
            time_set (str):

            edge (int):


        Returns:
            time (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_ctype = ctypes.create_string_buffer(time_set.encode(self._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge)  # case S150
        time_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDigital_GetTimeSetEdge(vi_ctype, pin_ctype, time_set_ctype, edge_ctype, None if time_ctype is None else (ctypes.pointer(time_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(time_ctype.value)

    @ivi_synchronized
    def get_time_set_edge_multiplier(self, time_set):
        r'''get_time_set_edge_multiplier

        TBD

        Tip:
        This method requires repeated capabilities (pins). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.pins[0,1].get_time_set_edge_multiplier(time_set)

        Args:
            time_set (str):


        Returns:
            edge_multiplier (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_ctype = ctypes.create_string_buffer(time_set.encode(self._encoding))  # case C020
        edge_multiplier_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetTimeSetEdgeMultiplier(vi_ctype, pin_ctype, time_set_ctype, None if edge_multiplier_ctype is None else (ctypes.pointer(edge_multiplier_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(edge_multiplier_ctype.value)

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
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1].ppmu_measure(measurement_type)

        Args:
            measurement_type (int):


        Returns:
            measurements (list of float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        measurement_type_ctype = _visatype.ViInt32(measurement_type)  # case S150
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
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1].ppmu_source()
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
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1].read_static()

        Returns:
            data (list of int):

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
        return [int(data_ctype[i]) for i in range(buffer_size_ctype.value)]

    @ivi_synchronized
    def reset_attribute(self, attribute_id):
        r'''reset_attribute

        TBD

        Tip:
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1].reset_attribute(attribute_id)

        Args:
            attribute_id (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        error_code = self._library.niDigital_ResetAttribute(vi_ctype, channel_name_ctype, attribute_id_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _set_attribute_vi_boolean(self, attribute, value):
        r'''_set_attribute_vi_boolean

        TBD

        Tip:
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1]._set_attribute_vi_boolean(property, value)

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
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1]._set_attribute_vi_int32(property, value)

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
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1]._set_attribute_vi_int64(property, value)

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
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1]._set_attribute_vi_real64(property, value)

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
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1]._set_attribute_vi_string(property, value)

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
    def tdr(self, apply_offsets):
        r'''tdr

        TBD

        Tip:
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1].tdr(apply_offsets)

        Args:
            apply_offsets (bool):


        Returns:
            offsets (list of float):

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
        return [float(offsets_ctype[i]) for i in range(offsets_buffer_size_ctype.value)]

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
    def write_static(self, state):
        r'''write_static

        TBD

        Tip:
        This method requires repeated capabilities (channels). If called directly on the
        nidigital.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidigital.Session repeated capabilities container, and calling this method on the result.:

            session.channels[0,1].write_static(state)

        Args:
            state (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        state_ctype = _visatype.ViUInt8(state)  # case S150
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

        # Instantiate any repeated capability objects
        self.channels = _RepeatedCapabilities(self, '')
        self.pins = _RepeatedCapabilities(self, '')
        self.devices = _RepeatedCapabilities(self, '')
        self.pattern_opcode_events = _RepeatedCapabilities(self, 'patternOpcodeEvent')
        self.conditional_jump_triggers = _RepeatedCapabilities(self, 'conditionalJumpTrigger')

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
    def apply_levels_and_timing(self, site_list, levels_sheet, timing_sheet, initial_state_high_pins, initial_state_low_pins, initial_state_tristate_pins):
        r'''apply_levels_and_timing

        TBD

        Args:
            site_list (str):

            levels_sheet (str):

            timing_sheet (str):

            initial_state_high_pins (str):

            initial_state_low_pins (str):

            initial_state_tristate_pins (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C020
        levels_sheet_ctype = ctypes.create_string_buffer(levels_sheet.encode(self._encoding))  # case C020
        timing_sheet_ctype = ctypes.create_string_buffer(timing_sheet.encode(self._encoding))  # case C020
        initial_state_high_pins_ctype = ctypes.create_string_buffer(initial_state_high_pins.encode(self._encoding))  # case C020
        initial_state_low_pins_ctype = ctypes.create_string_buffer(initial_state_low_pins.encode(self._encoding))  # case C020
        initial_state_tristate_pins_ctype = ctypes.create_string_buffer(initial_state_tristate_pins.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_ApplyLevelsAndTiming(vi_ctype, site_list_ctype, levels_sheet_ctype, timing_sheet_ctype, initial_state_high_pins_ctype, initial_state_low_pins_ctype, initial_state_tristate_pins_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def burst_pattern(self, site_list, start_label, select_digital_function, wait_until_done, timeout):
        r'''burst_pattern

        TBD

        Args:
            site_list (str):

            start_label (str):

            select_digital_function (bool):

            wait_until_done (bool):

            timeout (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C020
        start_label_ctype = ctypes.create_string_buffer(start_label.encode(self._encoding))  # case C020
        select_digital_function_ctype = _visatype.ViBoolean(select_digital_function)  # case S150
        wait_until_done_ctype = _visatype.ViBoolean(wait_until_done)  # case S150
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        error_code = self._library.niDigital_BurstPattern(vi_ctype, site_list_ctype, start_label_ctype, select_digital_function_ctype, wait_until_done_ctype, timeout_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def clear_error(self):
        r'''clear_error

        TBD
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_ClearError(vi_ctype)
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
    def configure_pattern_burst_sites(self, site_list):
        r'''configure_pattern_burst_sites

        TBD

        Args:
            site_list (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_ConfigurePatternBurstSites(vi_ctype, site_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_time_set_period(self, time_set, period):
        r'''configure_time_set_period

        TBD

        Args:
            time_set (str):

            period (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        time_set_ctype = ctypes.create_string_buffer(time_set.encode(self._encoding))  # case C020
        period_ctype = _visatype.ViReal64(period)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetPeriod(vi_ctype, time_set_ctype, period_ctype)
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
    def create_source_waveform_from_file_tdms(self, waveform_name, waveform_file_path, write_waveform_data):
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
    def disable_sites(self, site_list):
        r'''disable_sites

        TBD

        Args:
            site_list (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_DisableSites(vi_ctype, site_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def enable_sites(self, site_list):
        r'''enable_sites

        TBD

        Args:
            site_list (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_EnableSites(vi_ctype, site_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _fetch_capture_waveform(self, site_list, waveform_name, samples_to_read, timeout):
        # This is slightly modified codegen from the function
        # We cannot use codegen without major modifications to the code generator
        # This function uses two 'ivi-dance' parameters and then multiplies them together - see
        # the (modified) line below
        # Also, we want to return the two sized that normally wouldn't be returned
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C020
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

    def fetch_capture_waveform(self, site_list, waveform_name, samples_to_read, timeout):
        '''fetch_capture_waveform

        Returns dictionary where each key is the site number and the value is array.array of unsigned int

        Args:
            site_list (str):

            waveform_name (str):

            samples_to_read (int):

            timeout (float or datetime.timedelta):


        Returns:
            waveform ({ site: data, site: data, ... }): Dictionary where each key is the site number and the value is array.array of unsigned int

        '''
        data, actual_num_waveforms, actual_samples_per_waveform = self._fetch_capture_waveform(site_list, waveform_name, samples_to_read, timeout)

        # Get the site list
        site_list = self.get_site_results_site_numbers(site_list, enums.SiteResult.CAPTURE_WAVEFORM)
        assert len(site_list) == actual_num_waveforms

        waveforms = {}

        mv = memoryview(data)

        for i in range(actual_num_waveforms):
            start = i * actual_samples_per_waveform
            end = start + actual_samples_per_waveform
            waveforms[site_list[i]] = mv[start:end]

        return waveforms

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
            # Check the type by using string comparison so that we don't import numpy unecessarilly.
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

            site_list.append('site' + str(site))

            start = i * actual_samples_per_waveform
            end = start + actual_samples_per_waveform
            mv[start:end] = wfm

            i += 1

        site_list_str = ','.join(site_list)

        self._write_source_waveform_site_unique_u32(site_list_str, waveform_name, len(waveform_data), actual_samples_per_waveform, data)

    @ivi_synchronized
    def _fetch_history_ram_cycle_information(self, site, sample_index):
        r'''_fetch_history_ram_cycle_information

        TBD

        Args:
            site (str):

            sample_index (int):


        Returns:
            pattern_index (int):

            time_set_index (int):

            vector_number (int):

            cycle_number (int):

            num_dut_cycles (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(self._encoding))  # case C020
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
    def _fetch_history_ram_scan_cycle_number(self, site, sample_index):
        r'''_fetch_history_ram_scan_cycle_number

        TBD

        Args:
            site (str):

            sample_index (int):


        Returns:
            scan_cycle_number (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(self._encoding))  # case C020
        sample_index_ctype = _visatype.ViInt64(sample_index)  # case S150
        scan_cycle_number_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niDigital_FetchHistoryRAMScanCycleNumber(vi_ctype, site_ctype, sample_index_ctype, None if scan_cycle_number_ctype is None else (ctypes.pointer(scan_cycle_number_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(scan_cycle_number_ctype.value)

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
    def get_history_ram_sample_count(self, site):
        r'''get_history_ram_sample_count

        TBD

        Args:
            site (str):


        Returns:
            sample_count (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(self._encoding))  # case C020
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
    def get_pattern_pin_indexes(self, start_label):
        r'''get_pattern_pin_indexes

        TBD

        Args:
            start_label (str):


        Returns:
            pin_indexes (list of int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        start_label_ctype = ctypes.create_string_buffer(start_label.encode(self._encoding))  # case C020
        pin_indexes_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        pin_indexes_ctype = None  # case B610
        actual_num_pins_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetPatternPinIndexes(vi_ctype, start_label_ctype, pin_indexes_buffer_size_ctype, pin_indexes_ctype, None if actual_num_pins_ctype is None else (ctypes.pointer(actual_num_pins_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        pin_indexes_buffer_size_ctype = _visatype.ViInt32(actual_num_pins_ctype.value)  # case S200
        pin_indexes_size = actual_num_pins_ctype.value  # case B620
        pin_indexes_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=pin_indexes_size)  # case B620
        error_code = self._library.niDigital_GetPatternPinIndexes(vi_ctype, start_label_ctype, pin_indexes_buffer_size_ctype, pin_indexes_ctype, None if actual_num_pins_ctype is None else (ctypes.pointer(actual_num_pins_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(pin_indexes_ctype[i]) for i in range(pin_indexes_buffer_size_ctype.value)]

    @ivi_synchronized
    def get_pattern_pin_list(self, start_label):
        r'''get_pattern_pin_list

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
        return pin_list_ctype.value.decode(self._encoding)

    @ivi_synchronized
    def get_site_pass_fail(self, site_list):
        r'''get_site_pass_fail

        TBD

        Args:
            site_list (str):


        Returns:
            pass_fail (list of bool):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C020
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
    def get_site_results_site_numbers(self, site_list, site_result_type):
        r'''get_site_results_site_numbers

        TBD

        Args:
            site_list (str):

            site_result_type (enums.SiteResult):


        Returns:
            site_numbers (list of int):

        '''
        if type(site_result_type) is not enums.SiteResult:
            raise TypeError('Parameter site_result_type must be of type ' + str(enums.SiteResult))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C020
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
    def get_time_set_period(self, time_set):
        r'''get_time_set_period

        TBD

        Args:
            time_set (str):


        Returns:
            period (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        time_set_ctype = ctypes.create_string_buffer(time_set.encode(self._encoding))  # case C020
        period_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDigital_GetTimeSetPeriod(vi_ctype, time_set_ctype, None if period_ctype is None else (ctypes.pointer(period_ctype)))
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
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
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
    def is_site_enabled(self, site):
        r'''is_site_enabled

        TBD

        Args:
            site (str):


        Returns:
            enable (bool):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(self._encoding))  # case C020
        enable_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDigital_IsSiteEnabled(vi_ctype, site_ctype, None if enable_ctype is None else (ctypes.pointer(enable_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(enable_ctype.value)

    @ivi_synchronized
    def load_levels(self, levels_file_path):
        r'''load_levels

        TBD

        Args:
            levels_file_path (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        levels_file_path_ctype = ctypes.create_string_buffer(levels_file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadLevels(vi_ctype, levels_file_path_ctype)
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
    def load_pin_map(self, pin_map_file_path):
        r'''load_pin_map

        TBD

        Args:
            pin_map_file_path (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_map_file_path_ctype = ctypes.create_string_buffer(pin_map_file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadPinMap(vi_ctype, pin_map_file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def load_specifications(self, specifications_file_path):
        r'''load_specifications

        TBD

        Args:
            specifications_file_path (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        specifications_file_path_ctype = ctypes.create_string_buffer(specifications_file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadSpecifications(vi_ctype, specifications_file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def load_timing(self, timing_file_path):
        r'''load_timing

        TBD

        Args:
            timing_file_path (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        timing_file_path_ctype = ctypes.create_string_buffer(timing_file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadTiming(vi_ctype, timing_file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def read_sequencer_flag(self, flag):
        r'''read_sequencer_flag

        TBD

        Args:
            flag (str):


        Returns:
            value (bool):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        flag_ctype = ctypes.create_string_buffer(flag.encode(self._encoding))  # case C020
        value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDigital_ReadSequencerFlag(vi_ctype, flag_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(value_ctype.value)

    @ivi_synchronized
    def read_sequencer_register(self, reg):
        r'''read_sequencer_register

        TBD

        Args:
            reg (str):


        Returns:
            value (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        reg_ctype = ctypes.create_string_buffer(reg.encode(self._encoding))  # case C020
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

        TBD

        Args:
            trigger (int):

            trigger_identifier (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_ctype = _visatype.ViInt32(trigger)  # case S150
        trigger_identifier_ctype = ctypes.create_string_buffer(trigger_identifier.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_SendSoftwareEdgeTrigger(vi_ctype, trigger_ctype, trigger_identifier_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def unload_all_patterns(self, unload_keep_alive_pattern):
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
    def unload_specifications(self, specifications_file_path):
        r'''unload_specifications

        TBD

        Args:
            specifications_file_path (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        specifications_file_path_ctype = ctypes.create_string_buffer(specifications_file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_UnloadSpecifications(vi_ctype, specifications_file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def wait_until_done(self, timeout):
        r'''wait_until_done

        TBD

        Args:
            timeout (float):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        error_code = self._library.niDigital_WaitUntilDone(vi_ctype, timeout_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def write_sequencer_flag(self, flag, value):
        r'''write_sequencer_flag

        TBD

        Args:
            flag (str):

            value (bool):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        flag_ctype = ctypes.create_string_buffer(flag.encode(self._encoding))  # case C020
        value_ctype = _visatype.ViBoolean(value)  # case S150
        error_code = self._library.niDigital_WriteSequencerFlag(vi_ctype, flag_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def write_sequencer_register(self, reg, value):
        r'''write_sequencer_register

        TBD

        Args:
            reg (str):

            value (int):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        reg_ctype = ctypes.create_string_buffer(reg.encode(self._encoding))  # case C020
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

    @ivi_synchronized
    def _write_source_waveform_site_unique_u32(self, site_list, waveform_name, num_waveforms, samples_per_waveform, waveform_data):
        r'''_write_source_waveform_site_unique_u32

        TBD

        Args:
            site_list (str):

            waveform_name (str):

            num_waveforms (int):

            samples_per_waveform (int):

            waveform_data (array.array("L")):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C020
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        num_waveforms_ctype = _visatype.ViInt32(num_waveforms)  # case S150
        samples_per_waveform_ctype = _visatype.ViInt32(samples_per_waveform)  # case S150
        waveform_data_array = get_ctypes_and_array(value=waveform_data, array_type="L")  # case B550
        waveform_data_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_visatype.ViUInt32)  # case B550
        error_code = self._library.niDigital_WriteSourceWaveformSiteUniqueU32(vi_ctype, site_list_ctype, waveform_name_ctype, num_waveforms_ctype, samples_per_waveform_ctype, waveform_data_ctype)
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



