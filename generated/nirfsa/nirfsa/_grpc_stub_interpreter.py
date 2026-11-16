# -*- coding: utf-8 -*-
# This file was generated

import grpc
import hightime  # noqa: F401
import nitlsconfig
import session_pb2 as session_grpc_types
import threading
import warnings

from . import enums as enums  # noqa: F401
from . import errors as errors
from . import nidevice_pb2 as grpc_complex_types  # noqa: F401
from . import nirfsa_pb2 as grpc_types
from . import nirfsa_pb2_grpc as nirfsa_grpc

from . import coefficient_info_type as coefficient_info_type  # noqa: F401

from . import waveform_info as waveform_info  # noqa: F401

from . import spectrum_info_type as spectrum_info_type  # noqa: F401


class GrpcStubInterpreter(object):
    '''Interpreter for interacting with a gRPC Stub class'''

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._lock = threading.RLock()
        self._client = nirfsa_grpc.NiRFSAStub(grpc_options.grpc_channel)
        self.set_session_handle()

    def set_session_handle(self, value=session_grpc_types.Session()):
        self._vi = value

    def get_session_handle(self):
        return self._vi

    def _invoke(self, func, request, metadata=None):
        try:
            response = func(request, metadata=metadata)
            error_code = response.status
            error_message = ''
        except grpc.RpcError as rpc_error:
            error_code = None
            error_message = rpc_error.details()
            for entry in rpc_error.trailing_metadata() or []:
                if entry.key == 'ni-error':
                    value = entry.value if isinstance(entry.value, str) else entry.value.decode('utf-8')
                    try:
                        error_code = int(value)
                    except ValueError:
                        error_message += f'\nError status: {value}'

            grpc_error = rpc_error.code()
            if grpc_error == grpc.StatusCode.NOT_FOUND:
                raise errors.DriverTooOldError() from None
            elif grpc_error == grpc.StatusCode.INVALID_ARGUMENT:
                raise ValueError(error_message) from None
            elif grpc_error == grpc.StatusCode.UNAVAILABLE:
                # gRPC reports a rejected TLS handshake and an unreachable server with the
                # same code, so ask NI-TLS whether it built this channel and can say more.
                error_message = nitlsconfig.get_tls_connection_error_elaboration(
                    self._grpc_options.grpc_channel
                ) or 'Failed to connect to server'
            elif grpc_error == grpc.StatusCode.UNIMPLEMENTED:
                error_message = (
                    'This operation is not supported by the NI gRPC Device Server being used. Upgrade NI gRPC Device Server.'
                )

            if error_code is None:
                raise errors.RpcError(grpc_error, error_message) from None

        if error_code < 0:
            raise errors.DriverError(error_code, error_message)
        elif error_code > 0:
            if not error_message:
                try:
                    error_message = self.error_message(error_code)
                except errors.Error:
                    error_message = 'Failed to retrieve error description.'
            warnings.warn(errors.DriverWarning(error_code, error_message))
        return response

    def abort(self):  # noqa: N802
        self._invoke(
            self._client.Abort,
            grpc_types.AbortRequest(vi=self._vi),
        )

    def change_external_calibration_password(self, old_password, new_password):  # noqa: N802
        self._invoke(
            self._client.ChangeExternalCalibrationPassword,
            grpc_types.ChangeExternalCalibrationPasswordRequest(vi=self._vi, old_password=old_password, new_password=new_password),
        )

    def check_acquisition_status(self):  # noqa: N802
        response = self._invoke(
            self._client.CheckAcquisitionStatus,
            grpc_types.CheckAcquisitionStatusRequest(vi=self._vi),
        )
        return response.is_done

    def clear_self_calibrate_range(self):  # noqa: N802
        self._invoke(
            self._client.ClearSelfCalibrateRange,
            grpc_types.ClearSelfCalibrateRangeRequest(vi=self._vi),
        )

    def commit(self):  # noqa: N802
        self._invoke(
            self._client.Commit,
            grpc_types.CommitRequest(vi=self._vi),
        )

    def configure_deembedding_table_interpolation_linear(self, port, table_name, format):  # noqa: N802
        self._invoke(
            self._client.ConfigureDeembeddingTableInterpolationLinear,
            grpc_types.ConfigureDeembeddingTableInterpolationLinearRequest(vi=self._vi, port=port, table_name=table_name, format_raw=format.value),
        )

    def configure_deembedding_table_interpolation_nearest(self, port, table_name):  # noqa: N802
        self._invoke(
            self._client.ConfigureDeembeddingTableInterpolationNearest,
            grpc_types.ConfigureDeembeddingTableInterpolationNearestRequest(vi=self._vi, port=port, table_name=table_name),
        )

    def configure_deembedding_table_interpolation_spline(self, port, table_name):  # noqa: N802
        self._invoke(
            self._client.ConfigureDeembeddingTableInterpolationSpline,
            grpc_types.ConfigureDeembeddingTableInterpolationSplineRequest(vi=self._vi, port=port, table_name=table_name),
        )

    def configure_digital_edge_advance_trigger(self, source, edge):  # noqa: N802
        self._invoke(
            self._client.ConfigureDigitalEdgeAdvanceTrigger,
            grpc_types.ConfigureDigitalEdgeAdvanceTriggerRequest(vi=self._vi, source_raw=source, edge_raw=edge.value),
        )

    def configure_digital_edge_ref_trigger(self, source, edge, pretrigger_samples):  # noqa: N802
        self._invoke(
            self._client.ConfigureDigitalEdgeRefTrigger,
            grpc_types.ConfigureDigitalEdgeRefTriggerRequest(vi=self._vi, source_raw=source, edge_raw=edge.value, pretrigger_samples=pretrigger_samples),
        )

    def configure_digital_edge_start_trigger(self, source, edge):  # noqa: N802
        self._invoke(
            self._client.ConfigureDigitalEdgeStartTrigger,
            grpc_types.ConfigureDigitalEdgeStartTriggerRequest(vi=self._vi, source_raw=source, edge_raw=edge.value),
        )

    def configure_iq_power_edge_ref_trigger(self, source, level, slope, pretrigger_samples):  # noqa: N802
        self._invoke(
            self._client.ConfigureIQPowerEdgeRefTrigger,
            grpc_types.ConfigureIQPowerEdgeRefTriggerRequest(vi=self._vi, level=level, slope_raw=slope.value, pretrigger_samples=pretrigger_samples),
        )

    def configure_ref_clock(self, clock_source, ref_clock_rate):  # noqa: N802
        self._invoke(
            self._client.ConfigureRefClock,
            grpc_types.ConfigureRefClockRequest(vi=self._vi, clock_source_raw=clock_source.value, ref_clock_rate=ref_clock_rate),
        )

    def configure_software_edge_advance_trigger(self):  # noqa: N802
        self._invoke(
            self._client.ConfigureSoftwareEdgeAdvanceTrigger,
            grpc_types.ConfigureSoftwareEdgeAdvanceTriggerRequest(vi=self._vi),
        )

    def configure_software_edge_ref_trigger(self, pretrigger_samples):  # noqa: N802
        self._invoke(
            self._client.ConfigureSoftwareEdgeRefTrigger,
            grpc_types.ConfigureSoftwareEdgeRefTriggerRequest(vi=self._vi, pretrigger_samples=pretrigger_samples),
        )

    def configure_software_edge_start_trigger(self):  # noqa: N802
        self._invoke(
            self._client.ConfigureSoftwareEdgeStartTrigger,
            grpc_types.ConfigureSoftwareEdgeStartTriggerRequest(vi=self._vi),
        )

    def configure_spectrum_frequency_center_span(self, channel_list, center_frequency, span):  # noqa: N802
        self._invoke(
            self._client.ConfigureSpectrumFrequencyCenterSpan,
            grpc_types.ConfigureSpectrumFrequencyCenterSpanRequest(vi=self._vi, channel_list=channel_list, center_frequency=center_frequency, span=span),
        )

    def configure_spectrum_frequency_start_stop(self, channel_list, start_frequency, stop_frequency):  # noqa: N802
        self._invoke(
            self._client.ConfigureSpectrumFrequencyStartStop,
            grpc_types.ConfigureSpectrumFrequencyStartStopRequest(vi=self._vi, channel_list=channel_list, start_frequency=start_frequency, stop_frequency=stop_frequency),
        )

    def create_deembedding_sparameter_table_array(self, port, table_name, frequencies, sparameter_table, number_of_ports, sparameter_orientation):  # noqa: N802
        # Use ravel() so that gRPC always receives a flat numpy array, regardless of input dimensions.
        sparameter_table_list = [
            grpc_complex_types.NIComplexNumber(real=val.real, imaginary=val.imag)
            for val in sparameter_table.ravel()
        ]
        self._invoke(
            self._client.CreateDeembeddingSparameterTableArray,
            grpc_types.CreateDeembeddingSparameterTableArrayRequest(vi=self._vi, port=port, table_name=table_name, frequencies=frequencies, sparameter_table=sparameter_table_list, number_of_ports=number_of_ports, sparameter_orientation_raw=sparameter_orientation.value),
        )

    def create_deembedding_sparameter_table_s2p_file(self, port, table_name, s2p_file_path, sparameter_orientation):  # noqa: N802
        self._invoke(
            self._client.CreateDeembeddingSparameterTableS2PFile,
            grpc_types.CreateDeembeddingSparameterTableS2PFileRequest(vi=self._vi, port=port, table_name=table_name, s2p_file_path=s2p_file_path, sparameter_orientation_raw=sparameter_orientation.value),
        )

    def delete_all_deembedding_tables(self):  # noqa: N802
        self._invoke(
            self._client.DeleteAllDeembeddingTables,
            grpc_types.DeleteAllDeembeddingTablesRequest(vi=self._vi),
        )

    def delete_deembedding_table(self, port, table_name):  # noqa: N802
        self._invoke(
            self._client.DeleteDeembeddingTable,
            grpc_types.DeleteDeembeddingTableRequest(vi=self._vi, port=port, table_name=table_name),
        )

    def disable_advance_trigger(self):  # noqa: N802
        self._invoke(
            self._client.DisableAdvanceTrigger,
            grpc_types.DisableAdvanceTriggerRequest(vi=self._vi),
        )

    def disable_ref_trigger(self):  # noqa: N802
        self._invoke(
            self._client.DisableRefTrigger,
            grpc_types.DisableRefTriggerRequest(vi=self._vi),
        )

    def disable_start_trigger(self):  # noqa: N802
        self._invoke(
            self._client.DisableStartTrigger,
            grpc_types.DisableStartTriggerRequest(vi=self._vi),
        )

    def enable_session_access(self, enable):  # noqa: N802
        self._invoke(
            self._client.EnableSessionAccess,
            grpc_types.EnableSessionAccessRequest(vi=self._vi, enable=enable),
        )

    def error_message(self, error_code):  # noqa: N802
        response = self._invoke(
            self._client.ErrorMessage,
            grpc_types.ErrorMessageRequest(vi=self._vi, status_code=error_code),
        )
        return response.error_message

    def fetch_iq_multi_record_complex_f32(self, channel_list, starting_record, number_of_records, iq_data_arrays, timeout):  # noqa: N802
        import numpy
        samples_per_record = (iq_data_arrays.shape[1]) if iq_data_arrays is not None and iq_data_arrays.ndim > 1 else 0
        response = self._invoke(
            self._client.FetchIQMultiRecordComplexF32,
            grpc_types.FetchIQMultiRecordComplexF32Request(vi=self._vi, channel_list=channel_list, starting_record=starting_record, number_of_records=number_of_records, number_of_samples=samples_per_record, timeout=timeout),
        )
        data_flat = numpy.array([complex(x.real, x.imaginary) for x in response.data], dtype=numpy.complex64)
        for rec in range(number_of_records):
            iq_data_arrays[rec] = data_flat[rec * samples_per_record:(rec + 1) * samples_per_record]
        return [waveform_info.WaveformInfo(absolute_initial_x=r.absolute_initial_x, relative_initial_x=r.relative_initial_x, x_increment=r.x_increment, actual_samples=r.actual_samples, offset=r.offset, gain=r.gain) for r in response.wfm_info]

    def fetch_iq_multi_record_complex_f64(self, channel_list, starting_record, number_of_records, iq_data_arrays, timeout):  # noqa: N802
        import numpy
        samples_per_record = (iq_data_arrays.shape[1]) if iq_data_arrays is not None and iq_data_arrays.ndim > 1 else 0
        response = self._invoke(
            self._client.FetchIQMultiRecordComplexF64,
            grpc_types.FetchIQMultiRecordComplexF64Request(vi=self._vi, channel_list=channel_list, starting_record=starting_record, number_of_records=number_of_records, number_of_samples=samples_per_record, timeout=timeout),
        )
        data_flat = numpy.array([complex(x.real, x.imaginary) for x in response.data], dtype=numpy.complex128)
        for rec in range(number_of_records):
            iq_data_arrays[rec] = data_flat[rec * samples_per_record:(rec + 1) * samples_per_record]
        return [waveform_info.WaveformInfo(absolute_initial_x=r.absolute_initial_x, relative_initial_x=r.relative_initial_x, x_increment=r.x_increment, actual_samples=r.actual_samples, offset=r.offset, gain=r.gain) for r in response.wfm_info]

    def fetch_iq_multi_record_complex_i16(self, channel_list, starting_record, number_of_records, iq_data_arrays, timeout):  # noqa: N802
        samples_per_record = (iq_data_arrays.shape[1] // 2) if iq_data_arrays is not None and iq_data_arrays.ndim > 1 else 0
        response = self._invoke(
            self._client.FetchIQMultiRecordComplexI16,
            grpc_types.FetchIQMultiRecordComplexI16Request(vi=self._vi, channel_list=channel_list, starting_record=starting_record, number_of_records=number_of_records, number_of_samples=samples_per_record, timeout=timeout),
        )
        for rec in range(number_of_records):
            for i, x in enumerate(response.data[rec * samples_per_record:(rec + 1) * samples_per_record]):
                iq_data_arrays[rec, 2 * i] = x.real
                iq_data_arrays[rec, 2 * i + 1] = x.imaginary
        return [waveform_info.WaveformInfo(absolute_initial_x=r.absolute_initial_x, relative_initial_x=r.relative_initial_x, x_increment=r.x_increment, actual_samples=r.actual_samples, offset=r.offset, gain=r.gain) for r in response.wfm_info]

    def fetch_iq_single_record_complex_f32(self, channel_list, record_number, iq_data_array, timeout):  # noqa: N802
        import numpy
        response = self._invoke(
            self._client.FetchIQSingleRecordComplexF32,
            grpc_types.FetchIQSingleRecordComplexF32Request(vi=self._vi, channel_list=channel_list, record_number=record_number, number_of_samples=len(iq_data_array), timeout=timeout),
        )
        iq_data_array[:] = numpy.array([complex(x.real, x.imaginary) for x in response.data], dtype=numpy.complex64)
        r = response.wfm_info
        return waveform_info.WaveformInfo(absolute_initial_x=r.absolute_initial_x, relative_initial_x=r.relative_initial_x, x_increment=r.x_increment, actual_samples=r.actual_samples, offset=r.offset, gain=r.gain)

    def fetch_iq_single_record_complex_f64(self, channel_list, record_number, iq_data_array, timeout):  # noqa: N802
        import numpy
        response = self._invoke(
            self._client.FetchIQSingleRecordComplexF64,
            grpc_types.FetchIQSingleRecordComplexF64Request(vi=self._vi, channel_list=channel_list, record_number=record_number, number_of_samples=len(iq_data_array), timeout=timeout),
        )
        iq_data_array[:] = numpy.array([complex(x.real, x.imaginary) for x in response.data], dtype=numpy.complex128)
        r = response.wfm_info
        return waveform_info.WaveformInfo(absolute_initial_x=r.absolute_initial_x, relative_initial_x=r.relative_initial_x, x_increment=r.x_increment, actual_samples=r.actual_samples, offset=r.offset, gain=r.gain)

    def fetch_iq_single_record_complex_i16(self, channel_list, record_number, iq_data_array, timeout):  # noqa: N802
        response = self._invoke(
            self._client.FetchIQSingleRecordComplexI16,
            grpc_types.FetchIQSingleRecordComplexI16Request(vi=self._vi, channel_list=channel_list, record_number=record_number, number_of_samples=len(iq_data_array) // 2, timeout=timeout),
        )
        for i, x in enumerate(response.data):
            iq_data_array[2 * i] = x.real
            iq_data_array[2 * i + 1] = x.imaginary
        r = response.wfm_info
        return waveform_info.WaveformInfo(absolute_initial_x=r.absolute_initial_x, relative_initial_x=r.relative_initial_x, x_increment=r.x_increment, actual_samples=r.actual_samples, offset=r.offset, gain=r.gain)

    def get_attribute_vi_boolean(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViBoolean,
            grpc_types.GetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.value

    def get_attribute_vi_int32(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt32,
            grpc_types.GetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.value

    def get_attribute_vi_int64(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt64,
            grpc_types.GetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.value

    def get_attribute_vi_real64(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViReal64,
            grpc_types.GetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.value

    def get_attribute_vi_session(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViSession,
            grpc_types.GetAttributeViSessionRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.value

    def get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViString,
            grpc_types.GetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.value

    def get_deembedding_sparameters(self):
        import numpy as np
        response = self._invoke(
            self._client.GetDeembeddingSparameters,
            grpc_types.GetDeembeddingSparametersRequest(vi=self._vi),
        )
        number_of_ports = response.number_of_ports
        sparameters = np.array([c.real + 1j * c.imaginary for c in response.sparameters], dtype=np.complex128)
        sparameters = sparameters.reshape((number_of_ports, number_of_ports))
        return sparameters

    def get_deembedding_table_number_of_ports(self):  # noqa: N802
        response = self._invoke(
            self._client.GetDeembeddingTableNumberOfPorts,
            grpc_types.GetDeembeddingTableNumberOfPortsRequest(vi=self._vi),
        )
        return response.number_of_ports

    def get_error(self):  # noqa: N802
        response = self._invoke(
            self._client.GetError,
            grpc_types.GetErrorRequest(vi=self._vi),
        )
        return response.error_code, response.error_description

    def get_ext_cal_last_date_and_time(self):  # noqa: N802
        response = self._invoke(
            self._client.GetExtCalLastDateAndTime,
            grpc_types.GetExtCalLastDateAndTimeRequest(vi=self._vi),
        )
        return response.year, response.month, response.day, response.hour, response.minute

    def get_ext_cal_recommended_interval(self):  # noqa: N802
        response = self._invoke(
            self._client.GetExtCalRecommendedInterval,
            grpc_types.GetExtCalRecommendedIntervalRequest(vi=self._vi),
        )
        return response.months

    def get_fetch_backlog(self, channel_list, record_number):  # noqa: N802
        response = self._invoke(
            self._client.GetFetchBacklog,
            grpc_types.GetFetchBacklogRequest(vi=self._vi, channel_list=channel_list, record_number=record_number),
        )
        return response.backlog

    def get_frequency_response(self, channel_list):  # noqa: N802
        response = self._invoke(
            self._client.GetFrequencyResponse,
            grpc_types.GetFrequencyResponseRequest(vi=self._vi, channel_list=channel_list),
        )
        return response.frequencies, response.magnitude_response, response.phase_response

    def get_scaling_coefficients(self, channel_list):  # noqa: N802
        response = self._invoke(
            self._client.GetScalingCoefficients,
            grpc_types.GetScalingCoefficientsRequest(vi=self._vi, channel_list=channel_list),
        )
        return [coefficient_info_type.CoefficientInfo(x) for x in response.coefficient_info]

    def get_self_cal_last_date_and_time(self, self_calibration_step):  # noqa: N802
        response = self._invoke(
            self._client.GetSelfCalLastDateAndTime,
            grpc_types.GetSelfCalLastDateAndTimeRequest(vi=self._vi, self_calibration_step=self_calibration_step.value),
        )
        return response.year, response.month, response.day, response.hour, response.minute

    def get_self_calibration_temperature(self, self_calibration_step):  # noqa: N802
        response = self._invoke(
            self._client.GetSelfCalLastTemp,
            grpc_types.GetSelfCalLastTempRequest(vi=self._vi, self_calibration_step=self_calibration_step.value),
        )
        return response.temp

    def get_terminal_name(self, signal, signal_identifier):  # noqa: N802
        response = self._invoke(
            self._client.GetTerminalName,
            grpc_types.GetTerminalNameRequest(vi=self._vi, signal_raw=signal.value, signal_identifier=signal_identifier, buffer_size=2048),
        )
        return response.terminal_name

    def init_with_options(self, resource_name, id_query, reset_device, option_string):  # noqa: N802
        metadata = (
            ('ni-api-key', self._grpc_options.api_key),
        )
        response = self._invoke(
            self._client.InitWithOptions,
            grpc_types.InitWithOptionsRequest(resource_name=resource_name, id_query=id_query, reset=reset_device, option_string=option_string, session_name=self._grpc_options.session_name, initialization_behavior=self._grpc_options.initialization_behavior),
            metadata=metadata,
        )
        self._close_on_exit = response.new_session_initialized
        return response.vi

    def initiate(self):  # noqa: N802
        self._invoke(
            self._client.Initiate,
            grpc_types.InitiateRequest(vi=self._vi),
        )

    def is_self_cal_valid(self):  # noqa: N802
        response = self._invoke(
            self._client.IsSelfCalValid,
            grpc_types.IsSelfCalValidRequest(vi=self._vi),
        )
        return response.self_cal_valid, enums.SelfCalSteps(response.valid_steps_raw)

    def load_configurations_from_file(self, channel_name, file_path):  # noqa: N802
        self._invoke(
            self._client.LoadConfigurationsFromFile,
            grpc_types.LoadConfigurationsFromFileRequest(vi=self._vi, channel_name=channel_name, file_path=file_path),
        )

    def lock(self):  # noqa: N802
        self._lock.acquire()

    def perform_thermal_correction(self):  # noqa: N802
        self._invoke(
            self._client.PerformThermalCorrection,
            grpc_types.PerformThermalCorrectionRequest(vi=self._vi),
        )

    def read_iq_single_record_complex_f64(self, channel_list, iq_data_array, timeout):  # noqa: N802
        import numpy
        response = self._invoke(
            self._client.ReadIQSingleRecordComplexF64,
            grpc_types.ReadIQSingleRecordComplexF64Request(vi=self._vi, channel_list=channel_list, timeout=timeout, data_array_size=len(iq_data_array)),
        )
        iq_data_array[:] = numpy.array([complex(x.real, x.imaginary) for x in response.data], dtype=numpy.complex128)
        r = response.wfm_info
        return waveform_info.WaveformInfo(absolute_initial_x=r.absolute_initial_x, relative_initial_x=r.relative_initial_x, x_increment=r.x_increment, actual_samples=r.actual_samples, offset=r.offset, gain=r.gain)

    def read_power_spectrum_f32(self, channel_list, timeout, power_spectrum_data_array):  # noqa: N802
        response = self._invoke(
            self._client.ReadPowerSpectrumF32,
            grpc_types.ReadPowerSpectrumF32Request(vi=self._vi, channel_list=channel_list, timeout=timeout, data_array_size=len(power_spectrum_data_array)),
        )
        power_spectrum_data_array[:] = response.power_spectrum_data
        s = response.spectrum_info
        return spectrum_info_type.SpectrumInfo(initial_frequency=s.initial_frequency, frequency_increment=s.frequency_increment, number_of_spectral_lines=s.number_of_spectral_lines)

    def read_power_spectrum_f64(self, channel_list, timeout, power_spectrum_data_array):  # noqa: N802
        response = self._invoke(
            self._client.ReadPowerSpectrumF64,
            grpc_types.ReadPowerSpectrumF64Request(vi=self._vi, channel_list=channel_list, timeout=timeout, data_array_size=len(power_spectrum_data_array)),
        )
        power_spectrum_data_array[:] = response.power_spectrum_data
        s = response.spectrum_info
        return spectrum_info_type.SpectrumInfo(initial_frequency=s.initial_frequency, frequency_increment=s.frequency_increment, number_of_spectral_lines=s.number_of_spectral_lines)

    def reset_device(self):  # noqa: N802
        self._invoke(
            self._client.ResetDevice,
            grpc_types.ResetDeviceRequest(vi=self._vi),
        )

    def reset_with_options(self, steps_to_omit):  # noqa: N802
        self._invoke(
            self._client.ResetWithOptions,
            grpc_types.ResetWithOptionsRequest(vi=self._vi, steps_to_omit_raw=steps_to_omit.value),
        )

    def save_configurations_to_file(self, channel_name, file_path):  # noqa: N802
        self._invoke(
            self._client.SaveConfigurationsToFile,
            grpc_types.SaveConfigurationsToFileRequest(vi=self._vi, channel_name=channel_name, file_path=file_path),
        )

    def self_calibrate_range(self, steps_to_omit, minimum_frequency, maximum_frequency, minimum_reference_level, maximum_reference_level):  # noqa: N802
        self._invoke(
            self._client.SelfCalibrateRange,
            grpc_types.SelfCalibrateRangeRequest(vi=self._vi, steps_to_omit_raw=steps_to_omit.value, min_frequency=minimum_frequency, max_frequency=maximum_frequency, min_reference_level=minimum_reference_level, max_reference_level=maximum_reference_level),
        )

    def send_software_edge_trigger(self, trigger, trigger_identifier):  # noqa: N802
        self._invoke(
            self._client.SendSoftwareEdgeTrigger,
            grpc_types.SendSoftwareEdgeTriggerRequest(vi=self._vi, trigger_raw=trigger.value, trigger_identifier=trigger_identifier),
        )

    def set_attribute_vi_boolean(self, channel_name, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViBoolean,
            grpc_types.SetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, value=value),
        )

    def set_attribute_vi_int32(self, channel_name, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt32,
            grpc_types.SetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, value_raw=value),
        )

    def set_attribute_vi_int64(self, channel_name, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt64,
            grpc_types.SetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, value_raw=value),
        )

    def set_attribute_vi_real64(self, channel_name, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViReal64,
            grpc_types.SetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, value_raw=value),
        )

    def set_attribute_vi_session(self, channel_name, attribute_id):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViSession,
            grpc_types.SetAttributeViSessionRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, value=self._vi),
        )

    def set_attribute_vi_string(self, channel_name, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViString,
            grpc_types.SetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, value_raw=value),
        )

    def unlock(self):  # noqa: N802
        self._lock.release()

    def close(self):  # noqa: N802
        self._invoke(
            self._client.Close,
            grpc_types.CloseRequest(vi=self._vi),
        )

    def reset(self):  # noqa: N802
        self._invoke(
            self._client.Reset,
            grpc_types.ResetRequest(vi=self._vi),
        )

    def self_test(self):  # noqa: N802
        response = self._invoke(
            self._client.SelfTest,
            grpc_types.SelfTestRequest(vi=self._vi),
        )
        return response.test_result, response.test_message
