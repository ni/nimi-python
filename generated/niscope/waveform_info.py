import ctypes

from niscope import visatype


# This class is an internal implementation detail
# ctypes definition
# Name must match exactly what the name of the structure type is named in the C API.
class struct_niScope_wfmInfo(ctypes.Structure):  # noqa N801
    _pack_ = 8
    _fields_ = [
        ('absolute_initial_x', visatype.ViReal64),
        ('relative_initial_x', visatype.ViReal64),
        ('x_increment', visatype.ViReal64),
        ('actual_samples', visatype.ViInt32),
        ('offset', visatype.ViReal64),
        ('gain', visatype.ViReal64),
        ('reserved1', visatype.ViReal64),
        ('reserved2', visatype.ViReal64),
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
                 x_increment=0.0, actual_samples=0, offset=0.0, gain=0.0,
                 reserved1=0.0, reserved2=0.0):
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

    def __repr__(self):
        return '{0}(absolute_initial_x={1}, relative_initial_x={2}, x_increment={3}, actual_samples={4}, offset={5}, gain={6})'.format(
            self.__class__.__name__, self.absolute_initial_x, self.relative_initial_x, self.x_increment,
            self.actual_samples, self.offset, self.gain)

    def __str__(self):
        row_format_g = '{:<20}: {:,.6g}'
        row_format_d = '{:<20}: {:,}'
        string_representation = row_format_g.format('Absolute X0', self.absolute_initial_x) + '\n'
        string_representation += row_format_g.format('Relative X0', self.relative_initial_x) + '\n'
        string_representation += row_format_g.format('dt', self.x_increment) + '\n'
        string_representation += row_format_d.format('actual samples', self.actual_samples) + '\n'
        string_representation += row_format_g.format('offset', self.offset) + '\n'
        string_representation += row_format_g.format('gain', self.gain)
        try:
            string_representation += row_format_g.format('wfm length', len(self.wfm))
        except AttributeError:
            pass
        return string_representation

