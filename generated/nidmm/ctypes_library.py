# This file was generated

# Python ctypes wrapper around driver DLL.
# ctypes is a library to manage calling into C/C++ DLLs. It will ensure the correct
#  number and types of parameters are passed into the different entry points

import ctypes
import threading

from nidmm.ctypes_types import *  # noqa: F403,H303
import nidmm.python_types


class NidmmCtypesLibrary(object):
    def __init__(self, library_name, library_type):
        self._func_lock = threading.Lock()
        # We cache the cfunc object from the ctypes.CDLL object
        self.niDMM_Abort_cfunc = None
        self.niDMM_ClearError_cfunc = None
        self.niDMM_ClearInterchangeWarnings_cfunc = None
        self.niDMM_ConfigureACBandwidth_cfunc = None
        self.niDMM_ConfigureADCCalibration_cfunc = None
        self.niDMM_ConfigureAutoZeroMode_cfunc = None
        self.niDMM_ConfigureCableCompType_cfunc = None
        self.niDMM_ConfigureCurrentSource_cfunc = None
        self.niDMM_ConfigureFixedRefJunction_cfunc = None
        self.niDMM_ConfigureFrequencyVoltageRange_cfunc = None
        self.niDMM_ConfigureMeasCompleteDest_cfunc = None
        self.niDMM_ConfigureMeasCompleteSlope_cfunc = None
        self.niDMM_ConfigureMeasurementAbsolute_cfunc = None
        self.niDMM_ConfigureMeasurementDigits_cfunc = None
        self.niDMM_ConfigureMultiPoint_cfunc = None
        self.niDMM_ConfigureOffsetCompOhms_cfunc = None
        self.niDMM_ConfigureOpenCableCompValues_cfunc = None
        self.niDMM_ConfigurePowerLineFrequency_cfunc = None
        self.niDMM_ConfigureRTDCustom_cfunc = None
        self.niDMM_ConfigureRTDType_cfunc = None
        self.niDMM_ConfigureSampleTriggerSlope_cfunc = None
        self.niDMM_ConfigureShortCableCompValues_cfunc = None
        self.niDMM_ConfigureThermistorCustom_cfunc = None
        self.niDMM_ConfigureThermistorType_cfunc = None
        self.niDMM_ConfigureThermocouple_cfunc = None
        self.niDMM_ConfigureTransducerType_cfunc = None
        self.niDMM_ConfigureTrigger_cfunc = None
        self.niDMM_ConfigureTriggerSlope_cfunc = None
        self.niDMM_ConfigureWaveformAcquisition_cfunc = None
        self.niDMM_ConfigureWaveformCoupling_cfunc = None
        self.niDMM_Disable_cfunc = None
        self.niDMM_Fetch_cfunc = None
        self.niDMM_FetchMultiPoint_cfunc = None
        self.niDMM_FetchWaveform_cfunc = None
        self.niDMM_FormatMeasAbsolute_cfunc = None
        self.niDMM_GetApertureTimeInfo_cfunc = None
        self.niDMM_GetAttributeViBoolean_cfunc = None
        self.niDMM_GetAttributeViInt32_cfunc = None
        self.niDMM_GetAttributeViReal64_cfunc = None
        self.niDMM_GetAttributeViSession_cfunc = None
        self.niDMM_GetAttributeViString_cfunc = None
        self.niDMM_GetAutoRangeValue_cfunc = None
        self.niDMM_GetCalCount_cfunc = None
        self.niDMM_GetCalDateAndTime_cfunc = None
        self.niDMM_GetChannelName_cfunc = None
        self.niDMM_GetDevTemp_cfunc = None
        self.niDMM_GetError_cfunc = None
        self.niDMM_GetErrorMessage_cfunc = None
        self.niDMM_GetLastCalTemp_cfunc = None
        self.niDMM_GetMeasurementPeriod_cfunc = None
        self.niDMM_GetNextCoercionRecord_cfunc = None
        self.niDMM_GetNextInterchangeWarning_cfunc = None
        self.niDMM_GetSelfCalSupported_cfunc = None
        self.niDMM_InitWithOptions_cfunc = None
        self.niDMM_Initiate_cfunc = None
        self.niDMM_IsOverRange_cfunc = None
        self.niDMM_IsUnderRange_cfunc = None
        self.niDMM_LockSession_cfunc = None
        self.niDMM_PerformOpenCableComp_cfunc = None
        self.niDMM_PerformShortCableComp_cfunc = None
        self.niDMM_Read_cfunc = None
        self.niDMM_ReadMultiPoint_cfunc = None
        self.niDMM_ReadStatus_cfunc = None
        self.niDMM_ReadWaveform_cfunc = None
        self.niDMM_ResetInterchangeCheck_cfunc = None
        self.niDMM_ResetWithDefaults_cfunc = None
        self.niDMM_SelfCal_cfunc = None
        self.niDMM_SendSoftwareTrigger_cfunc = None
        self.niDMM_SetAttributeViBoolean_cfunc = None
        self.niDMM_SetAttributeViInt32_cfunc = None
        self.niDMM_SetAttributeViReal64_cfunc = None
        self.niDMM_SetAttributeViSession_cfunc = None
        self.niDMM_SetAttributeViString_cfunc = None
        self.niDMM_UnlockSession_cfunc = None
        self.niDMM_close_cfunc = None
        self.niDMM_error_message_cfunc = None
        self.niDMM_error_query_cfunc = None
        self.niDMM_reset_cfunc = None
        self.niDMM_revision_query_cfunc = None
        self.niDMM_self_test_cfunc = None

        if library_type == 'windll':
            self._library = ctypes.WinDLL(library_name)
        else:
            assert library_type == 'cdll'
            self._library = ctypes.CDLL(library_name)

    def niDMM_Abort(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_Abort_cfunc is None:
                self.niDMM_Abort_cfunc = self._library.niDMM_Abort
                self.niDMM_Abort_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDMM_Abort_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_Abort_cfunc(vi)

    def niDMM_ClearError(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ClearError_cfunc is None:
                self.niDMM_ClearError_cfunc = self._library.niDMM_ClearError
                self.niDMM_ClearError_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDMM_ClearError_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ClearError_cfunc(vi)

    def niDMM_ClearInterchangeWarnings(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ClearInterchangeWarnings_cfunc is None:
                self.niDMM_ClearInterchangeWarnings_cfunc = self._library.niDMM_ClearInterchangeWarnings
                self.niDMM_ClearInterchangeWarnings_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDMM_ClearInterchangeWarnings_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ClearInterchangeWarnings_cfunc(vi)

    def niDMM_ConfigureACBandwidth(self, vi, ac_minimum_frequency_hz, ac_maximum_frequency_hz):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureACBandwidth_cfunc is None:
                self.niDMM_ConfigureACBandwidth_cfunc = self._library.niDMM_ConfigureACBandwidth
                self.niDMM_ConfigureACBandwidth_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
                self.niDMM_ConfigureACBandwidth_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureACBandwidth_cfunc(vi, ac_minimum_frequency_hz, ac_maximum_frequency_hz)

    def niDMM_ConfigureADCCalibration(self, vi, adc_calibration):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureADCCalibration_cfunc is None:
                self.niDMM_ConfigureADCCalibration_cfunc = self._library.niDMM_ConfigureADCCalibration
                self.niDMM_ConfigureADCCalibration_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
                self.niDMM_ConfigureADCCalibration_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureADCCalibration_cfunc(vi, adc_calibration)

    def niDMM_ConfigureAutoZeroMode(self, vi, auto_zero_mode):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureAutoZeroMode_cfunc is None:
                self.niDMM_ConfigureAutoZeroMode_cfunc = self._library.niDMM_ConfigureAutoZeroMode
                self.niDMM_ConfigureAutoZeroMode_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
                self.niDMM_ConfigureAutoZeroMode_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureAutoZeroMode_cfunc(vi, auto_zero_mode)

    def niDMM_ConfigureCableCompType(self, vi, cable_comp_type):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureCableCompType_cfunc is None:
                self.niDMM_ConfigureCableCompType_cfunc = self._library.niDMM_ConfigureCableCompType
                self.niDMM_ConfigureCableCompType_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
                self.niDMM_ConfigureCableCompType_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureCableCompType_cfunc(vi, cable_comp_type)

    def niDMM_ConfigureCurrentSource(self, vi, current_source):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureCurrentSource_cfunc is None:
                self.niDMM_ConfigureCurrentSource_cfunc = self._library.niDMM_ConfigureCurrentSource
                self.niDMM_ConfigureCurrentSource_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype]  # noqa: F405
                self.niDMM_ConfigureCurrentSource_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureCurrentSource_cfunc(vi, current_source)

    def niDMM_ConfigureFixedRefJunction(self, vi, fixed_reference_junction):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureFixedRefJunction_cfunc is None:
                self.niDMM_ConfigureFixedRefJunction_cfunc = self._library.niDMM_ConfigureFixedRefJunction
                self.niDMM_ConfigureFixedRefJunction_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype]  # noqa: F405
                self.niDMM_ConfigureFixedRefJunction_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureFixedRefJunction_cfunc(vi, fixed_reference_junction)

    def niDMM_ConfigureFrequencyVoltageRange(self, vi, voltage_range):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureFrequencyVoltageRange_cfunc is None:
                self.niDMM_ConfigureFrequencyVoltageRange_cfunc = self._library.niDMM_ConfigureFrequencyVoltageRange
                self.niDMM_ConfigureFrequencyVoltageRange_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype]  # noqa: F405
                self.niDMM_ConfigureFrequencyVoltageRange_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureFrequencyVoltageRange_cfunc(vi, voltage_range)

    def niDMM_ConfigureMeasCompleteDest(self, vi, meas_complete_destination):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureMeasCompleteDest_cfunc is None:
                self.niDMM_ConfigureMeasCompleteDest_cfunc = self._library.niDMM_ConfigureMeasCompleteDest
                self.niDMM_ConfigureMeasCompleteDest_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
                self.niDMM_ConfigureMeasCompleteDest_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureMeasCompleteDest_cfunc(vi, meas_complete_destination)

    def niDMM_ConfigureMeasCompleteSlope(self, vi, meas_complete_slope):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureMeasCompleteSlope_cfunc is None:
                self.niDMM_ConfigureMeasCompleteSlope_cfunc = self._library.niDMM_ConfigureMeasCompleteSlope
                self.niDMM_ConfigureMeasCompleteSlope_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
                self.niDMM_ConfigureMeasCompleteSlope_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureMeasCompleteSlope_cfunc(vi, meas_complete_slope)

    def niDMM_ConfigureMeasurementAbsolute(self, vi, measurement_function, range, resolution_absolute):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureMeasurementAbsolute_cfunc is None:
                self.niDMM_ConfigureMeasurementAbsolute_cfunc = self._library.niDMM_ConfigureMeasurementAbsolute
                self.niDMM_ConfigureMeasurementAbsolute_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
                self.niDMM_ConfigureMeasurementAbsolute_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureMeasurementAbsolute_cfunc(vi, measurement_function, range, resolution_absolute)

    def niDMM_ConfigureMeasurementDigits(self, vi, measurement_function, range, resolution_digits):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureMeasurementDigits_cfunc is None:
                self.niDMM_ConfigureMeasurementDigits_cfunc = self._library.niDMM_ConfigureMeasurementDigits
                self.niDMM_ConfigureMeasurementDigits_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
                self.niDMM_ConfigureMeasurementDigits_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureMeasurementDigits_cfunc(vi, measurement_function, range, resolution_digits)

    def niDMM_ConfigureMultiPoint(self, vi, trigger_count, sample_count, sample_trigger, sample_interval):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureMultiPoint_cfunc is None:
                self.niDMM_ConfigureMultiPoint_cfunc = self._library.niDMM_ConfigureMultiPoint
                self.niDMM_ConfigureMultiPoint_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ViInt32_ctype, ViReal64_ctype]  # noqa: F405
                self.niDMM_ConfigureMultiPoint_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureMultiPoint_cfunc(vi, trigger_count, sample_count, sample_trigger, sample_interval)

    def niDMM_ConfigureOffsetCompOhms(self, vi, offset_comp_ohms):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureOffsetCompOhms_cfunc is None:
                self.niDMM_ConfigureOffsetCompOhms_cfunc = self._library.niDMM_ConfigureOffsetCompOhms
                self.niDMM_ConfigureOffsetCompOhms_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
                self.niDMM_ConfigureOffsetCompOhms_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureOffsetCompOhms_cfunc(vi, offset_comp_ohms)

    def niDMM_ConfigureOpenCableCompValues(self, vi, conductance, susceptance):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureOpenCableCompValues_cfunc is None:
                self.niDMM_ConfigureOpenCableCompValues_cfunc = self._library.niDMM_ConfigureOpenCableCompValues
                self.niDMM_ConfigureOpenCableCompValues_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
                self.niDMM_ConfigureOpenCableCompValues_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureOpenCableCompValues_cfunc(vi, conductance, susceptance)

    def niDMM_ConfigurePowerLineFrequency(self, vi, power_line_frequency_hz):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigurePowerLineFrequency_cfunc is None:
                self.niDMM_ConfigurePowerLineFrequency_cfunc = self._library.niDMM_ConfigurePowerLineFrequency
                self.niDMM_ConfigurePowerLineFrequency_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype]  # noqa: F405
                self.niDMM_ConfigurePowerLineFrequency_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigurePowerLineFrequency_cfunc(vi, power_line_frequency_hz)

    def niDMM_ConfigureRTDCustom(self, vi, rtd_a, rtd_b, rtd_c):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureRTDCustom_cfunc is None:
                self.niDMM_ConfigureRTDCustom_cfunc = self._library.niDMM_ConfigureRTDCustom
                self.niDMM_ConfigureRTDCustom_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
                self.niDMM_ConfigureRTDCustom_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureRTDCustom_cfunc(vi, rtd_a, rtd_b, rtd_c)

    def niDMM_ConfigureRTDType(self, vi, rtd_type, rtd_resistance):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureRTDType_cfunc is None:
                self.niDMM_ConfigureRTDType_cfunc = self._library.niDMM_ConfigureRTDType
                self.niDMM_ConfigureRTDType_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype]  # noqa: F405
                self.niDMM_ConfigureRTDType_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureRTDType_cfunc(vi, rtd_type, rtd_resistance)

    def niDMM_ConfigureSampleTriggerSlope(self, vi, sample_trigger_slope):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureSampleTriggerSlope_cfunc is None:
                self.niDMM_ConfigureSampleTriggerSlope_cfunc = self._library.niDMM_ConfigureSampleTriggerSlope
                self.niDMM_ConfigureSampleTriggerSlope_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
                self.niDMM_ConfigureSampleTriggerSlope_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureSampleTriggerSlope_cfunc(vi, sample_trigger_slope)

    def niDMM_ConfigureShortCableCompValues(self, vi, resistance, reactance):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureShortCableCompValues_cfunc is None:
                self.niDMM_ConfigureShortCableCompValues_cfunc = self._library.niDMM_ConfigureShortCableCompValues
                self.niDMM_ConfigureShortCableCompValues_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
                self.niDMM_ConfigureShortCableCompValues_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureShortCableCompValues_cfunc(vi, resistance, reactance)

    def niDMM_ConfigureThermistorCustom(self, vi, thermistor_a, thermistor_b, thermistor_c):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureThermistorCustom_cfunc is None:
                self.niDMM_ConfigureThermistorCustom_cfunc = self._library.niDMM_ConfigureThermistorCustom
                self.niDMM_ConfigureThermistorCustom_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
                self.niDMM_ConfigureThermistorCustom_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureThermistorCustom_cfunc(vi, thermistor_a, thermistor_b, thermistor_c)

    def niDMM_ConfigureThermistorType(self, vi, thermistor_type):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureThermistorType_cfunc is None:
                self.niDMM_ConfigureThermistorType_cfunc = self._library.niDMM_ConfigureThermistorType
                self.niDMM_ConfigureThermistorType_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
                self.niDMM_ConfigureThermistorType_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureThermistorType_cfunc(vi, thermistor_type)

    def niDMM_ConfigureThermocouple(self, vi, thermocouple_type, reference_junction_type):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureThermocouple_cfunc is None:
                self.niDMM_ConfigureThermocouple_cfunc = self._library.niDMM_ConfigureThermocouple
                self.niDMM_ConfigureThermocouple_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype]  # noqa: F405
                self.niDMM_ConfigureThermocouple_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureThermocouple_cfunc(vi, thermocouple_type, reference_junction_type)

    def niDMM_ConfigureTransducerType(self, vi, transducer_type):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureTransducerType_cfunc is None:
                self.niDMM_ConfigureTransducerType_cfunc = self._library.niDMM_ConfigureTransducerType
                self.niDMM_ConfigureTransducerType_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
                self.niDMM_ConfigureTransducerType_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureTransducerType_cfunc(vi, transducer_type)

    def niDMM_ConfigureTrigger(self, vi, trigger_source, trigger_delay):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureTrigger_cfunc is None:
                self.niDMM_ConfigureTrigger_cfunc = self._library.niDMM_ConfigureTrigger
                self.niDMM_ConfigureTrigger_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype]  # noqa: F405
                self.niDMM_ConfigureTrigger_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureTrigger_cfunc(vi, trigger_source, trigger_delay)

    def niDMM_ConfigureTriggerSlope(self, vi, trigger_slope):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureTriggerSlope_cfunc is None:
                self.niDMM_ConfigureTriggerSlope_cfunc = self._library.niDMM_ConfigureTriggerSlope
                self.niDMM_ConfigureTriggerSlope_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
                self.niDMM_ConfigureTriggerSlope_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureTriggerSlope_cfunc(vi, trigger_slope)

    def niDMM_ConfigureWaveformAcquisition(self, vi, measurement_function, range, rate, waveform_points):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureWaveformAcquisition_cfunc is None:
                self.niDMM_ConfigureWaveformAcquisition_cfunc = self._library.niDMM_ConfigureWaveformAcquisition
                self.niDMM_ConfigureWaveformAcquisition_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype, ViReal64_ctype, ViInt32_ctype]  # noqa: F405
                self.niDMM_ConfigureWaveformAcquisition_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureWaveformAcquisition_cfunc(vi, measurement_function, range, rate, waveform_points)

    def niDMM_ConfigureWaveformCoupling(self, vi, waveform_coupling):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureWaveformCoupling_cfunc is None:
                self.niDMM_ConfigureWaveformCoupling_cfunc = self._library.niDMM_ConfigureWaveformCoupling
                self.niDMM_ConfigureWaveformCoupling_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
                self.niDMM_ConfigureWaveformCoupling_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ConfigureWaveformCoupling_cfunc(vi, waveform_coupling)

    def niDMM_Disable(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_Disable_cfunc is None:
                self.niDMM_Disable_cfunc = self._library.niDMM_Disable
                self.niDMM_Disable_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDMM_Disable_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_Disable_cfunc(vi)

    def niDMM_Fetch(self, vi, maximum_time, reading):  # noqa: N802
        with self._func_lock:
            if self.niDMM_Fetch_cfunc is None:
                self.niDMM_Fetch_cfunc = self._library.niDMM_Fetch
                self.niDMM_Fetch_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niDMM_Fetch_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_Fetch_cfunc(vi, maximum_time, reading)

    def niDMM_FetchMultiPoint(self, vi, maximum_time, array_size, reading_array, actual_number_of_points):  # noqa: N802
        with self._func_lock:
            if self.niDMM_FetchMultiPoint_cfunc is None:
                self.niDMM_FetchMultiPoint_cfunc = self._library.niDMM_FetchMultiPoint
                self.niDMM_FetchMultiPoint_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
                self.niDMM_FetchMultiPoint_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_FetchMultiPoint_cfunc(vi, maximum_time, array_size, reading_array, actual_number_of_points)

    def niDMM_FetchWaveform(self, vi, maximum_time, array_size, waveform_array, actual_number_of_points):  # noqa: N802
        with self._func_lock:
            if self.niDMM_FetchWaveform_cfunc is None:
                self.niDMM_FetchWaveform_cfunc = self._library.niDMM_FetchWaveform
                self.niDMM_FetchWaveform_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
                self.niDMM_FetchWaveform_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_FetchWaveform_cfunc(vi, maximum_time, array_size, waveform_array, actual_number_of_points)

    def niDMM_FormatMeasAbsolute(self, measurement_function, range, resolution, measurement, mode_string, range_string, data_string):  # noqa: N802
        with self._func_lock:
            if self.niDMM_FormatMeasAbsolute_cfunc is None:
                self.niDMM_FormatMeasAbsolute_cfunc = self._library.niDMM_FormatMeasAbsolute
                self.niDMM_FormatMeasAbsolute_cfunc.argtypes = [ViInt32_ctype, ViReal64_ctype, ViReal64_ctype, ViReal64_ctype, ctypes.POINTER(ViChar_ctype), ctypes.POINTER(ViChar_ctype), ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niDMM_FormatMeasAbsolute_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_FormatMeasAbsolute_cfunc(measurement_function, range, resolution, measurement, mode_string, range_string, data_string)

    def niDMM_GetApertureTimeInfo(self, vi, aperture_time, aperture_time_units):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetApertureTimeInfo_cfunc is None:
                self.niDMM_GetApertureTimeInfo_cfunc = self._library.niDMM_GetApertureTimeInfo
                self.niDMM_GetApertureTimeInfo_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
                self.niDMM_GetApertureTimeInfo_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_GetApertureTimeInfo_cfunc(vi, aperture_time, aperture_time_units)

    def niDMM_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetAttributeViBoolean_cfunc is None:
                self.niDMM_GetAttributeViBoolean_cfunc = self._library.niDMM_GetAttributeViBoolean
                self.niDMM_GetAttributeViBoolean_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ctypes.POINTER(ViBoolean_ctype)]  # noqa: F405
                self.niDMM_GetAttributeViBoolean_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_GetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetAttributeViInt32_cfunc is None:
                self.niDMM_GetAttributeViInt32_cfunc = self._library.niDMM_GetAttributeViInt32
                self.niDMM_GetAttributeViInt32_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
                self.niDMM_GetAttributeViInt32_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_GetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetAttributeViReal64_cfunc is None:
                self.niDMM_GetAttributeViReal64_cfunc = self._library.niDMM_GetAttributeViReal64
                self.niDMM_GetAttributeViReal64_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niDMM_GetAttributeViReal64_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_GetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_GetAttributeViSession(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetAttributeViSession_cfunc is None:
                self.niDMM_GetAttributeViSession_cfunc = self._library.niDMM_GetAttributeViSession
                self.niDMM_GetAttributeViSession_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ctypes.POINTER(ViSession_ctype)]  # noqa: F405
                self.niDMM_GetAttributeViSession_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_GetAttributeViSession_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetAttributeViString_cfunc is None:
                self.niDMM_GetAttributeViString_cfunc = self._library.niDMM_GetAttributeViString
                self.niDMM_GetAttributeViString_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViInt32_ctype, ViString_ctype]  # noqa: F405
                self.niDMM_GetAttributeViString_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_GetAttributeViString_cfunc(vi, channel_name, attribute_id, buffer_size, attribute_value)

    def niDMM_GetAutoRangeValue(self, vi, actual_range):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetAutoRangeValue_cfunc is None:
                self.niDMM_GetAutoRangeValue_cfunc = self._library.niDMM_GetAutoRangeValue
                self.niDMM_GetAutoRangeValue_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niDMM_GetAutoRangeValue_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_GetAutoRangeValue_cfunc(vi, actual_range)

    def niDMM_GetCalCount(self, vi, cal_type, count):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetCalCount_cfunc is None:
                self.niDMM_GetCalCount_cfunc = self._library.niDMM_GetCalCount
                self.niDMM_GetCalCount_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
                self.niDMM_GetCalCount_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_GetCalCount_cfunc(vi, cal_type, count)

    def niDMM_GetCalDateAndTime(self, vi, cal_type, month, day, year, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetCalDateAndTime_cfunc is None:
                self.niDMM_GetCalDateAndTime_cfunc = self._library.niDMM_GetCalDateAndTime
                self.niDMM_GetCalDateAndTime_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
                self.niDMM_GetCalDateAndTime_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_GetCalDateAndTime_cfunc(vi, cal_type, month, day, year, hour, minute)

    def niDMM_GetChannelName(self, vi, index, buffer_size, channel_string):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetChannelName_cfunc is None:
                self.niDMM_GetChannelName_cfunc = self._library.niDMM_GetChannelName
                self.niDMM_GetChannelName_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niDMM_GetChannelName_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_GetChannelName_cfunc(vi, index, buffer_size, channel_string)

    def niDMM_GetDevTemp(self, vi, options, temperature):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetDevTemp_cfunc is None:
                self.niDMM_GetDevTemp_cfunc = self._library.niDMM_GetDevTemp
                self.niDMM_GetDevTemp_cfunc.argtypes = [ViSession_ctype, ViString_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niDMM_GetDevTemp_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_GetDevTemp_cfunc(vi, options, temperature)

    def niDMM_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetError_cfunc is None:
                self.niDMM_GetError_cfunc = self._library.niDMM_GetError
                self.niDMM_GetError_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViStatus_ctype), ViInt32_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niDMM_GetError_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_GetError_cfunc(vi, error_code, buffer_size, description)

    def niDMM_GetErrorMessage(self, vi, error_code, buffer_size, error_message):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetErrorMessage_cfunc is None:
                self.niDMM_GetErrorMessage_cfunc = self._library.niDMM_GetErrorMessage
                self.niDMM_GetErrorMessage_cfunc.argtypes = [ViSession_ctype, ViStatus_ctype, ViInt32_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niDMM_GetErrorMessage_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_GetErrorMessage_cfunc(vi, error_code, buffer_size, error_message)

    def niDMM_GetLastCalTemp(self, vi, cal_type, temperature):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetLastCalTemp_cfunc is None:
                self.niDMM_GetLastCalTemp_cfunc = self._library.niDMM_GetLastCalTemp
                self.niDMM_GetLastCalTemp_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niDMM_GetLastCalTemp_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_GetLastCalTemp_cfunc(vi, cal_type, temperature)

    def niDMM_GetMeasurementPeriod(self, vi, period):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetMeasurementPeriod_cfunc is None:
                self.niDMM_GetMeasurementPeriod_cfunc = self._library.niDMM_GetMeasurementPeriod
                self.niDMM_GetMeasurementPeriod_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niDMM_GetMeasurementPeriod_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_GetMeasurementPeriod_cfunc(vi, period)

    def niDMM_GetNextCoercionRecord(self, vi, buffer_size, coercion_record):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetNextCoercionRecord_cfunc is None:
                self.niDMM_GetNextCoercionRecord_cfunc = self._library.niDMM_GetNextCoercionRecord
                self.niDMM_GetNextCoercionRecord_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niDMM_GetNextCoercionRecord_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_GetNextCoercionRecord_cfunc(vi, buffer_size, coercion_record)

    def niDMM_GetNextInterchangeWarning(self, vi, buffer_size, interchange_warning):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetNextInterchangeWarning_cfunc is None:
                self.niDMM_GetNextInterchangeWarning_cfunc = self._library.niDMM_GetNextInterchangeWarning
                self.niDMM_GetNextInterchangeWarning_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niDMM_GetNextInterchangeWarning_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_GetNextInterchangeWarning_cfunc(vi, buffer_size, interchange_warning)

    def niDMM_GetSelfCalSupported(self, vi, self_cal_supported):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetSelfCalSupported_cfunc is None:
                self.niDMM_GetSelfCalSupported_cfunc = self._library.niDMM_GetSelfCalSupported
                self.niDMM_GetSelfCalSupported_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViBoolean_ctype)]  # noqa: F405
                self.niDMM_GetSelfCalSupported_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_GetSelfCalSupported_cfunc(vi, self_cal_supported)

    def niDMM_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_InitWithOptions_cfunc is None:
                self.niDMM_InitWithOptions_cfunc = self._library.niDMM_InitWithOptions
                self.niDMM_InitWithOptions_cfunc.argtypes = [ViString_ctype, ViBoolean_ctype, ViBoolean_ctype, ViString_ctype, ctypes.POINTER(ViSession_ctype)]  # noqa: F405
                self.niDMM_InitWithOptions_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_InitWithOptions_cfunc(resource_name, id_query, reset_device, option_string, vi)

    def niDMM_Initiate(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_Initiate_cfunc is None:
                self.niDMM_Initiate_cfunc = self._library.niDMM_Initiate
                self.niDMM_Initiate_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDMM_Initiate_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_Initiate_cfunc(vi)

    def niDMM_IsOverRange(self, vi, measurement_value, is_over_range):  # noqa: N802
        with self._func_lock:
            if self.niDMM_IsOverRange_cfunc is None:
                self.niDMM_IsOverRange_cfunc = self._library.niDMM_IsOverRange
                self.niDMM_IsOverRange_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ctypes.POINTER(ViBoolean_ctype)]  # noqa: F405
                self.niDMM_IsOverRange_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_IsOverRange_cfunc(vi, measurement_value, is_over_range)

    def niDMM_IsUnderRange(self, vi, measurement_value, is_under_range):  # noqa: N802
        with self._func_lock:
            if self.niDMM_IsUnderRange_cfunc is None:
                self.niDMM_IsUnderRange_cfunc = self._library.niDMM_IsUnderRange
                self.niDMM_IsUnderRange_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ctypes.POINTER(ViBoolean_ctype)]  # noqa: F405
                self.niDMM_IsUnderRange_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_IsUnderRange_cfunc(vi, measurement_value, is_under_range)

    def niDMM_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niDMM_LockSession_cfunc is None:
                self.niDMM_LockSession_cfunc = self._library.niDMM_LockSession
                self.niDMM_LockSession_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViBoolean_ctype)]  # noqa: F405
                self.niDMM_LockSession_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_LockSession_cfunc(vi, caller_has_lock)

    def niDMM_PerformOpenCableComp(self, vi, conductance, susceptance):  # noqa: N802
        with self._func_lock:
            if self.niDMM_PerformOpenCableComp_cfunc is None:
                self.niDMM_PerformOpenCableComp_cfunc = self._library.niDMM_PerformOpenCableComp
                self.niDMM_PerformOpenCableComp_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niDMM_PerformOpenCableComp_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_PerformOpenCableComp_cfunc(vi, conductance, susceptance)

    def niDMM_PerformShortCableComp(self, vi, resistance, reactance):  # noqa: N802
        with self._func_lock:
            if self.niDMM_PerformShortCableComp_cfunc is None:
                self.niDMM_PerformShortCableComp_cfunc = self._library.niDMM_PerformShortCableComp
                self.niDMM_PerformShortCableComp_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niDMM_PerformShortCableComp_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_PerformShortCableComp_cfunc(vi, resistance, reactance)

    def niDMM_Read(self, vi, maximum_time, reading):  # noqa: N802
        with self._func_lock:
            if self.niDMM_Read_cfunc is None:
                self.niDMM_Read_cfunc = self._library.niDMM_Read
                self.niDMM_Read_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niDMM_Read_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_Read_cfunc(vi, maximum_time, reading)

    def niDMM_ReadMultiPoint(self, vi, maximum_time, array_size, reading_array, actual_number_of_points):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ReadMultiPoint_cfunc is None:
                self.niDMM_ReadMultiPoint_cfunc = self._library.niDMM_ReadMultiPoint
                self.niDMM_ReadMultiPoint_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
                self.niDMM_ReadMultiPoint_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ReadMultiPoint_cfunc(vi, maximum_time, array_size, reading_array, actual_number_of_points)

    def niDMM_ReadStatus(self, vi, acquisition_backlog, acquisition_status):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ReadStatus_cfunc is None:
                self.niDMM_ReadStatus_cfunc = self._library.niDMM_ReadStatus
                self.niDMM_ReadStatus_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt16_ctype)]  # noqa: F405
                self.niDMM_ReadStatus_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ReadStatus_cfunc(vi, acquisition_backlog, acquisition_status)

    def niDMM_ReadWaveform(self, vi, maximum_time, array_size, waveform_array, actual_number_of_points):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ReadWaveform_cfunc is None:
                self.niDMM_ReadWaveform_cfunc = self._library.niDMM_ReadWaveform
                self.niDMM_ReadWaveform_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
                self.niDMM_ReadWaveform_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ReadWaveform_cfunc(vi, maximum_time, array_size, waveform_array, actual_number_of_points)

    def niDMM_ResetInterchangeCheck(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ResetInterchangeCheck_cfunc is None:
                self.niDMM_ResetInterchangeCheck_cfunc = self._library.niDMM_ResetInterchangeCheck
                self.niDMM_ResetInterchangeCheck_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDMM_ResetInterchangeCheck_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ResetInterchangeCheck_cfunc(vi)

    def niDMM_ResetWithDefaults(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ResetWithDefaults_cfunc is None:
                self.niDMM_ResetWithDefaults_cfunc = self._library.niDMM_ResetWithDefaults
                self.niDMM_ResetWithDefaults_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDMM_ResetWithDefaults_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_ResetWithDefaults_cfunc(vi)

    def niDMM_SelfCal(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SelfCal_cfunc is None:
                self.niDMM_SelfCal_cfunc = self._library.niDMM_SelfCal
                self.niDMM_SelfCal_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDMM_SelfCal_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_SelfCal_cfunc(vi)

    def niDMM_SendSoftwareTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SendSoftwareTrigger_cfunc is None:
                self.niDMM_SendSoftwareTrigger_cfunc = self._library.niDMM_SendSoftwareTrigger
                self.niDMM_SendSoftwareTrigger_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDMM_SendSoftwareTrigger_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_SendSoftwareTrigger_cfunc(vi)

    def niDMM_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SetAttributeViBoolean_cfunc is None:
                self.niDMM_SetAttributeViBoolean_cfunc = self._library.niDMM_SetAttributeViBoolean
                self.niDMM_SetAttributeViBoolean_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViBoolean_ctype]  # noqa: F405
                self.niDMM_SetAttributeViBoolean_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_SetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SetAttributeViInt32_cfunc is None:
                self.niDMM_SetAttributeViInt32_cfunc = self._library.niDMM_SetAttributeViInt32
                self.niDMM_SetAttributeViInt32_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViInt32_ctype]  # noqa: F405
                self.niDMM_SetAttributeViInt32_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_SetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SetAttributeViReal64_cfunc is None:
                self.niDMM_SetAttributeViReal64_cfunc = self._library.niDMM_SetAttributeViReal64
                self.niDMM_SetAttributeViReal64_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViReal64_ctype]  # noqa: F405
                self.niDMM_SetAttributeViReal64_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_SetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_SetAttributeViSession(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SetAttributeViSession_cfunc is None:
                self.niDMM_SetAttributeViSession_cfunc = self._library.niDMM_SetAttributeViSession
                self.niDMM_SetAttributeViSession_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViSession_ctype]  # noqa: F405
                self.niDMM_SetAttributeViSession_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_SetAttributeViSession_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SetAttributeViString_cfunc is None:
                self.niDMM_SetAttributeViString_cfunc = self._library.niDMM_SetAttributeViString
                self.niDMM_SetAttributeViString_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViString_ctype]  # noqa: F405
                self.niDMM_SetAttributeViString_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_SetAttributeViString_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niDMM_UnlockSession_cfunc is None:
                self.niDMM_UnlockSession_cfunc = self._library.niDMM_UnlockSession
                self.niDMM_UnlockSession_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViBoolean_ctype)]  # noqa: F405
                self.niDMM_UnlockSession_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_UnlockSession_cfunc(vi, caller_has_lock)

    def niDMM_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_close_cfunc is None:
                self.niDMM_close_cfunc = self._library.niDMM_close
                self.niDMM_close_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDMM_close_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_close_cfunc(vi)

    def niDMM_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niDMM_error_message_cfunc is None:
                self.niDMM_error_message_cfunc = self._library.niDMM_error_message
                self.niDMM_error_message_cfunc.argtypes = [ViSession_ctype, ViStatus_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niDMM_error_message_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_error_message_cfunc(vi, error_code, error_message)

    def niDMM_error_query(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niDMM_error_query_cfunc is None:
                self.niDMM_error_query_cfunc = self._library.niDMM_error_query
                self.niDMM_error_query_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViStatus_ctype), ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niDMM_error_query_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_error_query_cfunc(vi, error_code, error_message)

    def niDMM_reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_reset_cfunc is None:
                self.niDMM_reset_cfunc = self._library.niDMM_reset
                self.niDMM_reset_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDMM_reset_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_reset_cfunc(vi)

    def niDMM_revision_query(self, vi, instrument_driver_revision, firmware_revision):  # noqa: N802
        with self._func_lock:
            if self.niDMM_revision_query_cfunc is None:
                self.niDMM_revision_query_cfunc = self._library.niDMM_revision_query
                self.niDMM_revision_query_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViChar_ctype), ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niDMM_revision_query_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_revision_query_cfunc(vi, instrument_driver_revision, firmware_revision)

    def niDMM_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niDMM_self_test_cfunc is None:
                self.niDMM_self_test_cfunc = self._library.niDMM_self_test
                self.niDMM_self_test_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViInt16_ctype), ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niDMM_self_test_cfunc.restype = nidmm.python_types.ViStatus
        return self.niDMM_self_test_cfunc(vi, self_test_result, self_test_message)
