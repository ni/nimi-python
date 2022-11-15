
    def fetch_capture_waveform(self, site_list, waveform_name, samples_to_read, timeout):  # noqa: N802
        response = self._invoke(
            self._client.FetchCaptureWaveformU32,
            grpc_types.FetchCaptureWaveformU32Request(vi=self._vi, site_list=site_list, waveform_name=waveform_name, samples_to_read=samples_to_read, timeout=timeout),
        )
        ## Modified (vs. default generated code) to return bytes() and both size outputs
        return bytes(response.data), response.actual_num_waveforms, response.actual_samples_per_waveform
