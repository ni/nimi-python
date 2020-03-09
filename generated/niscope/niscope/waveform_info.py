import ctypes

import niscope._visatype


# This class is an internal implementation detail
# ctypes definition
# Name must match exactly what the name of the structure type is named in the C API.
class struct_niScope_wfmInfo(ctypes.Structure):  # noqa N801
    _pack_ = 8
    _fields_ = [
        ('absolute_initial_x', niscope._visatype.ViReal64),
        ('relative_initial_x', niscope._visatype.ViReal64),
        ('x_increment', niscope._visatype.ViReal64),
        ('actual_samples', niscope._visatype.ViInt32),
        ('offset', niscope._visatype.ViReal64),
        ('gain', niscope._visatype.ViReal64),
        ('reserved1', niscope._visatype.ViReal64),
        ('reserved2', niscope._visatype.ViReal64),
    ]

    def __init__(self, data=None, absolute_initial_x=0.0, relative_initial_x=0.0,
                 x_increment=0.0, actual_samples=0, offset=0.0, gain=0.0,
                 reserved1=0.0, reserved2=0.0):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            self.absolute_initial_x = data.absolute_initial_x
            self.relative_initial_x = data.relative_initial_x
            self.x_increment = data.x_increment
            self.actual_samples = data.actual_samples
            self.offset = data.offset
            self.gain = data.gain
            self.reserved1 = data.reserved1
            self.reserved2 = data.reserved2
        else:
            self.absolute_initial_x = absolute_initial_x
            self.relative_initial_x = relative_initial_x
            self.x_increment = x_increment
            self.actual_samples = actual_samples
            self.offset = offset
            self.gain = gain
            self.reserved1 = reserved1
            self.reserved2 = reserved2


class WaveformInfo(object):
    def __init__(self, data=None, absolute_initial_x=0.0, relative_initial_x=0.0,
                 x_increment=0.0, offset=0.0, gain=0.0,
                 reserved1=0.0, reserved2=0.0):
        if data is not None:
            self.absolute_initial_x = data.absolute_initial_x
            self.relative_initial_x = data.relative_initial_x
            self.x_increment = data.x_increment
            self.offset = data.offset
            self.gain = data.gain
            self.reserved1 = data.reserved1
            self.reserved2 = data.reserved2
            self._actual_samples = data.actual_samples
        else:
            self.absolute_initial_x = absolute_initial_x
            self.relative_initial_x = relative_initial_x
            self.x_increment = x_increment
            self.offset = offset
            self.gain = gain
            self.reserved1 = reserved1
            self.reserved2 = reserved2
            # _actual_samples is only used to calculate the end of the waveform we extract from the
            # entire 1D array of samples. It is only filled in when calling into the niscope driver.
            self._actual_samples = None

        # Additional fields filled in during fetch or fetch_into
        self.channel = None
        self.record = None
        self.samples = None

    def __repr__(self):
        parameter_list = [
            'absolute_initial_x={}'.format(self.absolute_initial_x),
            'relative_initial_x={}'.format(self.relative_initial_x),
            'x_increment={}'.format(self.x_increment),
            'offset={}'.format(self.offset),
            'gain={}'.format(self.gain),
        ]

        return '{0}({1})'.format(self.__class__.__name__, ', '.join(parameter_list))

    def __str__(self):
        # different format lines
        row_format_g = '{:<20}: {:,.6g}\n'
        row_format_d = '{:<20}: {:,}\n'
        row_format_s = '{:<20}: {:}\n'

        string_representation = ''
        if self.channel is not None:  # We explicitly look for not None to differentiate from empty string
            string_representation += row_format_s.format('channel', self.channel)
        if self.record is not None:  # We explicitly look for not None to differentiate from 0
            string_representation += row_format_d.format('record', self.record)

        string_representation += row_format_g.format('Absolute X0', self.absolute_initial_x)
        string_representation += row_format_g.format('Relative X0', self.relative_initial_x)
        string_representation += row_format_g.format('dt', self.x_increment)
        string_representation += row_format_g.format('offset', self.offset)
        string_representation += row_format_g.format('gain', self.gain)
        if self.samples is not None:  # We explicitly look for not None to differentiate from empty array
            string_representation += row_format_g.format('wfm length', len(self.samples))

        # Put possible private variable last
        if self._actual_samples is not None:  # We explicitly look for not None to differentiate from 0
            string_representation += row_format_d.format('_actual samples', self._actual_samples)

        return string_representation



