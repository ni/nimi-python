<%page args="f, config, method_template"/>\
<%
    '''Forwards to History RAM fetch functions'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        # TODO : Figure out how to do error handling
        if position < 0:
            raise ValueError('position should be greater than or equal to 0.')

        if samples_to_read < -1:
            raise ValueError('samples_to_read should be greater than or equal to -1.')

        samples_available = self.get_history_ram_sample_count(site)
        if position >= samples_available:
            raise ValueError('position: Specified value = {0}, Maximum value = {1}.'.format(position, samples_available - 1))

        if samples_to_read == -1:
            if not self.history_ram_number_of_samples_is_finite:
                raise errors.DriverError(
                    -1074118484,
                    'Specifying -1 to fetch all History RAM samples is not supported when the digital pattern instrument is '
                    'configured for continuous History RAM acquisition. You must specify an exact number of samples to fetch.')
            samples_to_read = samples_available - position

        if position + samples_to_read > samples_available:
            raise ValueError(
                'position: Specified value = {0}, samples_to_read: Specified value = {1}; Samples available = {2}.'
                .format(position, samples_to_read, samples_available))

        pattern_names = {}
        time_set_names = {}
        cycle_infos = []
        for _ in range(samples_to_read):
            cycle_info = history_ram_cycle_information.HistoryRAMCycleInformation()

            pattern_index, time_set_index, vector_number, cycle_number, num_dut_cycles = self._${f['python_name']}(site, position)

            if pattern_index not in pattern_names:
                pattern_names[pattern_index] = self.get_pattern_name(pattern_index)
            cycle_info.pattern_name = pattern_names[pattern_index]

            if time_set_index not in time_set_names:
                time_set_names[time_set_index] = self.get_time_set_name(time_set_index)
            cycle_info.time_set_name = time_set_names[time_set_index]

            cycle_info.vector_number = vector_number
            cycle_info.cycle_number = cycle_number
            cycle_info.scan_cycle_number = self._fetch_history_ram_scan_cycle_number(site, position)

            cycle_info.expected_pin_states = []
            cycle_info.actual_pin_states = []
            cycle_info.per_pin_pass_fail = []
            for dut_cycle_index in range(num_dut_cycles):
                expected_pin_states, actual_pin_states, per_pin_pass_fail = self._fetch_history_ram_cycle_pin_data(site, pin_list, position, dut_cycle_index)
                cycle_info.expected_pin_states.append(expected_pin_states)
                cycle_info.actual_pin_states.append(actual_pin_states)
                cycle_info.per_pin_pass_fail.append(per_pin_pass_fail)

            cycle_infos.append(cycle_info)
            position += 1

        return cycle_infos

