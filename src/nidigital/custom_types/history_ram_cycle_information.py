class HistoryRAMCycleInformation(object):
    def __init__(self):
        # Attributes populated while History RAM data is being fetched from driver
        self.pattern_name = None
        self.time_set_name = None
        self.vector_number = None
        self.cycle_number = None
        self.scan_cycle_number = None
        self.expected_pin_states = None
        self.actual_pin_states = None
        self.per_pin_pass_fail = None

    def __repr__(self):
        # TODO
        # parameter_list = [
        #     'absolute_initial_x={}'.format(self.absolute_initial_x),
        #     'relative_initial_x={}'.format(self.relative_initial_x),
        #     'x_increment={}'.format(self.x_increment),
        #     'offset={}'.format(self.offset),
        #     'gain={}'.format(self.gain),
        # ]
        #
        # return '{0}({1})'.format(self.__class__.__name__, ', '.join(parameter_list))
        return self.__class__.__name__

    def __str__(self):
        # TODO
        # # different format lines
        # row_format_g = '{:<20}: {:,.6g}\n'
        # row_format_d = '{:<20}: {:,}\n'
        # row_format_s = '{:<20}: {:}\n'
        #
        # string_representation = ''
        # if self.channel is not None:  # We explicitly look for not None to differentiate from empty string
        #     string_representation += row_format_s.format('channel', self.channel)
        # if self.record is not None:  # We explicitly look for not None to differentiate from 0
        #     string_representation += row_format_d.format('record', self.record)
        #
        # string_representation += row_format_g.format('Absolute X0', self.absolute_initial_x)
        # string_representation += row_format_g.format('Relative X0', self.relative_initial_x)
        # string_representation += row_format_g.format('dt', self.x_increment)
        # string_representation += row_format_g.format('offset', self.offset)
        # string_representation += row_format_g.format('gain', self.gain)
        # if self.samples is not None:  # We explicitly look for not None to differentiate from empty array
        #     string_representation += row_format_g.format('wfm length', len(self.samples))
        #
        # # Put possible private variable last
        # if self._actual_samples is not None:  # We explicitly look for not None to differentiate from 0
        #     string_representation += row_format_d.format('_actual samples', self._actual_samples)
        #
        # return string_representation
        return self.__class__.__name__



