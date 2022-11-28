
    def fetch_array_measurement(self, channel_list, timeout, array_meas_function, measurement_waveform_size):  # noqa: N802
        response = self._invoke(
            self._client.FetchArrayMeasurement,
            grpc_types.FetchArrayMeasurementRequest(vi=self._vi, channel_list=channel_list, timeout=timeout, array_meas_function_raw=array_meas_function.value),
        )
        return response.meas_wfm, [waveform_info.WaveformInfo(x) for x in response.wfm_info]
