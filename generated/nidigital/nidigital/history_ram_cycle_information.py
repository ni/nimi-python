class HistoryRAMCycleInformation(object):
    def __init__(self, pattern_name, time_set_name, vector_number, cycle_number, scan_cycle_number, expected_pin_states, actual_pin_states, per_pin_pass_fail):
        self.pattern_name = pattern_name
        self.time_set_name = time_set_name
        self.vector_number = vector_number
        self.cycle_number = cycle_number
        self.scan_cycle_number = scan_cycle_number
        self.expected_pin_states = expected_pin_states
        self.actual_pin_states = actual_pin_states
        self.per_pin_pass_fail = per_pin_pass_fail

    def __repr__(self):
        parameter_list = [
            'pattern_name="{}"'.format(self.pattern_name),
            'time_set_name="{}"'.format(self.time_set_name),
            'vector_number={}'.format(self.vector_number),
            'cycle_number={}'.format(self.cycle_number),
            'scan_cycle_number={}'.format(self.scan_cycle_number),
            'expected_pin_states={}'.format(self._digital_states_representation(self.expected_pin_states)),
            'actual_pin_states={}'.format(self._digital_states_representation(self.actual_pin_states)),
            'per_pin_pass_fail={}'.format(self.per_pin_pass_fail),
        ]

        return '{0}.{1}({2})'.format(self.__class__.__module__, self.__class__.__qualname__, ', '.join(parameter_list))

    def __str__(self):
        # different format lines
        row_format_d = '{:<20}: {:,}\n'
        row_format_s = '{:<20}: {:}\n'

        string_representation = ''
        string_representation += row_format_s.format('Pattern Name', self.pattern_name)
        string_representation += row_format_s.format('Time Set Name', self.time_set_name)
        string_representation += row_format_d.format('Vector Number', self.vector_number)
        string_representation += row_format_d.format('Cycle Number', self.cycle_number)
        string_representation += row_format_d.format('Scan Cycle Number', self.scan_cycle_number)
        string_representation += row_format_s.format('Expected Pin States', self._digital_states_string(self.expected_pin_states))
        string_representation += row_format_s.format('Actual Pin States', self._digital_states_string(self.actual_pin_states))
        string_representation += row_format_s.format('Per Pin Pass Fail', self.per_pin_pass_fail)

        return string_representation

    @staticmethod
    def _digital_states_representation(states):
        states_representation = [['{0}.{1}.{2}'.format(i.__class__.__module__, i.__class__.__qualname__, i.name) for i in j] for j in states]
        return '[{}]'.format(', '.join(['[{}]'.format(', '.join(i)) for i in states_representation]))

    @staticmethod
    def _digital_states_string(states):
        states_string = [[str(i) for i in j] for j in states]
        return '[{}]'.format(', '.join(['[{}]'.format(', '.join(i)) for i in states_string]))

