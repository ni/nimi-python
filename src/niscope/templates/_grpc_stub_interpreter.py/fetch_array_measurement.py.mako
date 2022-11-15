
    def fetch_array_measurement(self, channel_list, timeout, array_meas_function, measurement_waveform_size):  # noqa: N802
        if measurement_waveform_size is not None:
            raise ValueError("When using grpc-device, measurement_waveform_size should be None.")
        response = self._invoke(
            self._client.FetchArrayMeasurement,
            grpc_types.FetchArrayMeasurementRequest(vi=self._vi, channel_list=channel_list, timeout=timeout, array_meas_function_raw=array_meas_function.value),
        )
        return response.meas_wfm, [waveform_info.WaveformInfo(x) for x in response.wfm_info]
