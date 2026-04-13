# -*- coding: utf-8 -*-
# This file was generated

import grpc
import hightime  # noqa: F401
import threading
import warnings

from . import enums as enums  # noqa: F401
from . import errors as errors
from . import nidigitalpattern_pb2 as grpc_types
from . import nidigitalpattern_pb2_grpc as nidigital_grpc
from . import session_pb2 as session_grpc_types

from . import history_ram_cycle_information as history_ram_cycle_information  # noqa: F401


class GrpcStubInterpreter(object):
    '''Interpreter for interacting with a gRPC Stub class'''

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._lock = threading.RLock()
        self._client = nidigital_grpc.NiDigitalStub(grpc_options.grpc_channel)
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
                error_message = 'Failed to connect to server'
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

    def abort_keep_alive(self):  # noqa: N802
        self._invoke(
            self._client.AbortKeepAlive,
            grpc_types.AbortKeepAliveRequest(vi=self._vi),
        )

    def apply_levels_and_timing(self, site_list, levels_sheet, timing_sheet, initial_state_high_pins, initial_state_low_pins, initial_state_tristate_pins):  # noqa: N802
        self._invoke(
            self._client.ApplyLevelsAndTiming,
            grpc_types.ApplyLevelsAndTimingRequest(vi=self._vi, site_list=site_list, levels_sheet=levels_sheet, timing_sheet=timing_sheet, initial_state_high_pins=initial_state_high_pins, initial_state_low_pins=initial_state_low_pins, initial_state_tristate_pins=initial_state_tristate_pins),
        )

    def apply_tdr_offsets(self, channel_list, offsets):  # noqa: N802
        self._invoke(
            self._client.ApplyTDROffsets,
            grpc_types.ApplyTDROffsetsRequest(vi=self._vi, channel_list=channel_list, offsets=offsets),
        )

    def burst_pattern(self, site_list, start_label, select_digital_function, wait_until_done, timeout):  # noqa: N802
        self._invoke(
            self._client.BurstPattern,
            grpc_types.BurstPatternRequest(vi=self._vi, site_list=site_list, start_label=start_label, select_digital_function=select_digital_function, wait_until_done=wait_until_done, timeout=timeout),
        )

    def clock_generator_abort(self, channel_list):  # noqa: N802
        self._invoke(
            self._client.ClockGeneratorAbort,
            grpc_types.ClockGeneratorAbortRequest(vi=self._vi, channel_list=channel_list),
        )

    def clock_generator_generate_clock(self, channel_list, frequency, select_digital_function):  # noqa: N802
        self._invoke(
            self._client.ClockGeneratorGenerateClock,
            grpc_types.ClockGeneratorGenerateClockRequest(vi=self._vi, channel_list=channel_list, frequency=frequency, select_digital_function=select_digital_function),
        )

    def commit(self):  # noqa: N802
        self._invoke(
            self._client.Commit,
            grpc_types.CommitRequest(vi=self._vi),
        )

    def configure_active_load_levels(self, channel_list, iol, ioh, vcom):  # noqa: N802
        self._invoke(
            self._client.ConfigureActiveLoadLevels,
            grpc_types.ConfigureActiveLoadLevelsRequest(vi=self._vi, channel_list=channel_list, iol=iol, ioh=ioh, vcom=vcom),
        )

    def configure_pattern_burst_sites(self, site_list):  # noqa: N802
        self._invoke(
            self._client.ConfigurePatternBurstSites,
            grpc_types.ConfigurePatternBurstSitesRequest(vi=self._vi, site_list=site_list),
        )

    def configure_time_set_compare_edges_strobe(self, pin_list, time_set_name, strobe_edge):  # noqa: N802
        self._invoke(
            self._client.ConfigureTimeSetCompareEdgesStrobe,
            grpc_types.ConfigureTimeSetCompareEdgesStrobeRequest(vi=self._vi, pin_list=pin_list, time_set_name=time_set_name, strobe_edge=strobe_edge),
        )

    def configure_time_set_compare_edges_strobe2x(self, pin_list, time_set_name, strobe_edge, strobe2_edge):  # noqa: N802
        self._invoke(
            self._client.ConfigureTimeSetCompareEdgesStrobe2x,
            grpc_types.ConfigureTimeSetCompareEdgesStrobe2xRequest(vi=self._vi, pin_list=pin_list, time_set_name=time_set_name, strobe_edge=strobe_edge, strobe2_edge=strobe2_edge),
        )

    def configure_time_set_drive_edges(self, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge):  # noqa: N802
        self._invoke(
            self._client.ConfigureTimeSetDriveEdges,
            grpc_types.ConfigureTimeSetDriveEdgesRequest(vi=self._vi, pin_list=pin_list, time_set_name=time_set_name, format_raw=format.value, drive_on_edge=drive_on_edge, drive_data_edge=drive_data_edge, drive_return_edge=drive_return_edge, drive_off_edge=drive_off_edge),
        )

    def configure_time_set_drive_edges2x(self, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge):  # noqa: N802
        self._invoke(
            self._client.ConfigureTimeSetDriveEdges2x,
            grpc_types.ConfigureTimeSetDriveEdges2xRequest(vi=self._vi, pin_list=pin_list, time_set_name=time_set_name, format_raw=format.value, drive_on_edge=drive_on_edge, drive_data_edge=drive_data_edge, drive_return_edge=drive_return_edge, drive_off_edge=drive_off_edge, drive_data2_edge=drive_data2_edge, drive_return2_edge=drive_return2_edge),
        )

    def configure_time_set_drive_format(self, pin_list, time_set_name, drive_format):  # noqa: N802
        self._invoke(
            self._client.ConfigureTimeSetDriveFormat,
            grpc_types.ConfigureTimeSetDriveFormatRequest(vi=self._vi, pin_list=pin_list, time_set_name=time_set_name, drive_format_raw=drive_format.value),
        )

    def configure_time_set_edge(self, pin_list, time_set_name, edge, time):  # noqa: N802
        self._invoke(
            self._client.ConfigureTimeSetEdge,
            grpc_types.ConfigureTimeSetEdgeRequest(vi=self._vi, pin_list=pin_list, time_set_name=time_set_name, edge_raw=edge.value, time=time),
        )

    def configure_time_set_edge_multiplier(self, pin_list, time_set_name, edge_multiplier):  # noqa: N802
        self._invoke(
            self._client.ConfigureTimeSetEdgeMultiplier,
            grpc_types.ConfigureTimeSetEdgeMultiplierRequest(vi=self._vi, pin_list=pin_list, time_set_name=time_set_name, edge_multiplier=edge_multiplier),
        )

    def configure_time_set_period(self, time_set_name, period):  # noqa: N802
        self._invoke(
            self._client.ConfigureTimeSetPeriod,
            grpc_types.ConfigureTimeSetPeriodRequest(vi=self._vi, time_set_name=time_set_name, period=period),
        )

    def configure_voltage_levels(self, channel_list, vil, vih, vol, voh, vterm):  # noqa: N802
        self._invoke(
            self._client.ConfigureVoltageLevels,
            grpc_types.ConfigureVoltageLevelsRequest(vi=self._vi, channel_list=channel_list, vil=vil, vih=vih, vol=vol, voh=voh, vterm=vterm),
        )

    def create_capture_waveform_from_file_digicapture(self, waveform_name, waveform_file_path):  # noqa: N802
        self._invoke(
            self._client.CreateCaptureWaveformFromFileDigicapture,
            grpc_types.CreateCaptureWaveformFromFileDigicaptureRequest(vi=self._vi, waveform_name=waveform_name, waveform_file_path=waveform_file_path),
        )

    def create_capture_waveform_parallel(self, pin_list, waveform_name):  # noqa: N802
        self._invoke(
            self._client.CreateCaptureWaveformParallel,
            grpc_types.CreateCaptureWaveformParallelRequest(vi=self._vi, pin_list=pin_list, waveform_name=waveform_name),
        )

    def create_capture_waveform_serial(self, pin_list, waveform_name, sample_width, bit_order):  # noqa: N802
        self._invoke(
            self._client.CreateCaptureWaveformSerial,
            grpc_types.CreateCaptureWaveformSerialRequest(vi=self._vi, pin_list=pin_list, waveform_name=waveform_name, sample_width=sample_width, bit_order_raw=bit_order.value),
        )

    def create_source_waveform_from_file_tdms(self, waveform_name, waveform_file_path, write_waveform_data):  # noqa: N802
        self._invoke(
            self._client.CreateSourceWaveformFromFileTDMS,
            grpc_types.CreateSourceWaveformFromFileTDMSRequest(vi=self._vi, waveform_name=waveform_name, waveform_file_path=waveform_file_path, write_waveform_data=write_waveform_data),
        )

    def create_source_waveform_parallel(self, pin_list, waveform_name, data_mapping):  # noqa: N802
        self._invoke(
            self._client.CreateSourceWaveformParallel,
            grpc_types.CreateSourceWaveformParallelRequest(vi=self._vi, pin_list=pin_list, waveform_name=waveform_name, data_mapping_raw=data_mapping.value),
        )

    def create_source_waveform_serial(self, pin_list, waveform_name, data_mapping, sample_width, bit_order):  # noqa: N802
        self._invoke(
            self._client.CreateSourceWaveformSerial,
            grpc_types.CreateSourceWaveformSerialRequest(vi=self._vi, pin_list=pin_list, waveform_name=waveform_name, data_mapping_raw=data_mapping.value, sample_width=sample_width, bit_order_raw=bit_order.value),
        )

    def create_time_set(self, name):  # noqa: N802
        self._invoke(
            self._client.CreateTimeSet,
            grpc_types.CreateTimeSetRequest(vi=self._vi, name=name),
        )

    def delete_all_time_sets(self):  # noqa: N802
        self._invoke(
            self._client.DeleteAllTimeSets,
            grpc_types.DeleteAllTimeSetsRequest(vi=self._vi),
        )

    def disable_sites(self, site_list):  # noqa: N802
        self._invoke(
            self._client.DisableSites,
            grpc_types.DisableSitesRequest(vi=self._vi, site_list=site_list),
        )

    def enable_sites(self, site_list):  # noqa: N802
        self._invoke(
            self._client.EnableSites,
            grpc_types.EnableSitesRequest(vi=self._vi, site_list=site_list),
        )

    def fetch_capture_waveform(self, site_list, waveform_name, samples_to_read, timeout):  # noqa: N802
        response = self._invoke(
            self._client.FetchCaptureWaveformU32,
            grpc_types.FetchCaptureWaveformU32Request(vi=self._vi, site_list=site_list, waveform_name=waveform_name, samples_to_read=samples_to_read, timeout=timeout),
        )
        return bytes(response.data), response.actual_num_waveforms, response.actual_samples_per_waveform

    def fetch_history_ram_cycle_information(self, site, sample_index):  # noqa: N802
        response = self._invoke(
            self._client.FetchHistoryRAMCycleInformation,
            grpc_types.FetchHistoryRAMCycleInformationRequest(vi=self._vi, site=site, sample_index=sample_index),
        )
        return response.pattern_index, response.time_set_index, response.vector_number, response.cycle_number, response.num_dut_cycles

    def fetch_history_ram_cycle_pin_data(self, site, pin_list, sample_index, dut_cycle_index):  # noqa: N802
        response = self._invoke(
            self._client.FetchHistoryRAMCyclePinData,
            grpc_types.FetchHistoryRAMCyclePinDataRequest(vi=self._vi, site=site, pin_list=pin_list, sample_index=sample_index, dut_cycle_index=dut_cycle_index),
        )
        return [enums.PinState(x) for x in response.expected_pin_states_raw], [enums.PinState(x) for x in response.actual_pin_states_raw], response.per_pin_pass_fail

    def fetch_history_ram_scan_cycle_number(self, site, sample_index):  # noqa: N802
        response = self._invoke(
            self._client.FetchHistoryRAMScanCycleNumber,
            grpc_types.FetchHistoryRAMScanCycleNumberRequest(vi=self._vi, site=site, sample_index=sample_index),
        )
        return response.scan_cycle_number

    def frequency_counter_measure_frequency(self, channel_list):  # noqa: N802
        response = self._invoke(
            self._client.FrequencyCounterMeasureFrequency,
            grpc_types.FrequencyCounterMeasureFrequencyRequest(vi=self._vi, channel_list=channel_list),
        )
        return response.frequencies

    def get_attribute_vi_boolean(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViBoolean,
            grpc_types.GetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute=attribute),
        )
        return response.value

    def get_attribute_vi_int32(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt32,
            grpc_types.GetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute=attribute),
        )
        return response.value

    def get_attribute_vi_int64(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt64,
            grpc_types.GetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute=attribute),
        )
        return response.value

    def get_attribute_vi_real64(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViReal64,
            grpc_types.GetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute=attribute),
        )
        return response.value

    def get_attribute_vi_string(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViString,
            grpc_types.GetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute=attribute),
        )
        return response.value

    def get_channel_names(self, indices):  # noqa: N802
        response = self._invoke(
            self._client.GetChannelNameFromString,
            grpc_types.GetChannelNameFromStringRequest(vi=self._vi, indices=indices),
        )
        return response.names

    def get_error(self):  # noqa: N802
        response = self._invoke(
            self._client.GetError,
            grpc_types.GetErrorRequest(vi=self._vi),
        )
        return response.error_code, response.error_description

    def get_fail_count(self, channel_list):  # noqa: N802
        response = self._invoke(
            self._client.GetFailCount,
            grpc_types.GetFailCountRequest(vi=self._vi, channel_list=channel_list),
        )
        return response.failure_count

    def get_history_ram_sample_count(self, site):  # noqa: N802
        response = self._invoke(
            self._client.GetHistoryRAMSampleCount,
            grpc_types.GetHistoryRAMSampleCountRequest(vi=self._vi, site=site),
        )
        return response.sample_count

    def get_pattern_name(self, pattern_index):  # noqa: N802
        response = self._invoke(
            self._client.GetPatternName,
            grpc_types.GetPatternNameRequest(vi=self._vi, pattern_index=pattern_index),
        )
        return response.name

    def get_pattern_pin_names(self, start_label):  # noqa: N802
        response = self._invoke(
            self._client.GetPatternPinList,
            grpc_types.GetPatternPinListRequest(vi=self._vi, start_label=start_label),
        )
        return response.pin_list

    def get_pin_name(self, pin_index):  # noqa: N802
        response = self._invoke(
            self._client.GetPinName,
            grpc_types.GetPinNameRequest(vi=self._vi, pin_index=pin_index),
        )
        return response.name

    def get_pin_results_pin_information(self, channel_list):  # noqa: N802
        response = self._invoke(
            self._client.GetPinResultsPinInformation,
            grpc_types.GetPinResultsPinInformationRequest(vi=self._vi, channel_list=channel_list),
        )
        return response.pin_indexes, response.site_numbers, response.channel_indexes

    def get_site_pass_fail(self, site_list):  # noqa: N802
        response = self._invoke(
            self._client.GetSitePassFail,
            grpc_types.GetSitePassFailRequest(vi=self._vi, site_list=site_list),
        )
        return response.pass_fail

    def get_site_results_site_numbers(self, site_list, site_result_type):  # noqa: N802
        response = self._invoke(
            self._client.GetSiteResultsSiteNumbers,
            grpc_types.GetSiteResultsSiteNumbersRequest(vi=self._vi, site_list=site_list, site_result_type_raw=site_result_type.value),
        )
        return response.site_numbers

    def get_time_set_drive_format(self, pin, time_set_name):  # noqa: N802
        response = self._invoke(
            self._client.GetTimeSetDriveFormat,
            grpc_types.GetTimeSetDriveFormatRequest(vi=self._vi, pin=pin, time_set_name=time_set_name),
        )
        return enums.DriveFormat(response.format_raw)

    def get_time_set_edge(self, pin, time_set_name, edge):  # noqa: N802
        response = self._invoke(
            self._client.GetTimeSetEdge,
            grpc_types.GetTimeSetEdgeRequest(vi=self._vi, pin=pin, time_set_name=time_set_name, edge_raw=edge.value),
        )
        return response.time

    def get_time_set_edge_multiplier(self, pin, time_set_name):  # noqa: N802
        response = self._invoke(
            self._client.GetTimeSetEdgeMultiplier,
            grpc_types.GetTimeSetEdgeMultiplierRequest(vi=self._vi, pin=pin, time_set_name=time_set_name),
        )
        return response.edge_multiplier

    def get_time_set_name(self, time_set_index):  # noqa: N802
        response = self._invoke(
            self._client.GetTimeSetName,
            grpc_types.GetTimeSetNameRequest(vi=self._vi, time_set_index=time_set_index),
        )
        return response.name

    def get_time_set_period(self, time_set_name):  # noqa: N802
        response = self._invoke(
            self._client.GetTimeSetPeriod,
            grpc_types.GetTimeSetPeriodRequest(vi=self._vi, time_set_name=time_set_name),
        )
        return response.period

    def init_with_options(self, resource_name, id_query, reset_device, option_string):  # noqa: N802
        metadata = (
            ('ni-api-key', self._grpc_options.api_key),
        )
        response = self._invoke(
            self._client.InitWithOptions,
            grpc_types.InitWithOptionsRequest(resource_name=resource_name, id_query=id_query, reset_device=reset_device, option_string=option_string, session_name=self._grpc_options.session_name, initialization_behavior=self._grpc_options.initialization_behavior),
            metadata=metadata,
        )
        self._close_on_exit = response.new_session_initialized
        return response.vi

    def initiate(self):  # noqa: N802
        self._invoke(
            self._client.Initiate,
            grpc_types.InitiateRequest(vi=self._vi),
        )

    def is_done(self):  # noqa: N802
        response = self._invoke(
            self._client.IsDone,
            grpc_types.IsDoneRequest(vi=self._vi),
        )
        return response.done

    def is_site_enabled(self, site):  # noqa: N802
        response = self._invoke(
            self._client.IsSiteEnabled,
            grpc_types.IsSiteEnabledRequest(vi=self._vi, site=site),
        )
        return response.enable

    def load_levels(self, file_path):  # noqa: N802
        self._invoke(
            self._client.LoadLevels,
            grpc_types.LoadLevelsRequest(vi=self._vi, file_path=file_path),
        )

    def load_pattern(self, file_path):  # noqa: N802
        self._invoke(
            self._client.LoadPattern,
            grpc_types.LoadPatternRequest(vi=self._vi, file_path=file_path),
        )

    def load_pin_map(self, file_path):  # noqa: N802
        self._invoke(
            self._client.LoadPinMap,
            grpc_types.LoadPinMapRequest(vi=self._vi, file_path=file_path),
        )

    def load_specifications(self, file_path):  # noqa: N802
        self._invoke(
            self._client.LoadSpecifications,
            grpc_types.LoadSpecificationsRequest(vi=self._vi, file_path=file_path),
        )

    def load_timing(self, file_path):  # noqa: N802
        self._invoke(
            self._client.LoadTiming,
            grpc_types.LoadTimingRequest(vi=self._vi, file_path=file_path),
        )

    def lock(self):  # noqa: N802
        self._lock.acquire()

    def ppmu_measure(self, channel_list, measurement_type):  # noqa: N802
        response = self._invoke(
            self._client.PPMUMeasure,
            grpc_types.PPMUMeasureRequest(vi=self._vi, channel_list=channel_list, measurement_type_raw=measurement_type.value),
        )
        return response.measurements

    def ppmu_source(self, channel_list):  # noqa: N802
        self._invoke(
            self._client.PPMUSource,
            grpc_types.PPMUSourceRequest(vi=self._vi, channel_list=channel_list),
        )

    def read_sequencer_flag(self, flag):  # noqa: N802
        response = self._invoke(
            self._client.ReadSequencerFlag,
            grpc_types.ReadSequencerFlagRequest(vi=self._vi, flag=flag.value),
        )
        return response.value

    def read_sequencer_register(self, reg):  # noqa: N802
        response = self._invoke(
            self._client.ReadSequencerRegister,
            grpc_types.ReadSequencerRegisterRequest(vi=self._vi, reg=reg.value),
        )
        return response.value

    def read_static(self, channel_list):  # noqa: N802
        response = self._invoke(
            self._client.ReadStatic,
            grpc_types.ReadStaticRequest(vi=self._vi, channel_list=channel_list),
        )
        return [enums.PinState(x) for x in response.data_raw]

    def reset_device(self):  # noqa: N802
        self._invoke(
            self._client.ResetDevice,
            grpc_types.ResetDeviceRequest(vi=self._vi),
        )

    def self_calibrate(self):  # noqa: N802
        self._invoke(
            self._client.SelfCalibrate,
            grpc_types.SelfCalibrateRequest(vi=self._vi),
        )

    def send_software_edge_trigger(self, trigger, trigger_identifier):  # noqa: N802
        self._invoke(
            self._client.SendSoftwareEdgeTrigger,
            grpc_types.SendSoftwareEdgeTriggerRequest(vi=self._vi, trigger_raw=trigger.value, trigger_identifier=trigger_identifier),
        )

    def set_attribute_vi_boolean(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViBoolean,
            grpc_types.SetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute=attribute, value=value),
        )

    def set_attribute_vi_int32(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt32,
            grpc_types.SetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute=attribute, value_raw=value),
        )

    def set_attribute_vi_int64(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt64,
            grpc_types.SetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute=attribute, value_raw=value),
        )

    def set_attribute_vi_real64(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViReal64,
            grpc_types.SetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute=attribute, value_raw=value),
        )

    def set_attribute_vi_string(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViString,
            grpc_types.SetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute=attribute, value_raw=value),
        )

    def set_runtime_environment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        raise NotImplementedError('set_runtime_environment is not supported over gRPC')

    def tdr(self, channel_list, apply_offsets):  # noqa: N802
        response = self._invoke(
            self._client.TDR,
            grpc_types.TDRRequest(vi=self._vi, channel_list=channel_list, apply_offsets=apply_offsets),
        )
        return response.offsets

    def unload_all_patterns(self, unload_keep_alive_pattern):  # noqa: N802
        self._invoke(
            self._client.UnloadAllPatterns,
            grpc_types.UnloadAllPatternsRequest(vi=self._vi, unload_keep_alive_pattern=unload_keep_alive_pattern),
        )

    def unload_specifications(self, file_path):  # noqa: N802
        self._invoke(
            self._client.UnloadSpecifications,
            grpc_types.UnloadSpecificationsRequest(vi=self._vi, file_path=file_path),
        )

    def unlock(self):  # noqa: N802
        self._lock.release()

    def wait_until_done(self, timeout):  # noqa: N802
        self._invoke(
            self._client.WaitUntilDone,
            grpc_types.WaitUntilDoneRequest(vi=self._vi, timeout=timeout),
        )

    def write_sequencer_flag(self, flag, value):  # noqa: N802
        self._invoke(
            self._client.WriteSequencerFlag,
            grpc_types.WriteSequencerFlagRequest(vi=self._vi, flag=flag.value, value=value),
        )

    def write_sequencer_register(self, reg, value):  # noqa: N802
        self._invoke(
            self._client.WriteSequencerRegister,
            grpc_types.WriteSequencerRegisterRequest(vi=self._vi, reg=reg.value, value=value),
        )

    def write_source_waveform_broadcast(self, waveform_name, waveform_data):  # noqa: N802
        self._invoke(
            self._client.WriteSourceWaveformBroadcastU32,
            grpc_types.WriteSourceWaveformBroadcastU32Request(vi=self._vi, waveform_name=waveform_name, waveform_data=waveform_data),
        )

    def write_source_waveform_data_from_file_tdms(self, waveform_name, waveform_file_path):  # noqa: N802
        self._invoke(
            self._client.WriteSourceWaveformDataFromFileTDMS,
            grpc_types.WriteSourceWaveformDataFromFileTDMSRequest(vi=self._vi, waveform_name=waveform_name, waveform_file_path=waveform_file_path),
        )

    def write_source_waveform_site_unique_u32(self, site_list, waveform_name, num_waveforms, samples_per_waveform, waveform_data):  # noqa: N802
        self._invoke(
            self._client.WriteSourceWaveformSiteUniqueU32,
            grpc_types.WriteSourceWaveformSiteUniqueU32Request(vi=self._vi, site_list=site_list, waveform_name=waveform_name, num_waveforms=num_waveforms, samples_per_waveform=samples_per_waveform, waveform_data=waveform_data),
        )

    def write_static(self, channel_list, state):  # noqa: N802
        self._invoke(
            self._client.WriteStatic,
            grpc_types.WriteStaticRequest(vi=self._vi, channel_list=channel_list, state_raw=state.value),
        )

    def close(self):  # noqa: N802
        self._invoke(
            self._client.Close,
            grpc_types.CloseRequest(vi=self._vi),
        )

    def error_message(self, error_code):  # noqa: N802
        response = self._invoke(
            self._client.ErrorMessage,
            grpc_types.ErrorMessageRequest(vi=self._vi, error_code=error_code),
        )
        return response.error_message

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
