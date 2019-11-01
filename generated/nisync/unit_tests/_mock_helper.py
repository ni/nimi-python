# -*- coding: utf-8 -*-
# This file was generated
import sys  # noqa: F401   - Not all mock_helpers will need this


class MockFunctionCallError(Exception):
    def __init__(self, function, param=None):
        self.function = function
        self.param = param
        msg = "{0} called without setting side_effect".format(self.function)
        if param is not None:
            msg += " or setting the {0} parameter return value".format(self.param)
        super(Exception, self).__init__(msg)


class SideEffectsHelper(object):
    def __init__(self):
        self._defaults = {}
        self._defaults['ClearClock'] = {}
        self._defaults['ClearClock']['return'] = 0
        self._defaults['ClearFutureTimeEvents'] = {}
        self._defaults['ClearFutureTimeEvents']['return'] = 0
        self._defaults['ConfigureFpga'] = {}
        self._defaults['ConfigureFpga']['return'] = 0
        self._defaults['ConnectClkTerminals'] = {}
        self._defaults['ConnectClkTerminals']['return'] = 0
        self._defaults['ConnectSwTrigToTerminal'] = {}
        self._defaults['ConnectSwTrigToTerminal']['return'] = 0
        self._defaults['ConnectTrigTerminals'] = {}
        self._defaults['ConnectTrigTerminals']['return'] = 0
        self._defaults['CreateClock'] = {}
        self._defaults['CreateClock']['return'] = 0
        self._defaults['CreateFutureTimeEvent'] = {}
        self._defaults['CreateFutureTimeEvent']['return'] = 0
        self._defaults['DisableGpsTimestamping'] = {}
        self._defaults['DisableGpsTimestamping']['return'] = 0
        self._defaults['DisableIrigTimestamping'] = {}
        self._defaults['DisableIrigTimestamping']['return'] = 0
        self._defaults['DisableTimeStampTrigger'] = {}
        self._defaults['DisableTimeStampTrigger']['return'] = 0
        self._defaults['DisconnectClkTerminals'] = {}
        self._defaults['DisconnectClkTerminals']['return'] = 0
        self._defaults['DisconnectSwTrigFromTerminal'] = {}
        self._defaults['DisconnectSwTrigFromTerminal']['return'] = 0
        self._defaults['DisconnectTrigTerminals'] = {}
        self._defaults['DisconnectTrigTerminals']['return'] = 0
        self._defaults['EnableGpsTimestamping'] = {}
        self._defaults['EnableGpsTimestamping']['return'] = 0
        self._defaults['EnableIrigTimestamping'] = {}
        self._defaults['EnableIrigTimestamping']['return'] = 0
        self._defaults['EnableTimeStampTrigger'] = {}
        self._defaults['EnableTimeStampTrigger']['return'] = 0
        self._defaults['EnableTimeStampTriggerWithDecimation'] = {}
        self._defaults['EnableTimeStampTriggerWithDecimation']['return'] = 0
        self._defaults['GetAttributeViBoolean'] = {}
        self._defaults['GetAttributeViBoolean']['return'] = 0
        self._defaults['GetAttributeViBoolean']['attributeValue'] = None
        self._defaults['GetAttributeViInt32'] = {}
        self._defaults['GetAttributeViInt32']['return'] = 0
        self._defaults['GetAttributeViInt32']['attributeValue'] = None
        self._defaults['GetAttributeViReal64'] = {}
        self._defaults['GetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViReal64']['attributeValue'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['attributeValue'] = None
        self._defaults['GetLocation'] = {}
        self._defaults['GetLocation']['return'] = 0
        self._defaults['GetLocation']['latitude'] = None
        self._defaults['GetLocation']['longitude'] = None
        self._defaults['GetLocation']['altitude'] = None
        self._defaults['GetTime'] = {}
        self._defaults['GetTime']['return'] = 0
        self._defaults['GetTime']['timeSeconds'] = None
        self._defaults['GetTime']['timeNanoseconds'] = None
        self._defaults['GetTime']['timeFractionalNanoseconds'] = None
        self._defaults['GetTimeReferenceNames'] = {}
        self._defaults['GetTimeReferenceNames']['return'] = 0
        self._defaults['GetTimeReferenceNames']['timeReferenceNames'] = None
        self._defaults['GetVelocity'] = {}
        self._defaults['GetVelocity']['return'] = 0
        self._defaults['GetVelocity']['eastVelocity'] = None
        self._defaults['GetVelocity']['northVelocity'] = None
        self._defaults['GetVelocity']['upVelocity'] = None
        self._defaults['MeasureFrequency'] = {}
        self._defaults['MeasureFrequency']['return'] = 0
        self._defaults['MeasureFrequency']['actualDuration'] = None
        self._defaults['MeasureFrequency']['measuredFrequency'] = None
        self._defaults['MeasureFrequency']['frequencyError'] = None
        self._defaults['MeasureFrequencyEx'] = {}
        self._defaults['MeasureFrequencyEx']['return'] = 0
        self._defaults['MeasureFrequencyEx']['actualDuration'] = None
        self._defaults['MeasureFrequencyEx']['measuredFrequency'] = None
        self._defaults['MeasureFrequencyEx']['frequencyError'] = None
        self._defaults['PersistConfig'] = {}
        self._defaults['PersistConfig']['return'] = 0
        self._defaults['ReadCurrentTemperature'] = {}
        self._defaults['ReadCurrentTemperature']['return'] = 0
        self._defaults['ReadCurrentTemperature']['temperature'] = None
        self._defaults['ReadLastGpsTimestamp'] = {}
        self._defaults['ReadLastGpsTimestamp']['return'] = 0
        self._defaults['ReadLastGpsTimestamp']['timeSeconds'] = None
        self._defaults['ReadLastGpsTimestamp']['timeNanoseconds'] = None
        self._defaults['ReadLastGpsTimestamp']['timeFractionalNanoseconds'] = None
        self._defaults['ReadLastGpsTimestamp']['gpsSeconds'] = None
        self._defaults['ReadLastGpsTimestamp']['gpsNanoseconds'] = None
        self._defaults['ReadLastGpsTimestamp']['gpsFractionalNanoseconds'] = None
        self._defaults['ReadLastIrigTimestamp'] = {}
        self._defaults['ReadLastIrigTimestamp']['return'] = 0
        self._defaults['ReadLastIrigTimestamp']['timeSeconds'] = None
        self._defaults['ReadLastIrigTimestamp']['timeNanoseconds'] = None
        self._defaults['ReadLastIrigTimestamp']['timeFractionalNanoseconds'] = None
        self._defaults['ReadLastIrigTimestamp']['irigSeconds'] = None
        self._defaults['ReadLastIrigTimestamp']['irigNanoseconds'] = None
        self._defaults['ReadLastIrigTimestamp']['irigFractionalNanoseconds'] = None
        self._defaults['ReadMultipleTriggerTimeStamp'] = {}
        self._defaults['ReadMultipleTriggerTimeStamp']['return'] = 0
        self._defaults['ReadMultipleTriggerTimeStamp']['timeSeconds'] = None
        self._defaults['ReadMultipleTriggerTimeStamp']['timeNanoseconds'] = None
        self._defaults['ReadMultipleTriggerTimeStamp']['timeFractionalNanoseconds'] = None
        self._defaults['ReadMultipleTriggerTimeStamp']['detectedEdgeBuffer'] = None
        self._defaults['ReadMultipleTriggerTimeStamp']['timeStampsRead'] = None
        self._defaults['ReadTriggerTimeStamp'] = {}
        self._defaults['ReadTriggerTimeStamp']['return'] = 0
        self._defaults['ReadTriggerTimeStamp']['timeSeconds'] = None
        self._defaults['ReadTriggerTimeStamp']['timeNanoseconds'] = None
        self._defaults['ReadTriggerTimeStamp']['timeFractionalNanoseconds'] = None
        self._defaults['ReadTriggerTimeStamp']['detectedEdge'] = None
        self._defaults['ResetFrequency'] = {}
        self._defaults['ResetFrequency']['return'] = 0
        self._defaults['SendSoftwareTrigger'] = {}
        self._defaults['SendSoftwareTrigger']['return'] = 0
        self._defaults['SetAttributeViBoolean'] = {}
        self._defaults['SetAttributeViBoolean']['return'] = 0
        self._defaults['SetAttributeViInt32'] = {}
        self._defaults['SetAttributeViInt32']['return'] = 0
        self._defaults['SetAttributeViReal64'] = {}
        self._defaults['SetAttributeViReal64']['return'] = 0
        self._defaults['SetAttributeViString'] = {}
        self._defaults['SetAttributeViString']['return'] = 0
        self._defaults['SetTime'] = {}
        self._defaults['SetTime']['return'] = 0
        self._defaults['SetTimeReference1588OrdinaryClock'] = {}
        self._defaults['SetTimeReference1588OrdinaryClock']['return'] = 0
        self._defaults['SetTimeReferenceFreeRunning'] = {}
        self._defaults['SetTimeReferenceFreeRunning']['return'] = 0
        self._defaults['SetTimeReferenceGps'] = {}
        self._defaults['SetTimeReferenceGps']['return'] = 0
        self._defaults['SetTimeReferenceIrig'] = {}
        self._defaults['SetTimeReferenceIrig']['return'] = 0
        self._defaults['SetTimeReferencePps'] = {}
        self._defaults['SetTimeReferencePps']['return'] = 0
        self._defaults['Start1588'] = {}
        self._defaults['Start1588']['return'] = 0
        self._defaults['Stop1588'] = {}
        self._defaults['Stop1588']['return'] = 0
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0
        self._defaults['error_message'] = {}
        self._defaults['error_message']['return'] = 0
        self._defaults['error_message']['errorMessage'] = None
        self._defaults['init'] = {}
        self._defaults['init']['return'] = 0
        self._defaults['init']['vi'] = None
        self._defaults['reset'] = {}
        self._defaults['reset']['return'] = 0
        self._defaults['revision_query'] = {}
        self._defaults['revision_query']['return'] = 0
        self._defaults['revision_query']['instrumentDriverRevision'] = None
        self._defaults['revision_query']['firmwareRevision'] = None
        self._defaults['self_test'] = {}
        self._defaults['self_test']['return'] = 0
        self._defaults['self_test']['selfTestResult'] = None
        self._defaults['self_test']['selfTestMessage'] = None

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niSync_ClearClock(self, vi, terminal):  # noqa: N802
        if self._defaults['ClearClock']['return'] != 0:
            return self._defaults['ClearClock']['return']
        return self._defaults['ClearClock']['return']

    def niSync_ClearFutureTimeEvents(self, vi, terminal):  # noqa: N802
        if self._defaults['ClearFutureTimeEvents']['return'] != 0:
            return self._defaults['ClearFutureTimeEvents']['return']
        return self._defaults['ClearFutureTimeEvents']['return']

    def niSync_ConfigureFpga(self, vi, fpga_program_path):  # noqa: N802
        if self._defaults['ConfigureFpga']['return'] != 0:
            return self._defaults['ConfigureFpga']['return']
        return self._defaults['ConfigureFpga']['return']

    def niSync_ConnectClkTerminals(self, vi, source_terminal, destination_terminal):  # noqa: N802
        if self._defaults['ConnectClkTerminals']['return'] != 0:
            return self._defaults['ConnectClkTerminals']['return']
        return self._defaults['ConnectClkTerminals']['return']

    def niSync_ConnectSwTrigToTerminal(self, vi, source_terminal, destination_terminal, synchronization_clock, invert, update_edge, delay):  # noqa: N802
        if self._defaults['ConnectSwTrigToTerminal']['return'] != 0:
            return self._defaults['ConnectSwTrigToTerminal']['return']
        return self._defaults['ConnectSwTrigToTerminal']['return']

    def niSync_ConnectTrigTerminals(self, vi, source_terminal, destination_terminal, synchronization_clock, invert, update_edge):  # noqa: N802
        if self._defaults['ConnectTrigTerminals']['return'] != 0:
            return self._defaults['ConnectTrigTerminals']['return']
        return self._defaults['ConnectTrigTerminals']['return']

    def niSync_CreateClock(self, vi, terminal, high_ticks, low_ticks, start_time_seconds, start_time_nanoseconds, start_time_fractional_nsecs, stop_time_seconds, stop_time_nanoseconds, stop_time_fractional_nsecs):  # noqa: N802
        if self._defaults['CreateClock']['return'] != 0:
            return self._defaults['CreateClock']['return']
        return self._defaults['CreateClock']['return']

    def niSync_CreateFutureTimeEvent(self, vi, terminal, output_level, time_seconds, time_nanoseconds, time_fractional_nanoseconds):  # noqa: N802
        if self._defaults['CreateFutureTimeEvent']['return'] != 0:
            return self._defaults['CreateFutureTimeEvent']['return']
        return self._defaults['CreateFutureTimeEvent']['return']

    def niSync_DisableGpsTimestamping(self, vi):  # noqa: N802
        if self._defaults['DisableGpsTimestamping']['return'] != 0:
            return self._defaults['DisableGpsTimestamping']['return']
        return self._defaults['DisableGpsTimestamping']['return']

    def niSync_DisableIrigTimestamping(self, vi, terminal_name):  # noqa: N802
        if self._defaults['DisableIrigTimestamping']['return'] != 0:
            return self._defaults['DisableIrigTimestamping']['return']
        return self._defaults['DisableIrigTimestamping']['return']

    def niSync_DisableTimeStampTrigger(self, vi, terminal):  # noqa: N802
        if self._defaults['DisableTimeStampTrigger']['return'] != 0:
            return self._defaults['DisableTimeStampTrigger']['return']
        return self._defaults['DisableTimeStampTrigger']['return']

    def niSync_DisconnectClkTerminals(self, vi, source_terminal, destination_terminal):  # noqa: N802
        if self._defaults['DisconnectClkTerminals']['return'] != 0:
            return self._defaults['DisconnectClkTerminals']['return']
        return self._defaults['DisconnectClkTerminals']['return']

    def niSync_DisconnectSwTrigFromTerminal(self, vi, source_terminal, destination_terminal):  # noqa: N802
        if self._defaults['DisconnectSwTrigFromTerminal']['return'] != 0:
            return self._defaults['DisconnectSwTrigFromTerminal']['return']
        return self._defaults['DisconnectSwTrigFromTerminal']['return']

    def niSync_DisconnectTrigTerminals(self, vi, source_terminal, destination_terminal):  # noqa: N802
        if self._defaults['DisconnectTrigTerminals']['return'] != 0:
            return self._defaults['DisconnectTrigTerminals']['return']
        return self._defaults['DisconnectTrigTerminals']['return']

    def niSync_EnableGpsTimestamping(self, vi):  # noqa: N802
        if self._defaults['EnableGpsTimestamping']['return'] != 0:
            return self._defaults['EnableGpsTimestamping']['return']
        return self._defaults['EnableGpsTimestamping']['return']

    def niSync_EnableIrigTimestamping(self, vi, irig_type, terminal_name):  # noqa: N802
        if self._defaults['EnableIrigTimestamping']['return'] != 0:
            return self._defaults['EnableIrigTimestamping']['return']
        return self._defaults['EnableIrigTimestamping']['return']

    def niSync_EnableTimeStampTrigger(self, vi, terminal, active_edge):  # noqa: N802
        if self._defaults['EnableTimeStampTrigger']['return'] != 0:
            return self._defaults['EnableTimeStampTrigger']['return']
        return self._defaults['EnableTimeStampTrigger']['return']

    def niSync_EnableTimeStampTriggerWithDecimation(self, vi, terminal, active_edge, decimation_count):  # noqa: N802
        if self._defaults['EnableTimeStampTriggerWithDecimation']['return'] != 0:
            return self._defaults['EnableTimeStampTriggerWithDecimation']['return']
        return self._defaults['EnableTimeStampTriggerWithDecimation']['return']

    def niSync_GetAttributeViBoolean(self, vi, active_item, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        # attribute_value
        if self._defaults['GetAttributeViBoolean']['attributeValue'] is None:
            raise MockFunctionCallError("niSync_GetAttributeViBoolean", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViBoolean']['attributeValue']
        return self._defaults['GetAttributeViBoolean']['return']

    def niSync_GetAttributeViInt32(self, vi, active_item, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # attribute_value
        if self._defaults['GetAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niSync_GetAttributeViInt32", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViInt32']['attributeValue']
        return self._defaults['GetAttributeViInt32']['return']

    def niSync_GetAttributeViReal64(self, vi, active_item, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # attribute_value
        if self._defaults['GetAttributeViReal64']['attributeValue'] is None:
            raise MockFunctionCallError("niSync_GetAttributeViReal64", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViReal64']['attributeValue']
        return self._defaults['GetAttributeViReal64']['return']

    def niSync_GetAttributeViString(self, vi, active_item, attribute_id, buffer_size, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        if self._defaults['GetAttributeViString']['attributeValue'] is None:
            raise MockFunctionCallError("niSync_GetAttributeViString", param='attributeValue')
        if buffer_size.value == 0:
            return len(self._defaults['GetAttributeViString']['attributeValue'])
        attribute_value.value = self._defaults['GetAttributeViString']['attributeValue'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niSync_GetLocation(self, vi, latitude, longitude, altitude):  # noqa: N802
        if self._defaults['GetLocation']['return'] != 0:
            return self._defaults['GetLocation']['return']
        # latitude
        if self._defaults['GetLocation']['latitude'] is None:
            raise MockFunctionCallError("niSync_GetLocation", param='latitude')
        if latitude is not None:
            latitude.contents.value = self._defaults['GetLocation']['latitude']
        # longitude
        if self._defaults['GetLocation']['longitude'] is None:
            raise MockFunctionCallError("niSync_GetLocation", param='longitude')
        if longitude is not None:
            longitude.contents.value = self._defaults['GetLocation']['longitude']
        # altitude
        if self._defaults['GetLocation']['altitude'] is None:
            raise MockFunctionCallError("niSync_GetLocation", param='altitude')
        if altitude is not None:
            altitude.contents.value = self._defaults['GetLocation']['altitude']
        return self._defaults['GetLocation']['return']

    def niSync_GetTime(self, vi, time_seconds, time_nanoseconds, time_fractional_nanoseconds):  # noqa: N802
        if self._defaults['GetTime']['return'] != 0:
            return self._defaults['GetTime']['return']
        # time_seconds
        if self._defaults['GetTime']['timeSeconds'] is None:
            raise MockFunctionCallError("niSync_GetTime", param='timeSeconds')
        if time_seconds is not None:
            time_seconds.contents.value = self._defaults['GetTime']['timeSeconds']
        # time_nanoseconds
        if self._defaults['GetTime']['timeNanoseconds'] is None:
            raise MockFunctionCallError("niSync_GetTime", param='timeNanoseconds')
        if time_nanoseconds is not None:
            time_nanoseconds.contents.value = self._defaults['GetTime']['timeNanoseconds']
        # time_fractional_nanoseconds
        if self._defaults['GetTime']['timeFractionalNanoseconds'] is None:
            raise MockFunctionCallError("niSync_GetTime", param='timeFractionalNanoseconds')
        if time_fractional_nanoseconds is not None:
            time_fractional_nanoseconds.contents.value = self._defaults['GetTime']['timeFractionalNanoseconds']
        return self._defaults['GetTime']['return']

    def niSync_GetTimeReferenceNames(self, vi, buffer_size, time_reference_names):  # noqa: N802
        if self._defaults['GetTimeReferenceNames']['return'] != 0:
            return self._defaults['GetTimeReferenceNames']['return']
        if self._defaults['GetTimeReferenceNames']['timeReferenceNames'] is None:
            raise MockFunctionCallError("niSync_GetTimeReferenceNames", param='timeReferenceNames')
        if buffer_size.value == 0:
            return len(self._defaults['GetTimeReferenceNames']['timeReferenceNames'])
        time_reference_names.value = self._defaults['GetTimeReferenceNames']['timeReferenceNames'].encode('ascii')
        return self._defaults['GetTimeReferenceNames']['return']

    def niSync_GetVelocity(self, vi, east_velocity, north_velocity, up_velocity):  # noqa: N802
        if self._defaults['GetVelocity']['return'] != 0:
            return self._defaults['GetVelocity']['return']
        # east_velocity
        if self._defaults['GetVelocity']['eastVelocity'] is None:
            raise MockFunctionCallError("niSync_GetVelocity", param='eastVelocity')
        if east_velocity is not None:
            east_velocity.contents.value = self._defaults['GetVelocity']['eastVelocity']
        # north_velocity
        if self._defaults['GetVelocity']['northVelocity'] is None:
            raise MockFunctionCallError("niSync_GetVelocity", param='northVelocity')
        if north_velocity is not None:
            north_velocity.contents.value = self._defaults['GetVelocity']['northVelocity']
        # up_velocity
        if self._defaults['GetVelocity']['upVelocity'] is None:
            raise MockFunctionCallError("niSync_GetVelocity", param='upVelocity')
        if up_velocity is not None:
            up_velocity.contents.value = self._defaults['GetVelocity']['upVelocity']
        return self._defaults['GetVelocity']['return']

    def niSync_MeasureFrequency(self, vi, source_terminal, duration, actual_duration, measured_frequency, frequency_error):  # noqa: N802
        if self._defaults['MeasureFrequency']['return'] != 0:
            return self._defaults['MeasureFrequency']['return']
        # actual_duration
        if self._defaults['MeasureFrequency']['actualDuration'] is None:
            raise MockFunctionCallError("niSync_MeasureFrequency", param='actualDuration')
        if actual_duration is not None:
            actual_duration.contents.value = self._defaults['MeasureFrequency']['actualDuration']
        # measured_frequency
        if self._defaults['MeasureFrequency']['measuredFrequency'] is None:
            raise MockFunctionCallError("niSync_MeasureFrequency", param='measuredFrequency')
        if measured_frequency is not None:
            measured_frequency.contents.value = self._defaults['MeasureFrequency']['measuredFrequency']
        # frequency_error
        if self._defaults['MeasureFrequency']['frequencyError'] is None:
            raise MockFunctionCallError("niSync_MeasureFrequency", param='frequencyError')
        if frequency_error is not None:
            frequency_error.contents.value = self._defaults['MeasureFrequency']['frequencyError']
        return self._defaults['MeasureFrequency']['return']

    def niSync_MeasureFrequencyEx(self, vi, source_terminal, duration, decimation_count, actual_duration, measured_frequency, frequency_error):  # noqa: N802
        if self._defaults['MeasureFrequencyEx']['return'] != 0:
            return self._defaults['MeasureFrequencyEx']['return']
        # actual_duration
        if self._defaults['MeasureFrequencyEx']['actualDuration'] is None:
            raise MockFunctionCallError("niSync_MeasureFrequencyEx", param='actualDuration')
        if actual_duration is not None:
            actual_duration.contents.value = self._defaults['MeasureFrequencyEx']['actualDuration']
        # measured_frequency
        if self._defaults['MeasureFrequencyEx']['measuredFrequency'] is None:
            raise MockFunctionCallError("niSync_MeasureFrequencyEx", param='measuredFrequency')
        if measured_frequency is not None:
            measured_frequency.contents.value = self._defaults['MeasureFrequencyEx']['measuredFrequency']
        # frequency_error
        if self._defaults['MeasureFrequencyEx']['frequencyError'] is None:
            raise MockFunctionCallError("niSync_MeasureFrequencyEx", param='frequencyError')
        if frequency_error is not None:
            frequency_error.contents.value = self._defaults['MeasureFrequencyEx']['frequencyError']
        return self._defaults['MeasureFrequencyEx']['return']

    def niSync_PersistConfig(self, vi):  # noqa: N802
        if self._defaults['PersistConfig']['return'] != 0:
            return self._defaults['PersistConfig']['return']
        return self._defaults['PersistConfig']['return']

    def niSync_ReadCurrentTemperature(self, vi, temperature):  # noqa: N802
        if self._defaults['ReadCurrentTemperature']['return'] != 0:
            return self._defaults['ReadCurrentTemperature']['return']
        # temperature
        if self._defaults['ReadCurrentTemperature']['temperature'] is None:
            raise MockFunctionCallError("niSync_ReadCurrentTemperature", param='temperature')
        if temperature is not None:
            temperature.contents.value = self._defaults['ReadCurrentTemperature']['temperature']
        return self._defaults['ReadCurrentTemperature']['return']

    def niSync_ReadLastGpsTimestamp(self, vi, time_seconds, time_nanoseconds, time_fractional_nanoseconds, gps_seconds, gps_nanoseconds, gps_fractional_nanoseconds):  # noqa: N802
        if self._defaults['ReadLastGpsTimestamp']['return'] != 0:
            return self._defaults['ReadLastGpsTimestamp']['return']
        # time_seconds
        if self._defaults['ReadLastGpsTimestamp']['timeSeconds'] is None:
            raise MockFunctionCallError("niSync_ReadLastGpsTimestamp", param='timeSeconds')
        if time_seconds is not None:
            time_seconds.contents.value = self._defaults['ReadLastGpsTimestamp']['timeSeconds']
        # time_nanoseconds
        if self._defaults['ReadLastGpsTimestamp']['timeNanoseconds'] is None:
            raise MockFunctionCallError("niSync_ReadLastGpsTimestamp", param='timeNanoseconds')
        if time_nanoseconds is not None:
            time_nanoseconds.contents.value = self._defaults['ReadLastGpsTimestamp']['timeNanoseconds']
        # time_fractional_nanoseconds
        if self._defaults['ReadLastGpsTimestamp']['timeFractionalNanoseconds'] is None:
            raise MockFunctionCallError("niSync_ReadLastGpsTimestamp", param='timeFractionalNanoseconds')
        if time_fractional_nanoseconds is not None:
            time_fractional_nanoseconds.contents.value = self._defaults['ReadLastGpsTimestamp']['timeFractionalNanoseconds']
        # gps_seconds
        if self._defaults['ReadLastGpsTimestamp']['gpsSeconds'] is None:
            raise MockFunctionCallError("niSync_ReadLastGpsTimestamp", param='gpsSeconds')
        if gps_seconds is not None:
            gps_seconds.contents.value = self._defaults['ReadLastGpsTimestamp']['gpsSeconds']
        # gps_nanoseconds
        if self._defaults['ReadLastGpsTimestamp']['gpsNanoseconds'] is None:
            raise MockFunctionCallError("niSync_ReadLastGpsTimestamp", param='gpsNanoseconds')
        if gps_nanoseconds is not None:
            gps_nanoseconds.contents.value = self._defaults['ReadLastGpsTimestamp']['gpsNanoseconds']
        # gps_fractional_nanoseconds
        if self._defaults['ReadLastGpsTimestamp']['gpsFractionalNanoseconds'] is None:
            raise MockFunctionCallError("niSync_ReadLastGpsTimestamp", param='gpsFractionalNanoseconds')
        if gps_fractional_nanoseconds is not None:
            gps_fractional_nanoseconds.contents.value = self._defaults['ReadLastGpsTimestamp']['gpsFractionalNanoseconds']
        return self._defaults['ReadLastGpsTimestamp']['return']

    def niSync_ReadLastIrigTimestamp(self, vi, time_seconds, time_nanoseconds, time_fractional_nanoseconds, irig_seconds, irig_nanoseconds, irig_fractional_nanoseconds):  # noqa: N802
        if self._defaults['ReadLastIrigTimestamp']['return'] != 0:
            return self._defaults['ReadLastIrigTimestamp']['return']
        # time_seconds
        if self._defaults['ReadLastIrigTimestamp']['timeSeconds'] is None:
            raise MockFunctionCallError("niSync_ReadLastIrigTimestamp", param='timeSeconds')
        if time_seconds is not None:
            time_seconds.contents.value = self._defaults['ReadLastIrigTimestamp']['timeSeconds']
        # time_nanoseconds
        if self._defaults['ReadLastIrigTimestamp']['timeNanoseconds'] is None:
            raise MockFunctionCallError("niSync_ReadLastIrigTimestamp", param='timeNanoseconds')
        if time_nanoseconds is not None:
            time_nanoseconds.contents.value = self._defaults['ReadLastIrigTimestamp']['timeNanoseconds']
        # time_fractional_nanoseconds
        if self._defaults['ReadLastIrigTimestamp']['timeFractionalNanoseconds'] is None:
            raise MockFunctionCallError("niSync_ReadLastIrigTimestamp", param='timeFractionalNanoseconds')
        if time_fractional_nanoseconds is not None:
            time_fractional_nanoseconds.contents.value = self._defaults['ReadLastIrigTimestamp']['timeFractionalNanoseconds']
        # irig_seconds
        if self._defaults['ReadLastIrigTimestamp']['irigSeconds'] is None:
            raise MockFunctionCallError("niSync_ReadLastIrigTimestamp", param='irigSeconds')
        if irig_seconds is not None:
            irig_seconds.contents.value = self._defaults['ReadLastIrigTimestamp']['irigSeconds']
        # irig_nanoseconds
        if self._defaults['ReadLastIrigTimestamp']['irigNanoseconds'] is None:
            raise MockFunctionCallError("niSync_ReadLastIrigTimestamp", param='irigNanoseconds')
        if irig_nanoseconds is not None:
            irig_nanoseconds.contents.value = self._defaults['ReadLastIrigTimestamp']['irigNanoseconds']
        # irig_fractional_nanoseconds
        if self._defaults['ReadLastIrigTimestamp']['irigFractionalNanoseconds'] is None:
            raise MockFunctionCallError("niSync_ReadLastIrigTimestamp", param='irigFractionalNanoseconds')
        if irig_fractional_nanoseconds is not None:
            irig_fractional_nanoseconds.contents.value = self._defaults['ReadLastIrigTimestamp']['irigFractionalNanoseconds']
        return self._defaults['ReadLastIrigTimestamp']['return']

    def niSync_ReadMultipleTriggerTimeStamp(self, vi, terminal, time_stamps_to_read, timeout, time_seconds, time_nanoseconds, time_fractional_nanoseconds, detected_edge_buffer, time_stamps_read):  # noqa: N802
        if self._defaults['ReadMultipleTriggerTimeStamp']['return'] != 0:
            return self._defaults['ReadMultipleTriggerTimeStamp']['return']
        # time_seconds
        if self._defaults['ReadMultipleTriggerTimeStamp']['timeSeconds'] is None:
            raise MockFunctionCallError("niSync_ReadMultipleTriggerTimeStamp", param='timeSeconds')
        if time_seconds is not None:
            time_seconds.contents.value = self._defaults['ReadMultipleTriggerTimeStamp']['timeSeconds']
        # time_nanoseconds
        if self._defaults['ReadMultipleTriggerTimeStamp']['timeNanoseconds'] is None:
            raise MockFunctionCallError("niSync_ReadMultipleTriggerTimeStamp", param='timeNanoseconds')
        if time_nanoseconds is not None:
            time_nanoseconds.contents.value = self._defaults['ReadMultipleTriggerTimeStamp']['timeNanoseconds']
        # time_fractional_nanoseconds
        if self._defaults['ReadMultipleTriggerTimeStamp']['timeFractionalNanoseconds'] is None:
            raise MockFunctionCallError("niSync_ReadMultipleTriggerTimeStamp", param='timeFractionalNanoseconds')
        if time_fractional_nanoseconds is not None:
            time_fractional_nanoseconds.contents.value = self._defaults['ReadMultipleTriggerTimeStamp']['timeFractionalNanoseconds']
        # detected_edge_buffer
        if self._defaults['ReadMultipleTriggerTimeStamp']['detectedEdgeBuffer'] is None:
            raise MockFunctionCallError("niSync_ReadMultipleTriggerTimeStamp", param='detectedEdgeBuffer')
        if detected_edge_buffer is not None:
            detected_edge_buffer.contents.value = self._defaults['ReadMultipleTriggerTimeStamp']['detectedEdgeBuffer']
        # time_stamps_read
        if self._defaults['ReadMultipleTriggerTimeStamp']['timeStampsRead'] is None:
            raise MockFunctionCallError("niSync_ReadMultipleTriggerTimeStamp", param='timeStampsRead')
        if time_stamps_read is not None:
            time_stamps_read.contents.value = self._defaults['ReadMultipleTriggerTimeStamp']['timeStampsRead']
        return self._defaults['ReadMultipleTriggerTimeStamp']['return']

    def niSync_ReadTriggerTimeStamp(self, vi, terminal, timeout, time_seconds, time_nanoseconds, time_fractional_nanoseconds, detected_edge):  # noqa: N802
        if self._defaults['ReadTriggerTimeStamp']['return'] != 0:
            return self._defaults['ReadTriggerTimeStamp']['return']
        # time_seconds
        if self._defaults['ReadTriggerTimeStamp']['timeSeconds'] is None:
            raise MockFunctionCallError("niSync_ReadTriggerTimeStamp", param='timeSeconds')
        if time_seconds is not None:
            time_seconds.contents.value = self._defaults['ReadTriggerTimeStamp']['timeSeconds']
        # time_nanoseconds
        if self._defaults['ReadTriggerTimeStamp']['timeNanoseconds'] is None:
            raise MockFunctionCallError("niSync_ReadTriggerTimeStamp", param='timeNanoseconds')
        if time_nanoseconds is not None:
            time_nanoseconds.contents.value = self._defaults['ReadTriggerTimeStamp']['timeNanoseconds']
        # time_fractional_nanoseconds
        if self._defaults['ReadTriggerTimeStamp']['timeFractionalNanoseconds'] is None:
            raise MockFunctionCallError("niSync_ReadTriggerTimeStamp", param='timeFractionalNanoseconds')
        if time_fractional_nanoseconds is not None:
            time_fractional_nanoseconds.contents.value = self._defaults['ReadTriggerTimeStamp']['timeFractionalNanoseconds']
        # detected_edge
        if self._defaults['ReadTriggerTimeStamp']['detectedEdge'] is None:
            raise MockFunctionCallError("niSync_ReadTriggerTimeStamp", param='detectedEdge')
        if detected_edge is not None:
            detected_edge.contents.value = self._defaults['ReadTriggerTimeStamp']['detectedEdge']
        return self._defaults['ReadTriggerTimeStamp']['return']

    def niSync_ResetFrequency(self, vi):  # noqa: N802
        if self._defaults['ResetFrequency']['return'] != 0:
            return self._defaults['ResetFrequency']['return']
        return self._defaults['ResetFrequency']['return']

    def niSync_SendSoftwareTrigger(self, vi, source_terminal):  # noqa: N802
        if self._defaults['SendSoftwareTrigger']['return'] != 0:
            return self._defaults['SendSoftwareTrigger']['return']
        return self._defaults['SendSoftwareTrigger']['return']

    def niSync_SetAttributeViBoolean(self, vi, active_item, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niSync_SetAttributeViInt32(self, vi, active_item, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niSync_SetAttributeViReal64(self, vi, active_item, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niSync_SetAttributeViString(self, vi, active_item, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niSync_SetTime(self, vi, time_source, time_seconds, time_nanoseconds, time_fractional_nanoseconds):  # noqa: N802
        if self._defaults['SetTime']['return'] != 0:
            return self._defaults['SetTime']['return']
        return self._defaults['SetTime']['return']

    def niSync_SetTimeReference1588OrdinaryClock(self, vi):  # noqa: N802
        if self._defaults['SetTimeReference1588OrdinaryClock']['return'] != 0:
            return self._defaults['SetTimeReference1588OrdinaryClock']['return']
        return self._defaults['SetTimeReference1588OrdinaryClock']['return']

    def niSync_SetTimeReferenceFreeRunning(self, vi):  # noqa: N802
        if self._defaults['SetTimeReferenceFreeRunning']['return'] != 0:
            return self._defaults['SetTimeReferenceFreeRunning']['return']
        return self._defaults['SetTimeReferenceFreeRunning']['return']

    def niSync_SetTimeReferenceGps(self, vi):  # noqa: N802
        if self._defaults['SetTimeReferenceGps']['return'] != 0:
            return self._defaults['SetTimeReferenceGps']['return']
        return self._defaults['SetTimeReferenceGps']['return']

    def niSync_SetTimeReferenceIrig(self, vi, irig_type, terminal_name):  # noqa: N802
        if self._defaults['SetTimeReferenceIrig']['return'] != 0:
            return self._defaults['SetTimeReferenceIrig']['return']
        return self._defaults['SetTimeReferenceIrig']['return']

    def niSync_SetTimeReferencePps(self, vi, terminal_name, use_manual_time, initial_time_seconds, initial_nanoseconds, initial_fractional_nanoseconds):  # noqa: N802
        if self._defaults['SetTimeReferencePps']['return'] != 0:
            return self._defaults['SetTimeReferencePps']['return']
        return self._defaults['SetTimeReferencePps']['return']

    def niSync_Start1588(self, vi):  # noqa: N802
        if self._defaults['Start1588']['return'] != 0:
            return self._defaults['Start1588']['return']
        return self._defaults['Start1588']['return']

    def niSync_Stop1588(self, vi):  # noqa: N802
        if self._defaults['Stop1588']['return'] != 0:
            return self._defaults['Stop1588']['return']
        return self._defaults['Stop1588']['return']

    def niSync_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niSync_error_message(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['error_message']['return'] != 0:
            return self._defaults['error_message']['return']
        # error_message
        if self._defaults['error_message']['errorMessage'] is None:
            raise MockFunctionCallError("niSync_error_message", param='errorMessage')
        test_value = self._defaults['error_message']['errorMessage']
        if sys.version_info.major > 2 and type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(error_message) >= len(test_value)
        for i in range(len(test_value)):
            error_message[i] = test_value[i]
        return self._defaults['error_message']['return']

    def niSync_init(self, resource_name, id_query, reset_device, vi):  # noqa: N802
        if self._defaults['init']['return'] != 0:
            return self._defaults['init']['return']
        # vi
        if self._defaults['init']['vi'] is None:
            raise MockFunctionCallError("niSync_init", param='vi')
        if vi is not None:
            vi.contents.value = self._defaults['init']['vi']
        return self._defaults['init']['return']

    def niSync_reset(self, vi):  # noqa: N802
        if self._defaults['reset']['return'] != 0:
            return self._defaults['reset']['return']
        return self._defaults['reset']['return']

    def niSync_revision_query(self, vi, instrument_driver_revision, firmware_revision):  # noqa: N802
        if self._defaults['revision_query']['return'] != 0:
            return self._defaults['revision_query']['return']
        # instrument_driver_revision
        if self._defaults['revision_query']['instrumentDriverRevision'] is None:
            raise MockFunctionCallError("niSync_revision_query", param='instrumentDriverRevision')
        test_value = self._defaults['revision_query']['instrumentDriverRevision']
        if sys.version_info.major > 2 and type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(instrument_driver_revision) >= len(test_value)
        for i in range(len(test_value)):
            instrument_driver_revision[i] = test_value[i]
        # firmware_revision
        if self._defaults['revision_query']['firmwareRevision'] is None:
            raise MockFunctionCallError("niSync_revision_query", param='firmwareRevision')
        test_value = self._defaults['revision_query']['firmwareRevision']
        if sys.version_info.major > 2 and type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(firmware_revision) >= len(test_value)
        for i in range(len(test_value)):
            firmware_revision[i] = test_value[i]
        return self._defaults['revision_query']['return']

    def niSync_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        # self_test_result
        if self._defaults['self_test']['selfTestResult'] is None:
            raise MockFunctionCallError("niSync_self_test", param='selfTestResult')
        if self_test_result is not None:
            self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        # self_test_message
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niSync_self_test", param='selfTestMessage')
        test_value = self._defaults['self_test']['selfTestMessage']
        if sys.version_info.major > 2 and type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(self_test_message) >= len(test_value)
        for i in range(len(test_value)):
            self_test_message[i] = test_value[i]
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niSync_ClearClock.side_effect = MockFunctionCallError("niSync_ClearClock")
        mock_library.niSync_ClearClock.return_value = 0
        mock_library.niSync_ClearFutureTimeEvents.side_effect = MockFunctionCallError("niSync_ClearFutureTimeEvents")
        mock_library.niSync_ClearFutureTimeEvents.return_value = 0
        mock_library.niSync_ConfigureFpga.side_effect = MockFunctionCallError("niSync_ConfigureFpga")
        mock_library.niSync_ConfigureFpga.return_value = 0
        mock_library.niSync_ConnectClkTerminals.side_effect = MockFunctionCallError("niSync_ConnectClkTerminals")
        mock_library.niSync_ConnectClkTerminals.return_value = 0
        mock_library.niSync_ConnectSwTrigToTerminal.side_effect = MockFunctionCallError("niSync_ConnectSwTrigToTerminal")
        mock_library.niSync_ConnectSwTrigToTerminal.return_value = 0
        mock_library.niSync_ConnectTrigTerminals.side_effect = MockFunctionCallError("niSync_ConnectTrigTerminals")
        mock_library.niSync_ConnectTrigTerminals.return_value = 0
        mock_library.niSync_CreateClock.side_effect = MockFunctionCallError("niSync_CreateClock")
        mock_library.niSync_CreateClock.return_value = 0
        mock_library.niSync_CreateFutureTimeEvent.side_effect = MockFunctionCallError("niSync_CreateFutureTimeEvent")
        mock_library.niSync_CreateFutureTimeEvent.return_value = 0
        mock_library.niSync_DisableGpsTimestamping.side_effect = MockFunctionCallError("niSync_DisableGpsTimestamping")
        mock_library.niSync_DisableGpsTimestamping.return_value = 0
        mock_library.niSync_DisableIrigTimestamping.side_effect = MockFunctionCallError("niSync_DisableIrigTimestamping")
        mock_library.niSync_DisableIrigTimestamping.return_value = 0
        mock_library.niSync_DisableTimeStampTrigger.side_effect = MockFunctionCallError("niSync_DisableTimeStampTrigger")
        mock_library.niSync_DisableTimeStampTrigger.return_value = 0
        mock_library.niSync_DisconnectClkTerminals.side_effect = MockFunctionCallError("niSync_DisconnectClkTerminals")
        mock_library.niSync_DisconnectClkTerminals.return_value = 0
        mock_library.niSync_DisconnectSwTrigFromTerminal.side_effect = MockFunctionCallError("niSync_DisconnectSwTrigFromTerminal")
        mock_library.niSync_DisconnectSwTrigFromTerminal.return_value = 0
        mock_library.niSync_DisconnectTrigTerminals.side_effect = MockFunctionCallError("niSync_DisconnectTrigTerminals")
        mock_library.niSync_DisconnectTrigTerminals.return_value = 0
        mock_library.niSync_EnableGpsTimestamping.side_effect = MockFunctionCallError("niSync_EnableGpsTimestamping")
        mock_library.niSync_EnableGpsTimestamping.return_value = 0
        mock_library.niSync_EnableIrigTimestamping.side_effect = MockFunctionCallError("niSync_EnableIrigTimestamping")
        mock_library.niSync_EnableIrigTimestamping.return_value = 0
        mock_library.niSync_EnableTimeStampTrigger.side_effect = MockFunctionCallError("niSync_EnableTimeStampTrigger")
        mock_library.niSync_EnableTimeStampTrigger.return_value = 0
        mock_library.niSync_EnableTimeStampTriggerWithDecimation.side_effect = MockFunctionCallError("niSync_EnableTimeStampTriggerWithDecimation")
        mock_library.niSync_EnableTimeStampTriggerWithDecimation.return_value = 0
        mock_library.niSync_GetAttributeViBoolean.side_effect = MockFunctionCallError("niSync_GetAttributeViBoolean")
        mock_library.niSync_GetAttributeViBoolean.return_value = 0
        mock_library.niSync_GetAttributeViInt32.side_effect = MockFunctionCallError("niSync_GetAttributeViInt32")
        mock_library.niSync_GetAttributeViInt32.return_value = 0
        mock_library.niSync_GetAttributeViReal64.side_effect = MockFunctionCallError("niSync_GetAttributeViReal64")
        mock_library.niSync_GetAttributeViReal64.return_value = 0
        mock_library.niSync_GetAttributeViString.side_effect = MockFunctionCallError("niSync_GetAttributeViString")
        mock_library.niSync_GetAttributeViString.return_value = 0
        mock_library.niSync_GetLocation.side_effect = MockFunctionCallError("niSync_GetLocation")
        mock_library.niSync_GetLocation.return_value = 0
        mock_library.niSync_GetTime.side_effect = MockFunctionCallError("niSync_GetTime")
        mock_library.niSync_GetTime.return_value = 0
        mock_library.niSync_GetTimeReferenceNames.side_effect = MockFunctionCallError("niSync_GetTimeReferenceNames")
        mock_library.niSync_GetTimeReferenceNames.return_value = 0
        mock_library.niSync_GetVelocity.side_effect = MockFunctionCallError("niSync_GetVelocity")
        mock_library.niSync_GetVelocity.return_value = 0
        mock_library.niSync_MeasureFrequency.side_effect = MockFunctionCallError("niSync_MeasureFrequency")
        mock_library.niSync_MeasureFrequency.return_value = 0
        mock_library.niSync_MeasureFrequencyEx.side_effect = MockFunctionCallError("niSync_MeasureFrequencyEx")
        mock_library.niSync_MeasureFrequencyEx.return_value = 0
        mock_library.niSync_PersistConfig.side_effect = MockFunctionCallError("niSync_PersistConfig")
        mock_library.niSync_PersistConfig.return_value = 0
        mock_library.niSync_ReadCurrentTemperature.side_effect = MockFunctionCallError("niSync_ReadCurrentTemperature")
        mock_library.niSync_ReadCurrentTemperature.return_value = 0
        mock_library.niSync_ReadLastGpsTimestamp.side_effect = MockFunctionCallError("niSync_ReadLastGpsTimestamp")
        mock_library.niSync_ReadLastGpsTimestamp.return_value = 0
        mock_library.niSync_ReadLastIrigTimestamp.side_effect = MockFunctionCallError("niSync_ReadLastIrigTimestamp")
        mock_library.niSync_ReadLastIrigTimestamp.return_value = 0
        mock_library.niSync_ReadMultipleTriggerTimeStamp.side_effect = MockFunctionCallError("niSync_ReadMultipleTriggerTimeStamp")
        mock_library.niSync_ReadMultipleTriggerTimeStamp.return_value = 0
        mock_library.niSync_ReadTriggerTimeStamp.side_effect = MockFunctionCallError("niSync_ReadTriggerTimeStamp")
        mock_library.niSync_ReadTriggerTimeStamp.return_value = 0
        mock_library.niSync_ResetFrequency.side_effect = MockFunctionCallError("niSync_ResetFrequency")
        mock_library.niSync_ResetFrequency.return_value = 0
        mock_library.niSync_SendSoftwareTrigger.side_effect = MockFunctionCallError("niSync_SendSoftwareTrigger")
        mock_library.niSync_SendSoftwareTrigger.return_value = 0
        mock_library.niSync_SetAttributeViBoolean.side_effect = MockFunctionCallError("niSync_SetAttributeViBoolean")
        mock_library.niSync_SetAttributeViBoolean.return_value = 0
        mock_library.niSync_SetAttributeViInt32.side_effect = MockFunctionCallError("niSync_SetAttributeViInt32")
        mock_library.niSync_SetAttributeViInt32.return_value = 0
        mock_library.niSync_SetAttributeViReal64.side_effect = MockFunctionCallError("niSync_SetAttributeViReal64")
        mock_library.niSync_SetAttributeViReal64.return_value = 0
        mock_library.niSync_SetAttributeViString.side_effect = MockFunctionCallError("niSync_SetAttributeViString")
        mock_library.niSync_SetAttributeViString.return_value = 0
        mock_library.niSync_SetTime.side_effect = MockFunctionCallError("niSync_SetTime")
        mock_library.niSync_SetTime.return_value = 0
        mock_library.niSync_SetTimeReference1588OrdinaryClock.side_effect = MockFunctionCallError("niSync_SetTimeReference1588OrdinaryClock")
        mock_library.niSync_SetTimeReference1588OrdinaryClock.return_value = 0
        mock_library.niSync_SetTimeReferenceFreeRunning.side_effect = MockFunctionCallError("niSync_SetTimeReferenceFreeRunning")
        mock_library.niSync_SetTimeReferenceFreeRunning.return_value = 0
        mock_library.niSync_SetTimeReferenceGps.side_effect = MockFunctionCallError("niSync_SetTimeReferenceGps")
        mock_library.niSync_SetTimeReferenceGps.return_value = 0
        mock_library.niSync_SetTimeReferenceIrig.side_effect = MockFunctionCallError("niSync_SetTimeReferenceIrig")
        mock_library.niSync_SetTimeReferenceIrig.return_value = 0
        mock_library.niSync_SetTimeReferencePps.side_effect = MockFunctionCallError("niSync_SetTimeReferencePps")
        mock_library.niSync_SetTimeReferencePps.return_value = 0
        mock_library.niSync_Start1588.side_effect = MockFunctionCallError("niSync_Start1588")
        mock_library.niSync_Start1588.return_value = 0
        mock_library.niSync_Stop1588.side_effect = MockFunctionCallError("niSync_Stop1588")
        mock_library.niSync_Stop1588.return_value = 0
        mock_library.niSync_close.side_effect = MockFunctionCallError("niSync_close")
        mock_library.niSync_close.return_value = 0
        mock_library.niSync_error_message.side_effect = MockFunctionCallError("niSync_error_message")
        mock_library.niSync_error_message.return_value = 0
        mock_library.niSync_init.side_effect = MockFunctionCallError("niSync_init")
        mock_library.niSync_init.return_value = 0
        mock_library.niSync_reset.side_effect = MockFunctionCallError("niSync_reset")
        mock_library.niSync_reset.return_value = 0
        mock_library.niSync_revision_query.side_effect = MockFunctionCallError("niSync_revision_query")
        mock_library.niSync_revision_query.return_value = 0
        mock_library.niSync_self_test.side_effect = MockFunctionCallError("niSync_self_test")
        mock_library.niSync_self_test.return_value = 0
