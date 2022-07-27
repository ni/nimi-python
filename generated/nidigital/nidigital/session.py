# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
import ctypes
# Used by @ivi_synchronized
from functools import wraps

import nidigital._attributes as _attributes
import nidigital._converters as _converters
import nidigital._library_singleton as _library_singleton
import nidigital._visatype as _visatype
import nidigital.enums as enums
import nidigital.errors as errors

import nidigital.history_ram_cycle_information as history_ram_cycle_information  # noqa: F401

import hightime
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

        return _SessionBase(
            vi=self._session._vi,
            repeated_capability_list=complete_rep_cap_list,
            all_channels_in_session=self._session._all_channels_in_session,
            library=self._session._library,
            encoding=self._session._encoding,
            freeze_it=True
        )


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

    Specifies the current that the DUT sources to the active load while outputting a voltage above VCOM.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].active_load_ioh`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.active_load_ioh`
    '''
    active_load_iol = _attributes.AttributeViReal64(1150012)
    '''Type: float

    Specifies the current that the DUT sinks from the active load while outputting a voltage below VCOM.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].active_load_iol`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.active_load_iol`
    '''
    active_load_vcom = _attributes.AttributeViReal64(1150014)
    '''Type: float

    Specifies the voltage level at which the active load circuit switches between sourcing current and sinking current.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].active_load_vcom`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.active_load_vcom`
    '''
    cache = _attributes.AttributeViBoolean(1050004)
    '''Type: bool

    Specifies whether to cache the value of properties. When caching is enabled, the instrument driver keeps track of the current instrument settings and avoids sending redundant commands to the instrument. This significantly increases execution speed. Caching is always enabled in the driver, regardless of the value of this property.
    '''
    channel_count = _attributes.AttributeViInt32(1050203)
    '''Type: int

    Returns the number of channels that the specific digital pattern instrument driver supports.
    '''
    clock_generator_frequency = _attributes.AttributeViReal64(1150073)
    '''Type: float

    Specifies the frequency for the clock generator.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].clock_generator_frequency`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.clock_generator_frequency`
    '''
    clock_generator_is_running = _attributes.AttributeViBoolean(1150074)
    '''Type: bool

    Indicates whether the clock generator is running.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].clock_generator_is_running`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.clock_generator_is_running`
    '''
    conditional_jump_trigger_terminal_name = _attributes.AttributeViString(1150040)
    '''Type: str

    Specifies the terminal name from which the exported conditional jump trigger signal may be routed to other instruments through the PXI trigger bus. You can use this signal to trigger other instruments when the conditional jump trigger instance asserts on the digital pattern instrument.

    Tip:
    This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

    Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].conditional_jump_trigger_terminal_name`

    To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.conditional_jump_trigger_terminal_name`
    '''
    conditional_jump_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1150033)
    '''Type: enums.TriggerType

    Disables the conditional jump trigger or configures it for either hardware triggering or software triggering.  The default value is TriggerType.NONE.

    +--------------------------+------------------------------------------------------------------+
    | Valid Values:            |                                                                  |
    +==========================+==================================================================+
    | TriggerType.NONE         | Disables the conditional jump trigger.                           |
    +--------------------------+------------------------------------------------------------------+
    | TriggerType.DIGITAL_EDGE | Configures the conditional jump trigger for hardware triggering. |
    +--------------------------+------------------------------------------------------------------+
    | TriggerType.SOFTWARE     | Configures the conditional jump trigger for software triggering. |
    +--------------------------+------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

    Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].conditional_jump_trigger_type`

    To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.conditional_jump_trigger_type`
    '''
    cycle_number_history_ram_trigger_cycle_number = _attributes.AttributeViInt64(1150044)
    '''Type: int

    Specifies the cycle number on which History RAM starts acquiring pattern information when configured for a cycle number trigger.
    '''
    digital_edge_conditional_jump_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DigitalEdge, 1150035)
    '''Type: enums.DigitalEdge

    Configures the active edge of the incoming trigger signal for the conditional jump trigger instance. The default value is DigitalEdge.RISING.

    +---------------------+---------------------------------------------------------------+
    | Valid Values:       |                                                               |
    +=====================+===============================================================+
    | DigitalEdge.RISING  | Specifies the signal transition from low level to high level. |
    +---------------------+---------------------------------------------------------------+
    | DigitalEdge.FALLING | Specifies the signal transition from high level to low level. |
    +---------------------+---------------------------------------------------------------+

    Tip:
    This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

    Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].digital_edge_conditional_jump_trigger_edge`

    To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.digital_edge_conditional_jump_trigger_edge`
    '''
    digital_edge_conditional_jump_trigger_source = _attributes.AttributeViString(1150034)
    '''Type: str

    Configures the digital trigger source terminal for a conditional jump trigger instance. The PXIe-6570/6571 supports triggering through the PXI trigger bus. You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line). For example, you can set the source terminal on Dev1 to be /Dev2/ConditionalJumpTrigger0. The default value is VI_NULL.

    +----------------------------------------------+
    | Valid Values:                                |
    +==============================================+
    | String identifier to any valid terminal name |
    +----------------------------------------------+

    Tip:
    This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

    Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].digital_edge_conditional_jump_trigger_source`

    To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.digital_edge_conditional_jump_trigger_source`
    '''
    digital_edge_rio_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DigitalEdge, 1150088)
    '''Type: enums.DigitalEdge

    Configures the active edge of the incoming trigger signal for the RIO trigger instance. The default value is DigitalEdge.RISING.

    +---------------------+---------------------------------------------------------------+
    | Valid Values:       |                                                               |
    +=====================+===============================================================+
    | DigitalEdge.RISING  | Specifies the signal transition from low level to high level. |
    +---------------------+---------------------------------------------------------------+
    | DigitalEdge.FALLING | Specifies the signal transition from high level to low level. |
    +---------------------+---------------------------------------------------------------+

    Tip:
    This property can be set/get on specific rio_triggers within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container rio_triggers to specify a subset.

    Example: :py:attr:`my_session.rio_triggers[ ... ].digital_edge_rio_trigger_edge`

    To set/get on all rio_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.digital_edge_rio_trigger_edge`
    '''
    digital_edge_rio_trigger_source = _attributes.AttributeViString(1150087)
    '''Type: str

    Configures the digital trigger source terminal for a RIO trigger instance. The PXIe-6570/6571 supports triggering through the PXI trigger bus. You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line). For example, you can set the source terminal on Dev1 to be /Dev2/RIOTrigger0. The default value is VI_NULL.

    +----------------------------------------------+
    | Valid Values:                                |
    +==============================================+
    | String identifier to any valid terminal name |
    +----------------------------------------------+

    Tip:
    This property can be set/get on specific rio_triggers within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container rio_triggers to specify a subset.

    Example: :py:attr:`my_session.rio_triggers[ ... ].digital_edge_rio_trigger_source`

    To set/get on all rio_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.digital_edge_rio_trigger_source`
    '''
    digital_edge_start_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DigitalEdge, 1150031)
    '''Type: enums.DigitalEdge

    Specifies the active edge for the Start trigger. This property is used when the start_trigger_type property is set to Digital Edge.

    +---------------------+-------------------------------------------------------------------------------+
    | Defined Values:     |                                                                               |
    +=====================+===============================================================================+
    | DigitalEdge.RISING  | Asserts the trigger when the signal transitions from low level to high level. |
    +---------------------+-------------------------------------------------------------------------------+
    | DigitalEdge.FALLING | Asserts the trigger when the signal transitions from high level to low level. |
    +---------------------+-------------------------------------------------------------------------------+
    '''
    digital_edge_start_trigger_source = _attributes.AttributeViString(1150030)
    '''Type: str

    Specifies the source terminal for the Start trigger. This property is used when the start_trigger_type property is set to Digital Edge. You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line). For example, you can set the source terminal on Dev1 to be /Dev2/StartTrigger.

    +-----------------+--------------------+
    | Defined Values: |                    |
    +=================+====================+
    | PXI_Trig0       | PXI trigger line 0 |
    +-----------------+--------------------+
    | PXI_Trig1       | PXI trigger line 1 |
    +-----------------+--------------------+
    | PXI_Trig2       | PXI trigger line 2 |
    +-----------------+--------------------+
    | PXI_Trig3       | PXI trigger line 3 |
    +-----------------+--------------------+
    | PXI_Trig4       | PXI trigger line 4 |
    +-----------------+--------------------+
    | PXI_Trig5       | PXI trigger line 5 |
    +-----------------+--------------------+
    | PXI_Trig6       | PXI trigger line 6 |
    +-----------------+--------------------+
    | PXI_Trig7       | PXI trigger line 7 |
    +-----------------+--------------------+
    '''
    driver_setup = _attributes.AttributeViString(1050007)
    '''Type: str

    This property returns initial values for NI-Digital Pattern Driver properties as a string.
    '''
    exported_conditional_jump_trigger_output_terminal = _attributes.AttributeViString(1150036)
    '''Type: str

    Specifies the terminal to output the exported signal of the specified instance of the conditional jump trigger. The default value is VI_NULL.

    +---------------+-------------------------+
    | Valid Values: |                         |
    +===============+=========================+
    | VI_NULL ("")  | Returns an empty string |
    +---------------+-------------------------+
    | PXI_Trig0     | PXI trigger line 0      |
    +---------------+-------------------------+
    | PXI_Trig1     | PXI trigger line 1      |
    +---------------+-------------------------+
    | PXI_Trig2     | PXI trigger line 2      |
    +---------------+-------------------------+
    | PXI_Trig3     | PXI trigger line 3      |
    +---------------+-------------------------+
    | PXI_Trig4     | PXI trigger line 4      |
    +---------------+-------------------------+
    | PXI_Trig5     | PXI trigger line 5      |
    +---------------+-------------------------+
    | PXI_Trig6     | PXI trigger line 6      |
    +---------------+-------------------------+
    | PXI_Trig7     | PXI trigger line 7      |
    +---------------+-------------------------+

    Tip:
    This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

    Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].exported_conditional_jump_trigger_output_terminal`

    To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.exported_conditional_jump_trigger_output_terminal`
    '''
    exported_pattern_opcode_event_output_terminal = _attributes.AttributeViString(1150041)
    '''Type: str

    Specifies the destination terminal for exporting the Pattern Opcode Event. Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

    +-----------------+--------------------+
    | Defined Values: |                    |
    +=================+====================+
    | PXI_Trig0       | PXI trigger line 0 |
    +-----------------+--------------------+
    | PXI_Trig1       | PXI trigger line 1 |
    +-----------------+--------------------+
    | PXI_Trig2       | PXI trigger line 2 |
    +-----------------+--------------------+
    | PXI_Trig3       | PXI trigger line 3 |
    +-----------------+--------------------+
    | PXI_Trig4       | PXI trigger line 4 |
    +-----------------+--------------------+
    | PXI_Trig5       | PXI trigger line 5 |
    +-----------------+--------------------+
    | PXI_Trig6       | PXI trigger line 6 |
    +-----------------+--------------------+
    | PXI_Trig7       | PXI trigger line 7 |
    +-----------------+--------------------+

    Tip:
    This property can be set/get on specific pattern_opcode_events within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container pattern_opcode_events to specify a subset.

    Example: :py:attr:`my_session.pattern_opcode_events[ ... ].exported_pattern_opcode_event_output_terminal`

    To set/get on all pattern_opcode_events, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.exported_pattern_opcode_event_output_terminal`
    '''
    exported_rio_event_output_terminal = _attributes.AttributeViString(1150090)
    '''Type: str

    Specifies the destination terminal for exporting the RIO Event. Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

    +-----------------+--------------------+
    | Defined Values: |                    |
    +=================+====================+
    | PXI_Trig0       | PXI trigger line 0 |
    +-----------------+--------------------+
    | PXI_Trig1       | PXI trigger line 1 |
    +-----------------+--------------------+
    | PXI_Trig2       | PXI trigger line 2 |
    +-----------------+--------------------+
    | PXI_Trig3       | PXI trigger line 3 |
    +-----------------+--------------------+
    | PXI_Trig4       | PXI trigger line 4 |
    +-----------------+--------------------+
    | PXI_Trig5       | PXI trigger line 5 |
    +-----------------+--------------------+
    | PXI_Trig6       | PXI trigger line 6 |
    +-----------------+--------------------+
    | PXI_Trig7       | PXI trigger line 7 |
    +-----------------+--------------------+

    Tip:
    This property can be set/get on specific rio_events within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container rio_events to specify a subset.

    Example: :py:attr:`my_session.rio_events[ ... ].exported_rio_event_output_terminal`

    To set/get on all rio_events, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.exported_rio_event_output_terminal`
    '''
    exported_start_trigger_output_terminal = _attributes.AttributeViString(1150032)
    '''Type: str

    Specifies the destination terminal for exporting the Start trigger. Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

    +----------------------+-----------------------------+
    | Defined Values:      |                             |
    +======================+=============================+
    | Do not export signal | The signal is not exported. |
    +----------------------+-----------------------------+
    | PXI_Trig0            | PXI trigger line 0          |
    +----------------------+-----------------------------+
    | PXI_Trig1            | PXI trigger line 1          |
    +----------------------+-----------------------------+
    | PXI_Trig2            | PXI trigger line 2          |
    +----------------------+-----------------------------+
    | PXI_Trig3            | PXI trigger line 3          |
    +----------------------+-----------------------------+
    | PXI_Trig4            | PXI trigger line 4          |
    +----------------------+-----------------------------+
    | PXI_Trig5            | PXI trigger line 5          |
    +----------------------+-----------------------------+
    | PXI_Trig6            | PXI trigger line 6          |
    +----------------------+-----------------------------+
    | PXI_Trig7            | PXI trigger line 7          |
    +----------------------+-----------------------------+
    '''
    frequency_counter_hysteresis_enabled = _attributes.AttributeViBoolean(1150085)
    '''Type: bool

    Specifies whether hysteresis is enabled for the frequency counters of the digital pattern instrument.
    '''
    frequency_counter_measurement_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.FrequencyMeasurementMode, 1150084)
    '''Type: enums.FrequencyMeasurementMode

    Determines how the frequency counters of the digital pattern instrument make measurements.

    +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Valid Values:                     |                                                                                                                                                                                                                                                                                                                                                                                       |
    +===================================+=======================================================================================================================================================================================================================================================================================================================================================================================+
    | FrequencyMeasurementMode.BANKED   | Each discrete frequency counter is mapped to specific channels and makes frequency measurements from only those channels. Use banked mode when you need access to the full measure frequency range of the instrument. **Note:** If you request frequency measurements from multiple channels within the same bank, the measurements are made in series for the channels in that bank. |
    +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | FrequencyMeasurementMode.PARALLEL | All discrete frequency counters make frequency measurements from all channels in parallel with one another. Use parallel mode to increase the speed of frequency measurements if you do not need access to the full measure frequency range of the instrument; in parallel mode, you can also add frequency_counter_hysteresis_enabled to reduce measurement noise.                   |
    +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    '''
    frequency_counter_measurement_time = _attributes.AttributeViReal64TimeDeltaSeconds(1150069)
    '''Type: float in seconds or datetime.timedelta

    Specifies the measurement time for the frequency counter.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].frequency_counter_measurement_time`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.frequency_counter_measurement_time`
    '''
    group_capabilities = _attributes.AttributeViString(1050401)
    '''Type: str

    Returns a string that contains a comma-separated list of class-extension groups that the driver implements.
    '''
    halt_on_keep_alive_opcode = _attributes.AttributeViBoolean(1150062)
    '''Type: bool

    Specifies whether keep_alive opcodes should behave like halt opcodes.
    '''
    history_ram_buffer_size_per_site = _attributes.AttributeViInt64(1150079)
    '''Type: int

    Specifies the size, in samples, of the host memory buffer. The default value is 32000.

    +---------------+
    | Valid Values: |
    +===============+
    | 0-INT64_MAX   |
    +---------------+
    '''
    history_ram_cycles_to_acquire = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.HistoryRAMCyclesToAcquire, 1150047)
    '''Type: enums.HistoryRAMCyclesToAcquire

    Configures which cycles History RAM acquires after the trigger conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretrigger samples for History RAM to 0.

    +----------------------------------+-----------------------------------------------------------------------------------+
    | Defined Values:                  |                                                                                   |
    +==================================+===================================================================================+
    | HistoryRAMCyclesToAcquire.FAILED | Only acquires cycles that fail a compare after the triggering conditions are met. |
    +----------------------------------+-----------------------------------------------------------------------------------+
    | HistoryRAMCyclesToAcquire.ALL    | Acquires all cycles after the triggering conditions are met.                      |
    +----------------------------------+-----------------------------------------------------------------------------------+
    '''
    history_ram_max_samples_to_acquire_per_site = _attributes.AttributeViInt32(1150077)
    '''Type: int

    Specifies the maximum number of History RAM samples to acquire per site. If the property is set to -1, it will acquire until the History RAM buffer is full.
    '''
    history_ram_number_of_samples_is_finite = _attributes.AttributeViBoolean(1150078)
    '''Type: bool

    Specifies whether the instrument acquires a finite number of History Ram samples or acquires continuously. The maximum number of samples that will be acquired when this property is set to True is determined by the instrument History RAM depth specification and the History RAM Max Samples to Acquire Per Site property. The default value is True.

    +---------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Valid Values: |                                                                                                                                                      |
    +===============+======================================================================================================================================================+
    | True          | Specifies that History RAM results will not stream into the host buffer until a History RAM fetch API is called.                                     |
    +---------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
    | False         | Specifies that History RAM results will automatically start streaming into a host buffer after a pattern is burst and the History RAM has triggered. |
    +---------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
    '''
    history_ram_pretrigger_samples = _attributes.AttributeViInt32(1150048)
    '''Type: int

    Specifies the number of samples to acquire before the trigger conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretrigger samples for History RAM to 0.
    '''
    history_ram_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.HistoryRAMTriggerType, 1150043)
    '''Type: enums.HistoryRAMTriggerType

    Specifies the type of trigger condition on which History RAM starts acquiring pattern information.

    +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
    | Defined Values:                     |                                                                                                                                     |
    +=====================================+=====================================================================================================================================+
    | HistoryRAMTriggerType.FIRST_FAILURE | Starts acquiring pattern information in History RAM on the first failed cycle in a pattern burst.                                   |
    +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
    | HistoryRAMTriggerType.CYCLE_NUMBER  | Starts acquiring pattern information in History RAM starting from a specified cycle number.                                         |
    +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
    | HistoryRAMTriggerType.PATTERN_LABEL | Starts acquiring pattern information in History RAM starting from a specified pattern label, augmented by vector and cycle offsets. |
    +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
    '''
    instrument_firmware_revision = _attributes.AttributeViString(1050510)
    '''Type: str

    Returns a string that contains the firmware revision information for the digital pattern instrument.

    Tip:
    This property can be set/get on specific instruments within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].instrument_firmware_revision`

    To set/get on all instruments, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.instrument_firmware_revision`
    '''
    instrument_manufacturer = _attributes.AttributeViString(1050511)
    '''Type: str

    Returns a string ("National Instruments") that contains the name of the manufacturer of the digital pattern instrument.
    '''
    instrument_model = _attributes.AttributeViString(1050512)
    '''Type: str

    Returns a string that contains the model number or name of the digital pattern instrument.
    '''
    interchange_check = _attributes.AttributeViBoolean(1050021)
    '''Type: bool

    This property is not supported.
    '''
    io_resource_descriptor = _attributes.AttributeViString(1050304)
    '''Type: str

    Returns a string that contains the resource descriptor that the NI-Digital Pattern Driver uses to identify the digital pattern instrument.
    '''
    is_keep_alive_active = _attributes.AttributeViBoolean(1150063)
    '''Type: bool

    Returns True if the digital pattern instrument is driving the keep alive pattern.
    '''
    logical_name = _attributes.AttributeViString(1050305)
    '''Type: str

    Returns a string containing the logical name that you specified when opening the current IVI session. This property is not supported.
    '''
    mask_compare = _attributes.AttributeViBoolean(1150060)
    '''Type: bool

    Specifies whether the pattern comparisons are masked or not. When set to True for a specified pin, failures on that pin will be masked.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].mask_compare`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.mask_compare`
    '''
    pattern_label_history_ram_trigger_cycle_offset = _attributes.AttributeViInt64(1150045)
    '''Type: int

    Specifies the number of cycles that follow the specified pattern label and vector offset, after which History RAM will start acquiring pattern information when configured for a pattern label trigger.
    '''
    pattern_label_history_ram_trigger_label = _attributes.AttributeViString(1150046)
    '''Type: str

    Specifies the pattern label, augmented by the vector and cycle offset, to determine the point where History RAM will start acquiring pattern information when configured for a pattern label trigger.
    '''
    pattern_label_history_ram_trigger_vector_offset = _attributes.AttributeViInt64(1150052)
    '''Type: int

    Specifies the number of vectors that follow the specified pattern label, after which History RAM will start acquiring pattern information when configured for a pattern label trigger.
    '''
    pattern_opcode_event_terminal_name = _attributes.AttributeViString(1150042)
    '''Type: str

    Specifies the terminal name for the output trigger signal of the specified instance of a Pattern Opcode Event. You can use this terminal name as an input signal source for another trigger.

    Tip:
    This property can be set/get on specific pattern_opcode_events within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container pattern_opcode_events to specify a subset.

    Example: :py:attr:`my_session.pattern_opcode_events[ ... ].pattern_opcode_event_terminal_name`

    To set/get on all pattern_opcode_events, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.pattern_opcode_event_terminal_name`
    '''
    ppmu_allow_extended_voltage_range = _attributes.AttributeViBoolean(1150076)
    '''Type: bool

    Enables the instrument to operate in additional voltage ranges where instrument specifications may differ from standard ranges. When set to True, this property enables extended voltage range operation. Review specification deviations for application suitability before using this property. NI recommends setting this property to False when not using the extended voltage range to avoid unintentional use of this range. The extended voltage range is supported only for PPMU, with the output method set to DC Voltage. A voltage glitch may occur when you change the PPMU output voltage from a standard range to the extended voltage range, or vice-versa, while the PPMU is sourcing. NI recommends temporarily changing the selected_function property to Off before sourcing a voltage level that requires a range change.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_allow_extended_voltage_range`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_allow_extended_voltage_range`
    '''
    ppmu_aperture_time = _attributes.AttributeViReal64(1150037)
    '''Type: float

    Specifies the measurement aperture time for the PPMU. The ppmu_aperture_time_units property sets the units of the PPMU aperture time.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_aperture_time`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_aperture_time`
    '''
    ppmu_aperture_time_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PPMUApertureTimeUnits, 1150038)
    '''Type: enums.PPMUApertureTimeUnits

    Specifies the units of the measurement aperture time for the PPMU.

    +-------------------------------+-----------------------------------------+
    | Defined Values:               |                                         |
    +===============================+=========================================+
    | PPMUApertureTimeUnits.SECONDS | Specifies the aperture time in seconds. |
    +-------------------------------+-----------------------------------------+

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_aperture_time_units`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_aperture_time_units`
    '''
    ppmu_current_level = _attributes.AttributeViReal64(1150019)
    '''Type: float

    Specifies the current level, in amps, that the PPMU forces to the DUT. This property is applicable only when you set the ppmu_output_function property to DC Current. Specify valid values for the current level using the PPMU_ConfigureCurrentLevelRange method.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_current_level`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_current_level`
    '''
    ppmu_current_level_range = _attributes.AttributeViReal64(1150020)
    '''Type: float

    Specifies the range of valid values for the current level, in amps, that the PPMU forces to the DUT. This property is applicable only when you set the ppmu_output_function property to DC Current.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_current_level_range`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_current_level_range`
    '''
    ppmu_current_limit = _attributes.AttributeViReal64(1150054)
    '''Type: float

    Specifies the current limit, in amps, that the output cannot exceed while the PPMU forces voltage to the DUT. This property is applicable only when you set the ppmu_output_function property to DC Voltage. The PXIe-6570/6571 does not support the ppmu_current_limit property and only allows configuration of the ppmu_current_limit_range property.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_current_limit`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_current_limit`
    '''
    ppmu_current_limit_behavior = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PPMUCurrentLimitBehavior, 1150064)
    '''Type: enums.PPMUCurrentLimitBehavior

    Specifies how the output should behave when the current limit is reached.

    +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | Defined Values:                   |                                                                                                                                         |
    +===================================+=========================================================================================================================================+
    | PPMUCurrentLimitBehavior.REGULATE | Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached. |
    +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_current_limit_behavior`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_current_limit_behavior`
    '''
    ppmu_current_limit_range = _attributes.AttributeViReal64(1150017)
    '''Type: float

    Specifies the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT. This property is applicable only when you set the ppmu_output_function property to DC Voltage.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_current_limit_range`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_current_limit_range`
    '''
    ppmu_current_limit_supported = _attributes.AttributeViBoolean(1150055)
    '''Type: bool

    Returns whether the device supports configuration of a current limit when you set the ppmu_output_function property to DC Voltage.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_current_limit_supported`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_current_limit_supported`
    '''
    ppmu_output_function = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PPMUOutputFunction, 1150015)
    '''Type: enums.PPMUOutputFunction

    Specifies whether the PPMU forces voltage or current to the DUT.

    +----------------------------+--------------------------------------------+
    | Defined Values:            |                                            |
    +============================+============================================+
    | PPMUOutputFunction.VOLTAGE | Specifies the output method to DC Voltage. |
    +----------------------------+--------------------------------------------+
    | PPMUOutputFunction.CURRENT | Specifies the output method to DC Current. |
    +----------------------------+--------------------------------------------+

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_output_function`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_output_function`
    '''
    ppmu_voltage_level = _attributes.AttributeViReal64(1150016)
    '''Type: float

    Specifies the voltage level, in volts, that the PPMU forces to the DUT. This property is applicable only when you set the ppmu_output_function property to DC Voltage.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_voltage_level`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_voltage_level`
    '''
    ppmu_voltage_limit_high = _attributes.AttributeViReal64(1150022)
    '''Type: float

    Specifies the maximum voltage limit, or high clamp voltage (V :sub:`CH` ), in volts, at the pin when the PPMU forces current to the DUT. This property is applicable only when you set the ppmu_output_function property to DC Current.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_voltage_limit_high`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_voltage_limit_high`
    '''
    ppmu_voltage_limit_low = _attributes.AttributeViReal64(1150021)
    '''Type: float

    Specifies the minimum voltage limit, or low clamp voltage (V :sub:`CL` ), in volts, at the pin when the PPMU forces current to the DUT. This property is applicable only when you set the ppmu_output_function property to DC Current.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_voltage_limit_low`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_voltage_limit_low`
    '''
    query_instrument_status = _attributes.AttributeViBoolean(1050003)
    '''Type: bool

    Specifies whether the NI-Digital Pattern Driver queries the digital pattern instrument status after each operation. The instrument status is always queried, regardless of the property setting.
    '''
    range_check = _attributes.AttributeViBoolean(1050002)
    '''Type: bool

    Checks the range and validates parameter and property values you pass to NI-Digital Pattern Driver methods. Ranges are always checked, regardless of the property setting.
    '''
    record_coercions = _attributes.AttributeViBoolean(1050006)
    '''Type: bool

    Specifies whether the IVI engine keeps a list of the value coercions it makes for integer and real type properties. Enabling record value coercions is not supported.
    '''
    rio_event_terminal_name = _attributes.AttributeViString(1150091)
    '''Type: str

    Specifies the terminal name for the output signal of the specified instance of a RIO Event. You can use this terminal name as an input signal source for another trigger.

    Tip:
    This property can be set/get on specific rio_events within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container rio_events to specify a subset.

    Example: :py:attr:`my_session.rio_events[ ... ].rio_event_terminal_name`

    To set/get on all rio_events, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.rio_event_terminal_name`
    '''
    rio_trigger_terminal_name = _attributes.AttributeViString(1150089)
    '''Type: str

    Specifies the terminal name from which the exported RIO trigger signal may be routed to other instruments through the PXI trigger bus. You can use this signal to trigger other instruments when the RIO trigger instance asserts on the digital pattern instrument.

    Tip:
    This property can be set/get on specific rio_triggers within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container rio_triggers to specify a subset.

    Example: :py:attr:`my_session.rio_triggers[ ... ].rio_trigger_terminal_name`

    To set/get on all rio_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.rio_trigger_terminal_name`
    '''
    rio_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1150086)
    '''Type: enums.TriggerType

    Disables the rio trigger or configures it for hardware triggering.  The default value is TriggerType.NONE.

    +--------------------------+------------------------------------------------------------------+
    | Valid Values:            |                                                                  |
    +==========================+==================================================================+
    | TriggerType.NONE         | Disables the conditional jump trigger.                           |
    +--------------------------+------------------------------------------------------------------+
    | TriggerType.DIGITAL_EDGE | Configures the conditional jump trigger for hardware triggering. |
    +--------------------------+------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific rio_triggers within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container rio_triggers to specify a subset.

    Example: :py:attr:`my_session.rio_triggers[ ... ].rio_trigger_type`

    To set/get on all rio_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.rio_trigger_type`
    '''
    selected_function = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.SelectedFunction, 1150004)
    '''Type: enums.SelectedFunction

    Caution: In the Disconnect state, some I/O protection and sensing circuitry remains exposed. Do not subject the instrument to voltage beyond its operating range.

    Specifies whether digital pattern instrument channels are controlled by the pattern sequencer or PPMU, disconnected, or off.

    +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Defined Values:             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
    +=============================+==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
    | SelectedFunction.DIGITAL    | The pin is connected to the driver, comparator, and active load methods. The PPMU is not sourcing, but can make voltage measurements. The state of the digital pin driver when you change the selected_function to Digital is determined by the most recent call to the write_static method or the last vector of the most recently executed pattern burst, whichever happened last. Use the write_static method to control the state of the digital pin driver through software. Use the burst_pattern method to control the state of the digital pin driver through a pattern. Set the **selectDigitalFunction** parameter of the burst_pattern method to True to automatically switch the selected_function of the pins in the pattern burst to SelectedFunction.DIGITAL. |
    +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | SelectedFunction.PPMU       | The pin is connected to the PPMU. The driver, comparator, and active load are off while this method is selected. Call the ppmu_source method to source a voltage or current. The ppmu_source method automatically switches the selected_function to the PPMU state and starts sourcing from the PPMU. Changing the selected_function to SelectedFunction.DISCONNECT, SelectedFunction.OFF, or SelectedFunction.DIGITAL causes the PPMU to stop sourcing. If you set the selected_function property to PPMU, the PPMU is initially not sourcing.                                                                                                                                                                                                                              |
    +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | SelectedFunction.OFF        | The pin is electrically connected, and the PPMU and digital pin driver are off while this method is selected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
    +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | SelectedFunction.DISCONNECT | The pin is electrically disconnected from instrument methods. Selecting this method causes the PPMU to stop sourcing prior to disconnecting the pin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
    +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note: You can make PPMU voltage measurements using the ppmu_measure method from within any selected_function.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].selected_function`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.selected_function`
    '''
    sequencer_flag_terminal_name = _attributes.AttributeViString(1150059)
    '''Type: str

    Specifies the terminal name for the output trigger signal of the Sequencer Flags trigger. You can use this terminal name as an input signal source for another trigger.
    '''
    serial_number = _attributes.AttributeViString(1150001)
    '''Type: str

    Returns the serial number of the device.

    Tip:
    This property can be set/get on specific instruments within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].serial_number`

    To set/get on all instruments, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.serial_number`
    '''
    simulate = _attributes.AttributeViBoolean(1050005)
    '''Type: bool

    Simulates I/O operations. After you open a session, you cannot change the simulation state. Use the __init__ method to enable simulation.
    '''
    specific_driver_class_spec_major_version = _attributes.AttributeViInt32(1050515)
    '''Type: int

    Returns the major version number of the class specification with which NI-Digital is compliant. This property is not supported.
    '''
    specific_driver_class_spec_minor_version = _attributes.AttributeViInt32(1050516)
    '''Type: int

    Returns the minor version number of the class specification with which NI-Digital is compliant. This property is not supported.
    '''
    specific_driver_description = _attributes.AttributeViString(1050514)
    '''Type: str

    Returns a string that contains a brief description of the NI-Digital Pattern driver.
    '''
    specific_driver_prefix = _attributes.AttributeViString(1050302)
    '''Type: str

    Returns a string that contains the prefix for the NI-Digital Pattern driver.
    '''
    specific_driver_revision = _attributes.AttributeViString(1050551)
    '''Type: str

    Returns a string that contains additional version information about the NI-Digital Pattern Driver. For example, the driver can return Driver: NI-Digital 16.0 as the value of this property.
    '''
    specific_driver_vendor = _attributes.AttributeViString(1050513)
    '''Type: str

    Returns a string ("National Instruments") that contains the name of the vendor that supplies the NI-Digital Pattern Driver.
    '''
    start_label = _attributes.AttributeViString(1150023)
    '''Type: str

    Specifies the pattern name or exported pattern label from which to start bursting the pattern.
    '''
    start_trigger_terminal_name = _attributes.AttributeViString(1150039)
    '''Type: str

    Specifies the terminal name for the output trigger signal of the Start trigger. You can use this terminal name as an input signal source for another trigger.
    '''
    start_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1150029)
    '''Type: enums.TriggerType

    Specifies the Start trigger type. The digital pattern instrument waits for this trigger after you call the init method or the burst_pattern method, and does not burst a pattern until this trigger is received.

    +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Defined Values:          |                                                                                                                                                                                                                                                                                                        |
    +==========================+========================================================================================================================================================================================================================================================================================================+
    | TriggerType.NONE         | Disables the Start trigger. Pattern bursting starts immediately after you call the init method or the burst_pattern method.                                                                                                                                                                            |
    +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | TriggerType.DIGITAL_EDGE | Pattern bursting does not start until the digital pattern instrument detects a digital edge.                                                                                                                                                                                                           |
    +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | TriggerType.SOFTWARE     | Pattern bursting does not start until the digital pattern instrument receives a software Start trigger. Create a software Start trigger by calling the send_software_edge_trigger method and selecting start trigger in the **trigger** parameter.Related information: SendSoftwareEdgeTrigger method. |
    +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    supported_instrument_models = _attributes.AttributeViString(1050327)
    '''Type: str

    Returns a comma delimited string that contains the supported digital pattern instrument models for the specific driver.
    '''
    tdr_endpoint_termination = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TDREndpointTermination, 1150081)
    '''Type: enums.TDREndpointTermination

    Specifies whether TDR Channels are connected to an open circuit or a short to ground.
    '''
    tdr_offset = _attributes.AttributeViReal64TimeDeltaSeconds(1150051)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the TDR Offset.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].tdr_offset`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.tdr_offset`
    '''
    termination_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TerminationMode, 1150006)
    '''Type: enums.TerminationMode

    Specifies the behavior of the pin during non-drive cycles.

    +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Defined Values:             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
    +=============================+======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
    | TerminationMode.ACTIVE_LOAD | Specifies that, for non-drive pin states (L, H, X, V, M, E), the active load is connected and the instrument sources or sinks a defined amount of current to load the DUT. The amount of current sourced by the instrument and therefore sunk by the DUT is specified by IOL. The amount of current sunk by the instrument and therefore sourced by the DUT is specified by IOH. The voltage at which the instrument changes between sourcing and sinking is specified by VCOM.                                                                                                                                                                                                                                                                                                                                                                                      |
    +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | TerminationMode.VTERM       | Specifies that, for non-drive pin states (L, H, X, V, M, E), the pin driver terminates the pin to the configured VTERM voltage through a 50 Ω impedance. VTERM is adjustable to allow for the pin to terminate at a set level. This is useful for instruments that might operate incorrectly if an instrument pin is unterminated and is allowed to float to any voltage level within the instrument voltage range. To address this issue, enable VTERM by configuring the VTERM pin level to the desired voltage and selecting the VTERM termination mode. Setting VTERM to 0 V and selecting the VTERM termination mode has the effect of connecting a 50 Ω termination to ground, which provides an effective 50 Ω impedance for the pin. This can be useful for improving signal integrity of certain DUTs by reducing reflections while the DUT drives the pin. |
    +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | TerminationMode.HIGH_Z      | Specifies that, for non-drive pin states (L, H, X, V, M, E), the pin driver is put in a high-impedance state and the active load is disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].termination_mode`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.termination_mode`
    '''
    timing_absolute_delay = _attributes.AttributeViReal64TimeDeltaSeconds(1150072)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies a timing delay, measured in seconds, and applies the delay to the digital pattern instrument in addition to TDR and calibration adjustments. If the timing_absolute_delay_enabled property is set to True, this value is the intermodule skew measured by NI-TClk. You can modify this value to override the timing delay and align the I/O timing of this instrument with another instrument that shares the same reference clock. If the timing_absolute_delay_enabled property is False, this property will return 0.0. Changing the timing_absolute_delay_enabled property from False to True will set the timing_absolute_delay value back to your previously set value.

    Tip:
    This property can be set/get on specific instruments within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].timing_absolute_delay`

    To set/get on all instruments, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.timing_absolute_delay`
    '''
    timing_absolute_delay_enabled = _attributes.AttributeViBoolean(1150071)
    '''Type: bool

    Specifies whether the timing_absolute_delay property should be applied to adjust the digital pattern instrument timing reference relative to other instruments in the system. Do not use this feature with digital pattern instruments in a Semiconductor Test System (STS). Timing absolute delay conflicts with the adjustment performed during STS timing calibration. When set to True, the digital pattern instrument automatically adjusts the timing absolute delay to correct the instrument timing reference relative to other instruments in the system for better timing alignment among synchronized instruments.
    '''
    vih = _attributes.AttributeViReal64(1150008)
    '''Type: float

    Specifies the voltage that the digital pattern instrument will apply to the input of the DUT when the test instrument drives a logic high (1).

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].vih`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.vih`
    '''
    vil = _attributes.AttributeViReal64(1150007)
    '''Type: float

    Specifies the voltage that the digital pattern instrument will apply to the input of the DUT when the test instrument drives a logic low (0).

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].vil`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.vil`
    '''
    voh = _attributes.AttributeViReal64(1150010)
    '''Type: float

    Specifies the output voltage from the DUT above which the comparator on the digital pattern test instrument interprets a logic high (H).

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].voh`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.voh`
    '''
    vol = _attributes.AttributeViReal64(1150009)
    '''Type: float

    Specifies the output voltage from the DUT below which the comparator on the digital pattern test instrument interprets a logic low (L).

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].vol`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.vol`
    '''
    vterm = _attributes.AttributeViReal64(1150011)
    '''Type: float

    Specifies the termination voltage the digital pattern instrument applies during non-drive cycles when the termination mode is set to V :sub:`term`. The instrument applies the termination voltage through a 50 Ω parallel termination resistance.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].vterm`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.vterm`
    '''

    def __init__(self, repeated_capability_list, all_channels_in_session, vi, library, encoding, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
        self._all_channels_in_session = all_channels_in_session
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
        self.rio_events = _RepeatedCapabilities(self, 'RIOEvent', repeated_capability_list)
        self.rio_triggers = _RepeatedCapabilities(self, 'RIOTrigger', repeated_capability_list)

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
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
    def apply_levels_and_timing(self, levels_sheet, timing_sheet, initial_state_high_pins=None, initial_state_low_pins=None, initial_state_tristate_pins=None):
        r'''apply_levels_and_timing

        Applies digital levels and timing values defined in previously loaded levels and timing sheets. When applying a levels sheet, only the levels specified in the sheet are affected. Any levels not specified in the sheet remain unchanged. When applying a timing sheet, all existing time sets are deleted before the new time sets are loaded.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].apply_levels_and_timing`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.apply_levels_and_timing`

        Args:
            levels_sheet (str): Name of the levels sheet to apply. Use the name of the sheet or pass the absolute file path you use in the load_specifications_levels_and_timing method. The name of the levels sheet is the file name without the directory and file extension.

            timing_sheet (str): Name of the timing sheet to apply. Use the name of the sheet or pass the absolute file path that you use in the load_specifications_levels_and_timing method. The name of the timing sheet is the file name without the directory and file extension.

            initial_state_high_pins (basic sequence types or str): Comma-delimited list of pins, pin groups, or channels to initialize to a high state.

            initial_state_low_pins (basic sequence types or str): Comma-delimited list of pins, pin groups, or channels to initialize to a low state.

            initial_state_tristate_pins (basic sequence types or str): Comma-delimited list of pins, pin groups, or channels to initialize to a non-drive state (X)

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        levels_sheet_ctype = ctypes.create_string_buffer(levels_sheet.encode(self._encoding))  # case C020
        timing_sheet_ctype = ctypes.create_string_buffer(timing_sheet.encode(self._encoding))  # case C020
        initial_state_high_pins_ctype = ctypes.create_string_buffer(_converters.convert_repeated_capabilities_without_prefix(initial_state_high_pins).encode(self._encoding))  # case C040
        initial_state_low_pins_ctype = ctypes.create_string_buffer(_converters.convert_repeated_capabilities_without_prefix(initial_state_low_pins).encode(self._encoding))  # case C040
        initial_state_tristate_pins_ctype = ctypes.create_string_buffer(_converters.convert_repeated_capabilities_without_prefix(initial_state_tristate_pins).encode(self._encoding))  # case C040
        error_code = self._library.niDigital_ApplyLevelsAndTiming(vi_ctype, site_list_ctype, levels_sheet_ctype, timing_sheet_ctype, initial_state_high_pins_ctype, initial_state_low_pins_ctype, initial_state_tristate_pins_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def apply_tdr_offsets(self, offsets):
        r'''apply_tdr_offsets

        Applies the correction for propagation delay offsets to a digital pattern instrument. Use this method to apply TDR offsets that are stored from a past measurement or are measured by means other than the tdr method. Also use this method to apply correction for offsets if the **applyOffsets** input of the tdr method was set to False at the time of measurement.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].apply_tdr_offsets`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.apply_tdr_offsets`

        Args:
            offsets (basic sequence of hightime.timedelta, datetime.timedelta, or float in seconds): TDR offsets to apply, in seconds. Specify an offset for each pin or channel in the repeated capabilities. If the repeated capabilities contain pin names, you must specify offsets for each site in the channel map per pin.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        num_offsets_ctype = _visatype.ViInt32(0 if offsets is None else len(offsets))  # case S160
        offsets_converted = _converters.convert_timedeltas_to_seconds_real64(offsets)  # case B520
        offsets_ctype = get_ctypes_pointer_for_buffer(value=offsets_converted, library_type=_visatype.ViReal64)  # case B520
        error_code = self._library.niDigital_ApplyTDROffsets(vi_ctype, channel_list_ctype, num_offsets_ctype, offsets_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _burst_pattern(self, start_label, select_digital_function=True, wait_until_done=True, timeout=hightime.timedelta(seconds=10.0)):
        r'''_burst_pattern

        Uses the **startLabel** you specify to burst the pattern on the sites you specify and provides the option to wait for the burst to complete. Digital pins retain their state at the end of a pattern burst until the first vector of a subsequent pattern burst, a call to write_static, or a call to apply_levels_and_timing.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._burst_pattern`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._burst_pattern`

        Args:
            start_label (str): Pattern name or exported pattern label from which to start bursting the pattern.

            select_digital_function (bool): A Boolean that specifies whether to select the digital method for the pins in the pattern prior to bursting.

            wait_until_done (bool): A Boolean that indicates whether to wait until the bursting is complete.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.

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

        Stops clock generation on the specified channel(s) or pin(s) and pin group(s).

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].clock_generator_abort`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.clock_generator_abort`
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_ClockGenerator_Abort(vi_ctype, channel_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def clock_generator_generate_clock(self, frequency, select_digital_function=True):
        r'''clock_generator_generate_clock

        Configures clock generator frequency and initiates clock generation on the specified channel(s) or pin(s) and pin group(s).

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].clock_generator_generate_clock`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.clock_generator_generate_clock`

        Args:
            frequency (float): The frequency of the clock generation, in Hz.

            select_digital_function (bool): A Boolean that specifies whether to select the digital method for the pins specified prior to starting clock generation.

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

        Configures I\ :sub:`OL`, I\ :sub:`OH`, and V\ :sub:`COM` levels for the active load on the pins you specify. The DUT sources or sinks current based on the level values. To enable active load, set the termination mode to TerminationMode.ACTIVE_LOAD. To disable active load, set the termination mode of the instrument to TerminationMode.HIGH_Z or TerminationMode.VTERM.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_active_load_levels`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_active_load_levels`

        Args:
            iol (float): Maximum current that the DUT sinks while outputting a voltage below V\ :sub:`COM`.

            ioh (float): Maximum current that the DUT sources while outputting a voltage above V\ :sub:`COM`.

            vcom (float): Commutating voltage level at which the active load circuit switches between sourcing current and sinking current.

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

        Configures which sites burst the pattern on the next call to the initiate method. The pattern burst sites can also be modified through the repeated capabilities for the burst_pattern method. If a site has been disabled through the disable_sites method, the site does not burst a pattern even if included in the pattern burst sites.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].configure_pattern_burst_sites`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_pattern_burst_sites`
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_ConfigurePatternBurstSites(vi_ctype, site_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_time_set_compare_edges_strobe(self, time_set_name, strobe_edge):
        r'''configure_time_set_compare_edges_strobe

        Configures the strobe edge time for the specified pins. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_compare_edges_strobe`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_compare_edges_strobe`

        Args:
            time_set_name (str): The specified time set name.

            strobe_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Time when the comparison happens within a vector period.

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

        Configures the compare strobes for the specified pins in the time set, including the 2x strobe. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_compare_edges_strobe2x`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_compare_edges_strobe2x`

        Args:
            time_set_name (str): The specified time set name.

            strobe_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Time when the comparison happens within a vector period.

            strobe2_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Time when the comparison happens for the second DUT cycle within a vector period.

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

        Configures the drive format and drive edge placement for the specified pins. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_drive_edges`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_drive_edges`

        Args:
            time_set_name (str): The specified time set name.

            format (enums.DriveFormat): Drive format of the time set.

                -   DriveFormat.NR: Non-return.
                -   DriveFormat.RL: Return to low.
                -   DriveFormat.RH: Return to high.
                -   DriveFormat.SBC: Surround by complement.

            drive_on_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period for turning on the pin driver.This option applies only when the prior vector left the pin in a non-drive pin state (L, H, X, V, M, E). For the SBC format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven.

            drive_data_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period until the pattern data is driven to the pattern value.The ending state from the previous vector persists until this point.

            drive_return_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format.

            drive_off_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive symbol (L, H, X, V, M, E).

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

        Configures the drive edges of the pins in the time set, including 2x edges. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_drive_edges2x`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_drive_edges2x`

        Args:
            time_set_name (str): The specified time set name.

            format (enums.DriveFormat): Drive format of the time set.

                -   DriveFormat.NR: Non-return.
                -   DriveFormat.RL: Return to low.
                -   DriveFormat.RH: Return to high.
                -   DriveFormat.SBC: Surround by complement.

            drive_on_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period for turning on the pin driver.This option applies only when the prior vector left the pin in a non-drive pin state (L, H, X, V, M, E). For the SBC format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven.

            drive_data_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period until the pattern data is driven to the pattern value.The ending state from the previous vector persists until this point.

            drive_return_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format.

            drive_off_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive symbol (L, H, X, V, M, E).

            drive_data2_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period until the pattern data in the second DUT cycle is driven to the pattern value.

            drive_return2_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data in the second DUT cycle to the return value, as specified in the format.

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

        Configures the drive format for the pins specified in the **pinList**. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_drive_format`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_drive_format`

        Args:
            time_set_name (str): The specified time set name.

            drive_format (enums.DriveFormat): Drive format of the time set.

                -   DriveFormat.NR: Non-return.
                -   DriveFormat.RL: Return to low.
                -   DriveFormat.RH: Return to high.
                -   DriveFormat.SBC: Surround by complement.

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

        Configures the edge placement for the pins specified in the pin list. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_edge`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_edge`

        Args:
            time_set_name (str): The specified time set name.

            edge (enums.TimeSetEdgeType): Name of the edge.

                -   TimeSetEdgeType.DRIVE_ON
                -   TimeSetEdgeType.DRIVE_DATA
                -   TimeSetEdgeType.DRIVE_RETURN
                -   TimeSetEdgeType.DRIVE_OFF
                -   TimeSetEdgeType.COMPARE_STROBE
                -   TimeSetEdgeType.DRIVE_DATA2
                -   TimeSetEdgeType.DRIVE_RETURN2
                -   TimeSetEdgeType.COMPARE_STROBE2

            time (hightime.timedelta, datetime.timedelta, or float in seconds): The time from the beginning of the vector period in which to place the edge.

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

        Configures the edge multiplier of the pins in the time set. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_edge_multiplier`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_edge_multiplier`

        Args:
            time_set_name (str): The specified time set name.

            edge_multiplier (int): The specified edge multiplier for the pins in the pin list.

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

        Configures voltage levels for the pins you specify.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_voltage_levels`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_voltage_levels`

        Args:
            vil (float): Voltage that the instrument will apply to the input of the DUT when the pin driver drives a logic low (0).

            vih (float): Voltage that the instrument will apply to the input of the DUT when the test instrument drives a logic high (1).

            vol (float): Output voltage below which the comparator on the pin driver interprets a logic low (L).

            voh (float): Output voltage above which the comparator on the pin driver interprets a logic high (H).

            vterm (float): Termination voltage the instrument applies during non-drive cycles when the termination mode is set to V\ :sub:`term`. The instrument applies the termination voltage through a 50 ohm parallel termination resistance.

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

        Sets the capture waveform settings for parallel acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].create_capture_waveform_parallel`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.create_capture_waveform_parallel`

        Args:
            waveform_name (str): Waveform name you want to use. Use the waveform_name with the capture_start opcode in your pattern.

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

        Sets the capture waveform settings for serial acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].create_capture_waveform_serial`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.create_capture_waveform_serial`

        Args:
            waveform_name (str): Waveform name you want to use. Use the waveform_name with the capture_start opcode in your pattern.

            sample_width (int): Width in bits of each serial sample. Valid values are between 1 and 32.

            bit_order (enums.BitOrder): Order in which to shift the bits.

                -   BitOrder.MSB: Specifies the bit order by most significant bit first.
                -   BitOrder.LSB: Specifies the bit order by least significant bit first.

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

        Sets the source waveform settings required for parallel sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].create_source_waveform_parallel`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.create_source_waveform_parallel`

        Args:
            waveform_name (str): The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

            data_mapping (enums.SourceDataMapping): Parameter that specifies how to map data on multiple sites.

                -   SourceDataMapping.BROADCAST: Broadcasts the waveform you specify to all sites.
                -   SourceDataMapping.SITE_UNIQUE: Sources unique waveform data to each site.

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

        Sets the source waveform settings required for serial sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].create_source_waveform_serial`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.create_source_waveform_serial`

        Args:
            waveform_name (str): The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

            data_mapping (enums.SourceDataMapping): Parameter that specifies how to map data on multiple sites.

                -   SourceDataMapping.BROADCAST: Broadcasts the waveform you specify to all sites.
                -   SourceDataMapping.SITE_UNIQUE: Sources unique waveform data to each site.

            sample_width (int): Width in bits of each serial sample. Valid values are between 1 and 32.

            bit_order (enums.BitOrder): Order in which to shift the bits.

                -   BitOrder.MSB: Specifies the bit order by most significant bit first.
                -   BitOrder.LSB: Specifies the bit order by least significant bit first.

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

        Disables specified sites. Disabled sites are not included in pattern bursts initiated by the initiate method or the burst_pattern method, even if the site is specified in the list of pattern burst sites in configure_pattern_burst_sites method or in the repeated capabilities for the burst_pattern method. Additionally, if you specify a list of pin or pin group names in repeated capabilities in any NI-Digital method, digital pattern instrument channels mapped to disabled sites are not affected by the method. The methods that return per-pin data, such as the ppmu_measure method, do not return data for channels mapped to disabled sites. The digital pattern instrument channels mapped to the sites specified are left in their current state. NI TestStand Semiconductor Module requires all sites to always be enabled, and manages the set of active sites without disabling the sites in the digital instrument session. Do not use this method with the Semiconductor Module.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].disable_sites`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.disable_sites`
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_DisableSites(vi_ctype, site_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def enable_sites(self):
        r'''enable_sites

        Enables the sites you specify. All sites are enabled by default.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].enable_sites`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.enable_sites`
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_EnableSites(vi_ctype, site_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def burst_pattern(self, start_label, select_digital_function=True, wait_until_done=True, timeout=hightime.timedelta(seconds=10.0)):
        '''burst_pattern

        Uses the start_label you specify to burst the pattern on the sites you specify. If you
        specify wait_until_done as True, waits for the burst to complete, and returns comparison results for each site.

        Digital pins retain their state at the end of a pattern burst until the first vector of the pattern burst, a call to
        write_static, or a call to apply_levels_and_timing.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].burst_pattern`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.burst_pattern`

        Args:
            start_label (str): Pattern name or exported pattern label from which to start bursting the pattern.

            select_digital_function (bool): A Boolean that specifies whether to select the digital method for the pins in the pattern prior to bursting.

            wait_until_done (bool): A Boolean that indicates whether to wait until the bursting is complete.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.


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
    def fetch_capture_waveform(self, waveform_name, samples_to_read, timeout=hightime.timedelta(seconds=10.0)):
        '''fetch_capture_waveform

        Returns dictionary where each key is a site number and value is a collection of digital states representing capture waveform data

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].fetch_capture_waveform`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.fetch_capture_waveform`

        Args:
            waveform_name (str): Waveform name you create with the create capture waveform method. Use the waveform_name parameter with capture_start opcode in your pattern.

            samples_to_read (int): Number of samples to fetch.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.


        Returns:
            waveform ({ int: memoryview of array.array of unsigned int, int: memoryview of array.array of unsigned int, ... }): Dictionary where each key is a site number and value is a collection of digital states representing capture waveform data

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
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].fetch_history_ram_cycle_information`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.fetch_history_ram_cycle_information`

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
                pattern_names[pattern_index] = self._get_pattern_name(pattern_index)
            pattern_name = pattern_names[pattern_index]

            if time_set_index not in time_set_names:
                # Repeated capability is not used
                time_set_names[time_set_index] = self._get_time_set_name(time_set_index)
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

        Returns the pin names, site numbers, and channel names that correspond to per-pin data read from the digital pattern instrument. The method returns pin information in the same order as values read using the read_static method, ppmu_measure method, and get_fail_count method. Use this method to match values the previously listed methods return with pins, sites, and instrument channels.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_pin_results_pin_information`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_pin_results_pin_information`

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
            channel_names = self.get_channel_names(channel_indexes[i] - 1)  # channel_indexes are 1-based
            assert 1 == len(channel_names)
            pin_infos.append(PinInfo(pin_name=pin_name, site_number=site_numbers[i], channel_name=channel_names[0]))

        return pin_infos

    @ivi_synchronized
    def get_site_pass_fail(self):
        '''get_site_pass_fail

        Returns dictionary where each key is a site number and value is pass/fail

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].get_site_pass_fail`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_site_pass_fail`

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

        Gets the per-cycle pattern information acquired for the specified cycle.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._fetch_history_ram_cycle_information`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._fetch_history_ram_cycle_information`

        Args:
            sample_index (int): The index of the History RAM sample to fetch. Each History RAM sample contains information about a single cycle in the pattern burst.


        Returns:
            pattern_index (int): The returned index of the pattern for the acquired cycle. Use _get_pattern_name to get the name of the pattern from its index.

            time_set_index (int): The returned time set for the acquired cycle. Use _get_time_set_name to get the name of the time set from its index.

            vector_number (int): The returned vector number within the pattern for the acquired cycle. Vector numbers start at 0 from the beginning of the pattern.

            cycle_number (int): Returns the cycle number acquired by this History RAM sample. Cycle numbers start at 0 from the beginning of the pattern burst.

            num_dut_cycles (int): The returned number of DUT cycles contained in the cycle acquired by this History RAM sample. This is only needed if the pattern uses the edge multiplier feature.

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

        Gets the per-pin pattern data acquired for the specified cycle.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._fetch_history_ram_cycle_pin_data`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._fetch_history_ram_cycle_pin_data`

        Args:
            pin_list (str): The specified pins for which to retrieve History RAM data. If empty, the pin list from the pattern containing the start label is used. Call get_pattern_pin_names or GetPatternPinIndexeswith the start label to retrieve the pins associated with the pattern burst.

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            sample_index (int): The index of the History RAM sample to fetch. Each History RAM sample contains information about a single cycle in the pattern burst.

            dut_cycle_index (int): The specified index of the DUT cycle. If the pattern does not use the edge multiplier feature, pass 0 for this parameter. For History RAM samples that contain multiple DUT cycles, indicated by the **numDutCycles** value returned by _fetch_history_ram_cycle_information, call this method multiple times to retrieve pin states for each DUT cycle. The DUT cycle index should start at 0.


        Returns:
            expected_pin_states (list of enums.PinState): The returned pin state as expected by the loaded pattern in the order specified in **pinList**. Pins without defined edges in the specified DUT cycle will return PinState.NOT_A_PIN_STATE

            actual_pin_states (list of enums.PinState): The returned pin state acquired by History RAM in the order specified in **pinList**. Pins without defined edges in the specified DUT cycle will return PinState.NOT_A_PIN_STATE

            per_pin_pass_fail (list of bool): The returned pass fail information for pins in the order specified in **pinList**. Pins without defined edges in the specified DUT cycle will return pass (True).

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

        Fetches the History RAM Scan Cycle Number for the sample index. If the sample is not from a scan vector, the scan cycle number will be returned as -1.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._fetch_history_ram_scan_cycle_number`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._fetch_history_ram_scan_cycle_number`

        Args:
            sample_index (int): The index of the History RAM sample to fetch. Each History RAM sample contains information about a single cycle in the pattern burst.


        Returns:
            scan_cycle_number (int): Returns the scan cycle number acquired by this History RAM sample. Scan cycle numbers start at 0 from the first cycle of the scan vector. Scan cycle numbers are -1 for cycles that do not have a scan opcode.

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

        Measures the frequency on the specified channel(s) over the specified measurement time. All channels in the repeated capabilities should have the same measurement time.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].frequency_counter_measure_frequency`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.frequency_counter_measure_frequency`

        Returns:
            frequencies (list of float): The returned frequency counter measurement, in Hz.This method returns -1 if the measurement is invalid for the channel.

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

        Queries the value of a ViBoolean property. Use this method to get the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute (int): The ID of a property.


        Returns:
            value (bool): The returned current value of the property; pass the address of a ViBoolean variable.

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

        Queries the value of a ViInt32 property. Use this method to get the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute (int): The ID of a property.


        Returns:
            value (int): The returned current value of the property; pass the address of a ViInt32 variable.

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

        Queries the value of a ViInt64 property. Use this method to get the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int64`

        Args:
            attribute (int): The ID of a property.


        Returns:
            value (int): The returned current value of the property; pass the address of a ViInt64 variable.

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

        This method queries the value of a ViReal64 property. Use this method to get the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute (int): The ID of a property.


        Returns:
            value (float): The returned current value of the property; pass the address of a ViReal64 variable.

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

        Queries the value of a ViString property. Use this method to get the values of digital pattern instrument-specific properties and inherent IVI properties. You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the **bufferSize**. If the current value of the property, including the terminating NULL byte, is larger than the size you indicate in the **bufferSize**, the method copies (bufferSize - 1) bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the **bufferSize** you must pass to get the entire value. For example, if the value is "123456" and the **bufferSize** is 4, the method places "123" into the buffer and returns 7. If you want to call this method just to get the required buffer size, you can pass 0 for the **bufferSize** and VI_NULL for the value.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute (int): The ID of a property.


        Returns:
            value (str): The buffer in which the method returns the current value of the property; the buffer must be of type ViChar and have at least as many bytes as indicated in the **bufferSize**.

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
    def get_channel_names(self, indices):
        r'''get_channel_names

        Returns a list of channel names for given channel indices.

        Args:
            indices (basic sequence types or str or int): Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:

                -   A comma-separated list—for example, "0,2,3,1"
                -   A range using a hyphen—for example, "0-3"
                -   A range using a colon—for example, "0:3 "

                You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0," "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.


        Returns:
            names (list of str): The channel name(s) at the specified indices.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        indices_ctype = ctypes.create_string_buffer(_converters.convert_repeated_capabilities_without_prefix(indices).encode(self._encoding))  # case C040
        name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        names_ctype = None  # case C050
        error_code = self._library.niDigital_GetChannelNameFromString(vi_ctype, indices_ctype, name_buffer_size_ctype, names_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        names_ctype = (_visatype.ViChar * name_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetChannelNameFromString(vi_ctype, indices_ctype, name_buffer_size_ctype, names_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_comma_separated_string_to_list(names_ctype.value.decode(self._encoding))

    def _get_error(self):
        r'''_get_error

        Returns the error information associated with the digital pattern instrument handle. This method retrieves and then clears the error information for the session. If **vi** is VI_NULL, this method retrieves and then clears the error information for the current thread. You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the buffer size. If the current value of the error description, including the terminating NULL byte, is larger than the size you indicate in the buffer size, the method copies (buffer size -1) bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the method places "123" into the buffer and returns 7. If you want to call this method just to get the required buffer size, you can pass 0 for the buffer size and VI_NULL for **errorDescription**.

        Returns:
            error_code (int): The returned error code for the session or execution thread.

            error_description (str): The returned error description for the IVI session or execution thread.
                If there is no description, the method returns an empty string. The buffer must contain at least as many elements as the value you specify with the buffer size parameter.
                If you pass 0 for **errorDescriptionBufferSize**, you can pass VI_NULL for this parameter.

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

        Returns the comparison fail count for pins in the repeated capabilities.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_fail_count`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_fail_count`

        Returns:
            failure_count (list of int): Number of failures in an array. If a site is disabled or not enabled for burst, the method does not return data for that site. You can also use the get_pin_results_pin_information method to obtain a sorted list of returned sites and channels.

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
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].get_history_ram_sample_count`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_history_ram_sample_count`

        Returns:
            sample_count (int): The returned number of samples that History RAM acquired.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        sample_count_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niDigital_GetHistoryRAMSampleCount(vi_ctype, site_ctype, None if sample_count_ctype is None else (ctypes.pointer(sample_count_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(sample_count_ctype.value)

    @ivi_synchronized
    def _get_pattern_name(self, pattern_index):
        r'''_get_pattern_name

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

        Returns the name of the pin at the index you specify. You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the **nameBufferSize**. If the current value of the property, including the terminating NULL byte, is larger than the size you indicate in the buffer size, the method copies (buffer size - 1) bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the method places "123" into the buffer and returns 7. If you want to call this method just to get the required buffer size, you can pass 0 for **nameBufferSize** and VI_NULL for the name.

        Args:
            pin_index (int): Index of pin to query. Pin indexes begin at 0.


        Returns:
            name (str): Returns the pin name at the specified **pinIndex**.

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

        Returns the pin names, site numbers, and channel names that correspond to per-pin data read from the digital pattern instrument. The method returns pin information in the same order as values read using the read_static method, ppmu_measure method, and get_fail_count method. Use this method to match values the previously listed methods return with pins, sites, and instrument channels.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_pin_results_pin_information`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_pin_results_pin_information`

        Returns:
            pin_indexes (list of int): The returned index of the pins corresponding to data read from the digital pattern instrument using the specified repeated capabilities. If you do not want to use this parameter, pass VI_NULL.
                Call _get_pin_name to get the name of the pin associated with an index.

            site_numbers (list of int): The returned site numbers that correspond to data read from the digital pattern instrument using the specified repeated capabilities. If you do not want to use this parameter, pass VI_NULL.

            channel_indexes (list of int): The returned index of channels corresponding to data read from the digital pattern instrument using the specified repeated capabilities. If you do not want to use this parameter, pass VI_NULL.
                Call get_channel_name to get the name of the channel associated with an index. Channel indexes are one-based.

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

        Returns the pass or fail results for each site.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._get_site_pass_fail`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_site_pass_fail`

        Returns:
            pass_fail (list of bool): The returned array of pass (True) and fail results for the sites you specify in the repeated capabilities. If sites span multiple digital pattern instruments, you must use an AND operator for the partial results for those sites returned by each instrument. If a site is disabled or not enabled for burst, the method does not return data for that site. Use the SortSiteResultsViBoolean method to order and combine the data to match the repeated capabilities. You can also use the _get_site_results_site_numbers method to determine the order of the sites returned from this method call so that you can match the pass array with site numbers.

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

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

        Returns the site numbers that correspond to per-site data read from the digital pattern instrument. The method returns site numbers in the same order as values read using the _get_site_pass_fail and fetch_capture_waveform_u32 methods. Use this method to match values the previously listed methods return with site numbers.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._get_site_results_site_numbers`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_site_results_site_numbers`

        Args:
            site_result_type (enums.SiteResultType): The type of data specified in the results array.

                -   _SiteResultType.PASS_FAIL: Get site numbers for pass/fail data.
                -   _SiteResultType.CAPTURE_WAVEFORM: Get site numbers for capture waveforms.


        Returns:
            site_numbers (list of int): The returned array of site numbers that correspond to the values specified by **siteResultType**.

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

        Returns the drive format of a pin in the specified time set.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].get_time_set_drive_format`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_time_set_drive_format`

        Args:
            time_set_name (str): The specified time set name.


        Returns:
            format (enums.DriveFormat): Returned drive format of the time set for the specified pin.

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

        Returns the edge time of a pin in the specified time set.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].get_time_set_edge`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_time_set_edge`

        Args:
            time_set_name (str): The specified time set name.

            edge (enums.TimeSetEdgeType): Name of the edge.

                -   TimeSetEdgeType.DRIVE_ON
                -   TimeSetEdgeType.DRIVE_DATA
                -   TimeSetEdgeType.DRIVE_RETURN
                -   TimeSetEdgeType.DRIVE_OFF
                -   TimeSetEdgeType.COMPARE_STROBE
                -   TimeSetEdgeType.DRIVE_DATA2
                -   TimeSetEdgeType.DRIVE_RETURN2
                -   TimeSetEdgeType.COMPARE_STROBE2


        Returns:
            time (hightime.timedelta): Time from the beginning of the vector period in which to place the edge.

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
        return _converters.convert_seconds_real64_to_timedelta(float(time_ctype.value))

    @ivi_synchronized
    def get_time_set_edge_multiplier(self, time_set_name):
        r'''get_time_set_edge_multiplier

        Returns the edge multiplier of the specified time set.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].get_time_set_edge_multiplier`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_time_set_edge_multiplier`

        Args:
            time_set_name (str): The specified time set name.


        Returns:
            edge_multiplier (int): Returned edge multiplier of the time set for the specified pin.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        edge_multiplier_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetTimeSetEdgeMultiplier(vi_ctype, pin_ctype, time_set_name_ctype, None if edge_multiplier_ctype is None else (ctypes.pointer(edge_multiplier_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(edge_multiplier_ctype.value)

    @ivi_synchronized
    def _get_time_set_name(self, time_set_index):
        r'''_get_time_set_name

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

        Checks if a specified site is enabled.

        Note: The method returns an error if more than one site is specified.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].is_site_enabled`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.is_site_enabled`

        Returns:
            enable (bool): Boolean value that returns whether the site is enabled or disabled.

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

        Instructs the PPMU to measure voltage or current. This method can be called to take a voltage measurement even if the pin method is not set to PPMU.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].ppmu_measure`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.ppmu_measure`

        Args:
            measurement_type (enums.PPMUMeasurementType): Parameter that specifies whether the PPMU measures voltage or current from the DUT.

                -   PPMUMeasurementType.CURRENT: The PPMU measures current from the DUT.
                -   PPMUMeasurementType.VOLTAGE: The PPMU measures voltage from the DUT.


        Returns:
            measurements (list of float): The returned array of measurements in the order you specify in the repeated capabilities. If a site is disabled, the method does not return data for that site. You can also use the get_pin_results_pin_information method to obtain a sorted list of returned sites and channels.

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

        Starts sourcing voltage or current from the PPMU. This method automatically selects the PPMU method. Changes to PPMU source settings do not take effect until you call this method. If you modify source settings after you call this method, you must call this method again for changes in the configuration to take effect.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].ppmu_source`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.ppmu_source`
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_PPMU_Source(vi_ctype, channel_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def read_static(self):
        r'''read_static

        Reads the current state of comparators for pins you specify in the repeated capabilities. If there are uncommitted changes to levels or the termination mode, this method commits the changes to the pins.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].read_static`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.read_static`

        Returns:
            data (list of enums.PinState): The returned array of pin states read from the channels in the repeated capabilities. Data is returned in the order you specify in the repeated capabilities. If a site is disabled, the method does not return data for that site. You can also use the get_pin_results_pin_information method to obtain a sorted list of returned sites and channels.

                -   PinState.L: The comparators read a logic low pin state.
                -   PinState.H: The comparators read a logic high pin state.
                -   PinState.M: The comparators read a midband pin state.
                -   PinState.V: The comparators read a value that is above VOH and below VOL, which can occur when you set VOL higher than VOH.

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

        Sets the value of a ViBoolean property. Use this method to set the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute (int): The ID of a property.

            value (bool): The value to which you want to set the property; some of the values might not be valid depending on the current settings of the instrument session.

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

        Sets the value of a ViInt32 property. Use this method to set the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute (int): The ID of a property.

            value (int): The value to which you want to set the property; some of the values might not be valid depending on the current settings of the instrument session.

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

        Sets the value of a ViInt64 property. Use this method to set the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int64`

        Args:
            attribute (int): The ID of a property.

            value (int): The value to which you want to set the property; some of the values might not be valid depending on the current settings of the instrument session.

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

        Sets the value of a ViIntReal64 property. Use this method to set the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute (int): The ID of a property.

            value (float): The value to which you want to set the property; some of the values might not be valid depending on the current settings of the instrument session.

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

        Sets the value of a ViString property. Use this method to set the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute (int): The ID of a property.

            value (str): The value to which you want to set the property; some of the values might not be valid depending on the current settings of the instrument session.

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

        Measures propagation delays through cables, connectors, and load boards using Time-Domain Reflectometry (TDR). Ensure that the channels and pins you select are connected to an open circuit.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].tdr`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.tdr`

        Args:
            apply_offsets (bool): A Boolean that specifies whether to apply the measured TDR offsets. If you need to adjust the measured offsets prior to applying, set this input to False, and call the apply_tdr_offsets method to specify the adjusted TDR offsets values.


        Returns:
            offsets (list of hightime.timedelta): Measured TDR offsets specified in seconds.

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

        Writes one waveform per site. Use this write method if you set the parameter of the create source waveform method to Site Unique.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._write_source_waveform_site_unique_u32`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._write_source_waveform_site_unique_u32`

        Args:
            waveform_name (str): The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

            num_waveforms (int): Number of waveforms.

            samples_per_waveform (int): Number of samples per waveform.

            waveform_data (array.array("L")): An array of samples to use as source data. Data for each site must be appended sequentially in the array (non-interleaved).

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

        Writes a static state to the specified pins. The selected pins remain in the specified state until the next pattern burst or call to this method. If there are uncommitted changes to levels or the termination mode, this method commits the changes to the pins. This method does not change the selected pin method. If you write a static state to a pin that does not have the Digital method selected, the new static state is stored by the instrument, and affects the state of the pin the next time you change the selected method to Digital.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].write_static`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.write_static`

        Args:
            state (enums.WriteStaticPinState): Parameter that specifies one of the following digital states to assign to the pin.

                -   WriteStaticPinState.ZERO: Specifies to drive low.
                -   WriteStaticPinState.ONE: Specifies to drive high.
                -   WriteStaticPinState.X: Specifies to not drive.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

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

        Takes the error code returned by the digital pattern instrument driver methods, interprets it, and returns it as a user readable string.

        Args:
            error_code (int): The specified error code.


        Returns:
            error_message (str): The error information formatted as a string. The array must contain at least 256 characters.

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

        Creates and returns a new session to the specified digital pattern instrument to use in all subsequent method calls. To place the instrument in a known startup state when creating a new session, set the reset parameter to True, which is equivalent to calling the reset method immediately after initializing the session.

        Args:
            resource_name (str): The specified resource name shown in Measurement & Automation Explorer (MAX) for a digital pattern instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. **resourceName** can also be a logical IVI name. This parameter accepts a comma-delimited list of strings in the form PXI1Slot2,PXI1Slot3, where ``PXI1Slot2`` is one instrument resource name and ``PXI1Slot3`` is another. When including more than one digital pattern instrument in the comma-delimited list of strings, list the instruments in the same order they appear in the pin map.

                +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | |Note| | Note   You only can specify multiple instruments of the same model. For example, you can list two PXIe-6570s but not a PXIe-6570 and PXIe-6571. The instruments must be in the same chassis. |
                +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                .. |Note| image:: note.gif

                Note:

            id_query (bool): A Boolean that verifies that the digital pattern instrument you initialize is supported by NI-Digital. NI-Digital automatically performs this query, so setting this parameter is not necessary.

            reset_device (bool): A Boolean that specifies whether to reset a digital pattern instrument to a known state when the session is initialized. Setting the **resetDevice** value to True is equivalent to calling the reset method immediately after initializing the session.

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
            new_vi (int): The returned instrument session.

        '''
        # Initialize the superclass with default values first, populate them later
        super(Session, self).__init__(
            repeated_capability_list=[],
            vi=None,
            library=None,
            encoding=None,
            freeze_it=False,
            all_channels_in_session=None
        )
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

        # Store the list of channels in the Session which is needed by some nimi-python modules.
        # Use try/except because not all the modules support channels.
        # self.get_channel_names() and self.channel_count can only be called after the session
        # handle `self._vi` is set
        try:
            self._all_channels_in_session = self.get_channel_names(range(self.channel_count))
        except AttributeError:
            self._all_channels_in_session = None

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def initiate(self):
        '''initiate

        Starts bursting the pattern configured by start_label, causing the NI-Digital session to be committed. To stop the pattern burst, call abort. If keep alive pattern is bursting when abort is called or upon exiting the context manager, keep alive pattern will not be stopped. To stop the keep alive pattern, call abort_keep_alive.

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        '''
        return _Burst(self)

    def close(self):
        '''close

        Closes the specified instrument session to a digital pattern instrument, aborts pattern execution, and unloads pattern memory. The channels on a digital pattern instrument remain in their current state.

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

        Stops bursting the pattern.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def abort_keep_alive(self):
        r'''abort_keep_alive

        Stops the keep alive pattern if it is currently running. If a pattern burst is in progress, the method aborts the pattern burst. If you start a new pattern burst while a keep alive pattern is running, the keep alive pattern runs to the last keep alive vector, and the new pattern burst starts on the next cycle.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_AbortKeepAlive(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def commit(self):
        r'''commit

        Applies all previously configured pin levels, termination modes, clocks, triggers, and pattern timing to a digital pattern instrument. If you do not call the commit method, then the initiate method or the burst_pattern method will implicitly call this method for you. Calling this method moves the session from the Uncommitted state to the Committed state.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_Commit(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_time_set_period(self, time_set_name, period):
        r'''configure_time_set_period

        Configures the period of a time set. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Args:
            time_set_name (str): The specified time set name.

            period (hightime.timedelta, datetime.timedelta, or float in seconds): Period for this time set, in seconds.

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

        Creates a capture waveform with the configuration information from a Digicapture file generated by the Digital Pattern Editor.

        Args:
            waveform_name (str): Waveform name you want to use. You must specify waveform_name if the file contains multiple waveforms. Use the waveform_name with the capture_start opcode in your pattern.

            waveform_file_path (str): Absolute file path to the capture waveform file (.digicapture) you want to load.

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

        Creates a source waveform with configuration information from a TDMS file generated by the Digital Pattern Editor. It also optionally writes waveform data from the file.

        Args:
            waveform_name (str): The waveform name you want to use from the file. You must specify waveform_name if the file contains multiple waveforms. Use the waveform_name with the source_start opcode in your pattern.

            waveform_file_path (str): Absolute file path to the load source waveform file (.tdms).

            write_waveform_data (bool): A Boolean that writes waveform data to source memory if True and the waveform data is in the file.

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

        Creates a time set with the name that you specify. Use this method when you want to create time sets programmatically rather than with a timing sheet.

        Args:
            name (str): The specified name of the new time set.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        name_ctype = ctypes.create_string_buffer(name.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_CreateTimeSet(vi_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def delete_all_time_sets(self):
        r'''delete_all_time_sets

        Deletes all time sets from instrument memory.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_DeleteAllTimeSets(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def load_specifications_levels_and_timing(self, specifications_file_paths=None, levels_file_paths=None, timing_file_paths=None):
        '''load_specifications_levels_and_timing

        Loads settings in specifications, levels, and timing sheets. These settings are not
        applied to the digital pattern instrument until apply_levels_and_timing is called.

        If the levels and timing sheets contains formulas, they are evaluated at load time.
        If the formulas refer to variables, the specifications sheets that define those
        variables must be loaded either first, or at the same time as the levels and timing sheets.

        Args:
            specifications_file_paths (str or basic sequence of str): Absolute file path of one or more specifications files.

            levels_file_paths (str or basic sequence of str): Absolute file path of one or more levels sheet files.

            timing_file_paths (str or basic sequence of str): Absolute file path of one or more timing sheet files.

        '''
        self._call_method_with_iterable(self._load_specifications, specifications_file_paths)
        self._call_method_with_iterable(self._load_levels, levels_file_paths)
        self._call_method_with_iterable(self._load_timing, timing_file_paths)

    def _call_method_with_iterable(self, method, files):
        if files is None:
            return
        if isinstance(files, str):
            files = [files]
        for f in files:
            method(f)

    @ivi_synchronized
    def self_test(self):
        '''self_test

        Returns self test results from a digital pattern instrument. This test requires several minutes to execute.

        Raises `SelfTestError` on self test failure. Properties on exception object:

        - code - failure code from driver
        - message - status message from driver

        +----------------+-------------------+
        | Self-Test Code | Description       |
        +================+===================+
        | 0              | Self test passed. |
        +----------------+-------------------+
        | 1              | Self test failed. |
        +----------------+-------------------+
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
            file_paths (str or basic sequence of str): Absolute file path of one or more loaded specifications files.

        '''
        self._call_method_with_iterable(self._unload_specifications, file_paths)

    @ivi_synchronized
    def write_source_waveform_site_unique(self, waveform_name, waveform_data):
        '''write_source_waveform_site_unique

        Writes one waveform per site. Use this write method if you set the parameter of the create source waveform method to Site Unique.

        Args:
            waveform_name (str): The name to assign to the waveform. Use the waveform_name with source_start opcode in your pattern.

            waveform_data ({ int: basic sequence of unsigned int, int: basic sequence of unsigned int, ... }): Dictionary where each key is a site number and value is a collection of samples to use as source data

        '''
        from collections.abc import Mapping
        if not isinstance(waveform_data, Mapping):
            raise TypeError("Expecting waveform_data to be a dictionary but got {}".format(type(waveform_data)))
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
    def get_pattern_pin_names(self, start_label):
        r'''get_pattern_pin_names

        Returns the pattern pin list.

        Args:
            start_label (str): Pattern name or exported pattern label from which to get the pin names that the pattern references.


        Returns:
            pin_list (list of str): List of pins referenced by the pattern with the **startLabel**.

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

        Returns the period of the specified time set.

        Args:
            time_set_name (str): The specified time set name.


        Returns:
            period (hightime.timedelta): Returned period, in seconds, that the edge is configured to.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        period_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDigital_GetTimeSetPeriod(vi_ctype, time_set_name_ctype, None if period_ctype is None else (ctypes.pointer(period_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_seconds_real64_to_timedelta(float(period_ctype.value))

    def _init_with_options(self, resource_name, id_query=False, reset_device=False, option_string=""):
        r'''_init_with_options

        Creates and returns a new session to the specified digital pattern instrument to use in all subsequent method calls. To place the instrument in a known startup state when creating a new session, set the reset parameter to True, which is equivalent to calling the reset method immediately after initializing the session.

        Args:
            resource_name (str): The specified resource name shown in Measurement & Automation Explorer (MAX) for a digital pattern instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. **resourceName** can also be a logical IVI name. This parameter accepts a comma-delimited list of strings in the form PXI1Slot2,PXI1Slot3, where ``PXI1Slot2`` is one instrument resource name and ``PXI1Slot3`` is another. When including more than one digital pattern instrument in the comma-delimited list of strings, list the instruments in the same order they appear in the pin map.

                +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | |Note| | Note   You only can specify multiple instruments of the same model. For example, you can list two PXIe-6570s but not a PXIe-6570 and PXIe-6571. The instruments must be in the same chassis. |
                +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                .. |Note| image:: note.gif

                Note:

            id_query (bool): A Boolean that verifies that the digital pattern instrument you initialize is supported by NI-Digital. NI-Digital automatically performs this query, so setting this parameter is not necessary.

            reset_device (bool): A Boolean that specifies whether to reset a digital pattern instrument to a known state when the session is initialized. Setting the **resetDevice** value to True is equivalent to calling the reset method immediately after initializing the session.

            option_string (dict): The initial values of certain properties for the NI-Digital Pattern Driver session. The string can be empty. You can use the DriverSetup flag to simulate a digital pattern instrument. When simulating a digital pattern instrument, you must specify the model you want to simulate. For example, Simulate = 1, DriverSetup = Model:6570.


        Returns:
            new_vi (int): The returned instrument session.

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

        Starts bursting the pattern configured by start_label, causing the NI-Digital session to be committed. To stop the pattern burst, call abort. If keep alive pattern is bursting when abort is called or upon exiting the context manager, keep alive pattern will not be stopped. To stop the keep alive pattern, call abort_keep_alive.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_Initiate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def is_done(self):
        r'''is_done

        Checks the hardware to determine if the pattern burst has completed or if any errors have occurred.

        Returns:
            done (bool): A Boolean that indicates whether the pattern burst completed.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        done_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDigital_IsDone(vi_ctype, None if done_ctype is None else (ctypes.pointer(done_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(done_ctype.value)

    @ivi_synchronized
    def _load_levels(self, file_path):
        r'''_load_levels

        Loads a levels sheet from a specified file.

        Args:
            file_path (str): Absolute file path to the specified levels sheet file.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadLevels(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def load_pattern(self, file_path):
        r'''load_pattern

        Loads the specified pattern file.

        Args:
            file_path (str): Absolute file path of the binary .digipat pattern file to load. Specify the pattern to burst using start_label or the start_label parameter of the burst_pattern method.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadPattern(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def load_pin_map(self, file_path):
        r'''load_pin_map

        Loads a pin map file. You can load only a single pin and channel map file during an NI-Digital Pattern Driver session. To switch pin maps, create a new session or call the reset method.

        Args:
            file_path (str): Absolute file path to a pin map file created with the Digital Pattern Editor or the NI TestStand Semiconductor Module.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadPinMap(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _load_specifications(self, file_path):
        r'''_load_specifications

        Loads a specifications sheet from a specified file.

        Args:
            file_path (str): Absolute file path to a specifications file.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadSpecifications(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _load_timing(self, file_path):
        r'''_load_timing

        Loads a timing sheet from a specified file.

        Args:
            file_path (str): Absolute file path to the specified timing sheet file.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadTiming(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def read_sequencer_flag(self, flag):
        r'''read_sequencer_flag

        Reads the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program.

        Args:
            flag (enums.SequencerFlag): The pattern sequencer flag you want to read.

                -   SequencerFlag.FLAG0 ("seqflag0"): Reads pattern sequencer flag 0.
                -   SequencerFlag.FLAG1 ("seqflag1"): Reads pattern sequencer flag 1.
                -   SequencerFlag.FLAG2 ("seqflag2"): Reads pattern sequencer flag 2.
                -   SequencerFlag.FLAG3 ("seqflag3"): Reads pattern sequencer flag 3.


        Returns:
            value (bool): A Boolean that indicates the state of the pattern sequencer flag you specify.

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

        Reads the value of a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program. For example, you can use this method to read a register modified by the write_reg opcode during a pattern burst.

        Args:
            reg (enums.SequencerRegister): The sequencer register to read from.

                -   SequencerRegister.REGISTER0 ("reg0"): Reads sequencer register 0.
                -   SequencerRegister.REGISTER1 ("reg1"): Reads sequencer register 1.
                -   SequencerRegister.REGISTER2 ("reg2"): Reads sequencer register 2.
                -   SequencerRegister.REGISTER3 ("reg3"): Reads sequencer register 3.
                -   SequencerRegister.REGISTER4 ("reg4"): Reads sequencer register 4.
                -   SequencerRegister.REGISTER5 ("reg5"): Reads sequencer register 5.
                -   SequencerRegister.REGISTER6 ("reg6"): Reads sequencer register 6.
                -   SequencerRegister.REGISTER7 ("reg7"): Reads sequencer register 7.
                -   SequencerRegister.REGISTER8 ("reg8"): Reads sequencer register 8.
                -   SequencerRegister.REGISTER9 ("reg9"): Reads sequencer register 9.
                -   SequencerRegister.REGISTER10 ("reg10"): Reads sequencer register 10.
                -   SequencerRegister.REGISTER11 ("reg11"): Reads sequencer register 11.
                -   SequencerRegister.REGISTER12 ("reg12"): Reads sequencer register 12.
                -   SequencerRegister.REGISTER13 ("reg13"): Reads sequencer register 13.
                -   SequencerRegister.REGISTER14 ("reg14"): Reads sequencer register 14.
                -   SequencerRegister.REGISTER15 ("reg15"): Reads sequencer register 15.


        Returns:
            value (int): Value read from the sequencer register.

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

        Returns a digital pattern instrument to a known state. This method performs the following actions:

        - Aborts pattern execution.
        - Clears pin maps, time sets, source and capture waveforms, and patterns.
        - Resets all properties to default values, including the selected_function property that is set to SelectedFunction.DISCONNECT, causing the I/O switches to open.
        - Stops export of all external signals and events.
        - Clears over-temperature and over-power conditions.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_ResetDevice(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def self_calibrate(self):
        r'''self_calibrate

        Performs self-calibration on a digital pattern instrument.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_SelfCalibrate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def send_software_edge_trigger(self, trigger, trigger_identifier):
        r'''send_software_edge_trigger

        Forces a particular edge-based trigger to occur regardless of how the specified trigger is configured. You can use this method as a software override.

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

        Unloads all patterns, source waveforms, and capture waveforms from a digital pattern instrument.

        Args:
            unload_keep_alive_pattern (bool): A Boolean that specifies whether to keep or unload the keep alive pattern.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        unload_keep_alive_pattern_ctype = _visatype.ViBoolean(unload_keep_alive_pattern)  # case S150
        error_code = self._library.niDigital_UnloadAllPatterns(vi_ctype, unload_keep_alive_pattern_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _unload_specifications(self, file_path):
        r'''_unload_specifications

        Unloads the given specifications sheet present in the previously loaded specifications file that you select. You must call the _load_specifications method to reload the file with updated specifications values. You must then call the apply_levels_and_timing method in order to apply the levels and timing values that reference the updated specifications values.

        Args:
            file_path (str): Absolute file path to a loaded specifications file.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_UnloadSpecifications(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def wait_until_done(self, timeout=hightime.timedelta(seconds=10.0)):
        r'''wait_until_done

        Waits until the pattern burst has completed or the timeout has expired.

        Args:
            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        error_code = self._library.niDigital_WaitUntilDone(vi_ctype, timeout_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def write_sequencer_flag(self, flag, value):
        r'''write_sequencer_flag

        Writes the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program.

        Args:
            flag (enums.SequencerFlag): The pattern sequencer flag to write.

                -   SequencerFlag.FLAG0 ("seqflag0"): Writes pattern sequencer flag 0.
                -   SequencerFlag.FLAG1 ("seqflag1"): Writes pattern sequencer flag 1.
                -   SequencerFlag.FLAG2 ("seqflag2"): Writes pattern sequencer flag 2.
                -   SequencerFlag.FLAG3 ("seqflag3"): Writes pattern sequencer flag 3.

            value (bool): A Boolean that assigns a state to the pattern sequencer flag you specify.

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

        Writes a value to a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program.

        Args:
            reg (enums.SequencerRegister): The sequencer register you want to write to.

                -   SequencerRegister.REGISTER0 ("reg0"): Writes sequencer register 0.
                -   SequencerRegister.REGISTER1 ("reg1"): Writes sequencer register 1.
                -   SequencerRegister.REGISTER2 ("reg2"): Writes sequencer register 2.
                -   SequencerRegister.REGISTER3 ("reg3"): Writes sequencer register 3.
                -   SequencerRegister.REGISTER4 ("reg4"): Writes sequencer register 4.
                -   SequencerRegister.REGISTER5 ("reg5"): Writes sequencer register 5.
                -   SequencerRegister.REGISTER6 ("reg6"): Writes sequencer register 6.
                -   SequencerRegister.REGISTER7 ("reg7"): Writes sequencer register 7.
                -   SequencerRegister.REGISTER8 ("reg8"): Writes sequencer register 8.
                -   SequencerRegister.REGISTER9 ("reg9"): Writes sequencer register 9.
                -   SequencerRegister.REGISTER10 ("reg10"): Writes sequencer register 10.
                -   SequencerRegister.REGISTER11 ("reg11"): Writes sequencer register 11.
                -   SequencerRegister.REGISTER12 ("reg12"): Writes sequencer register 12.
                -   SequencerRegister.REGISTER13 ("reg13"): Writes sequencer register 13.
                -   SequencerRegister.REGISTER14 ("reg14"): Writes sequencer register 14.
                -   SequencerRegister.REGISTER15 ("reg15"): Writes sequencer register 15.

            value (int): The value you want to write to the register.

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

        Writes the same waveform data to all sites. Use this write method if you set the data_mapping parameter of the create source waveform method to SourceDataMapping.BROADCAST.

        Args:
            waveform_name (str): The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

            waveform_data (list of int): 1D array of samples to use as source data to apply to all sites.

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

        Writes a source waveform based on the waveform data and configuration information the file contains.

        Args:
            waveform_name (str): The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

            waveform_file_path (str): Absolute file path to the load source waveform file (.tdms).

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        waveform_file_path_ctype = ctypes.create_string_buffer(waveform_file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_WriteSourceWaveformDataFromFileTDMS(vi_ctype, waveform_name_ctype, waveform_file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self):
        r'''_close

        Closes the specified instrument session to a digital pattern instrument, aborts pattern execution, and unloads pattern memory. The channels on a digital pattern instrument remain in their current state.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def reset(self):
        r'''reset

        Returns a digital pattern instrument to a known state. This method performs the following actions:

        - Aborts pattern execution.
        - Clears pin maps, time sets, source and capture waveforms, and patterns.
        - Resets all properties to default values, including the selected_function property that is set to SelectedFunction.DISCONNECT, causing the I/O switches to open.
        - Stops exporting all external signals and events.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _self_test(self):
        r'''_self_test

        Returns self test results from a digital pattern instrument. This test requires several minutes to execute.

        Returns:
            test_result (int): A parameter that indicates if the self test passed (0) or failed (!=0).

            test_message (str): The returned self test status message. The array must contain at least 256 characters.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        test_result_ctype = _visatype.ViInt16()  # case S220
        test_message_ctype = (_visatype.ViChar * 2048)()  # case C070
        error_code = self._library.niDigital_self_test(vi_ctype, None if test_result_ctype is None else (ctypes.pointer(test_result_ctype)), test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(test_result_ctype.value), test_message_ctype.value.decode(self._encoding)



