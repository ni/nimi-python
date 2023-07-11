<%page args="results_name='wfm_info', results_description='waveforms', output_name='wfm_info'"/>\
<%
    '''Sub-template to populate channel and record info for a waveform in a fetch method.'''
%>\
        channel_names = _converters.expand_channel_string(
            self._repeated_capability,
            self._all_channels_in_session
        )

        ${results_name}_count = len(${results_name})
        channel_count = len(channel_names)
        # Should this raise instead? If this asserts, is it the users fault?
        assert ${results_name}_count % channel_count == 0, 'Number of ${results_description} should be evenly divisible by the number of channels: len(${results_name}) == {0}, len(channel_names) == {1}'.format(${results_name}_count, channel_count)
        actual_num_records = int(${results_name}_count / channel_count)
        waveform_info._populate_channel_and_record_info(${output_name}, channel_names, range(record_number, record_number + actual_num_records))