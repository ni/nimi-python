<%page args="f, config, method_template"/>\
<%
    '''Forwards to History RAM fetch functions'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
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
            pattern_index, time_set_index, vector_number, cycle_number, num_dut_cycles = self._${f['python_name']}(position)

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
