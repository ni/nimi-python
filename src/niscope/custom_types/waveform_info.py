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
        row_format_s = '{:<20}: {:}'
        string_representation = ''
        try:
            string_representation += row_format_s.format('channel', self.channel)
            string_representation += row_format_d.format('record', self.record)
        except AttributeError:
            pass
        string_representation += row_format_g.format('Absolute X0', self.absolute_initial_x) + '\n'
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


class Waveforms(list):
    def __init__(self, waveforms):
        # waveforms should be a list of lists, where each row is a channel
        self._waveforms = waveforms
        self._lookup = {}
        print('len(waveforms) == {0}'.format(len(waveforms)))
        row_len = len(self._waveforms[0])
        print('len(waveforms[0]) == {0}'.format(len(waveforms[0])))
        i = 0
        for chan_wfm in self._waveforms:
            # All rows should be the same length
            assert row_len == len(chan_wfm), 'Channel rows have different lengths.'
            chan_name = chan_wfm[0].channel
            self._lookup[chan_name] = {}
            j = 0
            for wfm in chan_wfm:
                # All wfm_info in a row should have the same channel name
                assert chan_name == wfm.channel, 'All wfms in channel row should have same channel name'
                self._lookup[wfm.channel][wfm.record] = (i, j)
                j += 1
            i += 1

    def lookup(self, channel, record):
        i, j = self._lookup[channel][record]
        return self._waveforms[i][j]

    def __len__(self):
        return len(self._waveforms)

    def __getitem__(self, index):
        return self._waveforms[index]

    def __repr__(self):
        return '{0}(waveforms={1})'.format(self.__class__.__name__, self._waveforms)

    def __str__(self):
        # all rows have been verified to be the same length
        string_representation = '{0} with size [{1}][{2}]\n'.format(self.__class__.__name__, len(self._waveforms), len(self._waveforms[0]))
        for i in range(len(self._waveforms)):
            for j in range(len(self._waveforms[i])):
                string_representation += 'Record at [{0}][{1}]\n'.format(i, j)
                string_representation += self._waveforms[i][j].__str__() + '\n'


